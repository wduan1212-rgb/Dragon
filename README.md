# 《龙之契》

《龙之契》是一款东方玄幻视觉小说 / 互动剧情 Demo，使用 Ren'Py 8.x 制作。当前版本聚焦主线剧情、角色选择、CG 图鉴、多个结局与基础音频演出。

## 当前版本

v0.1.0 Demo

## 本地运行

1. 安装 Ren'Py 8.x。
2. 打开 Ren'Py Launcher。
3. 选择本项目目录 `dragon_pact_renpy/`。
4. 点击 Launch Project 启动。

也可以下载桌面发行版，解压后运行对应平台的启动程序。桌面版压缩包建议通过 GitHub Release 发布，不建议直接提交到 `main` 分支。

## GitHub Pages 在线试玩

当前自动 Web/HTML5 构建暂未完成，网页版暂未开放。修复并成功生成 Web 版本后，可在 GitHub 仓库 Settings → Pages 中选择 `main` 分支 `/docs` 目录发布，在线地址通常为：

https://wduan1212-rgb.github.io/Dragon/

如果该地址暂时无法打开，说明 GitHub Pages 尚未启用、部署尚未完成，或当前版本仍未上传 Web 构建产物。

## 素材说明

本项目素材用于个人作品集、课程展示与测试版本。请勿将本仓库中的素材直接用于未授权的商业用途。

## 开发说明

- 正式运行素材保存在 `game/images/`、`game/audio/`、`game/fonts/` 与部分 `game/videos/` 目录中。
- `game/cache/`、`*.rpyc`、存档、构建缓存与超大参考素材不会提交到 GitHub。
- 已禁用的过场动画和最终 CG 不会在当前剧情流程中自动播放。
