# 發行新版本的 The Standard for Public Code

<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- SPDX-FileCopyrightText: 2021-2023 The Foundation for Public Code <info@publiccode.net>, https://standard.publiccode.net/AUTHORS -->

1. 審查「develop」分支狀態
   - 確保該版本的內容都已經完成合併
   - 請人校對目前的分支狀態
      - 如果有另外加入破折號，檢查是否能簡化文字並且移除破折號，改用較簡易的句子。如果需要複雜的句子，檢查是否能用其他符號來取代破折號。如果破折號最適合用來表達該句子的
涵義，請遵守[芝加哥格式手冊](https://en.wikipedia.org/wiki/Dash#En_dash_versus_em_dash)。

1. 建立發佈分支
   - 從 'develop'、`git switch -c "release-$MAJOR.$MINOR.$PATCH"`
   - 推動分支，`git push -u origin release-$MAJOR.$MINOR.$PATCH`

1. 更新新版本
   - [ ] 在[`AUTHORS.md`](../AUTHORS.md)加入新貢獻者資料
   - [ ] 更新[`CHANGELOG.md`](../CHANGELOG.md)
   - [ ] 更新 [`roadmap.md`](roadmap.md)
   - [ ] 在 diff 進行額外傳輸到 'main' 分支
      - 執行 `script/generate-review-template.sh` 與提交更新紀錄 `docs/review-template.html`
      - 使用審查範本的新文字更新 `docs/standard-for-public-code.html`，根據結果更新任何狀態
      - 重新檢查用字有變更的任何段落，確保變更的字詞適合該整體段落，並且沒有文法或拼字錯誤
      - 確保安裝[字體](https://brand.publiccode.net/typography/)，請參閱：`script/ensure-font.sh`
      - 使用 `script/pdf.sh rc1` 檢視渲染的 `.pdf`
         - 確保沒有連結相衝的問題
         - 移除或新增分頁符號 CSS 來檢查分頁符號，像是：`<p style="page-break-after: always;"></p>`
      - 若需要，進行修復並且重複進行額外傳輸
   - [ ] 推送分支，與 `main` 分支比較，如：
`https://github.com/publiccodenet/standard/compare/main...release-$MAJOR.$MINOR.$PATCH`
      - 要求多位審查人員（特別是校對人員）進行審查
      - 審查人員若有發現不會影響發行的缺失，則會建立議題
      - 如果是發行所需，審查人員可以建立拉入請求來解決問題
      - 若額外的拉入請求合併至發行分支，請要求重新審查
   - [ ] 執行「to-archive-org.sh」腳本

1. 在 GItHub 上發行，並且附上發行說明與版本號碼
   - [ ] `git tag trigger-$MAJOR.$MINOR.$PATCH`
   - [ ] `git push --tags` (see: `../.github/workflows/release-on-tag.yml`)
   - [ ] 移除本地端的標籤（tag）：`git tag -d trigger-$MAJOR.$MINOR.$PATCH`

1. [將印刷檔案傳送至印刷廠](printing.md)
   - [ ] 封面檔案
   - [ ] 內頁 PDF

1. 標記[翻譯](https://github.com/publiccodenet/community-translations-standard)貢獻者
