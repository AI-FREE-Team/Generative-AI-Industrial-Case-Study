# 單元一、業界實務應用情境

## 1. 前言
在此單元中，我們將深入探討生成式AI在教育、新聞出版和營銷領域的實際運用，學習如何利用這項技術來將文本內容生成和摘要。從教育界的論文撰寫到新聞媒體的文章生產，再到營銷與廣告領域的創意文案，說明這些技術如何提升工作效率和創意質量。

## 2. 教育界使用情境
在教學界當中，有非常多與文字相關的應用情境，包含：不同科目教材的設計、學界論文的研讀，甚至是自己要根據過往研究內容撰寫期刊內容，以下討論ChatGPT等生成式AI工具可能為這些面向帶來的可能改善。

### 2.1 教材設計與使用
1. **確認架構完整性**：如果是要撰寫科目教材，那麼身為教材的設計者就會需要安排完整架構的內容，這部分就可以與GPT共同討論，確認是架構是否完整，有沒有遺漏或是重疊的部分。
2. **指定科目教材助教**：直接將教材內容以RAG的形式（若讀者不知道什麼是RAG，請參考教案一單元三的內容）作為外部知識匯入GPT，這樣學生在學習的時候如果有遇到不懂的事情，除了老師或助教之外，現在也能直接詢問GPT。
3. **客製化設計**：針對不同孩童的使用需求，將相同的概念改為不同的版本，甚至是提供多國語言的版本。

### 2.2 學界論文研讀
1. **截圖詢問GPT**：在這部分可以針對想要瞭解更多的部份截圖，並且直接上傳ChatGPT（需要訂閱），這樣就可以針對截圖的內容和ChatGPT有更多討論。
2. **論文導讀**：如果是比較困難的論文需要整篇協助，那麼同樣也可以利用RAG的方式匯入GPT，然後再開始相關的提問。

### 2.3 撰寫期刊論文
1. **建立自己的知識庫**：通常到了能夠撰寫期刊論文的階段表示過去已經在該領域有數篇論文的發表了，然後我們會想要在期刊發表上，基於過去的研究再做更進一步的突破。此時可以利用RAG的方式將過往的研究作為外部知識，然後接著撰寫新的想法，而這些想法都能夠和相關的大型語言模型討論，在這邊如果擔心檔案外流，則建議讀者**不要使用**ChatGPT，改使用離線版本的大型語言模型才能確保完整的資料隱私。
2. **建立領域GPT**：在這邊可以利用RAG的技術或是自行微調大型語言模型，將目標領域的文獻全部當作知識匯入，而後就可以在有靈感的時候和這些語言模型對話。

在以上三個情境當中，我們都可以觀察到生成式AI服務能夠作為討論的夥伴，協助我們更好的達成目標。

## 3. 新聞媒體業使用情境
在新聞媒體業當中，如果要撰寫一篇網路文章，通常會需要經過以下流程：題材發想、文章主視覺決定、文案架構決定、蒐集題材資訊、撰寫文案、發布文章。

過去這些流程需要大量仰賴人力進行，如果是規模大一點的組織，可能可以請軟體部門協助自動化一定的流程（如：發布文章），但是在有了生成式工具的情況下，這些流程也可以有一定程度的改善與加速。

### 生成式AI可能帶來的效益
1. **分析網路關鍵字**：此步驟可以觀察網路上近一個禮拜到一個月的文章，並且請ChatGPT協助分析幾個特定的題材。
2. **顧問角色扮演**：我們也可以自己先設想幾個題材，然後再請GPT扮演相關的編輯顧問，一來一往的分析題材優勢與劣勢，進而幫助決策。
3. **輔助撰寫文案**：在決定好架構之後，我們可以提供GPT文案架構，請它針對該架構生成一定的文案，並且可以視情況給予相關限制，如字數上面的限制。
4. **自動化文章發布流程**：即使可能自己不是軟體工程師，我們也能夠將需求告訴ChatGPT，請他協助撰寫可以執行的`python`程式碼，要求GPT撰寫能夠自動幫我們發布在不同平台的程式碼。

## 4. 營銷和廣告使用情境（參考社群媒體貼文生成需求）
如果公司現在要推廣某個產品，如：貓咪衣服，那麼廣告營銷部門的人員就會需要在不同的通路進行推廣，可能包含：社群媒體、電視廣告、YouTube插播廣告、電台等。過去這些內容，一樣也會大量仰賴相關人員的專業，需要將同一個語言轉譯成適合不同媒介的題材；甚至是在提案的時候也需要一個理解公司各部門執掌的人員撰寫提案，而這些情況也會因為生成式AI工具的出現而有一定的變化。

#### 生成式AI可能帶來的效益
1. **提案發想**：這部分可以請ChatGPT扮演不同部門的主管（甚至是自己的上司），請它嘗試從不同的角度挑戰提案，並且進一步的改善提案內容，詳細的展示可以參考[教案六單元三](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/tree/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/%E5%96%AE%E5%85%833%EF%BC%9A%E5%AF%A6%E9%9A%9B%E6%B8%AC%E8%A9%A6%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%B7%A5%E5%85%B7)。
2. **渠道題材發想**：這部分我們可以提供GPT過往部門的推廣成果，請GPT協助分析適合用於新的推廣上的策略，同樣的相關的操作內容也可以參考[教案六單元三](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/tree/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/%E5%96%AE%E5%85%833%EF%BC%9A%E5%AF%A6%E9%9A%9B%E6%B8%AC%E8%A9%A6%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%B7%A5%E5%85%B7)。。