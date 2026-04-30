# Stage 6 Character Select Replace Report

## 新素材整理

| 原始文件 | 新文件 | 尺寸 | 接入状态 |
|---|---|---:|---|
| `新版角色选择页面.png` | `game/images/ui/character_select_new.png` | 1672x941 | 已接入 |

## 角色选择逻辑

- 新角色选择图作为完整全屏底图使用。
- 不再叠加旧角色卡、旧边框或额外角色说明。
- 仅保留透明点击热区。

## 热区设置

| 区域 | 行为 |
|---|---|
| 主角卡片 | `Return("protagonist")`，进入后续主线 |
| 开始冒险按钮 | `Return("protagonist")`，进入后续主线 |
| 李将军卡片 | 提示“该角色暂未开放” |
| 赵无炎卡片 | 提示“该角色暂未开放” |
| 龙灵卡片 | 提示“该角色暂未开放” |
| 返回按钮 | 返回主菜单 |

## 回退规则

如果 `game/images/ui/character_select_new.png` 缺失，`screen character_select` 会回退到旧 `character_select_ui.png`，并保持只允许选择主角。
