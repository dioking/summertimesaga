label tammy_lobby:
    return


label tammy_lobby.dark:
    scene tammy_main at stage
    show anon a_pocket o_right at left with dissolve
    anon @ -m_talk "( They'be sleeping by now... )"
    anon @ e_b f_happy m_teeth "( ... Or gaming! )"
    anon @ -m_talk "( Either way, I should leave them to it. )"
    hide anon with dissolve
    return


label tammy_lobby.skip:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( They'll be going to bed soon. I should think about making a move. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
