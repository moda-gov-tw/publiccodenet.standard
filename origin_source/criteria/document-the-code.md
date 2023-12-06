---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 9
redirect_from:
  - criteria/documenting
---
# 程式碼有文件

Well documented [source code](../glossary.md#source-code) helps people to understand what the source code does and how to use it.
Documentation is essential for people to start using the [codebase](../glossary.md#codebase) and contributing to it more quickly.

## 需求規範

* All of the functionality of the codebase, [policy](../glossary.md#policy) as well as source code, MUST be described in language clearly understandable for those that understand the purpose of the codebase.
* The documentation of the codebase MUST contain a description of how to install and run the software.
* The documentation of the codebase MUST contain examples demonstrating the key functionality.
* The documentation of the codebase SHOULD contain a high level description that is clearly understandable for a wide audience of stakeholders, like the [general public](../glossary.md#general-public) and journalists.
* The documentation of the codebase SHOULD contain a section describing how to install and run a standalone version of the source code, including, if necessary, a test dataset.
* The documentation of the codebase SHOULD contain examples for all functionality.
* The documentation SHOULD describe the key components or modules of the codebase and their relationships, for example as a high level architectural diagram.
* There SHOULD be [continuous integration](../glossary.md#continuous-integration) tests for the quality of the documentation.
* Including examples that make users want to immediately start using the codebase in the documentation of the codebase is OPTIONAL.

## 測試方式

* Confirm that other stakeholders, professionals from other public organizations and the general public find the documentation clear and understandable.
* Confirm that the documentation describes how to install and run the source code.
* Confirm that the documentation includes examples of the key functionality.
* Check with members of the general public and journalists if they can understand the high level description.
* Check that the instructions for how to install and run a standalone version of the source code result in a running system.
* Check that all functionality documented contains an example.
* Check that the documentation includes a high level architectural diagram or similar.
* Check that the documentation quality is part of integration testing, for example documentation is generated correctly, and links and images are tested.

## Public policy makers: what you need to do

* 定期查看代碼庫的非政策程式碼的變動情況。
* 針對如何讓非政策文件更清楚易懂提供意見回饋。

## Managers: what you need to do

* Try to use the codebase, so your feedback can improve how clearly the policy and source code are documented. For example, is the current documentation sufficient to persuade a manager at another public organization to use this codebase?
* Make sure you understand both the policy and source code as well as the documentation.

## 開發人員與設計師：需要的工作

* 定期查看代碼庫中非原始碼部分的變動情況。
* 針對如何讓非原始碼文件更清楚易懂提供意見回饋。

## 延伸閱讀

* Write the Docs《[文件指南](https://www.writethedocs.org/guide/)》。
