---
order: 16
redirect_from:
    - criteria/advertise-maturity
---
# 紀錄代碼庫成熟度

<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- written in 2019 - 2022 by The Foundation for Public Code <info@publiccode.net> -->

## 需求規範

* [代碼庫](../glossary.md#codebase)必須註明版本編號。
* 準備好可供使用的代碼庫，必須只能依賴其他也已經準備好可供使用的代碼庫。
* 尚未準備好使用的代碼庫，必須有所列標籤之一：prototype、alpha、beta、pre-release 等版本進度。
* 代碼庫應該包含每次版本的變動紀錄，像是以「`CHANGELOG`」日誌格式檔記錄。

## 此措施為何重要

清楚標示代碼庫的成熟度，有助於他人決定是否要重複使用、投資，或為該代碼庫做出貢獻。

## 此措施辦不到的事

* 保證他人會來使用[程式碼](../glossary.md#code)。

## 測試方式

* 確認代碼庫有版本編號策略，且有文件記載該策略。
* 確認有清楚表明最新版的取得位置。
* 確認代碼庫不依賴其他成熟度標示較低的任何代碼庫。
* 確認代碼庫是已準備好可供使用，還是仍標示為 prototype、alpha、beta、pre-release 等開發中版本。
* 檢查是否有變更紀錄。

## 政策制定者：需要的工作

* 制定[政策](../glossary.md#policy)時，請記住任何開發出來的程式碼都必須先經過測試與改善，才能夠投入服務。
* 考慮將政策的變動註明版本編號，尤其是因而觸發開發新版本原始碼的情況。

## 管理人員：需要的工作

* 要確認服務依賴的代碼庫成熟度等同或高於服務本身。舉例來說，正式上線的服務不要使用 beta 公測版代碼庫，公測版服務不要使用 prototype
原型代碼庫。
* 若代碼庫尚未準備好供一般使用，請與開發人員一起確保該代碼庫是否有標示適當標籤：
   * prototype：原型概念，測試外觀與感覺體驗，並且從內部證明技術的可行性概念，
   * alpha：內部測試，在限制的一群使用者中進行引導性測試，
   * beta：公開測試，讓更多[一般大眾](../glossary.md#general-public)參與測試，例如測試代碼庫在大規模操作下是否仍能運作，
   * pre-release：準發行版，已經準備好發行，但尚未獲得正式批准的程式碼。

## 開發人員與設計師：需要的工作

* 在每個指示程式碼成熟度的介面中加上明顯的標頭。
* 所有正式發行的程式碼都要有版本編號。
* 特別是在採用「滾動發行」的情況下，程式碼的版本資訊可以根據[版本控制](../glossary.md#version-control)系統的中介資料自動衍生（例如使用
[git describe](https://git-scm.com/docs/git-describe)）。

## 延伸閱讀

* 澳洲數位轉型局《[服務設計與交付流程](https://www.dta.gov.au/help-and-advice/build-and-improve-services/service-design-and-delivery-process)》。
* 英國政府數位服務團《[敏捷交付服務手冊](https://www.gov.uk/service-manual/agile-delivery)》。
* 許多代碼庫使用「[語意化版本控制規範](https://semver.org/)」來標示版本。
* 英國政府數位服務團《[什麼是服務開發當中的探索、Alpha、Beta、上線階段？ [影片 0'0"59]](https://www.youtube.com/watch?v=_cyI7DMhgYc)》。
