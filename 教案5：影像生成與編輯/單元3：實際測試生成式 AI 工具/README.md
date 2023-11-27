# 單元三、實際測試生成式 AI 工具

## 1. 前言
在平面設計領域中，設計是無所不在的，有的時候靈光乍現就需要趕快把靈感具象化以免忘記；有的時後是任務明確，需要好好的微調畫面色溫；有的時候則是單純的需要激發靈感，進行大量的創意思考。

在單元三中將實際應用生成式AI工具生成影像，並且實際展示三種情境，利用日常對話生成圖像的過程（ChatGPT結合DALLE），到Midjourney的文字轉圖片功能，以及Stable Diffusion Web UI實現圖片轉換，學習如何在圖像生成中的各式應用可能性。

## 2. 日常對話生成圖像
透過日常對話生成圖像，這樣的情境可以實現，說明了AI繪圖工具已經不只是普通的被使用的工具了，它在某種程度上已經升格為一個具備繪畫能力AI智能助理了。我們過去都是請專業的平面設計師，針對我們的需求進行創作；而在生成式AI出現的現在，同時搭配上ChatGPT的語言理解能力與DALLE的AI作畫能力，就可能逼近過去我們與設計師合作的過程，只是整體交流與創作的時間會大幅加速！

在這邊我們以本團隊過去開發的一個AI專案為例，我們當時想要幫這個專案繪製一個平面彩色的主視覺，希望展示出「在未來，每個家庭都能夠透過手機等3C設備拍攝兒童的書寫文字，進而察覺潛在的遲緩兒童病徵」，因此下方的對話，邀請各位讀者花一些時間，觀察這整個流程，並嘗試歸納出其具備的優勢。

| 對話一 | 對話二 | 對話三 | 對話四 |
| :--: | :--: | :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/step1.jpg) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/step2.jpg) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/step3.jpg) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/step4.jpg) |

| 對話五 | 對話六 | 結果 |
| :--: | :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/step5.jpg) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/step6.jpg) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/step7.jpg) |

這整個過程展示了此流程的三大優勢：
1. 能夠直接以我們熟悉的日常對話指示AI進行作畫
2. ChatGPT具備記憶的能力，所以很多話不用重新說明
3. 具備某種程度的可解釋性，AI會適時的解釋並分析自己的繪畫成果

## 3. 文字生成圖片（txt2img）
事實上文字生成圖片是最為基礎的AI繪圖技巧，多數的AI繪圖工具都提供這樣的服務，像是Midjourney、Stable Diffusion或是Image Creator都是如此。雖然隨著AI繪圖內部使用的AI模型的進步，漸漸地我們可以使用越來越接近自然語言的方式和AI繪圖工具對話，但如果我們有按照一定框架的行為撰寫關鍵字（Prompt），那麼整體影像的生成結果就容易接近我們的想像。

根據我們的經驗，撰寫關鍵字（Prompt）如果可以考量四個面向，包含：整體風格、視覺主體與客體的描述、攝影元素、補充效果，則通常生出來的圖片都會有一定品質，一些可以使用的字眼與舉例請參考下圖。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/pic1.promptframework.png" width="600px">
</div>

### 以聖誕節為例
假設準備要聖誕節了，因此我們打算製作相關的平面宣傳圖像，或許此時就能夠使用AI繪圖工具協助進行創作。我們參考上圖的關鍵字撰寫框架，並且設計出以下的關鍵字，並且嘗試Image Creator、Stable Diffusion Web UI這兩個AI繪圖工具，在Image Creator可以直接輸入中文，而在Stable Diffusion Web UI當中則會需要先翻譯成英文。
* 關鍵字：
    * 中文：`動畫風格，有一位和藹的聖誕老公公正在送一個紅色的禮物盒給一個褐色頭髮藍色眼睛的小男孩，它們兩個站在一棵有許多裝飾的聖誕樹前，讓畫面對焦在兩人，並景希望有景深的效果，高畫質`
    * 英文：`Animation style, there is an amiable Santa Claus is delivering a red gift box to a little boy with brown hair and blue eyes, the two of them are standing in front of a Christmas tree with a lot of decorations, let the picture focus on the two of them, and the scene hope to have the effect of depth of field, high quality`

| Image Creator 的生成結果 | Stable Diffusion 的生成結果 |
| :--: | :--: |
| ![]() | ![]() |
| 備註：Image Creator一次會生成四張影像 | 備註：我們可以自由調整使用的AI模型，在此使用[DreamShaper](https://civitai.com/models/4384?modelVersionId=128713) |

## 4. 圖片生成圖片（img2img）
或許我們可以利用文字生成圖片，或是日常對話生成圖片就完成大部分的創作了，但有時候會遇到你覺得特定影像風格很接近了，希望可以同樣以該風格進行創作與微調，這時候可能就可以利用圖生圖的方式達到這個目的。

下圖展現Stable Diffusion Web UI實際的圖生圖操作介面：

實際輸入與輸出也可以參考下面的這個表格，在這邊同樣使用DreamShaper這個AI模型，過程其實也含有許多的參數可以設定與調整，如果讀者對於這方面感到好奇，也歡迎參考我們團隊開設的[AI繪圖課程](https://hahow.in/cr/ai-art-master)。

| 參考圖像 | 生成結果 |
| :--: | :--: |
| ![]() | ![]() |