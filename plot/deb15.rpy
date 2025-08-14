label deb15_intro:
    call shot.debbie_bath_door
    show anon a_pocket f_shy o_right with dissolve
    anon @ -m_talk "( Hey, it looks like someone's in the bathroom... )"
    anon @ -m_talk "( ... I hope it's [saga.cast.debbie]! )"
    anon f_horny @ -m_talk "( Let's just have us a quick peek, shall we? )"
    hide anon with dissolve
    return


label deb15_bath:
    call shot.debbie_bath_peek
    stop sfx 
    show debbie_bath -water
    show layer master at blur(20)
    show debbie c_naked_wet o_right p_towel_hair behind steam at pos(.6)
    anon "( Hmm, it's so steamy... )"
    anon "( I can't quite make out- )"
    show layer master at reset
    with dissolve.nowait
    anon "( Man, she's sexy. )"
    anon "( Just look at those curves! )"
    anon "( Perfect. )"
    pause
    show debbie a_towel_boobs e_s p_stand
    anon "( I wonder how she'd react if I went in there right now? )"
    anon "( Given recent events, would she be okay with it? )"
    pause
    show debbie p_towel_legs s_800ms
    anon "( Oh, what if she let me help her dry off? )"
    anon "( That could be super hot. )"
    anon "( She might even let me jerk off to her body again! )"

    if _in_replay:
        jump deb15_bath.fast

    menu:
        "Go inside.":
            pass
        "Leave.":

            jump deb15_bath.bail

    label deb15_bath.fast hide:
    anon "( Argh, I can't resist... I'm going in! )"
    hide gap
    with dissolve
    show anon a_pocket e_sw f_horny o_right behind steam at left with dissolve.nowait
    anon "H-hey, [saga.cast.debbie]."
    show anon a_surprised e_w f_surprised
    show debbie a_wtf e_w f_surprised o_left p_stand at right
    debbie "{i}*Gasp*{/i} Sweetie!!"
    show anon e_wsw
    show debbie a_reach e_ssw f_worried_surprised p_bend
    pause
    debbie a_towel_cover e_wnw "W-what are you doing?!"
    show anon a_rub e_w f_worried_surprised
    debbie e_w of_blush p_stand "You can't just barge in here like that!"
    show debbie a_cover c_towel_wet f_sad
    with dissolve.nowait
    anon "N-no?"
    anon a_cover_face e_b f_distressed o_left "Sorry, I just thought-"
    debbie @ f_sceptical "What if [saga.cast.jenny] saw you?!"
    anon @ -m_talk "..."
    debbie "{i}*Sigh*{/i} Look, [saga.cast.anon]... I know we've lost our heads a few times now and done some {i}things{/i} we shouldn't have..."
    debbie "... But that doesn't mean all our boundaries are suddenly thrown out the window!"
    anon "Yeah, no... you're right."
    debbie "You can't just do as you'd like and think everything will be okay!"
    anon "I'm really sorry, [saga.cast.debbie]."
    anon "I'll just... umm..."
    hide anon with dissolve.nowait
    anon "... S-sorry!"
    debbie a_facepalm e_b @ -m_talk "( Sheesh, he's really getting bold. )"
    pause
    debbie a_cover e_w f_sceptical @ -m_talk "( Maybe I should put a stop to all this? )"
    debbie f_sad @ -m_talk "( But then he might get all angsty again. )"
    debbie e_sw @ -m_talk "( Tsk, I've made a mess of everything, haven't I? )"
    $ renpy.end_replay()

    call shot.debbie_bath_door
    with fade
    show anon a_cover_face e_b f_distressed with dissolve
    anon @ -m_talk "( Crap, that was a terrible, {i}terrible{/i} idea... )"
    anon a_rub e_osw f_sad @ -m_talk "( ... What the heck was I thinking?! )"
    pause
    anon a_facepalm @ -m_talk "( Ugh, I hope I haven't just ruined everything we had going! )"
    hide anon with dissolve
    return True


label deb15_bath.bail:
    anon "( I probably shouldn't. )"
    anon "( I don't want her to be upset. )"
    pause
    return


label deb15_bath.view:
    call shot.debbie_bath_peek
    stop sfx 
    show debbie_bath -water
    show layer master at blur(20)
    show debbie c_naked_wet o_right p_towel_legs s_800ms behind steam at pos(.6)
    pause
    show layer master
    with dissolve.nowait
    pause
    return


label deb15_outro:
    return


label deb15_outro.block:
    call shot.debbie_bath_door
    show anon a_pocket f_surprised m_teeth o_right with dissolve
    anon @ -m_talk "( Don't be dumb! )"
    anon f_worried_surprised -m_teeth @ -m_talk "( Going back in there now would only make things worse. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
