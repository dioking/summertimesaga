label jen20_lobby:
    scene debbie_lobby at stage
    show anon a_think e_nw f_pensive at right with dissolve
    anon @ -m_talk "( Hmm? )"
    anon @ -m_talk "( Why is the TV on? )"
    pause
    anon @ -m_talk "( Did someone forget to turn it off? )"
    anon @ -m_talk "( I should check it out. )"
    hide anon with dissolve
    return


label jen20_lounge:
    scene debbie_lounge at stage(.455, .625, 3, b=0)
    anon "( Is that [saga.cast.jenny]?! )"
    anon "( What on earth is she watching? )"
    return


label jen20_lounge.rails:
    scene camera at stage
    show anon at right with dissolve
    anon @ -m_talk "( I'll just check the TV first. )"
    anon @ -m_talk "( Someone probably just left it on by mistake. )"
    hide anon with dissolve
    return


label jen20_jenny:
    call shot.debbie_lounge_side
    show jenny p_couch_side_play s_5
    show anon a_pocket o_right behind couch at pos.couch_side_behind_far, blur(7.5), tint('00106545') with dissolve
    pause
    show anon e_s f_surprised at pos.couch_side_behind_right, blur(None), tint(None)
    with dissolve.nowait
    anon @ -m_talk "( !!! )"
    anon e_sse @ -m_talk "( She's masturbating in the living room! )"
    anon e_w @ -m_talk "( While watching... )"

    scene debbie_tv
    show tv foot onlayer aux
    with fade
    anon "( ... A woman jerking some guy off with her feet?! )"
    pause
    scene onlayer aux
    with hold.aux

    call shot.debbie_lounge_side
    show anon a_reach e_se f_confused p_bend behind couch at pos.couch_side_behind_right
    show jenny p_couch_side_play s_5
    with fade
    pause
    show anon e_sse f_surprised p_couch_side_peek at default
    anon @ -m_talk "( This is awesome! )"
    pause
    anon e_wnw f_confused @ -m_talk "( I wonder if this just happened to be on or if she's really into... )"
    anon "... Feet?"
    show anon a_shock e_s f_surprised m_teeth o_right p_stand_shock at pos.couch_side_behind_right
    jenny c_casual_top p_couch_side_pants_on "!!!" with hpunch
    show anon a_surprised_up_both e_ssw p_stand -m_teeth
    jenny c_casual_pants e_wnw f_angry m_teeth p_couch_side_sit "What the fuck, [saga.cast.anon]?!"
    show anon o_left p_couch_side_duck at default
    show jenny e_w
    with dissolve.nowait
    anon "I'm sorry, I-"
    jenny "Get out from behind there, idiot!"
    hide anon with dissolve.nowait
    jenny @ -m_talk "..."
    show anon d_hard e_s f_worried p_couch_side
    with dissolve.nowait
    pause
    anon e_e "I-"
    jenny "Are you just stalking me all over the house now?!"
    anon "Shh, you're gonna wake [saga.cast.debbie]!"
    jenny f_annoyed -m_teeth "Seriously, what do I have to do to get some alone time?!"
    jenny "It's really beginning to-"
    show jenny e_wsw f_surprised
    pause
    jenny e_w f_confused "Are you hard right now?"
    anon @ e_s "Uhh, yeah..."
    anon "You were masturbating and it was really hot and..."
    jenny f_annoyed @ e_r "Jesus."
    pause
    show jenny e_wsw
    pause
    show jenny f_horny
    pause
    jenny e_w "Let me see it."
    anon "Huh?"
    jenny "Show me!"
    anon "O-okay..."
    show jenny e_wsw
    show anon a_bottom_down_01 d_none e_s
    pause
    show anon a_bottom_down_02 with dissolve
    show anon a_side c_casual_down d_hard
    jenny "I've always wanted to try this..."
    show jenny a_up
    anon e_e "What are you-"
    show jenny a_rub s_2 z_b_ob
    show mimic jenny at pos.jenny
    anon d_none @ e_s f_surprised "Ahh!"
    jenny e_w f_annoyed @ -m_talk "Shhh!"
    jenny "Now you're the one who's going to wake up my mom!"
    show jenny e_wsw f_horny
    anon @ -m_talk "..."
    show anon e_s f_shy
    pause
    call jen20_jenny.dialogue1 (1)
    call jen20_jenny.dialogue1 (2)
    call jen20_jenny.dialogue1 (3)
    jump jen20_jenny.loop1


label jen20_jenny.cum:
    if saga.cast.jenny < 'footjob':
        show jenny f_surprised
    else:

        anon "Here it comes!"
        pause

    show jenny a_rub_03 e_sw oa_cumshot s_600ms
    anon @ e_b m_lip p_couch_side_tilt "HNNGGG!!!" with flash
    jenny e_b f_calm m_laugh @ -m_talk "Pfft, hahaha!"
    show anon a_cumshot_02
    hide mimic
    show jenny a_after_01 e_sw f_horny oa_none z_reset -m_laugh

    if saga.cast.jenny < 'footjob':
        jenny "I just made you cum with my feet!"
        show anon e_e
        jenny a_after "I'm like, a total sex goddess!!"
        anon "That was amazing!"
        jenny a_after_02 "I know, right?"
        jenny e_w "You're welcome, loser."
        show jenny e_e f_calm oa_cumshot p_couch_side_rise_turn
        anon f_worried "Where are you going?"
        jenny a_side e_w f_confused oa_none p_couch_side_sit "Umm, to wash my feet?"
        jenny a_after f_horny "Unless you wanna clean them with your tongue?"
    else:

        jenny "Sheesh, look at the mess you made of my pretty little feet!"
        show anon e_e
        jenny a_after e_w "You sure you don't wanna clean them up with your tongue?!"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon f_worried "Eugh, no way!"
        jenny a_after_01 e_b f_calm @ m_laugh "Hahaha!"
        jenny e_w f_horny "Aww, c'mon..."
        jenny "Lick my toes, [saga.cast.anon]!"
        anon "Forget it!"
        jenny e_b f_calm @ m_laugh "Hahaha!"
        jenny e_w f_horny "Fine."
    else:

        anon f_worried "Please, don't make me do that..."
        jenny a_after_01 e_b f_calm @ m_laugh "Hahaha!"
        jenny e_w f_horny "Don't ask stupid questions then."

    jenny "I'm going to go take a shower."
    jenny oa_cumshot p_couch_side_rise_turn "See ya, perv."
    hide jenny with dissolve.nowait
    pause
    anon e_s f_shy @ -m_talk "( Phew, that was awesome! )"
    anon e_n f_calm p_couch_side_tilt @ -m_talk "( I should turn this off and get to bed before [saga.cast.debbie] hears it. )"
    hide anon with dissolve
    return 'footjob'


label jen20_jenny.dialogue1(opt, rng=-1):
    if opt == 1:
        jenny @ e_w "Does it feel good?"
        anon "Yes."

    elif opt == 2:
        anon @ e_b m_lip p_couch_side_tilt "Hnngh!"
        anon "Holy crap!"

        if rng < .25:
            jenny @ e_w f_confused "Do you like when I clench my toes?"
            anon @ e_e "Y-yes."

    elif opt == 3:
        anon @ e_e "You're really good at this!"
        jenny @ e_b f_calm m_laugh "Hehehe!"

    pause
    return


label jen20_jenny.dialogue2(opt, rng=-1):
    if opt == 1:
        jenny "Ahh!"

    elif opt == 2:
        jenny "I love your dick so much!"
        jenny "Oh, god!!"

        if rng < .5:
            jenny "I love it, I love it, I LOVE IT!"

    elif opt == 3:
        jenny "FUUUCK, YES!"
        anon "Shh!!"

    elif opt == 4:
        jenny "C'mon, [saga.cast.anon]!"
        jenny "Fuck me harder!"

    elif opt == 5:
        anon "Stop pulling on me!"
        jenny "Oh, right there!"

    pause
    return


label jen20_jenny.inside:
    anon "I'm going to cum!"
    jenny "Me too!"
    anon "Let go of me!"
    jenny "NGGHHH!!!"
    anon "[saga.cast.jenny] I can't-"
    show jenny p_debbie_lounge_couch_missionary_cum s_400ms
    anon "HNNGGG!!!" with flash
    jenny "AHHHH!!!"
    show jenny p_debbie_lounge_couch_missionary_cum_01
    pause
    show jenny p_debbie_lounge_couch_missionary_pullout
    anon "Holy crap..."
    jenny "Haah... Haah..."

    call mini.womb (saga.cast.jenny)

    call shot.debbie_lounge_side
    show jenny c_casual_top e_ssw f_angry p_couch_side_cum
    show anon c_casual_top d_soft e_e f_worried od_cum p_couch_side
    with fade
    jenny "Oh my god, did you cum inside me?!"
    anon "I tried pulling out but you wouldn't let go of me!"
    jenny "Well, I was focused on cumming!"
    pause
    jenny "FUCK!"
    jenny "You are so dead if I get pregnant!"
    anon "M-me?!"
    anon "You're the one who held me there!"
    jenny "Shut up!"
    jenny c_casual_pants p_couch_side_pants_off "Grr, I'm getting in the shower!"
    show jenny p_couch_side_rise with dissolve
    hide jenny with dissolve
    jenny "Asshole..."
    anon "Oh, so it's all my fault, huh?!"
    pause
    anon @ -m_talk "( Aaaand she's gone. )"
    jump jen20_jenny.post


label jen20_jenny.loop1:
    menu(range=(2, 6, 2), screen='lewd', tag='jenny'):
        "Keep Going":
            pass
        "Cum":

            jump jen20_jenny.cum

        "Fuck" if saga.cast.jenny > 'visit':
            jump jen20_jenny.switch

    $ renpy.dynamic(pool=saga.lewd.pool(3, max=2))

    while pool:
        call jen20_jenny.dialogue1 (pool.pop(), rng=renpy.random.random()) from jen20_jenny.pool1

    jump jen20_jenny.loop1


label jen20_jenny.loop2:
    menu(screen='lewd', tag='jenny'):
        "Keep Going":
            pass
        "Cum Inside":

            jump jen20_jenny.inside
        "Cum Outside":

            jump jen20_jenny.outside

    $ renpy.dynamic(pool=saga.lewd.pool(4, max=2))

    while pool:
        call jen20_jenny.dialogue2 (pool.pop(), rng=renpy.random.random()) from jen20_jenny.pool2

    jump jen20_jenny.loop2


label jen20_jenny.outside:
    anon "I'm going to cum!"
    jenny "Me too!"
    jenny "NGGHHH!!!"
    show jenny p_debbie_lounge_couch_missionary_cumshot
    anon "HNNGGG!!!" with flash

    call shot.debbie_lounge_side
    show jenny c_casual_top e_ssw f_horny p_couch_side_cumshot
    show anon c_casual_top d_soft e_e f_worried p_couch_side
    with fade
    anon "Wow..."
    jenny "Haah... Haah..."
    anon "That was intense!"
    jenny "You came all over me!"
    anon "Would you rather I had cum inside of you?"
    jenny "No... but you could have-"
    pause
    jenny "{i}*Sigh*{/i} Never mind."
    jenny c_casual_pants p_couch_side_pants_off "I'm going to go take a shower."
    jenny e_w p_couch_side_rise_turn "Later, loser."
    hide jenny with dissolve
    anon "Yeah, see ya."
    jump jen20_jenny.post


label jen20_jenny.post:
    pause

    if saga.cast.jenny < 'couch.sex':
        anon e_s f_shy @ -m_talk "( I guess we're just fucking whenever now... )"
        anon @ -m_talk "( ... Awesome! )"

    hide anon with dissolve
    return 'sex'


label jen20_jenny.rails:
    scene debbie_lounge at stage
    show anon f_surprised at right with dissolve
    anon @ -m_talk "( Maybe I can get closer... )"
    anon a_think e_nw f_pensive @ -m_talk "( ... I mean, what's the worst that could happen? )"
    hide anon with dissolve
    return


label jen20_jenny.switch:
    show anon e_b m_lip p_couch_side_tilt
    pause

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jenny e_w "Are you getting close?"
        anon e_e p_couch_side -m_lip "Y-yes."
        show anon e_s f_worried
        show jenny a_rub_03
        pause
        anon e_e "What are you doing?!"
        jenny "I'm bored of this..."
        pause
        jenny "Let's fuck!"
        anon "Huh?!"
        jenny "You heard me."
        hide mimic
        show anon d_hard f_surprised
        show jenny p_couch_side_pants_off z_reset
        pause
        jenny a_side oa_pants_tease p_couch_side_sit "I want you inside me."
        anon f_worried "B-but, [saga.cast.debbie] is right in there!"
        jenny "So?"
        jenny "I can be quiet."
        anon f_shy "Yeah, right."
        jenny f_annoyed "C'mon, please?"
        anon f_surprised @ -m_talk "!!!"
        anon "Did you just say, please?"
        jenny e_r "... Maybe."
        show jenny e_w f_horny
        anon f_shy "Wow, you really do want it."
        jenny e_wsw @ -m_talk "Mmhmm!"
    else:

        jenny a_rub_03 e_w "Alright, I'm bored of this..."
        anon e_e p_couch_side -m_lip @ -m_talk "Hmm?"
        hide mimic
        show anon d_hard f_surprised
        show jenny p_couch_side_pants_off z_reset
        pause
        jenny a_side oa_pants_tease p_couch_side_sit "Get over here and fuck me."
        anon f_worried "What?!"
        jenny "You heard me."
        anon "B-but [saga.cast.debbie] is right next door!"
        jenny "I know, it's exciting! Isn't it?"
        anon "N-no?"
        jenny f_annoyed @ e_r "{i}*Sigh*{/i}"
        jenny "Yes, it is!"
        show jenny f_horny
        anon @ -m_talk "..."
        jenny "Don't be a pussy."
        jenny e_wsw "I want that big dick!"

    anon "Fine."
    show anon c_casual p_couch_side_pants_off
    show jenny e_sw
    pause
    show anon c_casual_top p_couch_side_jump
    jenny c_casual_top oa_none p_couch_side_surprise "Oh, fuuuuck!"

    scene debbie_lounge_couch_edge dark
    show jenny b_anon p_debbie_lounge_couch_missionary_anim s_8
    with fade
    anon "Shhh!"
    anon "[saga.cast.debbie] will freak out if she finds us!"
    jenny "I know!"
    jenny "It's just so deep, I can't-"
    pause
    call jen20_jenny.dialogue2 (1)
    call jen20_jenny.dialogue2 (2)
    call jen20_jenny.dialogue2 (3)
    call jen20_jenny.dialogue2 (4)
    jump jen20_jenny.loop2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
