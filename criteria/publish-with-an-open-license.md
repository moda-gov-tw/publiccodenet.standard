---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 13
redirect_from:
  - criteria/open-licenses
---

# 發行採用開放授權

採用開放且為人熟知的授權，讓任何人都可以查看[原始碼](../glossary.md#source-code)，使其能瞭解運作方式、自由使用，並且能為[程式基底](../glossary.md#codebase)做出貢獻。這也能促進供應商建立出以程式基底為中心的生態系。

明確指出程式基底中每一個檔案的授權，讓使用者能正確重複利用程式基底的部分內容，並表彰作者名稱。

## 需求規定

* 所有原始碼與文件，皆「必須」採用使其得以自由重複使用、自由修改、自由再次散布的授權條款。
* 軟體原始碼「必須」採用[經 OSI 開放原始碼促進會所批准，或由 FSF 自由軟體基金會所發表的自由授權條款](https://spdx.org/licenses/)。
* 所有原始碼皆「必須」搭配授權條款檔案一併發行。
* 「禁止」要求貢獻者將其貢獻的程式碼著作權轉讓給程式基底。
* 程式基底中所有原始碼檔案，皆「應該」包含機器可讀的著作權聲明與授權條款標頭內容。
* 「可選擇」是否為不同類型的原始碼與文件採用多重授權條款。

## 測試方式

* 確認程式基底有清楚給予授權條款。
* 確認原始碼的授權條款有列於[經 OSI 開放原始碼促進會所批准，或由 FSF 自由軟體基金會所發表的自由授權條款清單](https://spdx.org/licenses/)，以及文件的授權條款有[符合「開放定義」](https://opendefinition.org/licenses/)。
* 確認程式基底中有包含其採用的授權條款檔案。
* 確認貢獻指引中，以及[儲存庫](../glossary.md#repository)的組態設定中，沒有要求貢獻者轉讓著作權。
* 在程式基底[持續整合](../glossary.md#continuous-integration)測試中，確認是否有檢查授權內容為機器可讀的檢查項目。

## 公共政策制定者：需要的工作

* 制定要求原始碼必須採用[開放原始碼](../glossary.md#open-source)授權的[政策](../glossary.md#policy)。
* 制定抑制採購非開放原始碼授權程式碼，與非開放科技的政策。

## 管理人員：需要的工作

* 只與能採用開放原始碼授權交付、與發行其原始碼的開放原始碼軟體供應商合作。
* 請注意，雖然[創用CC授權](https://creativecommons.org/licenses/)適合用於文件作品，但其中指明「非商業性」或「禁止改作」
的授權條款，代表「無法」自由重複使用、自由修改、自由再次散布等，因此未能符合規定。

## 開發人員與設計師：需要的工作

* 每當建立新的程式基底時，都要加入新的「`license`」授權條款檔案。
* 每當建立新的原始碼檔案時，都要加入著作權聲明與授權條款標頭內容。
* 每當程式基底重複利用原始碼時，都要確認原始碼的授權與程式基底的授權相容。

<p style="page-break-after: always;"></p>

## 延伸閱讀

* 開放原始碼促進會所發表的《[開放原始碼定義](https://opensource.org/osd)》，所有開放原始碼授權條款皆符合這套定義。
* 紐西蘭CC Aotearoa《[創用CC介紹動畫影片](https://creativecommons.org/about/videos/creative-commons-kiwi)》。
* 歐洲自由軟體基金會所發表的《[REUSE 倡議規範](https://reuse.software/spec/)》，提供規範明確、人類可讀以及機器可讀的著作權與
授權資訊。
* Linux 基金會所發表的 [SPDX 授權條款清單](https://spdx.org/licenses/)，提供經標準化、且機器可讀的大多數授權條款縮寫表示
法。
