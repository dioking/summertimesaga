label school_office2:
    return


label school_office2.keypad:
    jump mini.keypad


label school_office2.lock:
    call shot.school_office2_door
    show anon a_think e_sw f_pensive with dissolve
    anon @ -m_talk "( Hmm, I guess [saga.cast.tori] keeps her office locked when she's not inside? )"
    anon @ -m_talk "( It's got one of those automated keypad locks too. )"
    anon a_pocket f_worried @ -m_talk "( I'm definitely not getting in there without a key code. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
