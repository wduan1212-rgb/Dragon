# Stage 8 BGM Update Report

## 新素材

| 原始文件 | 备份位置 | 项目文件 |
|---|---|---|
| `新结尾bgm.mp4` | `raw_assets_backup/stage8_audio_backup/新结尾bgm.mp4` | `game/audio/bgm/bgm_new_ending.ogg` |

## 转换结果

- 原文件为 MP4/MOV 容器，包含 AAC 音频轨。
- 已提取音频并转为 OGG/Vorbis。
- 项目内文件为 44.1kHz、立体声，约 20 秒。
- 游戏运行时不依赖系统绝对路径或外部转码工具。

## 接入逻辑

新增 `safe_ending_bgm()`：

1. 优先播放 `audio/bgm/bgm_new_ending.ogg`。
2. 若 OGG 缺失，尝试播放 `audio/bgm/bgm_new_ending.wav`。
3. 若新结尾 BGM 均缺失，回退 `audio/bgm/bgm_ending_watch.ogg`。

## 使用位置

| label | 第八阶段处理 |
|---|---|
| `ending_reseal` | 使用 `safe_ending_bgm()` |
| `ending_zhao_redemption` | 使用 `safe_ending_bgm()` |
| `ending_li_sacrifice` | 使用 `safe_ending_bgm()` |
| `ending_fail` | 保留 `bgm_bad_ending.ogg` |
| `ending_watch` | 使用 `safe_ending_bgm()` |

## 保留策略

旧 `bgm_ending_watch.ogg` 没有覆盖或删除，继续作为安全回退资源。
