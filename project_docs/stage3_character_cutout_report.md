# Stage 3 Character Cutout Report

## 处理原则

- 处理范围仅限 `game/images/characters/`。
- 修复前已备份到 `raw_assets_backup/stage3_characters_before_fix/`。
- 对轻微白边仅做保守边缘清理。
- 对疑似被自动抠坏的赵无炎立绘执行回退，并把坏图放入 `review_needed/stage3_bad_cutout/`。

## 检查结果

| 文件 | Alpha | 当前处理 | 脚本使用状态 | 后续建议 |
|---|---|---|---|---|
| `li_normal.png` | 有 | 保守清理白边 | 未在当前主线直接显示 | 可继续人工精修边缘 |
| `li_angry.png` | 有 | 保守清理白边 | 未在当前主线直接显示 | 可继续人工精修边缘 |
| `li_battle.png` | 有 | 保守清理白边 | 已用于李将军拦路段落 | 可用，建议后续人工精修脚底阴影 |
| `li_sad.png` | 有 | 保守清理白边 | 未在当前主线直接显示 | 可继续人工精修边缘 |
| `male_normal.png` | 有 | 保持现状 | 未在当前主线直接显示 | 可用 |
| `male_angry.png` | 有 | 保持现状 | 未在当前主线直接显示 | 可用 |
| `male_hurt.png` | 有 | 保持现状 | 未在当前主线直接显示 | 可用 |
| `male_serious.png` | 有 | 保持现状 | 已用于赵无炎对峙段落 | 可用 |
| `male_shadow.png` | 有 | 保持现状 | 未在当前主线直接显示 | 可用 |
| `zhao_shadow.png` | 有 | 保持现状 | 已用于赵无炎幻影段落 | 可用，视觉上为紫色半透明幻影 |
| `zhao_pain.png` | 有 | 保持现状 | 未在当前主线直接显示 | 可用 |
| `zhao_cold.png` | 无 | 从备份回退，不继续强抠 | 当前未被脚本引用 | 需要人工替换透明 PNG |
| `zhao_normal.png` | 无 | 从备份回退，不继续强抠 | 当前未被脚本引用 | 需要人工替换透明 PNG |

## 坏图回退记录

| 回退文件 | 坏图存放位置 | 原因 |
|---|---|---|
| `game/images/characters/zhao_cold.png` | `review_needed/stage3_bad_cutout/zhao_cold_bad_cutout.png` | 自动透明化版本存在脸部/发丝损伤风险。 |
| `game/images/characters/zhao_normal.png` | `review_needed/stage3_bad_cutout/zhao_normal_bad_cutout.png` | 自动透明化版本存在脸部/发丝损伤风险。 |

## 结论

- 当前剧情主线使用的 `li_battle.png`、`male_serious.png`、`zhao_shadow.png` 均不会因为坏图回退阻塞运行。
- 赵无炎 `zhao_cold.png` 与 `zhao_normal.png` 暂不作为主要立绘参与脚本显示，等待用户补充同名人工透明 PNG。
