---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 16
redirect_from:
    - criteria/advertise-maturity
    - criteria/document-maturity
---
# 記錄代碼庫成熟度

清楚標示[代碼庫](../glossary.md#codebase)的成熟度，有助於他人決定是否要使用或為該代碼庫做出貢獻。代碼庫成熟度包括其依附元件的成熟度。瞭解
代碼庫的演變，才能真正認識該代碼庫並且做出貢獻。

## 規定

* 代碼庫必須註明版本編號。
* 代碼庫必須明確標示是否有已經準備好使用的版本。
* 準備好可供使用的代碼庫版本，必須只能依賴其他也已經準備好可供使用的代碼庫版本。
* 代碼庫應該包含每次版本的變動紀錄，像是以「`CHANGELOG`」日誌格式檔記錄。
* 應該有文件記錄分配版本識別碼的方式。
* 可選擇是否使用語意化版本控制。

## 測試方式

* 確認代碼庫有版本編號策略，且有文件記載該策略。
* 確認政策制定者、管理人員、開發人員與設計師都相當清楚代碼庫是否有準備好可供使用的版本。
* 確認準備好可供使用的代碼庫版本，並不依賴尚未準備好可供使用的其他代碼庫的任何版本。
* 確認有記錄並遵守代碼庫的版本控制方式。
* 確認是否有版本的變動紀錄。

## 公共政策制定者：您的責任

* 制定[政策](../glossary.md#policy)時，請記住任何開發出來的 [程式碼](../glossary.md#source-code) 都必須先
經過測試與改善，才能夠投入服務。
* 考慮將政策的變動註明版本編號，尤其是因而觸發開發新版本原始碼的情況。

## 管理人員：您的義務

* 要確認服務依賴的代碼庫成熟度等同或高於服務本身。舉例來說，正式上線的服務不要使用 beta 公測版代碼庫。

## 開發人員與設計師：您的責任

* 確認所有發行都遵守代碼庫版本控制方式。

## 延伸閱讀

* 許多代碼庫使用「[語意化版本控制規範](https://semver.org/)」來標示版本。
* [軟體發行生命週期](https://en.wikipedia.org/wiki/Software_release_life_cycle)
* 澳洲數位轉型局《[服務設計與交付流
程](https://www.dta.gov.au/help-and-advice/build-and-improve-services/service-design-and-delivery-process)》。
* 英國政府數位服務團《[敏捷交付服務手冊](https://www.gov.uk/service-manual/agile-delivery)》。
