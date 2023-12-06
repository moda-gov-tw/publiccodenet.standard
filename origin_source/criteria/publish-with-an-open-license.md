---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 13
redirect_from:
  - criteria/open-licenses
---
# 發行採用開放授權

An open and well known license makes it possible for anyone to see the [source code](../glossary.md#source-code) in order to understand how it works, to use it freely and to contribute to the [codebase](../glossary.md#codebase).
This enables a vendor ecosystem to emerge around the codebase.

Clearly indicating the license for each file within a codebase facilitates correct reuse and attribution of parts of a codebase.

## 需求規範

* All source code and documentation MUST be licensed such that it may be freely reusable, changeable and redistributable.
* Software source code MUST be licensed under an [OSI-approved or FSF Free/Libre license](https://spdx.org/licenses/).
* All source code MUST be published with a license file.
* Contributors MUST NOT be required to transfer copyright of their contributions to the codebase.
* All source code files in the codebase SHOULD include a copyright notice and a license header that are machine-readable.
* Having multiple licenses for different types of source code and documentation is OPTIONAL.

## 測試方式

* 確認代碼庫有清楚給予授權條款。
* 確認原始碼的授權條款有列於[經 OSI 開放原始碼促進會所批准，或由 FSF 自由軟體基金會所發表的自由授權條款清單](https://spdx.org/licenses/)，以及文件的授權條款有
[符合「開放定義」](https://opendefinition.org/licenses/)。
* 確認代碼庫中有包含其採用的授權條款檔案。
* 確認貢獻指南中，以及[儲存庫](../glossary.md#repository)的組態設定中，沒有求貢獻者轉讓著作權。
* 在代碼庫[持續整合](../glossary.md#continuous-integration)測試中，確認是否有檢查授權內容為機器可讀的檢查項目。

## Public policy makers: what you need to do

* Develop [policy](../glossary.md#policy) that requires source code to be [open source](../glossary.md#open-source).
* Develop policy that disincentivizes non-open source code and technology in procurement.

## Managers: what you need to do

* Only work with open source vendors that deliver their source code by publishing it under an open source license.
* Beware that even though [Creative Commons licenses](https://creativecommons.org/licenses/) are great for documentation, licenses that stipulate Non-Commercial or No Derivatives are NOT freely reusable, changeable and redistributable and don't fulfill these requirements.

## 開發人員與設計師：需要的工作

* Add a new `license` file to every new codebase created.
* Add a copyright notice and a license header to every new source code file created.
* When source code is being reused by the codebase, make sure that it has a license that is compatible with the license or licenses of the codebase.

<p style="page-break-after: always;"></p>

## 延伸閱讀

* 開放原始碼促進會所發表的《[開放原始碼定義](https://opensource.org/osd)》，所有開放原始碼授權條款皆符合這套定義。
* 紐西蘭CC Aotearoa《[創用CC介紹動畫影片](https://creativecommons.org/about/videos/creative-commons-kiwi)》。
* 歐洲自由軟體基金會所發表的《[REUSE 倡議規範](https://reuse.software/spec/)》提供規範明確、人類可讀以及機器可讀的著作權與授權資訊。
* Linux 基金會所發表的 [SPDX 授權條款清單](https://spdx.org/licenses/)提供經標準化、且機器可讀的大多數授權條款縮寫表示法。
