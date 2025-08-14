label school_hall1:
    return


label school_hall1.late:
    scene school_main at stage
    show anon a_pocket f_worried at right with dissolve
    anon @ -m_talk "( It's all locked up. )"
    anon a_think e_nw f_pensive @ -m_talk "( Maybe if I {i}borrowed{/i} that master key [saga.cast.annie] was talking about... )"
    hide anon with dissolve
    return


label school_hall1.lock:
    scene school_main at stage
    show anon a_pocket f_worried at right with dissolve
    anon @ -m_talk "( It's the weekend. )"
    anon @ -m_talk "( The school is closed until Monday. )"
    hide anon with dissolve
    return


label school_hall1.skip:
    scene camera at stage

    menu:
        "End the school day and exit the building.":
            return True
        "Not yet.":

            pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
