# Asset Transparency Report

生成时间：2026-04-29

范围：只处理 `game/images/characters/` 与指定 UI 叠加素材；未处理背景、CG、结局图、首尾帧与视频。

备份目录：`raw_assets_backup/`。高风险复核目录：`review_needed/`。

环境说明：未检测到 `rembg`，本轮使用 Pillow。角色立绘使用边缘背景色连通剔除，兼容浅底与暗底；UI 使用棋盘格/浅底连通区域剔除。

| 文件路径 | 原格式/模式 | 原有 alpha | 需要透明底 | 已处理 | 处理方法 | 处理后尺寸/alpha | 需人工复核 |
|---|---|---:|---:|---:|---|---|---:|
| `game/images/characters/li_angry.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/li_battle.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/li_normal.png` | PNG / RGB / 1024x1536 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1024x1536 / 是 (0, 255) | 是 |
| `game/images/characters/li_sad.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/male_angry.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/male_hurt.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/male_normal.png` | PNG / RGB / 1024x1536 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1024x1536 / 是 (0, 255) | 是 |
| `game/images/characters/male_serious.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/male_shadow.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/zhao_cold.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/zhao_normal.png` | PNG / RGB / 1024x1536 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1024x1536 / 是 (0, 255) | 是 |
| `game/images/characters/zhao_pain.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/characters/zhao_shadow.png` | PNG / RGB / 1086x1448 | 否 | 是 | 是 | Pillow 边缘背景色连通剔除（浅底/暗底），轻微羽化 | RGBA / 1086x1448 / 是 (0, 255) | 是 |
| `game/images/ui/textbox.png` | PNG / RGB / 1672x941 | 否 | 是 | 是 | Pillow 棋盘格/浅底连通区域剔除，并裁切透明外边距 | RGBA / 1657x580 / 是 (0, 255) | 否 |
| `game/images/ui/nameplate.png` | PNG / RGB / 2508x627 | 否 | 是 | 是 | 原图含内嵌英文，已重制为干净透明中文名字条；原图保留在备份目录 | RGBA / 620x138 / 是 (0, 235) | 是 |
| `game/images/ui/choice_button_idle.png` | PNG / RGB / 2172x724 | 否 | 是 | 是 | Pillow 棋盘格/浅底连通区域剔除，并裁切透明外边距 | RGBA / 2017x495 / 是 (0, 255) | 否 |
| `game/images/ui/choice_button_hover.png` | PNG / RGB / 2172x724 | 否 | 是 | 是 | Pillow 棋盘格/浅底连通区域剔除，并裁切透明外边距 | RGBA / 2155x620 / 是 (0, 255) | 否 |
| `game/images/ui/chapter_frame.png` | PNG / RGB / 2244x701 | 否 | 是 | 是 | Pillow 棋盘格/浅底连通区域剔除，并裁切透明外边距 | RGBA / 2171x701 / 是 (0, 255) | 否 |
| `game/images/ui/battle_hud_overlay.png` | PNG / RGB / 1672x941 | 否 | 是 | 是 | Pillow 棋盘格/浅底连通区域剔除，保留原画布定位 | RGBA / 1672x941 / 是 (0, 255) | 是 |

## 复核说明

- 角色立绘由算法自动抠图，发丝、武器尖端、披风边缘建议后续人工精修。
- `nameplate.png` 的复制品已重制为无英文、无棋盘格的透明中文名字条；原始复制品在 `raw_assets_backup/game/images/ui/nameplate.png`。
- `battle_hud_overlay.png` 保持 1672x941 原画布，避免 HUD 元素位置偏移。
- 背景、CG、结局图、首尾帧与视频未处理，符合第二阶段限制。
- `.rpy` 引用路径未变化，不需要同步修改图片扩展名或路径。
