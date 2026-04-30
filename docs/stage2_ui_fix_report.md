# Stage 2 UI Fix Report

生成时间：2026-04-29

## 本轮目标

优先执行阶段 B-1 与 B-2，修复四个试玩问题：

- 对话框漂浮在画面中间。
- 名字条位置偏高、错位，并带有白底/棋盘格残留。
- 中文显示为方框字。
- 角色立绘与 UI 叠加素材不是透明底 PNG。

## B-1 对话框与名字条修复

修改文件：

- `game/screens.rpy`
- `game/gui.rpy`
- `game/script.rpy`

修复结果：

- `screen say` 不再把 `textbox.png` 作为全屏半透明图叠在画面上。
- 对话框固定在 1920x1080 画布底部，当前区域为宽 1580、高 282，底部留 30px 安全边距。
- 对话文本区域位于底部面板内部，使用深色半透明底提升可读性。
- 名字条绑定在对话框左上方，不再独立漂浮。
- 快捷菜单移动到右上角，避免覆盖底部对话框。
- 角色名显示统一为中文：男主、李将军、赵无炎、龙灵。

中文字体修复：

- `gui.text_font`、`gui.name_text_font`、`gui.interface_text_font` 已改为项目内相对路径字体选择逻辑。
- 当前内置 `game/fonts/SourceHanSansSC-Regular.otf`；若后续添加 `game/fonts/NotoSansSC-Regular.ttf`，会自动优先使用它。
- `style default`、`say_name`、`say_dialogue` 均使用该字体链路，避免中文方框字。

## B-2 透明底素材修复

修改内容：

- 建立 `raw_assets_backup/`，保存被处理素材的原始复制品。
- 建立 `review_needed/`，保存自动抠图后建议人工复核的角色与高风险 UI。
- 将 `game/images/characters/` 下所有角色立绘转换为带 alpha 的 PNG。
- 将 `textbox.png`、`nameplate.png`、`choice_button_idle.png`、`choice_button_hover.png`、`chapter_frame.png`、`battle_hud_overlay.png` 转换为带 alpha 的 PNG。
- `nameplate.png` 原复制品带有内嵌英文 “Li General”，已重制为干净透明中文名字条。

完整透明底处理明细见：

- `docs/asset_transparency_report.md`

## 显示检查结果

普通对白：

- 对话框贴底显示，不再漂浮。
- 中文文字使用显式 CJK 字体，预计不再出现方框字。
- “男主”名字条与对话框左上角对齐。

李将军对白：

- `李将军` 显示为中文角色名。
- 名字条不再露出棋盘格或英文标签。
- 角色立绘已具备 alpha 通道，叠加时不会用整张底色遮住背景。

赵无炎对白：

- `赵无炎` 显示为中文角色名。
- 幻影立绘已具备 alpha 通道，叠加到龙纹大厅时不会带白底/黑底整块遮罩。

选项界面：

- 选项按钮素材已具备 alpha 通道。
- 未修改菜单逻辑，三项选择仍按原流程跳转。

## 验证

- 已运行 Ren'Py 8.3.7 `lint`，通过。
- 已静态检查 `.rpy` 中的图片/视频引用路径，未发现缺失。

## 后续建议

- 角色自动抠图边缘建议美术复核，重点看发丝、武器尖端、披风末端。
- 后续如需替换字体，请放入 `game/fonts/` 并保持相对路径引用，避免打包后跨平台启动失败。
