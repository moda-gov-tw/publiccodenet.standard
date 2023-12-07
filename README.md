# 公共程式標準

<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS -->

《公共程式標準》提供公家機關一套準備開放原始碼解決方案的模型，讓他們能與其他地方相似的公家機關協作。該標準包含給政策制定者、市行政官、開發人員與供應商的指引。

![version 0.7.1](assets/version-badge.svg) [![License:
CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![標準承
諾](assets/standard-for-public-code-commitment.svg)](#help-improve-this-standard)

[![pages-build-deployment](https://github.com/publiccodenet/standard/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/publiccodenet/standard/actions/workflows/pages/pages-build-deployment)
[![測
試](https://github.com/publiccodenet/standard/actions/workflows/test.yml/badge.svg)](https://github.com/publiccodenet/standard/actions/workflows/test.yml)
[![standard main
badge](https://publiccodenet.github.io/publiccodenet-url-check/badges/standard.publiccode.net.svg)](https://publiccodenet.github.io/publiccodenet-url-check/standard.publiccode.net-url-check-look.json)
[![standard develop
badge](https://publiccodenet.github.io/publiccodenet-url-check/badges/standard.publiccode.net-develop.svg)](https://publiccodenet.github.io/publiccodenet-url-check/standard.publiccode.net-develop-url-check-look.json)

《公共程式標準》目前為草稿階段。我們正在準備發行 1.0 版，目前仍在幾個程式基底中作測試。

## 將《公共程式標準》套用到您的程式基底

若您想要將《公共程式標準》套用您的程式基底，就請放心去做，因為它是人人都能自由採用的開放標準。如果您希望宣傳程式基底社群達成《公共程式標準》準則要求時的熱誠，請使
用 [standard-for-public-code-commitment 徽章](assets/standard-for-public-code-commitment.svg)連結到這份承諾文件。若要瞭解您程式基底所達成的程度，可以做[自我資格評估](https://publiccodenet.github.io/assessment-eligibility)；它能幫助您大略瞭解，如果想要滿足所有
準則，還需要下多少功夫。

本標準 *應該* 足以自我解釋要如何套用到您的程式基底中。若標準中有任何不明確的地方，我們鼓勵您在此開立議題，來讓我們能協助您以及其他與您抱持同樣看法的人。如果需要
一點靈感啟發，請參閱[社群製作的《實踐指引》](https://publiccodenet.github.io/community-implementation-guide-standard/)，其中包
括範例與其他提示。

若新版的《公共程式標準》有任何導致過去作法不再適用的改動，則 Foundation for Public Code 的程式基底執事人員，會協助標準的實踐者理解該如何
銜接之間的落差。

若您致力讓您的程式基底完全遵循此標準，並想在未來能取得認證，請寫信與我們聯繫：
[info@publiccode.net](mailto:info@publiccode.net)，以展開正式[評
估](https://about.publiccode.net/activities/codebase-stewardship/lifecycle-diagram.html#assessment)。

## 徵求貢獻

我們相信公共政策與公共軟體，應該具備涵容、好用、開放、易懂、課責、近用、永續等特質。這代表我們需要一種新的方式，來設計、開發，以及付出心力育成原始碼和政策文件。

本標準為程式基底設立品質檢核水準，使其能滿足公家機關、社會機構、行政單位，以及其他重大基礎設施服務的需求。

本標準放在線上：[standard.publiccode.net](https://standard.publiccode.net/)。請參閱
[`index.md`](index.md) 查看整體內容概覽。

[![《公共程式標準》的影片縮圖：兩隻手中間放著本標準的印刷
本](https://img.youtube.com/vi/QWt6vB-cipE/mqdefault.jpg)](https://www.youtube.com/watch?
v=QWt6vB-cipE)

[《公共程式標準》的影片介紹](https://www.youtube.com/watch?v=QWt6vB-cipE)，出自 Creative Commons
Global Summit 2020 (4:12)，放在 YouTube 上。

## 幫忙改善這份標準

Foundation for Public Code 致力於維護與開發《公共程式標準》，且使其同時符合該標準自身的品質水準。

我們正在尋找像您這樣的人，能對此專案做出[貢獻](CONTRIBUTING.md)，像是建議改善方向，以及協助開發等。😊若要開始，請先參閱我們的[貢獻者指
引](CONTRIBUTING.md)。由於這是相當核心的文件，我們僅接受能帶來重大價值的貢獻。[治理方式聲明](GOVERNANCE.md)中有說明管理該標準的
方式。

請注意，本專案配合[行為守則](CODE_OF_CONDUCT.md)一同發行。如果要參加本專案，代表您同意遵守守則。請善待社群的所有其他成員。

## 預覽、建置、部署

儲存庫會建置一個靜態網站，並部署至 [standard.publiccode.net](https://standard.publiccode.net/)。網站採
用 [GitHub 頁面](https://pages.github.com) 與 [Jekyll](https://jekyllrb.com/) 技術。

網站內容透過 [Jekyll](http://jekyllrb.com/) 技術建置。這代表您需要有安裝 ruby 與 ruby-bundler，例如：

```bash
sudo apt-get install -y ruby ruby-bundler
```

一旦安裝好 `ruby` 與 `bundle` 後，就可以執行 `bundle install`，接著再利用 `script/serve.sh` 命令稿轉譯呈現出網
站成果。

### 測試

本專案內含許多測試命令稿。其中 `script/test-all.sh` 命令稿則統包執行所有本機測試。

請前往 [script](https://github.com/publiccodenet/standard/tree/main/script) 資料夾查看命令
稿。

### 生成《公共程式標準》的 PDF 檔案

除了先前提到的 Jekyll 以外，想生成 PDF 檔，還需要依賴 [Weasyprint](https://weasyprint.org/) 和
[QPDF](https://github.com/qpdf/qpdf)。[Pandoc](https://pandoc.org/) 則可將 PDF 檔轉換成
`.epub` 檔。

若要生成這類檔案，則應該要安裝依賴的軟體項目，例如：

```bash
sudo apt-get install -y pandoc qpdf weasyprint
```

使用以下命令稿，可以將 `standard-print.html` 檔案轉換成美觀的 PDF 檔，同時包括其他發行用的檔案：

```bash
script/pdf.sh
```

## 授權

© [作者與貢獻者](AUTHORS.md)

本標準採用 CC0 公眾領域貢獻宣告[給予授權](LICENSE)，該授權範圍涵蓋所有插圖與文件。CC0 代表任何人都能任意使用這些內容。如果您是貢獻者，代表您也將
這些權利賦予他人。若要進一步瞭解如何協助本專案，請參閱〈[貢獻指引](CONTRIBUTING.md)〉。

## 軟體中文化

本專案為數位部開放原始碼軟體中文化專案項目之一，其中文化與專案應用可參考 [Wiki](https://github.com/moda-gov-tw/publiccodenet.standard/wiki)。
