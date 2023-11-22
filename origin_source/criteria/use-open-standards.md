---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 11
redirect_from:
  - criteria/open-standards
---

# 採用開放標準

[Open standards](../glossary.md#open-standard) guarantee access to the knowledge required to use and contribute to the [codebase](../glossary.md#codebase).
They enable interoperability between systems and reduce the risk of vendor lock-in.
Open standards which are unambiguous allow for independent development of either side of data exchange.

## 需求規範

* For features of the codebase that facilitate the exchange of data the codebase MUST use an open standard that meets the [Open Source Initiative Open Standard Requirements](https://opensource.org/osr).
* Any non-open standards used MUST be recorded clearly as such in the documentation.
* Any standard chosen for use within the codebase MUST be listed in the documentation with a link to where it is available.
* Any non-open standards chosen for use within the codebase MUST NOT hinder collaboration and reuse.
* If no existing open standard is available, effort SHOULD be put into developing one.
* Open standards that are machine testable SHOULD be preferred over open standards that are not.
* Non-open standards that are machine testable SHOULD be preferred over non-open standards that are not.

## 測試方式

* 確認資料交換遵守 OSI 開放原始碼促進會批准的開放標準。
* 確認若有採用任何的非開放標準，皆有清楚記錄在文件中。
* 確認文件有清單列出代碼庫所採用的標準，其中各標準有對應的有效連結；或沒有採用任何標準時，則留下聲明。

## Public policy makers: what you need to do

* 以政策要求盡可能在任何情況下使用開放標準。
* 禁止採購不採用開放標準的技術科技。

## Managers: what you need to do

* Consider including open standard compliance assessment in [source code](../glossary.md#source-code) reviews.

## 開發人員與設計師：需要的工作

* 將是否依循標準加入[持續整合](../glossary.md#continuous-integration)測試中。
* 審查提交紀錄與其他[儲存庫](../glossary.md#repository)資源是否有參考開放標準，並交叉檢查其中有列出標準的部分。

## 延伸閱讀

* 英國內閣辦公室發表的《[開放標準原則](https://www.gov.uk/government/publications/open-standards-principles/open-standards-principles)》
[政策](../glossary.md#policy)報告。
