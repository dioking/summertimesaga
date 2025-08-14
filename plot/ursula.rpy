label ursula_school_lounge:
    scene school_lounge base at stage(.735, .58, 3.2)
    show old_ursula 33 at old_right
    show old_anon 22 at old_left with dissolve
    anon "( Oh crap! [saga.cast.ursula] is in here! )"
    show old_anon 11
    show old_ursula 31 with dissolve.nowait
    anon "( ... )"
    show old_ursula 32
    ursula "[saga.cast.anon]?"
    ursula "What in the world are you doing in the teachers' lounge?!"
    show old_ursula 31
    show old_anon 10
    anon "I was just-"
    show old_anon 11
    show old_ursula 32
    ursula "Students are not allowed to be in here!"
    ursula "Get back to your class immediately or I'll have you expelled!"
    show old_ursula 31
    show old_anon 10
    anon "Y-yes, ma'am!"
    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
