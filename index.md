---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2022 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
toc: false
---
# 政府開源協作指引

The Standard for Public Code 當中的標準，支持公共組織合作開發與維護軟體及政策。

The Standard for Public Code 指引正在建構自己開源解決方案的公共組織，方便他們未來能跟其他地區的類似公部門組織合作，並讓這些組織能重複利
用前述開源解決方案。The Standard for Public Code 提供建議給政策制定者、政府管理人員、開發人員與供應商。不同人士可透過The
Standard for Public Code ，合作建立可用、開放、易讀、負責且永續的代碼庫。The Standard for Public Code 適用於
各政府層級的代碼庫，從超國家到市政府。

The Standard for Public Code 將‘[公共程式](glossary.md#public-code)’定義為由公共組織所開發的開源軟體，並且
遵照相關政策與指引，方便協作與重複利用。

The Standard for Public Code 當中的標準符合開源軟體開發的指引與最佳實務。

{% for page in site.pages %}{% if page.name == "foreword.md" %} 額外情境與背景資訊請參閱
[序](foreword.md). {% endif%}{% endfor %}

## 目錄

* [讀者指南：如何詮釋此標準](readers-guide.md)
* [詞彙表](glossary.md)
* [標準](criteria/){% assign sorted = site.pages | sort:"order" %}{% for page in
sorted %}{% if page.dir == "/criteria/" %}{% if page.name != "index.md" %}{%
if page.title %}
   * [{{page.title}}]({{page.url}}){% endif%}{% endif%}{% endif%}{% endfor %}
* [作者群](AUTHORS.md)
* [貢獻指引](CONTRIBUTING.md)
* [行為準則](CODE_OF_CONDUCT.md)
* [治理](GOVERNANCE.md)
* [版本歷史](CHANGELOG.md)
* [授權](license.html)

## 社群會議

我們通常在每月第一個週四的 15:00 (CET/CEST) 舉辦社群會議。 [議
程](https://write.publiccode.net/pads/Community-Call-Standard-for-Public-Code) 在會議
前約一週的時間更新。您可以 [報
名](https://odoo.publiccode.net/survey/start/594b9243-c7e5-4bc1-8714-35137c971842)，
之後舉辦會議時會寄送邀情函給您。

## 其他資源

* [The Standard for Public Code 社群其他語
言](https://publiccodenet.github.io/community-translations-standard/) 非官方翻譯版
* 公部門開源代碼庫的 [標準遵循自我評估](https://publiccodenet.github.io/assessment-eligibility/)
* [標準資格檢查清單](/docs/review-template.html) 由公共程式基金會管理人員用於代碼庫審查
