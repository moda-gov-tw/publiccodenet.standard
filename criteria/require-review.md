---
order: 7
---

# 要求審查貢獻內容

<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- written in 2019 - 2022 by The Foundation for Public Code <info@publiccode.net> -->

## 需求規範

* 所有被接受或是提交給[代碼庫](../glossary.md#codebase)正式發行版本中的貢獻內容，都必須經過另一位貢獻者審查。
* 審查必須包含原始碼、[政策](../glossary.md#policy)、測試、文件等。
* 如果不接受貢獻內容，審查人員必須提供意見回饋。
* 貢獻內容應該遵循代碼庫的標準、架構、決策安排等，以通過審查。
* 審查內容應該包含執行[程式碼](../glossary.md#code)與執行代碼庫測試。
* 貢獻內容應該由與貢獻者不同背景情境的人來審查。
* 版本控制系統不應該在代碼庫的正式發行版本中，接受未經審查的貢獻內容。
* 審查應該在兩個工作天內進行。
* 可選擇是否由多位審查人員進行審查。

## 此措施為何重要

* 提升代碼庫品質。
* 降低安全性風險與營運風險。
* 打造每份貢獻內容皆能有品質的文化。
* 揪出可能發生的極明顯錯誤。
* 只有真正能為代碼庫提升價值的貢獻內容才會被接受，可以給予貢獻者安全感。
* 向貢獻者保證在一段時間內提供意見回饋或是合作改善。
* 快速審查能提高貢獻者交付貢獻內容的頻率以及參與熱度。

## 此措施辦不到的事

* 保證能找到問題的合適解決方案。
* 代表審查人員必須承擔責任。
* 貢獻者能從編寫文件與測試中免除責任。
* 提供您合適的審查人選。

## 測試方式

* 確認歷史紀錄中每個提交內容都有經過不同的貢獻者審查。
* 確認審查內容包含原始碼、政策、測試、文件等。
* 針對未被採用的貢獻內容，確認有適當解釋原因。
* 檢查審查範圍有涵蓋是否遵循標準、架構、代碼庫指引等。
* 檢查審查人員在審查時是否有執行程式碼與測試。
* 與審查人員確認，提交的內容是否有經過不同情境背景的不同貢獻者審查。
* 檢查[版本控制](../glossary.md#version-control)系統中是否有採用分支保護。
* 檢查貢獻提交與審查之間的時間間隔。

## 政策制定者：需要的工作

* 制定進行任何審查時，含程式碼與其他一切事物，都要恪遵「四眼原則」的政策。
* 採用具有審查與意見回饋功能的版本控制系統或作業流程。

## 管理人員：需要的工作

* 將交付妥善程式碼作為共同目標。
* 確保如原始碼、政策、文件、測試等的撰寫與審查貢獻，皆受到同等重視。
* 創造歡迎所有形式的貢獻，而且每個人都能夠審查貢獻內容的文化。
* 確保貢獻者在貢獻內容給代碼庫時，不是獨自一人埋頭苦幹。

## 開發人員與設計師：需要的工作

* 請代碼庫的其他貢獻者，審查您在貴組織單位內外的工作成果。
* 當他人請求您審查程式碼時，請盡快回覆，並先給出程式碼需要修正之處背後的概念。

## 延伸閱讀

* 英國政府數位服務團《[英國政府數位服務團程式碼審查程序](https://gds-way.cloudapps.digital/manuals/code-review-guidelines.html#content)》。
* [GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
與 [GitLab](https://about.gitlab.com/2014/11/26/keeping-your-code-protected/)
平臺的分支保護說明。
* Sage Sharp《[程式修補審查的和善藝術](https://sage.thesharps.us/2014/09/01/the-gentle-art-of-patch-review/)》。
* Mozilla《[參與度評測成果](https://docs.google.com/presentation/d/1hsJLv1ieSqtXBzd5YZusY-mB8e1VJzaeOmh8Q4VeMio/edit#slide=id.g43d857af8_0177)》。
