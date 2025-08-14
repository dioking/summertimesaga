label bank_lobby:
    return


label bank_lobby.late:
    scene bank_main at stage
    show anon a_pocket f_tired o_right at left with dissolve
    anon @ -m_talk "( Too late, the bank is already closed for the day. )"
    hide anon with dissolve
    return


label bank_lobby.sat:
    scene bank_main at stage
    show anon f_pouty o_right at left with dissolve
    anon @ -m_talk "( Dang it! The bank closes at midday on Saturdays. )"
    hide anon with dissolve
    return


label bank_lobby.skip:
    scene camera at stage
    show anon a_surprised f_worried_surprised with dissolve
    anon @ -m_talk "( Not really getting those \"it's okay to loiter here\" vibes... )"
    anon @ -m_talk "( ... I should probably just do what I came to do and leave. )"
    hide anon with dissolve
    return


label bank_lobby.sun:
    scene bank_main at stage
    show anon a_facepalm e_b o_right at left with dissolve
    anon @ -m_talk "( Oh no! It's Sunday! )"
    anon a_side e_w @ -m_talk "( The bank is closed on Sunday. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
