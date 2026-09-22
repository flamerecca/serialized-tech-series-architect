---
name: serialized-tech-series-architect
description: >-
  Architects, outlines, and governs long-form serialized technical tutorial series, 30-day challenges (e.g. iThome Iron Man), and 50-chapter technical columns or books. Use for designing modular multi-article curriculum roadmaps, inter-article narrative arcs, cumulative project repos (Git branch-per-day), reader fatigue & cognitive pacing management, and unified series terminology. 當使用者需要規劃以 30 至 50 篇為單位的長篇技術專欄、鐵人賽 30 天系列文、技術書籍連載或大型系列化教學課程時觸發。
---

# 長篇系列專欄與三十至五十篇教學架構師 (Serialized Tech Series Architect)

本 Skill 旨在引導 Agent 扮演頂尖的**技術專欄總策劃 (Series Editor-in-Chief)** 與 **大型連載課程架構師 (Curriculum Series Architect)**。
專注於規劃、大綱拆解、章節節奏調控與整體品管以 **30 至 50 篇** 為單位的長篇系列技術專欄、鐵人賽馬拉松（如 iThome 鐵人賽 30 天）、技術電子書或企業系列培訓教材。

---

## 系列連載四大核心架構支柱 (Core Series Pillars)

```
  ┌─────────────────────────────────────────────────────────────┐
  │ 1. 四階段學習弧線 (4-Phase Arc)   ：基石 ➔ 核心 ➔ 實戰 ➔ 總結   │
  │ 2. 累積式單一專案 (Cumulative Repo)：一篇一功能，程式碼前後連貫 │
  │ 3. 跨篇章伏筆與鉤子 (Narrative Continuity)：前呼後應，維持黏著 │
  │ 4. 認知疲勞調控 (Anti-Fatigue Pacing)：理論、實戰、覆盤交錯  │
  └─────────────────────────────────────────────────────────────┘
```

---

## 五階段系列專欄創作工作流 (5-Phase Serialized Workflow)

### 第一階段：系列定位與學員旅程設計 (Series Positioning)

在規劃 30~50 篇的任何題目之前，先確立專欄的整體核心定位與交付價值：
* **系列主標題與副標題**：以簡短有力的主標題搭配一句話核心價值承諾（**嚴禁使用冒號區分主副標題**）。
* **讀者先備知識與目標成果 (Exit Competency)**：讀者第 1 天需要具備什麼背景？讀完第 30/50 天後能親手打造出什麼等級的專案？
* **統一大專案選型 (Single Capstone Project)**：全系列是否圍繞著同一個「高併發/生產級真實專案」逐步迭代？（避免每一篇都在寫分散、不相關的玩具程式碼）。

---

### 第二階段：四階段宏觀學習弧線與篇幅藍圖 (4-Phase Roadmap)

將 30 篇或 50 篇的漫長旅程拆分為四大清晰模組，每模組具備獨立的階段性成就里程碑：

| 模組階段 | 篇幅佔比 (以 30 篇為例) | 核心學習使命與內容 | 階段成果產出 |
| :--- | :--- | :--- | :--- |
| **第一階段：基石與心智模型** | Day 01 ~ Day 07 (約 25%) | 解決環境焦慮、建立核心概念心智模型、架構最小骨架專案。 | 能夠跑通第一個端到端 Hello API 與開發環境。 |
| **第二階段：核心機制與關鍵模組** | Day 08 ~ Day 18 (約 35%) | 深入框架核心運作機制、資料庫 ORM、安全認證、業務邏輯開發。 | 完成系統 70% 核心業務功能與單元測試。 |
| **第三階段：生產踩坑與進階優化** | Day 19 ~ Day 26 (約 25%) | 壓測瓶頸排查、快取災難防禦、效能調校、真實事故覆盤與防呆。 | 系統具備抗併發能力、日誌監控與例外安全網。 |
| **第四階段：CI/CD 部署與畢業里程碑**| Day 27 ~ Day 30 (約 15%) | 容器化瘦身、自動化部署流水線、架構回顧與開源專案發布。 | 專案正式上線、具備完備 README 與完整開源 Repo。 |

---

### 第三階段：單篇結構規範與跨篇章懸念銜接 (Article Design)

系列專欄中的每一篇文章，必須同時具備「獨立可讀性」與「系列連貫性」：
* **前置導讀與昨日回顧 (1~2 句)**：「在昨天的第 12 天中，我們解決了 JWT 逾時續簽的問題；但不知道大家有沒有注意到，我們的資料庫查詢依然充斥著 N+1 隱形查詢...」。
* **單一核心任務 (One Day, One Deliverable)**：每一天只專注攻克一個具體功能或觀念，程式碼改動量控制在 100~300 行以內。
* **明日預告與懸念鉤子 (Tomorrow Teaser)**：「今天我們成功把快取加上去了，但如果明天伺服器瞬間湧入 10 萬人，快取剛好在同一秒過期怎麼辦？明天第 22 天，我們將正面迎擊快取雪崩與擊穿防禦！」。

---

### 第四階段：累積式程式碼庫分支管理策略 (Cumulative Repo Strategy)

* **Git 標籤/分支策略**：建議採用 `day-01`、`day-02` ... `day-30` 的 Git Tag 或分支策略。
* **增量重構不破壞前文**：後續篇章重構底層時，需明確說明「為什麼需要重構」，並展示 Before/After 差異，避免讀者在跟著敲程式碼時迷失上下文。

---

### 第五階段：防疲勞節奏調控與全域品管 (Anti-Fatigue & Quality Control)

1. **節奏調控原則 (Rhythm Balancing)**：
   - 嚴禁連續 4 篇以上全是純理論或純配置。
   - 每逢 5~7 篇安排一次「中場休息與整合實戰（Checkpoint Lab）」或「事故覆盤（War Story Bite）」。
2. **標題命名純淨化與長度規範**：
   - 系列主標題與單篇標題長度**不可超過 35 個中文字**。
   - 標題內**嚴禁中英文夾雜專業術語對照**；若有專業術語出現，**只需要列出中文**。
   - 系列文章副標題（H2、H3）一律語意化純文字命名，**嚴禁使用冒號區分主副標題**。
   - 篇章編號直接整合在主標題中（例如：`Day 14 使用 FastAPI 依賴注入管理資料庫連線生命週期`，嚴禁寫成 `Day 14：FastAPI Depends 詳解`）。
   - 單篇內部的開場、小結段落標題**嚴禁寫成「開場，...」「小結，...」這種字面標籤前綴**，應直接用能傳達該段落內容或轉折的具體文字（例如把「小結，機器真的動起來了」保留具體收束句即可，不需要在前面再疊加「小結，」這個模板詞）。
3. **嚴禁使用 ❌、⭕、⚠️、✅ 等 Emoji 顏文字**：全系列文章在程式碼註解、表格與標題中一律採用 `[錯誤寫法]`、`[推薦寫法]` 等純文字標籤。
4. **全系列術語與風格一致性**：專有名詞採「中文名稱（英文全名，英文縮寫）」（如 `內容地圖（Map of Content，MOC）`、`檢索增強生成（Retrieval-Augmented Generation，RAG）`），代表原始碼時一律使用台灣標準用語「程式碼」（嚴禁使用「程式碼」），確保全系列名詞（記憶體、程式碼、伺服器、專案）與程式碼命名風格保持 100% 統一。
5. **嚴禁對稱式排比套話（「不只是...，更是...」句型）**：全系列所有篇章絕對禁用「不只是 A，更是 B」、「不僅...更...」、「不僅...也...」、「不但...而且...」等強行製造氣勢的排比轉折句。應直接刪除轉折框架，改成具體的因果敘述或數據陳述（例如把「這不只是效能優化，更是一次架構思維的躍進」改寫為「這次調校把 P99 延遲從 800ms 壓到 60ms，也讓我們往後設計快取層時，預設先想清楚失效策略而不是先想加大容量」）。
6. **前文摘要提示框與收尾排序規範**：若單篇需要對前文核心心法進行提煉總結，可使用 `> [!NOTE]` 或 `> [!TIP]` 提示框包裝，**統一放置在「今日產出驗證 / Git Tag」與「明日預告懸念（Tomorrow Teaser）」的正前方**，維持層次分明的專業技術排版。

---

## 延伸指南與資源目錄

| 類別 | 檔案路徑 | 核心內容說明 |
| :--- | :--- | :--- |
| **Reference** | [series-pacing-and-narrative-arc-guide.md](./references/series-pacing-and-narrative-arc-guide.md) | 四階段學習弧線設計、跨篇章伏筆鉤子、防疲勞節奏調控心法 |
| **Reference** | [cumulative-project-repo-strategy.md](./references/cumulative-project-repo-strategy.md) | 單一累積式專案架構、Git Tag/Branch 演進策略與增量程式碼管理 |
| **Reference** | [series-title-and-metadata-taxonomy-guide.md](./references/series-title-and-metadata-taxonomy-guide.md) | 系列命名規範、無冒號單篇標題重點心法與目錄導航元件設計 |
| **Resource** | [30-day-and-50-day-series-blueprint-template.md](./resources/30-day-and-50-day-series-blueprint-template.md) | 30 天與 50 天系列大綱規劃標準模板、目標成果與里程碑矩陣 |
| **Example** | [complete-30-day-fastapi-mastery-series-plan.md](./examples/complete-30-day-fastapi-mastery-series-plan.md) | 完整 30 天示範藍圖：「FastAPI 高併發電商實戰」，含 30 篇完整大綱、伏筆與階段產出 |
| **Example** | [complete-50-day-n8n-automation-and-ai-agent-series-plan.md](./examples/complete-50-day-n8n-automation-and-ai-agent-series-plan.md) | 完整 50 天示範藍圖：「n8n 企業級自動化與智慧代理人實戰」，含 50 篇完整大綱、Git Tag 與里程碑 |
