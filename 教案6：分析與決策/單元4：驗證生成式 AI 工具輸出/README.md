# 生成式 AI 工具輸出驗證方法

## 1. 前言
我們曾經在教案三單元四中介紹過Human-in-the-loop的概念，如果是真的進入到決策階段，在重大的情節下我們都會建議讓人類介入，不過在比較單純簡單的情境當中，或許就能夠單純的應用在數個教案當中提到的RAG功能，直接讓用戶自己去看看GPT等大型語言模型提供的參考索引是否合理。本單元會探討在Human-in-the-loop當中，從全人工到全自動不同階段可能的使用情境，以確保AI輸出的可靠性不會危害的使用者。

## 2. Human-in-the-loop
其實並不是所有的情境都會需要人類大量的介入，我們會希望在重大的裁決過程中有更多的程度的人的介入，不過若是基本的一些自動化判斷，AI的準確率可能也超過人類專家了，這種情況或許就可以採用全為機器人（Bots Only）的模式。
| 全部都是人類 | AI輔佐人類 | 人類處理Cornor Cases | 全部都是AI |
| :--: | :--: | :--: | :--: |
| Humans Only | Bots Support Humans| Bots Triages for Human | Bots Only |
| 就是過去的決策方式 | AI提出一些資料的洞見，幫助人類決策 | AI處理較為簡單的大部分情境，困難或是難以判斷的情境交給人類 | 交給AI來做所有決策，建議可以加入RAG等機制，讓使用者能夠自行判斷AI的輸出內容 |

### 補充：歐盟提出的「可信賴人工智慧倫理準則」
人類自主性和監控(Human agency and oversight)：AI是為強化人類能力而存在，使人類使用者能夠做出更明智的決策並培養自身的基礎能力。同時，AI應有相關監控機制以確保AI系統不會侵害人類自主性或是引發其他負面效果。本準則建議，監控機制應可透過人機混合（一種整合人工智慧與人類協作的系統，例如human-in-the-loop, human-on-the-loop, and human-in-command）的操作方法來實現。

## 3. 參考企業實際導入生成式AI的方法
多數企業導入生成式AI的方法大多服從我們在教案三單元四提出的框架相同（見下圖），並且都會在使用條款上向使用者說明，生成式AI可能會產生錯誤的訊息，請使用者要多加注意。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%883%EF%BC%9A%E6%96%87%E5%AD%97%E5%85%A7%E5%AE%B9%E7%9A%84%E7%94%9F%E6%88%90%E8%88%87%E6%91%98%E8%A6%81/pics/unit4/pic.human-in-the-loop.png" height="600px">
</div>

### 補充：Nvidia NeMo 提出的 Guardrails
為了幫助企業在導入生成式AI服務的時候能夠最大程度避免錯誤訊息的輸出，Nvidia NeMo裡面也有提供Guardrails的服務，並針對三個面向做加強：
1. 主題安全護欄：可以避免應用程式偏離到不想要的領域。例如，它們可以防止客戶服務助理回答關於天氣的問題。
2. 安全護欄：確保應用程式回覆準確、適當的資訊。它們可以過濾不必要的語言，並強制要求只引用可信的來源。
3. 保全護欄：限制應用程式僅與已知為安全的外部連結建立連接。

如果各位讀者正在建立幫助自身決策的生成式AI機器人，不妨可以參考[這篇文章](https://blogs.nvidia.com.tw/2023/04/26/ai-chatbot-guardrails-nemo/)，嘗試將Nvidia NeMo Guardrails導入自己的服務當中。

## 參考資源
 * DeepLearnin.ai [Generative.AI for Everyone](https://www.deeplearning.ai/courses/generative-ai-for-everyone/)
 * Nvidia [NeMo Guardrails](https://blogs.nvidia.com.tw/2023/04/26/ai-chatbot-guardrails-nemo/) 