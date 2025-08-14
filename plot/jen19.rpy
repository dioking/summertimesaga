label jen19_intro:
    scene debbie_bed3 at stage
    show anon a_think e_nw f_pensive o_right at left with dissolve
    anon @ -m_talk "( Hmm, I wonder if [saga.cast.jenny] is still pissed at me? )"
    anon @ -m_talk "( She's probably downstairs eating breakfast right now. )"
    anon @ -m_talk "( Maybe I should go and talk to her? )"
    hide anon with dissolve
    return


label jen19_intro.jenny:
    if saga.cast.jenny in saga.sets.debbie_dining:
        call shot.debbie_dining_breakfast
        show jenny a_phone e_s f_annoyed p_table behind table
        pause
        show debbie_dining_table -chair3 -chair4 -table_legs
        show anon a_pocket e_wsw f_worried p_stand_far behind jenny at pos(.7)
        show debbie_dining_table chair3 chair4 table_legs as chairs behind jenny
        with dissolve.nowait

    elif saga.cast.jenny in saga.sets.debbie_yard:
        call shot.debbie_yard_jenny
        show anon a_pocket f_worried at right with dissolve.nowait
    else:

        call shot.debbie_bed2_jenny
        show anon a_pocket f_worried o_right at left with dissolve.nowait

    anon "[saga.cast.jenny]?"

    if saga.cast.jenny in saga.sets.debbie_dining:
        show jenny e_wnw

    jenny "Nu uh!"
    anon "Wha-"

    if saga.cast.jenny in saga.sets.debbie_dining:
        show jenny a_point_out
    else:
        show jenny a_point

    jenny "Get the fuck out of here asshole!!"
    anon "Would you just let me apologize?"

    if saga.cast.jenny in saga.sets.debbie_dining:
        show jenny p_table_rise
        show debbie_dining_table pull2
    else:

        show jenny a_upset

    show anon f_afraid m_teeth
    jenny f_angry m_teeth "I said fuck off, [saga.cast.anon]!!!"
    anon a_surrender "Okay, okay... I'm leaving."
    hide anon with dissolve
    return


label jen19_jenny:
    call shot.debbie_dining_breakfast
    show debbie_dining_table food3 plate3 -bowl3 as table
    show jenny a_phone e_s p_table behind table
    pause
    show debbie_dining_table -chair3 -chair4 -table_legs
    show anon a_pocket e_wsw f_worried p_stand_far behind jenny at pos(.7)
    show debbie_dining_table chair3 chair4 table_legs as chairs behind jenny
    with dissolve.nowait
    anon "Good morning."
    hide chairs
    show debbie_dining_table chair3 chair4 table_legs
    show anon a_bowl_01 e_s p_table at center
    with dissolve
    jenny @ -m_talk "..."
    anon e_e f_confused "You still pissed at me?"
    jenny e_w @ -m_talk "Hmm?"
    jenny f_annoyed "Oh."
    jenny "Morning, asshole!"
    anon f_calm "Heh, you're still mad."
    show anon a_bowl e_s
    jenny f_angry m_teeth "Of course, I'm mad!"
    show anon f_worried
    jenny "You're disgusting!"
    anon a_down e_e "Look, I didn't mean to cum on you! It was just-"
    jenny f_sad -m_teeth "Shhh!!!"
    jenny f_annoyed "Not so loud dummy, [saga.cast.debbie] will hear you!"
    anon @ e_w "Right, sorry."
    jenny f_angry m_teeth "I had to do laundry because of you!"
    jenny "You know I hate doing laundry!"
    anon f_confused "I thought [saga.cast.debbie] still did your laundry?"
    jenny "Well, I can't exactly just hand her a bunch of cum stained bed sheets to wash, now can I?!"
    anon f_worried "No, I guess not..."
    jenny e_r f_annoyed -m_teeth "Moron."
    show jenny e_w

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon f_grumpy "You don't have to be such a bitch about it."
        jenny "Ugh."
    else:

        anon @ -m_talk "..."
        anon "Seriously, I'm sorry!"

    jenny "Whatever."
    jenny "Next time it happens, {i}you're{/i} washing my sheets!"
    anon f_calm "Next time?"
    jenny "Well, yeah..."
    jenny f_calm "... We made mad bank with that stream!"
    anon f_surprised "Really?"
    jenny "Here."
    jenny a_money "Your cut."
    anon "Whoa, thanks!"
    show jenny a_fold
    pause
    anon f_calm "So when is our next show?"
    jenny "Any time in the afternoon works for me."
    jenny "Just come to my room."
    anon f_happy "Awesome!"
    show debbie_dining_table pull4
    show debbie a_potato e_wsw p_table_stand behind jenny
    show anon e_nw f_calm
    show jenny a_spoon e_s
    with dissolve.nowait
    debbie "Who's hungry?"
    anon "Me!"
    debbie "Hehe!"
    debbie "Here you go, sweetie."
    show debbie e_sw p_table_bend
    show anon e_sw f_horny
    pause
    show anon e_nw f_worried
    debbie e_wsw p_table_stand "Are you kids getting along okay?"
    show jenny e_w f_worried
    pause
    anon f_calm "Y-yes?"
    show jenny e_s f_calm
    debbie "Good."
    debbie "It warms my heart, you two spending time together."
    show jenny e_r f_annoyed
    anon "T-thanks, [saga.cast.debbie]."
    show jenny e_s f_calm
    debbie @ -m_talk "Mhmm."
    show anon e_s f_shy
    hide debbie
    with dissolve
    pause

    scene black
    with dissolve
    mono ""
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
