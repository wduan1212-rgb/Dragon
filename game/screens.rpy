transform fit_screen_t:
    xysize (config.screen_width, config.screen_height)

transform dim_fit(alpha_value=0.42):
    xysize (config.screen_width, config.screen_height)
    alpha alpha_value

screen main_menu():
    tag menu

    on "show" action Function(safe_bgm, "audio/bgm/bgm_title_theme.ogg", 1.5, True, 0.82)

    if renpy.loadable("images/bg/title_bg_new.png"):
        add "images/bg/title_bg_new.png" at fit_screen_t
    else:
        add ("images/endings/ending_title_unlocked.png" if getattr(persistent, "demo_cleared", False) else "images/bg/title_bg.png") at fit_screen_t

    add Solid("#00000072")
    add Solid("#06101a55")

    frame:
        xpos 120
        ypos 110
        xsize 700
        ysize 250
        background None

        vbox:
            spacing 18

            text _("龙之契") style "title_text"
            text _("封印将启，契约由你执笔") style "subtitle_text"

    vbox:
        xpos 1340
        ypos 610
        spacing 16

        textbutton _("开始游戏") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), Start()] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "main_menu_button"
        textbutton _("图鉴") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), ShowMenu("gallery")] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "main_menu_button"
        textbutton _("设置") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), ShowMenu("preferences")] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "main_menu_button"
        textbutton _("退出") action [Function(safe_sfx, "audio/sfx/sfx_ui_back.ogg"), Quit(confirm=True)] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "main_menu_button"

screen character_select():
    tag menu

    on "show" action Function(safe_bgm, "audio/bgm/bgm_character_select.ogg", 1.0, True, 0.78)

    if renpy.loadable("images/ui/character_select_new.png"):
        add "images/ui/character_select_new.png" at fit_screen_t

        button:
            xpos 36
            ypos 226
            xysize (214, 590)
            background None
            hover_background Solid("#5fb3ff20")
            action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), Return("protagonist")]

        button:
            xpos 260
            ypos 245
            xysize (155, 520)
            background None
            hover_background Solid("#00000025")
            action [Function(safe_sfx, "audio/sfx/sfx_ui_back.ogg"), Notify(_("该角色暂未开放"))]

        button:
            xpos 430
            ypos 245
            xysize (155, 520)
            background None
            hover_background Solid("#00000025")
            action [Function(safe_sfx, "audio/sfx/sfx_ui_back.ogg"), Notify(_("该角色暂未开放"))]

        button:
            xpos 606
            ypos 245
            xysize (145, 520)
            background None
            hover_background Solid("#00000025")
            action [Function(safe_sfx, "audio/sfx/sfx_ui_back.ogg"), Notify(_("该角色暂未开放"))]

        button:
            xpos 1460
            ypos 905
            xysize (400, 95)
            background None
            hover_background Solid("#5fb3ff18")
            action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), Return("protagonist")]

        button:
            xpos 1540
            ypos 1008
            xysize (260, 62)
            background None
            hover_background Solid("#ffffff12")
            action [Function(safe_sfx, "audio/sfx/sfx_ui_back.ogg"), MainMenu(confirm=False)]

    else:
        add "images/ui/character_select_ui.png" at fit_screen_t
        add Solid("#00000033")

        button:
            xalign 0.5
            yalign 0.5
            xysize (640, 820)
            background None
            hover_background Solid("#ffffff18")
            action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), Return("protagonist")]

        textbutton _("确认主角") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), Return("protagonist")] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "primary_button":
            xalign 0.5
            yalign 0.9

        textbutton _("返回") action [Function(safe_sfx, "audio/sfx/sfx_ui_back.ogg"), MainMenu(confirm=False)] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "small_menu_button":
            xalign 0.04
            yalign 0.06

screen loading_screen(progress=0, note="正在同步龙契"):
    if renpy.loadable("images/ui/loading_ui_new.png"):
        add "images/ui/loading_ui_new.png" at fit_screen_t
    else:
        add "images/ui/loading_ui.png" at fit_screen_t
        add Solid("#00000055")

        vbox:
            xalign 0.5
            yalign 0.82
            xsize 920
            spacing 18

            hbox:
                xfill True
                text note style "loading_text"
                text "[progress]%" style "loading_text":
                    xalign 1.0

            bar:
                value progress
                range 100
                xsize 920
                ysize 18
                left_bar Solid("#d6ad59")
                right_bar Solid("#16110f")
                thumb None
                thumb_shadow None

screen chapter_title(title=None):
    modal False
    add Solid("#00000055")
    add "images/ui/chapter_frame.png":
        xalign 0.5
        yalign 0.5
        xysize (920, 288)

screen say(who, what):
    zorder 200

    fixed:
        xysize (config.screen_width, config.screen_height)

        $ box_w = 1580
        $ box_h = 282
        $ box_x = int((config.screen_width - box_w) / 2)
        $ box_y = config.screen_height - box_h - 30

        add "images/ui/textbox.png":
            xpos box_x
            ypos box_y
            xysize (box_w, box_h)

        if who is not None:
            add "images/ui/nameplate.png":
                xpos box_x + 58
                ypos box_y - 48
                xysize (470, 104)

            frame:
                id "namebox"
                xpos box_x + 170
                ypos box_y - 25
                xsize 330
                ysize 58
                background None
                padding (0, 0, 0, 0)

                text who id "who" style "say_name":
                    yalign 0.5

        frame:
            id "window"
            xpos box_x + 120
            ypos box_y + 92
            xsize box_w - 240
            ysize 148
            background Solid("#05070bd2")
            padding (28, 18, 28, 18)

            text what id "what" style "say_dialogue"

screen choice(items):
    zorder 210
    vbox:
        xalign 0.5
        yalign 0.52
        spacing 18

        for i in items:
            textbutton i.caption action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), i.action] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "choice_button"

screen quick_menu():
    zorder 220

    if quick_menu:
        hbox:
            xalign 0.98
            yalign 0.04
            spacing 10

            textbutton _("存档") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), ShowMenu("save")] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "quick_button"
            textbutton _("读取") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), ShowMenu("load")] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "quick_button"
            textbutton _("设置") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), ShowMenu("preferences")] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "quick_button"

screen save():
    tag menu
    use file_slots(_("存档"), "images/ui/save_bg.png")

screen load():
    tag menu
    use file_slots(_("读取"), "images/ui/load_bg.png")

screen file_slots(title, bg_path):
    add bg_path at fit_screen_t
    add Solid("#00000066")

    text title style "menu_title":
        xpos 110
        ypos 78

    grid 3 2:
        xpos 120
        ypos 210
        spacing 28

        for slot in range(1, 7):
            button:
                action FileAction(slot)
                style "slot_button"

                vbox:
                    spacing 10
                    add FileScreenshot(slot):
                        xysize (430, 242)
                    text FileTime(slot, format="%Y.%m.%d  %H:%M", empty=_("空档位")) style "slot_text"
                    text FileSaveName(slot) style "slot_text"

    hbox:
        xalign 0.5
        yalign 0.94
        spacing 16

        textbutton _("上一页") action FilePagePrevious() style "small_menu_button"
        textbutton _("自动") action FilePage("auto") style "small_menu_button"
        textbutton _("快速") action FilePage("quick") style "small_menu_button"
        textbutton _("下一页") action FilePageNext() style "small_menu_button"
        textbutton _("返回") action Return() style "small_menu_button"

screen preferences():
    tag menu

    add "images/ui/settings_bg.png" at fit_screen_t
    add Solid("#00000070")

    text _("设置") style "menu_title":
        xpos 110
        ypos 78

    frame:
        xpos 130
        ypos 210
        xsize 980
        ysize 650
        padding (42, 38, 42, 38)
        background Solid("#0a070bdc")

        vbox:
            spacing 32

            text _("显示模式") style "section_text"
            hbox:
                spacing 16
                textbutton _("窗口") action Preference("display", "window") style "small_menu_button"
                textbutton _("全屏") action Preference("display", "fullscreen") style "small_menu_button"

            text _("文字速度") style "section_text"
            bar value Preference("text speed") xsize 780 ysize 18

            text _("自动前进") style "section_text"
            bar value Preference("auto-forward time") xsize 780 ysize 18

            text _("音量") style "section_text"
            bar value Preference("music volume") xsize 780 ysize 18
            bar value Preference("sound volume") xsize 780 ysize 18
            bar value Preference("voice volume") xsize 780 ysize 18

    textbutton _("返回") action Return() style "small_menu_button":
        xalign 0.92
        yalign 0.9

screen gallery():
    tag menu

    on "show" action Function(safe_bgm, "audio/bgm/bgm_gallery_ambient.ogg", 1.0, True, 0.55)

    add "images/ui/gallery_bg.png" at fit_screen_t
    add Solid("#00000068")

    text _("龙契图鉴") style "menu_title":
        xpos 110
        ypos 78

    viewport:
        xpos 120
        ypos 190
        xsize 1340
        ysize 760
        mousewheel True
        draggable True

        vbox:
            spacing 16

            for title, key, path in cg_catalog:
                use gallery_row(title, key, path, "cg")

            for title, key, path in ending_catalog:
                use gallery_row(title, key, path, "ending")

    textbutton _("返回") action Return() style "small_menu_button":
        xalign 0.92
        yalign 0.9

screen gallery_row(title, key, path, kind):
    $ cg_unlocks = getattr(persistent, "unlocked_cgs", []) or []
    $ ending_unlocks = getattr(persistent, "unlocked_endings", []) or []
    $ available = renpy.loadable(path)
    $ unlocked = ((key in cg_unlocks) if kind == "cg" else (key in ending_unlocks)) and available

    button:
        xsize 1280
        ysize 156
        background Solid("#0b080cd8")
        hover_background Solid("#1f1720e6")
        action (Show("image_viewer", title=title, path=path) if unlocked and available else NullAction())

        hbox:
            spacing 24
            xfill True
            yalign 0.5

            if unlocked:
                add path:
                    xysize (240, 135)
                vbox:
                    yalign 0.5
                    spacing 8
                    text title style "gallery_title"
                    text _("已解锁") style "gallery_meta"
            else:
                frame:
                    xysize (240, 135)
                    background Solid("#111111")
                    text _("未解锁") style "locked_text":
                        xalign 0.5
                        yalign 0.5
                vbox:
                    yalign 0.5
                    spacing 8
                    text title style "gallery_title"
                    text _("推进剧情后解锁") style "gallery_meta"

screen image_viewer(title, path):
    modal True
    zorder 300

    add Solid("#000000ee")
    if renpy.loadable(path):
        add path at fit_screen_t
    else:
        add Solid("#111111")
    add Solid("#00000044")

    text title style "viewer_title":
        xalign 0.5
        yalign 0.06

    textbutton _("关闭") action Hide("image_viewer") style "small_menu_button":
        xalign 0.5
        yalign 0.94

screen confirm(message, yes_action, no_action):
    modal True
    zorder 250

    add Solid("#000000aa")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        padding (46, 42, 46, 42)
        background Solid("#0d090ddf")

        vbox:
            spacing 30
            text message style "section_text":
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 20
                textbutton _("确认") action yes_action style "small_menu_button"
                textbutton _("取消") action no_action style "small_menu_button"

screen notify(message):
    zorder 200
    frame:
        xalign 0.5
        yalign 0.08
        padding (28, 18, 28, 18)
        background Solid("#0b080cd8")
        text message style "notify_text"
    timer 2.0 action Hide("notify")

screen ending_menu():
    modal True
    zorder 320

    add Solid("#000000aa")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 680
        padding (44, 40, 44, 40)
        background Solid("#0a070be8")

        vbox:
            xalign 0.5
            spacing 22

            text _("契约已结") style "ending_menu_title":
                xalign 0.5

            textbutton _("返回主菜单") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), MainMenu(confirm=False)] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "ending_menu_button"
            textbutton _("重新开始") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), Jump("start")] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "ending_menu_button"
            textbutton _("查看图鉴") action [Function(safe_sfx, "audio/sfx/sfx_ui_confirm.ogg"), ShowMenu("gallery")] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "ending_menu_button"
            textbutton _("退出游戏") action [Function(safe_sfx, "audio/sfx/sfx_ui_back.ogg"), Quit(confirm=True)] hovered Function(safe_sfx, "audio/sfx/sfx_ui_hover.ogg") style "ending_menu_button"

style default:
    font gui.text_font
    color "#f0e6d4"
    size 36
    outlines [(2, "#000000aa", 0, 0)]
    language "unicode"

style title_text:
    font gui.label_text_font
    size 104
    color "#f5d37a"
    outlines [(3, "#000000cc", 0, 0)]

style subtitle_text:
    font gui.interface_text_font
    size 32
    color "#dac6a3"

style main_menu_button:
    xsize 330
    ysize 64
    background Solid("#0a070bc8")
    hover_background Solid("#3a2631df")
    padding (26, 12, 26, 12)

style main_menu_button_text:
    font gui.button_text_font
    size 34
    color "#e8ddc6"
    hover_color "#ffffff"

style primary_button:
    xsize 360
    ysize 70
    background Frame("images/ui/choice_button_idle.png", 90, 90)
    hover_background Frame("images/ui/choice_button_hover.png", 90, 90)
    padding (28, 14, 28, 14)

style primary_button_text:
    font gui.button_text_font
    size 34
    color "#fff4d8"
    hover_color "#ffffff"
    xalign 0.5

style small_menu_button:
    ysize 54
    background Solid("#0a070bd5")
    hover_background Solid("#3a2631e6")
    padding (24, 10, 24, 10)

style small_menu_button_text:
    font gui.button_text_font
    size 28
    color "#e8ddc6"
    hover_color "#ffffff"

style quick_button is small_menu_button
style quick_button_text is small_menu_button_text:
    size 22

style loading_text:
    font gui.interface_text_font
    size 28
    color "#f2ddb0"

style chapter_text:
    font gui.label_text_font
    size 52
    color "#f4d27e"
    outlines [(3, "#000000cc", 0, 0)]

style say_name:
    font gui.name_text_font
    size 34
    color "#f2d384"
    outlines [(2, "#000000cc", 0, 0)]

style say_dialogue:
    font gui.text_font
    size 36
    color "#f4ead6"
    line_spacing 8

style choice_button:
    xsize 780
    ysize 84
    background Frame("images/ui/choice_button_idle.png", 90, 90)
    hover_background Frame("images/ui/choice_button_hover.png", 90, 90)
    padding (36, 18, 36, 18)

style choice_button_text:
    font gui.choice_button_text_font
    size 32
    color "#f6ead0"
    hover_color "#ffffff"
    xalign 0.5

style menu_title:
    font gui.label_text_font
    size 58
    color "#f3d27d"
    outlines [(3, "#000000cc", 0, 0)]

style section_text:
    font gui.interface_text_font
    size 34
    color "#ead7b0"

style slot_button:
    xsize 460
    ysize 340
    background Solid("#0b080cd8")
    hover_background Solid("#211721e6")
    padding (15, 15, 15, 15)

style slot_text:
    font gui.interface_text_font
    size 24
    color "#e8ddc6"

style gallery_title:
    font gui.label_text_font
    size 32
    color "#f0d08a"

style gallery_meta:
    font gui.interface_text_font
    size 24
    color "#c8b99b"

style locked_text:
    font gui.interface_text_font
    size 28
    color "#8e826e"

style viewer_title:
    font gui.label_text_font
    size 42
    color "#f2d384"

style notify_text:
    font gui.interface_text_font
    size 26
    color "#f4ead6"

style ending_menu_title:
    font gui.label_text_font
    size 48
    color "#f3d27d"
    outlines [(3, "#000000cc", 0, 0)]

style ending_menu_button:
    xsize 420
    ysize 62
    background Solid("#161014d8")
    hover_background Solid("#3a2631e6")
    padding (26, 12, 26, 12)

style ending_menu_button_text:
    font gui.button_text_font
    size 30
    color "#e8ddc6"
    hover_color "#ffffff"
    xalign 0.5
