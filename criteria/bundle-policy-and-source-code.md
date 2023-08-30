---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 2
redirect_from:
  - criteria/bundle-policy-and-code
---
# 同捆政策與原始碼

使用[原始碼](../glossary.md#source-code)以及[政策](../glossary.md#policy)註解，提供基石給想在當地脈絡使用代碼
庫的人或是想要對[代碼庫](../glossary.md#codebase)進一步發展有所貢獻的人。

瞭解網域與其政策，才能瞭解代碼庫想要解決的問題以及解決方式。

組織要能夠評估是否在新脈絡中執行代碼庫時，必須先瞭解如何改變其流程或是如何在現有解決方案中提供額外的可配置性，才能在新脈絡中使用該代碼庫。

## 規定

* 代碼庫「必須（Must）」包含做為原始碼基礎的政策。
* 若一個政策以原始碼為基礎，該原始碼「必須（Must）」包含在代碼庫內（用於詐騙偵測的原始碼除外）。
* 政策格式「應該（Should）」可以機讀且明確。
* [持續整合](../glossary.md#continuous-integration) 測試「應該（Should）」驗證原始碼與政策是否有一致執行。

## 測試方式

* 與公務人員確認有收錄做為原始碼基礎的完整政策。
* 與公務人員確認有收錄做為政策基礎的完成原始碼。
* 確認政策是否可由機器判讀。
* 透過持續整合測試，確認原始碼與政策的一致執行。

## 公共政策制定者：您的責任

* 與開發人員及設計師合作，確認政策程式碼與原始碼沒有錯配。
* 提供相關政策內文，用來收錄在[存放庫](../glossary.md#repository)中；若內文沒有英文版本，則請提供英文摘要。請務必附上貴機構所遵循的標
準，以及影響貴機構代碼庫開發或部署脈絡的組織流程。
* 引用支持政策的文字並附上連結。
* 用明確且可機讀的格式（像是[對象管理組織](https://www.omg.org/spec/)發佈的格式）來紀錄政策。
* 利用[相同的版本控制l](maintain-version-control.md)以及用來追蹤原始碼的註解，來追蹤政策。
* 定期檢查，瞭解代碼庫中的原始碼如何變動，以及是否依舊符合[政策意圖](document-codebase-objectives.md)。
* 納入影響社群、代碼庫與發展的政策，包括[一般資料保護規則](https://eur-lex.europa.eu/eli/reg/2016/679/oj)或是
[歐盟無障礙指令](https://ec.europa.eu/digital-single-market/en/web-accessibility)這些法律義
務，或是人權政策，像是公共組織對機會平等的承諾。

## 管理人員：您的義務

* 在整個開發流程中，讓政策制定者、開發人員與設計師全程參與。
* 確保政策制定者、開發人員與設計師有同樣的目標。

## 開發人員與設計師：您的責任

* 熟悉並且學會使用貴機構的政策制定者所使用的流程模型標記法。
* 與政策制定者合作，確保政策程式碼與原始碼沒有錯配。
* 針對如何讓政策註解更明確提供意見回饋。

## 延伸閱讀

* 維基百科的[商業流程模型與標記
法](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation)。
* Trisotech的[BPMN快速指南](https://www.bpmnquickguide.com/view-bpmn-quick-guide/)。
* 維基百科的[決策模型與標記法](https://en.wikipedia.org/wiki/Decision_Model_and_Notation)。
* 維基百科的[案例管理模型標記法](https://en.wikipedia.org/wiki/CMMN)。
