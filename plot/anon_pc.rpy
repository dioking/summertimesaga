label anon_pc:
    return


label anon_pc.broken:
    call shot.debbie_bed3_computer
    show anon with dissolve

    if saga.cast.erik < 'computer':
        anon @ -m_talk "( I should speak with [saga.cast.erik] about fixing this old broken PC. )"
    else:

        anon @ -m_talk "( [saga.cast.erik] said he gets his computer parts from Consum-R. )"
        anon a_think e_nw f_pensive @ -m_talk "( I guess I should take a look next time I'm in the mall. )"

    hide anon with dissolve
    return


label anon_pc.dark:
    call shot.debbie_bed3_computer
    show anon e_sw f_tired o_right with dissolve
    anon @ -m_talk "( I'm too tired to focus on that right now, maybe tomorrow. )"
    hide anon with dissolve
    return


label anon_pc.orcette:
    scene anon_pc
    anon "( Erm... )"
    anon "( No judgement, but I really can't see myself using this. )"
    return


label anon_pc.remote:
    scene anon_pc
    anon "( Weird. It doesn't seem to do anything. )"
    anon "( I wonder if it's trying to connect to another computer? )"
    return


label anon_pc.repair:
    call shot.debbie_bed3_computer
    show anon e_sw f_shy o_right with dissolve
    anon @ -m_talk "( Guess there's no time like the present. Hope this isn't too painful. )"
    show anon a_tired f_confused p_bend at pos(y=1.25)
    pause

    scene black
    with dissolve
    mono ""

    call shot.debbie_bed3_computer
    show debbie_bed3 t1 -anon_pc
    show anon a_computer p_bend_away at right
    with dissolve
    anon @ -m_talk "( Wow! That took waaay longer than expected... )"
    anon @ -m_talk "( ... But we are so back! )"
    anon a_uneasy e_b f_happy m_teeth p_stand @ -m_talk "( And now with these higher resolution graphics everything looks even better! )"
    hide anon with dissolve
    return


label anon_pc.saga:
    scene anon_pc
    anon "( Man... This game {i}always{/i} has bugs. )"
    return


label anon_pc.work:
    scene anon_pc
    anon "( I have no homework to do right now. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
