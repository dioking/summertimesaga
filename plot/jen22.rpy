label jen22_intro:
    jump jen19_intro


label jen22_intro.jenny:
    jump jen19_intro.jenny


label jen22_jenny:
    call shot.debbie_dining_breakfast
    show debbie_dining_table food3 plate3 -bowl3 as table
    show jenny a_phone e_s f_annoyed p_table behind table
    pause
    show debbie_dining_table -chair3 -chair4 -table_legs
    show anon a_pocket e_wsw f_shy p_stand_far behind jenny at pos(.7)
    show debbie_dining_table chair3 chair4 table_legs as chairs behind jenny
    with dissolve.nowait
    pause
    hide chairs
    show debbie_dining_table chair3 chair4 table_legs
    show anon a_down e_e p_table at center
    with dissolve
    jenny @ -m_talk "..."
    anon "Good morning."
    jenny "Yeah, morning."
    pause
    anon "Are you going to pay me for that camshow?"
    jenny e_w "Oh, you wanna get paid to cum down my throat, huh?"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon f_grumpy "[saga.cast.jenny], I warned you!"
        jenny "Yeah, well, it's hard to concentrate on what you're saying!"
        jenny f_sad "You're really good at-"
        show anon f_confused
        show jenny f_surprised
        pause
        jenny e_s f_annoyed "Never mind."
        anon "Really good at what?"
        anon f_horny "... Eating your pussy?"
        jenny e_w "I didn't say that..."
        anon f_calm "Mmm, you kinda did..."
        jenny a_fold "Shut up."
        pause
        anon f_confused "So are you going to pay me or what?"
    else:

        anon f_worried "I said, I was sorry..."
        show jenny e_s
        pause
        anon "You know, you came in my mouth too!"
        jenny f_calm "Haha, oh yeah!"
        jenny e_w "I forgot about that..."
        anon f_shy "You practically waterboarded me!"
        jenny @ e_b m_laugh "HAHAHAAH!"
        pause

    jenny @ e_r f_annoyed "{i}*Sigh*{/i} Fine."
    jenny a_money "I guess you earned it."
    show jenny a_phone e_s f_calm
    anon f_calm "Thanks."
    show anon a_bowl e_s f_shy
    pause
    jenny "You know, my fans really did like that show."
    anon a_bowl_01 e_e f_calm "Yeah?"
    jenny "It's got more than double the views that our handjob video has."
    anon a_down "That's great!"
    jenny e_w f_snide "Yeah, it means you're going to be eating a lot more pussy."

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon f_happy "... And you'll be sucking a lot more dick."
        jenny e_ssw "Tch, yeah... maybe."
        anon @ e_b m_laugh "Haha!"
        show jenny e_w f_annoyed
    else:

        anon f_surprised @ -m_talk "!!!"
        anon f_shy "O-okay."
        jenny "Lucky little loser..."

    jenny f_annoyed "Just don't go thinking I enjoy-"
    show jenny f_surprised
    show anon e_w f_worried
    debbie "What are you kids talking about?" with hpunch
    show anon e_nw
    show debbie a_potato e_wsw p_table_stand behind jenny
    show jenny e_wsw
    debbie "Has [saga.cast.anon] been eating something?"
    anon "I..."
    show jenny e_se
    anon e_w "W-we aren't..."
    jenny "Peaches!"
    anon e_e "Huh?!"
    jenny e_w "I bought some peaches the other day..."
    jenny f_calm "... [saga.cast.anon] was eating my peaches."
    show anon e_nw
    debbie "Oh, I love peaches!"
    debbie "They're so juicy!"
    anon e_b f_happy m_laugh @ -m_talk "{i}*Snort*{/i}"
    show anon e_e f_calm -m_laugh
    jenny f_snide "Heh, you should have seen him when he finished."
    show anon f_pouty
    jenny "[saga.cast.anon] is a real sloppy eater."
    debbie "Hehe, was his face all messy?"
    jenny e_b f_calm m_laugh @ -m_talk "He even had some in his hair!"
    show jenny e_w f_snide -m_laugh
    debbie @ e_b f_happy m_laugh "Haha!"
    pause
    debbie "It's nice you're sharing with [saga.cast.anon]."
    show anon e_nw f_pensive
    debbie "One day, you kids are going to realize how fortunate you are to have one another."
    anon f_calm "Heh, you think?"
    jenny "Yeah, right."
    debbie "Now, who wants bacon?!"
    anon "Oh, me!"
    show anon e_sw f_horny
    show debbie e_sw p_table_bend
    show jenny e_r f_annoyed
    pause

    scene black
    with dissolve
    mono ""
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
