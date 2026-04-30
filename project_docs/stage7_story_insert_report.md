# Stage 7 Story Insert Report

## 新增显示标签

新增 `label show_story_cg(key, path, hold=0.75)`：

- 显示前隐藏窗口。
- 使用 `renpy.loadable(path)` 检查文件。
- 文件存在才全屏显示并解锁图鉴。
- 文件缺失时直接返回，不阻塞剧情。

## 接入位置

| 段落 | 接入 CG |
|---|---|
| 开场进入封印门前 | `story_order_night`、`story_mountain_road_run` |
| 第一章封印门前期铺垫 | `story_refugees_escape`、`story_gate_closeup_storm`、`story_seal_disturbance`、`story_stone_tablet` |
| 李将军登场前后 | `story_li_first_appearance`、`story_purple_flame_hint` |
| 赵无炎幻影与选择前 | 全部 10 张 `truth_*` 真相推进 CG |
| 终局冲突前 | 全部 10 张 `climax_*` 高潮爆发 CG |
| 各结局后段 | 按结局分配显示 `aftermath_*` 战后余波 CG |

## 视频状态

第七阶段没有重新启用剧情过场动画或最终 CG。当前仍沿用第六阶段的稳定策略：剧情过场只走静态首尾帧，结尾直接进入 `ending_menu`。

## UI 清理

补充 CG 以 `scene expression fit_screen(path)` 全屏显示，不显示 battle HUD、Boss 血条、技能 UI 或章节标题。
