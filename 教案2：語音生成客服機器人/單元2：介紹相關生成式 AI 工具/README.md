# 單元二、介紹相關生成式 AI 工具

## 1. 前言
在金融業的實務情境中，資料往來上會有大量的實體、電子文件，人員實體互動上也因為金融與民生大幅相關，所以一定會有大量的客服業務需要處置。對於客戶情境的理解，並即時的回覆是金融業中一般職員其中的一項重要任務，然而也因為業務量的繁多，因此多數金融機構無論是在線上網頁中有整理好的QA列表，還是電話詢問的時候會先透夠分流的機制，初步將客戶的需求分派給適合的專員，讓人力資源有最大的使用效益。

## 2. ChatGPT 工具介紹
在本節的討論適用於多數知名的大型語言模型服務，如 [Anthropic Claude 2](https://www.anthropic.com/index/claude-2)、[Meta LLaMa](https://ai.meta.com/llama/)、[Google Bard](https://bard.google.com/chat?hl=zh-TW)或是 (Microsoft Bing)[https://www.bing.com/]，不過舉例上就會以ChatGPT背後的GPT4為主。

### 2.1 ChatGPT 網頁服務
目前ChatGPT開放GPT3.5讓大家免費使用，基本上大家只要完成註冊，都可以順利看到以下的畫面。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%882%EF%BC%9A%E8%AA%9E%E9%9F%B3%E7%94%9F%E6%88%90%E5%AE%A2%E6%9C%8D%E6%A9%9F%E5%99%A8%E4%BA%BA/pics/unit2/ChatGPT3.5.png" height="250px">
</div>

若有付費訂閱GPT4（目前訂閱費用每個月600TWD），除了語言模型的邏輯推理能力更強，更能夠處理複雜的任題之外，也涵蓋了許多不同的功能，如：上傳截圖、客製化GPT、使用AI繪圖、加入Plugin，以本教案鎖定金融業的使用情境，比較可能使用到的功能會有上傳截圖與客製化GPT，此部分下一個單元將會有相關示範。

然而，如果需要自行開發一個獨立於ChatGPT網頁元件的客製化機器人（甚至使其具備語音的功能），但是還是想要GPT3.5或是GPT4的大型語言模型負責理解客戶的需求，勢必需要使用OpenAI API。

### 2.2 OpenAI 語言模型 API
如果金融企業想要建置屬於自己的客服機器人，就不太可能是直接在ChatGPT的網頁介面上面直接架設。更可能的建置情境會是付費使用OpenAI語言模型（Language Model）的API，根據[OpenAI網頁的介紹](https://openai.com/pricing)，不同的語言模型所需要的費用也會有所不同。

#### 2.2.1 GPT-4 Turbo
能夠接受Context長度為128k，比GPT-4表現更好，輸入（Input）的費用每1000個Token花費0.01USD；而輸出的費用則是每1000個Token花費0.03USD。
| Model | Input | Output |
| :--: | :--: | :--: |
| gpt-4-1106-preview | $0.01/1K tokens | $0.03/1K tokens |
| gpt-4-1106-vision-preview | $0.01/1K tokens | $0.03/1K tokens |

#### 2.2.2 GPT-4

#### 2.2.3 GPT-3.5 Turbo

## 3. OpenAI Whisper 工具介紹

## 4. Nvidia NeMo 開源程式碼專案介紹