# 單元一、人工智慧概述
## 1. 前言
近來人工智慧（AI）快速發展，舉凡工業智能化的**物件偵測(Object Detection)**、**瑕疵檢測(Anomaly Detection)**，商業領域的**趨勢預測(Trend Prediction)**，到近期浮上檯面的生成式AI，諸多應用如雨後春筍不斷冒出，然而為何AI在短短幾年內間快速成長？主要領域包含哪些項目？生成式AI是什麼？我們又該如何運用生成式AI？這一單元將會提出一個大方向的概念與見解。

## 2. 大數據（Big Data）與人工智慧（AI）
人工智慧的討論其實從20世紀中葉就存在了，而之所以會在2010年之後才真的普及到日常生活當中的各個領域，原因與大數據以及軟硬體的運算更加有效率是有很大的關係的。

### 2.1 大數據的出現（Big Data）
事實上AI科技並非一夕之間快速成長，而是經過數位化時代長時間的資料蒐集，而構建了過去時常耳聞的**大數據（Big Data）**，大數據的存在促使AI能夠從中挖掘出對於任務有幫助的**模式（Pattern）**。

### 2.2 軟硬體效率的提升
除了大數據之外，在硬體面上有電腦運算資源的提升，如適合大量平行處理的GPU出現；在軟體面上也有演算法的精進，這些面向都促使AI的訓練更加迅速且準確，下圖顯示由於資料量（X軸）的充足及演算法之精進（藍色線）促使更好的表現（Y軸）結果。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%881%EF%BC%9A%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%9F%BA%E7%A4%8E/pics/unit1/Pic1.%E8%B3%87%E6%96%99%E9%87%8F%E8%88%87%E6%BC%94%E7%AE%97%E6%B3%95%E5%B0%8D%E6%96%BC%E6%A8%A1%E5%9E%8B%E8%A1%A8%E7%8F%BE%E4%B9%8B%E5%BD%B1%E9%9F%BF_v3.png" height="500px">
</div>

### 2.3 人工智慧（AI）
在檯面上，我們常常會聽到深度學習（Deep Learning）與機器學習（Machine Learning），其實這兩者都屬於人工智慧（AI）的一部份，這兩者都能夠幫助人類完成部分重複性高的日常任務，下面一節，我們就和大家介紹人工智慧（AI）現階段的四大領域。

## 3. 人工智慧（AI）的四個學習方式
在2020年之前，如果我們想要劃分人工智慧，多數的資料科學家可能會提供三個領域，包含：監督式學習、非監督式學習、強化學習；而我們近來熟悉的GPT等生成式AI服務，並不能直接單用一種學習方法就達到現在我們可以體驗到/看到的表現能力，它其實是使用了數個學習方法才有這樣的表現，在此節我們也會將這樣的整合學習法加入討論。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%881%EF%BC%9A%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%9F%BA%E7%A4%8E/pics/unit1/Pic2.%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E4%B8%BB%E8%A6%81%E6%96%B9%E6%B3%95_v2.png" height="500px">
</div>

### 3.1 監督式學習（Supervised Learning）
監督式學習利用大量具有標註之資料，訓練模型之輸出可相近於其標註（為任務驅動，Task-Oriented），以物件判別為例：當我想要判別圖片是否為貓咪，我需要大量標註「是貓咪」與「不是貓咪」的圖片進行訓練，並對模型進行訓練，此為監督式學習。

### 3.2 非監督式學習（Unsupervised Learning）
非監督式學習與監督式學習相反，其使用未標註之資料進行學習，而模型的目標為探索資料中的線索與特徵（數據驅動，Data-Driven），例如：對於眾多資料進行分群（Cluster）即為非監督式學習；

### 3.3 強化學習（Reinforcement Learning）
強化式學習強調於讓AI與外界透過獎懲機制進行互動式學習（從錯誤中學習），例如：透過廣告喜好與否與用戶互動，進而訓練模型將來應該推薦何種吸引該用戶的廣告。

### 3.4 整合學習（Integration Learning）
通常更加進階的任務當中，就會需要整合多元的訓練方式，像是我們熟知的GPT-3.5即為此例，資料科學家們需要整合使用上述三種基礎學習法（詳見下圖，圖中的RAG將會留到單元3進行介紹）才能夠取得適用於特定場景的ChatGPT智能助理，而這還只是文字類的生成式AI工具，其它還有像是圖片甚至是音訊的生成式AI工具也都會有其專屬的整合訓練方法。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%881%EF%BC%9A%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%9F%BA%E7%A4%8E/pics/unit1/Pic6.ChatGPT%E8%A8%93%E7%B7%B4%E6%96%B9%E5%BC%8F_v2.png" height="500px">
</div>

## 4. 預測型 AI 的三大應用 
目前大家對於AI的學習方法應該有個初步的理解了；從應用面來看，其實AI就分成兩大部分：預測型AI（Predictive AI）與生成式AI（Generative AI），而我們在過去十年間常見的AI應用全部都是屬於預測型AI的範疇。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%881%EF%BC%9A%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%9F%BA%E7%A4%8E/pics/unit1/Pic3.%E9%A0%90%E6%B8%AC%E5%9E%8BAI%E4%B8%89%E5%A4%A7%E6%87%89%E7%94%A8.png" height="500px">
</div>

#### 4.1 電腦視覺
電腦視覺主要處理的資料類型通常會是影像，包含了：黑白照片（術語是灰階影像，Grayscale Image）、彩色影像（RGB）、高光譜影像（Hyper-spectral）。拿到了這些資料之後，電腦視覺領域的資料科學家們時常針對不同的任務開發相應的神經網路模型，常見的主流任務有：影像分類（Image Classification）、物件偵測（Object Detection）、影像切割（Image Segmentation）、超解析度成像（Super Resolution）等等。

#### 4.2 自然語言處理
自然語言處理常見的資料即為我們人類日常生活中交換訊息會使用到的文字、聲音有關。常見的任務包含了專有名詞辨別（Name Entity Recognition）、評論分析（Review Analysis）、語音辨識（Automatic Speech Recognition）。

#### 4.3 時間序列處理
時間序列的部份可以從名字推斷，通常處理的資料在時間域上包含了重要的訊息，資料的次序（Order）是重要的，像是自然語言處理的文字和聲音在廣義而言可以算是時間序列的一部份，不過在時間序列上，更典型的應用通常會有：股價預測、房價分析、天氣預報等。

### 5. 生成式 AI 的三大應用
生成式AI透過大量數據的學習，具備能夠生成高品質的創新內容的能力，包含：圖片、文本、音訊的生成皆屬於生成式AI之範疇；更多相關的工具，我們將會在下一個單元，以及後續五個教案當中陸續向各位讀者介紹。

## 6. 未來三年的 AI 發展
在此我們引用著名的資料科學家 - 吳恩達（Andrew Ng）老師在 [Opportunities in AI](https://www.youtube.com/watch?v=5p248yoa3oE) 的演講中使用的投影片，AI在市場上的發展，在未來的三年內，還是會由預測型AI所主導，其市值成長幅度約為2倍；而生成式AI的應用將會以3倍的速度，更快地拓展到各個產業應用當中。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%881%EF%BC%9A%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%9F%BA%E7%A4%8E/pics/unit1/Pic4.%E6%9C%AA%E4%BE%863%E5%B9%B4%E7%9A%84AI%E7%99%BC%E5%B1%95.png" height="500px">
</div>

## （Optional）補充知識點：GPT 是如何學習的
生成式AI在文字上的應用最廣為熟知的就是ChatGPT，而事實上ChatGPT是由Transformer一路精進為GPT（Generative Pre-trained Transformer）系列模型後，才微調（Finetune）而來的大型語言模型（Large Language Model, LLM）。

在大型語言模型中，通常藉由自監督式學習（Self-Supervised Learning，為一種介於特化的監督式學習方法）節省大量標註資料的時間成本，透過長時間大量文本資料的訓練後，GPT模型將具有填空或接龍之能力。

舉例而言，若我收集到文本資料為「AI . FREE Team！」，則訓練資料如下圖所示，藉此透過大量文本之學習模型及可能學會對於文字的理解與應對!

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%881%EF%BC%9A%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%9F%BA%E7%A4%8E/pics/unit1/Pic5.GPT%E9%80%8F%E9%81%8E%E6%96%87%E6%9C%AC%E5%AD%B8%E7%BF%92_v5.png" height="500px">
</div>