# 缺失与后续建议素材

第一版 Demo 已可使用当前素材启动制作，不阻塞运行。后续建议补充：

- 透明背景角色立绘 PNG：用于传统视觉小说叠加站位。
- 游戏 Logo 透明 PNG：用于主菜单、启动画面、打包图标。
- 中文字体：当前已内置 `game/fonts/SourceHanSansSC-Regular.otf` 并在 `gui.rpy` 中通过相对路径引用。
- 可选补充：若后续希望使用首选文件名，可添加 `game/fonts/NotoSansSC-Regular.ttf`；字体选择逻辑会优先使用它。
- 正式配音文件：当前只接入了安全播放路径，`game/audio/voice/narrator/`、`male/`、`li/`、`zhao/`、`seal/` 下的逐句 `.ogg` 仍需按 `docs/voice_line_manifest.md` 录制补齐。
- 男主临时候选语音：已生成 `game/audio/voice_candidates/male/`，仅供试听复核，不会覆盖正式配音。
- 赵无炎透明立绘：`zhao_cold.png` 与 `zhao_normal.png` 已从备份回退，当前不是主要脚本引用立绘；后续建议补同名人工透明 PNG。
- 按钮音效：悬停、确认、取消已接入；翻页等额外 UI 音效可继续补充。
- 场景音效：封印嗡鸣、龙吟、兵器碰撞、魔化爆发、开门已接入；火焰、雷声等额外音效可继续补充。
- 游戏图标 `icon.png`：用于打包后的应用图标。
- 战斗 HUD 切片：血条、技能图标、状态栏独立素材。
- 分支提示小图标：信任龙、相信李将军、质疑赵无炎等。
