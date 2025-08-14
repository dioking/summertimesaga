label gym_workout:
    return


label gym_workout.dark:
    scene gym_main at stage
    show anon a_pocket o_right at left with dissolve
    anon @ -m_talk "( It's closed now, I can come back tomorrow. )"
    hide anon with dissolve
    return


label gym_workout.skip:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( I can't wait around here, the gym will be closing soon. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
