---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 7
redirect_from:
  - criteria/require-review
---

# 要求審查貢獻內容

同儕審查貢獻是[原始碼](../glossary.md#source-code)提升品質的關鍵，也能降低安全性風險與營運風險。

要求仔細審查貢獻，能孕育出確保貢獻都是優質、完整且能帶來價值的文化。審查原始碼能提高在原始碼加入[程式基底](../glossary.md#codebase)之前，
就發現與修正潛在臭蟲與出錯的機率。得知所有原始碼都會被審查，就不會孕育出習慣怪罪他人的文化，反倒是鼓勵每個人都專注在解決方案上。

快速審查[政策](../glossary.md#policy)在於向貢獻者保證，必定在一段時間內提供意見回饋或是協作式改善，進而提高貢獻者交付貢獻內容的頻率，以及參
與的熱度。

## 需求規定

* 所有被接受或是送交給程式基底正式發行版本中的貢獻內容，都「必須」經過另一位貢獻者審查。
* 審查「必須」包含原始碼、政策、測試、文件等。
* 如果不接受貢獻內容，審查人員「必須」提供意見回饋。
* 審查流程「應該」確認貢獻內容遵循程式基底的標準、架構、決策安排等，以通過審查。
* 審查內容「應該」包含執行軟體與執行程式基底測試。
* 貢獻內容「應該」由與貢獻者不同背景情境的人來審查。
* 版本控制系統「不應該」在程式基底的正式發行版本中，接受未經審查的貢獻內容。
* 審查「應該」在兩個工作天內進行。
* 「可選擇」是否由多位審查人員進行審查。

## 測試方式

* 確認歷史紀錄中，每個送交版次都有經過不同的貢獻者審查。
* 確認審查內容包含原始碼、政策、測試、文件等。
* 針對未被採用的貢獻內容，確認有適當解釋原因。
* 檢查審查人員指引中，有包含是否遵循標準、架構、程式基底指引等指示。
* 檢查審查人員在審查時是否有執行軟體與測試。
* 與審查人員確認，送交版次是否有經過不同情境背景的不同貢獻者審查。
* 檢查[版本控制](../glossary.md#version-control)系統中是否有採用分支保護。
* 檢查貢獻提交與審查之間的時間間隔。

## 公共政策制定者：需要的工作

* 制定進行任何審查時，含原始碼與其他一切事物，都要恪遵「四眼原則」的政策。
* 採用具有審查與意見回饋功能的版本控制系統，或作業流程。

## 管理人員：需要的工作

* 將交付妥善軟體作為共同目標。
* 確保如原始碼、政策、文件、測試等的貢獻內容撰寫與審查，皆受到同等重視。
* 創造歡迎所有形式的貢獻，而且每個人都能夠審查貢獻內容的文化。
* 確保貢獻者在貢獻內容給程式基底時，不是獨自一人埋頭苦幹。

## 開發人員與設計師：需要的工作

* 請程式基底的其他貢獻者，審查您在貴組織單位內外的工作成果。
* 當他人請求您審查時，請盡快回覆，並先給出需要修正之處背後的概念。

## 延伸閱讀

* 英國政府數位服務團《[英國政府數位服務團程式碼審查程序](https://gds-way.cloudapps.digital/manuals/code-review-guidelines.html#content)》。
* [GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
與
[GitLab](https://about.gitlab.com/blog/2014/11/26/keeping-your-code-protected/) 平
臺的分支保護說明。
* Sage Sharp《[程式修補審查的和善藝術](https://sage.thesharps.us/2014/09/01/the-gentle-art-of-patch-review/)》。
* Mozilla《[參與度評測成果](https://docs.google.com/presentation/d/1hsJLv1ieSqtXBzd5YZusY-mB8e1VJzaeOmh8Q4VeMio/edit#slide=id.g43d857af8_0177)》。
