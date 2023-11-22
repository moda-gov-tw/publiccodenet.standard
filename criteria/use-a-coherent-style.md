---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 15
redirect_from:
  - criteria/style
---

# 風格要前後一致

採用前後一致的風格，讓不同環境的貢獻者能夠一同合作。用詞統一能減少貢獻者之間在溝通上的摩擦。

## 需求規定

* [程式基底](../glossary.md#codebase)「必須」遵守程式碼撰寫風格指引、或文件寫作風格指引，可以是程式基底社群自身的風格指引，或是程式基底
有採用的既有風格。
* 貢獻內容「應該」通過自動化的風格測試。
* 風格指引「應該」描述對於較複雜的程式碼區段，如何作列內註解與為其寫下說明文件的期待。
* 「可選擇」是否將[可理解的白話英語](use-plain-english.md)期望加入風格指引之中。

## 測試方式

* 確認貢獻內容有遵循文件中指定的風格指引。
* 檢查是否有自動化的風格測試。

## 公共政策制定者：需要的工作

* 為[政策](../glossary.md#policy)與文件建立風格指引，遵守並且持續改善，同時記錄到程式基底文件中，像是「`CONTRIBUTING`」或
「`README`」檔案。

## 管理人員：需要的工作

* 將書面語言、原始碼、測試、政策標準等，包含在貴組織單位對品質的定義當中。

## 開發人員與設計師：需要的工作

如果程式基底還沒有工程指引，或其他貢獻者指引，則請先在[儲存庫](../glossary.md#repository)中加入相關文件，像是
「`CONTRIBUTING`」或「`README`」檔案，並描述目前在設立指引方面的進展。上述檔案的重要目的之一，在於宣達設計偏好、命名規則，以及機器不容易檢查
的其他層面。指引應該包含貢獻的[原始碼](../glossary.md#source-code)預期該符合哪些要求，才會被維護人員合併至程式基底中，包括原始碼、測
試、文件等項目。請持續改善與擴充這份文件內容，目標讓文件朝向工程指引演進。

此外：

* 使用 linter 程式碼品質梳理工具。
* 在程式基底中加入 linter 梳理工具的組態設定。

## 延伸閱讀

* 維基百科上的《[程式碼風格](https://en.wikipedia.org/wiki/Programming_style)》條目。
