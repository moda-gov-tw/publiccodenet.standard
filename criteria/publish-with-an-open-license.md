---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 13
redirect_from:
  - criteria/open-licenses
---
# 發行採用開放授權

有了開放且熟為人知的授權，任何人都可以看到[原始碼](../glossary.md#source-code)、認識其運作方式、任意使用原始碼，並且貢獻給[代碼
庫](../glossary.md#codebase)。這也讓供應商能建立以代碼庫為中心的生態系。

明確標示代碼庫中每一個檔案的授權，幫助使用者正確重複利用與引用代碼庫的內容。

## 規定

* 所有程式碼與文件，皆必須採用使其得以自由重複使用、自由修改、自由再次散布的授權條款。
* 軟體原始碼必須採用[經 OSI 開放原始碼促進會所批准，或由 FSF 自由軟體基金會所發表的自由授權條
款](https://spdx.org/licenses/)。
* 所有程式碼皆必須搭配授權條款檔案一併發行。
* 不得要求貢獻者將其貢獻的程式碼著作權轉讓給代碼庫。
* 代碼庫中所有原始碼檔案，皆應該包含機器可讀的著作權聲明與授權條款標頭內容。
* 可選擇是否為不同類型的原始碼與文件採用多重授權條款。

## 測試方式

* 確認代碼庫有清楚給予授權條款。
* 確認原始碼的授權條款有列於[經 OSI 開放原始碼促進會所批准，或由 FSF 自由軟體基金會所發表的自由授權條款清
單](https://spdx.org/licenses/)，以及文件的授權條款有[符合「開放定
義」](https://opendefinition.org/licenses/)。
* 確認代碼庫中有包含其採用的授權條款檔案。
* 確認貢獻指南中，以及[儲存庫](../glossary.md#repository)的組態設定中，沒有求貢獻者轉讓著作權。
* 在代碼庫[持續整合](../glossary.md#continuous-integration)測試中，確認是否有檢查授權內容為機器可讀的檢查項目。

## 公共政策制定者：您的責任

* 制定要求原始碼必須採用[開放原始碼](../glossary.md#open-source)授權的[政策](../glossary.md#policy)。
* 制定抑制採購非開放原始碼授權程式碼與非開放科技的政策。

## 管理人員：您的義務

* 只與能採用開放原始碼授權交付與發行其原始碼的開放原始碼軟體供應商合作。
* 請注意，雖然[創用CC授權](https://creativecommons.org/licenses/)適合用於文件作品，但其中指明「非商業性」或「禁止改作」
的授權條款，代表「無法」自由重複使用、自由修改、自由再次散布等，因此未能符合規定。

## 開發人員與設計師：您的責任

* 每當建立新的代碼庫時，都要加入新的「`license`」授權條款檔案。
* 每當建立新的原始碼檔案時，都要加入著作權聲明與授權條款標頭內容。
* 代碼庫重複利用原始碼時，確認原始碼的授權與代碼庫的授權相容。

<p style="page-break-after: always;"></p>
## Further reading

* 開放原始碼促進會所發表的《[開放原始碼定義](https://opensource.org/osd)》，所有開放原始碼授權條款皆符合這套定義。
* 紐西蘭 CC Aotearoa《[創用CC介紹動畫影
片](https://creativecommons.org/about/videos/creative-commons-kiwi)》。
* 歐洲自由軟體基金會所發表的《[REUSE 倡議規範](https://reuse.software/spec/)》提供規範明確、人類可讀以及機器可讀的著作權與授
權資訊。
* Linux 基金會所發表的 [SPDX 授權條款清單](https://spdx.org/licenses/)提供經標準化、且機器可讀的大多數授權條款縮寫表示
法。
