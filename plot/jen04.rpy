label jen04_landing:
    scene debbie_landing dark at stage
    show anon a_pocket f_worried o_right at left with dissolve
    anon @ -m_talk "..."
    anon @ -m_talk "( What's that light coming out of [saga.cast.jenny]'s room? )"
    pause
    anon @ f_sceptical -m_talk "( She must be on her computer or something... )"
    mans_voice "You like that don't ya, you little whore?!"
    show anon f_surprised
    jenny "Mmm, yeah I do!"
    mans_voice "Didn't I tell you to call me Daddy?!"
    jenny "I'm sorry, Daddy!"
    anon @ f_worried -m_talk "( What the- )"
    mans_voice "Do you think this big cock is gonna fit up your tight little asshole?!"
    jenny "Ahh, I dunno Daddy..."
    anon @ -m_talk "( Does she have somebody in there?! )"
    mans_voice "Well, you're about to find out... Get on your knees, bitch."
    jenny "Ngghhh, yes Daddy!"
    anon @ -m_talk "( Okay, I have to peek now! )"
    return


label jen04_bed2:
    scene debbie_bed2_jenny_porn -chair
    show jenny p_debbie_bed2_jenny_porn
    show debbie_bed2_jenny_porn chair as chair
    anon "( Phew, there's no guy in here... )"
    anon "( She's just watching porn. )"
    pause
    anon "!!!" with hpunch
    anon "( Whoa, I didn't know [saga.cast.jenny] watched porn! )"
    jenny "Ngghh!! Give it to me Daddy!"
    jenny "Please!!!"
    anon "{i}*Snort*{/i}"
    anon "( Dang, she's into some freaky- )"
    show jenny e_c f_surprised p_debbie_bed2_jenny_porn_turn
    anon "!!!" with hpunch
    jenny f_angry "OH MY GOD!"
    jenny "ARE YOU SPYING ON ME AGAIN?!"
    $ renpy.end_replay()

    call shot.debbie_bed2_door
    show anon a_pocket f_surprised m_teeth o_right at left
    with fade
    show jenny a_upset f_angry m_teeth at pos(.67) with dissolve.nowait
    jenny "What did I tell you!"
    anon -m_teeth "I'm sorry!"
    jenny "About spying on me!"
    show jenny a_dryer_hit_01 with dissolve
    show jenny a_dryer_hit_02
    anon a_cower p_bow "Ouch!!"
    jenny a_dryer_hit_01 "You freaking loser!"
    show jenny a_dryer_hit_02
    pause
    show jenny a_dryer_hit_01
    anon "Would you cut it out!"
    jenny a_upset @ -m_talk "..."
    anon a_pocket f_sceptical -p_bow "Sheesh, where do you keep pulling these hair dryers from anyways?!"
    show anon f_worried
    jenny "I'm telling Mom!"
    show jenny o_right at pos(.8)
    anon f_surprised "What?!"
    anon f_worried "No, no, no, please!!"
    show jenny a_fold -o_right at pos(.67)
    anon "Don't tell [saga.cast.debbie]!"
    show anon f_surprised m_teeth
    show jenny a_hips f_snide -m_teeth
    pause
    jenny "One hundred bucks."
    anon -m_teeth "What?!"
    jenny "Give me one hundred dollars or I'm telling my mom, right now!"
    anon f_worried "Seriously?!"
    pause
    anon f_sceptical "You're out of your mind if you think I'm gonn-"
    show jenny o_right at pos(.8)
    show anon f_surprised
    jenny "Mom!"
    anon a_surrender f_worried_surprised "Okay, okay, stop!"
    show jenny -o_right at pos(.67)

    if saga.cast.anon.cash > 99:
        anon a_side f_worried "Jesus..."
        pause
        anon a_cash "{i}*Sigh*{/i} Here."
        show anon a_pocket
        show jenny a_money_count e_ssw

    elif saga.cast.anon.cash:
        anon a_side e_osw f_sad "I don't even have one hundred."
        jenny "Then give me what you do have!"
        anon a_cash_bills e_w f_tired "{i}*Sigh*{/i} Here."
        show anon a_pocket
        show jenny a_money_count e_ssw
    else:

        anon a_wtf f_annoyed "I don't even have any money."
        jenny f_disgusted @ -m_talk "..."
        show anon a_side f_confused
        jenny f_annoyed "You're pathetic..."

    pause
    anon f_worried "So you're not gonna tell [saga.cast.debbie], right?"

    if saga.cast.anon.cash > 99:
        show jenny e_w f_snide
    else:
        show jenny e_r f_annoyed

    jenny "Not this time."

    if saga.cast.anon.cash > 99:
        jenny "Pleasure doing business with you, perv."
    else:
        jenny e_w f_angry m_teeth "Get some money, perv."

    hide jenny
    with dissolve
    pause
    anon f_tired @ -m_talk "( Phew, that was close! )"
    pause

    if saga.cast.anon.cash > 99:
        anon f_pouty @ -m_talk "( ... And expensive, damn it! )"

    anon @ -m_talk "( I have got to be more careful. )"
    hide anon
    with dissolve
    return


label jen04_bed2.rails:
    scene debbie_landing at stage
    show anon a_surprised f_surprised o_right at left with dissolve
    anon @ -m_talk "( Does [saga.cast.jenny] have some guy over? )"
    anon @ -m_talk "( I've gotta check this out! )"
    hide anon
    with dissolve
    return


label jen04_outro:
    return


label jen04_outro.block:
    scene debbie_landing at stage
    show anon a_pocket f_snide o_right at left with dissolve
    anon @ -m_talk "( I'd best leave her and \"Daddy\" alone. )"
    anon f_worried_surprised @ -m_talk "( Not too keen to take another beating from that hairdryer. )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
