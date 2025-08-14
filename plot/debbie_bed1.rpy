label debbie_bed1:
    return


label debbie_bed1.self:
    call shot.debbie_bed1_door
    show anon a_pocket f_worried with dissolve
    anon @ -m_talk "( I shouldn't snoop around [saga.cast.debbie]'s bedroom. )"
    hide anon with dissolve
    return


label debbie_bed1.sleep:
    scene debbie_bed1_visit anon
    show debbie p_debbie_bed1_visit_sleep
    anon "( [saga.cast.debbie]'s sleeping. )"
    anon "( I shouldn't make any noise. )"
    return


label debbie_bed1.sneak:
    scene debbie_bed1_visit anon
    anon "( [saga.cast.debbie]'s not in her room. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
