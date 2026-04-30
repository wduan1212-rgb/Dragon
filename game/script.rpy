define n = Character(None)
define p = Character("男主", color="#f2d384")
define li = Character("李将军", color="#d7b46c")
define zhao = Character("赵无炎", color="#caa2ff")
define seal = Character("龙灵", color="#90d6ff")

default quick_menu = True
default trust_dragon = False
default trust_li = False
default doubt_zhao = False
default zhao_redemption = False
default dragon_bond = 0

transform card_left:
    xysize (520, 735)
    xalign 0.13
    yalign 0.58

transform card_right:
    xysize (520, 735)
    xalign 0.87
    yalign 0.58

transform card_center:
    xysize (560, 746)
    xalign 0.5
    yalign 0.58

init python:
    cg_catalog = [
        ("密令入夜", "cg_letter", "images/cg/cg_letter.png"),
        ("走向封印之门", "cg_walk_to_gate", "images/cg/cg_walk_to_gate.png"),
        ("兵器相撞", "cg_spear_vs_halberd", "images/cg/cg_spear_vs_halberd.png"),
        ("符纸燃起", "cg_zhao_talisman", "images/cg/cg_zhao_talisman.png"),
        ("玉符落掌", "cg_zhao_jade", "images/cg/cg_zhao_jade.png"),
        ("幻影破碎", "cg_zhao_shadow_break", "images/cg/cg_zhao_shadow_break.png"),
        ("魔化登场", "cg_zhao_demon_intro", "images/cg/cg_zhao_demon_intro.png"),
        ("魔化之眼", "cg_zhao_demon_eye", "images/cg/cg_zhao_demon_eye.png"),
        ("龙契共鸣", "cg_dragon_resonance", "images/cg/cg_dragon_resonance.png"),
        ("李将军牺牲", "cg_li_sacrifice", "images/cg/cg_li_sacrifice.png"),
        ("龙化守护树", "cg_dragon_tree", "images/cg/cg_dragon_tree.png"),
    ]

    ending_catalog = [
        ("结局A：龙契重封", "ending_reseal", "images/endings/ending_reseal.png"),
        ("结局B：无炎救赎", "ending_zhao_redemption", "images/endings/ending_zhao_redemption.png"),
        ("结局C：李将军牺牲", "ending_li_sacrifice", "images/endings/ending_li_sacrifice.png"),
        ("结局D：新魔王", "ending_new_demon_king", "images/endings/ending_new_demon_king.png"),
        ("结局E：封印失败", "ending_fail", "images/endings/ending_fail.png"),
        ("坏结局：赵无炎彻底魔化", "ending_zhao_fallen", "images/endings/ending_zhao_fallen.png"),
        ("普通结尾：守望山河", "ending_watch", "images/endings/ending_watch.png"),
        ("开放结局：龙契断裂", "ending_contract_broken", "images/endings/ending_contract_broken.png"),
        ("隐藏结局：龙灵回响", "ending_dragon_echo", "images/endings/ending_dragon_echo.png"),
    ]

    story_cg_catalog = [
        ("前期铺垫：夜半接令", "story_order_night", "images/cg/story/prologue/story_order_night.png"),
        ("前期铺垫：山路疾行", "story_mountain_road_run", "images/cg/story/prologue/story_mountain_road_run.png"),
        ("前期铺垫：村民避难", "story_refugees_escape", "images/cg/story/prologue/story_refugees_escape.png"),
        ("前期铺垫：封印异动", "story_seal_disturbance", "images/cg/story/prologue/story_seal_disturbance.png"),
        ("前期铺垫：触摸石碑", "story_stone_tablet", "images/cg/story/prologue/story_stone_tablet.png"),
        ("前期铺垫：李将军初现", "story_li_first_appearance", "images/cg/story/prologue/story_li_first_appearance.png"),
        ("前期铺垫：雷雨封门", "story_gate_closeup_storm", "images/cg/story/prologue/story_gate_closeup_storm.png"),
        ("前期铺垫：紫焰闪现", "story_purple_flame_hint", "images/cg/story/prologue/story_purple_flame_hint.png"),
        ("真相推进：龙纹残卷", "truth_dragon_record_fragment", "images/cg/story/truth/truth_dragon_record_fragment.png"),
        ("真相推进：旧战场", "truth_old_battlefield", "images/cg/story/truth/truth_old_battlefield.png"),
        ("真相推进：李将军沉默", "truth_li_silence", "images/cg/story/truth/truth_li_silence.png"),
        ("真相推进：拾起玉符碎片", "truth_pickup_jade_piece", "images/cg/story/truth/truth_pickup_jade_piece.png"),
        ("真相推进：无炎旧忆", "truth_zhao_flashback_friendship", "images/cg/story/truth/truth_zhao_flashback_friendship.png"),
        ("真相推进：三人旧事", "truth_three_past", "images/cg/story/truth/truth_three_past.png"),
        ("真相推进：契约显形", "truth_contract_reveal", "images/cg/story/truth/truth_contract_reveal.png"),
        ("真相推进：李将军揭露", "truth_li_revelation", "images/cg/story/truth/truth_li_revelation.png"),
        ("真相推进：赵无炎伸手", "truth_zhao_reaching", "images/cg/story/truth/truth_zhao_reaching.png"),
        ("真相推进：抉择一刻", "truth_choice_moment", "images/cg/story/truth/truth_choice_moment.png"),
        ("高潮爆发：主角拔枪", "climax_hero_draw_spear", "images/cg/story/climax/climax_hero_draw_spear.png"),
        ("高潮爆发：李将军拦门", "climax_li_blocking_gate", "images/cg/story/climax/climax_li_blocking_gate.png"),
        ("高潮爆发：赵无炎半显形", "climax_zhao_half_manifest", "images/cg/story/climax/climax_zhao_half_manifest.png"),
        ("高潮爆发：古殿崩裂", "climax_temple_collapse", "images/cg/story/climax/climax_temple_collapse.png"),
        ("高潮爆发：主角被吞没", "climax_hero_swallowed", "images/cg/story/climax/climax_hero_swallowed.png"),
        ("高潮爆发：龙灵护主", "climax_dragon_protect", "images/cg/story/climax/climax_dragon_protect.png"),
        ("高潮爆发：李将军负伤", "climax_li_wounded_stand", "images/cg/story/climax/climax_li_wounded_stand.png"),
        ("高潮爆发：主角对峙无炎", "climax_hero_zhao_faceoff", "images/cg/story/climax/climax_hero_zhao_faceoff.png"),
        ("高潮爆发：龙契爆发", "climax_contract_burst", "images/cg/story/climax/climax_contract_burst.png"),
        ("高潮爆发：最后一息", "climax_last_second", "images/cg/story/climax/climax_last_second.png"),
        ("战后余波：古殿沉寂", "aftermath_temple_silence", "images/cg/story/aftermath/aftermath_temple_silence.png"),
        ("战后余波：主角跪地", "aftermath_hero_kneel", "images/cg/story/aftermath/aftermath_hero_kneel.png"),
        ("战后余波：李将军最后一眼", "aftermath_li_last_look", "images/cg/story/aftermath/aftermath_li_last_look.png"),
        ("战后余波：赵无炎回归", "aftermath_zhao_human_return", "images/cg/story/aftermath/aftermath_zhao_human_return.png"),
        ("战后余波：玉符碎裂", "aftermath_jade_break", "images/cg/story/aftermath/aftermath_jade_break.png"),
        ("战后余波：龙灵低语", "aftermath_dragon_whisper", "images/cg/story/aftermath/aftermath_dragon_whisper.png"),
        ("战后余波：破晓入殿", "aftermath_dawn_in_temple", "images/cg/story/aftermath/aftermath_dawn_in_temple.png"),
        ("战后余波：主角回望", "aftermath_hero_lookback", "images/cg/story/aftermath/aftermath_hero_lookback.png"),
        ("战后余波：山下宁静", "aftermath_village_peace", "images/cg/story/aftermath/aftermath_village_peace.png"),
        ("战后余波：龙纹残光", "aftermath_contract_remains", "images/cg/story/aftermath/aftermath_contract_remains.png"),
    ]
    cg_catalog.extend(story_cg_catalog)

    def fit_screen(path):
        return Transform(path, xysize=(config.screen_width, config.screen_height))

    def ensure_unlocks():
        if getattr(persistent, "unlocked_cgs", None) is None:
            persistent.unlocked_cgs = []
        if getattr(persistent, "unlocked_endings", None) is None:
            persistent.unlocked_endings = []
        if getattr(persistent, "demo_cleared", None) is None:
            persistent.demo_cleared = False

    def unlock_cg(key):
        ensure_unlocks()
        if key not in persistent.unlocked_cgs:
            persistent.unlocked_cgs.append(key)
            renpy.save_persistent()

    def unlock_ending(key):
        ensure_unlocks()
        if key not in persistent.unlocked_endings:
            persistent.unlocked_endings.append(key)
        persistent.demo_cleared = True
        renpy.save_persistent()

label before_main_menu:
    $ ensure_unlocks()
    return

label start:
    $ ensure_unlocks()
    $ stop_bgm(0.5)
    $ safe_bgm("audio/bgm/bgm_character_select.ogg", 0.8, True, 0.76)
    $ trust_dragon = False
    $ trust_li = False
    $ doubt_zhao = False
    $ zhao_redemption = False
    $ dragon_bond = 0

    call screen character_select
    if _return != "protagonist":
        return

    call loading_sequence from _call_loading_sequence
    jump opening_sequence

label loading_sequence:
    window hide
    $ safe_bgm("audio/bgm/bgm_loading_dark.ogg", 0.8, True, 0.55)
    show screen loading_screen(0, "正在读取密令")
    $ safe_sfx("audio/sfx/sfx_loading_tick.ogg")
    pause 0.2
    show screen loading_screen(24, "正在校准龙脉")
    $ safe_sfx("audio/sfx/sfx_loading_tick.ogg")
    pause 0.25
    show screen loading_screen(48, "正在进入北境")
    $ safe_sfx("audio/sfx/sfx_loading_tick.ogg")
    pause 0.25
    show screen loading_screen(68, "封印信号异常")
    $ safe_sfx("audio/sfx/sfx_loading_tick.ogg")
    pause 0.8
    show screen loading_screen(86, "正在稳定画面")
    $ safe_sfx("audio/sfx/sfx_loading_tick.ogg")
    pause 0.25
    show screen loading_screen(100, "同步完成")
    $ safe_sfx("audio/sfx/sfx_loading_complete.ogg")
    pause 0.45
    hide screen loading_screen
    return

label play_cutscene(start_frame, end_frame, hold=0.8):
    window hide
    scene expression fit_screen(start_frame)
    with fade
    pause hold
    scene expression fit_screen(end_frame)
    with dissolve
    pause hold

    return

label show_story_cg(key, path, hold=0.75):
    window hide
    if renpy.loadable(path):
        scene expression fit_screen(path)
        with fade
        $ unlock_cg(key)
        pause hold
    return

label show_chapter(title):
    window hide
    show screen chapter_title()
    with Dissolve(0.5)
    pause 1.5
    hide screen chapter_title
    with Dissolve(0.5)
    return

label play_optional_ending_cg():
    window hide
    return

label opening_sequence:
    $ safe_bgm("audio/bgm/bgm_dark_mountain.ogg", 1.2, True, 0.72)
    call show_story_cg("story_order_night", "images/cg/story/prologue/story_order_night.png") from _call_show_story_cg
    call show_story_cg("story_mountain_road_run", "images/cg/story/prologue/story_mountain_road_run.png") from _call_show_story_cg_1
    $ safe_voice("audio/voice/narrator/narrator_017.ogg")
    n "密令还未拆开，北境的风已经先一步催人上路。"
    $ safe_voice("audio/voice/male/male_016.ogg")
    p "若这封令只要我杀人，我宁愿先问清它从何而来。"
    $ safe_voice("audio/voice/narrator/narrator_018.ogg")
    n "山道尽头，龙脉逆着雨声翻涌，像一条被迫醒来的旧伤。"
    call play_cutscene("images/frames/opening_start.png", "images/frames/opening_end.png") from _call_play_cutscene

    scene expression fit_screen("images/cg/cg_letter.png")
    with fade
    $ unlock_cg("cg_letter")

    $ safe_voice("audio/voice/narrator/narrator_001.ogg")
    n "永宁三十七年，北境龙脉忽然倒流。"
    $ safe_voice("audio/voice/narrator/narrator_002.ogg")
    n "一封密令在子夜送入玄钧手中。"
    $ safe_voice("audio/voice/male/male_001.ogg")
    p "封印之门三日内必开。若龙契苏醒，持令者可先斩后奏。"
    $ safe_voice("audio/voice/narrator/narrator_003.ogg")
    n "纸上的朱砂尚未干透，门外的山风已经带着铁锈味。"

    scene expression fit_screen("images/cg/cg_walk_to_gate.png")
    with dissolve
    $ unlock_cg("cg_walk_to_gate")

    $ safe_voice("audio/voice/male/male_002.ogg")
    p "我不是来求一个答案的。"
    $ safe_voice("audio/voice/male/male_003.ogg")
    p "我是来确认，谁在替天下说谎。"

    jump seal_gate_chapter

label seal_gate_chapter:
    call show_chapter("第一章  封印之门") from _call_show_chapter
    $ safe_bgm("audio/bgm/bgm_fortress_tension.ogg", 1.0, True, 0.72)
    $ safe_sfx("audio/sfx/sfx_seal_hum.ogg")

    call show_story_cg("story_refugees_escape", "images/cg/story/prologue/story_refugees_escape.png") from _call_show_story_cg_2
    call show_story_cg("story_gate_closeup_storm", "images/cg/story/prologue/story_gate_closeup_storm.png") from _call_show_story_cg_3
    call show_story_cg("story_seal_disturbance", "images/cg/story/prologue/story_seal_disturbance.png") from _call_show_story_cg_4
    call show_story_cg("story_stone_tablet", "images/cg/story/prologue/story_stone_tablet.png") from _call_show_story_cg_5
    $ safe_voice("audio/voice/narrator/narrator_019.ogg")
    n "山下的村民拖着家当逃离，连哭声都不敢朝封印门那边去。"
    $ safe_voice("audio/voice/male/male_017.ogg")
    p "他们怕的不是龙，是门开之后还活着的人。"
    $ safe_voice("audio/voice/narrator/narrator_020.ogg")
    n "雷光照见石碑旧痕，玄钧掌心的契印随之一热。"
    $ safe_voice("audio/voice/seal/seal_005.ogg")
    seal "别让旧誓第二次被血写成。"
    $ safe_voice("audio/voice/male/male_018.ogg")
    p "旧誓？我从未向谁立过誓。"

    scene expression fit_screen("images/bg/seal_gate.png")
    with fade

    $ safe_voice("audio/voice/seal/seal_001.ogg")
    seal "封印残响正在回流。契印持有者，靠近。"
    $ safe_voice("audio/voice/male/male_004.ogg")
    p "这声音不是命令。"
    $ safe_voice("audio/voice/male/male_005.ogg")
    p "像是有人在黑暗里，替我记住了一段旧债。"

    call show_story_cg("story_li_first_appearance", "images/cg/story/prologue/story_li_first_appearance.png") from _call_show_story_cg_6
    $ safe_voice("audio/voice/narrator/narrator_021.ogg")
    n "李将军现身时，雨声像被一纸军令压低。"
    $ safe_voice("audio/voice/male/male_019.ogg")
    p "你不是来劝我退下的。"
    $ safe_voice("audio/voice/li/li_008.ogg")
    li "我守的不是这扇门，是门外还活着的人。"
    call play_cutscene("images/frames/li_intro_start.png", "images/frames/li_intro_end.png") from _call_play_cutscene_1

    scene expression fit_screen("images/bg/seal_gate.png")
    with dissolve
    show expression fit_screen("images/characters/li_battle.png") as li_card at card_right zorder 20

    $ safe_voice("audio/voice/li/li_001.ogg")
    li "玄钧，止步。"
    $ safe_voice("audio/voice/li/li_002.ogg")
    li "再往前半步，便按擅闯禁地论罪。"
    $ safe_voice("audio/voice/male/male_006.ogg")
    p "将军亲自守门，说明门后的东西已经不是传闻。"
    $ safe_voice("audio/voice/li/li_003.ogg")
    li "传闻会害死人。龙也会。"

    scene expression fit_screen("images/cg/cg_spear_vs_halberd.png")
    with dissolve
    $ safe_sfx("audio/sfx/sfx_weapon_clash.ogg")
    $ unlock_cg("cg_spear_vs_halberd")

    $ safe_voice("audio/voice/narrator/narrator_004.ogg")
    n "长戟压下，枪锋逆挑。"
    $ safe_voice("audio/voice/narrator/narrator_005.ogg")
    n "铁器相撞的刹那，封印门后的紫光裂开一线。"

    call show_story_cg("story_purple_flame_hint", "images/cg/story/prologue/story_purple_flame_hint.png") from _call_show_story_cg_7
    $ safe_voice("audio/voice/male/male_020.ogg")
    p "那道紫焰不像妖火。"
    $ safe_voice("audio/voice/male/male_021.ogg")
    p "它更像一道烧到现在的旧伤。"
    $ safe_voice("audio/voice/li/li_009.ogg")
    li "别听。"
    call play_cutscene("images/frames/zhao_shadow_start.png", "images/frames/zhao_shadow_end.png") from _call_play_cutscene_2

    scene expression fit_screen("images/cg/cg_zhao_talisman.png")
    with dissolve
    $ safe_bgm("audio/bgm/bgm_zhao_shadow.ogg", 0.8, True, 0.78)
    $ unlock_cg("cg_zhao_talisman")

    $ safe_voice("audio/voice/zhao/zhao_001.ogg")
    zhao "李将军还是这样，把愧疚披成军令。"
    $ safe_voice("audio/voice/li/li_004.ogg")
    li "赵无炎。"
    $ safe_voice("audio/voice/zhao/zhao_002.ogg")
    zhao "别急着喊我的名字。你们都需要一个死人来替真相开口。"

    scene expression fit_screen("images/bg/dragon_hall.png")
    with dissolve
    show expression fit_screen("images/characters/male_serious.png") as male_card at card_left zorder 20
    show expression fit_screen("images/characters/zhao_shadow.png") as zhao_card at card_right zorder 20

    $ safe_voice("audio/voice/zhao/zhao_003.ogg")
    zhao "玄钧，你以为龙是灾厄。"
    $ safe_voice("audio/voice/zhao/zhao_004.ogg")
    zhao "可若封印本身，才是吞噬天下的阵眼呢？"
    $ safe_voice("audio/voice/male/male_007.ogg")
    p "你想让我怀疑他，还是怀疑我手里的契印？"
    $ safe_voice("audio/voice/zhao/zhao_005.ogg")
    zhao "我只想让你在拔枪前，看一眼血是谁的。"

    call truth_sequence from _call_truth_sequence

    menu:
        "相信龙契的共鸣":
            $ trust_dragon = True
            $ dragon_bond += 2
            $ safe_voice("audio/voice/male/male_008.ogg")
            p "龙若真是灾厄，它不必等我来听见。"
            $ safe_voice("audio/voice/seal/seal_002.ogg")
            seal "契印回应。龙脉稳定。"

        "相信李将军的军令":
            $ trust_li = True
            $ safe_voice("audio/voice/male/male_009.ogg")
            p "将军守门二十年，不会只为一条谎言拔戟。"
            $ safe_voice("audio/voice/li/li_005.ogg")
            li "你若仍信我，就退到我身后。"

        "质疑赵无炎的幻影":
            $ doubt_zhao = True
            $ zhao_redemption = True
            $ safe_voice("audio/voice/male/male_010.ogg")
            p "死人若只说一半真相，便和活人一样危险。"
            $ safe_voice("audio/voice/zhao/zhao_006.ogg")
            zhao "很好。至少你还没有把怀疑交给别人。"

    jump demon_arrival

label truth_sequence:
    call show_story_cg("truth_dragon_record_fragment", "images/cg/story/truth/truth_dragon_record_fragment.png", 0.55) from _call_show_story_cg_8
    call show_story_cg("truth_old_battlefield", "images/cg/story/truth/truth_old_battlefield.png", 0.55) from _call_show_story_cg_9
    $ safe_voice("audio/voice/narrator/narrator_022.ogg")
    n "残卷上的龙纹被血浸断，只剩半句誓词仍在发亮。"
    $ safe_voice("audio/voice/narrator/narrator_023.ogg")
    n "旧战场没有尸骨，只有烧黑的军旗插在阵眼边。"
    call show_story_cg("truth_li_silence", "images/cg/story/truth/truth_li_silence.png", 0.55) from _call_show_story_cg_10
    call show_story_cg("truth_pickup_jade_piece", "images/cg/story/truth/truth_pickup_jade_piece.png", 0.55) from _call_show_story_cg_11
    $ safe_voice("audio/voice/male/male_022.ogg")
    p "将军，这些你都见过。"
    $ safe_voice("audio/voice/li/li_010.ogg")
    li "见过，不等于能说。"
    call show_story_cg("truth_zhao_flashback_friendship", "images/cg/story/truth/truth_zhao_flashback_friendship.png", 0.55) from _call_show_story_cg_12
    call show_story_cg("truth_three_past", "images/cg/story/truth/truth_three_past.png", 0.55) from _call_show_story_cg_13
    $ safe_voice("audio/voice/zhao/zhao_010.ogg")
    zhao "那时我也会信人。可惜信任最先被拿去祭阵。"
    $ safe_voice("audio/voice/zhao/zhao_011.ogg")
    zhao "你看，他们把少年写成叛徒，把沉默写成功勋。"
    call show_story_cg("truth_contract_reveal", "images/cg/story/truth/truth_contract_reveal.png", 0.55) from _call_show_story_cg_14
    call show_story_cg("truth_li_revelation", "images/cg/story/truth/truth_li_revelation.png", 0.55) from _call_show_story_cg_15
    call show_story_cg("truth_zhao_reaching", "images/cg/story/truth/truth_zhao_reaching.png", 0.55) from _call_show_story_cg_16
    call show_story_cg("truth_choice_moment", "images/cg/story/truth/truth_choice_moment.png", 0.55) from _call_show_story_cg_17
    $ safe_voice("audio/voice/seal/seal_006.ogg")
    seal "契约不是锁。被篡改之后，才成了锁。"
    $ safe_voice("audio/voice/male/male_023.ogg")
    p "所以门后困住的，未必是灾厄。"
    $ safe_voice("audio/voice/li/li_011.ogg")
    li "玄钧，真相若能救人，我早已开口。"
    $ safe_voice("audio/voice/male/male_024.ogg")
    p "那就让我自己选。"
    return

label demon_arrival:
    call show_story_cg("climax_hero_draw_spear", "images/cg/story/climax/climax_hero_draw_spear.png", 0.55) from _call_show_story_cg_18
    $ safe_voice("audio/voice/male/male_025.ogg")
    p "这一次，我不替任何人的军令拔枪。"
    call show_story_cg("climax_li_blocking_gate", "images/cg/story/climax/climax_li_blocking_gate.png", 0.55) from _call_show_story_cg_19
    $ safe_voice("audio/voice/li/li_012.ogg")
    li "退到我身后，这是命令，也是最后一次。"
    call show_story_cg("climax_zhao_half_manifest", "images/cg/story/climax/climax_zhao_half_manifest.png", 0.55) from _call_show_story_cg_20
    $ safe_voice("audio/voice/zhao/zhao_012.ogg")
    zhao "看清楚了吗？怪物也会疼。"
    call show_story_cg("climax_temple_collapse", "images/cg/story/climax/climax_temple_collapse.png", 0.55) from _call_show_story_cg_21
    $ safe_voice("audio/voice/narrator/narrator_024.ogg")
    n "古殿的梁柱一节节崩裂，像有人从地底扯断龙骨。"
    call show_story_cg("climax_hero_swallowed", "images/cg/story/climax/climax_hero_swallowed.png", 0.55) from _call_show_story_cg_22
    $ safe_voice("audio/voice/narrator/narrator_025.ogg")
    n "玄钧被紫黑色的光吞没，耳边只剩契印碎响。"
    call show_story_cg("climax_dragon_protect", "images/cg/story/climax/climax_dragon_protect.png", 0.55) from _call_show_story_cg_23
    $ safe_voice("audio/voice/seal/seal_007.ogg")
    seal "若要护住他，代价会落在你身上。"
    call show_story_cg("climax_li_wounded_stand", "images/cg/story/climax/climax_li_wounded_stand.png", 0.55) from _call_show_story_cg_24
    $ safe_voice("audio/voice/li/li_013.ogg")
    li "我守了半生的门，今日不能死在门前。"
    call show_story_cg("climax_hero_zhao_faceoff", "images/cg/story/climax/climax_hero_zhao_faceoff.png", 0.55) from _call_show_story_cg_25
    $ safe_voice("audio/voice/male/male_026.ogg")
    p "赵无炎，若你还听得见，就别把最后的人心交给魔焰。"
    call show_story_cg("climax_contract_burst", "images/cg/story/climax/climax_contract_burst.png", 0.55) from _call_show_story_cg_26
    $ safe_voice("audio/voice/zhao/zhao_013.ogg")
    zhao "晚了。可你可以试着再晚一点。"
    call show_story_cg("climax_last_second", "images/cg/story/climax/climax_last_second.png", 0.55) from _call_show_story_cg_27
    $ safe_voice("audio/voice/male/male_027.ogg")
    p "开门也好，封门也好，今日由活着的人承担。"
    call play_cutscene("images/frames/zhao_demon_start.png", "images/frames/zhao_demon_end.png") from _call_play_cutscene_3
    $ safe_bgm("audio/bgm/bgm_boss_phase1.ogg", 0.8, True, 0.82)

    scene expression fit_screen("images/bg/dragon_hall_broken.png")
    with fade
    $ safe_voice("audio/voice/narrator/narrator_006.ogg")
    n "封印之门没有开启。"
    $ safe_voice("audio/voice/narrator/narrator_007.ogg")
    n "它像被某种古老的意志从内部撕开。"

    $ safe_sfx("audio/sfx/sfx_magic_burst.ogg")

    scene expression fit_screen("images/cg/cg_zhao_demon_intro.png")
    with fade
    $ unlock_cg("cg_zhao_demon_intro")
    pause 0.4

    scene expression fit_screen("images/cg/cg_zhao_demon_eye.png")
    with dissolve
    $ unlock_cg("cg_zhao_demon_eye")

    $ safe_voice("audio/voice/zhao/zhao_007.ogg")
    zhao "现在，你们终于愿意看我一眼了。"
    $ safe_voice("audio/voice/li/li_006.ogg")
    li "退后！他身上的魔焰正在吞封印。"
    $ safe_voice("audio/voice/male/male_011.ogg")
    p "不。那不是吞噬。"

    scene expression fit_screen("images/cg/cg_dragon_resonance.png")
    with dissolve
    $ safe_bgm("audio/bgm/bgm_dragon_resonance.ogg", 1.0, True, 0.78)
    $ safe_sfx("audio/sfx/sfx_dragon_roar_low.ogg")
    $ unlock_cg("cg_dragon_resonance")

    $ safe_voice("audio/voice/seal/seal_003.ogg")
    seal "契印持有者，选择代价。"
    $ safe_voice("audio/voice/male/male_012.ogg")
    p "若天下只能靠一个谎言续命，那今日就让谎言见血。"

    $ safe_sfx("audio/sfx/sfx_gate_open.ogg")
    call play_cutscene("images/frames/gate_open_start.png", "images/frames/gate_open_end.png") from _call_play_cutscene_4

    jump ending_preview_menu

label ending_preview_menu:
    menu:
        "以龙契重封封印":
            jump ending_reseal

        "伸手接住紫色玉符":
            jump ending_zhao_redemption

        "替李将军挡下魔焰":
            jump ending_li_sacrifice

        "强行斩断门中龙脉":
            jump ending_fail

        "收枪，守住黎明前的山河":
            jump ending_watch

label ending_reseal:
    $ safe_ending_bgm(1.0, True, 0.72)
    scene expression fit_screen("images/endings/ending_reseal.png")
    with fade
    $ unlock_ending("ending_reseal")

    $ safe_voice("audio/voice/narrator/narrator_008.ogg")
    n "结局A：龙契重封"
    $ safe_voice("audio/voice/male/male_013.ogg")
    p "封印可以重铸，但这一次，契约写下的是我的名字。"
    $ safe_voice("audio/voice/seal/seal_004.ogg")
    seal "龙脉归位。代价确认。"
    $ safe_voice("audio/voice/male/male_028.ogg")
    p "我听见自己的名字沉进龙纹里。"
    $ safe_voice("audio/voice/male/male_029.ogg")
    p "这不是胜利，只是另一个人开始守门。"
    call show_story_cg("aftermath_temple_silence", "images/cg/story/aftermath/aftermath_temple_silence.png", 0.55) from _call_show_story_cg_28
    $ safe_voice("audio/voice/narrator/narrator_026.ogg")
    n "古殿安静下来，连灰烬落地都像在道别。"
    call show_story_cg("aftermath_hero_kneel", "images/cg/story/aftermath/aftermath_hero_kneel.png", 0.55) from _call_show_story_cg_29
    call show_story_cg("aftermath_dragon_whisper", "images/cg/story/aftermath/aftermath_dragon_whisper.png", 0.55) from _call_show_story_cg_30
    $ safe_voice("audio/voice/seal/seal_008.ogg")
    seal "契中有名，孤魂便不会被风吹散。"
    call show_story_cg("aftermath_dawn_in_temple", "images/cg/story/aftermath/aftermath_dawn_in_temple.png", 0.55) from _call_show_story_cg_31
    $ safe_voice("audio/voice/narrator/narrator_027.ogg")
    n "天光越过山门时，玄钧没有回头太久。"
    call show_story_cg("aftermath_hero_lookback", "images/cg/story/aftermath/aftermath_hero_lookback.png", 0.55) from _call_show_story_cg_32
    call show_story_cg("aftermath_contract_remains", "images/cg/story/aftermath/aftermath_contract_remains.png", 0.55) from _call_show_story_cg_33
    $ unlock_ending("ending_contract_broken")
    jump show_ending_menu

label ending_zhao_redemption:
    $ safe_ending_bgm(1.0, True, 0.72)
    scene expression fit_screen("images/cg/cg_zhao_jade.png")
    with fade
    $ unlock_cg("cg_zhao_jade")

    $ safe_voice("audio/voice/zhao/zhao_008.ogg")
    zhao "你敢接？那里面烧着我最后一寸人心。"
    $ safe_voice("audio/voice/male/male_014.ogg")
    p "人心若还会痛，就还没有死。"
    $ safe_voice("audio/voice/zhao/zhao_014.ogg")
    zhao "别用这种眼神看我。被原谅比被杀更难受。"
    $ safe_voice("audio/voice/male/male_030.ogg")
    p "我没有替你洗清罪名。"
    $ safe_voice("audio/voice/male/male_031.ogg")
    p "我只是接住还没有彻底死去的那一部分你。"

    scene expression fit_screen("images/endings/ending_zhao_redemption.png")
    with dissolve
    $ unlock_ending("ending_zhao_redemption")

    $ safe_voice("audio/voice/narrator/narrator_009.ogg")
    n "结局B：无炎救赎"
    $ safe_voice("audio/voice/narrator/narrator_010.ogg")
    n "紫焰退成灰白，赵无炎第一次没有笑。"
    call show_story_cg("aftermath_zhao_human_return", "images/cg/story/aftermath/aftermath_zhao_human_return.png", 0.55) from _call_show_story_cg_34
    call show_story_cg("aftermath_jade_break", "images/cg/story/aftermath/aftermath_jade_break.png", 0.55) from _call_show_story_cg_35
    $ safe_voice("audio/voice/narrator/narrator_028.ogg")
    n "玉符裂开的声音很轻，紫焰却像终于学会熄灭。"
    $ safe_voice("audio/voice/zhao/zhao_015.ogg")
    zhao "玄钧，若我醒来还是罪人呢？"
    $ safe_voice("audio/voice/male/male_032.ogg")
    p "那就活着偿还。"
    call show_story_cg("aftermath_dragon_whisper", "images/cg/story/aftermath/aftermath_dragon_whisper.png", 0.55) from _call_show_story_cg_36
    $ safe_voice("audio/voice/seal/seal_009.ogg")
    seal "龙脉仍乱，但怨火退了一寸。"
    call show_story_cg("aftermath_dawn_in_temple", "images/cg/story/aftermath/aftermath_dawn_in_temple.png", 0.55) from _call_show_story_cg_37
    jump show_ending_menu

label ending_li_sacrifice:
    $ safe_ending_bgm(1.0, True, 0.72)
    scene expression fit_screen("images/cg/cg_li_sacrifice.png")
    with fade
    $ unlock_cg("cg_li_sacrifice")

    $ safe_voice("audio/voice/li/li_007.ogg")
    li "玄钧，替我守住门外的人。"
    $ safe_voice("audio/voice/male/male_015.ogg")
    p "将军！"
    $ safe_voice("audio/voice/li/li_014.ogg")
    li "别学我，玄钧。别把一生都站成一扇门。"

    scene expression fit_screen("images/endings/ending_li_sacrifice.png")
    with dissolve
    $ unlock_ending("ending_li_sacrifice")

    $ safe_voice("audio/voice/narrator/narrator_011.ogg")
    n "结局C：李将军牺牲"
    $ safe_voice("audio/voice/narrator/narrator_012.ogg")
    n "长戟折断之前，封印终于重新合上。"
    call show_story_cg("aftermath_li_last_look", "images/cg/story/aftermath/aftermath_li_last_look.png", 0.55) from _call_show_story_cg_38
    $ safe_voice("audio/voice/male/male_033.ogg")
    p "可你至少守住了门外的人。"
    $ safe_voice("audio/voice/li/li_015.ogg")
    li "那就替我看看，他们明日是否还会点灯。"
    call show_story_cg("aftermath_hero_kneel", "images/cg/story/aftermath/aftermath_hero_kneel.png", 0.55) from _call_show_story_cg_39
    $ safe_voice("audio/voice/narrator/narrator_029.ogg")
    n "他最后一眼没有求赦，只确认山下仍有灯火。"
    call show_story_cg("aftermath_temple_silence", "images/cg/story/aftermath/aftermath_temple_silence.png", 0.55) from _call_show_story_cg_40
    jump show_ending_menu

label ending_fail:
    $ safe_bgm("audio/bgm/bgm_bad_ending.ogg", 1.0, True, 0.78)
    scene expression fit_screen("images/endings/ending_fail.png")
    with fade
    $ unlock_ending("ending_fail")

    $ safe_voice("audio/voice/narrator/narrator_013.ogg")
    n "结局E：封印失败"
    $ safe_voice("audio/voice/zhao/zhao_009.ogg")
    zhao "你们总说要救天下。可天下从未等过你们。"
    $ safe_voice("audio/voice/narrator/narrator_014.ogg")
    n "紫黑色的光吞没山门，北境烽火一夜不熄。"
    $ safe_voice("audio/voice/male/male_034.ogg")
    p "我斩断的不是谎言。"
    $ safe_voice("audio/voice/male/male_035.ogg")
    p "是最后一道还肯拦住灾厄的锁。"
    $ safe_voice("audio/voice/zhao/zhao_016.ogg")
    zhao "看吧，天下终于不用再被谁欺骗了。"
    call show_story_cg("aftermath_temple_silence", "images/cg/story/aftermath/aftermath_temple_silence.png", 0.55) from _call_show_story_cg_41
    call show_story_cg("aftermath_contract_remains", "images/cg/story/aftermath/aftermath_contract_remains.png", 0.55) from _call_show_story_cg_42
    $ safe_voice("audio/voice/narrator/narrator_030.ogg")
    n "龙纹残光贴在碎石上，像一只正在熄灭的眼。"
    $ unlock_ending("ending_zhao_fallen")
    $ unlock_ending("ending_new_demon_king")
    jump show_ending_menu

label ending_watch:
    $ safe_ending_bgm(1.0, True, 0.72)
    scene expression fit_screen("images/cg/cg_dragon_tree.png")
    with fade
    $ unlock_cg("cg_dragon_tree")

    scene expression fit_screen("images/endings/ending_watch.png")
    with dissolve
    $ unlock_ending("ending_watch")

    $ safe_voice("audio/voice/narrator/narrator_015.ogg")
    n "普通结尾：守望山河"
    $ safe_voice("audio/voice/narrator/narrator_016.ogg")
    n "龙化为树，根须穿过旧阵。黎明来时，山河仍在。"
    $ safe_voice("audio/voice/narrator/narrator_031.ogg")
    n "山下第一缕炊烟升起时，没人知道古殿里少了一场灾。"
    $ safe_voice("audio/voice/male/male_036.ogg")
    p "没有赢。只是还来得及守。"
    call show_story_cg("aftermath_village_peace", "images/cg/story/aftermath/aftermath_village_peace.png", 0.55) from _call_show_story_cg_43
    call show_story_cg("aftermath_dawn_in_temple", "images/cg/story/aftermath/aftermath_dawn_in_temple.png", 0.55) from _call_show_story_cg_44
    $ safe_voice("audio/voice/seal/seal_010.ogg")
    seal "契未尽，山河仍记得你的名字。"
    call show_story_cg("aftermath_hero_lookback", "images/cg/story/aftermath/aftermath_hero_lookback.png", 0.55) from _call_show_story_cg_45
    $ unlock_ending("ending_dragon_echo")
    jump show_ending_menu

label ending_actions:
    jump show_ending_menu

label show_ending_menu:
    window hide
    call screen ending_menu
    return
