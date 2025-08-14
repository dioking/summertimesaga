label library_lobby:
    return


label library_lobby.dark:
    scene library_main at stage
    show anon a_pocket o_right at left with dissolve
    anon @ -m_talk "( Huh... it's locked. I guess it's closed for the day. )"
    hide anon with dissolve
    return


label library_lobby.lock:
    scene library_main at stage
    show anon a_rub f_confused o_right at left with dissolve
    anon @ -m_talk "( Huh... it's closed. Guess I'll try again later. )"
    hide anon with dissolve
    return


label library_lobby.skip:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( I can't wait around here, the library will be closing soon. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
