# Stage 8 Voice Manifest Update

## 更新内容

第八阶段新增 57 句中文台词，并同步追加到 `docs/voice_line_manifest.md`。

## 新增 ID 范围

| 角色 | ID 范围 | 数量 |
|---|---|---:|
| 旁白 | `narrator_017` - `narrator_031` | 15 |
| 男主 | `male_016` - `male_036` | 21 |
| 李将军 | `li_008` - `li_015` | 8 |
| 赵无炎 | `zhao_010` - `zhao_016` | 7 |
| 龙灵 | `seal_005` - `seal_010` | 6 |

## 当前状态

- 所有新增语音文件均标记为“缺失”。
- `game/script.rpy` 已添加对应 `safe_voice()` 占位。
- 缺失语音不会导致游戏崩溃。
- 后续补配音时，可按 manifest 的文件路径直接放入 `game/audio/voice/` 对应角色目录。
