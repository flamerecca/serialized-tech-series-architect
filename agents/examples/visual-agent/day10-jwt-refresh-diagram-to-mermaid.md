# 範例：圖表佔位符 → Mermaid 架構圖

延續 [writing-agent 範例](../writing-agent/day10-jwt-refresh-spec-to-draft.md) 產出的初稿，示範 `visual-agent` 怎麼把正文裡的圖表佔位符轉譯成實際圖表。

## 輸入：圖表佔位符（節錄自 writing-agent 產出的初稿）

```
<!-- 圖表佔位：呈現「Access Token 過期」→「前端呼叫 /auth/refresh」→「後端驗證 Refresh Token」→「換發新 Access Token」→「前端重打原請求」這五個步驟的時序圖，節點之間是單向依序流動，沒有分支 -->
```

## 輸出：視覺產出

```markdown
## 視覺產出：用 Refresh Token 換發新 Access Token

**類型**：架構圖
**來源佔位符**：
> 呈現「Access Token 過期」→「前端呼叫 /auth/refresh」→「後端驗證 Refresh Token」→「換發新 Access Token」→「前端重打原請求」這五個步驟的時序圖，節點之間是單向依序流動，沒有分支

**判斷依據**：佔位描述點出五個明確節點，且節點之間是單向先後關係，屬於流程結構而非數量關係，適合轉譯成架構圖。
**轉譯輸入**：Access Token 過期、前端呼叫 /auth/refresh、後端驗證 Refresh Token、換發新 Access Token、前端重打原請求，五個節點依序單向流動，沒有分支。
**轉譯輸出**：

​```mermaid
sequenceDiagram
    participant FE as 前端
    participant API as /auth/refresh
    FE->>FE: Access Token 過期，收到 401
    FE->>API: 呼叫 /auth/refresh
    API->>API: 驗證 Refresh Token
    API-->>FE: 換發新 Access Token
    FE->>FE: 用新 Token 重打原請求
​```
```

## 這份範例示範了什麼

- **只轉譯佔位描述裡已經點出的內容**：五個節點與它們的先後順序完全來自佔位描述本身，沒有額外增加或推測節點。
- **判斷依據寫在輸出裡**：先說明「為什麼這是架構圖而不是資料視覺化」，讓使用者能核對轉譯邏輯，不是直接丟一張圖了事。
- **不修改正文、不評論論述**：即使這段文字本身可以再補充「Refresh Token 過期怎麼辦」，`visual-agent` 也不會回頭建議修改正文，那屬於 `critic-agent` 的職責。
