---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 2
redirect_from:
  - criteria/bundle-policy-and-code
---

# 政策與原始碼要合捆

對於想根據所在情境實作程式基底的人，或是想更進一步貢獻[程式基底](../glossary.md#codebase)開發的人來說，能同時取用[原始碼](../glossary.md#source-code)與[政策](../glossary.md#policy)文件兩者，可作為建置成品時的基礎組件。

瞭解作用範疇與該範疇的政策是基本原則，才能瞭解程式基底試圖想解決的問題是什麼，以及該如何解決這些問題的作法。

為了評估是否需要在新的情境中實作程式基底，組織單位需要瞭解必須做出改變的程序有哪些，或是如何對現有解決方案付出額外調整設定，以適應新的情境背景。

## 需求規定

* 程式基底「必須」包含原始碼所根據的政策。
* 如果政策根據原始碼而來，則該原始碼「必須」包含在程式基底中，用於偵測詐騙的原始碼則可除外。
* 政策「應該」採用機器可讀且明確的格式。
* [持續整合](../glossary.md#continuous-integration)測試「應該」驗證原始碼與政策是否有一致執行。

## 測試方式

* 與公務人員確認原始碼所根據的所有政策內容都有收錄在內。
* 與公務人員確認政策所根據的所有原始碼都有收錄在內。
* 確認政策內容是否能在機器上解讀。
* 確認原始碼與政策間的執行一致性能通過持續整合測試。

## 公共政策制定者：需要的工作

* 與開發人員及設計師合作，確保政策法規與原始碼之間沒有不相符之處。
* 提供相關政策內文，以便收錄於[儲存庫](../glossary.md#repository)中；如果政策內文沒有英文版，請提供英文版摘要。務必也同時包含貴組織單
位所選擇遵守的各項標準，以及影響貴組織單位程式基底開發或部署情境的任何組織單位流程。
* 請提供政策相關參考資料與連結。
* 政策內容請使用明確且機器可讀的格式，像是[物件管理群體](https://www.omg.org/spec/)所發表的格式。
* 追蹤政策時，請使用與追蹤原始碼[相同的版本控制](maintain-version-control.md)與文件。
* 定期檢查，瞭解程式基底中的原始碼如何變動，以及是否仍然符合[政策意圖](document-codebase-objectives.md)。
* 納入會影響社會群體、程式基底與開發目標的相關政策，包含 [GDPR 一般資料保護規則](https://eur-lex.europa.eu/eli/reg/2016/679/oj)或是[歐盟網頁無障礙命令](https://ec.europa.eu/digital-single-market/en/web-accessibility)等此類法律義務，或者是人權政
策，例如公家機關對機會平等的承諾等。

## 管理人員：需要的工作

* 讓政策制定者、開發人員與設計師持續參與，並且在整個開發過程中保持聯繫溝通。
* 確保政策制定者、開發人員與設計師朝相同目標努力。

## 開發人員與設計師：需要的工作

* 熟悉並且學會貴組織單位政策制定者所使用的流程模型標記法。
* 與政策制定者一同合作，確保政策法規與原始碼之間沒有不相符之處。
* 針對如何讓政策文字更清楚提供意見。

## 延伸閱讀

* 維基百科上的 [BPMN 業務流程模型與標記法](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation)。
* Trisotech 提供的 [BPMN 快速指南](https://www.bpmnquickguide.com/view-bpmn-quick-guide/)。
* 維基百科上的 [DMN 決策模型與標記法](https://en.wikipedia.org/wiki/Decision_Model_and_Notation)。
* 維基百科上的[ CMMN 案例管理模型標記法](https://en.wikipedia.org/wiki/CMMN)。
