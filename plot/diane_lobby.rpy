label diane_lobby:
    return


label diane_lobby.dark:
    scene camera at stage

    if saga.cast.anon in saga.sets.diane_main:
        show anon o_right at left with dissolve
    else:
        show anon with dissolve

    anon @ -m_talk "( Locked. )"
    anon @ -m_talk "( [saga.cast.diane] must have gone to bed. I can always stop by tomorrow. )"
    hide anon with dissolve
    return


label diane_lobby.skip:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( Don't want to overstay my welcome. I should think about getting out of here. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
