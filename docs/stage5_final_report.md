# Stage 5 Final Report

## 完成内容

- 扫描并整理根目录 `过场动画/` 中的 5 个中文命名视频。
- 将过场动画复制到 `game/videos/cutscenes/`，统一英文规范命名。
- 将最终 CG 复制并转码为 `game/videos/ending_cg/final_cg.mp4`。
- 将开场、李将军登场、赵无炎幻影、魔化登场、封印门开启接入剧情节点。
- 保留并强化视频安全降级：视频缺失或播放失败时显示首尾帧。
- 新增 `screen ending_menu()` 与 `label show_ending_menu`。
- 所有结局都改为播放终局 CG 后进入统一结尾菜单。
- 旧 `ending_actions` 已改为跳转到新结尾菜单，避免旧流程卡住。

## 修改文件

| 文件 | 修改说明 |
|---|---|
| `game/script.rpy` | 更新过场动画路径、终局 CG 路径、结局跳转、视频播放前隐藏 HUD |
| `game/screens.rpy` | 新增 `screen ending_menu()` 与相关样式 |
| `docs/stage5_video_asset_report.md` | 新增视频资源整理报告 |
| `docs/stage5_cutscene_mapping.md` | 新增过场动画剧情接入表 |
| `docs/stage5_ending_flow_report.md` | 新增结尾流程修复报告 |
| `docs/task_log.md` | 追加第五阶段执行记录 |

## 新增/整理视频

| 文件 | 用途 |
|---|---|
| `game/videos/cutscenes/cutscene_01_opening_gate.mp4` | 开场过场 |
| `game/videos/cutscenes/cutscene_02_li_intro.mp4` | 李将军登场 |
| `game/videos/cutscenes/cutscene_03_zhao_shadow.mp4` | 赵无炎幻影 |
| `game/videos/cutscenes/cutscene_04_zhao_demon.mp4` | 魔化登场 |
| `game/videos/cutscenes/cutscene_05_gate_open.mp4` | 封印门开启 |
| `game/videos/ending_cg/final_cg.mp4` | 统一终局 CG |

## 最终检查

| 检查项 | 结果 |
|---|---|
| Ren'Py lint | 通过 |
| lint 命令 | `/tmp/renpy-8.3.7-sdk/renpy.sh dragon_pact_renpy lint` |
| lint 时间 | 2026-04-29 22:16:14 |
| 缓存处理 | lint 前已删除旧 `game/cache/` 与 `game/*.rpyc`，lint 后 Ren'Py 重新生成新缓存 |
| 过场视频路径 | 已统一指向 `game/videos/cutscenes/` |
| 终局 CG 路径 | 已统一指向 `game/videos/ending_cg/final_cg.mp4` |
| 结局卡住风险 | 已修复，所有结局进入 `ending_menu` |
| 视频失败降级 | 已保留首尾帧降级 |
| `.md` 是否误入 `game/` | 未发现 |

## 后续建议

- 用 Ren'Py 启动后实际走一遍五个剧情节点，确认视频内容与剧情节奏完全贴合。
- 如果后续需要减小包体，可以把第三阶段旧视频副本迁入备份区，再统一更新构建策略。
