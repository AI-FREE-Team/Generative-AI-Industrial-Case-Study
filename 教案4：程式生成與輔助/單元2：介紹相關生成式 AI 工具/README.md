# 單元二、相關生成式 AI 工具

## 1. 前言
隨著生成式AI的興起，現今市面上出現了多款適用於程式生成及輔助的工具或套件，本單元將一一介紹這些工具如輔助軟體工程師開發程式碼，並學習如何透過工具來使程式開發者生產力提高，並且一併介紹到下一單元開發網頁預計會使用到的軟體套件：NeMo與Streamlit。

## 2. ChatGPT Code Interpreter### **（目前在ChatGPT介面中已更名為 ”Advanced data analysis” ）**
目前Code Interpreter 是一個針對有訂閱ChatGPT Plus用戶才能使用的功能。在進行傳統的數據分析工作時，往往要透過許多數據分析工具及套件，且需具備一定的撰寫程式能力，這也造就了一個相對較高的技術門檻。現在Code Interpreter的出現提供了一個創新的解決方案，現在用戶僅需使用自然語言就能實現他們的分析想法並在用戶界面上展示分析結果。這表示即使是那些沒有程式撰寫經驗的人也能夠透過詢問ChatGPT來處理數據、進行分析並解釋結果。

### 2.1 如何啟用 ChatGPT Code Interpreter ?
請先確認已經訂閱 ChatGPT Plus，點擊「Settings」的選項，將上圖紅框的選項打開。完成以上步驟後即可開始使用Code Interpreter（Advanced data analysis）的功能。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/%E5%95%9F%E7%94%A8GPT.png" width="600px">
</div>

### 2.2 如何使用 ChatGPT Code Interpreter（Advanced data analysis）？
目前版本的Code Interpreter已經不需要再特別選擇就可以直接使用，只需要點擊圖片中箭頭所指的地方後將你想分析的檔案上傳，ChatGPT辨別出需要進行資料分析時，就會自動啟用Code Interpreter的功能。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/%E4%BD%BF%E7%94%A8GPT.png" width="600px">
</div>

### 2.3 示範數據分析
這裡採用公開資料集[Iris dataset](https://www.kaggle.com/datasets/vikrishnan/iris-dataset)來進行示範，我們可以利用對話的方式直接請GPT幫我們繪製統計圖表。
| 對話 | 生成圖表一 | 生成圖表二 |
| :--: | :--: | :--: | 
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/%E7%A4%BA%E7%AF%84GPT%E6%93%8D%E4%BD%9C.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/GPT%E5%9C%96%E8%A1%A8%E4%B8%80.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/GPT%E5%9C%96%E8%A1%A8%E4%BA%8C.png) |

## 3. Github Copilot
**GitHub Copilot**是GitHub和OpenAI合作開發的程式撰寫輔助工具，當你在撰寫程式時會依照你的程式上下文給你相對應的建議。
* 支持多數的主流程式語言：Python、JavaScript、TypeScript、Ruby 和 Go等語言。
* 主要在Visual Studio Code上進行輔助撰寫。
* 費用：每月10美金或是每年100美金。開源貢獻者或學生可以申請免費方案。

### 3.1 示範一
按下`ctrl+I`能夠直接與GitHub Copilot說明撰寫程式的要求。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/copilot%E7%A4%BA%E7%AF%84%E4%B8%80.png" width="600px">
</div>

### 3.2 示範二
直接輸入需求後等候GitHub Copilot進行撰寫，按下Accept即採用GitHub Copilot所撰寫之程式碼。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/copilot%E7%A4%BA%E7%AF%84%E4%B8%89.png" width="600px">
</div>

### 3.3 示範三
若非從頭開始撰寫程式，也可以透過註解的方式告知GitHub Copilot你所想完成的事情，只需按下tab鍵就會採用灰色部分程式碼，換行會持續出現提示，直到完成該指令。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/copilot%E7%A4%BA%E7%AF%84%E4%B8%89.png" width="600px">
</div>

## 4. Nvidia NeMo 
NeMo是Nvidia推出的開源NLP工具，包含許多好用的語音識別與自然語言處理 API。這個開源套件讓我們距離人手一個智能助手的目標更加接近，它不僅能夠聽懂你說什麼，還能跟你聊天，甚至幫你寫詩！而NeMo擅長的事情，目前主要包含 3 個面向的 Toolkit：

1. ASR（Automatic Speech Recognition）：這是一種語音識別技術，能夠將我們口語的內容轉為文字。較常見的應用像是語音助手或語音輸入服務。
2. TTS（Text-to-Speech）：它將文字資料轉為聽起來像人說出來的語言，使機器能夠“說話”。我們團隊也曾經製作過太魯閣族的 TTS，並且使用此技術重現耆老的聲音
3. NLP（Natural Language Processing）：包含了各式各樣的文字處理功能，從翻譯、情感分析、資訊提取到自然語言理解，讓電腦能夠解釋和生成人類語言，以便更自然地與人類互動。

## 5. Python 套件: Streamlit
Streamlit是一個開源的Python Package，它讓數據科學家和開發者能夠快速創建和分享數據應用，呈現一個類似網頁的概念。

### 5.1 優點
- **簡潔性**: Streamlit的設計哲學是簡潔性，它允許開發者用極少的程式碼創建應用。
- **即時反饋**: 每次保存文件時，應用會自動更新，這為開發者提供即時反饋。
- **廣泛的套件庫**: Streamlit包含豐富的套件，如圖表、地圖和互動式素材。

### 5.2 安裝方法
1. 安裝指令: 使用pip安裝Streamlit非常簡單。
`pip install streamlit`
2. 創建第一個應用：只需寫幾行程式碼，就可以建立一個能夠運行的應用。
```python
import streamlit as st
st.write("Hello, world!")
```

### 5.3 使用情境
- **數據可視化**: Streamlit擅長將數據分析結果以視覺化的形式呈現。
- **機器學習模型展示**: 快速建立和分享機器學習模型，並提供使用者快速進行測試。