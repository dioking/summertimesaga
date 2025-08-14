label jen23_intro:
    scene debbie_bed3 at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( Hmm, I wonder if [saga.cast.tammy] is doing her morning yoga routine? )"
    anon a_side e_b f_happy m_teeth @ -m_talk "( I can usually see her through my telescope. )"
    hide anon with dissolve
    return


label jen23_scope:
    scene tammy_bed1_scope -curtains -wall
    show tammy_bed1_scope curtains wall as wall
    show anon_scope base

    if saga.cast.erik < 'june':
        show tammy_bed1_scope -ball
        show old_tammy scope 10 behind wall
        pause
        anon "( Hmm, she's just talking to [saga.cast.erik]. )"
        anon "( I guess there's not going to be a show today... )"
        pause
        show old_tammy scope 11 with dissolve.nowait
        anon "( Wait a minute, is she- )"
        show old_tammy scope 12
        anon "( !!! )" with hpunch
        anon "( He's going down on her! )"
        pause
        anon "( Way to go [saga.cast.erik]! )"
    else:

        show old_tammy scope 6 behind wall
        anon "( There she is... )"
        anon "( Whoa, she's completely naked! )"
        pause
        show old_tammy scope 7 with dissolve.nowait
        anon "( What is she- )"
        show old_tammy scope 8_9 slow
        anon "( !!! )" with hpunch
        anon "( Holy crap! )"
        pause
        anon "( Does she know I'm watching?! )"

    scene debbie_bed3_telescope -anon at blur(20)
    show debbie_bed3_telescope anon as scope
    with fade
    anon "Whoaaaa!"
    show debbie_bed3_telescope ajar at blur(0)
    show debbie_bed3_telescope as scope at blur(20)
    with dissolve
    pause
    show debbie_bed3_telescope open -ajar
    show jenny e_os f_snide p_debbie_bed3_telescope
    with dissolve
    pause

    scene debbie_bed3_telescope_floor
    show anon p_spy_away
    with fade
    pause
    show jenny e_sw f_horny p_spy_stand with dissolve
    pause
    jenny "Spying on the neighbor girl again?"
    show anon a_down d_hard e_nw f_surprised o_right p_sit_crossed at pos.scope
    anon @ -m_talk "!!!"
    anon f_worried "N-no, I'm not-"
    jenny "Yeah, right."
    jenny "Don't lie."
    jenny "What's she doing now?"
    show anon a_side p_sit_back at pos.scope_back
    show jenny e_wsw
    with dissolve
    show jenny p_spy_away
    anon e_w @ -m_talk "..."
    jenny "Holy shit!"

    scene tammy_bed1_scope -curtains -wall

    if saga.cast.erik < 'june':
        show tammy_bed1_scope -ball
        show old_tammy scope 12
    else:

        show old_tammy scope 8_9 slow

    show tammy_bed1_scope curtains wall as wall
    show anon_scope base
    with fade
    jenny "Isn't that your friend's landlady?"
    jenny "What's his name again?"
    anon "[saga.cast.erik]."
    jenny "Yeah, [saga.cast.erik]."
    pause

    if saga.cast.erik < 'june':
        jenny "Hah, she must be desperate if she's turning to that fat ass for some release!"
    else:
        jenny "Hah, what's she doing with that exercise ball?!"

    scene debbie_bed3_telescope_floor
    show anon d_hard f_worried o_right p_sit_back at pos.scope_back
    show jenny p_spy_away
    with fade

    if saga.cast.erik < 'june':
        anon "Hey, be nice!"
        anon "[saga.cast.erik] is a good guy."
        jenny a_down e_b m_laugh p_spy_away_turn @ -m_talk "Pfft, yeah whatever."
        show anon f_pouty
        jenny e_w -m_laugh "Nobody cares!"
        jenny p_spy_away "Well, she seems to be enjoying herself..."
        show jenny a_rub p_spy_lean_away s_4
        anon e_sw f_surprised @ -m_talk "( !!! )"
        jenny "I guess tubbo really knows what he's doing."
    else:

        anon "I don't-"
        jenny a_down e_sw f_surprised m_talk p_spy_away_turn "Wait a minute..."
        jenny e_w f_calm -m_talk "Does she know you're watching her?!"
        anon @ -m_talk "..."
        jenny e_b m_laugh @ -m_talk "No fucking way!"
        show jenny e_w -m_laugh
        anon @ -m_talk "..."
        jenny "You're fucking [saga.cast.tammy], [saga.cast.anon]?!"
        anon "Maybe..."
        anon f_shy "... Just a little."
        jenny p_spy_away "Hahahahaah!"
        pause
        jenny "I have to give it to you, [saga.cast.anon]."
        jenny "She's really good-looking for her age."
        anon "Y-yeah."
        jenny "I mean, she's nowhere near as hot as me, but still-"
        anon f_pouty @ -m_talk "..."
        show jenny a_rub p_spy_lean_away s_4
        anon e_sw f_surprised @ -m_talk "( !!! )"
        jenny "Damn, look at her go..."
        jenny "You think she's imagining your dick inside her, right now?"

    pause
    $ renpy.end_replay()
    label jen23_scope.cookie hide:
    anon e_w f_confused "So what, you're just going to start masturbating, right here in my room?"
    jenny p_spy_lean_away_turn "Hehe, why not?"
    jenny p_spy_lean_away "It's nothing you haven't seen before..."
    anon e_sw f_shy "Y-yeah, but-"
    pause
    show anon e_w f_worried
    jenny a_down p_spy_away_turn "Actually, you're right."
    jenny "Why masturbate when I could just as easily have you snack on my box?"
    anon f_worried_surprised "Huh?!"
    show anon f_surprised
    show jenny e_b p_spy_pants_off
    pause
    show anon e_nw
    show jenny c_casual_top e_wsw f_snide p_spy_stand

    if saga.cast.erik < 'june':
        jenny "I want what she's getting and you're going to give it to me."
    else:
        jenny "She's putting on a show for you and you're going to return the favor."

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon f_confused "Oh really?"
        jenny "Yup."
        anon f_calm "Maybe if you ask me nicely."
        jenny f_disgusted "Ugh, you're still hung up on that shit?!"
        show anon f_sceptical

        if renpy.random.random() < .5:
            anon "If you wanna go back to masturbating, suit yourself..."
        else:
            anon "I'm not your little whipping boy, [saga.cast.jenny]..."

        jenny f_annoyed "Grr, you are such a pain in the ass!"
        show jenny f_angry_pouty
        pause
        jenny f_annoyed "Fine."
        jenny @ e_r "[saga.cast.anon], would you please lick my pussy?"
        anon f_calm @ e_b f_happy m_laugh "Haha, sure!"
        pause
        jenny "Just, c'mon!"
        show anon e_o f_surprised
        hide jenny
        with dissolve.nowait
    else:

        anon f_confused "I am?"
        jenny "Yup."
        show anon f_worried
        jenny "C'mon, loser!"
        hide anon
        jenny b_anon p_spy_bend_away "I'm going to cum all over that idiot face of yours!"
        show jenny p_spy_throw

    pause

    label jen23_scope.reuse:
    scene debbie_bed3_side

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen23_scope.alt

    show anon p_car_faceplant at pos.bed3_faceplant

    if saga.cast.jenny > 'lickjob':
        show anon ob_sandals

    anon "Oof!" with vpunch
    show anon e_onw f_annoyed p_sit_edge_lay at pos(.7, 1.)

    if saga.cast.jenny < 'lickjob':
        anon "Damnit, [saga.cast.jenny]!"
    else:
        anon "Could you not do that?!"

    show anon e_nw
    show jenny c_casual_top e_wsw f_snide p_table_stand at pos(y=1.05), zoom(1.18)
    with dissolve.nowait

    if saga.cast.jenny < 'lickjob':
        jenny "Heh, nice landing."
        anon f_confused "Do you have to be so rough?"
        jenny "You like it."
    else:

        jenny "Heh, you like it."

    show jenny p_bed3_climb_away at pos.anon, zoom(1.)

    if saga.cast.jenny < 'lickjob':
        anon "W-wait a second."
    else:
        anon f_confused "Look- Hold on."

    show jenny p_bed3_stand_away

    if saga.cast.jenny < 'lickjob':
        anon e_n f_afraid "You're not gonna-"
    else:
        anon e_n f_afraid "Please, [saga.cast.jenny], at least-"

    scene debbie_bed3_cunni_sub
    show jenny b_anon c_casual_top p_debbie_bed3_lick_sub_stand
    with fade
    pause
    show jenny e_s p_debbie_bed3_lick_sub
    with none.nowait
    anon "!!!" with vpunch
    anon "Mrrphfffll!!"
    jenny "Stop struggling and stick your tongue out!"
    pause
    jenny p_debbie_bed3_lick_sub_anim s_12 "Yeah, there you go."
    jenny "Just like that."
    pause
    jenny "Mmm, that's it."
    jenny "Take it, you bitch!"
    anon "Urfs ma uhnny!"
    jenny "Shut up!"
    pause

    if saga.cast.jenny < 'lickjob':
        jenny "No actually, better idea!"
        jenny "Hum something."
        anon "Hrwaah?"
        jenny "Hum a song, dummy!"
        jenny "The vibration feels amazing!"
        anon "Eerrm?"
        pause
        anon "{i}♪ Errmyyoony orhz unnng eeewww iiiiiting. ♪{/i}"
        jenny s_16 "Oh, yeah... there we go!"
        anon "{i}♪ Ooh nunks errr, assst aahh iiiiitning. ♪{/i}"
        show jenny s_20
        pause
    else:

        jenny "Do that humming thing again!"
        anon "Urrgggnnn?"
        anon "Urrrmmm..."
        pause
        anon "{i}♪ Errmyyoony orhz unnng eeewww iiiiiting. ♪{/i}"
        jenny s_16 "Seriously, that song again?"
        anon "{i}♪ Ooh nunks errr, assst aahh iiiiitning. ♪{/i}"
        jenny s_20 "I think something is wrong with your brain."
        pause

    jenny "Ngh, fuck!"
    jenny "[saga.cast.anon]!!"
    pause
    anon "{i}♪ Innng aahh eeerr unnnnggh a iill eeeerrt iiiiitning. ♪{/i}"
    jenny s_24 "I can't believe this is actually working..."
    jenny "... I'm getting close!"
    pause
    jenny "Oh!"
    jenny s_28 "Oh, god!!"
    jenny "Oh, fuck... here it comes!!"
    anon "Erm aht umms?!"
    jenny s_32 "Oh, fuck!!"
    jenny "Open your mouth, dummy!"
    anon "Hurrmm!"
    jenny "Open, open, open!"
    anon "Ohhww!"
    jenny "Here it-"
    jenny p_debbie_bed3_lick_sub_cum s_400ms "NGGHHH!!!" with flash
    pause
    jenny "Fuck, fuck, FUUUUCK!!!"
    jenny p_debbie_bed3_lick_sub_fall "Ghuuuuuuuh!"

    scene debbie_bed3_side
    show jenny c_casual_top_up e_b of_blush p_bed3_coma
    show anon p_sit_edge_lay_flat at pos(.7)
    with fade
    pause
    jenny "Uwahhhhh..."
    pause
    anon e_o f_distressed p_sit_edge_lay @ of_wet "{i}*Gasp*{/i}"
    show anon a_wipe e_s f_surprised p_sit_edge_back
    jenny "Haah... Haah..."
    anon a_down e_wsw f_worried "Jesus Christ, [saga.cast.jenny]!"

    if saga.cast.jenny < 'lickjob':
        anon a_shy_neck p_sit_edge "You coulda killed me!"
    else:
        anon a_shy_neck p_sit_edge "You gotta quit doing that!"

    show anon f_grumpy
    jenny @ m_laugh "Hehehe!"

    if saga.cast.jenny < 'lickjob':
        jenny "You're such a baby."
        anon a_down "I am not!"
    else:

        jenny "You came to me, remember?"
        anon a_down "Yeah, but-"

    jenny "Haah...{w} Just shut up...{w} and lemme...{w} enjoy this...{w} for a second."
    anon e_e f_pouty "... Psh, whatever."
    pause
    $ renpy.end_replay()

    scene black
    with dissolve
    ""

    call shot.debbie_bed3_bedside
    show jenny a_hips c_casual_top of_blush at right
    show anon a_fold f_grumpy o_right at pos(.45)
    with dissolve

    if saga.cast.jenny < 'lickjob':
        jenny "Man, your face is extremely fuckable!"
        anon "Gee, thanks."
        jenny "Seriously, that was awesome, [saga.cast.anon]!"
    else:

        jenny "Excellent job, as per y'ush."
        anon "Gee, thanks."
        jenny "No, for reals... that was really good!"

    label jen23_scope.merge:
    anon "Yeah, for you."
    jenny e_b m_laugh @ -m_talk "Hahaha!"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        show anon f_surprised
    else:
        show anon a_side f_surprised

    jenny e_w -m_laugh "Don't worry, I'll take care of you later."
    show anon f_confused
    jenny f_snide "Maybe..."
    pause
    show anon f_worried
    jenny "... If you're a good boy."
    anon "C'mon, [saga.cast.jenny]..."
    jenny f_annoyed "No."
    jenny f_snide "Besides, don't you have some laundry to do?!"
    show jenny e_ssw p_pants_off_02
    anon f_grumpy @ e_sw -m_talk "..."
    jenny c_casual_pants e_w -p_pants_off_02 "Later, loser!"
    show anon -o_right
    hide jenny
    with dissolve.nowait
    jenny "Hahahaah!"
    anon f_pouty "{i}*Sigh*{/i}"
    hide anon with dissolve
    return 'lickjob'


label jen23_scope.alt:
    if saga.cast.jenny < 'lickjob':
        show jenny c_casual_top e_c f_snide p_bed3_sit_shut
        with fade
        jenny "Hehe, remember that cum you shot all over my comforter?!"
        jenny p_bed3_sit_open "It's payback time, bitch!"
        anon "Hey, I washed it for you!"
        jenny @ e_b f_calm m_laugh "Hahaha!"
    else:

        with fade
        show jenny c_casual_top e_c f_annoyed p_bed3_sit_open with dissolve
        jenny "Just... c'mon, already!"

    show jenny e_sw
    show anon a_reach f_confused p_bend at pos(.7, 1.1), zoom(1.05)
    with dissolve.nowait
    pause

    if saga.cast.jenny < 'lickjob':
        show jenny f_confused_snide

    show anon e_nw f_annoyed
    jenny "Well, what are you waiting for, an invitation?!"
    show anon a_finger e_w f_confused
    jenny a_beckon f_horny "Lick my puss-"

    scene debbie_bed3_cunni
    show jenny b_anon c_casual_top p_debbie_bed3_lick_anim s_8
    jenny "EEyyyy!!!" with hpunch
    pause
    jenny "Fuuuuuck!"
    pause
    jenny "Mmm, your tongue feels amazing!"
    jenny "Ahh!"
    pause
    show anon a_butt oa_butt p_debbie_bed3_lick
    jenny a_up e_os f_snide oa_legs p_debbie_bed3_lick -b_anon "Focus on my clit more, dummy!"
    jenny "... And play with my tits too!"
    anon "Ask nicely or I'm stopping..."
    show anon a_none -oa_butt
    jenny e_ose f_worried_surprised p_debbie_bed3_lick_lift "What?!"
    jenny f_nervous_sad "Oh my god, you can't stop now!"
    anon "Watch me."
    jenny f_annoyed "No, no, no!"
    jenny f_angry m_teeth @ -m_talk "Grr!"
    pause
    jenny e_nw f_angry_pouty -m_teeth @ -m_talk "..."
    pause
    jenny e_ose f_annoyed "Urgh!"
    show jenny e_os f_shy p_debbie_bed3_lick
    pause
    jenny "Please, play with my tits, [saga.cast.anon]..."
    pause
    show anon a_jenny_top_up_01 oa_butt
    with dissolve
    show jenny c_casual_top_flat
    show anon a_jenny_top_up_02
    with dissolve
    show anon a_jenny_top_up_03
    with dissolve
    show anon a_none
    show jenny c_casual_top_up
    with dissolve
    hide anon
    hide mimic
    show jenny b_anon p_debbie_bed3_lick_anim
    with dissolve.nowait
    pause
    jump jen23_scope.loop


label jen23_scope.cum:
    jenny "I'm gonna-"
    jenny s_16 "Oh fuck!"
    pause
    jenny p_debbie_bed3_lick_cum s_400ms "NGGHHH!!!" with flash
    show anon a_butt oa_butt p_debbie_bed3_lick
    jenny ob_wet of_blush p_debbie_bed3_lick -b_anon "Haah... Haah..."
    anon "Sheesh, you soaked me."
    jenny f_snide "Psh, you like it!"
    anon "Yeah, right..."
    jenny e_b f_calm m_laugh @ -m_talk "Hehehe!"

    scene debbie_bed3_side
    show jenny c_casual_top_up e_b of_blush p_bed3_coma
    show anon a_wipe_mouth e_wsw f_shy p_stoop at pos(.8), zoom(1.1)
    with fade
    pause
    show anon a_down p_sit_edge at pos(.825), zoom(1.)
    anon "You okay over there?"
    jenny "Haah... Yeah..."
    jenny "... I just need... haah..."
    jenny "... a minute."
    anon "Heh, by all means."
    $ renpy.end_replay()

    scene black
    with dissolve
    ""

    call shot.debbie_bed3_bedside
    show jenny a_hips c_casual_top of_blush at right
    show anon a_pocket f_worried o_right at pos(.45)
    with dissolve
    anon "Better?"
    jenny "Phew, yeah... Alright, that was pretty good."
    jump jen23_scope.merge


label jen23_scope.dialogue(opt, rng=-1):
    if opt == 1:
        jenny "!!!"

    elif opt == 2:
        jenny "Right there!"

    elif opt == 3:
        jenny "Just like that."

        if rng < .5:
            jenny "Yesss!!"

    elif opt == 4:
        jenny "Mmm, I'm getting close!"

    pause
    return


label jen23_scope.loop:
    menu(screen='lewd', tag='jenny'):
        "Keep Going":
            pass
        "Finish":

            jump jen23_scope.cum

    $ renpy.dynamic(pool=saga.lewd.pool(4, max=2))

    while pool:
        call jen23_scope.dialogue (pool.pop(), rng=renpy.random.random()) from jen23_scope.pool

    jump jen23_scope.loop


label jen23_scope.rails:
    jump jen16_scope.rails
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
