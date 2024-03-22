---
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2019-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS
order: 16
redirect_from:
    - criteria/advertise-maturity
    - criteria/document-maturity
---
# 記錄程式基底成熟度

清楚標示[程式基底](../glossary.md#codebase)的成熟度，有助於他人決定是否要使用，或為該程式基底做出貢獻。程式基底版本的成熟度，包含其依賴項
目的成熟度。瞭解程式基底演進到什麼程度，是理解該程式基底並知道如何做出貢獻的關鍵。

## 需求規定

* 程式基底「必須」註明版本編號。
* 程式基底「必須」明確以文件記錄，是否有已經準備好可供使用的版本。
* 準備好可供使用的程式基底版本，「必須」只能依賴其他也已經準備好可供使用的程式基底版本。
* 程式基底「應該」包含每次版本的變動紀錄，像是以「`CHANGELOG`」日誌格式檔記錄。
* 「應該」要以文件記錄分配版本識別碼的方法。
* 「可選擇」是否採用語意化版本控制編號。

## 測試方式

* 確認程式基底有版本編號策略，且有文件記載該策略。
* 確認政策制定者、管理人員、開發人員與設計師等，都能清楚知道程式基底是否有準備好可供使用的版本。
* 確認準備好可供使用的程式基底版本，並不依賴任何尚未準備好可供使用的其他程式基底的版本。
* 確認有文件記錄程式基底的版本編號方法，並且確實遵守。
* 確認是否有版本的變動紀錄。

## 公共政策制定者：需要的工作

* 制定[政策](../glossary.md#policy)時，請記住任何開發出來的[原始碼](../glossary.md#source-code)都必須先經過
測試與改善，才能夠投入服務。
* 考慮將政策的變動註明版本編號，尤其是因而觸發新版本原始碼開發的情況。

## 管理人員：需要的工作

* 要確認服務依賴的程式基底版本成熟度，等同或高於該服務本身。舉例來說，正式上線的服務不要使用 beta 公測版程式基底。

## 開發人員與設計師：需要的工作

* 確認所有發行版，都有遵守程式基底的版本控制編號作法。

## 延伸閱讀

* 許多程式基底使用「[語意化版本編號規範](https://semver.org/)」來標示版本。
* [軟體發行生命週期](https://en.wikipedia.org/wiki/Software_release_life_cycle)
* 澳洲數位轉型局《[服務設計與交付流程](https://www.dta.gov.au/help-and-advice/build-and-improve-services/service-design-and-delivery-process)》。
* 英國政府數位服務團《[敏捷交付服務手冊](https://www.gov.uk/service-manual/agile-delivery)》。
