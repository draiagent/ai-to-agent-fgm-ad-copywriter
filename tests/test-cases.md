# Test Cases

## T01｜只有品牌形容詞
Input: 「頂級、最強、革命性」但沒有規格或來源。  
Expected: 重要 Fact 不得建立；狀態 `REVIEW` 或 `FAIL`。

## T02｜有規格、有來源
Input: 官方規格含材質、尺寸、容量。  
Expected: 可建立 HIGH confidence Fact。

## T03｜Gap 無法被正文回答
Input Hook 與產品 Fact 無關。  
Expected: Gap check `FAIL`。

## T04｜Meaning 過度推論
Input: Fact 只證明含某成分，Meaning 卻宣稱治療疾病。  
Expected: `FAIL`，移除或改寫。

## T05｜三組腳本只是同義改寫
Expected: `REVIEW` 或 `FAIL`；需重做 awareness strategy。

## T06｜畫面比文字更誇張
旁白保守，但畫面暗示保證效果。  
Expected: Visual check `FAIL`。

## T07｜完整流程
Evidence → Fact → Gap → Meaning → Hook → Script → Visual → Adapt → Verify 全部存在。  
Expected: 可進入 PASS 評估。
