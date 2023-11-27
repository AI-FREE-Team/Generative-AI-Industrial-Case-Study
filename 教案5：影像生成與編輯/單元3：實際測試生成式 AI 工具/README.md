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
以Midjourney

## 4. 圖片生成圖片（img2img）
以Stable Diffusion Web UI 為例
