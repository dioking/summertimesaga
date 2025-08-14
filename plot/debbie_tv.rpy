label debbie_tv:
    return


label debbie_tv.auth:
    scene debbie_tv
    anon "( !!! )"
    anon "( It worked! )"
    return


label debbie_tv.boot:
    scene debbie_tv
    anon "( Hmm... Let's see what's on TV. )"
    return


label debbie_tv.dark:
    scene debbie_lounge at stage
    show anon a_pocket f_tired o_right at left with dissolve
    anon @ -m_talk "( I don't have the energy... I think I should go to bed. )"
    hide anon with dissolve
    return


label debbie_tv.dead:
    scene debbie_tv
    anon "( This channel's a dud. )"
    return


label debbie_tv.debbie:
    show anon a_jerk_01 e_w f_surprised m_talk p_couch_side_turn
    with none.nowait
    debbie "[saga.cast.anon]?" with hpunch
    anon e_s p_couch_side -m_talk @ -m_talk "( Oh, crap! )"
    anon e_e f_worried p_couch_side_twist_hide @ -m_talk "( [saga.cast.debbie] is coming! )"
    show debbie_lounge_couch_side open
    show debbie a_doorframe f_worried p_couch_side_door behind couch at default, blur(10), tint('00106545')
    show anon c_casual e_nw f_afraid m_teeth p_couch_side_hide at tint('00106545')
    with dissolve.nowait
    debbie "Is somebody out here?!"
    show debbie a_side f_confused p_stand at pos.couch_side_behind_walk, blur(5), noop
    debbie "Hello?!"
    debbie f_curious o_right "Oh, they left the TV-"
    show debbie a_embarrassed f_surprised at pos.couch_side_behind_end, blur(None), tint(None)
    debbie @ -m_talk "!!!"
    show anon f_confused -m_teeth
    debbie "Oh, my."
    pause
    debbie a_clasp f_confused "Who in the world was-"
    show debbie f_surprised
    pause
    show debbie_lounge_couch_side as couch behind debbie
    show debbie e_n f_curious o_left p_couch_side_squat_tilt at reset
    pause
    show debbie a_side p_couch_side_lean_tilt
    pause
    show anon f_surprised
    debbie f_concerned "Wow, they're really going at it..."
    pause
    debbie "I shouldn't be watching this!"
    show anon f_worried_surprised
    debbie e_e f_shy p_couch_side_lean_turn "[saga.cast.anon] or [saga.cast.jenny] could walk in here any second!"
    show debbie a_remote e_n f_concerned p_couch_side_lean_tilt
    pause
    show anon f_worried
    show layer master at darken, tint('00106545')
    with dissolvefast.nowait
    pause
    show debbie p_couch_side_walk_off
    pause
    show debbie p_couch_side_door_away behind couch at blur(10)
    pause
    show anon e_b f_calm m_smoke
    show debbie_lounge_couch_side -open
    hide debbie
    with dissolve
    pause

    scene debbie_lounge at stage with fade
    show anon a_surprised f_worried at right with dissolve
    anon @ -m_talk "( That was close! )"
    anon a_rub f_shy @ -m_talk "( I'd better just go to bed... )"
    hide anon with dissolve
    return


label debbie_tv.jenny:
    show jenny e_se f_annoyed o_right behind couch at pos.couch_side_behind_far, blur(7.5), tint('00106545')
    show anon a_jerk_01 e_w f_surprised m_talk p_couch_side_turn
    jenny "Surprise, perv!" with hpunch
    show jenny a_hips e_wsw f_snide o_left at pos.couch_side_behind_end, blur(None), tint(None)
    show anon a_cover e_s p_couch_side -m_talk
    pause
    anon e_e f_worried "You scared me!"

    if 'build' < saga.cast.diane < 'barn':
        jenny "Where's [saga.cast.diane]?"
        anon "I dunno, she must be working late or something..."

    show debbie_lounge_couch_side as couch behind jenny
    show jenny a_side e_w f_annoyed p_couch_side_sit at reset
    show anon f_surprised
    jenny "Who said you could use my Pink Channel account?"
    show jenny e_e
    anon f_worried "I didn't think you would mind-"
    jenny "Ugh, lesbians..."
    jenny e_w f_snide "Don't you think that's kinda boring?"
    anon f_shy "Not really."
    jenny "It just seems kinda pointless when there's no dick involved..."
    anon @ -m_talk "..."
    show jenny e_wsw f_surprised
    show anon f_worried
    pause
    show anon e_s
    jenny "Oh my god, were you jerking it?!"
    show jenny f_horny
    anon e_e "N-no..."
    jenny e_w "Yes, you were."
    jenny @ e_b f_calm m_laugh "Look at your dick, it's rock hard!"
    anon @ -m_talk "..."
    jenny "You know, if you ask me real nice... I might just help you out with that."
    anon "R-really?"
    jenny "Yeah, but only if you beg me for it."

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon "Screw you!"
        jenny f_annoyed "What?!"
        anon "I'm not begging you for anything."
        jenny f_angry m_teeth "Don't talk to me like that!"
        anon "Shh, you're going to wake up [saga.cast.debbie]!"
        jenny @ -m_talk "Grr!"
        anon a_jerk_01 e_s "Just go away and let me finish."
        show anon a_jerk e_n f_calm p_couch_side_tilt s_4
        jenny e_wsw f_angry_pouty -m_teeth @ -m_talk "..."
        jenny e_w f_annoyed "You are such an asshole!"
        anon @ e_e f_worried p_couch_side "You're the one who's trying to make me beg for it!"
        jenny "Whatever."
        show jenny e_wsw f_disgusted
        pause
        jenny f_annoyed "{i}*Sigh*{/i}"
        jenny "Here..."
        show jenny a_rub f_horny z_b_ob
        show mimic jenny at pos.jenny
        anon a_side e_s f_surprised p_couch_side @ -m_talk "!!!" with hpunch
        anon e_e "I thought you didn't want to-"
        jenny "Just shut up!"
        jenny "I walked all the way down here, I might as well have some fun."
        show anon e_s f_shy
        pause
    else:

        anon @ -m_talk "..."
        anon "P-please?"
        jenny @ e_r f_annoyed "Oh c'mon, that was pathetic!"
        anon @ -m_talk "..."
        jenny "Say this:"
        jenny "\"Please, Princess [saga.cast.jenny].\""
        anon "Please, Princess [saga.cast.jenny]."
        jenny "\"I know, I'm just a pathetic little loser...\""
        anon "{i}*Sigh*{/i} I know, I'm just a pathetic little loser..."
        jenny "\"... Not even worthy of your feet.\""
        anon "... Not even worthy of your feet."
        jenny @ e_b f_calm m_laugh "Hahahaah!"
        anon "Shh, you're going to wake up [saga.cast.debbie]!"
        jenny "Yeah, yeah... alright, get it out, loser."
        show jenny e_wsw
        show anon a_side d_hard e_s
        pause
        show jenny a_rub z_b_ob
        show anon d_none f_shy
        show mimic jenny at pos.jenny
        with dissolve

    jenny "How does that feel?"
    anon @ e_e "So good!"
    pause
    jenny e_w "You are such a pervert, you know that?"
    jenny "Getting off to my feet?"
    anon e_e "This was your idea..."
    jenny @ e_b f_calm m_laugh "Hahahaah!"
    show jenny e_wsw
    show anon e_s
    jump jen20_jenny.loop1


label debbie_tv.pink:
    scene debbie_tv
    anon "( Man, I wish I could access this channel. )"
    return


label debbie_tv.play:
    scene debbie_tv
    anon "( Oooh, lesbians! )"

    menu:
        "Have some fun.":
            pass
        "Maybe later.":

            return

    anon "( Hmm, I should probably wait until [saga.cast.debbie] is asleep. )"
    anon "( Maybe there's something good I can watch in the meantime. )"
    show tv info 02 as num at tv_info
    show tv wrestle1
    with fadefast.aux
    anon "( Nice! Chicas Luchadoras Televisión! )"
    anon "( This'll work, it's a re-run but such a fun match. )"
    show tv wrestle2
    anon "( But I always feel a little bad for Toxic Terror... )"

    scene black
    with dissolve
    mono ""
    debbie "Do you want dinner, honey?"
    anon "{i}Zzzzz...{/i}"
    debbie "Oh, I'm sorry, enjoy your nap."
    mono ""

    scene debbie_tv
    show tv wrestle3
    with dissolve
    anon "{i}*Yawn*{/i}"
    anon "( Huh, I must have been more tired than I realised... )"
    show tv wrestle4
    anon "( It's crazy how one-sided this match is. Cyclone is merciless! )"

    scene black
    with dissolve
    mono ""
    debbie "Goodnight, [saga.cast.anon], sleep well."
    mono ""

    scene debbie_tv dark
    show tv wrestle5
    with dissolve
    anon "{i}*Yawn*{/i}"
    anon "( So much power in those thighs... )"
    show tv wrestle6
    anon "( Utterly dominated. )"
    pause
    anon "( It's pretty late, [saga.cast.debbie] should definitely be asleep by now. )"
    anon "( Time for some fun! )"
    show tv info as num at tv_info
    show tv lesbian
    with fadefast.aux
    label debbie_tv.cookie hide:
    anon "( Wow... that same pair of girls are still going?! )"

    call shot.debbie_lounge_side
    show anon d_hard e_n p_couch_side_tilt
    with fade
    anon @ -m_talk "( This is the perfect opportunity to rub one out! )"
    show anon a_bottom_down_01 d_none e_s f_shy p_couch_side
    pause
    show anon a_bottom_down_02 with dissolve
    show anon a_jerk c_casual_down e_n f_calm p_couch_side_tilt
    pause
    anon s_4 @ -m_talk "( Damn these chicks are hot! )"
    anon e_b f_shy m_lip s_6 @ -m_talk "( I'm getting close! )"
    return True


label debbie_tv.solo:
    anon a_cumshot s_400ms @ -m_talk "HNNGGG!!!" with flash
    pause
    anon @ -m_talk "( Phew, that felt awesome! )"
    show anon e_n f_calm -m_lip
    pause
    anon e_s f_shy p_couch_side @ -m_talk "( I guess I'd better go and get cleaned up. )"
    hide anon with dissolve
    return


label debbie_tv.soon:
    scene debbie_lounge at stage
    show anon a_pocket e_nw f_pensive at right with dissolve
    anon @ -m_talk "( Urgh! Daytime TV? But I'm not sick... )"
    anon e_w f_worried @ -m_talk "( And I can't watch porn during the day, [saga.cast.debbie] could catch me. )"
    anon e_o f_surprised @ -m_talk "( I am {i}not{/i} having that conversation again! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
