label school_office1:
    return


label school_office1.deny:
    scene school_office1 -ursula at stage
    show old_ursula 3b at old_right
    show anon a_pocket f_surprised m_teeth o_right at left with dissolve
    anon @ -m_talk "( Oh crap! She's here! )"

    if renpy.random.random() < .5:
        show old_ursula 5
        ursula "What are you doing here?!"
        show old_ursula 3
        anon "Oh... umm..."
        anon @ f_shy "I was... looking for the washroom?"
        show old_ursula 4
        ursula "Don't play dumb with me, [saga.cast.anon]!"
        ursula "Didn't I just tell you earlier to get to class?!"
        show old_ursula 1
        anon "Well-"
    else:

        ursula "..."
        show old_ursula 27
        with dissolve.nowait
        ursula "... Can I help you with something?"
        show anon a_uneasy f_shy -m_teeth
        show old_ursula 26
        with dissolve.nowait
        anon "Oh! I was just-"
        anon "... Err, I was... just wondering..."
        show old_ursula 4
        with dissolve.nowait
        ursula "Spit it out, [saga.cast.anon]!"
        show old_ursula 3
        with dissolve.nowait
        anon "Uhh, how are you doing, Mrs. [saga.cast.ursula.clan]?"
        ursula "..."
        show old_ursula 27
        with dissolve.nowait
        ursula "Busy."

    show anon a_surprised f_surprised m_teeth
    show old_ursula 2
    ursula "Now, get out of my office!" with hpunch
    show old_ursula 1
    anon a_salute f_afraid "Y-yes, ma'am!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
