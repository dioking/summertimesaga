label school_locker:
    return


label school_locker.item:
    scene camera at stage
    show anon f_grumpy with dissolve
    anon @ -m_talk "( Locked. )"
    pause
    anon a_think e_nw f_pensive @ -m_talk "( Didn't [saga.cast.annie] mention something about a master key? )"
    anon @ -m_talk "( I bet that would be useful here. )"
    hide anon with dissolve
    return


label school_locker.near:
    scene camera at stage
    show anon f_grumpy with dissolve
    anon @ -m_talk "( Probably best to wait for an individual to leave the immediate area {i}before{/i} I go callously snooping around in their locker. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
