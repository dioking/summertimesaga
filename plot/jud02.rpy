label jud02_hall1w:
    call shot.school_hall1w_judith
    show judith a_clasp f_afraid o_right at pos(.215)
    show camila a_fold at pos(.65)
    show val a_hips at pos(.8)
    with None
    val "Just look at those nasty-ass saggy tits!"
    judith a_cover_boobs e_s f_sad @ f_surprised_afraid "Eep!"
    camila "She's probably too poor to afford a bra..."
    judith e_w "It's not like that!!"
    val "You think you're gonna get the boys' attention showing your tits around like that?"
    judith e_s "My breasts are sensitive!! It hurts when I wear a bra..."
    judith a_clasp @ f_nervous "I'm just more comfortable like this!!"
    show judith e_w
    val @ e_b f_happy m_laugh "Haha!"
    show judith a_cover_face e_b f_crying
    camila f_angry "Yo, you better not hang around here no more..."
    pause
    camila a_sign "PUTA! Did you just hear? This is our turf, so get out!"
    show anon a_pocket f_confused o_right behind judith at pos(.375)
    with dissolve.nowait
    anon "What's going on here?!"
    show anon e_e f_worried
    show camila a_fold
    judith @ -m_talk "{i}*Sobbing*{/i}"
    show anon e_w f_pouty
    show val f_annoyed
    camila "You defending this ugly bitch now?"
    val "Keep walking white boy!"
    pause
    anon e_e f_worried "Are you okay [saga.cast.judith]?"
    show anon a_surprised e_w -o_right
    hide judith
    with dissolve
    camila "What's the matter, white boy, you not gonna run after your bitch?"
    anon a_side f_sceptical o_right "You didn't have to do this..."
    camila a_sign "We'll do whatever the fuck we want!"
    val e_b f_happy m_laugh @ -m_talk "Haha! See ya!"
    hide val
    hide camila
    with dissolve
    pause
    anon f_worried -o_right @ -m_talk "( I think [saga.cast.judith] ran into the girls' locker room... )"
    anon @ -m_talk "( ... Perhaps I should see if she's okay. )"
    hide anon with dissolve
    return


label jud02_stall:
    scene school_stall
    show judith p_sit_cry
    window hide
    pause
    show anon e_sw f_surprised behind judith at pos.stall with dissolve
    anon f_worried @ f_surprised -m_talk "!!!"
    judith "{i}*Sobbing*{/i}"
    anon "[saga.cast.judith]?!"
    judith a_shy e_nw f_sad p_sit_legs "... Hey, [saga.cast.anon]."
    show judith e_ssw
    anon "Are you okay?"
    judith "I just wanted to stay away, from everyone."
    anon f_confused "What do you mean?"
    judith e_nw "No one likes me... and everyone makes fun of my body..."
    judith @ e_w "... So at least in here I won't be made fun of."
    anon f_worried "You can't let these people get to you that way!"
    judith e_ssw "They're right, though. I am ugly..."

    if _in_replay:
        jump jud02_stall.fast1

    menu:
        "You're not ugly!":
            pass
        "I know...":

            jump jud02_stall.bail1

    label jud02_stall.fast1 hide:
    anon a_handshake f_shy "I don't think you're ugly at all!!"
    judith e_nw f_shy "... Really?"
    anon a_side f_calm "Yeah!"
    anon @ f_happy "I think you look good!"
    judith e_ssw "That's... the nicest thing anyone has said to me..."
    anon "Well, I'm just being honest... and I'm sure I'm not the only one!"
    anon "You just have to ignore all the negative stuff at school."
    judith "I guess you're right..."
    anon a_point_back "Anyway, we should probably get out of here and back to class."
    pause
    anon a_side f_confused "[saga.cast.judith]?"
    show anon e_s f_surprised
    judith a_touch_anon e_nw p_sit "Wait!"
    show anon e_sw f_shy_surprised
    judith "Stay here a little longer... with me..."

    if _in_replay:
        jump jud02_stall.fast2

    menu:
        "Ok.":
            pass
        "We should leave.":

            jump jud02_stall.bail2

    label jud02_stall.fast2 hide:
    anon "Oh... okay."
    judith "Do you remember the other day when..."
    judith e_w "... We were both in the locker room? In front of [saga.cast.annie]?"
    show anon e_nw f_pensive
    pause
    anon e_sw f_confused "Yeah?"
    judith e_nw "Well, I... I liked the way you looked at me."
    anon f_shy_surprised @ -m_talk "!!!"
    judith e_ssw "It wasn't just your eyes... your body was also reacting."
    anon f_shy @ -m_talk "..."
    judith e_nw "Was it my breasts that made you... so happy... {i}down there{/i}?"
    anon f_worried "I... I'm sorry!"
    judith "Don't be sorry!!"
    judith e_ssw "... I really liked it and..."
    show anon f_surprised
    judith e_nw "... I was wondering If I could, you know, see it again?"

    if _in_replay:
        jump jud02_stall.fast3

    menu:
        "Sure.":
            pass
        "I can't.":

            jump jud02_stall.bail3

    label jud02_stall.fast3 hide:
    anon f_shy "I guess so..."
    judith "Let me..."
    show judith a_anon_bottom_down_01 e_ssw p_sit_lean
    anon a_surprised e_s f_surprised @ -m_talk "!!!" with hpunch
    show judith a_anon_bottom_down_02 f_happy
    show anon c_casual_down
    pause
    show judith a_anon_bottom_down_03 f_surprised
    pause
    show anon d_hard z_b_ob_f_of_a_oa_d_od
    show judith a_surprised p_sit
    pause
    show anon a_side e_sw f_shy_surprised
    judith f_shy "Oh, wowie waffles!"
    pause
    show anon d_none e_s f_shy
    judith a_rub_anon_04 oa_lap "It's so... nice..."
    show judith a_rub_anon s_12
    anon a_surprised "{i}*Gasp*{/i}"
    show anon f_horny
    judith "... And thick."
    show anon a_side e_sw
    judith e_nw "I just love how it feels in my hand..."
    show anon e_s
    pause
    judith @ -m_talk "..."
    show anon e_sw
    judith "Would you like to touch my breasts?"

    if _in_replay:
        jump jud02_stall.fast4

    menu:
        "Yes.":
            jump jud02_stall.merge2
        "Faster.":

            pass
        "We should stop.":

            jump jud02_stall.bail4

    label jud02_stall.fast4 hide:
    anon "Could you stroke it a little faster?"
    judith "O-of course!"
    show anon e_b f_calm
    show judith e_ssw s_24
    pause
    judith e_nw "Do you like it?"
    anon "Uh huh."
    anon e_sw f_horny "You're doing a great job."
    judith e_ssw f_happy of_blush @ -m_talk "( !!! )"
    pause
    judith e_nw f_shy "Do you want to see my breasts too?"
    label jud02_stall.merge2:
    anon "Yeah! I'd love to..."
    show judith a_top_up_01 e_w o_right -oa_lap -p_sit at pos.anon.grope
    anon d_hard e_w @ -m_talk "..."
    show judith a_top_up_02 c_casual_up_flat e_s of_blush
    anon e_sw "Wow..."
    judith a_top_up e_w s_400ms "Go ahead!"
    show anon e_w
    judith "Touch them... but please be gentle! They're really sensitive..."
    show anon a_none e_sw
    show judith a_anon_grope e_b f_sad s_800ms
    pause
    judith e_n f_nervous m_lip s_400ms @ -m_talk "Mmph!"
    pause
    show anon a_up e_w f_surprised
    judith a_top_up_04 e_b f_sad -m_lip "Fnaaagh!" with hpunch
    judith a_top_up_01 c_casual e_w f_shy "It's just too much. My body gets all fuzzy when you touch my nipples..."
    show anon a_bottom_up e_s f_worried
    show judith a_clasp
    pause
    anon a_pants_off_01 c_casual d_none e_w "I didn't mean to hurt you."
    show anon a_side
    judith "No, it's fine! It felt really good... I'm just sensitive..."
    anon a_pocket f_shy "Maybe we should stop..."
    judith "Yeah... Thanks for staying with me, I feel much better..."
    label jud02_stall.merge3:
    show anon f_shy
    judith "... And if you want, we could do this again, some time..."
    show judith f_happy
    anon f_calm "I'd like that!"
    judith "I'll see you later then."
    show anon o_right
    hide judith
    with dissolve
    pause
    show anon e_b f_happy m_teeth
    pause
    hide anon with dissolve
    return True


label jud02_stall.bail1:
    anon "I know, but you have to learn to deal with it..."
    judith e_nw @ -m_talk "..."
    show anon a_surprised f_surprised m_teeth
    judith p_sit_cry "{i}*Sobbing*{/i}"
    show anon a_tired e_w f_confused p_bend -m_teeth at pos(.7, 1.)
    anon "I'm sorry..."
    judith "I just want to be alone right now."
    anon @ -m_talk "..."
    anon "I'll see you later, then..."
    hide anon with dissolve
    return


label jud02_stall.bail2:
    anon f_worried "We should really go... I don't want to be late and [saga.cast.annie] is already on my case..."
    show judith a_side e_ssw f_sad
    label jud02_stall.merge1:
    judith "Oh..."
    judith "You go then. I'll stay here a little bit longer I think..."
    anon "Alright, I'll see you later then."
    show judith a_shy p_sit_legs
    hide anon with dissolve
    return


label jud02_stall.bail3:
    anon f_worried_surprised "I can't do that right now, [saga.cast.judith]..."
    show judith a_side
    anon a_uneasy f_worried "Also, we should really go..."
    anon "... I don't want to be late and [saga.cast.annie] could see us in here."
    show judith a_shy e_ssw f_sad p_sit_legs
    jump jud02_stall.merge1


label jud02_stall.bail4:
    anon f_worried "I think we should stop..."
    show anon a_bottom_up d_hard
    show judith a_side e_ssw -oa_lap
    pause
    show judith e_nw
    anon a_pants_off_01 c_casual d_none "We can't be late for class and [saga.cast.annie] could see us in here..."
    show anon a_pocket e_w
    show judith a_clasp e_w o_right -p_sit at pos.anon.grope
    judith "I understand. Thanks for staying with me..."
    jump jud02_stall.merge3


label jud02_stall.girls:
    scene school_girls at stage
    show anon f_worried o_right at left with dissolve
    anon @ -m_talk "( I can still hear sobbing. )"
    anon @ -m_talk "( There's definitely someone in here... )"
    hide anon with dissolve
    return


label jud02_stall.hall1w:
    scene school_hall1w at stage
    show anon a_pocket f_confused with dissolve
    anon @ -m_talk "Hmm..."
    anon e_nw f_pensive @ -m_talk "( I can hear something... )"
    anon e_w f_worried @ -m_talk "( Is that someone... sobbing? )"
    anon @ -m_talk "( I think it's coming from the girls' locker room... )"
    hide anon with dissolve
    return


label jud02_reset:
    return


label jud02_reset.block:
    scene school_girls at stage
    show anon f_worried o_right at left with dissolve
    anon @ -m_talk "( I don't think I ended up helping very much... )"
    anon @ -m_talk "( ... I should give her some time to herself for now. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
