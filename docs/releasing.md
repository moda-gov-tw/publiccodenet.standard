# 發行新版本的《公共程式標準》

<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- SPDX-FileCopyrightText: 2021-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS -->

1. 審查「develop」分支的狀態
   - 確認預計收入該次發行版的所有變更都已完成合併
   - 邀請校對該分支目前的狀態
      - 如果有引入新的破折號，檢查是否能簡化文字並且移除破折號，例如改用較簡易的句子。如果需要用到複雜的句子，檢查是否能用其他標點符號來取代破折號。如果破折號最適合用來
表達該句子的涵義，則請遵守《[芝加哥格式手
冊](https://en.wikipedia.org/wiki/Dash#En_dash_versus_em_dash)》的規範。

1. 建立發行用分支
   - 從「develop」分支下命令，`git switch -c "release-$MAJOR.$MINOR.$PATCH"`
   - 推送分支，`git push -u origin release-$MAJOR.$MINOR.$PATCH`

1. 更新本次新發行
   - [ ] 在 [`AUTHORS.md`](../AUTHORS.md) 中加入新貢獻者的資料
   - [ ] 更新 [`CHANGELOG.md`](../CHANGELOG.md)
   - [ ] 更新 [`roadmap.md`](roadmap.md)
   - [ ] 透過 diff 進行額外傳輸到「main」分支
      - 執行 `script/generate-review-template.sh` 並送交更新後的 `docs/review-template.html` 版次記
錄
      - 使用審查範本中的新文字來更新 `docs/standard-for-public-code.html`，會將任何狀態變更作為結果更新
      - 重新檢查用字有變更的任何小節或段落，確保變更的字詞適合該整體內容，並且沒有文法或拼字錯誤
      - 確認有安裝[字型](https://brand.publiccode.net/typography/)，請參見：`script/ensure-font.sh`
      - 使用 `script/pdf.sh rc1` 檢查轉譯出的 `.pdf` 檔
         - 確認沒有連結相衝的問題
         - 檢查文字分頁之處，可能需要移除或新增 CSS 分頁語法，像是：`<p style="page-break-after: always;"></p>`
      - 如果有需要，送交修正版次，並重複進行額外傳輸
   - [ ] 推送分支，與「main」分支比較，範例：
`https://github.com/publiccodenet/standard/compare/main...release-$MAJOR.$MINOR.$PATCH`
      - 請多位審查人員（特別是校對人員）進行審查
      - 審查人員若發現不會阻礙發行的缺失，則會建立議題
      - 如果是發行所需處理的缺失，審查人員可以提交拉取請求來解決問題
      - 若有額外的拉取請求合併至發行分支，則再次請求審查
   - [ ] 執行 to-archive-org.sh 命令稿

1. 在 GItHub 上發行，附上發行備註與版本編號
   - [ ] `git tag trigger-$MAJOR.$MINOR.$PATCH`
   - [ ] `git push --tags`（請參見：`../.github/workflows/release-on-tag.yml`）
   - [ ] 移除本地端的 tag 標記：`git tag -d trigger-$MAJOR.$MINOR.$PATCH`

1. [將檔案傳送給印刷廠商印刷](printing.md)
   - [ ] 封面檔案
   - [ ] 內頁 PDF

1. 通知[翻譯](https://github.com/publiccodenet/community-translations-standard)貢獻者
