label deb_shower:
    return


label deb_shower.bail:
    if saga.cast.debbie < 'sex':
        anon "( I probably shouldn't. )"
        anon "( I don't want her to be upset. )"
    else:

        anon "( I should leave her to shower in peace. )"

    pause
    return


label deb_shower.peek1(seed):
    call shot.debbie_bath_peek
    show layer master at blur(20)
    call deb_shower.wash
    anon "( Hmm, it's so steamy... )"
    anon "( I can't quite make out- )"
    show layer master
    with dissolve.nowait
    anon "( Oh, it's [saga.cast.debbie]. )"
    pause
    anon "( I kinda feel bad peeping on her, she takes such good care of me... )"
    anon "( ... But then again... )"
    pause
    call deb_shower.wash
    anon "( ... Man, just look at her! )"
    pause
    anon "( She's got curves in all the right places! )"
    pause
    anon "( Alright, that's enough. )"
    anon "( Best move on before someone catches me. )"
    pause
    return


label deb_shower.peek2(seed):
    call shot.debbie_bath_peek
    show layer master at blur(20)
    call deb_shower.wash
    anon "( Hmm, it's so steamy... )"
    anon "( I can't quite make out- )"
    show layer master
    with dissolve.nowait
    anon "( Ah, it's [saga.cast.debbie] again. )"
    pause
    anon "( How did I go all these years never realizing just how beautiful she is? )"
    anon "( Now it's all I see. )"
    pause
    call deb_shower.wash
    anon "( Ngh, I wish things were different and we could become closer. )"
    anon "( I'd go in there right now and sweep her off her feet! )"
    pause
    anon "( {i}*Sigh*{/i} Oh well, it's just not in the cards. )"
    anon "( I shouldn't linger too long, best get out of here. )"
    return


label deb_shower.peek3(seed):
    call shot.debbie_bath_peek
    show layer master at blur(20)
    call deb_shower.wash
    anon "( Hmm, it's so steamy... )"
    anon "( I can't quite make out- )"
    show layer master
    with dissolve.nowait
    anon "( Oh, hello [saga.cast.debbie]! )"
    pause
    anon "( So much has happened between us recently, it's hard believe. )"
    anon "( I wonder if she'll be willing to push things a little further in the future? )"
    anon "( It's certainly nice to consid- )"
    call deb_shower.play
    anon "( !!! )" with hpunch
    pause
    anon "( I'd say this bodes well for my chances. )"
    pause
    anon "( That is so freaking hot! )"
    anon "( Wish I could hang around here and watch but getting caught now could ruin everything. )"
    pause
    return


label deb_shower.peek4(seed, busy):
    call shot.debbie_bath_peek
    show layer master at blur(20)
    call deb_shower.wash
    anon "( Hmm, it's so steamy... )"
    anon "( I can't quite make out- )"
    show layer master
    with dissolve.nowait
    anon "( Oh, momma! )"
    anon "( Man, I could stare at that body all day... so delicious! )"
    pause
    call deb_shower.play
    anon "( Oh, it looks like someone is feeling naughty! )"

    if saga.time.dark:
        anon "( Man, if it wasn't so late I'd be in there in a flash! )"
        anon "( Oh well, maybe next time. )"
        pause
        return

    if busy:
        anon "( Man, it's a shame I've got so much stuff to do. )"
        anon "( Ugh, I hate walking away from this but- )"
        pause
        anon "( {i}*Sigh*{/i} Maybe next time. )"
        return

    if seed < .5:
        anon "( Too bad she's already done with her shower... )"
        anon "( ... Maybe next time. )"
        pause
        return

    pause

    menu:
        "Go inside.":
            pass

        "{color=1ceda7}Preview animations which will be worked into future updates!{/color}" if saga.cast.debbie > 'shower.handjob':
            jump wip.deb_shower
        "Leave.":

            anon "( Maybe some other time. )"
            pause
            return

    hide gap
    with dissolve
    show anon d_hard e_sw f_horny_smug o_right behind steam at left with dissolve.nowait
    pause
    anon e_w f_horny "[saga.cast.debbie]?"
    show anon f_shy
    show debbie_bath water
    show debbie_bath -water as glass
    show debbie a_surprised f_surprised p_stand at pos(.6)
    debbie @ -m_talk "Hmm?"
    debbie a_cover f_shy of_blush "Oh, umm... H-hey, sweetie."

    if saga.cast.debbie < 'shower.handjob':
        debbie f_curious "You weren't, umm... watching me... were you?"
        anon a_uneasy "Maybe a bit."
        debbie e_sw f_shy "Oh, dear... I-"
        show debbie f_surprised
        anon "Can I join you?"
        show anon f_confused
        debbie @ -m_talk "..."
        anon "[saga.cast.debbie]?"
        debbie f_shy "... Y-yeah, sure... I suppose."
        anon a_fists f_happy "Sweet!"
        show debbie a_shy m_lip
        show anon a_pants_off_01_boner e_s f_horny
        pause
        show anon c_casual_top p_pants_off_02
        pause
        show debbie f_surprised -m_lip
        show anon a_top_off c_naked e_b f_happy p_stand
        pause
        show debbie e_se f_shy
        show anon a_throw_top e_ese
        pause
        show anon a_side_nervous e_w
        debbie a_nervous e_w of_none "[saga.cast.jenny] didn't see you come in here, did she?"
        show anon a_surprised c_naked_wet f_calm behind debbie at pos(.405)
        anon "No, of course not."
        anon "I promised you I'd be careful."
        debbie "Oh, good."
        anon e_sw f_horny "Man, you look sexy!"
        debbie a_cover e_s "Hehe, sweetie... you're embarrassing me!"
        show debbie e_w
    else:

        anon "Can I join you?"
        debbie a_shy f_happy "Yes, of course."
        anon f_happy "Nice!"
        show debbie e_sw f_horny m_lip
        show anon a_pants_off_01_boner e_s f_horny
        pause
        show anon c_casual_top p_pants_off_02
        pause
        show anon a_top_off c_naked e_b f_happy p_stand
        pause
        show anon a_throw_top e_ese
        pause
        show anon a_side_nervous e_w
        debbie a_nervous e_w f_shy of_none -m_lip "You made sure [saga.cast.jenny] didn't see you, right?"
        show anon a_surprised c_naked_wet f_calm behind debbie at pos(.405)
        anon "Yeah, I was careful."
        debbie f_calm "Oh, thank goodness."

    anon e_w "C'mere."
    hide anon
    debbie b_anon p_kiss "Mm."
    pause
    show anon a_surprised c_naked_wet d_hard f_happy o_right behind debbie at pos(.405)
    show debbie a_side_nervous f_horny of_blush p_stand -b_anon
    pause
    show debbie e_sw
    pause
    debbie e_w "You're, umm-"
    debbie e_sw "{i}*Ahem*{/i} Certainly full of energy today."
    anon e_s f_surprised @ -m_talk "Hmm?"
    anon e_w f_shy "Oh, yeah... I suppose I am."
    debbie e_w "Don't worry, sweetie... I'll take care of you."

    if saga.cast.debbie < 'blowjob':
        jump deb_shower_handjob

    menu:
        "Handjob.":
            jump deb_shower_handjob
        "Blowjob.":

            jump deb_shower_blowjob
        "Can I touch you?":

            pass

    return


label deb_shower.play:
    if seed < .5:
        show debbie c_naked_wet o_left p_towel_play s_1 behind steam at pos(.6)
    else:

        show debbie_bath -water
        show debbie_bath water as glass
        show debbie a_rub c_naked_wet p_shower_play s_400ms behind glass

    if seed < .5 and renpy.showing('glass'):
        show debbie_bath debbie_sink glass misc_towel -water
        hide glass
        stop sfx 

    return


label deb_shower.view(seed):
    call shot.debbie_bath_peek
    show layer master at blur(20)

    if seed < 1:
        call deb_shower.wash
    else:

        $ seed = seed % 1
        call deb_shower.play

    pause
    show layer master
    with dissolve.nowait
    pause
    return


label deb_shower.wash:
    if seed < .166:
        show debbie c_naked_wet p_towel_hair s_700ms behind steam at pos(.6)
    elif seed < .333:
        show debbie a_towel_boobs c_naked_wet e_s p_stand s_800ms behind steam at pos(.6)
    elif seed < .5:
        show debbie c_naked_wet o_right p_towel_legs s_700ms behind steam at pos(.6)
    elif seed < .75:
        show debbie c_naked_wet p_shower_hair s_800ms behind glass
    else:
        show debbie c_naked_wet p_shower_legs s_700ms behind glass

    if seed < .5 and renpy.showing('glass'):
        show debbie_bath debbie_sink glass misc_towel -water
        hide glass
        stop sfx 

    $ seed = seed * 6 % .5 + (0 if seed < .5 else .5)
    return


label deb_shower_blowjob:
    anon "Could you... y'know... use your mouth?"
    return


label deb_shower_handjob:
    anon "I love when you use your hand."
    debbie "Then turn around for me."
    show debbie behind anon
    anon e_e o_left "You don't mind, do you?"
    show debbie a_wash_anon_shoulders e_wsw oa_hands s_1 z_b_ob_f_of_a at pos.anon.wash
    show mimic debbie as debbie_hands behind glass at pos.debbie
    debbie "Not at all!"
    debbie "I enjoy taking care of my boy."
    anon f_happy "Mmm, that feels nice."
    pause
    show anon e_b z_b_ob_f_of
    show mimic anon as anon_arms behind glass at pos.anon
    debbie a_wash_anon_torso "You just relax, okay?"
    anon @ -m_talk "Mhmm."
    pause
    show debbie a_jerk_04 e_s oa_hand p_lean z_b_f_of at pos.anon.hold_hips
    show mimic debbie as debbie_hands at pos.debbie
    anon a_surprised_reach d_none e_s f_surprised "Ahh!"
    show anon f_horny
    show debbie a_jerk s_2
    pause
    debbie "Does that feel good?"
    anon e_b "Oh, yeah."
    pause
    anon e_sw "Your hands are so soft."
    debbie e_ne "You like that?"
    anon "D-definitely."
    show debbie e_s s_4
    anon e_s f_horny_smug @ f_shy "Haah!"
    pause
    show anon e_sw
    debbie "I just can't get over how big you are..."
    show anon e_s
    debbie "... I can't even get my hand all the way around it."
    pause
    show anon e_b f_horny
    debbie "That's it, sweetie... just relax and think about happy thoughts."
    anon "That shouldn't be too difficult."
    anon "Everything about this gives me happy thoughts."
    debbie @ e_b f_happy m_laugh "Hehe!"
    pause

    if saga.cast.debbie < 'blowjob':
        jump deb_shower_handjob.fast

    menu:
        "Blowjob.":
            jump deb_shower_blowjob
        "Cum.":

            pass

    label deb_shower_handjob.fast hide:
    show debbie s_6
    anon e_s f_shy "Oh, [saga.cast.debbie]!"
    anon e_sw "I'm getting close!"
    debbie "That's good, sweetie..."
    debbie "... Just let it all out for me."
    pause
    anon e_s "Oh!"
    pause
    anon e_b f_distressed "Oh, [saga.cast.debbie]!"
    pause
    anon "I-"
    hide anon_arms
    hide debbie_hands
    show anon m_talk p_debbie_lean_hj_cum z_reset at pos.debbie
    show debbie a_none b_anon od_cumshot p_lean_hj_cum s_400ms z_reset
    anon "HNNGGG!!!" with flash
    debbie "There we go."
    pause
    show anon e_sw f_shy -m_talk
    debbie e_ne od_cum p_lean_hj_cum_02 "Good boy!"
    show anon a_surprised d_firm e_e p_stand at pos(.405)
    show debbie a_wash_anon_shoulders_02 e_sw f_calm oa_hands od_none p_stand z_b_f_a -b_anon at pos.anon.wash
    show mimic debbie as debbie_hands behind glass at pos.debbie
    debbie "See, all better."
    show debbie e_wsw
    anon "Man, that really hit the spot."
    hide debbie_hands
    show anon e_w o_right behind debbie
    show debbie a_touch_anon_face e_w at pos.anon.touch_face
    debbie "I take good care of my boy, don't I?"
    anon "I'd say you do, yeah."
    debbie a_shy "Now, let's get cleaned up quickly and I'll go make us some food."
    anon a_surprised_reach d_soft "Have I mentioned you're the best landlady ever?"
    debbie "Heh, aww."
    show anon a_surprised
    debbie a_side_nervous e_e f_curious o_right "You wanna wash my back for me?"
    anon f_happy "Umm, do bears shit in the woods?!"
    show anon f_worried
    debbie f_sad "Sweetie, language!"
    anon f_shy "Heh, sorry."
    show debbie f_happy
    anon a_surprised_reach "I'd love to wash your back for you."

    scene black
    with dissolve
    mono ""
    return 'handjob'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
