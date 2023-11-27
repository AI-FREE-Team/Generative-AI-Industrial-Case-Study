# 單元四、微調生成式 AI 工具輸出結果

## 1. 前言
在設計的過程中，確實有的時候會遇到AI繪圖生成的結果距離目標還有一點點差異，因此在這單元，我們將探討如何利用生成式AI工具，微調生成式AI工具的輸出結果，學習如何讓ChatGPT調整關鍵字來改善生成結果，並使用遮罩技術（Inpainting）進行影像的細微調整，以達到能夠製作出精準視覺意象的情境。

## 2. 請 ChatGPT 根據目前的結果修正關鍵字

### 2.1 情境描述
我們在第三個單元，曾經利用以下的關鍵字（Prompt）生成下方具備聖誕氛圍的影像結果。

關鍵字：Animation style, there is an amiable Santa Claus is delivering a red gift box to a little boy with brown hair and blue eyes, the two of them are standing in front of a Christmas tree with a lot of decorations, let the picture focus on the two of them, and the scene hope to have the effect of depth of field, high quality
（中文翻譯：動畫風格，有一位和藹的聖誕老公公正在送一個紅色的禮物盒給一個褐色頭髮藍色眼睛的小男孩，它們兩個站在一棵有許多裝飾的聖誕樹前，讓畫面對焦在兩人，並景希望有景深的效果，高畫質）

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit3/pic4.img2imgoutput.png" width="600px">
</div>

如果我的客戶希望我能夠調整畫面中的男孩姿勢，例如：希望男孩面向鏡頭，那麼我們該如何利用生成式AI工具

### 2.2 使用ChatGPT調整關鍵字（Prompt）
在付費訂閱ChatGPT網頁服務之後，原則上讀者都可以上傳圖片，並根據圖片的內容請GPT進行討論，舉例而言，我可以上傳註記好的影像，並且提出需求，請ChatGPT幫我修正關鍵字（Prompt）。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/yellowbox.png" width="600px">
</div>

再將ChatGPT修正的結果丟入AI繪圖工具（如：Stable Diffusion）繪製，即可得以下不同的成果。
| 成果一 | 成果二 | 成果三 | 成果四 |
| :--: | :--: | :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_1.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_2.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_3.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_4.png) |

Note：使用圖生圖的形式，重繪幅度設為0.5。
雖然並非每一張影像都有辦法直接的達到目標成果，不過利用AI繪圖生圖迅速的優勢，還是有機會能夠取得相符期待的成果，如：上表的成果一。

## 3. 利用遮罩（Inpaint）微調影像生成結果
不過上面提到的方法會動到整張影像，另一個比較進階的作法就是直接指定特定的區域修正，而這樣的技巧被稱為「遮罩」法，在Stable Diffusion Web UI當中的圖生圖就有這樣子的功能，下圖展示Stable Diffusion Web UI的操作介面。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/inpaintUI.png" width="600px">
</div>

一併也展示利用遮罩所生成的四張影像。
| 成果一 | 成果二 | 成果三 | 成果四 |
| :--: | :--: | :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_5.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_6.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_7.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_8.png) |

可以發現其中有兩張影像很明顯是AI繪圖會錯意了，不過剩下的兩張就有比較完整的呈現出我們所希望的視覺意象了。這個過程可以確保遮罩以外的區域不會變動，不過也不保證遮罩內的區域就一定可以馬上就試成功，整體流程還是需要一定的實驗與調整。因此也有許多繪師，繪將成果直接繪入Photoshop的編輯軟體做細部調整。

### 補充情境：替換指定人物
如果希望更進一步控制人的肢體架構不變，那麼就可以結合遮罩與進階的ControlNet技巧，雖然不能夠調整人物面向的位置，但是可以替換成不一樣的人物，因此也能夠滿足部分的使用情境。

| 成果一 | 成果二 | 成果三 | 成果四 |
| :--: | :--: | :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_9.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_10.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_11.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%885%EF%BC%9A%E5%BD%B1%E5%83%8F%E7%94%9F%E6%88%90%E8%88%87%E7%B7%A8%E8%BC%AF/pics/unit4/result_12.png) |