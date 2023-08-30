# The Standard for Public Code

<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS -->

The Standard for Public Code 提供公共組織一個準備開源解決方案的模型，讓他們與其他地方相似的公共組織合作。該標準包含給政策制定者、城市管
理者、開發人員與供應商的指引。

![version 0.7.1](assets/version-badge.svg) [![License:
CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![標準承
諾](assets/standard-for-public-code-commitment.svg)](#help-improve-this-standard)

[![頁面-建造-部
署](https://github.com/publiccodenet/standard/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/publiccodenet/standard/actions/workflows/pages/pages-build-deployment)
[![測
試](https://github.com/publiccodenet/standard/actions/workflows/test.yml/badge.svg)](https://github.com/publiccodenet/standard/actions/workflows/test.yml)
[![標準主徽
章](https://publiccodenet.github.io/publiccodenet-url-check/badges/standard.publiccode.net.svg)](https://publiccodenet.github.io/publiccodenet-url-check/standard.publiccode.net-url-check-look.json)
[![標準開發徽
章](https://publiccodenet.github.io/publiccodenet-url-check/badges/standard.publiccode.net-develop.svg)](https://publiccodenet.github.io/publiccodenet-url-check/standard.publiccode.net-develop-url-check-look.json)

The Standard for Public Code 目前為草稿階段。我們正在準備推出1.0版，目前正在幾個代碼庫上測試。

## 將 The Standard for Public Code 套用在您的代碼庫

如果您想要採用公共程式標準於您的代碼庫中，請隨意使用，它是一個開放標準與免費給任何人使用。如果您希望推廣代碼庫社群期望達成公共程式標準的資格，請使用 [公共程式標準
徽章](assets/standard-for-public-code-commitment.svg) 連結到此份承諾文件。了解您的代碼庫準備的如何，您可以透過
[快速自我檢測](https://publiccodenet.github.io/assessment-eligibility)粗略的瞭解您還需要準備多少才能符合
所有的資格。

將 The Standard for Public Code 套用在您的代碼庫上時，「應該」不用額外說明。若該標準中有任何不明確的地方，鼓勵您在此創建議題，讓我們能
夠協助您以及其他與您抱持同樣看法的民眾。如需靈感，請參閱[社群打造的實施指
南](https://publiccodenet.github.io/community-implementation-guide-standard/)，當中包括
範例與其他訣竅。

若新版的 The Standard for Public Code 有突破性的修改，The Foundation for Public Code 的代碼庫管理人員會
幫助The Standard for Public Code 使用者彌補不同版之間的差異。

若您想提交您的代碼庫，讓代碼庫能完全遵循此標準並且在未來能取得認證，請寫信與我們聯繫：
[info@publiccode.net](mailto:info@publiccode.net)，並開始正式[評
估](https://about.publiccode.net/activities/codebase-stewardship/lifecycle-diagram.html#assessment)。

## 徵求貢獻

我們相信公共政策與軟體應該具有包容、可用、開放、易讀、負責、易懂以及永續的特性。這代表我們需要以新的方式來設計、開發與採購原始碼以及政策註解。

本標準設定代碼庫品質水準，滿足公共組織、機構行政機關以及其他基礎設施服務的需求。

The Standard for Public Code 就在
[standard.publiccode.net](https://standard.publiccode.net/)。內容概覽請參閱
[`index.md`](index.md)。

[![The Standard for Public Code YouTube 影片縮圖：兩隻手中間放著一本印刷版 The Standard for Public
Code ](https://img.youtube.com/vi/QWt6vB-cipE/mqdefault.jpg)](https://www.youtube.com/watch?
v=QWt6vB-cipE)

[The Standard for Public Code 介紹影片](https://www.youtube.com/watch?v=QWt6vB-cipE)
from Creative Commons Global Summit 2020 (4:12) on YouTube.

## 幫忙改善本標準

The Foundation for Public Code 致力於維護與開發 The Standard for Public Code ，且品質也會符合該標準本身
的品質。

我們在找像您這樣的人對此專案提出[貢獻](CONTRIBUTING.md)，像是建議改善方向以及協助開發。😊若要開始，請先參閱我們的[貢獻者指
南](CONTRIBUTING.md)。由於這是相當核心的文件，我們僅接受能帶來非常大的價值的貢獻。[治理聲明](GOVERNANCE.md)提到我們管理該標準的
方式。

請注意，本專案有其[行為準則](CODE_OF_CONDUCT.md)。參加本專案代表您同意遵守該準則。請善待社群所有成員。

## 預覽、建造與部署

存放庫會上傳到部署於[standard.publiccode.net](https://standard.publiccode.net/)的靜態網站，使用的是
[GitHub pages](https://pages.github.com)與[Jekyll](https://jekyllrb.com/)。

當中內容格式就是要使用[Jekyll](http://jekyllrb.com/)來建構，換句話說您需要安裝ruby與ruby-bundler，像是：

```bash
sudo apt-get install -y ruby ruby-bundler
```

如果安裝了`ruby`與`bundle`，就可以執行`bundle install`，用 `script/serve.sh` 腳本來渲染網站。

### 測試

本標準包含許多測試腳本。`script/test-all.sh` 腳本則會開始執行所有本機測試。

所有腳本都在[腳本](https://github.com/publiccodenet/standard/tree/main/script)檔案夾。

### 生成 The Standard for Public Code PDF 檔案

除了 Jekyll 以外，要生成 PDF 檔案也需要仰賴[Weasyprint](https://weasyprint.org/)以及
[QPDF](https://github.com/qpdf/qpdf)。[Pandoc](https://pandoc.org/)可以將 PDF 轉換成
`.epub`檔案。

若要生成這些種類的檔案，則需要安裝類似下列的依附元件：

```bash
sudo apt-get install -y pandoc qpdf weasyprint
```

使用以下腳本，可以將 `standard-print.html` 檔案以及其他的版本檔案轉換成美觀的 PDF：

```bash
script/pdf.sh
```

## 授權

© [作者與貢獻者](AUTHORS.md)

The Standard for Public Code 採用 CC 0 [授權](LICENSE)，該授權也涵蓋所有圖解與註解。換句話說，任何人都可以任意使用這些
內容。如果您是貢獻者，您也將這些權利賦予他人。若要進一步瞭解如何幫助本專案，請參閱[貢獻指南](CONTRIBUTING.md)。
