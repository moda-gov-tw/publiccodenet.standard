---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 10
redirect_from:
  - criteria/understandable-english-first
---

# 使用白話的英語

English is the <i>de facto</i> language of collaboration in software development.

Public sector information needs to be accessible to all its constituents.
Plain and simple language makes the [code](../glossary.md#code) and what it does easier to understand for a wider variety of people.

Translations further increase the possible reach of a [codebase](../glossary.md#codebase).
Language that is easy to understand lowers the cost of creating and maintaining translations.

## 需求規範

* All codebase documentation MUST be in English.
* All [source code](../glossary.md#source-code) MUST be in English, except where [policy](../glossary.md#policy) is machine interpreted as code.
* All bundled policy not available in English MUST have an accompanying summary in English.
* Any translation MUST be up to date with the English version and vice versa.
* There SHOULD be no acronyms, abbreviations, puns or legal/non-English/domain specific terms in the codebase without an explanation preceding it or a link to an explanation.
* Documentation SHOULD aim for a lower secondary education reading level, as recommended by the [Web Content Accessibility Guidelines 2](https://www.w3.org/WAI/WCAG21/quickref/?showtechniques=315#readable).
* Providing a translation of any code, documentation or tests is OPTIONAL.

## How to test

* 確認代碼庫文件有英語版本。
* 確認原始碼為英語，確認任何非英語內容都是政策，或確認術語在其前方有先行說明等。
* 確認任何非英語政策都有隨附英語版摘要。
* 確認翻譯版與英語版內容相同。
* 確認文件當中，沒有任何未說明的首字母縮寫字、縮寫、雙關語，或法律/非英語/行業特定詞彙等。
* 檢查文件的拼字、文法與易讀性等。

## Public policy makers: what you need to do

* Frequently test with other managers, developers and designers in the process if they understand what you are delivering and how you document it.

## Managers: what you need to do

* 在團隊內部與利害關係人之間的內部溝通中，試著限制首字母縮寫字、縮寫、雙關語，或法律/非英語/行業特定詞彙的使用。如果有使用到的話，則將這些用語加入詞彙表，並且在使用這些詞彙的地方加上詞彙表連結。
* 以批判性觀點看待提案與修改當中的文件與描述。如果有您看不懂的內容，很有可能其他人也同樣迷惘。

## 開發人員與設計師：需要的工作

* Frequently test with policy makers and managers if they understand what you are delivering and how you document it.
* Ask someone outside of your context if they understand the content (for example, a developer working on a different codebase).

<p style="page-break-after: always;"></p>

## Further reading

* Meeting the [Web Content Accessibility Guidelines 2.1, Guideline 3.1 Readable](https://www.w3.org/TR/WCAG21/#readable) by W3C makes text content readable and understandable.
* The[European Union accessibility directive](https://ec.europa.eu/digital-single-market/en/web-accessibility) by the European Commission, is an example of regulation requiring high accessibility.
* [Definition of plain language](https://www.plainlanguage.gov/about/definitions/) by United States General Services Administration.
