---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 11
redirect_from:
  - criteria/open-standards
---

# 採用開放標準

[開放標準](../glossary.md#open-standard)保證可以取得使用與貢獻[程式基底](../glossary.md#codebase)所需的知
識。不僅能為不同的系統之間建立互通性，更能降低廠商套牢的可能性。開放標準如果明確，不同方就可以各自獨立開發作資料交換。

## 需求規定

* 程式基底如要促進資料交換的特性，就「必須」採用符合 [OSI 開放原始碼促進會其《開放標準需求規範](https://opensource.org/osr)》的
開放標準。
* 如果有使用到任何非開放標準，則「必須」在文件中清楚記錄。
* 程式基底選擇採用的任何標準，皆「必須」在文件中列出，並且只要有的話，就附上該標準的連結。
* 程式基底選擇採用的任何非開放標準，皆「禁止」妨礙程式基底的協作與重複使用。
* 如果還沒有已存在的開放標準可採用，則「應該」投入開發新標準。
* 採用開放標準時，「應該」優先選擇可經機器測試的開放標準。
* 採用非開放標準時，「應該」優先選擇可經機器測試的非開放標準。

## 測試方式

* 確認資料交換遵守 OSI 開放原始碼促進會批准的開放標準。
* 確認若有採用任何的非開放標準，皆有清楚記錄在文件中。
* 確認文件有清單列出程式基底所採用的標準，其中各標準有對應的有效連結；或沒有採用任何標準時，則留下聲明。

## 公共政策制定者：需要的工作

* 以政策要求盡可能在任何情況下採用開放標準。
* 禁止採購不採用開放標準的技術科技。

## 管理人員：需要的工作

* 考慮在[原始碼](../glossary.md#source-code)審查中納入開放標準依循評估。

## 開發人員與設計師：需要的工作

* 將是否依循標準加入[持續整合](../glossary.md#continuous-integration)測試中。
* 審查送交版次與[儲存庫](../glossary.md#repository)其他資源是否有參考開放標準，並交叉檢查其中有列出標準的部分。

## 延伸閱讀

* 英國內閣辦公室發表的《[開放標準原則](https://www.gov.uk/government/publications/open-standards-principles/open-standards-principles)》
[政策](../glossary.md#policy)報告。
