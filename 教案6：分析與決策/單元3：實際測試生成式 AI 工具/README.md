# 單元三、實際測試生成式 AI 工具

## 1. 前言
在這個單元，我們將展示如何使用ChatGPT將企業目標（在本單元會以產品行銷策略為例）轉譯成不同管理層級的具體行動，在分派任務的時候會參考不同職位的功能，然而再將生成出來的文字以XMind心智圖呈現。另一個面向，我們也會參考[Kaggle上的商業數據：Dummy Marketing and Sales Data](https://www.kaggle.com/datasets/harrimansaragih/dummy-advertising-and-sales-data)，實際展示如何運用Code Interpretor從中挖取資訊，幫助下一輪的決策更加優化。

讀者將能在本單元實際體驗到如何利用生成式AI工具輔助我們做決策與分析。

## 2. 情境說明
假設我們身為某零售店商公司的行銷部門主管，我們希望在明天的主管會議中提案：希望各部門都能幫助自身團隊，一起推廣下一季預計新上架的產品-貓咪衣服。

為了要做到這件事情，你心裡知道，你會需要以下部門協助完成以下的事情，而且為了說服大家做，你還需要向老闆說明如果達到多少%的轉換率的話，就可以有多少的獲利，因此以下可能是你會列下的文字框架：
### 面向上級主管（老闆）
* 說明每件貓咪衣服的毛利率。
* 計算出可以打平開銷的數量。
* 說明潛在TA有100萬人，而真正的買家會有5%的事實（基於過去的資料）。

### 面向行銷推廣部門
* 在電視（TV）、社群媒體（Social Media）、電台（Radio）推廣。
* 預計在上架前一個月開始宣傳。
* 考慮到過去轉換率有5%，為了達到5萬件貓咪衣服的銷售，我們需要觸及到100萬人次。

### 面向軟體開發部門
* 為新產品製作一頁專屬的Landing Page。
* 在產品頁面埋下資料追蹤點，以利後續資料分析。

### 面向美術設計部門
* 幫助行銷推廣部門準備不同的素材。
* 幫助軟體開發部門提供網頁主視覺。

### 面向人力資源部門
* 為每個部門計算所需人力，確保此提案可行性是高的。

通常在這個步驟，我們會建議讀者盡可能地將自己知道的內容全部提供出來，這樣子可以有效避免GPT發生幻覺行為的情況。

## 3. 組織目標的轉譯
為了將上述情境轉化成不同單位的行動目標，我們在本節會利用ChatGPT角色扮演成不同部門的主管，並請GPT針對上述提案進行挑戰，然後再優化文案；而後將定案的文案利用XMind呈現出來。

### 3.1 請GPT扮演不同主管
我們實際將上述模板提供給GPT，並且明確指示GPT扮演不同的主管，針對我們的提案提出挑戰，並請GPT針對這些挑戰回頭去調整文案。

#### 步驟一：扮演主管提出挑戰
```
ChatGPT您好，我是公司的行銷部門主管，我在明天的主管會議（會有不同部門的主管參與）當中想要提案，希望各部門都能幫助自身團隊，一起推廣下一季預計新上架的產品-貓咪衣服。

虛線以內是我目前針對這個提案發想出來，希望不同部門能做的事情。
--------（虛線開始）--------
在此插入上方的文字
--------（虛線結束）--------

我希望你能「扮演不同部門的主管」，向我的提案提出三個挑戰，請參考下方的格式以列點的形式呈現。

#身為老闆，以下是我的想法
* 挑戰一：
* 挑戰二：
* 挑戰三：

#身為行銷推廣部門主管，以下是我的想法
* 挑戰一：
* 挑戰二：
* 挑戰三：

#身為軟體開發部門主管，以下是我的想法
* 挑戰一：
* 挑戰二：
* 挑戰三：

#身為美術設計部門主管，以下是我的想法
* 挑戰一：
* 挑戰二：
* 挑戰三：

#身為人力資源部門主管，以下是我的想法
* 挑戰一：
* 挑戰二：
* 挑戰三：
```
下表是實際詢問與回覆的畫面，若讀者有興趣參考，歡迎點擊後仔細閱覽：
| 詢問GPT-4 | ChatGPT的回覆內容1 | ChatGPT的回覆內容2 |
| :--: | :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic1.ask.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic2.ans1.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic3.ans2.png) |

#### 步驟二：根據挑戰內容修改既有提案
```
非常謝謝你提出的見解，我覺得都非常的實際

以下是希望你完成的兩件事情：
1. 我希望你能扮演我的角色，根據上述你提及的所有挑戰，根據下面的架構優化我的提案內容。
2. 當你完成提案的撰寫後，請你再告訴我有哪邊的資訊是我需要補充，以增加這個提案通過的可行性！

### 面向上級主管（老闆）
* 項目一
* 項目二
* 項目三

### 面向行銷推廣部門
* 項目一
* 項目二
* 項目三

### 面向軟體開發部門
* 項目一
* 項目二
* 項目三

### 面向美術設計部門
* 項目一
* 項目二
* 項目三

### 面向人力資源部門
* 項目一
* 項目二
* 項目三
```

下表是實際詢問與回覆的畫面，若讀者有興趣參考，歡迎點擊後仔細閱覽：
| 詢問GPT-4 | ChatGPT的回覆內容1 | ChatGPT的回覆內容2 |
| :--: | :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic4.ask.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic5.ans1.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic6.ans2.png) |

而這樣的流程都可以一直進行下去，直到你提供了完整的資訊，或是GPT已經產出讓你滿意的架構了。

### 3.2 視覺化文字架構
假設我們覺得GPT以下的架構非常不錯，我們就可以請它將這段文字內容轉換成XMind可以匯入的形式，如**markdown**。
```
提案內容

面向上級主管（老闆）
項目一：全面市場分析 - 提供全面的市場分析報告，包括競爭對手分析、市場趨勢、目標客群的擴展潛力，以及對比我們產品的獨特賣點。
項目二：長期盈利性規劃 - 展示一個全面的財務模型，不僅涵蓋初期的毛利率和打平開銷數量，還包括長期盈利計劃和風險管理策略。
項目三：市場擴展策略 - 提出具體策略來拓展目標客群，包括新市場的開發和現有市場的深度開掘，並展示預期的成果和時程。

面向行銷推廣部門
項目一：整合營銷計劃 - 制定一個多渠道整合營銷計劃，確保在不同平台（如TV、社群媒體、電台）上的品牌信息一致性和創意性。
項目二：預算分配與效益分析 - 詳細的預算計劃，展示如何在不同的宣傳渠道上分配資源，以及預期的回報率。
項目三：宣傳效果追蹤與分析 - 設計一套系統來追蹤和分析各個宣傳渠道的效果，並制定一套應對計劃以快速調整策略。

面向軟體開發部門
項目一：用戶體驗優化 - 確保Landing Page不僅具有吸引力，而且在用戶導航、購買流程和互動性方面提供卓越的體驗。
項目二：數據安全與隱私保護 - 在追蹤和分析用戶行為時，強調數據安全和隱私保護的重要性，並遵守相關法律法規。
項目三：技術支援與系統維護 - 確立一個強有力的技術支援和網站維護計劃，以應對高流量和潛在的技術問題。

面向美術設計部門
項目一：創意與品牌一致性 - 確保所有設計元素不僅創新吸引，而且與品牌的整體形象和信息保持一致。
項目二：多平台設計適應性 - 強調設計工作需要考慮到不同平台的特性和要求，以確保最佳的用戶體驗。
項目三：時間管理與資源優化 - 提出具體的時間管理和資源分配計劃，以應對多個部門的需求和緊迫的時限。

面向人力資源部門
項目一：人力資源規劃與配置 - 提出一個詳細的人力資源需求計劃，包括每個部門所需的專業技能和人數。
項目二：員工培訓與發展計劃 - 提出一個全面的培訓計劃，幫助員工獲得與新產品推廣相關的技能和知識。
項目三：激勵機制與團隊協作 - 設計有效的激勵機制以提高員工參與度，並促進跨部門之間的協作和溝通。

請幫我將上述文字內容儲存成一個 markdwon 檔案，我想要匯入XMind裡面
```

完整的問答請參考以下表格，注意這邊建議使用GPT-3.5，才不會將事情複雜化：

| 詢問GPT-3.5內容1 | 詢問GPT-3.5內容2 | ChatGPT的回覆內容1 | ChatGPT的回覆內容2 |
| :--: | :--: | :--: | :--: |
| ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic7.ask1.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic8.ask2.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic9.ans1.png) | ![](https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic10.ans2.png) |

這時候請讀者將文字內容儲存在一個markdown檔案裡面，像是本資料夾中的`xmind_input.md`一樣。
再利用Xmind的匯入功能，即可取得以下成果。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic11.xmind.png" width="600px">
</div>

## 4. 基於數據的洞見
這邊我們利用Code Interpretor從真實數據挖掘相關的數據事實，協助決策。延續剛剛的情境，假設我們現在已經行銷了兩個禮拜，然後還有剩下兩個禮拜，我們打算在行銷部門裡面調整行銷策略，我們**想要針對過去行銷和實際銷售的金額**決定之後要怎麼微調，因此我們就可以利用ChatGPT的Code Interpretor功能，幫我們解析資料。

請讀者參考[此Kaggle連結](https://www.kaggle.com/datasets/harrimansaragih/dummy-advertising-and-sales-data)，下載可以操作的Excel檔案，完成後就能夠上傳到GPT，開始我們的提問。

### 4.1 在 Explore 當中找到 Data Analysis 的 GPT
目前針對訂閱的ChatGPT使用者，OpenAI有提供數種不同功能的GPT，這邊我們因為要做數據分析，因此就選擇Data Analysis的GPT作為對話的對象。

<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic12.dataanalysis.png" width="600px">
</div>

### 4.2 上傳檔案，並且直接提出我們的疑問
```
GPT您好，這份檔案是我的部門過去投入在TV、Social Media、Radio對應到實際銷售額（Sales）的檔案，我有以下需求希望你可以幫助我完成：
1. 繪製我們過去投入在 TV、Social Media、Radio 的金額占比（圓餅圖）
2. 請繪製相關的統計圖表，告訴我，我應該要如何調整花費在TV、Social Media、Radio的金額，以獲得最高的銷售額

請你使用繁體中文回答我，不過在繪製圖表的時候維持英文沒關係
如果有遇到任何一個欄位有NaN，請直接將該筆資料（Row）刪除
```

你可以發現，我們在這邊問的問題，和我們一般工作流程中，會去詢問資料科學家的問題非常的相似，而讀者也可以自己看一下這份`Dummy Data HSS.csv`，想想看自己有什麼問題是你好奇的。

| 提問 | 回答1 | 回答2 | 回答3 |
| :--: | :--: | :--: | :--: |
| !()[https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic13.ask.png] | !()[https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic14.ans1.png] | !()[https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic15.ans2.png] | !()[https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic16.ans3.png] |

Note: 
* 會請GPT在繪製圖表的時候使用英文，是因為通常在繪製圖表時使用繁體中文會造成文字編碼的問題，進而影像最後的呈現結果。
* GPT將會一步驟一步驟的像讀者說明目前的進度，整體而言會是一個動態的過程。

#### Data Analysis GPT 告訴我們的結論
* 針對 Q1：投入在 TV、Social Media、Radio 的金額占比（圓餅圖）
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%886%EF%BC%9A%E5%88%86%E6%9E%90%E8%88%87%E6%B1%BA%E7%AD%96/pics/unit3/pic17.pie.png" width="600px">
</div>
* 針對 Q2：如何調整花費在TV、Social Media、Radio的金額，以獲得最高的銷售額

```mardown
根據迴歸分析的結果，我們可以得到以下結論：

1. TV 廣告投資回報率 (ROI): TV廣告的係數為3.5626，這意味著每增加一個單位的TV廣告支出，銷售額平均會增加大約3.56個單位。這是顯著的，因為其P值遠小於0.05。

2. Radio 廣告投資回報率: Radio廣告的係數為-0.0040，但這個結果並不顯著（P值為0.685），這意味著Radio廣告支出對銷售額的影響不明顯。

3. Social Media 廣告投資回報率: Social Media廣告的係數為0.0050，但同樣地，這個結果並不顯著（P值為0.842），表示Social Media廣告支出對銷售額的影響也不明顯。

綜合上述，TV廣告似乎是影響銷售額最大的因素。因此，如果目的是為了最大化銷售額，建議增加在TV廣告上的投資。然而，值得注意的是，廣告效果可能受到許多其他因素的影響，如廣告內容、定位和市場環境等，這些因素在這個分析中並未被考慮。此外，Radio和Social Media的廣告可能在品牌知名度、客戶忠誠度等其他方面有貢獻，儘管它們對銷售額的直接影響不大。 ​
```