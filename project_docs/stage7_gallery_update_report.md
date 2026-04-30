# Stage 7 Gallery Update Report

## 图鉴接入

- 新增 `story_cg_catalog`，并通过 `cg_catalog.extend(story_cg_catalog)` 接入现有图鉴系统。
- 已加入图鉴的补充 CG 数量：38。
- 图鉴标题按四类标注：前期铺垫、真相推进、高潮爆发、战后余波。

## 解锁逻辑

- 新增 `label show_story_cg(key, path, hold=0.75)`。
- 每张补充 CG 在剧情中显示后会调用 `unlock_cg(key)`。
- 未观看的补充 CG 在图鉴中保持锁定。

## 安全保护

- `screen gallery_row` 已增加 `renpy.loadable(path)` 检查。
- 如果某张已加入图鉴的图片后续被移动或删除，图鉴不会崩溃；该项会保持不可点状态。
- `screen image_viewer` 也增加了文件存在判断。
