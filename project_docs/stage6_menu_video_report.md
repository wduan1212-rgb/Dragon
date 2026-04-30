# Stage 6 Menu Video Report

## 首页视频整理

| 原始文件 | 新文件 | 格式 | 时长 | 大小 | 接入状态 |
|---|---|---|---:|---:|---|
| `主页面动画.mp4` | `game/videos/menu/menu_bg_loop.mp4` | MP4 / H.264 | 00:00:15.04 | 24,415,867 bytes | 已保留但不再由主菜单引用 |

## 当前规则

- `screen main_menu` 现在优先显示 `images/bg/title_bg_new.png`。
- 如果新图缺失，则回退旧静态首页图。
- 主菜单不再检查或播放 `videos/menu/menu_bg_loop.mp4`。
- 主菜单 BGM 仍由 `safe_bgm("audio/bgm/bgm_title_theme.ogg")` 管理，视频不承担流程控制。

## 兼容性

- 首页视频文件保留在项目中，便于后续恢复动态首页。
- 当前版本按用户要求使用静态首页新图。
