# AI to Agent FGM Ad Copywriter

> **Fact → Gap → Meaning**：把可驗證的產品證據，轉成讓受眾自己得出結論的廣告說服力。

**Repo:** `ai-to-agent-fgm-ad-copywriter`  
**Skill:** `fgm-ad-copywriter`  
**Version:** `0.1.2`

![FGM 技能總覽](assets/cards/01-overview.png)

## Why

本專案處理廣告創作常見的問題：把「品牌想說的」誤當成「消費者會相信的」。FGM 將廣告拆回三個可檢查的核心：

1. **Fact｜事實**：可驗證、可追溯、去形容詞化。
2. **Gap｜缺口**：刻意保留一段資訊差，讓受眾產生「為什麼？」。
3. **Meaning｜言外之意**：不替受眾把結論說死，讓畫面、證據與情境共同完成推論。

## What

FGM 核心方法不變，但在 Agent 執行層加入三個必要環節：

```text
Evidence → Fact → Gap → Meaning → Hook → Script → Visual → Adapt → Verify
             
```

- **Evidence**：先確認來源與證據等級。
- **Adapt**：依 Reels / TikTok / Meta / 圖卡 / 社群貼文調整格式。
- **Verify**：發布前檢查事實、邏輯、合規與輸出完整性。

這三步不是改寫 FGM，而是讓 FGM 從「文案公式」升級為可被 Agent 執行、檢查、驗收的 Skill。

## Core Guardrails

### 1. Fact 必須可驗證
- 不把品牌自述當成客觀事實。
- 不把形容詞、口號、推測寫成證據。
- 有數據時保留來源、單位、條件與時間。
- 無法驗證時標記為 `UNVERIFIED`，不可包裝成確定陳述。

### 2. Gap 必須形成真正資訊落差
- 不是單純聳動或誇大。
- Hook 應讓受眾產生具體疑問，而非只靠恐懼、羞辱、誤導。
- Gap 必須能由後續 Fact 或機制回答。

### 3. Meaning 不替消費者把話說死
- 不把「可能適合」偷換成「一定有效」。
- 優先用證據、對比、情境與畫面讓受眾自行推論。
- 對健康、財務、法律等高風險領域，必須加強來源與合規檢查。

## Outputs

每次執行至少輸出：

1. **事實提煉表**：Evidence / Fact / Source / Confidence / Risk
2. **3 組廣告腳本**：Problem-Aware / Solution-Aware / Product-Aware
3. **前三秒 Gap Hook**
4. **鏡頭與旁白拆解**
5. **靜態圖卡 / 社群貼文文案**
6. **驗收報告**：Fact、Gap、Meaning、合規、格式完整性

## Quick Start

將產品資訊提供給 Agent，例如：

```text
用 fgm-ad-copywriter 分析以下產品。
目標：生成 3 組 30 秒短影音廣告。
素材：產品頁、規格表、原料／結構、客群痛點、可引用證據。
平台：Instagram Reels。
```

Agent 應先完成 Evidence 與 Fact，不應直接跳到 Hook。

完整規格見 [`skill/fgm-ad-copywriter/SKILL.md`](skill/fgm-ad-copywriter/SKILL.md)。

## 教學圖卡

| 頁次 | 主題 |
|---|---|
| 01 | [技能總覽](assets/cards/01-overview.png) |
| 02 | [FGM 三步核心](assets/cards/02-fgm-core.png) |
| 03 | [Agent 九步執行](assets/cards/03-agent-pipeline.png) |
| 04 | [三項核心檢查](assets/cards/04-core-checks.png) |
| 05 | [技能使用與交付](assets/cards/05-usage-outputs.png) |
| 06 | [驗收與修正閉環](assets/cards/06-verification-loop.png) |

設計風格：[翡翠金境｜Emerald Goldscape](docs/visual-style.md)。
圖卡 v0.1.0 沿用已定稿內容，套件 v0.1.2 修正技能格式及示例。

補充文件：[社群文章（完整署名）](docs/social-post.md) · [逐頁文字](docs/cards-transcript.md) · [資產權利](docs/asset-rights.md) · [發布說明](docs/release-notes.md)

## Repository Structure

```text
.
├─ README.md
├─ AGENTS.md
├─ VERSION
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ LICENSE
├─ repo-metadata.json
├─ skill/fgm-ad-copywriter/
│  ├─ SKILL.md
│  └─ output-schema.json
├─ docs/
│  ├─ methodology.md
│  ├─ usage.md
│  ├─ fact-verification.md
│  ├─ compliance-guardrails.md
│  ├─ validation.md
│  ├─ publishing.md
│  ├─ social-post.md
│  └─ release-notes.md
├─ examples/
├─ tests/
├─ assets/
└─ .github/
```

## Validation Standard

FGM 不是「寫完就算完成」。輸出至少要通過：

- Fact 可追溯且沒有把推測偽裝成事實。
- Gap 可由後文回答，沒有 Clickbait-only。
- Meaning 與 Fact 之間不存在邏輯跳躍。
- Hook、Script、Visual 三者一致。
- 內容符合指定平台與長度。
- 高風險宣稱被移除、改寫或標記。
- 三個客群認知層級的切角必須真的不同。

詳見 [`docs/validation.md`](docs/validation.md)。

## 使用範圍與限制

適用於有產品證據的行銷提案、腳本與教學；不適用於無證據的效果承諾。這是指令型 Skill，沒有自動投放程式或內建廣告帳號連線。

將技能文件及產品資料交給支援自訂指令的 Agent，要求遵循完整九步流程。不同平台的自動載入與安裝方式尚未實測，不能宣稱複製資料夾後就會自動啟用。

[完整示例](examples/output-example.md) 採虛構教學資料，包含三組腳本、分鏡、圖卡及驗收。

## 驗收紀錄

執行 `python3 .github/scripts/repo-check.py`。檢查範圍與未驗證項目見 [驗收報告](docs/validation-report.md)。

## 後續計畫

以真實產品及不同 Agent 平台驗證使用流程；再進行廣告投放比較。這些尚未完成。

## Versioning

採 Semantic Versioning。現在版本：**v0.1.2**，日期 2026-10-14，狀態：已發布為公開 Repo，tag v0.1.2；尚未建立 GitHub Release。

## Rights & License

此版本未擅自套用 MIT、Apache、CC 等開放授權。原創方法、文字、品牌資產與第三方素材的權利範圍分開管理，詳見 [`LICENSE`](LICENSE) 與 [`docs/publishing.md`](docs/publishing.md)。

---

**AI Coach 益力康陳董 x CGM Coach 血糖教練 | 2026 AI to Agent | 2027 AI to AGI Agent**
