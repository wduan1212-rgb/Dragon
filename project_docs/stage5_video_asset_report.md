# Stage 5 Video Asset Report

## 目录整理

- 已确保 `game/videos/cutscenes/` 存在。
- 已确保 `game/videos/ending_cg/` 存在。
- 已确保 `raw_inbox/过场动画/` 与 `raw_inbox/终局CG/` 存在，供后续继续投放素材。
- 原始中文命名素材未删除。

## 过场动画整理表

| 原始路径 | 新路径 | 格式/编码 | 时长 | 大小 | 复制状态 | 是否建议转码 | 剧情节点 |
|---|---|---|---:|---:|---|---|---|
| `过场动画/开场视频.mp4` | `game/videos/cutscenes/cutscene_01_opening_gate.mp4` | MP4 / H.264 + AAC | 00:00:10.05 | 8,245,180 bytes | 已复制 | 否 | 开场山道到封印之门 |
| `过场动画/李将军登场.mp4` | `game/videos/cutscenes/cutscene_02_li_intro.mp4` | MP4 / H.264 + AAC | 00:00:06.06 | 5,079,818 bytes | 已复制 | 否 | 李将军登场 |
| `过场动画/赵无炎幻影.mp4` | `game/videos/cutscenes/cutscene_03_zhao_shadow.mp4` | MP4 / H.264 + AAC | 00:00:07.06 | 5,873,108 bytes | 已复制 | 否 | 赵无炎幻影出现 |
| `过场动画/魔化登场.mp4` | `game/videos/cutscenes/cutscene_04_zhao_demon.mp4` | MP4 / H.264 + AAC | 00:00:07.06 | 5,873,101 bytes | 已复制 | 否 | 魔化赵无炎登场 |
| `过场动画/封印之门开启.mp4` | `game/videos/cutscenes/cutscene_05_gate_open.mp4` | MP4 / H.264 + AAC | 00:00:07.06 | 5,901,783 bytes | 已复制 | 否 | 龙契共鸣后封印门开启 |

## 终局 CG 整理表

| 原始路径 | 新路径 | 格式/编码 | 时长 | 大小 | 处理状态 | 是否建议转码 | 用途 |
|---|---|---|---:|---:|---|---|---|
| `龙之契-cg.mp4` | `game/videos/ending_cg/final_cg.mp4` | MP4 / H.264 + AAC | 00:02:48.55 | 183,836,646 bytes | 已复制并转码为 H.264 正式播放版 | 已完成 | 所有结局后的终局 CG |
| `龙之契-cg.mp4` | `raw_assets_backup/stage5_videos/final_cg_source_hevc.mp4` | MP4 / HEVC + AAC | 00:02:48.53 | 206,790,864 bytes | 已备份原始 HEVC 版本 | 不作为正式播放文件 | 源文件备份 |

## 说明

- 五个过场动画本身已经是 H.264 + AAC，适合直接接入 Ren'Py。
- 终局 CG 原始视频为 HEVC，跨平台播放风险较高；正式 `final_cg.mp4` 已转为 H.264 + AAC，保留视频原声。
- `game/videos/ending_cg/ending_final_cg.mp4` 是第三阶段旧命名副本，保留不删；第五阶段脚本改用 `final_cg.mp4`。
