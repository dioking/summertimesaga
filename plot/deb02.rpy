label deb02_debbie:
    call shot.debbie_kitchen_stool
    show debbie a_pen e_s f_sad o_right oa_hand p_table_lean_in z_b_ob_f_of_a behind island at pos.kitchen_stool
    show mimic debbie at pos.debbie
    show anon a_pocket o_right at pos(.3) with dissolve
    anon "Hi, [saga.cast.debbie]."
    debbie e_e f_shy "Hey, sweetie."
    anon a_point f_confused @ e_wsw "Whatcha doing?"
    debbie e_s f_sad "Oh, you know how your father always did the crossword with his coffee in the morning."
    anon a_side f_calm "Of course."
    debbie a_down_low e_e p_table "Well, his paper's just been sitting here... and I keep looking over at it and replaying the funeral in my head..."
    anon f_confused "So you thought, maybe doing it would give you some relief?"
    debbie a_pen e_s p_table_lean_in "... Y-yeah."
    show anon e_wsw f_worried
    pause
    anon e_w "Is it working?"
    debbie "Not really."
    show anon a_surprised e_sw behind island at pos(.425)
    anon @ -m_talk "Hmm."
    anon a_tired f_confused p_bend "Looks like you're pretty close to finishing it."
    debbie @ e_se f_shy "Yeah..."
    debbie "... It's this one here that's giving me the most trouble."
    label deb02_debbie.cookie hide:
    anon "Hmm, a four letter word for a private investigator?"

    if _in_replay:
        jump deb02_debbie.fast

    $ renpy.dynamic(pool=set())

    menu deb02_debbie.choice:
        set pool
        "Perp":

            jump deb02_debbie.perp
        "Dick":

            pass
        "John":

            jump deb02_debbie.john
        "Fuzz":

            jump deb02_debbie.fuzz

    label deb02_debbie.fast hide:
    anon e_nw "Dick?"
    debbie e_se f_annoyed "[saga.cast.anon], language!!"
    show debbie e_e
    anon a_wtf e_w f_surprised -p_bend "W-what, I'm serious!"
    anon f_shy "I've heard them called that in movies."
    show anon a_side
    debbie e_s f_disgusted @ -m_talk "..."
    show anon e_sw f_happy
    debbie f_calm "Oh, wow... you're right!"
    show anon e_w f_surprised
    debbie @ e_e f_elated "Dick was exactly what I needed."
    anon a_uneasy e_b f_happy m_laugh @ -m_talk "{i}*Snort*{/i}"
    debbie f_shy "Well, that's a silly thing to call them..."
    show anon a_side e_w -m_laugh
    debbie "... I never would have gotten that!"
    anon f_shy "Oh, I'm sure you would have gotten that dick eventually."
    debbie e_e f_calm "No way."
    show anon f_happy
    debbie f_elated "Great job, sweetie!"
    debbie a_stretch_pen_01 e_b f_calm p_table "Ugh, I feel like I've been staring at that for twenty minutes now!"
    show anon e_nnw f_shy
    show debbie a_stretch_pen_02 -oa_hand
    pause
    show debbie_kitchen as island behind anon
    show mimic debbie behind anon
    show anon a_surprised e_sw f_surprised -o_right
    debbie a_down_low e_e f_shy oa_hand "Dang it!"
    show anon e_s o_right at pos(.3)
    show debbie e_se
    "*Sounds of a pen rolling across the floor*"
    hide mimic
    show debbie p_table_twist_turn z_reset
    anon a_side f_shy "I've got it."
    hide debbie
    show anon b_debbie p_bend_bonk behind island at pos(.4)
    with none.nowait
    "*Bonk*" with hpunch

    scene debbie_kitchen base at stage(.6, .5, 3, b=0)
    show debbie e_sw f_shy p_kitchen_drop
    show anon e_b f_hurt m_teeth p_kitchen_drop
    with fade
    anon @ -m_talk "Ack!"
    debbie "Hehe, you alright?"
    anon @ -m_talk "Errrmhrmm."
    debbie "Aww, my poor baby..."
    debbie "... Come here."
    hide anon
    debbie p_kitchen_drop_kiss @ -m_talk "Muah!"
    show anon e_se f_surprised p_kitchen_drop
    debbie p_kitchen_drop "There we go."

    scene debbie_kitchen_cleavage dawn with none.nowait
    with hpunch
    pause
    debbie "Better?"
    pause
    debbie "Sweetie?"
    anon "Hmm?"
    debbie "Better?"

    call shot.debbie_kitchen_stool
    show debbie f_curious behind island at pos(.6)
    show anon a_rub d_hard f_shy o_right of_blush at pos(.375)
    with fade
    anon "Y-yeah, umm..."
    pause
    show anon e_s with dissolve
    anon f_shocked @ m_open "!!!"
    anon a_cover_dick e_w f_worried_surprised "... Gee, look at the time..."
    show anon p_run_away -o_right at pos(.315)
    show debbie f_surprised
    with dissolvefast.nowait
    anon f_shy "... I should get going!"
    hide anon
    with dissolvefast.nowait
    debbie a_embarrassed "But sweetie, you haven't even eaten yet!"
    anon "That's okay!"
    show debbie a_clasp f_curious
    anon "Busy, busy... ya know?!"
    debbie "Uhh, alright..."
    debbie "... Be safe."
    $ renpy.end_replay()

    scene debbie_lobby at stage with fade
    show anon a_facepalm d_hard e_sw f_shy_surprised of_blush with dissolve
    anon @ -m_talk "( Sheesh, that was embarrassing! )"
    anon a_shy_down e_s f_confused @ -m_talk "( I've never gotten one of {i}those{/i} with [saga.cast.debbie] before... )"
    anon f_pensive @ -m_talk "( ... Why would that even- )"
    pause
    anon a_rub e_osw f_sad -of_blush @ -m_talk "( It's probably just stress... )"
    pause
    anon a_handshake f_serious @ -m_talk "..."
    show anon a_cheek e_b f_distressed m_teeth with none.nowait
    "*Slap*" with hpunch
    anon a_protect d_none @ -m_talk "( Ugh, shake it off [saga.cast.anon]! )"
    anon a_fists e_sw f_grumpy -m_teeth @ -m_talk "( Get a grip! )"
    hide anon with dissolve
    return


label deb02_debbie.fuzz:
    anon @ e_nw "Fuzz?"
    debbie "Hmm, no that doesn't fit."
    pause
    debbie "Any other ideas?"
    jump deb02_debbie.choice


label deb02_debbie.john:
    anon @ e_nw "John?"
    debbie "Hmm, no that doesn't fit."
    pause
    debbie "Any other ideas?"
    jump deb02_debbie.choice


label deb02_debbie.perp:
    anon e_nw "Perp?"
    debbie "Hmm, no that doesn't fit."
    show anon e_sw
    pause
    debbie "Any other ideas?"
    jump deb02_debbie.choice


label deb02_outro:
    return


label deb02_outro.block:
    scene debbie_lobby at stage
    show anon e_sw f_worried with dissolve
    anon @ -m_talk "( Nah, I should steer clear of [saga.cast.debbie] while my... {i}thing{/i} is on the fritz. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
