label jen24_intro:
    call shot.debbie_bed3_sleep
    with fade
    pause
    show debbie_bed3_visit -bed -computer -door
    show jenny e_ose f_snide p_bed3_peek q_tod behind anon
    show debbie_bed3_visit ajar bed computer door as computer behind anon
    with dissolve
    pause
    show debbie_bed3_visit door open
    show debbie_bed3_visit -ajar -door as computer
    jenny p_bed3_door "Psst, [saga.cast.anon]..."
    show anon p_bed3_stretch
    pause
    anon a_down e_w f_tired p_bed3_sit "Watsa-"
    anon f_tired_annoyed "Damn it, [saga.cast.jenny]..."
    jenny "Hehehehe!"
    anon "{i}*Sigh*{/i} You really gotta stop doing this."
    jenny "Aww, poor baby..."
    jenny "Hurry up, breakfast is ready."
    anon "So?"
    jenny "So trust me, you're going to need your strength today."
    anon f_sceptical "What does that mean?"
    jenny "It means, get up, loser!"
    anon @ -m_talk "..."
    hide jenny
    show debbie_bed3_visit ajar -open
    with dissolve.nowait
    jenny "C'mon, get your ass downstairs!"
    anon f_tired "Ugh!"

    scene debbie_bed3 at stage with fade
    show anon p_top_on with dissolve
    show anon f_tired -p_top_on
    pause
    anon "I guess I should get downstairs and see what she's going on about..."
    hide anon with dissolve
    return


label jen24_dining:
    call shot.debbie_dining_breakfast
    show debbie_dining_table food3 plate3 -bowl3 as table
    show jenny a_phone e_s f_annoyed p_table behind table
    pause
    show debbie_dining_table -chair3 -chair4 -table_legs
    show anon a_pocket e_wsw f_sceptical p_stand_far behind jenny at pos(.7)
    show debbie_dining_table chair3 chair4 table_legs as chairs behind jenny
    with dissolve.nowait
    jenny a_spoon e_wnw "About time..."
    show anon f_grumpy
    pause
    hide chairs
    show debbie_dining_table chair3 chair4 table_legs
    show anon a_down e_e p_table at center
    with dissolve.nowait
    anon "What is your problem?"
    jenny "We've got a big show today."
    anon f_confused "Big show?"
    jenny "That's right so eat up."
    show jenny e_s
    anon "What do you-"
    show anon e_w f_surprised
    debbie "Good morning, sweetheart!"
    show debbie_dining_table pull4
    show debbie a_mug e_wsw p_table_stand behind jenny
    with dissolve.nowait
    anon e_nw f_calm "Morning, [saga.cast.debbie]."
    show anon e_w
    show debbie_dining_table -pull4
    debbie e_w p_table "I hope you're hungry."
    show jenny e_r
    anon "Starving."
    show anon a_bowl e_s
    jenny e_w f_calm "[saga.cast.debbie], do you know where my uniform is?"
    show anon a_eat m_bite
    debbie "What uniform, dear?"
    show anon a_down v_chew -m_bite
    jenny "You know, from college..."
    show anon a_bowl v_normal
    debbie "You mean, your cheerleading costume?"
    show anon a_eat m_bite
    jenny f_annoyed "[saga.cast.debbie], it's a uniform!"
    show anon a_down v_chew -m_bite
    debbie "Okay, okay, uniform."
    show anon a_bowl v_normal
    debbie @ f_shy "Umm..."
    show anon a_eat m_bite
    debbie "It's probably stored away in the attic with the rest of our old clothes..."
    show anon a_down v_chew -m_bite
    jenny f_surprised "In the attic?!"
    show anon e_e f_surprised
    jenny f_angry m_teeth "Damn it, [saga.cast.debbie]!"
    show debbie f_surprised
    jenny "It's going to be covered in dust and cobwebs!"
    show anon e_w v_normal
    show jenny f_angry_pouty -m_teeth
    debbie f_sad "Well, I'm sorry dear..."
    debbie "I dunno-"
    pause
    show anon a_bowl e_s f_calm
    debbie f_shy "What do you need that old thing for anyways?"
    show anon a_eat m_bite
    debbie "It probably won't even fit you now."
    show anon a_down e_e f_surprised v_chew -m_bite
    jenny f_annoyed "Yeah, I know but my fans-"
    show jenny f_surprised
    pause
    jenny f_worried "Err... I mean, I-"
    show jenny e_wsw
    pause
    jenny e_w f_annoyed "{i}*Sigh*{/i} It's not important, just never mind."
    show anon e_w v_normal
    debbie f_calm "Would you like me to get it down and wash it for you?"
    show anon e_e
    jenny "Ugh, I said forget it, [saga.cast.debbie]!!"
    show debbie f_sad

    menu:
        "Remain Silent {color=7ff7}[[Submissive]{/color}":
            $ renpy.dynamic(what=+1)
            anon e_s f_worried @ -m_talk "..."
            show debbie_dining_table pull4
            debbie e_wsw p_table_stand "O-okay, dear."
            hide debbie
            with dissolve.nowait
            pause
            jenny "Why does nothing ever go right in this house?!"
            anon e_e "I don't know."
        "Say Something {color=f77b}[[Dominant]{/color}":

            $ renpy.dynamic(what=-1)
            anon f_grumpy "Hey, don't talk to [saga.cast.debbie] like that!"
            debbie f_surprised @ -m_talk "!!!"

            if saga.cast.jenny.dom <= saga.cast.jenny.sub:
                jump jen24_dining.alt

            jenny f_angry m_teeth "What did you say?!"
            show debbie f_sad
            anon "She's just trying to help!"
            pause
            jenny "Well, I didn't ask for her help, did I?!"
            anon f_worried "I wasn't-"
            anon f_surprised "I didn't mean to-"
            show anon m_teeth
            jenny "Mind your own business, loser!"
            anon e_s @ -m_talk "..."
            show anon e_nw -m_teeth
            show debbie_dining_table pull4
            debbie e_wsw p_table_stand "Would you two please not fight at the breakfast table?!"
            show anon e_w f_worried
            hide debbie
            with dissolve.nowait
            debbie "I just don't understand where she gets that temper from..."

    label jen24_dining.merge:
    jenny e_w f_annoyed m_idle "Before you come to my room this afternoon, pop up in the attic and grab my cheer uniform."
    anon e_e "Huh?"
    anon f_confused "Why?"
    jenny "Because I'm going to wear it for the show today."
    anon f_surprised @ -m_talk "!!!"
    anon f_calm "R-really?!"
    show anon e_b f_happy m_laugh
    pause
    show anon e_e -m_laugh
    jenny e_r "Yes, perv..."
    show debbie_dining_table pull2
    jenny e_w p_table_rise "Don't forget."
    show anon e_w
    hide jenny
    with dissolve.nowait
    pause
    anon @ e_b m_laugh "( Hmm, I wonder what we're going to do while she's wearing her old cheerleading outfit? )"

    scene black
    with dissolve
    mono ""
    return what


label jen24_dining.alt:
    show jenny f_angry m_teeth
    anon "She's just trying to help!"
    show debbie f_sad
    anon "You know, kinda like I {i}was{/i} going to help you with your new job..."
    anon "... But now I'm thinking I won't bother."
    jenny f_surprised -m_teeth "That's not-"
    jenny f_sad "I didn't mean to-"
    show jenny f_worried
    anon @ e_w f_worried "[saga.cast.jenny] is sorry."
    anon f_calm "Aren't you?"
    show jenny f_angry m_teeth
    pause
    anon f_confused "Well?"
    show jenny f_angry_pouty -m_teeth
    pause
    show anon f_calm
    jenny e_s f_worried "S-sorry, [saga.cast.debbie]..."
    pause
    jenny e_w "... I'm just, having a bad day."
    show anon e_w
    debbie "It's alright, dear. I understand."
    show jenny e_s
    pause
    show debbie_dining_table pull4 -chair3 -table_legs
    show debbie_dining_table chair3 table_legs as chairs behind anon
    show debbie_dining_table coffee as table
    show debbie a_kiss e_wsw f_calm p_table_bend behind chairs at pos (.425)
    debbie "Thank you, sweetie."
    show jenny e_w f_confused
    show debbie e_b m_kiss at pos(.375)
    with dissolve.nowait
    anon e_se f_surprised @ -m_talk "!!!"
    show anon e_s f_shy of_blush
    show jenny e_r f_annoyed
    show debbie a_mug e_wsw p_table_stand -m_kiss at center
    show debbie_dining_table -coffee as table
    pause
    hide debbie with dissolve
    jenny e_w "You know, I liked you better before you grew a backbone..."
    anon e_e f_worried -of_blush "No, you didn't."
    jenny e_r "W-whatever..."
    jump jen24_dining.merge


label jen24_dining.debbie:
    jump jen07_dining.debbie


label jen24_dining.rails:
    scene camera at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( What does she mean, \"I'm gonna need my strength today?\" )"
    anon a_side e_w f_calm @ -m_talk "( I'd better head down to breakfast and see what she's planning... )"
    hide anon with dissolve
    return


label jen24_jenny:
    scene debbie_bed2 -jenny at stage
    show jenny a_fold f_annoyed at right
    show anon f_worried o_right at left with dissolve
    anon "Alright, I got your uniform down from the attic."
    show anon a_backpack e_s
    jenny f_disgusted "Is it all dusty?"
    label jen24_jenny.merge:
    show jenny e_wsw
    anon a_cheerleader "No, it looks fine to-"
    show jenny a_palm f_annoyed at pos(.675)
    jenny "Give it here!"
    show anon a_surprised_up_both e_w f_surprised
    show jenny a_cheerleader e_sw
    pause
    show anon a_side f_worried
    jenny "Hmm, it'll have to do."
    anon @ -m_talk "..."
    jenny a_hips e_w "Why are you still wearing clothes?!"
    show jenny e_ssw f_snide p_top_off_01
    anon "Uhh..."
    show anon f_surprised
    show jenny p_top_off_02
    pause
    show anon e_sw
    show jenny p_top_off
    pause
    show jenny c_pants e_w f_annoyed -p_top_off
    show anon f_horny
    pause
    jenny "Hurry up, my fans are waiting..."
    show jenny a_pants_off_01 c_naked e_ssw f_snide
    anon e_w f_calm "R-right..."
    show jenny c_cheer p_bottom_off_02
    show anon a_top_off c_casual_bottom e_s
    pause
    show jenny p_bottom_off_01
    anon a_towel e_w "What are we doing today?"
    show anon p_bottom_off
    show jenny p_top_off_04
    pause
    show anon a_side c_pants -p_bottom_off
    jenny e_w p_top_off_01 "Something special."
    jenny a_hips f_horny -p_top_off_01 "Well, what do you think?"
    anon e_wsw f_shy "It's a bit small..."
    jenny f_calm @ e_b m_laugh "Haha, more than a bit!"
    jenny a_up f_horny p_twist_turn "It's sexy though, right?"
    show jenny e_sw f_smug o_right p_stand_away_turn
    anon e_w f_happy "Y-yeah!"
    jenny a_hips e_w f_horny -o_right -p_stand_away_turn "Haha, good!"
    jenny f_snide "Get on the bed."
    hide jenny with dissolve.nowait
    jenny "And put your mask on!"
    hide anon with dissolve

    label jen24_jenny.cookie hide:
    scene debbie_bed2_bed
    show anon c_pants e_sw f_shy of_lucha p_cam_sit_back
    show debbie_bed2_bed laptop as laptop
    show jenny c_cheer e_sw f_horny p_bed_prone_laptop
    with fade
    pause
    jenny e_b f_calm m_laugh @ -m_talk "Hehe, see!"
    jenny e_sw f_horny -m_laugh "I told you guys I used to be head cheerleader."
    pause
    jenny "Oh, really?"
    pause
    jenny "So you always wanted to fuck a cheerleader, huh?"
    pause
    jenny "How about the rest of you boys?!"
    jenny "You wanna see me get fucked?"
    anon f_surprised @ -m_talk "( !!! )"
    "*PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*"
    jenny "You can do better than that..."
    "*PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*{w=.02} *PING*"
    label jen24_jenny.reuse:
    jenny e_b f_calm m_laugh @ -m_talk "Hehehe!"
    jenny e_sw f_horny -m_laugh "Alright, let me get things ready..."
    show anon a_up d_soft p_cam_lay z_b_ob_of_a_oa
    show mimic anon behind laptop at pos.anon
    show jenny p_bed_mount_away behind mimic
    with dissolve
    anon "Are we really going to-"
    show anon a_side
    jenny a_hips p_bed_sit_top_away "Shh!"
    show anon a_up
    show jenny a_out
    pause
    show jenny a_handcuffs
    anon "Aww, c'mon [saga.cast.jenny]!"
    anon d_hard "You know I hate these things..."
    show anon oa_cuffs
    jenny a_out "Shut your mouth!"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon "I don't like them!"
        jenny "HOLD STILL!"
        anon "Grr!"
        jenny "I'm in charge here, not you!"
        "*PING*{w=.06} *PING*{w=.06} *PING*{w=.06} *PING*{w=.06} *PING*"
        jenny a_hips "There!"
        jenny "Sheesh, I don't know what you're complaining about..."
        jenny "Here I am, offering to fuck your brains out, and you're whining about stupid handcuffs!"
        jenny a_side f_smug p_bed_sit_top_away_turn "You boys wouldn't put up a fight, would you?!"
    else:

        anon "..."
        pause
        show jenny a_hips

        if saga.cast.jenny < 'sex':
            jenny "Good."
        else:

            jenny "And if you hate them that much, quit moaning about them and do something."
            jenny "They're only plastic, I'm sure the boys would love to see you try and break free!"

        jenny "Now, beg for it."
        anon "What?!"
        jenny "You want me to take that big cock of yours for a ride, don't you?"
        anon "Y-yes..."
        jenny "Then you're going to beg me for it, in front of my fans!"
        anon "..."
        jenny "Go on!"
        anon "Please..."
        jenny "Princess!"
        anon "..."
        anon "Please, Princess [saga.cast.jenny]..."
        "*PING*{w=.06} *PING*{w=.06} *PING*{w=.06} *PING*{w=.06} *PING*"
        jenny "HAHAHAAH!"
        jenny a_side f_smug p_bed_sit_top_away_turn "You boys ready?"

    "*PING* *PING* *PING* *PING* *PING*"
    show jenny e_ssw f_horny p_bed_sit_top with dissolve
    show jenny a_anon_pants_down_01
    show anon c_pants_down
    hide mimic
    with dissolve
    pause
    show jenny a_anon_pants_down_02 with dissolve
    show mimic anon behind laptop at pos.anon
    show jenny a_side e_sw
    with dissolve
    "*PING* *PING* *PING* *PING* *PING*"
    jenny a_hips p_bed_sit_top_away "Heh, they're excited..."
    show jenny p_bed_sit_insert
    hide mimic
    with dissolve
    pause

    scene debbie_bed2_front
    show jenny b_anon c_cheer p_debbie_bed2_ride_insert
    with fade

    if saga.cast.jenny < 'sex':
        jenny "( Here we go, [saga.cast.anon]... The moment you've been dreaming of! )"

    jenny p_debbie_bed2_ride_anim_09 "Ohh!"
    jenny p_debbie_bed2_ride_anim_12 "Holy shit!"
    jenny p_debbie_bed2_ride_anim_15 "Oh my god, you guys..."
    jenny p_debbie_bed2_ride_anim_18 "This is a {i}really{/i} big dick!"
    show jenny p_debbie_bed2_ride_anim s_6
    jump jen24_jenny.loop1


label jen24_jenny.cheer:
    scene debbie_attic at stage
    show anon a_cheerleader e_s f_pensive with dissolve
    anon @ -m_talk "( Hmm, I don't see any dust or cobwebs... )"
    anon f_shy @ -m_talk "( I guess I'll take it with me to the next camshow. )"
    hide anon with dissolve
    return


label jen24_jenny.dialogue1(opt, rng=-1):
    if opt == 1:
        jenny "Ahh!"

    elif opt == 2:
        jenny "This is so fucking good!"

    elif opt == 3:
        jenny "Oh, fuck!"
        jenny "I'm gonna squirt all over that big dick!"

    elif opt == 4:
        jenny "Mmm, fuck!"

    elif opt == 5:
        jenny "It's so good!!"
        anon "I'm getting close!"
        jenny "SO FUCKING GOOD!!"
        anon "[saga.cast.jenny]!"

    elif opt == 6:
        anon "You're really good at this!"

    elif opt == 7:
        jenny "You like that, don't you?!"
        anon "Y-yeah."

        if rng < .3:
            jenny "Tell me you like it!"
            anon "I like it!"
            jenny "Tell me you love my pussy!"
            anon "Ahh, I love it!"
            jenny "Hahahaah!"
            jenny s_18 "Mmm, yeah!" with hpunch

    pause
    return


label jen24_jenny.dialogue2(opt, rng=-1):
    if opt == 1:
        jenny "OH FUCK!!"

    elif opt == 2:
        jenny "FUCK ME!{w} FUCK ME!"
        jenny "FUUUUCK MEEEE!!!"

    elif opt == 3:
        jenny "AHHH!!!"

    elif opt == 4:
        "*PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*"

    elif opt == 5:
        "*PING*{w=.012} *PING*{w=.012} *PING*{w=.012} *PING*{w=.012} *PING*{w=.012} *PING*"

    elif opt == 6:
        jenny "{i}*Pant*{/i}"

    elif opt == 7:
        if saga.cast.jenny.dom < saga.cast.jenny.sub:
            anon "Enjoying yourself, {i}Princess{/i} [saga.cast.jenny]?"
        else:
            anon "Are you close, Princess [saga.cast.jenny]?"

        if rng < .3:
            jenny s_13 "Ngghhh!!" with hpunch
            "*PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*"
        else:

            jenny "Fuuuucck!"

    pause
    return


label jen24_jenny.fail:
    $ renpy.notify(_('Insufficient {color=e40002}STR{/color}.'))
    jenny "Oh my god!"
    pause
    jenny "Fuck me!"
    pause
    jenny "FUCK ME!!"
    jump jen24_jenny.loop1


label jen24_jenny.inside1:
    if saga.cast.jenny < 'sex':
        anon "I can't hold it!"
    else:
        anon "Get off!"

    pause
    anon "[saga.cast.jenny]!!!"
    jenny "NGGHHH!!!"
    anon "I can't-"
    pause
    show jenny p_debbie_bed2_ride_cum s_400ms
    anon "HNNGGG!!!" with flash
    pause
    show jenny p_debbie_bed2_ride_pullout_01

    call mini.womb (saga.cast.jenny)

    jenny "Haah... Haaah..."
    jenny p_debbie_bed2_ride_pullout "Fuuuck, that was incredi-"
    jenny "!!!"
    jenny "Did you cum inside me?!"
    anon "I warned you!"
    jenny "I didn't hear anything!"
    anon "Well, what do you want me to do?!"
    anon "I'm handcuffed to your bed!"
    jenny "I could get pregnant you moron!"
    anon "Then you should have gotten off when I warned you!"
    jump jen24_jenny.post


label jen24_jenny.inside2:
    anon "I'm getting close!"
    pause
    jenny "Don't stop!"
    anon "[saga.cast.jenny], I can't-"
    jenny "DON'T STOP!"
    pause
    jenny "NGGHHH!!!"
    show jenny p_debbie_bed2_free_cum s_400ms
    anon "HNNGGG!!!" with flash
    pause
    show jenny p_debbie_bed2_free_pullout_01

    call mini.womb (saga.cast.jenny)

    jenny "Haah... Haaah..."
    jenny p_debbie_bed2_free_pullout "Fuuuck, that was incredi-"
    jenny "!!!"
    jenny "Did you cum inside me?!"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon "You told me not to stop..."
        jenny "I didn't mean for you to cum inside me, idiot!"
        anon "Don't start in with the name-calling..."
        jenny "What if I get pregnant!!"
    else:

        anon "Y-you told me not to stop..."
        jenny "Yeah, but I didn't say to finish inside me you idiot!"
        anon "I'm sorry, I didn't mean to-"
        jenny "What if I get pregnant?!"
        anon "..."

    jump jen24_jenny.post


label jen24_jenny.item:
    scene debbie_bed2 -jenny at stage
    show jenny a_fold f_annoyed at right
    show anon a_pocket f_worried o_right at left with dissolve
    jenny "What are you doing?!"
    anon f_confused "You told me to meet you here this afternoon."
    jenny "Yeah, with my cheerleading uniform!"
    anon f_worried "Oh, right."
    jenny a_point "Hurry up and go get it from the attic!"
    hide anon with dissolve.nowait
    pause
    jenny a_side @ e_r "Idiot..."
    return


label jen24_jenny.loop1:
    menu(range=(6, 18, 3), screen='lewd', tag='jenny'):
        "Keep Going":
            pass
        "Cum Inside":

            jump jen24_jenny.inside1
        "Cum Outside":

            jump jen24_jenny.outside1

        "Break Free" if saga.cast.jenny.dom < saga.cast.jenny.sub or saga.cast.jenny > 'sex':
            if saga.cast.anon.str < 7:
                jump jen24_jenny.fail

            jump jen24_jenny.switch

        "Costume" if _in_replay:
            if 'c_cheer' in renpy.get_attributes('jenny'):
                show jenny c_naked
            else:
                show jenny c_cheer

    $ renpy.dynamic(pool=saga.lewd.pool(7, max=2))

    while pool:
        call jen24_jenny.dialogue1 (pool.pop(), rng=renpy.random.random()) from jen24_jenny.pool1

    jump jen24_jenny.loop1


label jen24_jenny.loop2:
    menu(range=(9, 13, 1), screen='lewd', tag='jenny'):
        "Keep Going":
            pass
        "Cum Inside":

            jump jen24_jenny.inside2
        "Cum Outside":

            jump jen24_jenny.outside2

        "Costume" if _in_replay:
            if 'c_cheer' in renpy.get_attributes('jenny'):
                show jenny c_naked
            else:
                show jenny c_cheer

    $ renpy.dynamic(pool=saga.lewd.pool(7, max=2))

    while pool:
        call jen24_jenny.dialogue2 (pool.pop(), rng=renpy.random.random()) from jen24_jenny.pool2

    jump jen24_jenny.loop2


label jen24_jenny.outside1:
    anon "I'm going to cum!"
    jenny "Hold it!"
    anon "W-what?! It doesn't work like that!"
    jenny "I'm so close!"
    anon "[saga.cast.jenny]!!!"
    jenny "FUCK!!"
    show jenny d_anon p_debbie_bed2_ride_cumshot s_400ms
    anon "HNNGGG!!!" with flash
    pause
    anon "Haah... Haah..."
    jenny "You couldn't have lasted another ten seconds?!"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon "It's difficult when I'm handcuffed to the bed!"
    else:
        anon "S-sorry."

    jenny "Whatever..."
    jump jen24_jenny.post


label jen24_jenny.outside2:
    anon "I'm getting close!"
    pause
    jenny "Don't stop!"
    anon "[saga.cast.jenny], I can't-"
    jenny "DON'T STOP!"
    pause
    jenny "NGGHHH!!!"
    show jenny d_anon p_debbie_bed2_free_cumshot s_400ms
    anon "HNNGGG!!!" with flash
    pause
    anon "Haah... Haah..."
    jenny "What the fuck, I told you not to stop!!"
    anon "What, do you want me to cum inside you?!"
    jenny "N-no, it just... Felt really good and-"
    jenny "{i}*Sigh*{/i} Never mind..."
    jump jen24_jenny.post


label jen24_jenny.plan:
    jump jen18_jenny.plan


label jen24_jenny.post:
    "*PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*"
    jenny "Oh for fuck's sake..."
    jenny "Show's over, pervs!"
    $ renpy.end_replay()

    scene debbie_bed2 t1 -jenny at stage
    show jenny a_hips c_cheer f_annoyed at right
    show anon c_pants f_happy o_right at left
    with fade
    anon "That was awesome!"
    jenny @ e_r "Yeah, whatever."
    jenny "You were alright."
    show anon f_worried
    jenny "Now, get out!"
    anon "Can't we just-"
    jenny a_money "No, take your stupid money and get out!"
    hide jenny with dissolve.nowait
    show anon a_cash at pos(.4)
    anon "Alright, sheesh..."
    hide anon with dissolve

    call shot.debbie_bed2_door
    show debbie_landing t1
    with fade
    show anon a_pocket e_b f_happy m_teeth with dissolve

    if saga.cast.jenny < 'sex':
        anon @ -m_talk "( I just had sex with [saga.cast.jenny]... )"
        anon @ -m_talk "( On camera in front of hundreds of people! )"
        pause
        anon @ -m_talk "( How crazy is that?! )"
        anon @ -m_talk "( I hope we do it again. )"
    else:

        anon @ -m_talk "( Ahh, another wonderful day in the life of a camslut. )"
        anon @ -m_talk "( If only all jobs were this gratifying! )"

    hide anon with dissolve
    return 'sex'


label jen24_jenny.switch:
    jenny p_debbie_bed2_free_break "!!!" with hpunch
    jenny p_debbie_bed2_free_anim s_9 "OH FUCK!!"
    pause
    jenny "OHMYGOD, OHMYGOD, OHMYGOD!!!"
    pause
    jenny "AHHH!!!"
    "*PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*{w=.01} *PING*"
    pause
    jenny "FUUUUCK MEEEE!!!"
    jump jen24_jenny.loop2


label jen24_reset:
    return


label jen24_reset.bed2:
    jump jen18_reset.bed2


label jen24_retry:
    scene debbie_bed2 -jenny at stage
    show jenny a_hips f_annoyed at right
    show anon o_right at left with dissolve
    jenny "What the fuck, [saga.cast.anon]?!"
    anon f_confused @ -m_talk "Huh?"
    jenny "I had to push back the show because of you!"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen24_retry.alt

    show jenny e_wsw
    anon a_respect p_bow "I'm sorry!"
    jenny "Gah, you're such a pathetic loser..."
    jenny "... I don't even know why I bother with you!"
    show jenny e_w
    anon a_side e_osw f_sad -p_bow @ -m_talk "..."
    jenny "You're lucky my fans like your big cock, otherwise I'd find someone else!"
    anon e_w f_confused "But I thought nobody else wanted to do this with you?"
    show anon f_surprised m_teeth
    jenny a_upset f_angry m_teeth "Shut up!!" with hpunch
    show jenny a_side
    show anon f_worried_surprised -m_teeth
    pause

    if saga.prop.costume_cheer_old not in saga.cast.anon:
        jump jen24_retry.item

    anon "I uhh-"
    anon f_shy "I brought that uniform you wanted."
    show anon a_backpack e_s
    label jen24_retry.merge:
    jenny f_annoyed m_idle @ e_r "Yeah, and it's probably all fucking dusty."
    jump jen24_jenny.merge


label jen24_retry.alt:
    anon a_rub f_shy "Oh, uhh... my bad."
    jenny "What, you think just because you have a nice cock, you can flake on me and I'll just happily play with it next time?"
    anon a_side f_confused "Ehh, will you not?"
    jenny a_fold f_angry_pouty @ -m_talk "..."

    if saga.prop.costume_cheer_old not in saga.cast.anon:
        jump jen24_retry.item

    anon f_calm "Hey, look..."
    anon a_backpack e_s f_shy "... I went up in the attic and got your cheerleading outfit!"
    jump jen24_retry.merge


label jen24_retry.item:
    show jenny a_palm f_annoyed at pos(.675)
    jenny "Gimme my uniform."
    anon a_uneasy f_worried "Oooh, crap..."
    anon @ f_shy "... I knew I was forgetting something."
    jenny a_side @ e_r "Holy shit, you are worthless!"
    anon a_side "Look, I'll go get it right now, just remind me where it's at?"
    pause
    jenny a_upset e_b f_calm m_drink @ -m_talk "{i}*Inhales*{/i}"
    show anon f_confused
    jenny a_side @ -m_talk "{i}*Exhales*{/i}"
    show anon f_worried
    jenny e_w f_annoyed -m_drink "It's in the attic."
    anon "A-"
    show anon f_afraid m_teeth
    jenny a_upset f_angry m_teeth "You absolute blockhead."
    anon "Alright, I'll be right back."
    hide anon with dissolvefast
    return


label jen24_retry.jenny:
    jump jen19_intro.jenny


label jen24_retry.plan:
    jump jen18_retry.plan


label jen24_cheer:
    scene debbie_attic at stage
    show anon a_cheerleader e_s f_confused with dissolve
    anon @ -m_talk "( Hmm, it seems oddly clean considering... )"
    anon f_shy @ -m_talk "( ... At least [saga.cast.jenny] will be pleased. )"
    hide anon with dissolve
    return


label jen24_cheer.fence:
    scene camera at stage
    show anon with dissolve
    anon @ -m_talk "( [saga.cast.jenny] said her cheerleading uniform should be in the attic. )"
    anon f_pouty @ -m_talk "( This camshow had better be worth all the trouble I'm going through... )"
    hide anon with dissolve
    return


label jen24_give:
    jump jen24_jenny


label jen24_give.rails:
    scene camera at stage
    show anon a_cheerleader e_s f_confused with dissolve
    anon @ -m_talk "( Heh, is [saga.cast.jenny] really gonna try and squeeze into this thing? )"
    anon f_calm @ -m_talk "( I can't wait to find out! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
