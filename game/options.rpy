define config.name = _("龙之契")
define gui.show_name = True

define config.version = "0.1.0"
define build.name = "dragon_pact"

define config.screen_width = 1920
define config.screen_height = 1080

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

define config.enter_transition = Dissolve(0.25)
define config.exit_transition = Dissolve(0.25)
define config.intra_transition = Dissolve(0.18)
define config.after_load_transition = None
define config.end_game_transition = Fade(0.4, 0.2, 0.4)

define config.save_directory = "dragon_pact_demo"
define config.check_conflicting_properties = True

default preferences.text_cps = 22
default preferences.afm_time = 12

init python:
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("docs/**", None)
    build.classify("project_docs/**", None)
    build.classify("raw_assets_backup/**", None)
    build.classify("raw_inbox/**", None)
    build.classify("review_needed/**", None)
    build.classify("game/cache/**", None)
    build.classify("game/saves/**", None)
    build.classify("game/videos/**", None)
    build.classify("game/audio/source_voice/**", None)
    build.classify("game/audio/voice_candidates/**", None)
    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/images/**", "archive")
    build.classify("game/fonts/**", "archive")
    build.classify("game/audio/**", "archive")
