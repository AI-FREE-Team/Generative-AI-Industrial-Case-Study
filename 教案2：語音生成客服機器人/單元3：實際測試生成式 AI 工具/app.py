import os
import whisper
import streamlit as st
from pydub import AudioSegment
import warnings
from st_audiorec import st_audiorec
from openai import OpenAI

# 忽略特定类型的警告
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Whisper based ASR",
    page_icon="musical_note",
    layout="wide",
    initial_sidebar_state="auto",
)

audio_tags = {'comments': 'Converted using pydub!'}

upload_path = "uploads/"
download_path = "downloads/"
transcript_path = "transcripts/"

# @st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def to_mp3(audio_file, output_audio_file, upload_path, download_path):
    ## Converting Different Audio Formats To MP3 ##
    if audio_file.split('.')[-1].lower()=="wav":
        audio_data = AudioSegment.from_wav(os.path.join(upload_path,audio_file))
        audio_data.export(os.path.join(download_path,output_audio_file), format="mp3", tags=audio_tags)

    elif audio_file.split('.')[-1].lower()=="mp3":
        audio_data = AudioSegment.from_mp3(os.path.join(upload_path,audio_file))
        audio_data.export(os.path.join(download_path,output_audio_file), format="mp3", tags=audio_tags)
    return output_audio_file

# @st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def process_audio(filename, model_type):
    model = whisper.load_model(model_type)
    result = model.transcribe(filename)
    return result["text"]

def whisper_infer(wav_path):
    transcript = process_audio(wav_path , 'base')
    return transcript

st.title("🗣Streamlit ASR + GPT + TTS ✨")
st.info('✨ Supports all popular audio formats - WAV, MP3, MP4, OGG, WMA, AAC, FLAC, FLV 😉')
st.info('請輸入音檔或是直接說話')

uploaded_file = st.file_uploader("Upload audio file", type=["wav","mp3","ogg","wma","aac","flac","mp4","flv"])
radio_bytes = st_audiorec()

audio_file = None
transcript = None
response = None

if uploaded_file is not None:
    audio_bytes = uploaded_file.read()
    with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
        f.write((uploaded_file).getbuffer())
    with st.spinner(f"Processing Audio ... 💫"):
        output_audio_file = uploaded_file.name.split('.')[0] + '.mp3'
        audio_file = uploaded_file.name
        output_audio_file = to_mp3(audio_file, output_audio_file, upload_path, download_path)
        audio_file = open(os.path.join(download_path,output_audio_file), 'rb')
        audio_bytes = audio_file.read()
    st.markdown("---")
    st.markdown("Feel free to play your uploaded audio file 🎼")
    st.audio(audio_bytes)
    wav_path = str(os.path.abspath(os.path.join(download_path,output_audio_file)))
    if st.button("Generate Transcript"):
        with st.spinner(f"Generating Transcript... 💫"):
            st.write("Transcription Result:")
            transcript = whisper_infer(wav_path)
            st.write(transcript)
            st.success('✅ Recoginize Successful !!')

if radio_bytes is not None:
    wav_name = 'test.wav'
    with open(os.path.join(upload_path,wav_name),"wb") as f:
        f.write(radio_bytes)
    with st.spinner(f"Processing Audio ... 💫"):
        output_audio_file = wav_name.split('.')[0] + '.mp3'
        output_audio_file = to_mp3(wav_name, output_audio_file, upload_path, download_path)
        audio_file = open(os.path.join(download_path,output_audio_file), 'rb')
        audio_bytes = audio_file.read()
    wav_path = str(os.path.abspath(os.path.join(download_path,output_audio_file)))
    if st.button("Generate Radio Transcript"):
        with st.spinner(f"Generating Transcript... 💫"):
            st.write("Transcription Result:")
            transcript = whisper_infer(wav_path)
            st.write(transcript)
            st.success('✅ Recoginize Successful !!')

if transcript is not None:
    client = OpenAI(
        api_key = '請改成自己的OpenAI API KEY'
    )

    # question = '台幣怎麼換成美元'
    entity = '證件準備、選擇銀行與帳戶類型、填寫申請表格、提交申請、等待審核、存款、設定網路銀行與行動銀行'

    qqq = f"""
    你是一個專業的金融相關的人員\
    請你完成回覆金融相關的知識 \
    以下是提問的問題\n {transcript}\
    請回答上述問題\
    請幫我把專有名詞抓出來 回覆時請換行 例如:{entity} 再額外換行\
    """
    with st.spinner(f"Generate Response... 💫"):
        completion = client.completions.create(
            model="text-davinci-003",
            prompt=qqq,
            max_tokens=512,
            temperature=0.5,
            )

        response = completion.choices[0].text
        with st.spinner(f"銀行機器人專業回覆"):
            st.write(response)
    with st.spinner(f"Generate Speech... 💫"):
        speech_serve = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=response
        )
        print(speech_serve)
        speech_serve.stream_to_file(os.path.join(download_path , 'speech.mp3'))
        tts_file = open(os.path.join(download_path,'speech.mp3'), 'rb')
        tts_bytes = tts_file.read()
    st.audio(tts_bytes)
    st.success('✅ TTS Output !')