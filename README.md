# serialized-tech-series-architect

把「規劃、撰寫、視覺、審查」四線 Agent 的長篇系列技術文生成 pipeline，打包成 Claude Code 的 Skill 與 Agent，讓你在對話中把一則靈感筆記，逐步變成一整個系列的技術文章。

## 這個套件包含什麼

```
serialized-tech-series-architect/
├── install.sh   一鍵安裝腳本：把 skills/ 與 agents/ 複製到指定範圍
├── skills/
│   └── serialized-tech-series-architect/   系列層級規劃：大綱、節奏、命名規範
└── agents/
    ├── planning-agent.md   第一線：靈感筆記 → 寫作規格書
    ├── writing-agent.md    第二線：規格書 → 單篇初稿
    ├── visual-agent.md     第三線：正文 → 架構圖／資料視覺化／封面
    └── proofreading-agent.md   第四線：初稿 → 審查報告
```

### Skill

| 名稱 | 用途 |
| :--- | :--- |
| **serialized-tech-series-architect** | 規劃以 30 至 50 篇為單位的長篇系列技術專欄、鐵人賽 30 天、技術書籍連載，負責系列定位、四階段學習弧線、累積式專案 Repo 策略、防疲勞節奏調控與全系列命名規範。單篇文章實際怎麼寫，交給下面四個 Agent 依序接手。 |

### Agent，依處理順序排列

| 順序 | 名稱 | 用途 |
| :--- | :--- | :--- |
| 1 | **planning-agent** | 把一則靈感筆記逆向拆解成結構化的寫作規格書，只規劃、不動筆寫正文，也不做技術審查。 |
| 2 | **writing-agent** | 依規格書逐章節生成單篇技術文章初稿，內建 AI 味防範清單，涉及具體 API 或指令語法時會用 WebSearch／WebFetch 先查證再寫。 |
| 3 | **visual-agent** | 讀取正文裡標記的圖表佔位符，轉譯成架構圖、資料視覺化圖表或封面插圖之一，不判斷論述邏輯、不改正文文字。 |
| 4 | **proofreading-agent** | 依全域錨點檔案、風格指南與目標受眾畫像、對應段落的 Section Spec 三份既定依據，複核初稿的事實正確性、可讀性與去 AI 腔調、格式一致性，只找問題、不動手重寫。 |

## 系統需求

- 支援 Skill 與 Agent 的 Claude Code 版本，才能讀取本套件裡的 SKILL.md 與 Agent 定義。
- `writing-agent`、`proofreading-agent` 會用 WebSearch／WebFetch 查證具時效性的技術宣稱，需要這兩個工具在你的環境裡可用，缺少時仍可運作，只是會跳過查證直接依訓練記憶撰寫或審查，風險較高。
- 這套 pipeline 假設你有既有的筆記或知識庫可以被 Grep／Glob 檢索，用來串接已解鎖知識與參考素材；沒有的話 `planning-agent` 仍會依你提供的靈感筆記單獨運作，只是少了既有筆記的參照。
- 想用方式二的 Plugin 安裝，需要支援 Plugin Marketplace 的 Claude Code 版本；不確定版本是否支援時，改用方式一的手動複製即可。
- 想用方式三的一鍵安裝指令，環境需要有 `git` 與 Bash，指令內部會用 `git clone` 抓取套件內容，兩者缺一都無法執行，改用方式一即可。

## 安裝方式

### 方式一：手動複製，最簡單、保證可用

1. 把這個儲存庫 clone 下來。
2. 依你想套用的範圍，把 `skills/` 與 `agents/` 底下的資料夾複製到對應位置：
   - 全域套用：`~/.claude/skills/`、`~/.claude/agents/`
   - 單一專案套用：`<專案根目錄>/.claude/skills/`、`<專案根目錄>/.claude/agents/`

```bash
git clone https://github.com/flamerecca/serialized-tech-series-architect.git
cp -R serialized-tech-series-architect/skills/* ~/.claude/skills/
cp -R serialized-tech-series-architect/agents/* ~/.claude/agents/
```

複製完成後重新啟動 Claude Code，即可在對話中直接呼叫 `serialized-tech-series-architect` Skill，或讓 Claude Code 依情境自動叫用 `planning-agent`、`writing-agent`、`visual-agent`、`proofreading-agent` 這四個 Agent。

### 方式二：作為 Claude Code Plugin 安裝

這個儲存庫本身就是一份 Marketplace，內含單一 Plugin `serialized-tech-series-architect`，在 Claude Code 對話中輸入：

```
/plugin marketplace add flamerecca/serialized-tech-series-architect
/plugin install serialized-tech-series-architect@serialized-tech-series-architect
```

### 方式三：一鍵安裝指令，最快速

不想手動 clone 也不想透過 Plugin Marketplace 時，直接執行 [`install.sh`](./install.sh)：

```bash
curl -fsSL https://raw.githubusercontent.com/flamerecca/serialized-tech-series-architect/main/install.sh | bash
```

指令內部會把套件 clone 到暫存目錄，再將 `skills/` 與 `agents/` 複製到 `~/.claude/`，完成後自動清除暫存目錄。若要安裝到目前所在專案而非全域，加上 `--project` 參數，會改複製到 `<目前目錄>/.claude/`：

```bash
curl -fsSL https://raw.githubusercontent.com/flamerecca/serialized-tech-series-architect/main/install.sh | bash -s -- --project
```

複製完成後同樣需要重新啟動 Claude Code 才會套用。

## 快速開始

安裝完成後，先用 `serialized-tech-series-architect` Skill 規劃整個系列的大綱，再逐篇交給四線 Agent 接力生成，例如：

> 幫我規劃一個 30 天的鐵人賽系列，主題是用 FastAPI 打造一個高併發電商後端。

Claude Code 會依序：

1. 套用 `serialized-tech-series-architect` Skill，產出系列定位、四階段學習弧線與 30 篇大綱。
2. 針對其中一篇丟一句靈感，例如「今天要寫 Day 12：解決 JWT 逾時續簽」，呼叫 `planning-agent` 拆解成該篇的寫作規格書。
3. 呼叫 `writing-agent` 依規格書生成這篇初稿，正文裡需要圖表的地方會留下佔位符。
4. 呼叫 `visual-agent` 讀取佔位符，補上對應的架構圖或資料視覺化圖表。
5. 呼叫 `proofreading-agent` 複核初稿與圖表，產出一份審查報告，列出需要你決策或直接可判定成立的問題。

## 延伸閱讀

`serialized-tech-series-architect` Skill 底下還有以下可以獨立閱讀的教材：

- [series-pacing-and-narrative-arc-guide.md](./skills/serialized-tech-series-architect/references/series-pacing-and-narrative-arc-guide.md)：四階段學習弧線設計、跨篇章伏筆鉤子、防疲勞節奏調控心法。
- [cumulative-project-repo-strategy.md](./skills/serialized-tech-series-architect/references/cumulative-project-repo-strategy.md)：單一累積式專案架構、Git Tag/Branch 演進策略。
- [series-title-and-metadata-taxonomy-guide.md](./skills/serialized-tech-series-architect/references/series-title-and-metadata-taxonomy-guide.md)：系列命名規範、無冒號單篇標題重點心法。
- [30-day-and-50-day-series-blueprint-template.md](./skills/serialized-tech-series-architect/resources/30-day-and-50-day-series-blueprint-template.md)：30 天與 50 天系列大綱規劃標準模板。
- [complete-30-day-fastapi-mastery-series-plan.md](./skills/serialized-tech-series-architect/examples/complete-30-day-fastapi-mastery-series-plan.md)：完整 30 天示範藍圖。
- [complete-50-day-n8n-automation-and-ai-agent-series-plan.md](./skills/serialized-tech-series-architect/examples/complete-50-day-n8n-automation-and-ai-agent-series-plan.md)：完整 50 天示範藍圖。

四個 Agent 各自也有一份對應的輸入輸出範例，四份串起來剛好是同一個 Day 10「雙重權杖簽發與自動過期刷新機制」從靈感到審查報告的完整流程：

- [planning-agent 範例](./agents/examples/planning-agent/day10-jwt-refresh-idea-to-spec.md)：靈感筆記 → 寫作規格書
- [writing-agent 範例](./agents/examples/writing-agent/day10-jwt-refresh-spec-to-draft.md)：規格書 → 初稿
- [visual-agent 範例](./agents/examples/visual-agent/day10-jwt-refresh-diagram-to-mermaid.md)：圖表佔位符 → Mermaid 架構圖
- [proofreading-agent 範例](./agents/examples/proofreading-agent/day10-jwt-refresh-review-report.md)：初稿 → 審查報告

## 使用時機

要規劃 30 至 50 篇的長篇系列技術專欄、鐵人賽 30 天系列文、技術書籍連載或大型系列化教學課程時，在對話中提出需求，Claude Code 會自動判斷套用 `serialized-tech-series-architect` Skill 規劃系列骨架；實際逐篇生成內容時，依「靈感筆記 → 規格書 → 初稿 → 配圖 → 審查」的順序，依序呼叫 `planning-agent`、`writing-agent`、`visual-agent`、`proofreading-agent`。

## 授權

MIT License，詳見 [LICENSE](./LICENSE)。
