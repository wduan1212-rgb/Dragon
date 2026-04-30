# Stage 5 Ending Flow Report

## 本轮修复目标

修复所有结局播放结束后可能停在最后一帧、无法返回主菜单的问题，并把终局 CG 接入统一结尾流程。

## 采用的结尾顺序

本阶段采用以下顺序：

```text
对应结局图与结局对白
→ 播放 game/videos/ending_cg/final_cg.mp4
→ 显示 screen ending_menu
```

这样可以保留每个结局本身的静态结局图和对白，同时把最终 2 分钟 CG 作为统一终局演出。若 `final_cg.mp4` 缺失或播放失败，会安全跳过并进入结尾菜单。

## 结局跳转表

| 结局 label | 原末尾行为 | 新末尾行为 | 状态 |
|---|---|---|---|
| `ending_reseal` | 播放终局 CG 后进入旧 `ending_actions` | `call play_optional_ending_cg` 后 `jump show_ending_menu` | 已修复 |
| `ending_zhao_redemption` | 播放终局 CG 后进入旧 `ending_actions` | `call play_optional_ending_cg` 后 `jump show_ending_menu` | 已修复 |
| `ending_li_sacrifice` | 播放终局 CG 后进入旧 `ending_actions` | `call play_optional_ending_cg` 后 `jump show_ending_menu` | 已修复 |
| `ending_fail` | 播放终局 CG 后进入旧 `ending_actions` | `call play_optional_ending_cg` 后 `jump show_ending_menu` | 已修复 |
| `ending_watch` | 播放终局 CG 后进入旧 `ending_actions` | `call play_optional_ending_cg` 后 `jump show_ending_menu` | 已修复 |

## 新增 ending_menu

已新增 `screen ending_menu()`，包含：

- 返回主菜单：`MainMenu(confirm=False)`
- 重新开始：`Jump("start")`
- 查看图鉴：`ShowMenu("gallery")`
- 退出游戏：`Quit(confirm=True)`

## 兼容保留

- 旧 `label ending_actions` 仍保留，但现在只负责跳转到 `show_ending_menu`，避免旧存档或旧跳转目标卡住。
- `label show_ending_menu` 负责隐藏窗口和战斗 HUD，再调用 `screen ending_menu`。

## 安全性

- `play_optional_ending_cg` 默认播放 `videos/ending_cg/final_cg.mp4`。
- 播放前隐藏战斗 HUD 并停止 BGM，让终局 CG 原声优先。
- 视频缺失、编码失败或播放异常时，标签会安全 pause 后返回，不阻塞进入结尾菜单。
