# Deploy Check Report

生成时间：2026-04-30 14:45（Asia/Shanghai）

## 1. GitHub 上传状态

| 项目 | 结果 |
|---|---|
| 本地 Git 仓库 | 已初始化 |
| 远程仓库 | `https://github.com/wduan1212-rgb/Dragon.git` |
| 当前分支 | `main` |
| 源码上传 | 已成功 push |
| Web 发布提交 | 已随本报告所在提交推送 |

说明：

- 源码已经上传到 GitHub `main` 分支。
- 前期 push 曾遇到网络/HTTPS 连接不稳定，后续重试已成功。
- 本轮将提交 `docs/` Web 构建产物，用于 GitHub Pages 从 `/docs` 发布。

## 2. Web/HTML5 构建状态

| 项目 | 结果 |
|---|---|
| RenPyWeb 支持包 | 已安装到临时 SDK `/tmp/renpy-8.3.7-sdk/web` |
| 命令行 Web 构建 | 成功 |
| `docs/index.html` | 存在 |
| `docs/game.zip` | 约 18MB |
| `docs/` 总大小 | 约 304MB |
| 单个超 95MB 文件 | 未发现 |

构建命令：

```bash
/tmp/renpy-8.3.7-sdk/renpy.sh /tmp/renpy-8.3.7-sdk web_build "$PWD/dragon_pact_renpy" --destination "$PWD/dragon_pact_renpy_web_build"
```

处理记录：

- 初次 Web 构建成功但包体过大，`game.zip` 超过 GitHub 单文件上传限制。
- 已更新 `game/options.rpy` 的构建分类规则，排除开发文档、原始素材备份、禁用视频、参考语音与候选语音。
- 重新构建后 `game.zip` 降至约 18MB，可提交到 GitHub。
- 旧开发文档已移动到 `project_docs/`，`docs/` 专用于 GitHub Pages。

## 3. 项目结构检查

| 检查项 | 结果 |
|---|---|
| `game/` | 存在 |
| `README.md` | 存在并已更新 |
| `docs/index.html` | 存在 |
| `project_docs/` | 存在，保存开发报告 |
| `.gitignore` | 已创建 |
| iCloud 占位文件 | 未发现 `.icloud` 文件 |
| 当前路径 | `/Users/macbookpro/Desktop/龙之契game/game企划/dragon_pact_renpy` |

当前路径不在 `~/Library/Mobile Documents/` 或 `CloudDocs` 下，未检测到典型 iCloud 占位文件。

## 4. Ren'Py 检查

| 检查项 | 结果 |
|---|---|
| Ren'Py lint | 通过 |
| 最后一次 lint 时间 | 2026-04-30 14:33:17 |
| Web 构建 | 成功 |
| 已禁用视频过场 | 未重新接入 |
| 最终 CG 视频 | 未重新接入 |

## 5. 缺失资源检查

未发现会阻断启动或 Web 构建的必需资源缺失。

发现的非阻塞缺失项：

- `game/fonts/NotoSansSC-Regular.ttf`：缺失，但项目已有 `game/fonts/SourceHanSansSC-Regular.otf`，中文字体可用。
- `game/audio/bgm/bgm_new_ending.wav`：缺失，但 `bgm_new_ending.ogg` 已存在，WAV 只是 fallback。
- `game/audio/voice/**` 下正式逐句语音文件缺失：当前全部通过 `safe_voice()` 安全跳过，不会导致崩溃。

## 6. 超大文件与提交策略

发现的本地超大文件仍不建议提交到 `main`：

| 文件 | 大小 | 处理建议 |
|---|---:|---|
| `game/audio/source_voice/raw/cg_audio_reference_01.mp3` | 约 197MB | 不进 main，后续可放 Release 或 Git LFS |
| `game/videos/ending_cg/ending_final_cg.mp4` | 约 197MB | 不进 main，后续可放 Release 或 Git LFS |
| `game/videos/ending_cg/final_cg.mp4` | 约 175MB | 不进 main，后续可放 Release 或 Git LFS |
| `raw_assets_backup/stage5_videos/final_cg_source_hevc.mp4` | 约 197MB | 不进 main，本地备份 |

本轮 Web 构建与 Git 提交未包含以上超大文件。

## 7. Web 加载风险

- `docs/` 包含 RenPyWeb 运行所需的 `index.html`、`renpy.wasm`、`renpy.data`、`game.zip` 与 progressive download 文件。
- 当前 Web 构建未包含禁用的视频过场和最终 CG，降低浏览器端加载风险。
- 图片素材较多，首次加载仍可能偏慢。后续可继续压缩 PNG/JPG 或微调 progressive download 策略。
- 音频文件较多但未发现单个超限文件；如网页加载慢，可优先压缩 BGM 与 SFX。

## 8. GitHub Pages 建议

建议开启 GitHub Pages：

1. 打开 GitHub 仓库页面。
2. 进入 Settings。
3. 点击 Pages。
4. Source 选择 `Deploy from a branch`。
5. Branch 选择 `main`。
6. Folder 选择 `/docs`。
7. 点击 Save。
8. 等待 1-3 分钟。
9. 打开 `https://wduan1212-rgb.github.io/Dragon/`。

本机环境未安装 `gh`，且没有可用的 GitHub Pages API 认证工具，因此 Pages 开关可能需要在 GitHub 网页中手动启用。

## 9. 下一步建议

- 本轮提交并 push 后，优先在 GitHub 仓库 Settings → Pages 打开 `/docs` 发布。
- 如果网页首次打开较慢，优先检查浏览器控制台中是否有资源 404 或音频加载失败。
- 桌面发行版 zip 不建议提交到 `main` 分支，后续应通过 GitHub Release 上传。
