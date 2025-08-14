label deb18_debbies:
    call shot.debbie_main_drive
    show anon a_surprised_up f_surprised at right with dissolve
    anon @ -m_talk "!!!"
    anon a_surprised f_shocked m_open @ -m_talk "( Oh, no! )"
    anon @ -m_talk "( That's the vehicle those Russian goons drive around in! )"

    if saga.cast.yumi < 'guard':
        anon a_rub f_surprised m_teeth @ -m_talk "( I need to get in there! )"
    else:
        anon a_rub f_surprised m_teeth @ -m_talk "( Where the heck is [saga.cast.yumi]?! )"

    hide anon with dissolve
    return


label deb18_lobby:
    play music villain fadeout 1 fadein 1 if_changed
    stop sound fadeout .7

    scene mono debbie_lobby_slap1
    mono "It quickly became apparent that both [saga.cast.dimitri] and [saga.cast.igor] were already inside our home, threatening [saga.cast.debbie]." with fade

    scene mono debbie_lobby_slap2
    mono "I couldn't make out what they were saying, but she looked terrified. I was completely frozen, unsure what to do or how to save her..." with fade

    scene mono debbie_lobby_slap2 slap
    play audio smack
    mono "... And then [saga.cast.dimitri] stuck her." with hpunch
    mono "I watched, in horror as [saga.cast.debbie] crumpled to the floor and my vision went red."
    mono "I felt my body moving towards the door of it's own accord."
    more "I had to get in there! I had to do something!"

    stop music fadeout 5

    scene debbie_lobby -debbie at stage(.49, .53, 1.95)
    show debbie a_reach p_bend_away at pos(y=1.15)
    show dimitri e_sw at pos(.9)
    show igor e_sw o_right at pos(.1)
    with fade
    show igor e_w
    show dimitri e_e
    anon "[saga.cast.debbie]!!"
    show anon a_reach e_sw f_confused p_bend behind debbie at pos(.6)
    show dimitri e_sw
    show igor e_sw
    with dissolve.nowait
    debbie "[saga.cast.anon]?"
    anon "Are you okay??"
    show anon a_handshake e_w f_worried p_stand
    show debbie a_shock f_worried_surprised o_right p_stand at pos(.4, 1.)
    show dimitri e_w
    show igor e_w
    with dissolve.nowait
    debbie "N-no, you shouldn't be here!"
    dimitri "Ah, wonderful!"
    show anon a_protect f_angry o_right at pos(.55)
    show debbie a_nervous f_sad behind anon at pos(.41)
    dimitri "You've come at perfect time."
    anon "Get out of our house!"
    dimitri @ a_out "Oh, such fire!"
    igor a_point "You want we should take them to [saga.cast.raz] now?"
    debbie o_left "P-please, you can't-"
    show igor a_side
    anon a_fists o_left "Back off!"
    anon "I swear, if you touch her again I'm going to-"
    show anon o_right
    show debbie e_e
    dimitri @ e_b f_smug m_laugh "Hah, what are you going to do, little bunny?"
    dimitri "Attack us with carrot?"
    show debbie e_w f_sceptical
    igor a_hand f_curious "I don't see carrot, [saga.cast.dimitri]."
    dimitri f_angry "Don't be stupid, I only make joke."
    show debbie e_r f_bored
    igor a_side e_s f_ashamed "Oh."
    show debbie e_e f_sad
    anon "I'm calling the cops!"
    show igor e_w f_calm
    dimitri a_stop "I think not!"
    show debbie f_worried_surprised
    show igor a_threat
    dimitri "Hold him."
    show debbie e_w
    show dimitri a_side
    igor "Yes, [saga.cast.dimitri]."
    show debbie a_stop p_stand_away at pos(.3)
    show igor a_side f_curious behind debbie at pos(.15)
    with dissolve.nowait
    debbie "N-no!"
    show debbie a_wtf o_right p_stand behind igor
    show igor a_hold_anon e_osw f_angry at center
    show anon e_ne f_shocked m_open p_igor_hold at pos.igor
    anon @ -m_talk "Get off me!"
    debbie a_nervous "I'll get you the money, please!"
    debbie "Don't hurt him."
    show anon e_w f_afraid m_teeth
    show debbie f_sad
    dimitri "Be silent!"
    dimitri "You had your chance."
    dimitri "Now you must pay in blood."
    hide anon
    hide dimitri
    show debbie a_shock e_wsw f_worried_surprised
    show igor a_hold_anon_dimitri_punch_face
    with dissolve.nowait
    anon "Gah!"
    show igor a_hold_anon_slump
    show dimitri a_clasp at pos(.9)
    with dissolve.nowait
    debbie e_b f_crying "[saga.cast.anon]!!!"
    dimitri "This is what happens, when [saga.cast.raz] does not get his money."
    hide dimitri
    show debbie a_cover_face
    show igor a_hold_anon_dimitri_punch_gut
    show anon e_b f_hurt m_teeth o_right of_blood_nose p_igor_hold_dimitri_punch_gut at pos.igor
    with dissolve.nowait
    anon @ -m_talk "Ugh!"
    hide anon
    show dimitri a_clasp at pos(.9)
    show igor a_hold_anon_slump
    with dissolve.nowait
    dimitri "Perhaps we kill him, and you watch, eh?"
    debbie a_nervous e_w f_sad "Stop, please!!"
    hide dimitri
    show debbie e_wsw f_worried_surprised
    show igor a_hold_anon_dimitri_punch_gut
    show anon e_b f_hurt m_teeth o_right of_blood_nose p_igor_hold_dimitri_punch_gut at pos.igor
    with dissolve.nowait
    anon @ -m_talk "Urk!"
    hide anon
    show dimitri a_clasp at pos(.9)
    show igor a_hold_anon_slump
    with dissolve.nowait
    debbie e_w f_sad "I'll do anything!"
    dimitri "Heh, indeed you will."
    show igor a_hold_anon_dimitri_grab_face
    show dimitri f_smug p_igor_hold_anon at pos.igor
    with dissolve.nowait
    dimitri e_wsw "You see, little bunny."
    dimitri "[saga.cast.raz] always gets what is owed."
    show debbie f_worried_surprised
    dimitri e_w "Perhaps he make whore of your friend, huh?"
    show debbie a_cover f_disgusted at pos(.15)
    with dissolve.nowait
    dimitri "She will repay debt on her knees, with cock in her mouth."
    show igor e_e f_smug
    pause
    igor "Heh, I like this plan, [saga.cast.dimitri]."
    show debbie f_worried_surprised
    dimitri "Come then, take off robe and let us see-"
    show debbie f_surprised
    show dimitri f_surprised
    show igor e_w f_surprised
    "*Sirens blaring*"
    show debbie f_sad
    show dimitri f_angry
    igor f_sad "The police come, [saga.cast.dimitri]."
    dimitri "Yes, I have ears, idiot!"
    igor f_curious @ e_osw "What of them?"
    dimitri "Leave them for now."
    hide dimitri
    show debbie e_wsw f_worried_surprised
    show igor a_hold_anon_dimitri_punch_gut e_osw
    show anon e_b f_hurt m_teeth o_right of_blood_nose p_igor_hold_dimitri_punch_gut at pos.igor
    with dissolve.nowait
    anon @ -m_talk "..."
    hide anon
    show debbie e_w f_sad
    show dimitri a_clasp at pos(.9)
    show igor a_hold_anon_slump
    with dissolve.nowait
    dimitri a_point "This is far from over."
    dimitri "You tell the cops of this, we fucking kill you all!"
    show anon a_hurt e_b f_hurt m_teeth o_right of_blood_nose p_stoop at pos(.6)
    show dimitri a_throat
    show igor a_side e_w f_sad
    with dissolve.nowait
    debbie a_shock f_worried_surprised @ -m_talk "!!!"
    dimitri a_side "You hear me?"
    igor "We must go, [saga.cast.dimitri]!"
    hide igor with dissolve.nowait
    dimitri e_sw f_smug "See you soon, little bunny."
    hide dimitri with dissolve
    show debbie a_gimme e_wsw f_sad oa_hand at pos(.325)
    with dissolve.nowait
    debbie "Oh, [saga.cast.anon]!"
    show debbie a_none oa_none at pos.anon.hold
    anon a_debbie_hold e_osw f_sad p_stand -m_teeth "Ugh."
    debbie "Speak to me!"
    anon "I think my nose is broken."
    show anon e_b f_hurt m_teeth
    debbie "{i}*Sniff*{/i} I'm so sorry, sweetie!"
    jenny "Are they gone?"
    show anon e_osw f_sad -m_teeth
    show debbie e_w
    show jenny a_shock f_sad at pos(.85)
    with dissolve.nowait
    jenny "Oh god, he's bleeding!"
    jenny "I called the cops like you told me."
    show jenny a_side
    debbie "I know."
    debbie "You did good, [saga.cast.jenny]."
    jenny "Is he gonna be okay?"
    debbie "Help me get him upstairs to the shower."
    jenny "The shower?"
    debbie "We can't let the police see him like this!"
    jenny @ f_confused "Why not?!"
    debbie "Just do what I ask, please!"
    debbie "Easy, sweetie."
    debbie "I've got you."

    scene mono debbie_lobby_stairs hurt
    mono "If this were a mere work of fiction, it's where I'd lean into the cliché and tell you that the real casualty in all this had been my pride." with fade
    more "No such luck."
    mono "I can still recall the stinging, fizzing pain behind my nose, my watering eyes, and the fear that just maybe my soul had been knocked out of my body at the same time as my breath."
    mono "Quite how [saga.cast.debbie] and [saga.cast.jenny] managed to get me up those stairs in that state before the cops arrived is one of life's great mysteries."

    scene debbie_bath noon -water at stage
    stop sfx 
    show anon f_sad o_right of_blood_nose at pos(.55)
    show debbie f_sad at pos.anon.touch_face
    show jenny a_fold f_sad o_right at left
    with fade
    anon "I tried to stop them."
    show anon e_osw
    debbie a_touch_anon_face "I know, sweetie."
    debbie "You were so brave."
    jenny "I can't believe they did this."
    debbie a_side "[saga.cast.jenny], I need you to go and open the door for the police."
    jenny "Okay-"
    show jenny a_side f_surprised
    debbie "Don't mention [saga.cast.anon]!"
    jenny f_sad @ -m_talk "..."
    debbie "I'll be down in a second."
    hide jenny with dissolve.nowait
    pause
    show anon e_e
    show debbie a_washcloth e_sw o_right behind anon at pos.anon.top_off
    debbie "C'mon, let's get these bloody clothes off you."
    show debbie a_gimme
    pause
    show anon a_top_off_debbie_01 c_casual_bottom
    show debbie a_none
    pause
    show debbie e_w
    anon a_top_off_debbie_02 e_b f_hurt m_teeth @ m_cough "Agh!"
    show anon a_rub
    show debbie a_side at pos(.3)
    with dissolve.nowait
    debbie "Are you alright?"
    anon a_side e_w f_sad o_left -m_teeth "Y-yeah, just really sore."
    debbie "A warm shower will help."
    debbie "I'll come back to check on you as soon as the cops leave, okay?"
    anon "Thanks, [saga.cast.debbie]."
    hide debbie with dissolve

    call shot.debbie_bath_door
    with fade
    show debbie a_clasp f_sad at right with dissolve
    debbie @ -m_talk "( I feel like I should be in there taking care of him. )"
    pause
    show debbie a_nervous at center

    if saga.cast.debbie < 'rescue':
        debbie @ -m_talk "( I can't believe he stood up to those men, for me. )"
    else:

        debbie @ -m_talk "( I can't believe I got him injured again... )"
        debbie @ -m_talk "( ... And all because of my silly pride. )"

    debbie e_e @ -m_talk "( He's grown up so quickly because everything that's happened... )"
    debbie a_embarrassed f_shy of_blush @ -m_talk "( ... And in more ways than one. )"
    debbie e_nw f_pensive @ -m_talk "( Hmm, maybe I should- )"
    show debbie a_surprised e_e f_surprised
    jenny "[saga.cast.debbie]!"
    jenny "[saga.cast.yumi] and [saga.cast.harold] are waiting down here!"
    show debbie a_side e_w f_sad o_right of_none at right
    debbie "I'm coming!"
    hide debbie with dissolve

    scene black
    with dissolve
    mono ""

    label deb18_lobby.cookie hide:
    call shot.debbie_bath_shower
    show anon a_wash c_naked_wet d_soft e_s f_worried o_right ob_soap behind glass at pos(.55)
    show steam
    with dissolve
    pause
    show anon ob_none with dissolveslow.nowait
    pause
    show anon a_nose e_osw f_sad
    pause
    anon a_smell_finger e_ssw @ -m_talk "( Well, it looks like the bleeding finally stopped. )"
    show debbie c_naked o_right behind steam at pos(.15)
    anon a_nose e_osw @ -m_talk "( Maybe it's not broken after all. )"
    show anon a_surprised d_firm e_o f_surprised
    show debbie a_wash_anon_shoulders_01 c_naked_wet d_soft e_wsw oa_hands s_1 z_b_f_a behind anon at pos.anon.wash
    show mimic debbie as debbie_hands behind glass at pos.debbie
    pause
    anon d_soft e_e "[saga.cast.debbie]??"
    anon "Why are you-"
    debbie a_wash_anon_shoulders f_shy "Shhh, It's okay, Sweetie."
    debbie "I'm just here to help you."
    show anon f_shy

    if saga.cast.debbie < 'rescue':
        debbie "You deserve it, after what you did back there."
    else:
        debbie "You deserve it, after everything you've been through."

    pause
    show anon d_firm e_s f_surprised z_b_ob_f_of_d_od
    show debbie a_wash_anon_torso e_sw
    show mimic anon as anon_arms behind glass at pos.anon
    pause
    debbie e_w "How's your head?"
    anon e_e f_shy "My ears are ringing, but I think I'll live."
    debbie e_wsw "Heh, when did my boy get so tough, huh?"
    show anon a_surprised_up_both d_hard_out e_se f_surprised
    show debbie a_hold_anon_hips e_sw at pos.anon.hold_hips
    show mimic debbie as debbie_hands at pos.debbie
    debbie "I'm so very proud of the man you're becoming."
    anon e_e f_shy "Thanks, [saga.cast.debbie]."
    pause
    debbie "Here, I know what will make you feel better."
    anon f_confused @ -m_talk "Hmm?"
    show debbie a_jerk_04 e_s oa_hand p_lean z_b_f_of
    anon a_surprised_reach d_none e_s f_surprised @ f_shocked m_open "OH!!"
    anon e_sw "R-really, you don't have to-"
    debbie "I know that, sweetie... I want to do it."
    debbie "Besides, you deserve it."
    show anon e_s f_shy
    show debbie a_jerk s_2
    pause
    anon f_horny @ e_sw "Ahh, that feels good."
    debbie f_horny "That's it, sweetie... just let me take care of you."
    debbie "Mm, my big strong boy."
    debbie "I can barely wrap my hand around it."
    anon e_sw "Y-yeah, sorry."
    show anon f_surprised
    debbie @ e_ne "There's nothing to be sorry about... I'm just admiring it."
    anon "You're admiring... m-my..."
    pause
    anon e_b f_distressed "... Oh, [saga.cast.debbie], I'm gonna-"
    debbie @ e_ne "Go ahead, sweetie..."
    debbie "... Let it out for me."
    anon "Oh, wow!"
    hide anon_arms
    hide debbie_hands
    show anon m_talk p_debbie_lean_hj_cum z_reset at pos.debbie
    show debbie a_none b_anon od_cumshot p_lean_hj_cum s_400ms z_reset
    anon "HNNGGG!!!" with flash
    debbie "That's it."
    pause
    show anon e_sw f_shy -m_talk
    debbie e_ne od_cum p_lean_hj_cum_02 "Good boy!"
    show anon a_surprised d_firm e_e p_stand at pos(.55)
    show debbie a_wash_anon_shoulders_02 e_sw f_calm oa_hands od_none p_stand z_b_f_a -b_anon at pos.anon.wash
    show mimic debbie as debbie_hands behind glass at pos.debbie
    pause
    debbie e_wsw "I'll bet you're feeling better now, aren't you, sweetie?"
    anon "So much better."
    anon "Thank you, [saga.cast.debbie]!"
    debbie "You're welcome."
    show anon e_s f_horny z_b_ob_f_of_d_od
    show mimic anon as anon_arms behind glass at pos.anon
    debbie a_wash_anon_torso e_sw f_shy "Now, let's get you cleaned up."
    $ renpy.end_replay()

    stop sfx fadeout 3.

    scene black
    with dissolve
    mono ""

    scene debbie_bath noon -water at stage
    stop sfx 
    show debbie a_towel_boobs c_naked_wet s_800ms at right
    show anon o_right p_top_on at left
    show steam
    with dissolve
    pause
    show anon a_pocket f_shy p_stand
    show debbie a_towel_cover
    pause
    show debbie a_cover c_towel_wet
    anon f_confused "[saga.cast.debbie], was this just a one-time thing?"
    debbie f_shy @ -m_talk "..."
    debbie "Oh, sweetie... I don't know."
    anon f_worried "It's alright if it is, I just-"
    debbie f_calm "I suppose, we can do it again."
    anon f_happy_surprised "Really?!"
    debbie f_worried_surprised "But you can't tell {i}anybody{/i}, okay?"
    debbie "A-and this is as far as things go... and this time I mean it!"
    show anon f_calm
    debbie f_shy "Agreed?"
    anon "Y-yeah, of course!"
    debbie f_worried_surprised "And we absolutely {i}cannot{/i} let [saga.cast.jenny] find out!"
    anon "I understand, [saga.cast.debbie]."
    debbie f_calm "Good."
    debbie "Now, I need to get dinner started."
    debbie f_shy "I want you to wait here for a few minutes before coming out of the bathroom."
    debbie "Alright?"
    anon "O-okay, [saga.cast.debbie]."
    debbie f_calm "That's my boy."
    hide debbie
    show anon o_left
    with dissolve
    pause
    anon @ e_b f_happy m_laugh "Wow!"
    anon @ -m_talk "( That was totally worth a few bruises and some head trauma! )"
    hide anon
    with dissolve
    return


label deb18_lobby.rails:
    call shot.debbie_main_drive
    show anon a_surprised_up f_worried_surprised at right with dissolve
    anon @ -m_talk "( I can't leave now. )"
    anon a_surprised f_annoyed @ -m_talk "( [saga.cast.debbie] needs me! )"
    hide anon
    with dissolve
    return


label deb18_outro:
    return


label deb18_outro.block:
    scene camera at stage
    show anon a_rub f_tired with dissolve
    anon @ -m_talk "( It's been a long night for all of us... )"
    anon @ -m_talk "( ... I should let her rest. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
