---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 15
redirect_from:
  - criteria/style
---

# 風格要前後一致

Following a consistent and coherent style enables contributors in different environments to work together.
Unifying vocabularies reduces friction in communication between contributors.

## 需求規範

* The [codebase](../glossary.md#codebase) MUST use a coding or writing style guide, either the codebase community's own or an existing one referred to in the codebase.
* Contributions SHOULD pass automated tests on style.
* The style guide SHOULD include expectations for inline comments and documentation for non-trivial sections.
* Including expectations for [understandable English](use-plain-english.md) in the style guide is OPTIONAL.

## 測試方式

* 確認貢獻內容有遵循文件中指定的風格指南。
* 檢查是否有自動化的風格測試。

## Public policy makers: what you need to do

* 為[政策](../glossary.md#policy)與文件建立風格指南，遵守並且持續改善，同時記錄到代碼庫文件中，像是「`CONTRIBUTING`」或「
`README`」檔案。

## Managers: what you need to do

* 將書面語言、原始碼、測試、政策標準等，包含在貴組織單位對品質的定義當中。

## 開發人員與設計師：需要的工作

If the codebase does not already have engineering guidelines or other contributor guidance, start by adding documentation to the [repository](../glossary.md#repository) describing whatever is being done now, for example in the `CONTRIBUTING` or `README`.
An important purpose of the file is to communicate design preferences, naming conventions, and other aspects machines can't easily check.
Guidance should include what would be expected from [source code](../glossary.md#source-code) contributions in order for them to be merged by the maintainers, including source, tests and documentation.
Continually improve upon and expand this documentation with the aim of evolving this documentation into engineering guidelines.

此外：

* 使用程式碼品質分析工具 (linter)。
* 在代碼庫中加入程式碼品質分析工具的組態設定。

## 延伸閱讀

* [Programming style](https://en.wikipedia.org/wiki/Programming_style) on Wikipedia.
