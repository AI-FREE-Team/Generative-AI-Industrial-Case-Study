# 單元二、介紹相關生成式 AI 工具

## 1. 前言
在金融業的實務情境中，資料往來上會有大量的實體、電子文件，人員實體互動上也因為金融與民生大幅相關，所以一定會有大量的客服業務需要處置。對於客戶情境的理解，並即時的回覆是金融業中一般職員其中的一項重要任務，然而也因為業務量的繁多，因此多數金融機構無論是在線上網頁中有整理好的QA列表，還是電話詢問的時候會先透夠分流的機制，初步將客戶的需求分派給適合的專員，讓人力資源有最大的使用效益。

## 2. ChatGPT 工具介紹
在本節的討論適用於多數知名的大型語言模型服務，如 [Anthropic Claude 2](https://www.anthropic.com/index/claude-2)、[Meta LLaMa](https://ai.meta.com/llama/)、[Google Bard](https://bard.google.com/chat?hl=zh-TW)或是 [Microsoft Bing](https://www.bing.com/)，不過舉例上就會以ChatGPT背後的GPT4為主。

### 2.1 ChatGPT 網頁服務
目前ChatGPT開放GPT3.5讓大家免費使用，基本上大家只要完成註冊，都可以順利看到以下的畫面。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%882%EF%BC%9A%E8%AA%9E%E9%9F%B3%E7%94%9F%E6%88%90%E5%AE%A2%E6%9C%8D%E6%A9%9F%E5%99%A8%E4%BA%BA/pics/unit2/ChatGPT3.5.png" height="400px">
</div>

若有付費訂閱GPT4（目前訂閱費用每個月600TWD），除了語言模型的邏輯推理能力更強，更能夠處理複雜的任題之外，也涵蓋了許多不同的功能，如：上傳截圖、客製化GPT、使用AI繪圖、加入Plugin，以本教案鎖定金融業的使用情境，比較可能使用到的功能會有上傳截圖與客製化GPT，此部分下一個單元將會有相關示範。

然而，如果需要自行開發一個獨立於ChatGPT網頁元件的客製化機器人（甚至使其具備語音的功能），但是還是想要GPT3.5或是GPT4的大型語言模型負責理解客戶的需求，勢必需要使用OpenAI API。

### 2.2 OpenAI 語言模型 API
如果金融企業想要建置屬於自己的客服機器人，就不太可能是直接在ChatGPT的網頁介面上面直接架設。更可能的建置情境會是付費使用OpenAI語言模型（Language Model）的API，根據[OpenAI網頁的介紹](https://openai.com/pricing)，不同的語言模型所需要的費用也會有所不同。

而OpenAI提供的API服務也不只有語言模型（Language Model），其中也包含了像是影像的生成或是語音的生成服務，下面主要是針對文字的部分進行討論，更多資訊都可以參考[OpenAI為軟體工程師提供的平台](https://platform.openai.com/docs/overview)。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%882%EF%BC%9A%E8%AA%9E%E9%9F%B3%E7%94%9F%E6%88%90%E5%AE%A2%E6%9C%8D%E6%A9%9F%E5%99%A8%E4%BA%BA/pics/unit2/Pic2.OpenAI.API.Dev.Platform.png" height="400px">
</div>

#### 2.2.1 GPT-4 Turbo
能夠接受Context長度（也就是Token數目）為128k，比GPT-4表現更好，輸入（Input）的費用每1000個Token花費0.01USD；而輸出的費用則是每1000個Token花費0.03USD（Note：一個完整的問答包含了輸入和輸出）。
| 模型（Model） | 輸入（Input） | 輸出（Output） |
| :--: | :--: | :--: |
| gpt-4-1106-preview | $0.01/1K tokens | $0.03/1K tokens |
| gpt-4-1106-vision-preview | $0.01/1K tokens | $0.03/1K tokens |

#### 2.2.2 GPT-4
不同模型（Model）因為能夠接受的Token數目不同，因此需要的費用也有所不同，詳見下表。
| 模型（Model） | 輸入（Input） | 輸出（Output） |
| :--: | :--: | :--: |
| gpt-4 | $0.03/1K tokens | $0.06/1K tokens |
| gpt-4-32k | $0.06/1K tokens | $0.12/1K tokens |

#### 2.2.3 GPT-3.5 Turbo
GPT-3.5 Turbo的模型原則上是所需成本最低系列，`gpt-3.5-turbo`能夠接受的Token數目為16K，而`gpt-3.5-turbo-instruct`則是能接受4K的Token數目，費用也有所不同。
| 模型（Model） | 輸入（Input） | 輸出（Output） |
| :--: | :--: | :--: |
| gpt-3.5-turbo-1106 | $0.0010/1K tokens | $0.0020/1K tokens |
| gpt-3.5-turbo-instruct | $0.0015/1K tokens | $0.0020/1K tokens |

#### 2.2.4 微調模型（Fine-tuning models）
如果讀者發現GPT模型在回覆上不夠接近使用情境的話，也能夠準備大量的語料樣本，自行訓練/微調GPT的大型語言模型，然而在嘗試這樣的做法之前，我們通常都會建議先嘗試看看RAG的方式，嘗試以外部資料幫助GPT模型回覆答案。下表羅列GPT-3.5-turbo的費用：
| 模型（Model）| 訓練（Training） | 輸入（Input Usage） | 輸出（Output Usage） |
| :--: | :--: | :--: | :--: |
| gpt-3.5-turbo | $0.0080/1K tokens | $0.0030/1K tokens | 0.0060/1K tokens |

#### 2.2.5 嵌入模型（Embedding model）
在資料科學界，比較不會直接把Embedding model直翻成嵌入模型，在此是為了完整性才這樣做，然而若要建立RAG的回覆模式，首先我們會需要做的事情就是將外部資訊的文本轉換成向量的形式，而這個**轉換**的動作通常就是由Embedding model來執行，下表羅列其費用：
| 模型（Model） | 使用（Usage） |
| :--: | :--: |
| ada v2 | $0.0001/1K tokens |

## 3. OpenAI Whisper 工具介紹
本節介紹的OpenAI Whisper與下一節介紹的Nvidia NeMo都是可以用來生成聲音的工具，不過OpenAI的Whisper是需要花費使用的，詳細的介紹可以參考[此Github連結](https://github.com/openai/whisper#available-models-and-languages)。

### 3.1 多元音色
目前whisper提供了6種不一樣的聲音（Alloy, Echo, Fable, Onyx, Nova, Shimmer），歡迎讀者點擊此連結（即可看到下圖畫面），實際聽聽看不同人選的音色為何。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%882%EF%BC%9A%E8%AA%9E%E9%9F%B3%E7%94%9F%E6%88%90%E5%AE%A2%E6%9C%8D%E6%A9%9F%E5%99%A8%E4%BA%BA/pics/unit2/pic2.whisper_voice.png" height="400px">
</div>

### 3.2 支援語言
而語言的部分則支援了數十種語言，目前一共包含以下這些語言：
```
Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.
```

### 3.3 模型選擇
而模型的選擇上也可以基於硬體的記憶體限制，或是要求的回覆速度與品質，自由選擇，在Github上的專案中也有詳細的列出不同大小的模型對應的數值表現，目前的情況可見下表，通常越大的模型表現越好，但是反應速度和對硬體的要求就會更高一些。

| Size | Parameters | English-only model | Multilingual model | Required VRAM | Relative Speed |
| : -- : | : -- : | : -- : | : -- : | : -- : | : -- : |
| tiny | 39M | `tiny.en` | `tiny` | ~1GB | ~32x |
| base | 74M | `base.en` | `base` | ~1GB | ~16x |
| small | 244M | `small.en` | `base` | ~2GB | ~6x |
| medium | 769M | `medium.en` | `medium` | ~5GB | ~2x |
| large | 1550M | N/A | `large` | ~10GB | 1x |

## 4. Nvidia NeMo 開源程式碼專案介紹
Nvidia NeMo是面對自然語言處理（Natural Language Processing）的開源套件，非常適合想要嘗試建置智能語音助理的開發團隊，只要利用NeMo提供的文字轉語音（Text-to-Speech）API，即可快速建立語音生成的服務。

詳盡的資料可以參考[NeMo在Github的開源專案](https://github.com/NVIDIA/NeMo/tree/main)，在[教學網站](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/stable/starthere/tutorials.html)（下圖）中也將使用情境分成四種領域（Domain），包含：一般（General）、語音辨識（ASR）、自然語言處理（NLP，主要針對純文字的任務）與這個教案著重討論的文字轉語音（TTS）。





## 5. 小節
針對金融領域的業者而言，建議先使用ChatGPT網業服務，感受GPT-3.5與GPT-4的問答能力是否可行；而後再開發專屬客服機器人的時候，再根據使用體驗，決定要使用GPT-3.5系列的API還是GPT-4系列的API，如果發現客服機器人回答還差強人意，則可以考慮利用嵌入（Embedding）模型加入RAG的功能，最後如果還是不行的話，就再考慮微調（Finetune）GPT模型了（如果是GPT-3.5的情境，現在尚未開放GPT-4的微調）！