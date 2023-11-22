---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 6
redirect_from:
  - criteria/version-control-and-history
---

# 維護版本控制

[Version control](../glossary.md#version-control) means keeping track of changes to the [source code](../glossary.md#source-code) and other files of the [codebase](../glossary.md#codebase) over time.
This allows you to maintain structured documentation of the history of the codebase.
This is essential for collaboration at scale, as it enables developers to work on changes in parallel and helps future developers to understand the reasons for changes.

## 需求規範

* All files in the codebase MUST be version controlled.
* All decisions MUST be documented in commit messages.
* Every commit message MUST link to discussions and issues wherever possible.
* The codebase SHOULD be maintained in a distributed version control system.
* Contribution guidelines SHOULD require contributors to group relevant changes in commits.
* Maintainers SHOULD mark released versions of the codebase, for example using revision tags or textual labels.
* Contribution guidelines SHOULD encourage file formats where the changes within the files can be easily viewed and understood in the version control system.
* It is OPTIONAL for contributors to sign their commits and provide an email address, so that future contributors are able to contact past contributors with questions about their work.

## How to test

* 確認代碼庫維持在版本控制狀態中，像是使用 Git 之類的軟體。
* 審查提交內容歷史紀錄，確認所有的提交訊息皆有解釋之前程式碼修改變動的原因。
* 審查提交內容歷史紀錄，確認所有提交訊息之中，盡可能在所有討論過修改變更的地方，包含變動內容以及連結位置（提供網址）。
* 檢查版本控制系統是否為分散式。
* 審查提交內容歷史紀錄，檢查是否有根據貢獻指南將相關的程式碼變動以群組分類。
* 檢查是否可能透過像是修訂版次標記，或文字標籤，來存取代碼庫中的特定版本。
* 檢查代碼庫在可能的情況下，檔案都是採用文字格式。

## Public policy makers: what you need to do

* 如果因為[政策](../glossary.md#policy)改變而在代碼庫中有新的版本，則請確認有在文件中清楚說明：
   * 政策改變的地方，
   * 代碼庫如何因應而改變。

舉例來說，在做權限管理賦予取用權的代碼庫中，如果要新增申請方類別，就會視為政策變動。

## Managers: what you need to do

* 支持政策制定者、開發人員與設計師，使其能清楚表達他們對代碼庫做出的改善。確保改善代碼庫不會有公關風險。

## 開發人員與設計師：需要的工作

* Make sure that all files required to understand the code, build and deploy are in the version control system.
* Write clear commit messages so that it is easy to understand why the commit was made.
* Mark different versions so that it is easy to access a specific version, for example using revision tags or textual labels.
* Write clear commit messages so that versions can be usefully compared.
* Work with policy makers to describe how the source code was updated after a policy change.

## 延伸閱讀

* [Producing OSS: Version Control Vocabulary](https://producingoss.com/en/vc.html#vc-vocabulary) by Karl Fogel.
* [Maintaining version control in coding](https://www.gov.uk/service-manual/technology/maintaining-version-control-in-coding) by the UK Government Digital Service.
* [GitHub Skills](https://skills.github.com/) by GitHub for learning how to use GitHub or refresh your skills.
* [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) by GitHub, a list with the most common used git commands.
