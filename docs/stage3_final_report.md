# Stage 3 Final Report

## 完成内容

- 修复 UI 层级：普通剧情不再显示战斗 HUD；HUD 仅在 `demon_arrival` 以 `zorder 5`、`alpha 0.18` 显示。
- 固定对话框与名字条：`screen say` 使用底部固定对话区域，名字条绑定在左上方，中文角色名保持不变。
- 修复李将军白边：已对李将军系列立绘做保守边缘清理，并保留处理前备份。
- 处理赵无炎坏立绘：`zhao_cold.png`、`zhao_normal.png` 已从备份回退，坏图已放入 `review_needed/stage3_bad_cutout/`，当前主线不引用这两张。
- 整理中文命名音频与终局 CG：已将用户提供素材转换/复制到 `game/audio/` 与 `game/videos/ending_cg/` 的英文安全路径。
- 生成男主临时候选库：已从参考音频切分 12 个候选片段，保存到 `game/audio/voice_candidates/male/`。
- 导出逐句配音清单：`docs/voice_line_manifest.md` 已生成，脚本已按逐句 `safe_voice()` 接入。
- 接入安全 BGM/SFX/voice 播放：缺失音频会静默跳过，不会让游戏崩溃。
- 增加可选终局 CG 播放：所有结局后调用 `play_optional_ending_cg`，视频缺失或播放失败时会安全跳过。

## 新增/更新文件

| 文件 | 说明 |
|---|---|
| `game/audio.rpy` | 安全音频播放函数 |
| `game/script.rpy` | BGM/SFX/voice/终局 CG 接入，HUD 层级修复 |
| `game/screens.rpy` | UI 层级、菜单 BGM、按钮 SFX |
| `game/options.rpy` | 打包包含 `game/audio/**` |
| `docs/stage3_ui_layer_report.md` | UI 层级报告 |
| `docs/stage3_character_cutout_report.md` | 角色透明底与坏图回退报告 |
| `docs/stage3_ui_asset_report.md` | UI 透明素材复查报告 |
| `docs/stage3_audio_system_report.md` | 音频安全系统报告 |
| `docs/stage3_audio_video_update_report.md` | 音频/视频整理概览 |
| `docs/stage3_raw_asset_rename_map.md` | 中文素材到英文安全路径映射 |
| `docs/bgm_mapping.md` | BGM 场景映射 |
| `docs/ending_cg_mapping.md` | 终局 CG 映射 |
| `docs/voice_candidate_manifest.md` | 男主候选片段清单 |
| `docs/voice_temp_mapping.md` | 临时语音候选映射 |
| `docs/voice_line_manifest.md` | 逐句正式配音清单 |
| `docs/missing_assets.md` | 后续缺失素材说明 |
| `docs/task_log.md` | 第三阶段执行日志 |

## 最终检查

| 检查项 | 结果 |
|---|---|
| Ren'Py lint | 通过 |
| lint 命令 | `/tmp/renpy-8.3.7-sdk/renpy.sh dragon_pact_renpy lint` |
| lint 时间 | 2026-04-29 18:22:56 |
| 旧缓存处理 | lint 前已删除 `game/cache/` 与 `game/*.rpyc`，lint 后 Ren'Py 重新生成新缓存 |
| 系统绝对字体路径 | 未发现旧系统字体绝对路径 |
| 说明 MD 是否误入 `game/` | 未发现 |
| label/jump | 通过 |
| HUD 引用 | 仅 `game/script.rpy` 的 `demon_arrival` 一处 |
| 非语音关键资源路径 | 通过；`fonts/NotoSansSC-Regular.ttf` 为可选首选字体，缺失时回退到已存在的 `fonts/SourceHanSansSC-Regular.otf` |
| 正式 voice 文件 | 允许缺失，已通过 `safe_voice()` 安全跳过 |

## 后续需要用户补充

- 按 `docs/voice_line_manifest.md` 补正式配音 `.ogg`。
- 复核 `game/audio/voice_candidates/male/` 的 12 个男主候选片段，确认是否采用为临时占位。
- 为 `zhao_cold.png` 与 `zhao_normal.png` 补同名人工透明 PNG。
- 可选补充 `game/fonts/NotoSansSC-Regular.ttf`；当前已有 `SourceHanSansSC-Regular.otf`，中文显示不受影响。
