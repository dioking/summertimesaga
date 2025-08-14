label debbie_drawer:
    return


label debbie_drawer.dark:
    call shot.debbie_bed1_drawer
    show anon f_worried with dissolve
    anon @ -m_talk "( Probably not the best time to be rummaging through [saga.cast.debbie]'s drawers. )"
    hide anon with dissolve
    return


label debbie_drawer.near:
    call shot.debbie_bed1_drawer
    show anon f_worried_surprised o_right with dissolve
    anon @ -m_talk "( We shouldn't go rooting around in her panty drawer while she's in here! )"
    anon @ -m_talk "( C'mon, man... use your head! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
