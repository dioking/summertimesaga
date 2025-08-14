label deb05_intro:
    scene debbie_bed3 at stage
    show anon a_think e_nw f_pensive o_right with dissolve
    anon @ -m_talk "( I wonder if [saga.cast.debbie] needs more help around the house? )"
    anon @ -m_talk "( I should try and help her whenever possible and lighten her load. )"
    hide anon with dissolve
    return


label deb05_delay:
    return


label deb05_delay.debbie:
    anon f_confused "Anything else you need help with?"

    if saga.time.dawn:
        debbie f_calm "No. Not right now, sweetie."
        debbie "Maybe later, if you're still available."
    else:

        debbie f_calm "No. Not today, sweetie."
        debbie "Maybe tomorrow, if you're still available."

    show anon f_calm
    debbie f_happy "Thanks for asking!"
    anon "You're welcome, [saga.cast.debbie]."
    hide anon with dissolve
    return


label deb05_dishes:
    call shot.debbie_kitchen_far
    show debbie a_wash_plate e_sw behind island at pos(.8)
    pause
    show anon a_pocket o_right behind island at pos(.35) with dissolve.nowait
    pause
    debbie a_wash_plate_02 e_w "Oh, hey, sweetie!"
    anon "Hey, [saga.cast.debbie]!"
    debbie f_curious "You need something?"
    show anon e_sw
    debbie a_wash_plate e_sw f_calm "I'm just finishing up the dishes..."

    menu:
        "Let me help.":
            pass
        "Never mind.":

            anon a_wave e_w "Okay. I'll come back later, then."
            hide anon with dissolve
            return False

    show debbie a_wash_plate_01 e_w f_surprised
    anon e_w "Why don't you take a break for a while?"
    anon a_palm "I'll dry the rest."
    debbie f_shy "That's very sweet but you don't have to do that."
    anon "Nah, it's fine... I'm bored anyways."
    debbie f_calm "Heh, well, alright. If you're bored anyway...!"
    show anon a_plate_clean
    debbie a_clasp "... We just need to dry and store them away in the cabinets."
    anon "Can do!"
    debbie f_happy "Thanks for helping out around here, sweetie."
    anon e_b f_happy m_laugh "My pleasure, [saga.cast.debbie]."

    scene mono debbie_dishes
    mono "I don't think [saga.cast.debbie] had ever had help with dishes before." with fade
    mono "She told me her late husband never did any work around the house and my dad only really helped with yardwork or broken appliances."
    mono "She stayed with me in the kitchen until I was finished and we had a nice long chat. It was nice getting to know [saga.cast.debbie] better."

    scene black
    with dissolve
    mono ""
    return True


label deb05_vacuum:
    call shot.debbie_lobby_center
    show debbie a_vaccuum e_sw f_sad p_bend s_1 at pos(.85)
    pause
    show anon a_pocket o_right at left with dissolve
    debbie e_w f_surprised -p_bend "Oh, you startled me!"
    show debbie f_calm
    anon @ e_b f_happy m_laugh "Sorry, [saga.cast.debbie]..."
    anon "... that wasn't my intention."
    debbie f_curious "Is the noise bothering you?"
    debbie "I'm nearly finished."
    anon "You doing alright?"
    debbie e_se f_shy "Ugh, it's just this stupid back of mine is acting up!"

    menu:
        "Let me help.":
            pass
        "Take a break.":

            anon a_point f_confused "Maybe you should take a break for a bit?"
            debbie e_w f_sad "Oh, umm..."
            show anon a_side f_calm
            debbie "... Yeah, alright."
            show anon f_confused
            debbie e_s "Sorry."
            anon a_up f_worried_surprised "No, it's not the noise, it's-"
            debbie e_w "I just need to stay busy, ya know?"
            show anon a_side
            debbie "Keep my mind occupied and off recent events."
            show debbie e_sw
            anon e_sw f_sad "{i}*Sigh*{/i} Yeah, I get it."
            pause
            show debbie a_pan o_right p_stand_away at pos(.95)
            debbie "There's plenty of things that need doing in the kitchen."
            show anon a_surprised e_w f_worried at pos(.375)
            hide debbie
            with dissolve.nowait
            anon "Just try not to overwork yourself, okay?"
            debbie "Oh, don't worry... I'm fine!"
            anon a_side f_confused "If you say so."
            pause
            hide anon with dissolve
            return False

    show anon a_palm at pos(.4)
    show debbie e_w f_curious
    anon "Here, [saga.cast.debbie], pass me the vacuum."
    debbie "Really?"
    debbie "You're going to vacuum?"
    anon a_side f_confused "Yeah, why not?"
    show debbie f_shy
    anon f_calm "Have yourself a little rest."
    anon f_shy "No sense in working yourself so hard when I'm here to help."
    debbie "That's sweet, but really... you don't have-"
    anon f_calm "I know I don't have to help, [saga.cast.debbie]..."
    anon f_happy "... I want to help!"
    debbie f_calm "Well, I suppose I can't say no to that."
    show anon a_vaccuum e_s f_horny
    debbie a_clasp f_happy "You're such a wonderful boy!"
    anon e_w f_happy "Happy to do it!"

    scene mono debbie_lobby_stairs vacuum
    mono "I felt bad [saga.cast.debbie] was having a hard time with her back pain. The least I could do was help her out, even if it was more work than I intended." with fade
    mono "Turns out cleaning stairs is a hassle! No wonder her back was hurting her...\nAt least [saga.cast.debbie] kept me company while I worked."

    scene black
    with dissolve
    mono ""
    return True


label deb05_laundry:
    call shot.debbie_utility_laundry
    show debbie a_basket at right
    show anon a_pocket o_right at left
    debbie "Hey, sweetie!"
    debbie "You need something?"

    menu:
        "Let me help.":
            pass
        "You're busy.":

            anon "Looks like you're busy."
            anon "I'll come back later."
            hide anon with dissolve
            return False

    show anon at pos(.35) with dissolve.nowait
    anon a_surprised "I can do that laundry, [saga.cast.debbie]. Why don't you take a break."
    debbie f_shy "No, it's fine... I can do it."
    anon a_side f_shy "C'mon, you deserve a rest."
    anon "You do so much around here and besides, I'm really starting to enjoy helping you."
    show anon f_happy
    debbie "Oh, [saga.cast.anon]... You're spoiling me!"
    show anon a_surprised p_stand_away at center with dissolve.nowait
    debbie "You'd better be careful, cause a girl could get used to this..."
    show anon a_basket -p_stand_away
    debbie a_clasp f_curious "... You know how everything works?"
    anon f_calm "I think so, but you're welcome to instruct."
    debbie f_shy "Thanks so much for doing this, [saga.cast.anon]."
    debbie "I really appreciate it."
    show anon f_happy
    debbie "Your father would be so proud of you!"
    anon "Heh, thanks!"

    scene mono debbie_utility_laundry2
    mono "I was having a lot of fun helping [saga.cast.debbie] out around the house, and I know she was enjoying it as well. Always so eager to strike up a conversation and learn more about my life." with fade
    mono "The time spent together brought us closer and I couldn't help but admire her beauty and charm."
    mono "She seemed to be growing more comfortable with me too. The way she looked at me, and her innocent touches..."

    call shot.debbie_utility_laundry
    show debbie a_clasp at right
    show anon o_right at left
    with fade
    debbie "Heh, this has all been really wonderful, [saga.cast.anon]..."
    debbie "... I can't for the life of me figure out why we didn't spend this time together sooner."
    anon "Yeah, I know what you mean."
    debbie a_nervous f_shy "Tsk, you know... you've been such a big help recently..."
    debbie "... And I hate to ask you for more but-"
    anon "It's okay, you can ask!"
    show anon e_sw f_surprised
    debbie a_reach o_right p_bend_away "Would you mind running this basket of clean laundry upstairs so I can fold it?"
    show anon e_ssw
    debbie e_sw f_sad p_bend -o_right "It's just so heavy and I've been cleaning all day... and-"
    show debbie a_side e_w f_shy -p_bend
    anon a_surrender e_b f_calm "Say no more."
    show debbie e_sw
    show anon a_reach e_s p_bend
    pause
    show debbie e_w
    anon a_basket e_w -p_bend "You want it upstairs in your bedroom?"
    debbie "Yeah, I usually fold everything on my bed before putting it away."
    show anon -o_right
    hide debbie with dissolve.nowait
    anon "You got it!"
    hide anon with dissolve.nowait
    debbie "Aww, thanks sweetie."

    scene mono debbie_utility_stairs
    mono "Looking back, it's clear there was more motivating me to help [saga.cast.debbie] than just my usual altruistic nature." with fade
    mono "She could have asked me for the moon at that moment and I would have mindlessly agreed to wrest it from the stars."

    scene debbie_bed1 -debbie_basket at stage(.4, .42, 2)
    show debbie a_clasp o_right at right
    with fade
    pause
    show debbie -o_right
    show anon a_basket e_e
    with dissolve.nowait
    anon "You want it here?"
    debbie "Yeah, just over there by the window will be fine... thank you."
    show anon e_s o_right at left
    pause
    show debbie e_sw
    show anon a_reach p_bend
    pause
    show anon a_side e_w -p_bend
    debbie e_w "It's gonna feel so good to sit down and rest my legs for a bit!"
    anon a_uneasy "Yeah, I bet."
    hide debbie with dissolve

    scene debbie_bed1_bed_edge
    show debbie a_rub_leg e_s f_sad o_right p_sit_edge_bend at pos.debbie_bed1_bed_edge
    with fade
    pause
    show anon e_sw f_worried at pos(.75, .84)
    anon "Are you hurting badly?"
    debbie e_nw f_shy "Oh, no more than usual."
    show anon f_disgusted
    debbie e_s "But my skin is awfully dry this year..."
    debbie f_sad "... There must be something in the air."
    debbie e_nw f_shy "Would you hand me the lotion from the top drawer of my dresser?"
    anon f_calm "Absolutely."
    show debbie e_w
    hide anon
    with dissolve
    return True


label deb05_lotion:
    scene debbie_drawer
    anon "{i}*Sniiiiiiiiiff*{/i}"
    anon "( Mmm, what an enticing fragrance... )"
    anon "( ... So this is why she always smells so wonderful. )"
    return


label deb05_lotion.debbie:
    scene debbie_bed1_bed_edge
    show debbie a_rub_leg e_s f_sad o_right p_sit_edge_bend at pos.debbie_bed1_bed_edge
    show anon a_finger e_sw f_confused at pos(.75, .84) with dissolve
    anon "W-"
    show anon f_surprised
    debbie e_nw "The lotion is just over there in the dresser, sweetie."
    anon a_salute f_shy_surprised "On it!"
    show debbie e_w
    hide anon
    with dissolve
    return


label deb05_lotion.pants:
    scene debbie_drawer
    anon "( Oooh, those are- )"
    anon "( No! Mustn't get distracted! )"

    if saga.prop.misc_lotion in saga.cast.anon:
        anon "( [saga.cast.debbie] is right there! )"
    else:
        anon "( I should just grab the lotion and go! )"

    return


label deb05_lotion.rails:
    scene debbie_bed1 at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( [saga.cast.debbie] is waiting on me. )"
    anon @ -m_talk "( She said the she keeps her lotion in her dresser. )"
    hide anon with dissolve
    return


label deb05_debbie:
    scene debbie_bed1_bed_edge
    show debbie a_rub_leg e_s f_sad o_right p_sit_edge_bend at pos.debbie_bed1_bed_edge
    show anon a_lotion e_sw at pos(.65, .84) with dissolve
    anon "Here you are, [saga.cast.debbie]."
    debbie e_nw "Thanks, sweetie!"
    show debbie e_s
    show anon a_down e_e f_surprised o_right p_sit_edge behind debbie at pos.debbie.lotion_sit
    with dissolve.nowait
    debbie "Tsk, just look at my knees."
    anon e_sse @ -m_talk "Mhm."
    show anon e_se
    show debbie a_down p_sit_edge_back
    pause
    debbie "It's really no fun getting old, [saga.cast.anon]... I don't recommend it!"
    pause
    anon a_shy_neck e_e f_shy "Do you want me to help you?"
    debbie e_w f_curious @ -m_talk "Hmm?"
    debbie "You mean... with my lotion?"
    anon a_down "Well, yeah..."
    anon "... Err, I mean, if you want."
    debbie f_shy "Mm, I dunno."
    anon f_happy "I just figure, with your legs being sore and all... maybe a bit of massaging could help?"
    anon "And I can apply your lotion while I'm doing it."
    anon "You know, two birds with one stone."
    debbie @ -m_talk "..."
    debbie "Oh, I guess there's no harm in it."
    debbie "Never say no to a free massage, right?"
    show anon a_surprised e_sse f_surprised
    debbie f_calm p_sit_edge_open "Just be careful you aren't too rough with me!"
    anon e_e f_happy "One extra special leg massage, coming right up!"
    show anon a_reach e_sw
    debbie @ f_curious "Oh, I get to experience the extra special version, huh?"
    show debbie e_wsw
    anon a_lotion_01 e_e f_calm "Of course."
    show debbie a_surprised e_sw f_surprised ob_lotion
    anon a_lotion_02 e_sse f_surprised @ -m_talk "( !!! )"
    show debbie e_b f_happy m_laugh
    anon a_lotion_01 e_e "Whoops, that came out faster than I was expecting."
    debbie a_down e_w -m_laugh "Heh."
    show anon a_massage_02 e_sse f_shy z_b_ob_f_of_d_od
    show mimic anon at pos.anon
    debbie "That's alright, sweetie... there's a lot of ground to cover."
    anon e_e f_confused "O-okay."
    show anon a_massage e_sse f_calm
    debbie e_sw f_horny "Mmm, that does feel nice."
    show debbie -ob_lotion
    anon @ -m_talk "..."
    anon "I don't feel any dry skin."
    debbie e_w f_shy "Oh, stop it."
    anon e_e "No, I'm serious!"
    show debbie e_sw
    anon e_sse "It's smooth as silk down here."
    debbie "Heh, I guess it's a good thing I shaved today."
    show debbie e_w f_curious
    anon a_massage_02 e_e f_confused "Should I continue upwards?"
    debbie f_sad "You don't think it's weird, do you?"
    anon f_calm "Nah, why should it be weird?"
    debbie "Well, because I'm-"
    show anon f_confused
    debbie a_cheek e_se f_shy "We're-"
    pause
    debbie a_down e_r f_bored "Ehh, never mind... I'm just being silly."
    show debbie e_w f_calm
    show anon f_calm
    pause
    show debbie e_sw
    show anon a_massage e_s p_kneel_edge -o_right at pos.debbie.lotion_kneel
    show mimic anon at pos.anon
    pause

    scene debbie_bed1_bed_massage
    show debbie e_s f_shy p_sit_massage
    show anon a_massage_leg p_sit_massage
    with fade
    pause
    debbie e_ownw "Phew, you're pretty good at this, [saga.cast.anon]..."
    debbie "... Maybe you could... rub a bit harder?"
    show anon s_1
    debbie e_s "Oh, yeah... that's the spot!"
    anon "Y-yeah, you're really bound up here... I can feel it."
    debbie "Mm, this is heaven!"
    show debbie f_calm m_lip
    anon "( !!! )"
    anon "( She's really opening up. )"
    anon "( I wonder if she realizes I can see her panties? )"
    debbie e_ownw f_shy -m_lip "Oh, sweetie..."
    debbie "... You have such wonderful hands!"
    show debbie e_s
    pause
    debbie e_ownw "Maybe we should send you off to get your masseuse license?"
    debbie "You would make a fortune!"
    show debbie e_s
    pause
    debbie "Haah, wow!!"
    show debbie f_calm m_lip
    pause
    show anon a_massage_leg_01
    debbie c_robe_lewd f_shy p_sit_massage_tilt -m_lip "Nghh!!" with flash
    pause
    show debbie of_blush p_sit_massage
    pause
    debbie e_se f_curious @ -m_talk "( !!! )"

    scene debbie_bed1_bed_edge
    show debbie a_down c_robe_lewd e_wsw f_sad o_right of_blush p_sit_edge_open at pos.debbie_bed1_bed_edge
    show anon a_massage e_sw f_confused p_kneel_edge z_b_ob_f_of_d_od behind debbie at pos.debbie.lotion_kneel
    show mimic anon at pos.anon
    with fade
    debbie "... Heh, that's... probably enough..."
    anon e_nw @ -m_talk "Hmm?"
    hide mimic
    show anon a_surprised e_e f_surprised o_right p_sit_edge z_reset at pos.debbie.lotion_sit
    debbie a_surprised e_w "... I can do the rest."
    show debbie a_cover c_robe f_worried_surprised p_sit_edge_back
    pause
    anon a_down f_confused "You're sure?"
    debbie f_shy "Y-yeah."
    show anon f_worried
    debbie "Why don't you get on with your day, hmm?"
    debbie "I've got all this laundry waiting to be folded."
    show debbie e_wnw
    show anon a_side e_wsw -o_right -p_sit_edge at pos(.65, .84)
    anon "Y-yeah, okay."
    show anon f_calm
    debbie "Thanks again, sweetie."
    anon "You're welcome."
    show debbie e_w
    hide anon
    with dissolve.nowait
    pause
    show debbie e_b
    pause
    $ renpy.end_replay()

    call shot.debbie_bed1_door
    with fade
    show anon a_pocket e_sw f_pouty o_right with dissolve
    anon @ -m_talk "( Dang, I was really enjoying that! )"
    pause
    anon f_pensive @ -m_talk "( It sounds weird to admit it but my landlady can be pretty sexy sometimes. )"
    show anon d_hard f_horny z_b_ob_f_of_a_oa_d_od
    pause
    show anon a_surprised e_s f_shocked m_open
    pause
    anon a_shy_down f_surprised z_reset -m_open @ -m_talk "( Ugh, I shouldn't be thinking these thoughts! )"
    anon f_worried_surprised @ -m_talk "( Better to occupy my mind with other things for a while. )"
    hide anon with dissolve
    return


label deb05_debbie.rails:
    scene debbie_bed1 at stage
    show anon a_lotion o_right at left with dissolve.nowait
    anon "( [saga.cast.debbie] is waiting on me. )"
    anon "( I should get back to her with this lotion. )"
    hide anon
    with dissolve
    return


label deb05_outro:
    return


label deb05_outro.block:
    call shot.debbie_bed1_door
    show anon a_pocket f_worried with dissolve
    anon @ -m_talk "( Probably best I give her some space... )"
    anon @ -m_talk "( ... Don't want to make things awkward. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
