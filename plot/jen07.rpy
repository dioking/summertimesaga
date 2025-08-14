label jen07_intro:
    jump jen03_intro


label jen07_intro.bed2:
    call shot.debbie_bed2_door
    show anon a_wtf e_r f_bored o_right with dissolve
    anon @ -m_talk "( Oh yeah, sure, because it turned out so great the last time. )"
    anon a_pocket e_w f_tired -o_right @ -m_talk "( That'll be a hard no. )"
    hide anon with dissolve
    return


label jen07_dining:
    call shot.debbie_dining_breakfast
    show debbie_dining_table food3 plate3 -bowl3 as table
    show jenny a_phone e_s p_table behind table
    pause
    show debbie_dining_table -chair3 -chair4 -table_legs
    show anon a_pocket e_wsw f_shy p_stand_far behind jenny at pos(.7)
    show debbie_dining_table chair3 chair4 table_legs as chairs behind jenny
    with dissolve.nowait
    anon "Morning."
    hide chairs
    show debbie_dining_table chair3 chair4 table_legs
    show anon a_bowl e_e p_table at center
    with dissolve
    pause
    show anon a_eat e_s f_calm m_bite
    pause
    anon a_down e_e f_grumpy v_chew -m_bite "Hello?!"
    jenny f_annoyed "Hmm, what?!"
    anon "What's your problem?"
    jenny "Nothing, leave me alone."
    anon a_bowl e_s f_shy v_normal @ -m_talk "..."
    pause
    show anon a_eat f_calm m_bite
    jenny @ e_r "Ugh, this stupid Sluttygram thing is a waste of time!"
    anon a_down e_e f_surprised v_chew -m_bite "Those pictures didn't help?"
    jenny "They did but it's just not making me enough money..."
    anon f_calm v_normal "Yeah, well, Sluttygram is pretty small potatoes compared to what's out there..."
    jenny e_w "What do you mean?"
    anon "You do realize that porn exists, right?"
    jenny "Yeah, so?"
    anon "Why would anyone pay good money to look at sexy photos with no nudity when they can watch hardcore porn, for free?!"
    jenny e_r "Umm, I dunno... How about because I'm hot and those porno skanks aren't?!"
    show jenny e_w
    anon @ e_b f_happy m_laugh "You're joking, right?"
    jenny f_angry m_teeth "No, shut up!"
    show anon f_surprised
    show debbie_dining_table pull2
    jenny f_annoyed p_table_rise -m_teeth "Don't pretend like you don't think I'm hot!"
    anon @ -m_talk "..."
    show anon e_o
    jenny f_angry m_teeth "Say it!" with hpunch

    menu:
        "Fine. {color=7ff7}[[Submissive]{/color}":
            pass
        "Screw you. {color=f77b}[[Dominant]{/color}":

            jump jen07_dining.alt

    anon e_e f_worried "You're hot."
    jenny a_fold f_annoyed "Damn right!"
    show debbie_dining_table -pull2
    show jenny a_phone e_s p_table -m_teeth
    with dissolve
    show anon a_bowl e_s f_shy
    pause
    show anon a_eat f_calm m_bite
    pause
    anon a_down e_e f_grumpy v_chew -m_bite "But it's still small potatoes."
    show anon e_s f_calm
    jenny "Yeah, yeah..."
    show anon a_bowl f_shy v_normal
    pause
    show anon a_eat f_calm m_bite
    jenny @ e_r "Grr, I need more money!!!"
    show anon a_down v_chew -m_bite
    pause
    show anon a_bowl f_shy v_normal with dissolve
    show jenny e_w
    pause
    jenny "Come with me."
    anon a_down e_e f_worried "Huh, where?"
    jenny "To my room, dummy."
    jenny "I've got a proposition for you."
    show debbie_dining_table pull2
    hide jenny
    with dissolve.nowait
    anon e_w "Uhh, okay."
    anon @ -m_talk "( I hope I didn't piss her off... )"
    show debbie_dining_table pull3
    show debbie_dining_table -plate3 as table
    hide anon
    with dissolve
    pause
    return +1


label jen07_dining.alt:
    show anon a_eat e_s f_calm m_bite
    pause
    anon a_down e_e f_grumpy v_chew -m_bite "Wow, are you that desperate for attention?"
    jenny a_fold f_confused -m_teeth "What?!"
    jenny f_annoyed "That's not-"
    show jenny f_angry m_teeth
    pause
    jenny "SHUT UP!"
    anon f_calm v_normal "Heh and you call me pathetic..."
    jenny @ -m_talk "Grrr!!"
    hide jenny with dissolve
    show anon a_bowl e_s
    pause
    show debbie_dining_table pull4
    show debbie a_potato e_wsw f_sad p_table_stand behind table
    with dissolve
    debbie "What's gotten into her this morning?"
    anon a_down e_nw f_worried "Who knows?"
    debbie "This whole job business must really be stressing her out."
    anon "Yeah, maybe."
    debbie "Poor thing."
    debbie "Here's some more breakfast, sweetie."
    show anon e_sw f_surprised
    show debbie e_sw f_calm p_table_bend
    pause
    show debbie e_wsw p_table_stand
    anon e_nw f_shy "Thanks, [saga.cast.debbie]!"
    anon "I uh-"
    anon "{i}*Ahem*{/i} C-could I have a bit more?"
    debbie "Of course."
    show anon e_sw f_surprised
    debbie e_sw p_table_bend "My little man can have as much as he wants!"
    anon f_horny "Mmm, those look wonderful..."
    show debbie e_wsw p_table_stand
    anon e_nw f_shy "... You're the best."
    debbie "Aww, thanks sweetie!"
    show anon a_bowl e_s
    hide debbie
    with dissolve
    pause
    anon f_worried @ -m_talk "( I should probably go and check on [saga.cast.jenny]... )"
    anon @ -m_talk "( I wasn't trying to be mean, she just really knows how to push my buttons. )"
    anon f_shy @ -m_talk "( Not until after I eat this delicious breakfast though! )"
    show anon a_eat f_calm m_bite
    pause

    scene black
    with dissolve
    return -1


label jen07_dining.debbie:
    call shot.debbie_kitchen_hob
    show anon at right with dissolve
    anon "Mmm, mmm..."
    show debbie_kitchen pan
    show debbie a_side o_right -p_stand_away
    anon "... That smells delicious [saga.cast.debbie]!"
    debbie "Heh, yours is already on the table, sweetie."
    anon "Oh, man... You're the best!"
    hide anon
    with dissolve
    show debbie_kitchen -pan
    show debbie a_pan p_stand_away -o_right
    with dissolve
    return


label jen07_dining.rails:
    scene camera at stage
    show anon with dissolve
    anon @ -m_talk "( I should go see what [saga.cast.debbie] is cooking up for breakfast. )"
    hide anon
    with dissolve
    return


label jen07_bed2:
    call shot.debbie_bed2_jenny

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen07_bed2.alt

    show jenny a_phone e_ssw f_snide o_right with none.nowait
    show anon a_pocket f_worried o_right at left with dissolve
    anon "Listen, [saga.cast.jenny] I wasn't trying to-"
    jenny a_hips e_w f_annoyed -o_right "Just shut up..."
    jenny "I've got a proposition for you."
    anon "Okay, what?"
    jenny f_snide "You're a horny little loser, right?"
    anon a_uneasy f_shy "What?! N-no..."
    jenny a_fold f_annoyed "And I need money, so..."
    pause
    jenny @ e_r "... How about you pay me two hundred dollars and I let you look at my tits?"
    anon a_side f_sceptical "Two hundred dollars?!"
    anon f_worried "I dunno, that's a lot..."
    jenny "Okay, but we're talking like actual, real tits here."
    jenny "Not anime tits like you're used to, loser."
    anon f_pouty "I've seen real tits."
    jenny @ e_r "Yeah, sure ya have..."
    jenny "... Can you pay or not?"

    label jen07_bed2.merge1:
    if saga.cast.anon.cash < 200:
        anon a_pocket f_worried "No."
        jenny "Well, I'm not showing you my tits for anything less than two hundred."
        jenny "So you'd better go get it if you want a look..."
        anon e_osw f_sad "{i}*Sigh*{/i} Fine."
        anon e_w f_tired "I'll get it."
        jenny "Hurry up, loser."
        jenny "I need that money!"
        hide anon
        with dissolve.nowait
        anon "Yeah, yeah."
        return

    anon a_think @ e_nw f_pensive -m_talk "..."
    anon f_snide "Fine."
    show anon a_cash f_worried at pos(.375)
    show jenny a_fold f_calm
    anon "Here."
    show anon a_pocket f_calm
    show jenny a_money_count e_ssw f_snide
    pause
    show jenny a_hips

    if saga.cast.jenny < 'deal':
        jenny e_r f_annoyed "I should have asked for three hundred..."
        show jenny e_w f_disgusted
        pause
        jenny f_annoyed "{i}*Sigh*{/i}"

    jenny "I hope you can appreciate how lucky you are."
    show jenny e_ssw f_snide p_top_off_01
    pause
    show anon e_wsw
    show jenny p_top_off_02
    pause
    show anon e_sw f_surprised
    show jenny p_top_off_03 with dissolve
    show jenny p_top_off_04
    anon @ -m_talk "!!!"
    show jenny a_hip e_w p_grope
    anon d_hard f_horny z_b_f_a_d "Wow..."
    jenny "Tuck your tongue back into your mouth, nerd!"
    pause
    show jenny e_wsw f_surprised
    pause
    jenny "I... T-that's..."
    pause
    anon "They're so-"
    jenny e_w f_snide "Beautiful."
    show anon a_surprised_up_both -z_b_f_a_d
    jenny "I know."
    show anon a_none behind jenny at pos.jenny.grope_touch
    jenny a_up b_anon f_surprised p_grope_touch_01 "!!!" with hpunch
    show anon a_surprised_up_both e_w f_surprised
    jenny a_cover c_casual_pants_up f_angry m_teeth p_twist_turn -b_anon "Hey, no touching!"
    show jenny a_clench c_casual_pants p_grope
    anon a_uneasy f_worried "Sorry, I didn't mean to-"
    jenny a_hip f_annoyed -m_teeth "Pathetic little losers don't get to touch!"
    show anon a_side e_sw f_surprised
    jenny p_top_off_01 "I think that's enough..."
    show jenny a_hips -p_top_off_01
    anon e_w f_grumpy "Aww, c'mon!"
    jenny "No, you've looked plenty."
    jenny f_snide "You want to look again, you know the price."
    anon d_none f_worried "Two hundred?"
    jenny "That's right."
    jenny f_annoyed "Now get out."
    hide jenny with dissolve
    pause
    show anon f_confused o_left at left
    anon "Aww, man..."
    hide anon with dissolve
    $ renpy.end_replay()

    call shot.debbie_bed2_door
    show anon a_pocket f_happy with dissolve
    anon @ -m_talk "( Wow, she's got like, the best tits in the world. )"
    anon f_horny_smug @ -m_talk "( I wish I could have touched them properly... )"
    anon @ -m_talk "( Maybe next time? )"
    hide anon
    with dissolve
    return True


label jen07_bed2.alt:
    show jenny o_right with none.nowait
    show anon a_pocket f_worried o_right at left with dissolve
    anon "Listen, [saga.cast.jenny] I wasn't trying to-"
    hide jenny
    show jenny e_ssw f_snide p_top_off_01 at right
    with dissolve
    pause
    show jenny p_top_off_02
    show anon e_wsw f_confused
    pause
    show anon e_sw f_surprised m_teeth
    show jenny p_top_off_03
    with dissolve
    show jenny p_top_off_04
    anon @ -m_talk "!!!" with hpunch
    show jenny a_hip e_w f_annoyed p_grope
    anon e_w @ f_shocked m_open "W-what are you doing?"
    jenny "Tell me these aren't the hottest pair of tits you've ever seen?!"
    show anon e_sw -m_teeth
    pause
    anon f_shy @ e_w "Y-yeah..."
    anon d_hard z_b_f_a_d "{i}*Gulp*{/i} Those are really nice!"
    jenny "That's what I thought."
    pause
    show jenny e_wsw f_surprised
    pause
    jenny "Fuck! That's..."
    pause
    jenny e_r f_annoyed "... I should have made you pay for this."
    show jenny e_w
    anon f_worried "I'll pay you."
    jenny f_surprised "Hmm?"
    anon f_horny "If you let me touch them."
    jenny e_r f_annoyed "Yeah, right!"
    jenny e_w "In your dreams, loser!"
    anon e_w f_pouty @ -m_talk "..."
    show jenny f_confused
    anon e_e -o_right "Fine."
    show jenny f_sad
    hide anon
    with dissolve
    pause
    jenny "Wait!"
    pause
    show anon a_pocket d_hard f_horny_smug o_right z_b_f_a_d at left with dissolve.nowait
    jenny f_annoyed "Two hundred."
    anon f_worried "What?"
    jenny "Two hundred and you can touch them."
    anon f_horny "Alright."
    show anon e_sw
    jenny e_r "I cannot believe I'm doing this..."
    jenny e_w "... You're lucky I need the money."
    pause
    jenny "You can afford it, right?"

    label jen07_bed2.merge2:
    if saga.cast.anon.cash < 200:
        anon f_worried "No."
        jenny @ f_disgusted "Ugh, seriously?!"
        jenny "Well, you're definitely not touching them for free!"
        anon e_w f_shy "Cut me a deal?"
        jenny "No way!"
        jenny "If you think I'm letting you touch them for anything less than two hundred, you're nuts!"
        anon f_worried @ -m_talk "..."
        anon "{i}*Sigh*{/i} Fine."
        anon "I'll get it."
        jenny "Hurry up, loser."
        jenny "I need that money!"
        hide anon
        with dissolve.nowait
        anon "Yeah, yeah."
        return

    show jenny a_fold f_calm p_stand
    show anon a_cash e_w at pos(.375)
    anon "Here."
    show anon a_pocket
    show jenny a_money_count e_ssw f_snide
    pause
    show jenny a_hips

    if saga.cast.jenny < 'deal':
        jenny e_r f_annoyed "I should have asked for three hundred..."
        show jenny e_w
        anon f_snide "Too late now."

    show anon e_sw f_horny
    show jenny e_ssw f_snide p_top_off_01
    pause
    show jenny p_top_off_02
    pause
    show jenny p_top_off_03 with dissolve
    show jenny p_top_off_04
    pause
    jenny a_hip e_w f_annoyed p_grope "Just hurry up."
    show anon a_none f_surprised behind jenny at pos.jenny.grope_touch
    show jenny b_anon p_grope_touch s_800ms
    pause
    anon "Wow!"
    anon "They're so soft!"
    jenny e_r "Well yeah, dummy."
    show jenny e_w
    pause
    jenny a_up f_sad s_600ms "Mmm, be careful!"
    jenny "My nipples are sensitive!"
    pause
    hide anon
    jenny a_clench e_b f_nervous p_grope_suck s_400ms "!!!" with hpunch
    jenny e_ssw f_worried_surprised "I never said you could-"
    jenny e_b f_nervous m_talk "Ahh!"
    pause
    jenny e_s m_lip @ -m_talk "Fffffuu-"
    pause
    show anon a_surprised_up_both f_surprised o_right at pos(.475)
    jenny a_cover c_casual_pants_up e_w f_sad p_twist_turn -b_anon -m_lip "Stop!"
    jenny "It's too much, I can't..."
    show anon a_side f_horny_smug
    pause
    jenny f_annoyed "Ugh, you're such a pervert!"
    anon f_smug "You liked it."
    jenny "N-no, I didn't!"
    anon @ e_b f_happy m_laugh "Liar."
    jenny "Just get out."
    anon "Fine."
    anon a_wave "Pleasure doing business with you, [saga.cast.jenny]."
    hide anon
    with dissolve.nowait
    jenny "Shut up!"
    $ renpy.end_replay()

    call shot.debbie_bed2_door
    show anon a_pocket f_horny_smug with dissolve
    anon @ -m_talk "( Wow, she's got like, the best tits in the world. )"
    anon @ -m_talk "( I can't believe she's letting me touch them! )"
    anon @ -m_talk "( This is awesome! )"
    hide anon
    with dissolve
    return True


label jen07_bed2.rails:
    scene camera at stage
    show anon with dissolve
    anon @ -m_talk "( I should check on [saga.cast.jenny]. )"
    hide anon
    with dissolve
    return


label jen07_jenny:
    anon f_worried "Can I see your tits?"
    jenny f_annoyed "I dunno, do you have two hundred dollars?"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen07_bed2.merge2

    jump jen07_bed2.merge1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
