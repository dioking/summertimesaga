label jen27_intro:
    scene debbie_bed3 at stage
    show anon a_pocket f_worried with dissolve
    anon @ -m_talk "( Hmm, I just don't understand [saga.cast.jenny]... )"
    anon @ -m_talk "( Why is she so weird about our relationship? )"
    show anon a_think e_nw f_pensive
    pause
    anon a_pocket e_w f_worried @ -m_talk "( I should talk to her about it... )"
    anon @ -m_talk "( She's usually downstairs eating breakfast in the morning. )"
    hide anon with dissolve
    return


label jen27_kitchen:
    scene debbie_kitchen -debbie at stage
    show jenny a_fold f_annoyed o_right at pos(.45)
    show debbie a_mug f_sad at right
    with None
    debbie "Oh, good grief [saga.cast.jenny]..."
    debbie "I never wanted you to leave in the first place!"
    jenny e_r "Well, I want to get a place of my own, it's just..."
    jenny e_w f_sad "I'm not ready yet."
    debbie f_calm "That's perfectly fine, dear."
    debbie "You're welcome to stay here at home forever, so far as I'm concerned."
    debbie @ e_b f_happy m_laugh "God knows, I could use the help!"
    jenny f_calm "Yeah, that's exactly what I was thinking, and with my work going so well, I could probably chip in a couple hundred more a month."
    debbie "Oh, that would be wonderful, dear!"
    show anon a_pocket o_right at pos(.275)
    anon "What's going on?"
    show jenny -o_right
    debbie "Good morning, sweetie!"
    debbie "We were just talking about [saga.cast.jenny] moving out."
    anon f_shocked m_open @ -m_talk "WHAT?!"
    anon f_worried -m_open "Y-you're moving out?!"
    show jenny f_snide
    debbie @ e_b f_happy m_laugh "Oh, no, no, no!"
    debbie "I meant to say, she's not moving out."
    jenny f_calm "Yeah, I've decided to stay here a while longer."
    jenny "Save up some money, you know?"
    debbie "Isn't that wonderful, [saga.cast.anon]?!"
    anon f_calm "Y-yeah, wonderful!"
    hide jenny
    show debbie e_iw f_shy p_jenny_hug_side at pos(.6)
    show jenny b_debbie_mug f_disgusted o_right p_hug_side behind debbie at pos.debbie
    with dissolve
    debbie "I'm just so proud of you, dear!"
    jenny "T-thanks, Mom..."
    show debbie e_w f_calm -p_jenny_hug_side at pos(.7)
    show jenny f_calm -b_debbie_mug -p_hug_side at pos(.45)
    debbie "Why don't you two go have a seat at the table and I'll whip you up some eggs and bacon?"
    jenny "Alright."
    hide jenny with dissolve
    anon e_b f_happy m_laugh @ -m_talk "Mmm, that sounds great!"
    hide anon with dissolve

    call shot.debbie_dining_breakfast
    show debbie_dining_table food3 plate3 -bowl3 as table
    show jenny a_phone e_s f_annoyed p_table behind table
    with fade
    pause
    show debbie_dining_table -chair3 -chair4 -table_legs
    show anon a_pocket e_wsw f_shy p_stand_far behind jenny at pos(.7)
    show debbie_dining_table chair3 chair4 table_legs as chairs behind jenny
    with dissolve.nowait
    anon "So uhh..."
    hide chairs
    show debbie_dining_table chair3 chair4 table_legs
    show anon a_down e_e p_table at center
    anon "About last night..."
    jenny e_w "Ugh, you're not going to start in with this lovey-dovey bullshit again, are you?"
    anon "Why are you being so weird about it?"
    jenny f_angry m_teeth "Umm, you're the one being weird!"
    jenny a_spoon f_annoyed -m_teeth "I'm not interested in dating you, [saga.cast.anon]..."
    jenny "We're having phenomenal sex and making great money, why can't that be enough for you?!"
    anon "You really don't want more?"
    jenny "What, like marriage and kids?!"
    jenny "A little brick house with a white picket fence?"
    anon f_calm "... Sounds kinda nice."
    jenny f_disgusted "Eugh, don't make me barf!"
    anon f_worried @ -m_talk "..."
    show jenny f_annoyed
    show debbie_dining_table pull4
    show debbie a_potato e_wsw p_table_stand behind table
    show anon e_nw
    debbie "Alright, who's hungry?!"
    jenny f_calm "Right here!"
    debbie "What were you all talking about?"
    jenny "Nothing important."
    anon e_e @ -m_talk "..."
    anon e_nw "Actually, I've just lost my appetite."
    show anon e_e
    show debbie f_sad
    jenny f_annoyed @ e_r "Ugh, so what, now you're all mad?"
    debbie @ -m_talk "..."
    anon e_nw "Can I be excused?"
    debbie "O-of course..."
    debbie "... Is everything alright, sweetie?"
    show debbie e_w
    show debbie_dining_table -chair3
    show anon a_pocket e_w o_right p_stand_far at pos(.55)
    show debbie_dining_table chair3 pull3 as chairs behind jenny
    with dissolve.nowait
    anon f_tired "Yeah, I'm fine."
    hide anon with dissolve
    debbie e_wsw "What's going on with you two?"
    jenny "It's nothing, Mom."
    jenny "[saga.cast.anon]'s just being a big baby..."

    scene debbie_lobby at stage with fade
    show anon a_pocket f_worried at right with dissolve
    anon @ -m_talk "( Well, that could have gone better... )"
    pause
    anon f_sceptical @ -m_talk "( She's just so damn stubborn! )"
    anon @ -m_talk "( Even if she did want more, she'd never admit it. )"
    anon f_tired @ -m_talk "( {i}*Sigh*{/i} )"
    anon f_worried @ -m_talk "( I should just give her some space... )"
    anon @ -m_talk "( ... Maybe she'll come around? )"
    hide anon with dissolve
    return


label jen27_kitchen.rails:
    scene camera at stage
    show anon with dissolve
    anon @ -m_talk "( I should head down to breakfast and speak with [saga.cast.jenny]. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
