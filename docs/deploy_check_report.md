# Deploy Check Report

生成时间：2026-04-30 14:05（Asia/Shanghai）

## 1. GitHub 上传状态

| 项目 | 结果 |
|---|---|
| 本地 Git 仓库 | 已初始化 |
| 远程仓库 | `https://github.com/wduan1212-rgb/Dragon.git` |
| 本地源码提交 | 已创建并推送源码与部署报告提交 |
| push 到 GitHub | 已成功 |

push 结果说明：

- 第一次 push 失败：`Error in the HTTP2 framing layer`。
- 第二次 push 使用 HTTP/1.1 后失败：`HTTP 408`、`remote end hung up unexpectedly`。
- 随后的 `git ls-remote` 也因无法连接 GitHub 失败：`Failed to connect to github.com port 443`。
- 第三次执行 `git gc` 后重新 push 成功，随后报告修正也已推送到远端 `main`。
- 当前判断：源码仓库已成功上传，前两次失败是网络/HTTPS 连接不稳定导致。

## 2. Web/HTML5 构建状态

| 项目 | 结果 |
|---|---|
| 命令行 Web 构建 | 失败 |
| `docs/index.html` | 不存在 |
| 是否已复制 Web 构建到 `docs/` | 否 |

尝试命令：

```bash
/tmp/renpy-8.3.7-sdk/renpy.sh /tmp/renpy-8.3.7-sdk web_build "$PWD/dragon_pact_renpy" --destination "$PWD/dragon_pact_renpy_web_build"
```

失败原因：

- 当前 Ren'Py SDK 未安装 RenPyWeb 支持包。
- Launcher 内部变量 `WEB_PATH` 为 `None`。
- 构建在“Preparing progressive download”阶段报错：

```text
TypeError: expected str, bytes or os.PathLike object, not NoneType
```

已处理：

- 没有把半成品 Web 输出复制到 `docs/`。
- 临时半成品目录 `dragon_pact_renpy_web_build/` 已删除，避免误部署。
- `docs/` 仍保留为开发文档目录。

## 3. 项目结构检查

| 检查项 | 结果 |
|---|---|
| `game/` | 存在 |
| `README.md` | 存在并已更新 |
| `docs/` | 存在 |
| `.gitignore` | 已创建 |
| iCloud 占位文件 | 未发现 `.icloud` 文件 |
| 当前路径 | `/Users/macbookpro/Desktop/龙之契game/game企划/dragon_pact_renpy` |

当前路径不在 `~/Library/Mobile Documents/` 或 `CloudDocs` 下，未检测到典型 iCloud 占位文件。

## 4. Ren'Py 检查

| 检查项 | 结果 |
|---|---|
| Ren'Py lint | 通过 |
| 最后一次 lint 时间 | 2026-04-30 14:10:26 |
| 对话块 | 108 |
| 菜单 | 2 |
| image 定义 | 38 |
| screens | 17 |

## 5. 缺失资源检查

未发现缺失的必需图片、BGM、SFX 或视频首尾帧。

发现的非阻塞缺失项：

- `game/fonts/NotoSansSC-Regular.ttf`：缺失，但项目已有 `game/fonts/SourceHanSansSC-Regular.otf`，中文字体可用。
- `game/audio/bgm/bgm_new_ending.wav`：缺失，但 `bgm_new_ending.ogg` 已存在，WAV 只是 fallback。
- `game/audio/voice/**` 下正式逐句语音文件缺失：当前全部通过 `safe_voice()` 安全跳过，不会导致崩溃。

## 6. 超大文件与提交策略

发现的本地超大文件：

| 文件 | 大小 | 处理建议 |
|---|---:|---|
| `game/audio/source_voice/raw/cg_audio_reference_01.mp3` | 约 197MB | 不进 main，后续可放 Release 或 Git LFS |
| `game/videos/ending_cg/ending_final_cg.mp4` | 约 197MB | 不进 main，后续可放 Release 或 Git LFS |
| `game/videos/ending_cg/final_cg.mp4` | 约 175MB | 不进 main，后续可放 Release 或 Git LFS |
| `raw_assets_backup/stage5_videos/final_cg_source_hevc.mp4` | 约 197MB | 不进 main，本地备份 |

已通过 `.gitignore` 排除：

- `game/cache/`
- `game/saves/`
- `*.rpyc`
- `raw_assets_backup/`
- `raw_inbox/`
- `review_needed/`
- `game/videos/ending_cg/`
- `game/audio/source_voice/`
- `game/audio/voice_candidates/`

## 7. Web 加载风险

可能影响 Web 版本的因素：

- 当前 Ren'Py SDK 缺少 RenPyWeb 支持包，必须先安装。
- Web 平台对视频支持有限；当前剧情流程没有重新启用视频过场和最终 CG。
- 已在 `game/options.rpy` 中将禁用的过场视频、终局 CG、参考语音和候选语音排除出构建包，降低 Web 体积和加载风险。
- 图片素材较多，Web 首次加载仍可能偏慢，后续可以考虑压缩 PNG 或配置 progressive download。

## 8. GitHub Pages 建议

当前不建议立即开启 GitHub Pages，因为 Web 构建未成功，`docs/index.html` 不存在。

修复 Web 构建后，建议：

1. 使用 Ren'Py Launcher 安装 RenPyWeb 支持。
2. 重新构建 Web 版本。
3. 将包含 `index.html` 的 Web 输出复制到 `docs/`。
4. 若 `docs/` 中已有开发文档，先移动到 `project_docs/` 或 `docs_dev_backup/`。
5. 再提交并 push。

## 9. 下一步建议

### 上传源码

源码已成功上传。后续如需再次上传新增修改：

```bash
cd "/Users/macbookpro/Desktop/龙之契game/game企划/dragon_pact_renpy"
git add .
git commit -m "Your commit message"
git push
```

### 生成 Web 版本

请在 Ren'Py Launcher 中执行：

1. 打开 Ren'Py Launcher。
2. 选择《龙之契》项目。
3. 点击“网页 / Web”。
4. 按提示下载/安装 RenPyWeb 支持包。
5. 点击“Build Web Application”。
6. 找到生成的 Web 构建目录。

### 桌面发行版

桌面发行版 zip 不建议提交到 `main` 分支。后续应通过 GitHub Release 上传。
