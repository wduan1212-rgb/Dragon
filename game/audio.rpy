init -1 python:
    def safe_audio_loadable(path):
        return bool(path) and renpy.loadable(path)

    def safe_voice(path):
        if safe_audio_loadable(path):
            renpy.music.play(path, channel="voice")

    def safe_bgm(path, fadein=1.0, loop=True, volume=1.0):
        if safe_audio_loadable(path):
            renpy.music.play(
                path,
                channel="music",
                fadein=fadein,
                loop=loop,
                if_changed=True,
                relative_volume=volume,
            )

    def stop_bgm(fadeout=1.0):
        renpy.music.stop(channel="music", fadeout=fadeout)

    def safe_ending_bgm(fadein=1.0, loop=True, volume=0.72):
        if safe_audio_loadable("audio/bgm/bgm_new_ending.ogg"):
            safe_bgm("audio/bgm/bgm_new_ending.ogg", fadein, loop, volume)
        elif safe_audio_loadable("audio/bgm/bgm_new_ending.wav"):
            safe_bgm("audio/bgm/bgm_new_ending.wav", fadein, loop, volume)
        else:
            safe_bgm("audio/bgm/bgm_ending_watch.ogg", fadein, loop, volume)

    def safe_sfx(path):
        if safe_audio_loadable(path):
            renpy.sound.play(path)
