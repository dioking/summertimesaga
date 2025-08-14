label jud_stall_ready:
    anon f_calm "Say, would you like to sneak into the girls' locker room for a little... you know?"
    judith f_surprised "... You really want to..."
    judith f_confused "... W-with me?"
    anon "I mean, yeah!"
    show judith f_happy
    anon "If that's okay?"
    judith "Oh, definitely!"
    judith "Let's go!"
    hide judith

    if saga.cast.anon in saga.sets.school_hall1w:
        show anon a_surprised o_left p_stand_away
    else:
        show anon a_surprised p_stand_away

    with dissolve.nowait
    anon "Aaand she's off! Hehe!"
    hide anon with dissolve
    return


label jud_stall_ready.busy:
    anon f_shy "You wanna fool around?"
    judith f_sad "N-no, I don't have time today."
    judith f_afraid "I'm sorry, [saga.cast.anon]... please don't be mad at me!"
    anon a_wave "No worries, [saga.cast.judith], another time."
    hide anon with dissolve
    return


label jud_stall_event:
    scene school_stall
    show judith a_shy e_nw f_shy p_sit_legs
    show anon a_wave e_sw f_shy behind judith at pos.stall with dissolve
    anon "Hey!"
    judith "Hey, [saga.cast.anon]."
    show anon a_side
    judith "Did anyone see you come in here?"
    anon @ e_e "I don't think so?"
    judith "Oh, good."
    show anon f_happy
    judith e_ssw "S-so... did you wanna... do more stuff?"

    if saga.cast.judith < 'kiss':
        anon a_think e_nw f_pensive @ -m_talk "Hmm..."
        show judith e_nw
        anon e_sw "Have you ever been kissed before?"
        show anon a_side f_happy
        judith "You mean, like f-from a boy?"
        anon "Well, yeah!"
        judith e_s @ f_nervous "N-no."
        anon f_horny "You wanna try it?"
        show anon a_surprised_up e_w f_surprised
        show judith a_clasp e_w f_happy o_right -p_sit_legs at pos.anon.grope
        judith "Y-yeah, okay."
        show anon f_happy
        pause
        hide anon
        show judith b_anon p_kiss
        pause
        show anon f_horny at pos.stall
        judith -b_anon -p_kiss "Magnificent muffins! That felt really nice!"
        anon "Heh, yeah... I thought so too."
        judith @ f_confused "C-can we do more?"
        anon e_sw "Sure."
        pause
        judith e_s f_confused @ -m_talk "..?"
    else:

        anon @ f_calm "What did you have in mind?"
        judith e_nw "Maybe... we could... try kissing some more?"
        anon "Sure!"
        show anon e_w
        show judith a_clasp e_w o_right -p_sit_legs at pos.anon.grope
        judith "C-cool."
        pause
        hide anon
        show judith b_anon p_kiss
        pause
        show anon f_horny at pos.stall
        show judith e_ssw -b_anon -p_kiss
        pause
        anon "So what's next in your illicit bathoom liason secret master plan of doom?"
        judith a_cover_boobs e_w f_surprised "What- I-"
        anon a_surrender f_shy "Calm down, [saga.cast.judith], I'm just teasing!"
        judith a_side @ -m_talk "..."
        show anon a_uneasy e_e f_nervous m_teeth
        judith f_shy @ -m_talk "..."
        show anon e_w f_shy -m_teeth

    judith a_top_up_01 e_w "D-do you maybe want to touch my breasts again?"
    anon a_uneasy e_w f_shy "Y-yes, please!"
    judith e_ssw f_happy of_blush @ -m_talk "..."
    show anon a_side e_sw f_horny
    show judith a_top_up_02 c_casual_up_flat e_s
    pause
    judith a_top_up e_w f_shy "D-do you like them?"
    anon e_w "Yeah, I do."
    show judith a_anon_grope_03 e_b f_sad
    show anon a_none e_sw behind judith
    anon "They're so big and mushy!"
    show judith a_anon_grope s_800ms
    pause
    judith e_n f_nervous m_lip s_400ms @ -m_talk "Mmph!"
    pause
    show anon a_up e_w f_shy
    judith a_top_up_04 e_b f_sad -m_lip "Haah!"
    show judith a_top_up_01 c_casual e_w f_shy
    pause
    show anon a_side e_sw
    show judith a_side e_s f_happy p_sit -o_right at center
    pause
    show judith a_touch_anon e_ssw
    pause
    judith e_nw f_shy "You want to try something else?"
    anon f_horny "Think you could do that thing with your hand again?"
    judith "Y-you want me to?"
    anon @ f_calm "Definitely."
    judith "Hehe, okay."
    show anon a_surprised e_s f_shy
    show judith a_anon_bottom_down_01 e_ssw p_sit_lean
    pause
    show judith a_anon_bottom_down_02 f_happy
    show anon c_casual_down
    pause
    show judith a_anon_bottom_down_03
    pause
    show anon a_side d_hard z_b_ob_f_of_a_oa
    show mimic anon at pos.anon
    judith a_surprised f_surprised "Holy honey buns!"
    judith f_happy "I'm never gonna get used to that."
    pause
    hide mimic
    judith a_rub_anon_04 oa_lap "It's so... firm..."
    show judith a_rub_anon s_16
    anon a_surprised "{i}*Gasp*{/i}"
    show anon f_horny
    judith e_nw f_shy "... And... hot."
    show anon a_side
    pause
    show anon e_sw
    judith e_ssw f_happy "I love how it feels in my hand..."
    pause
    show judith m_lip s_32
    anon e_b f_calm m_drink @ -m_talk "Fuuuu..."
    show judith e_nw
    pause
    anon "That feels sooo good, [saga.cast.judith]!"
    judith e_n f_nervous @ -m_talk "( !!! )"
    show judith e_ssw f_happy
    pause
    judith e_nw f_shy -m_lip "S-should I keep going?"
    anon e_sw f_horny -m_drink "Could you play with the shaft a bit more?"
    show anon e_s
    show judith a_surprised e_ssw
    show mimic anon at pos.anon
    pause
    show anon e_b f_happy
    show judith a_rub_anon p_sit s_24
    hide mimic
    judith e_nw "Like this?"
    anon @ f_smug "Yesss!"
    pause
    anon "Just like that!"
    show judith f_happy
    anon e_sw "I love this!"
    show anon e_b f_calm m_drink
    show judith e_ssw m_lip s_32
    pause
    anon e_sw f_horny -m_drink "I'm getting close!"
    show judith e_nw f_shy -m_lip
    anon "Are you ready?"
    judith "Y-yes, anything for y-"
    show judith a_cumshot_anon e_ssw f_surprised s_400ms
    anon a_surprised e_b f_distressed m_talk "HNNGGG!!!" with flash
    pause
    show judith a_surprised e_s f_shy ob_cum -oa_lap
    anon f_happy od_cum z_b_ob_f_of_a_oa_d_od -m_talk "Haah... Haah..."
    show anon a_side e_sw
    judith @ -m_talk "..."
    show anon f_worried
    judith a_side e_nw "Wow, that's a lot of cum!"
    anon "Sorry! I didn't mean to make a mess of your shirt."
    show judith a_reach e_w p_sit_lean behind anon
    judith "N-no, that's okay..."
    show anon f_confused
    judith a_scrub_01 e_s p_sit "... I had a lot of fun!"
    show judith a_scrub_02
    anon f_shy "Oh..."
    show anon a_bottom_up e_s
    show judith a_scrub_01
    pause
    show judith a_scrub_02
    anon a_pants_off_01 c_casual d_none e_sw f_calm -od_cum "... Well, glad you enjoyed it!"
    judith a_scrub_01 e_nw -ob_cum "M-maybe we could... you know, do this again sometime?"
    show judith a_scrub_02
    anon a_pocket f_happy "Yeah, I'd like that!"
    judith f_happy "C-cool."
    show judith e_s
    pause
    show judith a_side e_nw
    anon e_e f_calm "We should probably get out of here, ya know?"
    show anon e_w
    show judith a_clasp e_w f_shy o_right -p_sit at pos.anon.grope
    judith "Y-yeah, okay!"
    hide anon
    hide judith
    with dissolve
    return


label jud_stall_event.rails:
    scene camera at stage
    show anon e_b f_happy m_teeth with dissolve
    anon @ -m_talk "( It's adorable how excited [saga.cast.judith] can get... )"
    anon @ -m_talk "( ... Definitely shouldn't keep her waiting. To the bathroom! )"
    hide anon with dissolve
    return


label jud_stall_reset:
    anon f_shy "You wanna fool around some more?"
    judith f_sad "N-not right now..."
    judith e_ssw f_shy of_blush "... I had fun earlier though."
    show judith e_w
    anon @ e_b f_happy m_laugh "Hehe!"
    show judith f_happy
    anon a_wave f_calm "Me too, [saga.cast.judith], see you later."
    hide anon with dissolve
    judith a_cover_face @ -m_talk "!!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
