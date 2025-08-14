label deb06_intro:
    scene debbie_bed3 at stage
    show anon a_uneasy f_horny o_right with dissolve
    anon @ -m_talk "( Mmm, I can't stop thinking about what happened with [saga.cast.debbie] in her bedroom... )"
    anon @ -m_talk "( ... I keep imagining her... writhing with pleasure under my touch... )"
    anon f_horny_smug @ -m_talk "( ... Those curvy thighs and her smooth, delicate skin. )"
    anon a_smell_finger e_b f_happy @ -m_talk "( Tsk, the smell of her lotion has almost faded and with it, I fear the memories might also. )"
    pause
    anon a_side e_sw f_tired @ -m_talk "( {i}*Sigh*{/i} I'm not ready to let go of these feelings just yet. )"
    pause
    anon a_think e_nw f_pensive o_left @ -m_talk "( Maybe I should get a little dab of it from her room? )"
    anon @ -m_talk "( You know, just to keep things from getting foggy. )"
    anon a_side e_w f_happy @ -m_talk "( I'm sure she wouldn't mind that, right? )"
    hide anon with dissolve
    return


label deb06_lotion(busy):
    scene debbie_drawer_side
    show anon a_lotion_look e_sw f_confused at pos.debbie_drawer_side
    anon @ -m_talk "( Brazilian Bum Bum... cream? )"
    anon @ -m_talk "( With salted caramel, vanilla, and hints of pistachio and jasmine. )"
    anon a_side f_horny @ -m_talk "Mmm."
    anon @ -m_talk "( The entire drawer smells of it! )"
    show anon p_debbie_drawer_bow at reset
    anon @ -m_talk "{i}*SNIIIIIIIIIIIIIIIIIIIIFFF*{/i}"

    scene debbie_bed1_bed_massage
    show debbie c_robe e_s m_lip p_sit_massage w_normal
    show anon a_massage_leg p_sit_massage
    show layer master at daydream
    with flash
    pause

    scene debbie_drawer_side
    show anon p_debbie_drawer_bow
    with fade
    anon "( Ahh, that's intoxicating! )"
    show anon a_wtf e_sse_ssw f_surprised of_debbie_pants p_stand at pos.debbie_drawer_side
    anon @ -m_talk "( !!! )"
    show anon a_debbie_pants_up e_sw of_none
    pause
    anon f_confused @ -m_talk "( Man, these don't look like {i}'mom panties'{/i} at all... )"
    anon f_horny @ -m_talk "( ... They're kinda sexy actually. )"
    show anon f_horny_smug
    pause
    anon a_debbie_pants_smell e_b f_happy m_laugh @ -m_talk "{i}*SNIIIIIIIIIIIIIIIIIIIIFFF*{/i}"

    scene debbie_bed1_bed_massage
    show debbie c_robe e_ownw f_shy p_sit_massage w_normal
    show anon a_massage_leg_02 p_sit_massage
    show layer master at stage(.475, .7, 3, b=0), daydream
    with flash
    pause
    hide anon
    show layer master at stage(.455, .42, 4.25, b=0), daydream
    with flash
    pause
    show debbie c_robe_lewd p_sit_massage_tilt
    show layer master at stage(.425, .305, 2, b=0), daydream
    with flash
    pause

    scene debbie_drawer_side
    show anon a_debbie_pants_smell d_hard e_nne_nnw f_elated at pos.debbie_drawer_side
    with fade
    anon @ -m_talk "( Oh, this is- )"
    anon e_b f_tired @ m_yawn "( I think, I- )"
    show anon a_facepalm e_nnw
    pause
    anon @ -m_talk "( I gotta lie down! )"
    show anon o_right p_climb_away_pipe at pos(.65, 1.275), blur(20), zoom(.85)
    pause
    show anon e_nw f_confused o_left p_sit_edge_lay at pos(.635, 1.225), rotate(-15), blur(20), zoom(.75)
    pause

    scene debbie_bed1_visit
    show anon a_tired e_b p_debbie_bed1_visit
    with fade
    anon @ -m_talk "( Oh, gee... my head is spinning... )"
    anon @ -m_talk "( ... What is happening to me? )"
    pause
    anon a_pants_hold e_se @ -m_talk "( I'm still holding them. )"
    anon @ -m_talk "( Hmm, I didn't realize [saga.cast.debbie] had sexy panties like this... )"
    anon a_pants_smell @ e_b -m_talk "( ... Ooh, this smell!! )"
    label deb06_lotion.merge:
    pause
    anon a_pants_smell @ e_b -m_talk "{i}*SNIIIIIIIIIIIIIIIIIIIIFFF*{/i}"
    pause
    anon @ -m_talk "Oh, [saga.cast.debbie]..."
    show anon a_undress c_casual_lewd
    pause
    show anon a_jerk
    pause
    show anon e_b
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
    debbie "Oh my god!!" with hpunch
    anon "[saga.cast.debbie]?!"
    debbie "What are you-"
    show debbie_bed1_visit door
    show debbie a_stop o_right p_stand_away at pos.debbie_bed1_visit_shut
    show debbie_bed1_visit -door -open as bed
    show anon c_casual e_nw f_afraid m_teeth ob_debbie_pants p_car_slide at pos(.565)
    with dissolve.nowait
    pause
    show debbie a_shock e_sw f_surprised p_stand
    show anon ob_none p_car_faceplant at pos(.8, 1.35)
    with vpunch
    pause
    hide anon with dissolve.nowait
    debbie e_w "I-"

    scene debbie_bed1 at stage(.7, .55, 2.25)
    show debbie a_shock f_worried_surprised at right
    with fade
    debbie "I umm... I'm sorry, I didn't mean to..."
    show anon a_behind_held e_s f_worried_surprised o_right at left with dissolve.nowait
    debbie f_sad "... I mean, I wasn't expecting-"
    debbie a_side "W-were those-"
    show anon e_ese f_worried of_blush
    show debbie f_worried_surprised
    pause
    debbie e_e "I should leave!"
    show debbie a_facepalm e_b f_sad o_right at pos(.9)
    anon a_up e_w f_worried_surprised "W-wait, it's not-"
    debbie a_side e_w o_left "No, it's fine... I don't..."
    debbie e_e "... just... excuse me."
    hide debbie with dissolve.nowait
    anon a_side e_osw f_sad of_none @ -m_talk "..."

    call shot.debbie_bed1_door
    with fade
    show debbie e_wsw f_surprised o_right with dissolve.nowait
    debbie @ -m_talk "( I can't believe what I just saw! )"
    debbie @ -m_talk "( Was he really just doing... {i}that{/i}?! )"
    debbie a_facepalm e_b f_sad @ -m_talk "( In my room?! )"
    debbie @ -m_talk "( Why would he be doing that in my room?! )"
    debbie a_clasp e_w o_left @ -m_talk "( Surely he can't be attracted to me, can he?! )"
    debbie @ -m_talk "..."
    debbie a_cover_face e_b f_worried_surprised o_right @ -m_talk "( Is this normal? )"
    debbie @ -m_talk "( I mean, he is a young man with hormones running rampant. )"
    debbie a_embarrassed f_shy @ -m_talk "( Yeah, that's gotta be it! )"
    debbie e_w @ -m_talk "( And with everything that's happened recently, the poor thing is probably just feeling confused. )"
    debbie a_clasp f_curious @ -m_talk "( Should I talk to him about it? )"
    debbie f_shy @ -m_talk "( I suppose, I should at least try and get an understanding of what's going through his head. )"

    scene debbie_bed1_bed_edge
    show anon a_head_hand o_right p_sit_edge_bow at pos(.45)
    with fade
    anon @ -m_talk "( Oh, crap. This is bad! )"
    anon @ -m_talk "( I'm {i}so{/i} screwed... )"
    anon @ -m_talk "( Why did I even {i}do{/i} this! )"
    anon a_uneasy e_osw f_sad p_sit_edge @ -m_talk "... Ugh..."
    anon @ -m_talk "( I'm so stupid... )"
    anon a_down @ -m_talk "( ... Things were going so well between us and now this might ruin everything! )"
    pause
    show anon a_side e_w f_worried p_stand at pos(.5, .84)
    anon @ -m_talk "( Time to face the music, I guess. )"
    hide anon with dissolve

    call shot.debbie_bed1_door
    show debbie a_mug f_shy at right
    with fade
    show anon a_surprised f_worried_surprised o_right at left with dissolve
    debbie "H-hey, sweetie."
    anon a_pocket e_ssw f_worried of_blush @ -m_talk "..."
    debbie "Listen, I just want you to know I'm not mad..."
    show anon e_w f_confused
    debbie "... Masturbation is perfectly normal and all boys your age do it."
    show anon f_worried_surprised
    debbie "I know you have been going through a lot recently; losing your dad and now you're stuck in a house with only girls..."
    anon a_facepalm e_osw f_sad @ -m_talk "..."
    debbie "... You've got to be stressed and I imagine you're experiencing a bunch of confusing feelings."
    anon a_side "Y-yeah, you could say that."
    debbie @ -m_talk "Mhmm."
    debbie "It's completely natural."
    debbie f_sad "But you shouldn't be doing {i}that{/i}... umm, in my room."
    debbie @ f_worried_surprised "And certainly not with my underwear!"
    anon e_w f_worried "I know, I'm sorry... I just-"
    debbie "You just what, sweetie?"
    anon a_shy_neck e_ese "I wanted to borrow some of your lotion and then I started feeling lightheaded... so I laid down..."
    anon "... I don't even remember picking up your... umm, ya know?"
    debbie f_curious "My panties?"
    anon a_side e_w "It just sorta, happened."
    debbie f_shy "It's alright, sweetie."
    show anon f_surprised
    debbie "We just need to find you a nice little girlfriend or something..."
    debbie f_curious "... Isn't there anyone at school you'd like to get closer with?"
    anon a_uneasy e_e f_shy "[saga.cast.debbie]... please stop, this is all really embarrassing!"
    debbie f_happy @ e_b m_laugh "I'm sorry, sweetie. I'm just trying to help..."
    show anon a_side e_w
    debbie f_shy "... And you don't need to be embarrassed.... Really, it's not a big deal."
    debbie "Everyone masturbates."
    debbie "I think you're just going through a rough time right now and maybe some wires got crossed, huh?"
    anon of_none "Y-yeah, maybe."
    debbie "I know you didn't mean any harm, you're such a wonderful kid."
    anon "I'm not a kid."
    debbie "You're right, I'm sorry... you aren't a kid."
    debbie "Just promise me you won't do that in my room any more, yeah?"
    anon "Y-yeah, I promise."
    show debbie b_anon e_sw f_calm p_hug_lean at center
    show anon e_nw f_worried p_debbie_hug_lean at center
    debbie "That's my good boy!"
    pause
    show debbie e_w p_stand -b_anon at pos(.65)
    show anon e_w f_shy p_stand at pos(.35)
    debbie "You want me to make you something to eat?"
    anon "N-no, that's okay..."
    anon "... Thanks though, for being so understanding about all this."
    debbie "Not a problem, sweetie."
    hide debbie with dissolve.nowait
    pause
    anon a_rub e_osw f_sad_happy @ -m_talk "( This could have gone so much worse. What the heck was I thinking? )"
    anon @ -m_talk "( I can't believe I did that. )"
    hide anon with dissolve
    return


label deb06_lotion.alt:
    anon s_6 @ -m_talk "( Oh, [saga.cast.debbie]! )"
    anon s_8 @ -m_talk "( Your legs are so- )"
    anon p_debbie_bed1_visit_cum s_1 @ -m_talk "HNNGGG!!!" with flash
    with dissolve.nowait
    show anon a_jerk_01
    with dissolve.nowait
    anon @ -m_talk "Haah... Haah..."
    show anon a_undress e_se ob_cum p_debbie_bed1_visit
    with dissolve.nowait
    anon @ -m_talk "( Hoo, boy... I needed that! )"

    scene debbie_bed1 at stage(.7, .52, 3) with fade
    show anon a_surprised_up e_sw f_surprised m_teeth o_right with dissolve
    anon @ -m_talk "( Eugh, how did I manage to get it on her pillow?! )"
    show anon a_surprised o_left
    pause
    show anon o_right
    pause
    anon a_think e_nw f_pensive -m_teeth @ -m_talk "( I guess I could just use it to wipe the rest up, flip it over, and hope she doesn't notice? )"
    pause
    show anon a_reach e_sw f_confused p_bend at pos(.6)
    anon @ -m_talk "( Sorry, [saga.cast.debbie]! )"
    hide anon with dissolve
    return


label deb06_lotion.bed1:
    call shot.debbie_bed1_door
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "Hmmm."

    if saga.time.dusk:
        anon @ -m_talk "( Even though I don't think she would mind my borrowing some of her lotion... )"
        anon @ -m_talk "( ... I also don't {i}really{/i} want to have to explain myself. )"
        pause
        anon a_pocket e_w f_calm o_right @ -m_talk "( Eh, I'll just come back during the day when [saga.cast.debbie] is more likely to be occupied. )"
    else:

        anon @ -m_talk "( \"Hi [saga.cast.debbie], it's only me. I'm just here to smell some of your lotion. Go back to sleep.\" )"
        anon a_side e_w f_pouty o_right @ -m_talk "( Yeah... nope. )"

    hide anon with dissolve
    return


label deb06_reset:
    scene debbie_bed3 at stage
    show anon a_think e_nw f_pensive o_right with dissolve
    anon @ -m_talk "( Urgh, I'm still thinking about that massage with [saga.cast.debbie]! )"
    anon a_pocket e_w f_shy @ -m_talk "( Maybe I should try masturbating with her panties again and see if that helps? )"
    hide anon with dissolve
    return


label deb06_reset.pants:
    scene debbie_drawer
    anon "( Nah, I shouldn't push my luck. )"
    anon "( It's a miracle I didn't get caught the last time! )"
    return


label deb06_pants(busy):
    scene debbie_drawer_side
    show anon a_debbie_pants_up e_sw f_pensive at pos.debbie_drawer_side
    with fade
    anon @ -m_talk "( Am I really doing this again? )"
    pause
    show anon f_horny_smug
    pause
    anon a_debbie_pants_smell e_b f_happy m_laugh @ -m_talk "{i}*SNIIIIIIIIIIIIIIIIIIIIFFF*{/i}"
    anon d_hard e_nne_nnw f_elated -m_laugh @ -m_talk "( Phew... Oh, yeah... )"
    anon a_side e_s f_horny_smug @ -m_talk "( ... I just can't help myself. )"
    show anon a_surprised p_stand_away at pos(.35, 1.), blur(5), zoom(1.15)
    show debbie_drawer_side drawer as drawer
    with dissolve
    pause
    show anon o_right at pos(.3), blur(22.5), zoom(.70)
    pause
    show anon a_tired e_sw f_confused p_bend at pos(.45, 1.125), rotate(10), blur(25), zoom(.65)
    pause
    show anon e_nw o_left p_sit_edge_lay at pos(.635, 1.225), rotate(-15), blur(20), zoom(.75)
    pause

    scene debbie_bed1_visit
    show anon a_pants_hold e_se p_debbie_bed1_visit
    with fade
    jump deb06_lotion.merge


label deb06_pants.late:
    call shot.debbie_bed1_drawer
    show anon a_debbie_pants_up e_sw f_worried
    anon @ -m_talk "( I really shouldn't do this now. )"
    anon @ -m_talk "( This late in the day, [saga.cast.debbie] will almost certainly catch me. )"
    show anon e_e
    pause
    anon e_sw @ -m_talk "( I'll just put these back. )"
    hide anon with dissolve
    return


label deb06_outro:
    return


label deb06_outro.block:
    call shot.debbie_bed1_door
    show anon a_pocket f_worried with dissolve
    anon @ -m_talk "( Nah, I think there's been quite enough embarrassment for the both of us today. )"
    anon @ -m_talk "( Let's just give her space, eh? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
