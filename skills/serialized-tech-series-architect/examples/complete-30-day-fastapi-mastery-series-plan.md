# 完整三十天系列專欄示範大綱：FastAPI 生產級電商微服務

本範例提供一份標準、可直接執行的 30 天長篇系列專欄完整規劃藍圖，示範如何將「四階段學習弧線」、「跨篇章伏筆銜接」與「累積式 Git 標籤專案」落地於真實技術連載。

---

## 系列專欄前導宣告

* **系列主標題**：從零打造生產級 FastAPI 高併發電商微服務 30 天實戰
* **系列副標題**：掌握非同步 ORM、JWT 認證、Redis 分散式快取、Celery 任務佇列與 Docker 雲原生部署的全端工程演進
* **目標讀者**：具備基礎 Python 語法與基本 Web 概念，希望跨入非同步後端高併發架構的中階工程師
* **全系列累積專案**：`fastapi-ecommerce-pro`（開源非同步電商微服務）

---

## 第一階段：基石與最小骨架 (Day 01 - Day 07)

### Day 01 告別同步阻塞與建立現代非同步開發環境
* **核心使命**：剖析同步 vs 非同步 I/O 底層差異，使用 `uv` 初始化專案與安裝 FastAPI。
* **今日交付**：完成 `main.py` 並啟動 Uvicorn 跑通 `/health` 端點。
* **跨篇伏筆**：*「今天我們成功跑起了第一個非同步伺服器，但要讓它處理複雜業務，我們需要一套乾淨的專案目錄分層...」*
* **Git Tag**：`tag: day-01-environment-scaffolding`

### Day 02 生產級專案分層架構與環境設定管理
* **核心使命**：建立 Routers、Schemas、Models、Services、Core 分層，使用 `pydantic-settings` 注入環境變數。
* **今日交付**：完成 `app/core/config.py` 與階層式目錄骨架。
* **Git Tag**：`tag: day-02-project-structure`

### Day 03 非同步資料庫連線與引擎初始化
* **核心使命**：配置 `create_async_engine` 與 `async_sessionmaker`，解析連線池參數調校心法。
* **今日交付**：建立 `app/core/database.py`。
* **Git Tag**：`tag: day-03-async-database-engine`

### Day 04 掌握請求生命週期與資料庫連線依賴注入
* **核心使命**：使用 `yield` 產生器實作依賴注入，保證每個 HTTP 請求安全釋放連線。
* **今日交付**：完成 `get_db_session` 依賴函式。
* **Git Tag**：`tag: day-04-depends-session-lifecycle`

### Day 05 宣告式資料模型與自動資料庫遷移
* **核心使命**：使用 SQLAlchemy 2.0 宣告式語法定義 User 與 Product 資料表，配置 Alembic 非同步遷移。
* **今日交付**：完成首個 Migration 腳本並成功生成 SQLite/PostgreSQL 本地資料表。
* **Git Tag**：`tag: day-05-models-and-migrations`

### Day 06 打造第一個強型別商品增刪改查路由
* **核心使命**：定義 Pydantic Request/Response Schemas，實作商品清單分頁與單筆新增。
* **今日交付**：完成 `app/routers/products.py`。
* **Git Tag**：`tag: day-06-products-crud-api`

### Day 07 第一階段整合驗收與非同步測試架構
* **核心使命**：配置 `pytest-asyncio` 與 `httpx.AsyncClient`，為前 6 天的功能編寫自動化測試。
* **今日交付**：測試覆蓋率達標，第一階段骨架封裝完成。
* **Git Tag**：`tag: day-07-phase1-checkpoint`

---

## 第二階段：核心機制與業務模組 (Day 08 - Day 18)

### Day 08 統一錯誤回應與自訂例外處理中介軟體
* **核心使命**：封裝全局 `HTTPException` 與 `RequestValidationError` 處理器，標準化 JSON 錯誤結構。
* **今日交付**：完成 `app/core/exceptions.py`。
* **Git Tag**：`tag: day-08-exception-handlers`

### Day 09 密碼學安全雜湊與用戶註冊登入
* **核心使命**：使用 `bcrypt` 進行密碼單向雜湊加鹽，實作使用者註冊端點。
* **今日交付**：完成 `app/services/auth.py`。
* **Git Tag**：`tag: day-09-user-registration`

### Day 10 雙重權杖簽發與自動過期刷新機制
* **核心使命**：設計 Access Token (15分鐘) 與 Refresh Token (7天) 輪替架構。
* **今日交付**：完成 `/auth/token` 與 `/auth/refresh` 端點。
* **Git Tag**：`tag: day-10-jwt-token-refresh`

### Day 11 角色權限守門員與複合依賴注入
* **核心使命**：實作 `get_current_active_user` 與 `require_admin` 角色守門員。
* **今日交付**：商品新增/下架 API 成功套用管理員權限保護。
* **Git Tag**：`tag: day-11-role-based-access-control`

### Day 12 購物車模組與複雜資料庫關聯查詢
* **核心使命**：設計 User、Cart、CartItem 的一對多與多對多 ORM 關聯。
* **今日交付**：完成購物車加入、修改數量與查詢清單端點。
* **Git Tag**：`tag: day-12-shopping-cart-module`

### Day 13 防範查詢放大與關聯預載入深度調校
* **核心使命**：剖析 `selectinload` 與 `joinedload` 差異，徹底消除隱形 N+1 查詢。
* **今日交付**：購物車查詢 SQL 次數由 N+1 次縮減為常數 2 次。
* **Git Tag**：`tag: day-13-eager-loading-optimization`

### Day 14 訂單建立與資料庫交易隔離
* **核心使命**：使用 `session.begin()` 確保庫存扣減與訂單明細寫入在同一交易中完成。
* **今日交付**：完成 `/orders/checkout` 端點。
* **Git Tag**：`tag: day-14-order-transaction-acid`

### Day 15 檔案上傳串流與雲端物件儲存整合
* **核心使命**：使用 `UploadFile` 串流接收商品圖片，非同步上傳至 S3 / MinIO。
* **今日交付**：完成商品圖片上傳與縮圖生成服務。
* **Git Tag**：`tag: day-15-file-upload-s3`

### Day 16 內建背景任務與非同步郵件發送
* **核心使命**：使用 FastAPI 內建 `BackgroundTasks` 在下單後非同步發送購買通知信。
* **今日交付**：下單 API 不再阻塞於 SMTP 網路延遲。
* **Git Tag**：`tag: day-16-background-email-tasks`

### Day 17 進階測試矩陣與測試依賴覆寫
* **核心使命**：使用 `app.dependency_overrides` 隔離真實資料庫與外部寄信服務。
* **今日交付**：完成全套下單與認證測試套件。
* **Git Tag**：`tag: day-17-test-dependency-overrides`

### Day 18 第二階段電商核心功能整合驗收
* **核心使命**：執行端到端業務流測試（註冊 ➔ 登入 ➔ 挑選商品 ➔ 購物車 ➔ 結帳下單 ➔ 寄信）。
* **今日交付**：第二階段業務功能全線通暢。
* **Git Tag**：`tag: day-18-phase2-checkpoint`

---

## 第三階段：效能調校與生產踩坑 (Day 19 - Day 26)

### Day 19 導入快取旁路模式與熱門商品讀取優化
* **核心使命**：整合 `redis-py`，針對高頻熱門商品列表建立多級快取機制。
* **今日交付**：商品列表讀取延遲由 45ms 降至 2ms。
* **Git Tag**：`tag: day-19-redis-cache-aside`

### Day 20 快取三大災難防禦與隨機過期時間
* **核心使命**：撰寫「空物件快取」防穿透，加入隨機離散過期時間防雪崩。
* **今日交付**：完成防禦性快取工具函式庫。
* **Git Tag**：`tag: day-20-cache-disasters-defense`

### Day 21 秒殺搶購超賣防禦與分散式鎖實戰
* **核心使命**：使用 `SET NX PX` 與 Lua 腳本實作原子扣庫存，徹底消除超賣現象。
* **今日交付**：秒殺下單 API 通過 1,000 併發超賣壓力測試。
* **Git Tag**：`tag: day-21-redis-distributed-lock`

### Day 22 打造高精度滑動窗口限流器
* **核心使命**：在 API Gateway / Middleware 層限制單一 IP 每分鐘最多發送 60 次請求。
* **今日交付**：完成 `RateLimiterMiddleware`。
* **Git Tag**：`tag: day-22-sliding-window-rate-limiter`

### Day 23 真實連線池耗盡事故覆盤與調校
* **核心使命**：重現「在交易區塊內呼叫第三方金流 API」導致連線池瞬間耗盡的生產慘劇。
* **今日交付**：完成 Before/After 程式碼重構與連線佔用監控表格。
* **Git Tag**：`tag: day-23-connection-pool-postmortem`

### Day 24 慢查詢執行計畫深度解讀與複合索引
* **核心使命**：使用 `EXPLAIN (ANALYZE, BUFFERS)` 排查訂單歷史查詢全表掃描瓶頸。
* **今日交付**：建立 `(user_id, created_at)` 複合索引，查詢效能躍升 40 倍。
* **Git Tag**：`tag: day-24-slow-query-indexing`

### Day 25 非同步任務佇列與重度報表匯出
* **核心使命**：將巨量訂單 CSV 匯出移至獨立 Worker 行程，支援進度查詢與檔案下載。
* **今日交付**：完成 Celery 非同步報表產生管線。
* **Git Tag**：`tag: day-25-celery-report-export`

### Day 26 系統高併發壓力測試與基準指標驗收
* **核心使命**：使用 Locust 進行 5,000 併發使用者負載測試，產出 P50/P95/P99 效能基準報表。
* **今日交付**：系統穩定支撐 3,200 RPS 吞吐量。
* **Git Tag**：`tag: day-26-phase3-checkpoint`

---

## 第四階段：容器部署與畢業里程碑 (Day 27 - Day 30)

### Day 27 容器多階段建置與映像檔極致瘦身
* **核心使命**：使用 Multi-Stage Build 將映像檔體積由 1.2GB 瘦身至 65MB，配置非 Root 容器安全。
* **今日交付**：完成生產級 `Dockerfile` 與 `.dockerignore`。
* **Git Tag**：`tag: day-27-docker-multi-stage`

### Day 28 打造自動化測試與持續整合流水線
* **核心使命**：配置程式碼風格檢查 (ruff)、pytest 異步測試與自動構建推播至 GHCR。
* **今日交付**：完成 `.github/workflows/ci.yml`。
* **Git Tag**：`tag: day-28-github-actions-cicd`

### Day 29 容器生產編排反向代理與憑證配置
* **核心使命**：編排 App、PostgreSQL、Redis、Celery 與 Nginx 叢集，配置 SSL 自動續簽。
* **今日交付**：完成 `docker-compose.prod.yml`。
* **Git Tag**：`tag: day-29-docker-compose-production`

### Day 30 全系列架構覆盤與開源專案發布
* **核心使命**：全面回顧 30 天架構演進歷程，發布完整開源專案 README 與架構圖，頒發畢業證書。
* **今日交付**：`fastapi-ecommerce-pro` 開源專案正式上線。
* **Git Tag**：`tag: day-30-series-graduation`
