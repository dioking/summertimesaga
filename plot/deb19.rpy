label deb19_intro:
    call sleep

    scene debbie_bed3_side -blanket
    show anon c_pants e_b p_bed3_visit at tint('00106545')
    show debbie_bed3_side blanket sleep as blanket
    with fade
    pause
    show anon e_ne f_tired p_bed3_visit_sit
    pause
    anon @ -m_talk "( Man, I just can't seem to fall asleep tonight. )"
    anon @ -m_talk "( So many things have happened lately and my mind is just racing like crazy. )"
    show anon e_wsw
    pause
    show debbie_bed3_side mess as blanket behind anon
    show anon a_rub e_w p_stand at pos(.1), blur(20), zoom(1.75)
    anon @ -m_talk "( Maybe a glass of warm milk will help? )"
    hide anon with dissolve
    return


label deb19_kitchen:
    call shot.debbie_kitchen_island
    show debbie a_nervous o_right p_stand_away at right
    show anon c_pants o_right p_stretch at left with dissolve
    anon "{i}*Yawn*{/i}"
    anon a_rub f_confused p_stand "[saga.cast.debbie]?"
    show anon e_wsw
    debbie a_pills_open c_robe_open f_confused o_left p_stand @ -m_talk "Hmm?"
    show anon f_surprised
    debbie a_tied f_worried_surprised "Oh, umm..."
    show anon a_side f_horny_smug
    debbie f_shy "... S-sweetie, I'm sorry... I-"
    show debbie f_confused
    pause
    debbie a_wtf e_s f_surprised of_blush "Oh!"
    show anon f_shy
    show debbie a_open_01 c_robe
    pause
    show anon e_w
    debbie a_clasp e_w f_worried_surprised "{i}*Ahem*{/i}"
    debbie f_shy "I thought you'd gone to bed."
    anon f_worried "Yeah, I had."
    show debbie f_sad
    anon e_s "Couldn't fall asleep though..."
    show debbie of_none
    pause
    anon e_w "... Came down here thinking a glass of warm milk might help."
    debbie e_sw "Ah, I see."
    anon f_confused "What are you doing up?"
    debbie e_w @ -m_talk "Hmm?"
    debbie "Oh, nothing... I just-"
    debbie f_shy "M-my throat was dry and I thought a glass of water would-"
    show debbie f_worried_surprised
    anon f_worried "And the pills?"
    debbie a_nervous f_shy "Heh, saw those, did ya?"
    anon f_shy "I did."
    debbie o_right p_stand_away "It's nothing to worry about, sweetie..."
    show anon e_wsw
    debbie a_pills_open e_sw o_left p_stand "... Just a little sleep aid [saga.cast.diane] gave me after the funeral."
    anon e_w f_confused "Oh?"
    debbie a_pills_clasp e_w "I thought it was silly at the time but they really have come in handy."
    anon f_worried "I didn't realize you were struggling so much."
    debbie f_sad "We're all struggling, sweetie."
    anon e_osw f_sad "Yeah, I suppose you're right about that."
    pause
    debbie a_nervous o_right p_stand_away "Everything's been so chaotic since your father passed."
    show anon e_wsw f_worried
    show debbie a_reach p_bend_away at pos(y=1.1)
    debbie "Dealing with the fallout, and all his assets..."
    debbie "... Funeral preparations, police investigations, and now these Russian thugs."
    show anon e_w
    show debbie a_side o_left p_stand at pos(y=1.)
    debbie "I feel like I've hardly had time to process any of it."
    anon "Y-yeah, I know what you mean."
    anon "But then at night, everything quiets down and it all just hits you at once."
    show anon e_osw f_sad
    debbie e_sw "Yeah."
    debbie a_cover "And the worst part is lying in there, alone... in that big empty bed."
    debbie "I keep reaching out, thinking he'll be there and he's just..."
    show anon e_w f_worried_surprised
    debbie a_cover_face e_b f_crying "... Gone."
    show anon a_surprised f_worried behind debbie at center
    anon "Aww, [saga.cast.debbie]."
    hide anon
    debbie b_anon_pants p_hug "I don't wanna be alone anymore!"
    anon "Shh, you're not alone."
    anon "I'm here."
    debbie @ -m_talk "{i}*Sniff*{/i}"
    anon "Everything is gonna be alright, I promise."
    show anon c_pants f_shy o_right
    debbie a_side e_w f_sad p_stand -b_anon_pants "I don't suppose, you'd-"
    anon f_confused "What?"
    debbie a_clasp e_s f_shy of_blush "N-no, never mind... it's silly."
    anon "Tell me."
    debbie e_w "Do you maybe, wanna... sleep in my bed tonight?"
    anon f_surprised "Really?"
    debbie f_sad "I know, it's stupid... but-"
    anon f_worried "N-no, it's not stupid!"
    anon f_calm "I'd be happy to."
    debbie f_shy "You're not embarrassed..."
    debbie "... Sleeping in your landlady's bed?"
    anon "Not at all."
    anon "In fact, I think it would be good for both of us."
    show anon f_shy
    debbie e_se "Alright, well... then maybe I won't need those pills tonight after all."
    show anon e_sw
    pause
    show anon e_w f_calm
    debbie a_surprised e_w f_calm "C'mon, sweetie."
    hide debbie with dissolve.nowait
    anon a_neck f_shy_surprised o_left @ -m_talk "( Man, is this really happening? )"
    debbie "You coming?"
    anon f_shy "Mhmm, right behind you."
    show anon a_surprised at pos(.15)
    anon @ -m_talk "( Alright, I've gotta keep my head here... this isn't the time to push things. )"
    hide anon with dissolve

    label deb19_kitchen.cookie hide:
    scene debbie_bed1_top -sheet
    show debbie e_sw p_sleep_awake
    show debbie_bed1_top sheet as sheet
    show layer master at tint('00106545')
    with fade
    pause
    hide sheet
    show anon c_pants p_bed1_climb
    with dissolve.nowait
    pause
    show anon p_bed1_leave
    pause
    show debbie_bed1_top far sheet as sheet
    show anon a_rest e_ne o_right p_bed2_side at pos.bed1_sleep
    pause
    debbie "Are you sure you're okay with this?"
    show anon at pos.bed1_sleep
    anon "Of course."
    debbie "I know it's silly but I feel so much better knowing there's someone here with me."
    anon "I'll always be here for you, [saga.cast.debbie]... if you want me to be."
    debbie "Thank you, sweetie."
    debbie "You're such a good boy..."
    debbie "... I dunno what I did to deserve you."
    anon "Heh, I feel the same way about you."
    debbie of_blush "That's-"
    debbie "Really... sweet."
    debbie "I-"
    pause
    debbie "{i}*Ahem*{/i} Well, goodnight."
    show debbie e_b of_none
    anon "Goodnight."
    show anon e_b
    pause
    debbie e_sw @ -m_talk "..."
    anon e_ne @ -m_talk "..."
    show debbie_bed1_top xray as sheet
    with dissolve.nowait
    pause
    hide anon
    show debbie_bed1_top near -far as sheet
    show debbie b_anon p_sleep_peck
    pause
    debbie "Mmm."
    anon "( She's not pulling away? )"
    pause
    show debbie p_sleep_kiss
    anon "( !!! )"
    anon "( Wow, this is a lot more than a \"goodnight kiss\". )"
    debbie p_sleep_peck "Mmm."
    pause
    anon "( Maybe I should see about pushing things a little further? )"

    if _in_replay:
        jump deb19_kitchen.fast1

    menu:
        "Stop things here.":
            jump deb19_kitchen.bail
        "Kiss lower.":

            pass

    label deb19_kitchen.fast1 hide:
    show debbie_bed1_top -near as sheet
    debbie a_up ob_anon_kiss_neck p_sleep_awake -b_anon @ -m_talk "Mmm."
    pause
    debbie "Ahh!"
    pause
    debbie "T-that feels..."
    debbie "... So good!"
    pause

    if _in_replay:
        jump deb19_kitchen.fast2

    menu:
        "Stop things here.":
            jump deb19_kitchen.bail
        "Keep going.":

            pass

    label deb19_kitchen.fast2 hide:
    show debbie_bed1_top near as sheet
    show anon a_open_debbie_01 c_pants e_sse f_shy o_right p_bed2_side behind sheet at pos.debbie.sleep_open
    show debbie a_side c_robe_flat ob_none z_b_f_of
    show mimic debbie behind sheet
    pause
    show anon a_open_debbie_02
    show debbie e_ssw f_shy
    pause
    hide anon
    hide mimic
    show debbie_bed1_top -near as sheet
    debbie a_robe f_distressed ob_anon_tease z_reset "Oh, sweetie!"
    show debbie e_b
    pause
    debbie "Haah!"
    anon "Mmm."
    show debbie f_shy m_lip
    pause

    if _in_replay:
        jump deb19_kitchen.fast3

    menu:
        "Stop things here.":
            jump deb19_kitchen.bail
        "Don't stop.":

            pass

    label deb19_kitchen.fast3 hide:
    debbie e_ssw ob_anon_suck "Goodness, I-"
    show debbie e_b
    pause
    debbie @ f_distressed "Oh, baby!"
    debbie @ e_ssw "W-we, shouldn't-"
    pause
    debbie @ f_distressed "Ahh!!"
    pause

    if _in_replay:
        jump deb19_kitchen.fast4

    menu:
        "Stop things here.":
            jump deb19_kitchen.bail
        "Reach lower.":

            pass

    label deb19_kitchen.fast4 hide:
    debbie e_ssw ob_anon_reach -m_lip "N-no, sweetie..."
    debbie a_none e_sw f_calm ob_reject_anon "... We can't-"
    show debbie_bed1_top far -near as sheet
    show debbie a_down c_robe ob_none
    show anon a_rest c_pants e_ne f_shy o_right p_bed2_side behind sheet at pos.bed1_sleep
    anon "Are you sure?"
    debbie @ -m_talk "{i}*Gulp*{/i}"
    debbie "That's too much..."
    debbie "... it wouldn't... be right."
    anon f_calm "Yeah, okay."
    pause
    debbie "Thank you..."
    debbie "... For respecting my boundaries."
    anon "Of course."
    anon e_b "Sweet dreams, [saga.cast.debbie]."
    debbie "Mm, you too."
    debbie "My wonderful boy."
    show debbie p_sleep
    pause

    scene black
    with dissolve
    return


label deb19_kitchen.bail:
    show debbie_bed1_top far -near as sheet
    show debbie a_down b_default c_robe e_sw f_calm m_idle ob_none p_sleep_awake
    show anon a_rest c_pants e_ne f_shy o_right p_bed2_side behind debbie at pos.bed1_sleep
    anon "{i}*Ahem*{/i} R-right, well..."
    anon e_b f_calm "Sweet dreams, [saga.cast.debbie]."
    debbie "Y-yeah, umm..."
    debbie "... {i}*Gulp*{/i} You too, my wonderful boy."
    show debbie p_sleep
    pause

    scene black
    with dissolve
    return


label deb19_kitchen.rails:
    scene camera
    show anon c_pants f_tired with dissolve
    anon @ -m_talk "( I doubt I'll find any warm milk there. )"
    anon @ -m_talk "( Maybe try the kitchen? )"
    return


label deb19_wake:
    scene debbie_bed1_top -sheet
    show debbie a_down e_sw p_sleep_awake
    show anon a_rest c_pants e_b o_right p_bed2_side at pos.bed1_sleep
    show debbie_bed1_top far sheet as sheet
    with fade
    debbie "Sweetie?"
    anon @ -m_talk "Hmm?"
    debbie "Sweetie, wake up."
    anon "{i}*Yawn*{/i}"
    anon e_ne "What time is it?"
    debbie "It's early."
    debbie "But you'd probably better get back upstairs to your own bed, just in case [saga.cast.jenny] gets up."
    anon "Mm, yeah... okay."
    anon "How did you sleep?"
    debbie "I slept great!"
    debbie "Best sleep I've had since... well..."
    debbie "... For a long time."
    anon "Yeah, me too."
    pause
    anon "I guess, this was a good idea then."
    debbie "I'd say so, yes."
    anon "Does that mean this can be a regular thing?"
    debbie "Well, I-"
    debbie "I suppose, so long as we're careful."
    debbie "I wouldn't want-"
    anon "You don't want [saga.cast.jenny] to find out... Yeah, I know."
    debbie "Heh."
    anon "I'll be careful."
    debbie "That's my boy."
    hide anon
    debbie b_anon p_sleep_peck_01 "Mmm."
    show anon a_rest c_pants e_ne o_right p_bed2_side behind sheet at pos.bed1_sleep
    debbie p_sleep_awake -b_anon "Now get that cute butt upstairs while I get started on breakfast!"
    anon "Yes, ma'am."
    hide sheet
    show anon o_left p_bed1_leave at center
    pause
    hide anon
    show debbie_bed1_top sheet as sheet
    with dissolve

    scene black
    with dissolve
    mono ""

    call shot.debbie_bed3_bedside
    show anon p_top_on
    with dissolve
    pause
    anon f_happy p_stand @ -m_talk "( What a start to the day... )"
    anon a_cheer e_b m_teeth @ -m_talk "( ... It's put a real spring in my step! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
