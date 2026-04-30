# Stage 3 UI Layer Report

## 修复范围

- 检查并调整 `game/script.rpy`、`game/screens.rpy` 中 HUD、角色、对话框、选项、快捷菜单的显示层级。
- 保持 `game/gui.rpy` 的项目内中文字体系统，不引入任何系统绝对字体路径。
- 普通剧情对白默认不显示 `battle_hud_overlay.png`。

## 层级规范

| 层级 | 当前实现 | 说明 |
|---|---|---|
| 背景 / CG | `scene expression fit_screen(...)` | 背景、CG、结局图铺满画面。 |
| 战斗 HUD | `zorder 5`，`alpha 0.18` | 只在 `demon_arrival` 的模拟战斗段落显示。 |
| 角色立绘 | `zorder 20` | 李将军、男主、赵无炎立绘高于 HUD。 |
| 对话框 / 名字条 / 文字 | `screen say`，`zorder 200` | 固定底部，永远高于角色与 HUD。 |
| 选项 | `screen choice`，`zorder 210` | 高于对话框区域，避免被 HUD 遮挡。 |
| 快捷菜单 | `screen quick_menu`，`zorder 220` | 右上角显示，不覆盖对白主体。 |
| 图片查看器 | `screen image_viewer`，`zorder 300` | 图鉴大图查看时位于最上层。 |

## 对话框与名字条

- `screen say` 使用固定底部区域，不再把 `textbox.png` 当全屏遮罩。
- 对话框尺寸固定为 `1580x282`，底部偏移 `30px`，位于安全区域内。
- 名字条绑定到对话框左上角，使用 `images/ui/nameplate.png`，无白底和英文残留。
- 角色名继续统一使用中文：`男主 / 李将军 / 赵无炎 / 龙灵`。

## 脚本检查

| 检查项 | 结果 |
|---|---|
| 普通对白是否显示 HUD | 否 |
| 李将军对白是否被 HUD 覆盖 | 否，李将军立绘 `zorder 20`，对白层 `zorder 200` |
| 赵无炎对白是否被 HUD 覆盖 | 否，赵无炎幻影段落未显示 HUD |
| 模拟战斗段落 HUD 透明度 | `alpha 0.18`，低于建议上限 |
| `battle_hud_overlay.png` 出现场景 | 仅 `demon_arrival` |

## 备注

本轮以 Ren'Py lint 与脚本层静态检查为准。若后续继续做视觉验收，建议截取普通对白、李将军对白、赵无炎对白、模拟战斗段落四张画面复核构图。
