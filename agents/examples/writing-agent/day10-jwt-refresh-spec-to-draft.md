# 範例：寫作規格書 → 單篇初稿

延續 [planning-agent 範例](../planning-agent/day10-jwt-refresh-idea-to-spec.md) 產出的 Day 10 規格書，示範 `writing-agent` 怎麼把規格書、風格指南、全域錨點摘要三份輸入，展開成一篇初稿。

## 輸入一：規格書

沿用 [planning-agent 範例](../planning-agent/day10-jwt-refresh-idea-to-spec.md) 產出的完整規格書，不重複貼一份。

## 輸入二：風格指南（節錄）

```markdown
語氣定位：直接了當的工程師對話口吻，不用正式技術文件腔。
禁用語詞：值得注意的是、不僅如此、賦能、打造、顛覆性。
排版規約：中英文之間留半形空格；專有名詞保留英文原文；清單一律用 `- `。
```

## 輸入三：全域錨點摘要（節錄）

```markdown
全域系列地圖：本篇為 fastapi-ecommerce-pro 30 天系列的 Day 10，前一篇 Day 09 完成使用者註冊登入。
滾動摘要視窗：Day 09 用 bcrypt 對密碼加鹽雜湊，完成 `/auth/register` 與 `/auth/login`，讀者手上已經有一組能登入的帳號。
已解鎖知識清單：bcrypt 密碼雜湊、`/auth/login` 基本登入流程，兩者只能引用、不能重講。
```

## 輸出：初稿

```markdown
---
date: 2026-03-10
category: FastAPI 生產級電商微服務
summary: 設計 Access Token 與 Refresh Token 雙權杖架構，讓 Token 過期時能自動續簽，不必強迫使用者重新登入。
tags:
  - fastapi
  - jwt
  - fastapi-ecommerce-pro
---

# 雙重權杖簽發與自動過期刷新機制

昨天 Day 09 把 `/auth/register` 跟 `/auth/login` 兜起來了，使用者現在能拿著帳密換到一組能用的 Token。但這組 Token 很快就會過期，過期之後呢？

有個使用者在結帳頁填了半天信用卡資料，按下送出的瞬間 Access Token 剛好過期，畫面直接被踢回登入頁，剛剛填的資料全部消失。這不是假設，Access Token 效期設得越短越安全，但也代表這種中斷情境的機率越高。解法不是把效期拉長犧牲安全性，而是設計一組 Refresh Token，讓系統能在背景悄悄換發新的 Access Token。

## 雙 Token 的分工

Access Token 效期設 15 分鐘，跟著每個請求的 `Authorization` 標頭一起送出，外洩風險視窗很短。Refresh Token 效期設 7 天，只在換發新 Access Token 時使用一次，儲存位置也跟 Access Token 分開。

| Token 類型 | 效期 | 建議儲存位置 | 外洩風險 |
| :--- | :--- | :--- | :--- |
| Access Token | 15 分鐘 | 記憶體 | 低，效期短，就算外洩很快失效 |
| Refresh Token | 7 天 | HttpOnly Cookie | 中，需要額外的撤銷機制防止長期濫用 |

## 簽發雙 Token

`/auth/token` 在驗證帳密成功後，同時簽發兩組 Token：

```python
@router.post("/auth/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    access_token = create_access_token(user.id, expires_minutes=15)
    refresh_token = create_refresh_token(user.id, expires_days=7)
    return {"access_token": access_token, "refresh_token": refresh_token}
```

## 用 Refresh Token 換發新 Access Token

<!-- 圖表佔位：呈現「Access Token 過期」→「前端呼叫 /auth/refresh」→「後端驗證 Refresh Token」→「換發新 Access Token」→「前端重打原請求」這五個步驟的時序圖，節點之間是單向依序流動，沒有分支 -->

`/auth/refresh` 只做一件事：驗證 Refresh Token 沒過期、沒被撤銷，就換一組新的 Access Token。

```python
@router.post("/auth/refresh")
async def refresh(refresh_token: str = Cookie(...)):
    payload = verify_refresh_token(refresh_token)
    new_access_token = create_access_token(payload.user_id, expires_minutes=15)
    return {"access_token": new_access_token}
```

前端只要在 Access Token 過期收到 401 時，自動呼叫一次 `/auth/refresh`，拿到新 Token 後重打原本那個請求，使用者完全不會感覺到中斷。

這套雙 Token 架構解決了「過期就得重新登入」的體驗問題，但 Refresh Token 本身如果外洩，攻擊者能在 7 天內持續換發 Access Token。明天 Day 11，我們要幫 API 加上角色權限守門員，讓換發出來的 Token 就算被冒用，也只能做這個角色被允許的事。
```

## 這份範例示範了什麼

- **單一核心動作**：這篇只講「雙 Token 簽發與續簽」，不會因為提到 Refresh Token 就順手把權限控管也塞進來，那是 Day 11 的範圍。
- **已解鎖知識用連結帶過**：開頭直接說「昨天 Day 09 把 `/auth/register` 跟 `/auth/login` 兜起來了」，不重新解釋 bcrypt 雜湊機制。
- **圖表佔位符的寫法**：佔位描述裡明確點出五個節點與它們的先後關係，這是 `visual-agent` 唯一會讀到的輸入，寫得越具體，轉譯出來的圖越準確。
- **收尾預告鉤子**：結尾點出 Refresh Token 外洩的風險，直接銜接到 Day 11 的角色權限主題。
