# Stage 6 UI Cleanup Report

## 章节卡修复

- `screen chapter_title` 不再叠加程序文本。
- `label show_chapter` 只显示章节卡图片本身。
- 章节卡淡入 0.5 秒，停留 1.5 秒，淡出 0.5 秒。
- 章节卡显示期间隐藏对话窗口，不显示名字条和 HUD。

## HUD 清理

- 第六阶段暂时禁用 `battle_hud_overlay.png` 在剧情中的显示。
- `script.rpy` 中不再 `show battle_hud`。
- 普通剧情、全屏 CG、结局图默认只显示自身画面和必要对白。
- 静态检查确认 `game/*.rpy` 中没有 `battle_hud_overlay` 引用。

## 视频流程简化

- `play_cutscene` 不再播放 `game/videos/cutscenes/` 视频，只显示首尾帧。
- `play_optional_ending_cg` 不再播放最终 CG，直接返回。
- `game/*.rpy` 中不再引用 `videos/cutscenes/` 或 `videos/ending_cg/final_cg.mp4`。

## 素材本身提示

若某张图片素材内部已经绘制了 UI、英文装饰或 HUD 风格元素，代码无法单独隐藏其内嵌内容；这类问题需后续替换为干净图。本轮已避免额外叠加代码层 HUD。
