# 單元二、介紹相關生成式 AI 工具

## 1. 前言
在單元二介紹生成式AI工具如何應用於決策與分析的各個環節。雖然在教案一裡面提到的文字類型生成式AI工具（如：Bing Chat, Google Bard）都可以做到這些事情，不過這裡會將重點放在ChatGPT的使用上，從解讀數據到模擬不同部門員工的角色；同時也會介紹XMind心智圖工具，我們會在下一單元實際操作的時候實際與ChatGPT整合起來，呈現視覺化的心智圖，進一步拓展思維方式與優化決策的流程。

## 2. ChatGPT 工具介紹
若讀者是從第一個教案依次閱覽到此教案，應該對於ChatGPT的服務不會感到陌生；不過如果是直接進入到此教案的讀者，以下是簡短的GPT服務介紹，ChatGPT是OpneAI打造的文字類型生成式AI工具，由於內部的參數量非常的龐大（以GPT-3.5而言，它就有1750億個參數，正常來說只要有100億個參數就可以進行較為困難的邏輯思維能力），因此能夠協助人類撰寫文案等。

OpenAI提供了不同使用者不同的服務方式，如果是面向一般大眾，則提供了ChatGPT網頁服務，在這網頁服務當中又分成有無訂閱之分的GPT-3.5與GPT-4；而如果是面向軟體工程師，則提供用多少付多少的OpenAI API服務，可以直接將GPT的服務建立在自己的軟體上，我們在這單元的討論會以ChatGPT網頁服務的操作為主。

### 2.1 利用 Code Interpretor 從數據中獲得見解
Code Interpretor現在已經改名成Advanced data analysis，各位讀者可以參考[教案四的單元二](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/tree/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/%E5%96%AE%E5%85%832%EF%BC%9A%E4%BB%8B%E7%B4%B9%E7%9B%B8%E9%97%9C%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%B7%A5%E5%85%B7)，有完整的啟用流程，主要是要和讀者告知，在這個環節會先需要訂閱GPT服務，才能在GPT-4當中使用到這個功能。

#### 不需要具備軟體開發能力也能數據分析
Code Interpretor帶來的改變是巨大的，過往我們如果要從原始資料（Raw Data）獲取一些洞見（Insight），往往會需要精熟Excel或是熟悉資料科學套件（如：Numpy, Pandas, Matplotlib）的軟體工程師幫忙，即使完成了分析，最後或許在決策報告上面也會需要附上較為美觀的分析圖表；而這部分又需要花費一定的功夫做圖。
而這些重複性高且具備一定技術門檻的事情現在都可以透過自然語言（也就是普通的對話）就能夠請ChatGPT直接幫我們繪製出來。

下表呈現我們請GPT繪製的統計圖表，詳細的對話內容請參考[教案四的單元二](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/tree/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/%E5%96%AE%E5%85%832%EF%BC%9A%E4%BB%8B%E7%B4%B9%E7%9B%B8%E9%97%9C%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%B7%A5%E5%85%B7)。

| GPT產出圖表1 | GPT產出圖表2|
| :--: | :--: |
|![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/GPT%E5%9C%96%E8%A1%A8%E4%B8%80.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit2/GPT%E5%9C%96%E8%A1%A8%E4%BA%8C.png) |

### 2.2 請 ChatGPT 扮演不同部門不同層級的職員
我們曾經在[教案一單元三](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/tree/main/%E6%95%99%E6%A1%881%EF%BC%9A%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%9F%BA%E7%A4%8E/%E5%96%AE%E5%85%833%EF%BC%9A%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8%E9%A0%88%E7%9F%A5)提及「角色扮演」，這是和GPT對話的時候能夠大幅幫助GPT進入狀況的關鍵字（Prompt）技巧。

因此面對不同的場景，如果你需要相關的文字建議，以下的起手式請各位讀者務必要記得：
#### 請GPT扮演一個角色：軟體外包專案
```
GPT您好，請你扮演一個資深的技術主管，我是XXX專案的PM，目前手邊有一個軟體專案預計要外包，我希望你能協助我思考相關文件的架構 ...
```

#### 請GPT扮演多個角色：行銷策略規劃與執行
```
GPT您好，我目前是XXX產品線的產品經理，我需要將剛剛的會議記錄轉化成不同部門的行動方針，請你參考虛線以內的會議紀錄，並根據最下方的回覆模板回答

----------（虛線開始）----------
...
會議記錄
...
----------（虛線結束）----------

#軟體部門
* To-Do 1：
* To-Do 2：
* To-Do 3：
...

#行銷部門
* To-Do 1：
* To-Do 2：
* To-Do 3：
...

#行政部門
* To-Do 1：
* To-Do 2：
* To-Do 3：
...
```

在這邊提到的關鍵字模板都一定可以再根據讀者自身的情境優化，例如加入更多專案背景資訊、加入RAG服務直接導入外部知識、使用Emotion Prompt提高回覆水準等。

## 3. XMind 心智圖工具
在團隊會議中，心智圖往往是最常出現的圖表之一，市面上也有許多的心智圖工具，我們在本教案使用[XMind](https://xmind.app/)這個免費的服務，並嘗試整合GPT輸出的內容與XMind，目標是讓GPT輸出的內容可以直接的請XMind繪製出心智圖。

若想要一起在下個單元與我們實際操作，歡迎讀者先至XMind官方網站下載其APP。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit2/XMIND.png" width="600px">
</div>