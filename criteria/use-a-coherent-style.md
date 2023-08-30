---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 15
redirect_from:
  - criteria/style
---
# 風格要前後一致

採用前後一致的風格，讓不同環境的貢獻者能夠合作。用詞統一能減少貢獻者之間在溝通上的摩擦。

## 規定

* [代碼庫](../glossary.md#codebase)必須遵守程式碼撰寫風格指南、或文件寫作風格指南，可以是代碼庫社群自身的風格指南，或是代碼庫有採用的既
有風格。
* 貢獻內容應該通過自動化的風格測試。
* 風格指南應該描述對較複雜的程式碼區段，當中列內註解與說明文件的期望。
* 可選擇是否將[可理解的白話英語](use-plain-english.md)小節加入風格指南之中。

## 測試方式

* 確認貢獻內容有遵循文件中指定的風格指南。
* 檢查是否有自動化的風格測試。

## 公共政策制定者：您的責任

* 為[政策](../glossary.md#policy)與文件建立風格指南，遵守並且持續改善，同時記錄到代碼庫文件中，像是「`CONTRIBUTING`」或
「`README`」檔案。

## 管理人員：您的義務

* 將書面語言、原始碼、測試、政策標準等，包含在貴組織單位對品質的定義當中。

## 開發人員與設計師：您的責任

如果代碼庫還沒有工程指南，或其他貢獻者指南，則請先在[儲存庫](../glossary.md#repository)中加入相關文件，像是
「`CONTRIBUTING`」或「`README`」檔案，並描述目前在設立指南方面的進展。上述檔案的重要目的之一，在於宣達設計偏好、命名規則，以及機器不容易檢查
的其他層面。指南應該包含貢獻的[原始碼](../glossary.md#source-code)預期該符合哪些要求，才會被維護人員加入代碼庫中，包含原始碼、測試、
文件等項目。請持續改善與擴充這份文件內容，目標讓文件朝向工程指南演進。

此外：

* 使用程式碼品質分析工具 (linter)。
* 在代碼庫中加入程式碼品質分析工具的組態設定。

## 延伸閱讀

* 維基百科上的《[代碼風格](https://en.wikipedia.org/wiki/Programming_style)》條目。
