init -2 python:
    gui.init(1920, 1080)

    def dragon_pact_cjk_font():
        for font_path in (
            "fonts/NotoSansSC-Regular.ttf",
            "fonts/SourceHanSansSC-Regular.otf",
        ):
            if renpy.loadable(font_path):
                return font_path

        return "DejaVuSans.ttf"

define gui.text_font = dragon_pact_cjk_font()
define gui.name_text_font = dragon_pact_cjk_font()
define gui.interface_text_font = dragon_pact_cjk_font()
define gui.button_text_font = dragon_pact_cjk_font()
define gui.choice_button_text_font = dragon_pact_cjk_font()
define gui.label_text_font = dragon_pact_cjk_font()

define gui.accent_color = "#c7a65c"
define gui.idle_color = "#e8ddc6"
define gui.hover_color = "#ffffff"
define gui.selected_color = "#f1c66a"
define gui.insensitive_color = "#807565"

define gui.text_color = "#f0e6d4"
define gui.interface_text_color = "#f0e6d4"
define gui.name_text_color = "#f3d27d"

define gui.text_size = 38
define gui.name_text_size = 42
define gui.interface_text_size = 34
define gui.button_text_size = 34

define gui.dialogue_width = 1340
define gui.dialogue_xpos = 290
define gui.dialogue_ypos = 862
