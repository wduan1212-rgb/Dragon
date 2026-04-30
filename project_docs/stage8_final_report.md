# Stage 8 Final Report

## 完成内容

- 根据第八阶段审核版方案，为新增剧情 CG 周围补充 57 句中文台词。
- 扩写开场、封印门、李将军登场、紫焰提示、真相推进、高潮爆发与五个结局余波。
- 将 `新结尾bgm.mp4` 备份并转换为 `game/audio/bgm/bgm_new_ending.ogg`。
- 新增 `safe_ending_bgm()`，新结尾 BGM 缺失时回退旧好结局 BGM。
- 正向结局改用新结尾 BGM，坏结局继续保留坏结局 BGM。
- 更新 BGM 映射、语音清单与第八阶段报告。

## 修改文件

| 文件 | 说明 |
|---|---|
| `game/script.rpy` | 新增剧情台词、语音占位、结尾 BGM 调用 |
| `game/audio.rpy` | 新增 `safe_ending_bgm()` |
| `game/audio/bgm/bgm_new_ending.ogg` | 新结尾 BGM |
| `docs/bgm_mapping.md` | 追加新结尾 BGM 映射 |
| `docs/voice_line_manifest.md` | 追加 57 条新增台词语音占位 |
| `docs/task_log.md` | 追加第八阶段任务记录 |

## 新增报告

- `docs/stage8_dialogue_expansion_report.md`
- `docs/stage8_bgm_update_report.md`
- `docs/stage8_voice_manifest_update.md`
- `docs/stage8_final_report.md`

## 验证

| 检查 | 结果 |
|---|---|
| Ren'Py lint | 通过 |
| Ren'Py compile | 通过 |
| 新结尾 BGM 文件 | 已生成 |
| `game/` 是否误入 `.md` | 未发现 |
| 系统绝对字体路径 | 未发现 |
| 视频过场 / final CG / HUD | 未重新启用 |

最终 lint 时间：2026-04-30 13:28:33。

## 人工复核建议

- 重点试玩 `truth_sequence` 和 `demon_arrival`，确认新增台词不会拖慢高潮节奏。
- 重点试听四个正向结局，确认 20 秒新 BGM 循环可接受。
- 坏结局应继续保持原坏结局 BGM。
