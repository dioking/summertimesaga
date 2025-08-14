label debbie_bed2:
    return


label debbie_bed2.dark:
    call shot.debbie_bed2_door
    show anon f_sceptical o_right with dissolve
    anon @ -m_talk "( No thanks, I don't feel like getting murdered tonight. )"
    hide anon with dissolve
    return


label debbie_bed2.near:
    call shot.debbie_bed2_door
    show anon f_worried_surprised o_right with dissolve
    anon @ -m_talk "( Are you crazy?! I'm not going in there! )"
    anon @ -m_talk "( [saga.cast.jenny] would kill me! )"
    hide anon with dissolve
    return


label debbie_bed2.skip:
    scene debbie_bed2 at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( Nothing I know about [saga.cast.jenny] makes me think that trying to loiter in her room is a good idea. )"
    anon a_pocket f_calm @ -m_talk "( So no. No, I don't think I will. )"
    hide anon with dissolve
    return


label debbie_bed2.wait:
    call shot.debbie_bed2_door
    show anon f_worried o_right with dissolve
    anon @ -m_talk "( If she catches in there, I'm a dead man. )"
    anon @ -m_talk "( Best not. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
