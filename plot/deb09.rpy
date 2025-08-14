label deb09_dream:
    scene dream_ursula dawn onlayer aux
    show debbie a_down c_shawl e_c p_dream_ursula w_normal onlayer aux

    scene aux:
        subpixel True yalign 0. ysize 2340
    with fade
    debbie "Sweetie?"
    anon "Hmm?"
    debbie "Wake up, sweetie."
    anon "[saga.cast.debbie]?"
    anon "W-what's going on?"
    anon "Where are we?"
    debbie "Shh, there's nothing to worry about..."
    debbie "... Not anymore."
    debbie "I'm gonna take care of you now and always."
    show debbie a_jerk s_666ms
    show aux:
        instant (-12 if renpy.suppress_transition() else 0)
        ease 12. yalign 1.
    anon "O-oh, wow... you're-"
    anon "I can't believe this is happening."
    debbie "Just relax, sweetie... I wanna make you feel good."
    anon "Ahh, you are... making me feel..."
    anon "... Ngh, so good."
    pause
    show aux:
        yalign 1.
    hide debbie
    show ursula a_crush c_shawl e_c f_angry p_dream_ursula w_normal onlayer aux
    anon "Hrk!" with hpunch
    ursula "MR. [saga.cast.anon.clan!u]!!"
    show aux:
        instant (-.5 if renpy.suppress_transition() else 0)
        linear .5 yalign 0.
        ysize 1.
    pause .5
    anon "Wait, huh?" with vpunch
    ursula "WHAT IS THE MEANING OF THIS?!"
    anon "M-mrs. [saga.cast.ursula.clan]?!"
    ursula "You think this is appropriate behavior for a school?!"
    anon "N-no, I didn't mean to-"
    ursula "You'd better get this FILTHY cock out of my sight THIS INSTANT or so help me..."
    ursula "... I'll RIP IT OFF and use it for a PAPER WEIGHT!!"
    anon "Eeep!!"

    scene onlayer aux
    with hold.aux
    $ renpy.end_replay()

    call shot.debbie_bed3_sleep
    with fade
    anon a_down e_w f_afraid p_bed3_sit "HOLY MOTHER OF-"
    anon e_o f_surprised @ -m_talk "( !!! )"
    show anon e_e
    pause
    show anon e_w
    pause
    show anon e_sw p_bed3_sit_sheet
    pause
    anon e_b f_shy p_bed3_sit @ -m_talk "( Oh, thank god... it was just a dream! )"
    anon e_w f_worried_surprised @ -m_talk "( I really thought Mrs. [saga.cast.ursula.clan] was gonna- )"
    anon f_confused @ -m_talk "( Why in the heck would I dream that?! )"
    pause
    anon f_shy @ -m_talk "( And that stuff with [saga.cast.debbie]... )"
    anon @ -m_talk "( ... It definitely didn't feel like normal dreams a person should be having about their landlady. )"
    pause
    anon e_b f_calm p_bed3_sleep @ -m_talk "( Man, things just keep getting weirder and weirder. )"
    anon @ -m_talk "( Mm, zzz. )"

    scene black
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
