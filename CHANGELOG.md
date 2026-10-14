# Changelog

## [0.1.1] - 2026-10-14

### Added
- 六張定稿圖卡、品牌素材、翡翠金境風格規格與逐頁文字。
- 資產來源說明及實際驗收紀錄。

### Fixed
- 補齊 Skill frontmatter 與觸發條件，九步編號統一為 01–09。
- 修正官方來源即等於高可信度的過度簡化。
- 用完整教學示例替換缺少分鏡且暗示未驗證效果的示例。
- 增加本地連結、版本、圖卡完整性及檔案雜湊檢查。

### Compatibility
- FGM 核心與既有 JSON schema 維持不變；圖卡保留 v0.1.0。

### Release
- 發布為公開 Repo，tag v0.1.1；LICENSE 原文不變（保留所有權利）。
- `.github/scripts/repo-check.py`：讀取文字檔時明確指定 UTF-8，修正在 Windows（預設 cp950）直接執行會 UnicodeDecodeError 的問題；檢查項目不變。
- 新增 `.gitattributes`（統一 LF 檢出），使 SHA256SUMS.txt 在 Windows clone 後仍可驗證。


## [0.1.0] - 2026-10-14

### Added
- FGM core methodology: Fact → Gap → Meaning.
- Evidence-first Agent pipeline.
- Three awareness-level ad outputs.
- Fact verification and compliance guardrails.
- Verification matrix and test cases.
- Structured Skill specification and JSON output schema.
- Repository validation workflow.
