# Stage 6 Fix Report

## 完成内容

- 接入首页动态视频背景 `game/videos/menu/menu_bg_loop.mp4`，缺失时回退静态图。
- 追加修复：按用户要求将首页改为静态新图 `game/images/bg/title_bg_new.png`，不再使用首页视频背景。
- 追加修复：将加载页改为 `game/images/ui/loading_ui_new.png`，新图存在时不再叠加旧动态进度 UI。
- 替换角色选择页为 `game/images/ui/character_select_new.png`。
- 角色选择只允许选择主角，其他角色点击后提示未开放。
- 暂时禁用剧情过场动画与最终 CG 播放，避免视频流程卡死。
- 修复章节卡文字叠加：章节卡不再额外绘制中文标题。
- 移除普通剧情里的 battle HUD 显示。
- 所有结局不再播放 final CG，直接进入统一 `ending_menu`。
- 将部分未充分利用图片加入图鉴/剧情解锁，详见 `stage6_asset_utilization_report.md`。

## 修改文件

| 文件 | 说明 |
|---|---|
| `game/script.rpy` | 禁用剧情视频播放、禁用 final CG、清理 HUD、扩充图鉴条目与解锁 |
| `game/screens.rpy` | 新主菜单、首页视频背景、新角色选择热区、章节卡去叠字 |
| `docs/asset_manifest.md` | 记录第六阶段新增素材映射 |
| `docs/task_log.md` | 记录第六阶段修改与验证 |

## 新增报告

- `docs/stage6_menu_report.md`
- `docs/stage6_menu_video_report.md`
- `docs/stage6_character_select_replace_report.md`
- `docs/stage6_ui_cleanup_report.md`
- `docs/stage6_ending_menu_report.md`
- `docs/stage6_asset_utilization_report.md`

## 验证结果

| 检查 | 结果 |
|---|---|
| Ren'Py lint | 通过 |
| Ren'Py compile | 通过 |
| label/jump 静态检查 | 通过 |
| 必要素材路径检查 | 通过 |
| `.md` 是否误入 `game/` | 未发现 |
| 旧系统字体路径 | 未发现 |
| 剧情过场 / final CG 播放调用 | 未发现 |
| battle HUD 脚本引用 | 未发现 |

## 验证命令

```text
/tmp/renpy-8.3.7-sdk/renpy.sh dragon_pact_renpy lint
/tmp/renpy-8.3.7-sdk/renpy.sh --compile dragon_pact_renpy compile
```

最终 lint 时间：2026-04-29 22:52:33。
