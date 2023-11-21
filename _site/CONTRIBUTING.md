# 貢獻此標準

<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- SPDX-FileCopyrightText: 2019-2022 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS -->

🙇‍♀️ 感謝您的貢獻！

我們理解這樣的標準，只有在盡可能與公共技術人員、政策制定者，以及有興趣的人士協作下才能完成。因此，我們很感謝您的意見，樂意得到回饋，以及歡迎提供改善此專案的建議。我
們非常開放任何合作的機會。

我們歡迎每個人提出的議題，以及拉取請求。如果您不大習慣 GitHub ，也歡迎將意見回饋用電子郵件寄送到
[info@publiccode.net](mailto:info@publiccode.net)。

## 問題、建議與議題等

在[發展路線圖](/docs/roadmap.md)中可查看我們勾勒的精要概覽。歡迎回報問題、建議修改，以及發問等，來協助發展。您可以到 [Standard
for Public Code 的 GitHub
Issue](https://github.com/publiccodenet/standard/issues) 頁面中，為本專案[提出 GitHub 議
題](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)。

或者，註冊加入[郵遞論壇列
表](https://lists.publiccode.net/mailman/postorius/lists/standard.lists.publiccode.net/)，
並寄送電子郵件到[standard@lists.publiccode.net](mailto:standard@lists.publiccode.net)。

您不一定要修改我們的程式碼或文件，也能成為貢獻者！

## 為文件與程式碼提出拉取請求

如果您想要在我們的專案中，為文件或程式碼加入新內容，您應該提出拉取請求 (Pull Request，亦可簡稱 PR)。

若您從未使用過 GitHub，歡迎先[認識 GitHub 作業流
程](https://docs.github.com/en/get-started/quickstart/github-flow)，或是參加 [GitHub
Skills](https://skills.github.com/) 免費且優質的互動式課程，當中會介紹該如何使用 GitHub 以及 MarkDown 語法。
MarkDown 是本專案文件所採用的撰寫語法。

本專案採用創用CC 0 1.0 通用式公眾領域貢獻宣告給予授權；這本質上代表本專案，以及您所做出的貢獻，在無論何種司法管轄情況下，都屬於公眾領域，也就是任何人都可以
任意使用。

### 1. 作出您的修改

貢獻內容應該[遵守](docs/standard-for-public-code.html)《公共程式標準》自身所列出的準則規定。審查人員同時也會確保貢獻內容，符合
[公共程式的價值](foreword.md#values-of-public-code)。此外，他們也會審查貢獻是否遵循[標
準](#standards-to-follow)，且與整體作品有所連貫。

本專案使用 [GitFlow 分支與工作流程](https://nvie.com/posts/a-successful-git-branching-model/)。
當您對此儲存庫作分支以後，請務必依照 GitFlow 模型建立新功能分支。

將您所作的變更內容加入送交版次，[並附上內容說
明](https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message)。如果需要作
出多種類型的變更，請將相關變更依據邏輯分類，不同類型各自放在不同的送交版次中。例如：修正空白、以及文字內容更動，兩者應該放在不同的送交版次中。當新增檔案時，請選用
容易以「`diff` 」檢視的檔案格式，如「`.svg` 」格式就勝過二進位影像。在送交版次訊息中，請記錄您所作的選擇與決策，如此未來其他人都能知道您當時的抉
擇。

如果您是要新增程式碼，請確保您有新增與更新相關文件與測試項目，之後再提交您的拉取請求。請務必撰寫可以展示新增或修改後程式碼行為的測試項目。

#### 適用政策

就目前而言，《公共程式標準》並非在執行任何特定的公共政策。

#### 風格

《公共程式標準》目標[使用白話的英語](criteria/use-plain-english.md)，而拼字採用美式英文。文字內容基本上以每句一行為原則，沒有文繞圖
換行，來讓「`diff`」輸出更容易檢視。然而，我們想要強調更重要的是，您應該專注在貢獻內容上，而不是擔心拼字與排版。我們的審查流程會協助修正這一部分，也會另外再次檢查品質才[推出新發行版本](docs/releasing.md)。

#### 遵守的標準

這些是《公共程式標準》所採用的標準。請確保您的貢獻內容也遵守這些標準，才會更容易合併。

* [IETF RFC 2119](https://tools.ietf.org/html/rfc2119) - 要求等級關鍵字
* [網頁內容可近用無障礙指引 2.1](https://www.w3.org/TR/WCAG21/#readable) - 易讀性

### 2. 拉取請求

當您提出拉取請求時，請隨附描述您想要解決的問題，以及該拉取請求所能修正的議題編號。以一個拉取請求處理單一項議題為佳。若一組變動能同時解決多項議題，則請列出所有能一併
修正的議題編號。

### 3. 改善

所有貢獻都必須接受審查。Foundation for Public Code 致力於確保有維護人員能審查貢獻內容，目標是在兩個工作日內提供意見回饋。

維護人員有時候可以立即合併您的貢獻內容。不過一般來說，新的拉取請求通常需要再經過改善後，才能夠合併。其他貢獻者（或是輔助用機器人）可能會提供意見回饋。若是如此，負責
審查您貢獻內容的維護人員，將協助您改善文件與程式碼。

一旦您的文件與程式碼通過人工審查，就會合併。

### 4. 慶祝

您的構想、文件與程式碼，已成為本專案的一部份。您就是我們需要的開放原始碼英雄！

誠摯歡迎您提出拉取請求，將您的名字加到 [`AUTHORS`](AUTHORS.md) 檔案中，讓您所做的貢獻能銘記在本專案中。

## 翻譯成其他語言

《公共程式標準》沒有官方版本的翻譯，您仍可以協助本標準維護已有的[社群翻譯](https://github.com/publiccodenet/community-translations-standard)，或是新增翻譯。

## 發行版本

我們有提供[發行新版本](/docs/releasing.md)，與[訂購印刷版標準](/docs/printing.md)的專用詳細文件。

若要進一步瞭解如何使用，以及協助貢獻本專案，請參閱 [`README `](README.md)。
