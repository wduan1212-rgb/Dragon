# Stage 5 Cutscene Mapping

## 剧情接入表

| 顺序 | 视频文件 | 接入 label | 接入位置 | 降级首帧 | 降级尾帧 | 状态 |
|---:|---|---|---|---|---|---|
| 1 | `videos/cutscenes/cutscene_01_opening_gate.mp4` | `opening_sequence` | 加载结束后，正式进入密令与封印之门前 | `images/frames/opening_start.png` | `images/frames/opening_end.png` | 已接入 |
| 2 | `videos/cutscenes/cutscene_02_li_intro.mp4` | `seal_gate_chapter` | 主角抵达封印门，李将军对白前 | `images/frames/li_intro_start.png` | `images/frames/li_intro_end.png` | 已接入 |
| 3 | `videos/cutscenes/cutscene_03_zhao_shadow.mp4` | `seal_gate_chapter` | 李将军警告后，赵无炎幻影出现前 | `images/frames/zhao_shadow_start.png` | `images/frames/zhao_shadow_end.png` | 已接入 |
| 4 | `videos/cutscenes/cutscene_04_zhao_demon.mp4` | `demon_arrival` | 玩家完成关键选择后，Boss 对峙前 | `images/frames/zhao_demon_start.png` | `images/frames/zhao_demon_end.png` | 已接入 |
| 5 | `videos/cutscenes/cutscene_05_gate_open.mp4` | `demon_arrival` | 龙契共鸣对白后，进入结局选择前 | `images/frames/gate_open_start.png` | `images/frames/gate_open_end.png` | 已接入 |

## 安全播放逻辑

- 所有过场动画都通过 `label play_cutscene(video_path, start_frame, end_frame, hold=0.8)` 播放。
- 播放前执行 `window hide` 与 `hide battle_hud`。
- 若视频存在且 Ren'Py 能播放，则调用 `renpy.movie_cutscene(video_path)`。
- 若视频缺失或播放抛错，则自动显示对应首尾帧，不会崩溃或黑屏卡住。

## 旧路径处理

- 第三阶段旧路径 `game/videos/opening_path_to_gate.mp4`、`li_intro_blocking_path.mp4`、`zhao_shadow_summon.mp4`、`zhao_demon_transformation.mp4`、`gate_open_sequence.mp4` 保留不删。
- 第五阶段脚本引用已统一改为 `game/videos/cutscenes/` 下的英文规范命名文件。
