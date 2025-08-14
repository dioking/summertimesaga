label tor_office:
    hide anon
    show old_anon 2 at old_right
    anon "Are you free at the moment?"
    show old_anon 1
    show old_tori 7
    tori "Why, have you come for another round of testing?"
    show old_anon 2
    show old_tori 6
    anon "Yeah, if you want?"
    show old_anon 1
    show old_tori 7
    tori "Of course, just let me just attach your sensory AR device..."
    show old_anon 11 behind old_tori
    show old_tori 89 at pos(.596), face_right
    with dissolve.nowait
    pause
    show old_anon 10
    anon "I really don't like this part..."
    show old_anon 11
    show old_tori 7 at center
    show old_tori MC eyes2 as anon_eyes at old_right
    with dissolve.nowait
    tori "Oh, it's not so bad!"
    show old_tori 39 with dissolve.nowait
    anon "..."
    show old_anon 21
    show old_tori 40
    with dissolve
    anon "Now this part I like!"
    show old_anon 28
    show old_tori 41 with dissolve.nowait
    pause
    show old_tori 42 with dissolve.nowait
    pause
    show old_anon 83c
    show old_tori 43
    with dissolve
    pause
    show old_tori 44 with dissolve
    pause
    show old_tori 45
    tori "Ready to get started?"
    show old_anon 83b
    show old_tori 44
    anon "You bet!"

    if saga.cast.tori < 'plug':
        anon "I'm really excited to-"
        show old_anon 82
        pause
        show old_anon 83
        anon "Do you hear a buzzing sound?"
        show old_anon 82
        show old_tori 45
        tori "Hehe, maaaaaybe..."
        show old_tori 44
        anon "..."
        show old_tori 45
        tori "Don't look so worried, [saga.cast.anon]!"
        show old_tori 90 with dissolve
        tori "It's just my new toy."
        tori "I've had it in all day."
        show old_anon 83
        show old_tori 44 with dissolve
        anon "O-okay."
        show old_anon 83
        pause
        anon "... But if we're going into the augmented reality, won't I feel-"
        show old_anon 81
        show old_tori MC eyes as anon_eyes
        anon "( !!! )" with hpunch

    scene school_office2_chair space -chair
    show old_tori sex 1b_2b_3b_4b_5b_6b_7b_8b_9b_10b s150
    with flash
    jump tor06_office2.loop


label tor_office.area:
    show anon a_side f_horny at pos(.55)
    anon "I can't wait to get you out of that lab coat..."
    show old_tori 3
    tori "What, right here in front of everyone?"
    show old_tori 6
    anon f_shy "N-no, I meant upstairs in-"
    show anon f_surprised
    show old_tori 7
    tori "Like, you'll sweep everything off one of these lab benches, throw me down, and have your way with me?!"
    show old_tori 6
    anon a_uneasy f_worried_surprised "That's not-"
    show anon f_confused
    show old_tori 10c
    tori "Our heaving bodies entwined in a carnal embrace for all the students to see!"
    show old_tori 10b
    anon a_finger f_worried "Umm, [saga.cast.tori]?"
    show old_tori 10c
    tori "Your muscles glistening with perspiration as we grapple for control..."
    show old_tori 10b
    anon a_side f_surprised of_blush @ -m_talk "..."
    show anon d_hard
    show old_tori 77
    tori "... Your throbbing cock driving into me, over and over and over!"
    show old_tori 78
    anon f_worried "Okay, never-"
    show anon e_s f_surprised
    show old_tori 79
    tori "Ngh, give it to me [saga.cast.anon]!!"
    show anon a_shy_down e_sw f_worried_surprised at center
    show old_tori 81
    tori "Yes, yes, YES!!!"
    show old_tori 79 at pos(.715, 1.35)
    show anon e_e
    pause
    show old_tori 77
    show anon e_w
    pause
    hide anon with dissolve
    return


label tor_office.busy:
    anon "You know, you're looking especially sexy right now, [saga.cast.tori]..."
    show anon f_worried_surprised
    show old_tori 5
    tori "Not now, [saga.cast.anon]!"
    show old_tori 3
    tori "Can't you see I'm close to a breakthrough here?!"
    show old_tori 10b at pos(.45), face_left
    anon a_rub f_shy "Oh, you are?"
    show old_tori 10c
    tori "With the proper application of electrical stimulus between the L1 and L3 vertebrae, an orgasmic feedback loop {i}should{/i} theoretically be possible..."
    show old_tori 10b
    anon a_side f_confused "Umm, huh?!"
    show old_tori 10c
    tori "... Of course, I'll need to heighten pineal function and keep the subject's brain from liquefying."
    show old_tori 10
    anon "Right, I'll just leave you to it then."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
