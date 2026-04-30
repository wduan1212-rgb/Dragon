# Task Log

## 2026-04-29

### 阶段 1：项目初始化

- 创建 `dragon_pact_renpy/` Ren'Py 项目目录。
- 创建 `game/images/`、`game/videos/`、`game/audio/` 与 `docs/` 子目录。
- 将中文原始素材复制到项目内，并按指南转换为英文文件名。
- 保留原始 `图片素材/`、`过场动画/`、`首尾帧/` 文件夹不变。
- 新增 `docs/asset_manifest.md` 与 `docs/missing_assets.md`。

### 阶段 2：最小可运行 Demo

- 新增 `game/options.rpy`，设置游戏名、版本、1920x1080 分辨率与构建配置。
- 新增 `game/gui.rpy`，设置基础 UI 色彩与文字尺寸。
- 新增 `game/script.rpy`，实现角色选择、加载、视频播放降级、封印之门剧情、分支选择与 5 个结局。

### 阶段 3：界面系统

- 新增 `game/screens.rpy`，实现主菜单、对话框、选项按钮、加载界面、存档、读取、设置与图鉴。
- 图鉴使用 persistent 记录已解锁 CG 与结局。

### 验证

- 检查脚本内 50 个 `images/` 与 `videos/` 引用，均能在 `game/` 下找到对应文件。
- 检查 `script.rpy` 中所有 `jump` 目标，均存在对应 label。
- 临时下载 Ren'Py 8.3.7 SDK 后执行 `renpy.sh dragon_pact_renpy lint`，lint 通过。

## 2026-04-29 第二阶段 B-1 / B-2

### 对话框与名字条定位修复

- 修改 `game/screens.rpy`，重写 `screen say` 的底部对话框布局。
- 对话框从全屏半透明叠图改为固定底部面板，避免漂浮在画面中间。
- 名字条贴合对话框左上方，并将快捷菜单移到右上角，避免覆盖对白。
- 修改 `game/gui.rpy`，为中文字体接入项目内相对路径，修复中文方框字风险。
- 修改 `game/script.rpy`，统一角色名显示为男主、李将军、赵无炎、龙灵。

### 透明底素材规范化

- 新建 `raw_assets_backup/`，备份所有被处理的角色/UI 原图复制品。
- 新建 `review_needed/`，放置自动抠图后建议人工复核的角色与高风险 UI。
- 将 `game/images/characters/` 角色立绘转换为 RGBA 透明底 PNG。
- 将 `textbox.png`、`choice_button_idle.png`、`choice_button_hover.png`、`chapter_frame.png`、`battle_hud_overlay.png` 转换为 RGBA 透明底 PNG。
- `nameplate.png` 原复制品带有内嵌英文，已重制为干净透明中文名字条。
- 新增 `docs/asset_transparency_report.md` 与 `docs/stage2_ui_fix_report.md`。

### 验证

- 使用 Ren'Py 8.3.7 执行 `renpy.sh dragon_pact_renpy lint`，lint 通过。

## 2026-04-29 第三阶段修复与音频接入

### UI 层级与对话框

- 修改 `game/screens.rpy`，为 `screen say`、`screen choice`、`screen quick_menu` 设置明确 zorder。
- 修改 `game/script.rpy`，普通剧情不再显示 `battle_hud_overlay.png`。
- 将战斗 HUD 限定到 `demon_arrival` 段落，使用 `zorder 5` 与 `alpha 0.18`，避免盖住角色和对白。
- 保持对话框固定在底部，名字条绑定到对话框左上角，角色名继续使用中文。

### 角色透明底与坏图回退

- 备份 `game/images/characters/` 到 `raw_assets_backup/stage3_characters_before_fix/`。
- 对李将军系列立绘执行保守白边清理。
- 将自动抠图风险较高的 `zhao_cold.png` 与 `zhao_normal.png` 从备份回退，并把坏图移入 `review_needed/stage3_bad_cutout/`。
- 当前脚本未引用回退后的 `zhao_cold.png` 与 `zhao_normal.png`，避免坏图成为主要立绘。

### 中文命名音频与终局 CG 整理

- 扫描 `音频素材/` 与项目根目录终局 CG，复制/转换为英文安全路径。
- 新增 `game/audio/bgm/`、`game/audio/sfx/`、`game/audio/source_voice/`、`game/audio/voice_candidates/` 与 `game/videos/ending_cg/` 等规范目录。
- 将 BGM/SFX 转为 `.ogg`，终局 CG 复制为 `game/videos/ending_cg/ending_final_cg.mp4`。
- 从用户提供的参考音频与 CG 音轨提取 source voice，并切分 12 个男主临时候选片段。

### 安全音频系统与脚本接入

- 新增 `game/audio.rpy`，提供 `safe_voice`、`safe_bgm`、`stop_bgm`、`safe_sfx`。
- 修改 `game/script.rpy`，为 BGM、SFX、逐句语音和可选终局 CG 播放接入安全逻辑。
- 修改 `game/screens.rpy`，为主菜单、角色选择、图鉴与 UI 按钮接入安全 BGM/SFX。
- 修改 `game/options.rpy`，将 `game/audio/**` 纳入构建归档。

### 文档

- 新增或更新 `docs/stage3_ui_layer_report.md`、`docs/stage3_character_cutout_report.md`、`docs/stage3_ui_asset_report.md`、`docs/stage3_audio_system_report.md`。
- 新增或更新 `docs/stage3_raw_asset_rename_map.md`、`docs/bgm_mapping.md`、`docs/ending_cg_mapping.md`、`docs/stage3_audio_video_update_report.md`。
- 新增 `docs/voice_line_manifest.md`、`docs/voice_candidate_manifest.md`、`docs/voice_temp_mapping.md`。
- 更新 `docs/missing_assets.md`，记录正式配音、赵无炎人工透明 PNG 等后续补充项。

### 验证

- 删除旧 `game/cache/` 与 `game/*.rpyc` 后重新运行 Ren'Py lint。
- 删除旧 `game/cache/` 与 `game/*.rpyc` 后，使用 Ren'Py 8.3.7 执行 `/tmp/renpy-8.3.7-sdk/renpy.sh dragon_pact_renpy lint`，lint 通过。
- 检查未发现旧系统字体绝对路径。
- 检查未发现 `.md` 文件误放入 `game/` 目录。
- 检查 `jump` 目标均有对应 label。
- 检查 `battle_hud_overlay.png` 仅在 `demon_arrival` 段落显示。

## 2026-04-29 字体系统修复

- 新建 `game/fonts/`，并加入项目内中文字体 `game/fonts/SourceHanSansSC-Regular.otf`。
- 修改 `game/gui.rpy`，移除 macOS 系统绝对字体路径，改为优先加载 `fonts/NotoSansSC-Regular.ttf`，其次加载 `fonts/SourceHanSansSC-Regular.otf`，缺失时回退 Ren'Py 默认字体。
- 补齐 `gui.button_text_font`、`gui.choice_button_text_font`、`gui.label_text_font` 等字体定义，统一使用项目内字体选择逻辑。
- 修改 `game/screens.rpy`，让标题、按钮、选项、菜单、图鉴、提示文本等样式显式使用对应字体变量。
- 修改 `game/options.rpy`，将 `game/fonts/**` 纳入构建归档。
- 更新 `docs/missing_assets.md` 与 `docs/stage2_ui_fix_report.md`，删除旧的系统字体路径说明。
- 删除 `game/cache/` 下的旧缓存文件，并移除旧 `.rpyc`，避免 Ren'Py 继续读取含旧字体路径的编译缓存。
- 使用 Ren'Py 8.3.7 执行 `renpy.sh dragon_pact_renpy lint`，lint 通过。

## 2026-04-29 第五阶段过场动画与结尾菜单

### 视频素材整理

- 扫描根目录 `过场动画/`，整理 5 个中文命名过场视频。
- 新建 `game/videos/cutscenes/`，复制并重命名为 `cutscene_01_opening_gate.mp4` 到 `cutscene_05_gate_open.mp4`。
- 复制根目录 `龙之契-cg.mp4`，转码为正式播放文件 `game/videos/ending_cg/final_cg.mp4`。
- 将原始 HEVC 终局 CG 备份到 `raw_assets_backup/stage5_videos/final_cg_source_hevc.mp4`。

### 剧情接入

- 修改 `game/script.rpy`，开场过场接入 `opening_sequence`。
- 修改 `game/script.rpy`，李将军登场与赵无炎幻影过场接入 `seal_gate_chapter`。
- 修改 `game/script.rpy`，魔化登场与封印门开启过场接入 `demon_arrival`。
- `play_cutscene` 播放前隐藏战斗 HUD；视频缺失或播放失败时继续使用首尾帧降级。

### 结尾流程

- 修改 `play_optional_ending_cg` 默认播放 `videos/ending_cg/final_cg.mp4`。
- 新增 `screen ending_menu()`，包含返回主菜单、重新开始、查看图鉴、退出游戏。
- 新增 `label show_ending_menu`，所有结局播放终局 CG 后统一跳转到该菜单。
- 保留旧 `ending_actions` label，并改为跳转新结尾菜单，避免旧存档或旧跳转目标卡住。

### 文档与验证

- 新增 `docs/stage5_video_asset_report.md`。
- 新增 `docs/stage5_cutscene_mapping.md`。
- 新增 `docs/stage5_ending_flow_report.md`。
- 新增 `docs/stage5_final_report.md`。
- 删除旧 `game/cache/` 与 `game/*.rpyc` 后，使用 Ren'Py 8.3.7 执行 `/tmp/renpy-8.3.7-sdk/renpy.sh dragon_pact_renpy lint`，lint 通过。

## 2026-04-29 第六阶段简化稳定修复

### 首页与角色选择

- 复制 `主页面动画.mp4` 到 `game/videos/menu/menu_bg_loop.mp4`。
- 修改 `game/screens.rpy`，主菜单优先使用首页循环视频背景，缺失时回退静态主菜单图。
- 精简主菜单按钮为开始游戏、图鉴、设置、退出。
- 复制 `新版角色选择页面.png` 到 `game/images/ui/character_select_new.png`。
- 修改 `screen character_select`，新版角色选择图作为完整底图，只保留透明热区。
- 主角卡片与开始按钮可进入主线；李将军、赵无炎、龙灵点击后提示“该角色暂未开放”。

### 流程简化与 UI 清理

- 修改 `play_cutscene`，暂时不播放剧情过场动画，只显示首尾帧。
- 修改 `play_optional_ending_cg`，暂时不播放最终 CG。
- 修改 `screen chapter_title`，去掉程序额外标题文字，只显示章节卡图片本身。
- 移除剧情中的 `battle_hud_overlay` 显示，普通剧情与全屏 CG 不再叠加战斗 HUD。
- 所有结局结束后直接进入 `ending_menu`，不再停在最后一帧。

### 素材利用

- 将 `cg_zhao_demon_intro.png` 接入魔化登场静态 CG。
- 将新魔王、赵无炎彻底魔化、龙契断裂、龙灵回响等额外结局图加入图鉴列表，并在相关结局中解锁。
- 新增 `docs/stage6_asset_utilization_report.md`，记录未充分利用图片素材的当前处理与后续建议。

### 文档与验证

- 新增 `docs/stage6_fix_report.md`。
- 新增 `docs/stage6_menu_report.md`。
- 新增 `docs/stage6_menu_video_report.md`。
- 新增 `docs/stage6_character_select_replace_report.md`。
- 新增 `docs/stage6_ui_cleanup_report.md`。
- 新增 `docs/stage6_ending_menu_report.md`。
- 使用 Ren'Py 8.3.7 执行 `/tmp/renpy-8.3.7-sdk/renpy.sh dragon_pact_renpy lint`，lint 通过。
- 使用 Ren'Py 8.3.7 执行 `/tmp/renpy-8.3.7-sdk/renpy.sh --compile dragon_pact_renpy compile`，compile 通过。
- 静态检查 label/jump、必要资源路径、说明文件位置、字体路径、禁用视频调用与 HUD 引用，均通过。

## 2026-04-29 首页与加载页静态图替换

- 复制 `主菜单背景图 新.png` 到 `game/images/bg/title_bg_new.png`。
- 复制 `加载页面 新.png` 到 `game/images/ui/loading_ui_new.png`。
- 修改 `game/screens.rpy`，主菜单不再优先播放 `videos/menu/menu_bg_loop.mp4`，改为使用新静态首页图。
- 修改 `screen loading_screen`，新加载图存在时直接显示完整新图，不再叠加旧动态进度文字和进度条。
- 更新 `docs/asset_manifest.md`、`docs/stage6_menu_report.md`、`docs/stage6_menu_video_report.md` 与 `docs/stage6_fix_report.md`。

## 2026-04-30 第七阶段补充剧情 CG 接入

### 素材整理

- 扫描 `素材图 新 补充版/`，识别 38 张补充剧情 CG。
- 新建 `game/images/cg/story/prologue/`、`truth/`、`climax/`、`aftermath/`。
- 将中文命名的前期铺垫图复制并整理为英文规范命名。
- 将已英文命名的 truth、climax、aftermath 图直接归类复制。
- 新增 `game/story_cg_definitions.rpy`，定义 38 个 `cg_*` image。

### 剧情与图鉴接入

- 修改 `game/script.rpy`，新增 `story_cg_catalog` 并并入现有 `cg_catalog`。
- 新增 `show_story_cg()`，显示前检查 `renpy.loadable()`，缺图时安全跳过。
- 将前期铺垫、真相推进、高潮爆发、战后余波 CG 按剧情节奏插入主线。
- 修改 `game/screens.rpy`，为图鉴行和大图查看器加入文件存在保护。

### 复核与报告

- 新增 `docs/stage7_cg_asset_report.md`。
- 新增 `docs/stage7_cg_mapping.md`。
- 新增 `docs/stage7_gallery_update_report.md`。
- 新增 `docs/stage7_story_insert_report.md`。
- 新增 `docs/stage7_manual_review_needed.md`。
- 新增 `docs/stage7_final_report.md`。
- 记录缺失的 `story_first_look_temple.png` 与 `story_hero_li_standoff.png`，本轮未接入，避免缺图崩溃。

### 验证

- 使用 Ren'Py 8.3.7 执行 `/tmp/renpy-8.3.7-sdk/renpy.sh dragon_pact_renpy lint`，lint 通过。
- 使用 Ren'Py 8.3.7 执行 `/tmp/renpy-8.3.7-sdk/renpy.sh --compile dragon_pact_renpy compile`，compile 通过。
- 静态检查 label/jump、必要资源路径、说明文件位置、系统绝对字体路径、视频过场调用与 HUD 引用，均通过。

## 2026-04-30 第八阶段剧情台词扩写与新结尾 BGM 替换

### 剧情扩写

- 根据 `龙之契_第八阶段剧情台词扩写与新结尾BGM替换_Codex_审核版.md` 执行。
- 修改 `game/script.rpy`，在第七阶段新增 CG 周围补充 57 句中文台词。
- 扩写开场、第一章封印门前、李将军登场、紫焰第一次闪现、真相推进、高潮爆发与五个结局余波。
- 新增台词保持短句为主，重点承接角色反应、迟疑、打断和选择压力。
- 为所有新增台词加入 `safe_voice()` 占位，缺失语音时不会影响运行。

### 新结尾 BGM

- 备份 `新结尾bgm.mp4` 到 `raw_assets_backup/stage8_audio_backup/新结尾bgm.mp4`。
- 将 `新结尾bgm.mp4` 的音轨转换为 `game/audio/bgm/bgm_new_ending.ogg`。
- 修改 `game/audio.rpy`，新增 `safe_ending_bgm()`，优先播放新结尾 BGM，缺失时回退 `bgm_ending_watch.ogg`。
- 修改 `game/script.rpy`，正向结局使用 `safe_ending_bgm()`；坏结局继续使用 `bgm_bad_ending.ogg`。

### 文档

- 更新 `docs/bgm_mapping.md`。
- 更新 `docs/voice_line_manifest.md`。
- 新增 `docs/stage8_dialogue_expansion_report.md`。
- 新增 `docs/stage8_bgm_update_report.md`。
- 新增 `docs/stage8_voice_manifest_update.md`。
- 新增 `docs/stage8_final_report.md`。

### 验证

- 使用 Ren'Py 8.3.7 执行 `/tmp/renpy-8.3.7-sdk/renpy.sh dragon_pact_renpy lint`，lint 通过，最终时间 2026-04-30 13:28:33。
- 使用 Ren'Py 8.3.7 执行 `/tmp/renpy-8.3.7-sdk/renpy.sh --compile dragon_pact_renpy compile`，compile 通过。
- 静态检查说明文件位置、系统绝对字体路径、视频过场调用、final CG 调用、battle HUD 引用与 BGM 目录，均通过。
