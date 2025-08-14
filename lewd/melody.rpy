label melody_menu:
    return


label melody_menu.music_drums:
    jump mel01_intro.cookie


label melody_menu.music_slip:
    call shot.school_music_melody
    show old_melody 1 at old_left
    show old_anon 1 at old_right
    jump mel02_outro
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
