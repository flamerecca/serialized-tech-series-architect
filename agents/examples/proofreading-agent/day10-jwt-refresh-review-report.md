# 範例：初稿 → 審查報告

延續 [writing-agent 範例](../writing-agent/day10-jwt-refresh-spec-to-draft.md) 的初稿與 [visual-agent 範例](../visual-agent/day10-jwt-refresh-diagram-to-mermaid.md) 的圖表，示範 `proofreading-agent` 怎麼依三份既定依據複核成品。

## 輸入：待審成品與三份既定依據（節錄）

- **待審成品**：[writing-agent 範例](../writing-agent/day10-jwt-refresh-spec-to-draft.md) 的初稿全文，含 [visual-agent 範例](../visual-agent/day10-jwt-refresh-diagram-to-mermaid.md) 產出的時序圖。
- **全域錨點檔案**：本篇為 fastapi-ecommerce-pro 第 10 天，已定案「續簽」作為 Token Refresh 的中文譯名。
- **風格指南**：直接了當的工程師對話口吻，禁用「值得注意的是」「不僅如此」等制式轉折語。
- **Section Spec**：來自 [planning-agent 範例](../planning-agent/day10-jwt-refresh-idea-to-spec.md) 的規格書，要求 Refresh Token 建議儲存位置為 HttpOnly Cookie。

## 輸出：審查報告

```markdown
# 雙重權杖簽發與自動過期刷新機制 審查報告

## 事實正確性
- 「用 Refresh Token 換發新 Access Token」段落：`/auth/refresh` 的程式碼用 `Cookie(...)` 讀取 Refresh Token，但全篇沒有任何地方示範簽發 Refresh Token 時呼叫 `response.set_cookie(...)`，查證 FastAPI 官方文件，`Cookie` 相依項只負責讀取既有 Cookie，`httponly`／`secure` 這些安全屬性必須在簽發端呼叫 `set_cookie` 時明確指定，缺少這段程式碼無法判斷是否真的做到規格要求的 HttpOnly Cookie 儲存。可自動判定成立：程式碼片段缺少 Refresh Token 簽發時的 `set_cookie` 呼叫。

## 可讀性與去 AI 腔調
- 全文未命中內建 AI 味防範清單的制式轉折語或空洞句型，段落開頭句型有交錯，沒有連續重複的起手式。

## 格式一致性
- Access Token／Refresh Token 對照表三欄位對齊與標點收尾一致。
- 結尾預告鉤子存在，且正確銜接 Day 11 主題，格式正確。

## 待使用者決策事項
- **Refresh Token 儲存位置的落差**：規格書要求 Refresh Token 存在 HttpOnly Cookie，但 `/auth/token` 的範例程式碼是把 `refresh_token` 直接放進 JSON 回應 body 裡回傳，並沒有透過 `Set-Cookie` 標頭寫入。這裡有兩種合理解讀：
  1. 範例程式碼本來就只示範核心的雙 Token 簽發與驗證邏輯，Cookie 簽發的細節留給讀者依規格書自行補上，不需要在教學文章裡展示每一行設定。
  2. 範例應該完整補上 `response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, secure=True)` 這類呼叫，否則讀者可能直接照抄「回傳 JSON 裡的 refresh_token」這個做法，跟規格書設計的安全考量產生落差。
```

## 這份範例示範了什麼

- **比對基準是既定依據，不是主觀品味**：抓到的落差是「規格書要求 HttpOnly Cookie」對照「程式碼實際回傳 JSON body」，比對來源是 Section Spec 這份既定文件，不是 `proofreading-agent` 自己覺得哪種寫法比較好。
- **HITL 判準的實際運作**：程式碼缺少 `set_cookie` 呼叫這件事本身可自動判定成立；但「該不該在教學文章裡展示完整 Cookie 設定」涉及主觀取捨，因此連同兩種合理解讀一併交給使用者決定，不是替使用者做決定。
- **只找問題、不動手改**：報告完全沒有動手改寫程式碼或正文，落差修正的執行權留給 `writing-agent` 依使用者的決策重新處理。
