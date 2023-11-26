# 單元二、介紹相關生成式 AI 工具

## 1. 前言
此單元將展示一系列的生成式AI影像工具。從動態影片到靜態圖像，介紹包括Runway、Pika Labs在內的平台，以及Stable Diffusion、Image Creator等圖像生成工具。最後探討如何利用ChatGPT與DALLE這類整合型工具來增添創作靈感，為藝術設計相關從業人員提供創意發想方向。

## 2. 生成影片的工具
目前AI繪圖除了在影像的生成領域大放異彩外，事實上也有相應的組織正在開發能夠直接利用文字生成影片的生成式AI工具，而目前最廣為人知的服務分別有需要付費訂閱（提供限量試用token）的[Runway](https://runwayml.com/)，以及開源免費的[Pika Labs](https://www.pika.art/)，甚至有耳聞Stability.ai這家開源了Stable Diffusion工具的團隊，也正在開發Stable Video Diffusion工具。

### 2.1 Runway
在 Runway 當中提供了幾種常見的使用情境（可見下圖的**Popular AI Magic Tools**）：Video to Video、Text/Image to Video、Remove Background、Text to Image、Image to Image、Train your own Generator。而其中最為有名的就是 Text/Image to Video。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic0.runway.png" width="600px">
</div>

下圖展示實際使用Image to Video的操作介面，可見右上方有撰寫試用的token數（以秒計），每一次生成一段影片都是以4秒為一階段，如果對於每一階段的成果都很滿意，最多可以針對同一段片段連續生成4個片段，也就是16秒，整體操作上非常直覺，各位讀者只需要要Google的帳戶就可以快速嘗試看看。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic1.runwayui.png" width="600px">
</div>

下表左圖是利用AI繪圖生成的一個Logo視覺意象，而右邊的影片則是利用Runway生成的結果，這邊是使用Runway當中的Motion Brush功能。

| 輸入（AI繪圖結果） | 輸出（Runway輸出結果） |
| :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic1.coolbunny.jpg) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic2.coolbungygif.gif) |

### 2.2 Pika Labs
與Runway不同，Pika Labs則是開源免費的服務，讀者只需要有Discord就可以訂閱Pika Labs的頻道並開始使用相關的功能。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic2.pikalab.png" width="600px">
</div>

讀者進入此連結後，將能夠點選下方的`JOIN BETA`按鈕。接著的操作會因為讀者是否有Discord的帳戶而有些微的不同，然而在完成註冊之後，大家都可以看到像是下面的Pika操作介面。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic2.pikaui.png" width="600px">
</div>

如果要開始利用這個工具生成影片，就要進入左側的`#generate`房間，輸入類似以下的關鍵字（Prompt）即可生成相應的影片。
`/create prompt: a robot is walking in the forest, sunset -ar 16:9 -motion 2`
上述指令中 `-ar` 表示 aspect ration（輸出長寬比）； `-motion` 則與移動的幅度有關，下圖為實際產製影片的過程會看到的畫面，這段過程會是非常動態的，因為可以看到世界各地的人和你在同一個房間輸入各式各樣不一樣的關鍵字（Prompt）。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic3.generatinginaction.png" width="600px">
</div>

而下表則實際展示三個不同的Prompt所生成的影片結果。

| | 範例一 | 範例二 | 範例三 |
| :--: | :--: | :--: | :--: |
| 關鍵字（Prompt）| `a robot is walking in the forest, sunset -ar 16:9 -motion 2` | `a white cat is eating a fish happily, cute cat, giant blue eyes -ar 16:9 -motion 1` | `a school bus is moving on the bridge, aerial view -ar 16:9 -motion 3` | 
| 影片生成結果 | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pika_exp_1.gif) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pika_exp_2.gif) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pika_exp_3.gif) |

Note: 此表展示的gif受限於檔案大小，因此有針對長寬進行調整，原始輸出的mp4檔確實為16:9的影片。

## 3. 生成圖像的工具
在網路上有許多AI繪圖工具，其中最為知名的就是此節會介紹到的Stable Diffusion和Image Creator以及Midjourney。這些工具不外乎都具備文字生成圖片（txt2img）的功能，通常在輸入關鍵字足夠精確的情況下，輸出的品質往往都非常的高。

### 3.1 Stable Diffusion
Stable Diffusion是Stability.ai這家公司所開源出來的服務，因此我們都能夠開源免費的使用這個服務，由於此服務屬於開源專案，因此在網路上可以找到許多延伸的開源應用，在此舉出網路上知名的三個例子。
| | **Fast Stable Diffusion** | **Stable Diffusion Web UI** | **Stable Diffusion Online** |
| :--: |  :--: | :--: | :--: |
| | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic4.faststablediffusion.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic5.stablediffusionwebui.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic6.stablediffusiononline.png) |
| 面向TA | 自己的電腦配備比較沒有那麼好，或是本地端沒有GPU硬體的用戶 | 熟悉程式碼撰寫與環境安裝，並且在本地端有GPU硬體的用戶 | 單純想要在網頁上體驗AI繪圖基礎功能的用戶 |
| 特色 | 只要訂閱Google Colab Pro就可以使用，功能全面 | 進入門檻最高，功能全面 | 無進入門檻，但功能最少 |
| 連結 | [Github Link](https://github.com/TheLastBen/fast-stable-diffusion) | [Github Link](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | [Webpage Link](https://stablediffusionweb.com/) |

若讀者對於AI繪圖感興趣，並且也想要學習可控性最高的AI繪圖工具 - Stable Diffusion，歡迎大家參考我們團隊開設的[AI繪圖課程 - AI繪圖溝通術：搭上AI藝術的魔法列車](https://hahow.in/cr/ai-art-master)。

### 3.2 Image Creator
Image Creator背後的AI模型是DALLE3，此模型具備強大的文字理解能力，能夠很精確的根據我們在關鍵字（Prompt）的文字產生圖像，此服務一開始有提供100個token，若是使用完之後則需要訂閱才可以繼續使用，不過生成的影像在風格上就會比Stable Diffusion與Midjourney還有少一些，讀者可以點擊[此連結](https://www.bing.com/images/create)前往試用。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic7.imagecreator.png" width="600px">
</div>

Note：
* 關鍵字：一個正在繪製都市高樓大廈藍圖的建築設計師，穿著白色襯衫，藍色牛仔褲，手裡拿著筆和尺仔細的計算長度
* 畫面中間是Image Creator根據上方關鍵字生成的四張影像
* 畫面右側則是過去的繪畫記錄

### 3.3 Midjourney
Midjourney同樣也是在Discord的服務，不過一定需要先行訂閱才能夠使用裡面的功能，有興趣操作的讀者歡迎點擊此連結，在登入後就會進入訂閱介面，完成訂閱後即可開始利用此工具進行創作！

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic8.midjourneysub.png" width="600px">
</div>

創作流程與Pika有幾分神似，在Pika需要輸入`create/`關鍵字，不過在Midjourney則是要輸入`imagine/`字樣，下圖為實際的操作介面，同樣可以看到世界各地的人輸入關鍵字創作的過程。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic9.midjourneyui.png" width="600px">
</div>

## 4. 整合型工具：ChatGPT 結合 DALLE
最後一個想要和各位讀者介紹的工具是上述工具中最接近智能助理的存在，在ChatGPT網頁服務中，針對有訂閱的用戶，現階段ChatGPT會主動理解我們的文字需求，如果在其中有提到希望AI能夠幫助我們生成AI繪圖，那麼ChatGPT會自動觸發繪圖機制，並且將我們的文字描述送給DALLE生成精美的圖像，在第三單元我們會有更多關於這方面的操作，在此展示可能的對話情況供讀者參考。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit2/pic10.chatgptdalle.png" width="600px">
</div>