# Stage 3 Audio System Report

## 新增安全播放系统

已新增 `game/audio.rpy`，提供以下函数：

| 函数 | 用途 | 缺失文件行为 |
|---|---|---|
| `safe_voice(path)` | 播放逐句语音 | 静默跳过 |
| `safe_bgm(path, fadein=1.0, loop=True, volume=1.0)` | 播放 BGM | 静默跳过 |
| `stop_bgm(fadeout=1.0)` | 停止 BGM | 安全停止 |
| `safe_sfx(path)` | 播放音效 | 静默跳过 |

所有函数都通过 `renpy.loadable(path)` 检查文件是否存在，不会因为缺失 voice/BGM/SFX 让游戏崩溃。

## 目录状态

| 目录 | 状态 |
|---|---|
| `game/audio/bgm/` | 已创建并放入转换后的 BGM |
| `game/audio/sfx/` | 已创建并放入转换后的 SFX |
| `game/audio/voice/narrator/` | 已创建，等待正式配音 |
| `game/audio/voice/male/` | 已创建，等待正式配音 |
| `game/audio/voice/li/` | 已创建，等待正式配音 |
| `game/audio/voice/zhao/` | 已创建，等待正式配音 |
| `game/audio/voice/seal/` | 已创建，等待正式配音 |
| `game/audio/source_voice/` | 已创建，用于保存用户参考音频与提取音轨 |
| `game/audio/voice_candidates/male/` | 已创建，保存临时男主候选切片 |

## BGM 接入

- 主菜单：`bgm_title_theme.ogg`
- 角色选择：`bgm_character_select.ogg`
- 加载界面：`bgm_loading_dark.ogg`
- 开场山道：`bgm_dark_mountain.ogg`
- 封印之门：`bgm_fortress_tension.ogg`
- 赵无炎幻影：`bgm_zhao_shadow.ogg`
- 魔化/Boss 段落：`bgm_boss_phase1.ogg`
- 龙契共鸣：`bgm_dragon_resonance.ogg`
- 好结局/守望山河：`bgm_ending_watch.ogg`
- 坏结局：`bgm_bad_ending.ogg`
- 图鉴：`bgm_gallery_ambient.ogg`

## SFX 接入

- UI 悬停、确认、返回：`sfx_ui_hover.ogg`、`sfx_ui_confirm.ogg`、`sfx_ui_back.ogg`
- 加载进度：`sfx_loading_tick.ogg`、`sfx_loading_complete.ogg`
- 封印门与龙契：`sfx_seal_hum.ogg`、`sfx_gate_open.ogg`、`sfx_dragon_roar_low.ogg`
- 战斗表现：`sfx_weapon_clash.ogg`、`sfx_magic_burst.ogg`

## 语音与候选库

- `docs/voice_line_manifest.md` 已导出逐句正式配音清单。
- `docs/voice_candidate_manifest.md` 已记录从用户参考音频切出的 12 个男主候选片段。
- `docs/voice_temp_mapping.md` 仅作为试听占位建议，不会覆盖正式 `game/audio/voice/`。

## 构建配置

`game/options.rpy` 已把 `game/audio/**` 纳入构建归档，后续打包时会包含音频资源。
