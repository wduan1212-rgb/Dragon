# Stage 3 UI Asset Report

## 复查范围

| 文件 | Alpha | 当前用途 | 处理结论 |
|---|---|---|---|
| `game/images/ui/textbox.png` | 有 | 底部对话框贴图 | 可用，不再全屏拉伸。 |
| `game/images/ui/nameplate.png` | 有 | 名字条 | 可用，已为透明中文名字条，无英文残留。 |
| `game/images/ui/choice_button_idle.png` | 有 | 选项/主按钮普通态 | 可用。 |
| `game/images/ui/choice_button_hover.png` | 有 | 选项/主按钮悬停态 | 可用。 |
| `game/images/ui/chapter_frame.png` | 有 | 章节标题框 | 可用。 |
| `game/images/ui/battle_hud_overlay.png` | 有 | 模拟战斗 HUD | 仅在战斗段落低透明度显示。 |

## 使用层面修复

- `textbox.png` 只在 `screen say` 的底部固定区域显示。
- `nameplate.png` 绑定在对话框左上方，避免独立漂浮。
- `choice_button_idle.png` 与 `choice_button_hover.png` 继续作为按钮 `Frame` 背景。
- `battle_hud_overlay.png` 从普通剧情对白中移除，只保留在 `demon_arrival`，并以 `alpha 0.18`、`zorder 5` 显示。
- `character_select_ui.png`、`save_bg.png`、`load_bg.png`、`settings_bg.png`、`gallery_bg.png`、`loading_ui.png` 是全屏背景类 UI，未要求透明，保持原样。

## 结论

本阶段未发现对话框、名字条、选项按钮、章节框、战斗 HUD 存在会阻塞运行的白底或棋盘格残留。后续可继续把 HUD 拆成更细切片，以便做真正的战斗演示界面。
