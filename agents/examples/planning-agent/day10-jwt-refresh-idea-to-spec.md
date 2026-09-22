# 範例：靈感筆記 → 寫作規格書

這份範例延續 [complete-30-day-fastapi-mastery-series-plan.md](../../../skills/serialized-tech-series-architect/examples/complete-30-day-fastapi-mastery-series-plan.md) 裡的 Day 10，示範 `planning-agent` 怎麼把一句簡短的靈感筆記，拆解成 `writing-agent` 可以直接使用的寫作規格書。

## 輸入：靈感筆記

> 今天要寫 Day 10：雙重權杖簽發與自動過期刷新機制。Access Token 15 分鐘、Refresh Token 7 天，昨天 Day 09 已經做完密碼雜湊與註冊登入，讀者應該已經有一組能登入的帳號。

## 輸出：寫作規格書

```markdown
---
title: 雙重權杖簽發與自動過期刷新機制
target_reader: 已完成 Day 09 使用者註冊登入、正在用 FastAPI 開發 fastapi-ecommerce-pro 的中階工程師
pain_point: Access Token 過期後，前端只能強迫使用者重新登入，體驗中斷；直接延長 Token 效期又犧牲安全性
source_note: "[[Day 10 靈感筆記：雙重權杖與自動刷新]]"
status: draft-spec
---

# 雙重權杖簽發與自動過期刷新機制 寫作規格書

## 目標讀者與痛點
讀者已經會用 bcrypt 雜湊密碼、完成基本註冊登入，但還沒處理過 Token 過期後的續簽機制，痛點是 Access Token 過期只能強迫使用者重新輸入帳密。

## 必要規格元件
- 場景鋪陳: 使用者在結帳頁填完信用卡資料，Access Token 剛好過期，整頁資料被登出清空的真實場景
- 程式碼要求:
  - FastAPI + PyJWT: 示範 `/auth/token` 同時簽發 Access Token（15 分鐘）與 Refresh Token（7 天），以及 `/auth/refresh` 驗證 Refresh Token 並換發新 Access Token
- 對比或表格要求: Access Token 與 Refresh Token 的效期、建議儲存位置、外洩風險三欄對照表
- 視覺元素要求: 一張時序圖，呈現 Access Token 過期 → 前端呼叫 `/auth/refresh` → 換發新 Token → 前端重打原請求的完整流程

規劃備註：本篇需正式定案「續簽」一詞作為 Token Refresh 的中文譯名，後續系列一律沿用；這句屬於編輯協作用元資訊，不得出現在 `key_points` 或任何會被直接轉寫為讀者可見文字的欄位中。

## 參考素材
- [[Day 09 密碼學安全雜湊與用戶註冊登入]]

## 給 Writing Agent 的備註
讀者已經看過 Day 09 的註冊登入流程，這篇不需要重講密碼雜湊機制，直接從「使用者已登入、拿到第一組 Token」的狀態切入。
```

## 這份範例示範了什麼

- **產出優先思維**：規格書先鎖定「Access Token 過期造成的結帳中斷」這個具體痛點，再往下反推需要哪些程式碼與圖表，不是先蒐集 JWT 相關資料再拼湊。
- **規劃備註的隱藏用途**：「續簽」一詞的定案宣告只出現在「規劃備註」，不會流入 `writing-agent` 產出的正文，讀者不會看到「這個詞從今天開始定案」這種編輯協作用的內部宣告。
- **已解鎖知識的銜接**：透過「參考素材」點名 Day 09，讓 `writing-agent` 知道密碼雜湊已經講過，可以直接跳過。
