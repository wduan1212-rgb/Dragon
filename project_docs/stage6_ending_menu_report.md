# Stage 6 Ending Menu Report

## 结尾流程

所有结局完成最后对白后直接进入 `show_ending_menu`，不再播放最终 CG。

| 结局 label | 结尾行为 |
|---|---|
| `ending_reseal` | 解锁结局与开放结局图后进入 ending_menu |
| `ending_zhao_redemption` | 解锁结局后进入 ending_menu |
| `ending_li_sacrifice` | 解锁结局后进入 ending_menu |
| `ending_fail` | 解锁坏结局相关图后进入 ending_menu |
| `ending_watch` | 解锁普通结尾与隐藏结局图后进入 ending_menu |

## ending_menu 按钮

| 按钮 | 行为 |
|---|---|
| 返回主菜单 | `MainMenu(confirm=False)` |
| 重新开始 | `Jump("start")` |
| 查看图鉴 | `ShowMenu("gallery")` |
| 退出游戏 | `Quit(confirm=True)` |

## 防卡死措施

- 不再调用最终 2 分钟 CG。
- 不停在最后一张结局图。
- 旧 `ending_actions` label 保留，并转向 `show_ending_menu`，兼容旧跳转。
