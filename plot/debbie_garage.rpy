label debbie_garage:
    scene debbie_garage -debbie_car at stage(.325, .58, 4.)
    show anon f_happy o_right with dissolve.nowait
    anon @ -m_talk "( Oh, I guess that key is for the garage. )"
    anon @ -m_talk "( Good to know. )"
    hide anon with dissolve
    return


label debbie_garage.area:
    scene debbie_main -car_police -vehicle -yumi at stage(.4, .6, 3.)
    show anon a_think e_nw f_pensive with dissolve.nowait
    anon @ -m_talk "( Hmm, looks like I'll need to open this from the inside. )"

    if saga.prop.key_garage in saga.cast.anon:
        anon e_w f_happy @ -m_talk "( Good thing [saga.cast.debbie] brought that doormat with a picture of a car on it... )"
        anon a_surprised e_b m_teeth o_right @ -m_talk "( ... Otherwise one might risk an entire lifetime never even knowing a door was there! )"
    else:

        anon @ -m_talk "( The garage key has got to be hanging around somewhere in this house. )"

    hide anon with dissolve
    return


label debbie_garage.item:
    scene debbie_hall flip at stage(.4, .465, 3.)
    show anon f_pouty with dissolve.nowait
    anon @ -m_talk "( Locked. )"
    pause
    anon f_pensive @ -m_talk "( But there should be a key around here somewhere. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
