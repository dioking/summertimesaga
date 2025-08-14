label helen_lobby:
    return


label helen_lobby.dark:
    scene helen_main at stage
    show anon a_surprised f_afraid m_teeth o_right at left with dissolve
    anon @ -m_talk "( Sneaking into a cop's home at night seems like a {i}really{/i} bad idea. )"
    hide anon with dissolve
    return


label helen_lobby.skip:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( They'll be going to bed soon. I should think about getting out of here. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
