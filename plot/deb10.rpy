label deb10_lounge:
    scene debbie_lounge at stage
    show debbie_lounge desk as desk
    show anon a_pocket f_surprised behind desk with dissolve
    "*Muffled noises*"
    anon f_confused @ -m_talk "( Huh? )"
    anon a_think e_nw f_pensive @ -m_talk "( Is [saga.cast.debbie] in her room... at this time of day? )"
    anon @ -m_talk "( That's unusual. )"
    show anon e_w f_surprised
    debbie "Oh, no..."
    show anon a_side
    debbie "Ngh, we c-can't... it's so wrong!"
    anon f_confused @ -m_talk "( What the- )"
    show anon f_worried_surprised
    debbie "Ahh, please... not there!"
    anon f_worried @ -m_talk "( Sounds like she's struggling with something... )"
    anon @ -m_talk "( ... I should probably check on her! )"
    hide anon with dissolve
    return


label deb10_bed1:
    scene debbie_bed1_visit
    show debbie c_robe_open p_debbie_bed1_visit_rub
    pause
    show debbie_bed1_visit anon
    with dissolve
    anon "( WHOA!! )"
    anon "( Is she... )"
    anon "( ... No! )"
    anon "( She's masturbating!! )"
    debbie "Oh, you feel so good!"
    debbie "I can't believe I'm-"
    anon "( I didn't know landladies masturbated!! )"
    debbie "Ahh!!"
    anon "( This is so awesome! )"
    debbie "It's been so long, and you're so... big..."
    debbie "... And hard!"
    anon "( I wonder what she's thinking about? )"
    anon "( Dad, I imagine. )"
    debbie "Ngh, sweetie...."
    anon "( !!! )" with hpunch
    debbie "... R-right there!"
    anon "( Holy shit! )"
    debbie "Y-yes!!"
    debbie "Ahh, baby!!"

    call shot.debbie_bed1_door
    show anon a_door p_bend_away at pos(.35)
    with fade
    anon "( Is this really happening?! )"
    anon "( Could she really be thinking... about me?! )"
    $ renpy.end_replay()
    show jenny f_confused at right with dissolve.nowait
    jenny @ -m_talk "..."
    jenny "{i}What{/i} are you doing?!"
    show anon a_surprised_up_both f_shocked m_open o_right p_stand
    with none.nowait
    with hpunch
    anon @ -m_talk "WHA-"
    anon a_uneasy f_shy -m_open "N-no... nothing!"
    jenny f_annoyed "Don't lie!"
    jenny a_point "You're spying on my mom you little perv!"
    anon a_surrender f_worried "That's not-"
    anon "I just heard some weird noises and thought I'd better investigate."
    jenny a_hips @ e_r "Yeah, sure you did."
    show anon a_side
    jenny f_confused "What is she, changing or something?"
    anon f_shy "N-no?"
    jenny "Well, what's so interesting then?"
    show anon a_surrender e_wsw f_surprised m_teeth o_left at center
    show jenny p_bend_away at pos(.44)
    with dissolve.nowait
    jenny "Move, dummy!"
    show anon -m_teeth at pos(.65)
    with dissolve.nowait
    anon "W-wait, dont-"
    show anon a_side e_ssw
    jenny "..."
    show anon d_hard
    jenny "Eugh!"
    show anon e_w f_worried
    jenny a_surprised f_disgusted p_stand "I did not need to see that!"
    anon "I tried to warn you."
    show anon e_wsw f_confused
    jenny p_bend_away "Who flicks their bean in the middle of the day with their kid in the house?!"
    anon "Kid?!"
    anon a_wtf f_sceptical "You're twenty-two."
    jenny "So?"
    anon a_side "So you're not exactly a kid any more, are you?"
    jenny "That is so not the point..."
    pause
    show anon f_surprised
    jenny "... Geez, she's like three knuckles deep in that thing!"
    show anon e_w
    show jenny a_side f_confused o_right p_stand at pos(.375)
    with dissolve.nowait
    jenny "You really get your rocks off to this?"
    anon e_e f_shy "I mean, n-no?"

    if saga.cast.jenny < 'seen':
        show jenny a_fold f_horny
    else:
        show jenny a_touch_low f_horny

    jenny @ e_sw "Pfft, tell that to the summer sausage in your pants."
    anon a_surprised e_s f_shocked m_open @ -m_talk "( !!! )"
    show anon a_shy_down f_worried_surprised -m_open
    show jenny o_left p_bend_away at pos(.44)
    with dissolve.nowait
    jenny f_snide "Heh, you're so pathetic."
    anon e_wsw f_grumpy "You're peeking too, ya know?"
    jenny "I just think it's funny, is all."
    anon "Whatever."
    pause
    anon a_side f_worried "You're not gonna tell her... are you?"
    show jenny a_side f_confused o_right p_stand at pos(.375)
    show anon e_w
    jenny "Tell her what?"
    anon "That I was peeking on her!"
    jenny a_hips f_snide @ -m_talk "Hmm..."
    jenny "... That depends."
    anon f_worried_surprised "What do you mean, \"it depends\"?!"
    jenny "On whether or not you do what I say, when I say it."
    anon f_sceptical "What the heck does that even mean?"
    jenny "I dunno yet... You'll just have to wait and see."
    pause
    show jenny f_horny
    anon e_osw f_sad "{i}*Sigh*{/i} Alright, damnit."
    pause
    show anon a_surprised e_w f_surprised
    show jenny e_e f_surprised
    debbie "Ooohhh, {i}ooohhh, OOOOHHHH!!!{/i}"
    jenny e_b f_calm @ m_laugh "Hah!"
    jenny e_w f_snide "Sounds like she's getting close in there..."

    if saga.cast.jenny < 'seen':
        show anon a_side f_worried o_right
    else:
        show anon a_side f_shy o_right

    hide jenny
    with dissolve.nowait
    jenny "... Enjoy the rest of the show, perv!"
    anon @ -m_talk "( Man, that does not bode well for me in the future... )"
    pause
    show anon e_e f_surprised
    debbie "Yes, sweetie!! YES!!!"
    anon e_w f_horny o_left @ -m_talk "( ... But you can't get rainbows without a little rain, I suppose. )"
    show anon a_door p_bend_away at pos(.35)
    with dissolve.nowait
    anon @ -m_talk "( Good day. )"
    pause
    return


label deb10_bed1.rails:
    scene debbie_lounge at stage
    show debbie_lounge desk as desk
    show anon f_worried behind desk with dissolve
    anon @ -m_talk "( [saga.cast.debbie] is making weird noises in her room. )"
    anon @ -m_talk "( I should make sure she's alright. )"
    hide anon with dissolve
    return


label deb10_outro:
    return


label deb10_outro.block:
    scene debbie_bed1_visit
    show debbie c_robe_open p_debbie_bed1_visit_rub
    show debbie_bed1_visit anon with dissolve
    debbie "( Ahh, sweetie... )"
    debbie "( ... I'm gonna- )"
    pause
    show debbie_bed1_visit -anon with dissolve

    call shot.debbie_bed1_door
    show anon a_surprised d_hard f_shy o_right at pos(.35)
    with fade
    anon @ -m_talk "( This is all so surreal... )"
    anon e_b f_happy m_teeth @ -m_talk "( ... What a good day! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
