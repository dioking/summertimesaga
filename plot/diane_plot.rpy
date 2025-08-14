label diane_plot:
    call mini.garden

    scene black
    with dissolve
    return _return[0]


label diane_plot.diane:
    anon f_calm "Please could I have my wages?"
    diane "Of course, handsome."
    show anon e_sw f_happy
    diane a_shovel_money "Here you are."
    show diane a_shovel_hip
    anon a_cash e_w "Thanks, [saga.cast.diane]!"
    show anon a_pocket
    diane @ e_b f_happy "Hehe, my pleasure."
    return


label diane_plot.late:
    scene camera at stage
    show anon a_pocket e_sw f_worried with dissolve

    if saga.time.dusk:
        anon @ -m_talk "( Trying to garden in this failing light doesn't seem like a good idea. )"
    else:
        anon @ -m_talk "( Trying to garden in the dark really doesn't seem like a good idea. )"

    anon f_happy @ -m_talk "( I'll come back when the sun's out. )"
    hide anon with dissolve
    return


label diane_plot.wait:
    scene camera at stage
    show anon a_think e_sw f_pensive with dissolve
    anon @ -m_talk "( Hmm... )"
    anon a_pocket f_happy @ -m_talk "( ... Nah. Once a day is enough. )"
    anon @ -m_talk "( Need to at least give the garden a little time to recover. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
