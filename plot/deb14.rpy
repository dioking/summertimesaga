label deb14_intro:
    scene debbie_lobby at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( Man, it's wonderful being more intimate with [saga.cast.debbie] when we go on our shopping trips... )"
    anon @ -m_talk "( ... But it sucks that we have to be so secretive about it. )"
    anon @ -m_talk "( I wish things were different. )"
    anon @ -m_talk "( That we could be more... have more... {i}do{/i} more! )"
    anon f_surprised @ -m_talk "( ... )"
    anon @ -m_talk "( Arg, being around her all the time but not being able to express how I feel is like torture... )"
    anon @ -m_talk "( ... I just need some kind of relief! )"
    anon f_shy @ -m_talk "( Maybe I should try jerking off to her again? )"
    anon @ -m_talk "( I know, promises were made, but I have to do something or I'll drive myself insane! )"
    anon @ -m_talk "( Maybe if I do it quickly and quietly, I can snag a pair of her panties and bust a nut without her noticing. )"
    anon @ -m_talk "( I think it's worth a shot... )"
    anon @ -m_talk "( Y-you know, just for the quick release... To clear my head! )"
    pause
    anon @ -m_talk "( Yeah, I'm sure [saga.cast.debbie] would understand. )"
    hide anon with dissolve
    return


label deb14_pants(busy):
    scene debbie_drawer_side
    show anon a_debbie_pants_up e_sw f_horny_smug at pos.debbie_drawer_side
    with fade
    anon @ -m_talk "( ... Mmm, I can't resist. )"
    anon a_debbie_pants_smell e_b f_happy m_laugh @ -m_talk "{i}*SNIIIIIIIIIIIIIIIIIIIIFFF*{/i}"
    anon d_hard e_nne_nnw f_elated -m_laugh @ -m_talk "( Ahh... That's the stuff... )"
    pause
    anon a_debbie_pants_up e_sw f_horny_smug @ -m_talk "( I'm sure one more time won't hurt. )"
    show anon a_surprised p_stand_away at pos(.35, 1.), blur(5), zoom(1.15)
    show debbie_drawer_side drawer as drawer
    with dissolve
    pause
    show anon o_right at pos(.3), blur(22.5), zoom(.70)
    pause
    show anon a_tired f_confused p_bend at pos(.45, 1.125), rotate(10), blur(25), zoom(.65)
    pause
    show anon e_nw o_left p_sit_edge_lay at pos(.635, 1.225), rotate(-15), blur(20), zoom(.75)
    pause

    scene debbie_bed1_visit
    show anon a_pants_hold e_se p_debbie_bed1_visit
    with fade
    pause
    anon a_pants_smell @ e_b -m_talk "{i}*SNIIIIIIIIIIIIIIIIIIIIFFF*{/i}"
    show anon a_undress c_casual_lewd
    pause
    anon a_jerk @ -m_talk "( These feel so soft against my skin. )"
    pause
    anon e_b @ -m_talk "( Oh, this is just what I needed. )"
    pause
    show anon s_4
    pause

    if busy:
        jump deb06_lotion.alt

    show debbie_bed1_visit -bed -door
    show debbie a_stop_side e_ow f_surprised behind anon at pos.debbie_bed1_visit_half
    show debbie_bed1_visit bed door half open as bed behind anon
    with dissolve.nowait
    debbie @ -m_talk "( !!! )"
    show debbie a_shock f_sad at pos.debbie_bed1_visit_open
    show debbie_bed1_visit -half as bed
    show anon p_debbie_bed1_visit_caught
    with none.nowait
    debbie "{i}Again?!{/i}" with hpunch
    anon "[saga.cast.debbie]?!"
    show debbie_bed1_visit door
    show debbie a_stop o_right p_stand_away at pos.debbie_bed1_visit_shut
    show debbie_bed1_visit -door -open as bed
    show anon c_casual e_nw f_worried_surprised ob_debbie_pants p_car_slide at pos(.565)
    with dissolve.nowait
    pause
    show debbie a_embarrassed e_sw f_surprised p_stand
    show anon ob_none p_car_faceplant at pos(.8, 1.35)
    with vpunch
    pause
    hide anon
    show debbie a_facepalm e_b f_sad
    with dissolve.nowait
    pause




    scene debbie_bed1 at stage(.7, .55, 2.25)
    show debbie a_facepalm e_b f_worried_surprised at right
    with fade
    debbie "Sweetie..."
    show anon a_behind_held e_s f_worried_surprised o_right at left with dissolve.nowait
    debbie a_gimme e_w f_sad oa_hand "... We talked about this!"
    show anon f_worried
    pause
    debbie a_clasp oa_none @ -m_talk "..."
    debbie "You promised you wouldn't do this in my room!"

    if _in_replay:
        jump deb14_pants.fast1




    menu:
        "I couldn't help it!":
            pass
        "I know, I'm sorry.":

            jump deb14_pants.fail1

    label deb14_pants.fast1 hide:
    anon e_w f_worried_surprised "I'm sorry, [saga.cast.debbie]..."
    show debbie a_surprised f_surprised
    anon a_cover_face e_b f_distressed o_left "... There's just all these feelings swirling around in my head and I-"
    show debbie e_wsw
    hide anon with dissolve

    scene debbie_bed1_bed_edge
    show anon a_head_hand o_right p_sit_edge_bow at pos(.3)
    with fade
    pause
    show debbie a_clasp e_sw f_sad behind anon at pos(.7, .84) with dissolve.nowait
    debbie "I know, sweetie... but this just isn't right, you doing {i}that{/i} in my bed... with my underwear!"
    debbie "We need to find you some other outlet for releasing your... umm, {i}energy{/i}."
    show debbie e_wsw
    anon a_down f_confused p_sit_edge @ e_wnw "Like what?"
    show debbie a_rub_leg e_sw o_right p_sit_edge_bend at pos.anon.shoulder_touch
    debbie "Oh, I don't know, sweetie..."
    debbie e_e f_shy "... Maybe try pornography."
    debbie "That stuff is all over the internet nowadays, you know?"
    anon f_shy "Y-yeah, I know."
    anon "I've tried it before, but..."
    anon e_osw f_sad_happy "... it's just so impersonal, you know?"
    debbie @ f_calm "Most boys like that."
    anon e_w f_worried "Well, I don't."
    anon a_shy_neck e_sse f_shy of_blush "I like to feel a connection."
    pause
    debbie e_sw @ -m_talk "Hmm."
    debbie "Well in that case..."
    show anon a_down e_w f_surprised of_none
    debbie e_e f_curious "... Have you thought about finding yourself a nice girlfriend?"
    debbie "Maybe someone from school?"

    if False:
        debbie f_shy "I know there's a few candidates at least."

    if _in_replay:
        jump deb14_pants.fast2

    menu:
        "I'm trying.":
            jump deb14_pants.fail2
        "They're not you.":

            pass
        "Not really.":

            jump deb14_pants.fail3

    label deb14_pants.fast2 hide:
    show debbie f_worried_surprised
    anon "They don't even compare to you, [saga.cast.debbie]."
    debbie e_sw f_sad "{i}*Sigh*{/i}"
    show anon f_worried
    pause
    debbie "Sweetie, I don't think you understand what you're saying."
    anon "No, that's the thing, I do..."
    show debbie e_e
    anon f_shy "... [saga.cast.debbie], you're all I think about!"
    pause
    show debbie f_surprised
    anon a_uneasy e_sse "These feelings and desires, they just keep building up inside of me..."
    anon "... Things I've never felt for anyone before."
    debbie e_sw of_blush @ -m_talk "..."
    debbie f_shy "I-"
    debbie "I don't know what to say, sweetie."
    pause
    show anon a_down e_w f_confused
    debbie f_sad "{i}*Sigh*{/i} This is all my fault..."
    show anon f_worried
    debbie "... the kissing and the-"
    show anon f_confused
    debbie f_surprised of_none "Oh god, that thing I did in the car."
    show anon e_sw f_worried_surprised
    debbie a_head_hands p_sit_edge_bow @ -m_talk "I'm a terrible landlady."
    anon a_touch_shoulder "No you're not."
    anon f_shy "You're a wonderful landlady..."
    anon @ f_happy "... The best!"
    pause
    anon a_down e_s f_worried "I'm the one who's fucked up in the head."
    debbie a_worried e_e p_sit_edge "Sweetie, language!"
    show debbie f_sceptical
    anon e_w f_confused "Well, it's the truth, isn't it?"
    show debbie f_surprised
    anon f_worried "I know it's wrong but I don't care..."
    anon f_shy "... I just want to be with you."
    debbie e_sw f_shy @ -m_talk "..."
    anon e_s "Maybe I'm just broken or something?"
    debbie e_e f_surprised "No, Sweetie... don't say that."
    show anon e_w
    debbie f_shy "You're just confused, that's all."
    pause
    show anon f_confused
    debbie e_sw "{i}*Sigh*{/i}"
    show anon e_wnw
    show debbie a_clasp e_wsw o_left p_stand at pos.anon.strip
    debbie "I think maybe you just need to get this out of your system?"
    anon "What do you mean?"
    debbie "I'm going to try something and maybe it will help..."
    show anon f_surprised
    debbie "... but only this {i}one{/i} time."
    debbie f_sad "And you have to promise me that you'll make an effort to talk with girls at school, alright?"
    anon f_confused "What are you gonna do?"

    call shot.debbie_bed1_strip
    show anon p_debbie_bed1_strip
    show debbie a_open_01 e_s f_shy p_debbie_bed1_strip
    with fade
    pause
    show debbie a_open_03 c_naked e_sw ob_pants
    pause
    show debbie a_open_04
    show anon f_surprised
    with dissolve.nowait
    anon @ -m_talk "( !!! )" with hpunch
    debbie of_blush "Go ahead and finish what you started, sweetie..."
    debbie "... I want you to jerk this out of your system."
    anon f_confused "Really, you want me to-"
    debbie e_e "Yes."
    pause
    debbie "It's okay, just this once!"
    anon f_horny "Oh, this is awesome!"

    scene debbie_bed1_bed_edge
    show anon a_down e_wsw f_happy o_right p_sit_edge at pos(.3)
    show debbie a_open_04 c_pants e_e f_shy of_blush at pos.anon.strip
    with fade
    pause
    show anon a_bottom_off_01 e_s f_shy
    pause
    show anon a_bottom_off_02 c_casual_top d_rise e_ssw f_surprised p_sit_edge_back
    pause
    anon a_down e_wsw f_shy ob_shorts_down "Oh, [saga.cast.debbie]..."
    show anon a_jerk d_none f_horny
    pause
    anon @ e_wnw f_shy "... You're so beautiful!"
    show anon s_3
    debbie "Ngh, that's nice of you to say."
    pause

    call shot.debbie_bed1_strip
    show anon p_debbie_bed1_strip
    show debbie a_open_04 c_naked e_e f_shy ob_pants of_blush p_debbie_bed1_strip
    with fade
    anon "No, I mean it!"
    anon "You have the best body in the entire world!"
    debbie e_owsw f_curious of_none "I think you're exaggerating a bit, sweetie."
    show debbie e_ossw f_surprised
    pause
    show debbie e_e f_shy of_blush
    anon "N-no, I'm not!"

    scene debbie_bed1_bed_edge
    show anon a_jerk c_casual_top e_wsw f_horny o_right ob_shorts_down p_sit_edge_back at pos(.3)
    show debbie a_open_04 c_pants e_e f_shy of_blush at pos.anon.strip
    with fade
    anon "That girl at the mall was right when she brought up your curves..."
    anon "... They're perfect!"
    debbie e_wsw of_none "Sweetie..."
    show anon a_jerk_02 e_wnw f_confused
    debbie "... You're embarrassing me!"
    anon f_shy "Sorry."
    debbie e_sw f_surprised @ -m_talk "( !!! )"
    show anon e_ssw f_confused
    show debbie e_e f_shy m_lip of_blush
    pause
    show anon e_wnw
    debbie -m_lip "Are you getting close?"
    anon f_shy "Yeah, kinda."
    show anon a_jerk e_wsw f_horny
    pause
    anon "Your boobs are incredible..."
    anon "... I love them so much!"
    debbie e_sw f_sad "Y-yeah, I can see that."
    debbie @ -m_talk "{i}*Gulp*{/i}"
    debbie "It looks really... angry."
    anon a_jerk_02 e_wnw f_confused "Angry?"
    anon "Is that bad?"
    debbie f_shy "N-no, not at all..."
    pause
    show anon a_jerk e_wsw f_shy s_4
    pause
    show anon f_horny
    debbie "It's just-"
    show anon s_5
    pause
    debbie e_wsw f_curious "You really get this worked up... over me?"
    anon s_6 "Hell yes!"
    show anon a_jerk_02 e_wnw f_surprised
    debbie f_sad "Sweetie, language."
    anon f_shy "R-right, sorry."

    call shot.debbie_bed1_strip
    show anon p_debbie_bed1_strip
    show debbie a_open_04 c_naked e_ossw f_shy ob_pants p_debbie_bed1_strip
    with fade
    anon "Does it bother you, watching me?"
    debbie e_owsw f_curious @ -m_talk "Hmm?"
    debbie f_shy "N-no, sweetie... I don't mind."
    debbie e_ossw "In fact, it's kinda..."
    debbie "... kinda...."

    scene debbie_bed1_bed_edge
    show anon a_jerk c_casual_top e_wsw f_horny o_right ob_shorts_down p_sit_edge_back s_8 at pos(.3)
    show debbie a_open_04 c_pants e_sw f_shy behind anon at pos.anon.strip
    with fade
    anon "Oh, [saga.cast.debbie]... I-"
    show debbie e_wsw f_curious
    anon e_b f_distressed @ -m_talk "HMMMM!"
    show debbie e_s f_surprised m_talk
    anon ob_cumshot p_sit_edge_back_cum s_400ms "HNNGGG!!!" with flash
    debbie -m_talk "{i}*Gasp*{/i}"
    show debbie ob_cum
    anon a_down d_firm e_osw f_sad_happy ob_shorts_down od_cum p_sit_edge_back "Haah, haah."
    show anon e_wnw f_shy
    debbie "Oh, my goodness..."
    debbie f_shy "... you really had a lot in there."
    anon e_wsw "Y-yeah, I did."
    anon f_calm "{i}*Sigh*{/i}"
    anon e_wnw f_shy "So much better."
    debbie e_wsw f_calm "Well, I'm... uhh, glad... you're feeling better."
    anon "Sorry about the mess."
    debbie f_sad "No, it's okay!"
    debbie e_s f_shy "It's actually kinda..."
    show debbie a_open_02 c_robe_open m_lip of_blush
    show anon a_bottom_off_02 e_sw
    pause
    show anon a_bottom_off_01 c_casual d_none e_s ob_none od_none p_sit_edge
    show debbie a_open_01 c_robe
    pause
    show anon a_down e_wnw f_calm
    debbie a_side e_wsw -m_lip "Err, I mean... it's nothing a quick shower won't fix."
    show anon f_happy
    pause
    debbie a_gimme oa_hand "C'mere."
    show debbie e_w
    show anon a_surprised e_w p_stand at pos(.375, .84)
    pause
    hide anon
    show debbie b_anon e_b p_hug
    anon "Thanks for helping me, [saga.cast.debbie]."
    debbie "You're welcome, sweetie."
    pause
    show anon f_shy o_right at pos(.375, .84)
    debbie a_nervous e_w oa_none p_stand -b_anon "I'm going to jump in the shower, you should get yourself cleaned up too."
    anon "Okay."
    show anon a_wave
    hide debbie with dissolve.nowait
    pause
    return True


label deb14_pants.bed1:
    scene debbie_bed1_visit anon
    anon "( Alright, coast is clear! )"
    anon "( Now I just need to grab a pair of her panties before getting into her bed. )"
    anon "( Oh, sweet release... here I come! )"
    return


label deb14_pants.fail1:
    anon "I'm sorry, [saga.cast.debbie]..."
    anon a_uneasy e_w "... I don't know what came over me!"
    anon "It won't happen again, I promise!"
    show anon a_respect p_bow
    debbie e_wsw "Oh, sweetie."
    debbie "Just please, try and do it elsewhere from now on."
    show anon a_side p_stand
    debbie e_w f_sceptical "Can you do that for me?"
    anon a_salute "Yes, ma'am."
    hide anon with dissolve
    return


label deb14_pants.fail2:
    anon f_worried "Girls my age are... I dunno, difficult."
    debbie f_sad @ -m_talk "..."
    debbie f_sceptical "Have you tried talking with them?"
    anon f_confused "Kinda."
    anon e_s f_worried "I just get tongue tied and make a mess of things."
    debbie "Well, you have to keep trying, sweetie!"
    anon e_osw f_sad "{i}*Sigh*{/i} I will, [saga.cast.debbie]."
    label deb14_pants.merge:
    debbie f_shy "That's my boy!"
    pause
    show anon e_w f_confused
    debbie "Come on."
    show anon e_wnw f_surprised
    show debbie a_hips e_wsw o_left p_stand at pos(.7, .84) with dissolve.nowait
    debbie "Time you get cleaned up."
    show anon a_surprised e_s
    pause
    show anon f_disgusted
    debbie "We {i}will{/i} get through this."
    show anon a_side e_w f_worried p_stand at pos(.375, .84)
    show debbie e_w
    anon "Yes, ma'am."
    hide anon
    show debbie o_right
    with dissolve.nowait
    pause
    show debbie a_facepalm e_b f_sad
    pause
    return


label deb14_pants.fail3:
    anon f_worried "I dunno, not really."
    anon @ f_confused "It's difficult out there, ya know?"
    show debbie f_sad
    anon e_osw f_sad "And with losing dad... and all this school work piled up..."
    anon "... Finding the right one seems almost impossible."
    debbie e_sw "I know, sweetie."
    anon @ -m_talk "..."
    debbie @ -m_talk "..."
    pause
    show debbie f_calm
    pause
    debbie e_e f_shy "How about that neighbor girl?"
    show anon e_w f_confused
    debbie f_curious "What's her name again?"
    anon "[saga.cast.mia]?"
    debbie f_calm "Yeah!"
    debbie "What about [saga.cast.mia]?"
    debbie f_happy "She's adorable!"
    anon a_uneasy f_shy "Yeah, I guess."
    debbie f_shy "Well, you have to make an effort, sweetie!"
    anon "I'll try, [saga.cast.debbie]."
    show anon a_down
    jump deb14_pants.merge


label deb14_pants.late:
    jump deb06_pants.late


label deb14_reset1:
    return


label deb14_reset1.pants:
    jump deb06_reset.pants


label deb14_reject:
    return


label deb14_reject.block:
    call shot.debbie_bed1_door
    show anon a_facepalm e_sw f_worried with dissolve
    anon @ -m_talk "( That was so embarrassing! )"
    anon f_disgusted @ -m_talk "( Ugh, what's wrong with me? )"
    hide anon with dissolve
    return


label deb14_reset2:
    return


label deb14_reset2.pants:
    scene debbie_drawer
    anon "( Haven't I embarrassed myself enough for the time being? )"
    anon "( Let's show some restraint for at least a couple days, huh? )"
    return


label deb14_outro:
    return


label deb14_outro.bath1:
    call shot.debbie_bath_door
    show anon a_think e_nw f_pensive o_right at left with dissolve
    anon @ -m_talk "( [saga.cast.debbie] seemed surprisingly agreeable with everything that went on down there... )"
    anon @ -m_talk "( ... But maybe a quick look in on her wouldn't be the worst idea. )"
    anon e_b f_happy m_teeth @ -m_talk "( Just to be certain she's okay. )"
    hide anon with dissolve

    call shot.debbie_bath_peek
    show layer master at blur(20)
    show debbie a_rub c_naked_wet p_shower_play s_400ms behind glass
    with fade
    anon "( Hmm, it's so steamy... )"
    anon "( I can't quite make out- )"
    show layer master
    with dissolve.nowait
    anon "( !!! )"
    pause
    anon "( S-she's masturbating... )"
    anon "( ... Because of- )"
    pause
    anon "( Welp, I'd say she seems more than okay with it! )"
    anon "( Best leave before she notices me peeping. )"
    anon "( Definitely don't wanna screw this up. )"
    return


label deb14_outro.bath2:
    call shot.debbie_bath_peek
    show layer master at blur(20)
    show debbie a_rub c_naked_wet p_shower_play s_400ms behind glass
    pause
    show layer master
    with dissolve.nowait
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
