label deb20_lobby:
    scene debbie_lobby at stage
    show anon a_pocket e_nw f_pensive o_right with dissolve
    anon @ -m_talk "{i}*Distant voice*{/i}"
    anon @ -m_talk "( Hmm, who's [saga.cast.debbie] talking with in the kitchen? )"
    anon e_w f_confused @ -m_talk "( I should go take a look. )"
    hide anon with dissolve
    return


label deb20_kitchen:
    scene debbie_kitchen -debbie -island -stool at stage(.706, .495, 1.7, b=0)
    show diane a_wine f_curious oa_hand z_b_ob_f_of_a at pos(.87)
    show debbie a_wine f_sad o_right oa_hand z_b_ob_f_of_a
    show debbie_kitchen gap island peek as island at stage(.706, .495, 1.7, b=0)
    show mimic debbie as debbie_hand at pos.debbie
    show mimic diane as diane_hand at pos.diane
    with fade
    diane "... I'm still not seeing the problem... Isn't it a good thing that he's helping you around the house?"
    debbie "Of course it's a good thing, that's not the issue!"
    debbie "It's like he's become a completely different person since [saga.cast.frank] died."
    diane f_sad "That's not surprising, the poor boy's just lost his father..."
    diane "... You can never be sure how loss is going to affect someone."
    debbie "I understand that."
    show diane f_surprised
    debbie @ f_worried_surprised "But this is not normal [saga.cast.diane], I'm telling you!"
    debbie e_sw "Since the funeral he's been... overly affectionate... with me."
    show debbie f_shy
    diane f_curious "Overly affectionate?"
    diane "What does that even mean?"
    debbie e_w f_sad "You know what it means!"
    debbie f_worried_surprised "He dotes on me like I'm his highschool crush or something."
    diane f_ashamed "Sounds wonderful."
    debbie f_annoyed "Be serious, [saga.cast.diane], please!"
    debbie "I'm worried about him."
    show debbie f_sad
    diane @ e_r f_bored "Ugh!"
    diane f_calm "It's probably nothing..."
    diane "... I'm sure he's just feeling vulnerable after all that's happened and probably craving some familiarity."
    debbie @ e_b "It's not that."
    debbie f_worried_surprised "I get the feeling he's after something more..."
    show diane f_surprised
    debbie e_s f_shy of_blush "... Sensual."
    pause
    diane f_horny "Okay..."
    diane "... How do you mean?"
    pause
    debbie e_w "Well, for instance... a few weeks ago it started to become apparent that he was getting... well..."
    debbie "... Excited..."
    debbie "... When he was around me."
    diane "... As in?"
    debbie f_sad "Hard, [saga.cast.diane]."
    debbie f_worried_surprised "His {i}thing{/i} was getting hard whenever I was around."
    show debbie f_confused
    diane @ e_b f_shy m_laugh "Hehehe!"
    show debbie f_pensive
    diane f_curious "His {i}thing{/i}... seriously?"
    diane f_calm "Just say cock like a normal person."
    debbie @ e_r f_bored -m_talk "..."
    debbie f_sad "Anyway, then I began to notice lots of little things... a sultry look here or a familiar touch there..."
    diane f_horny "Go on."
    show diane f_surprised
    debbie f_worried_surprised "And the other day, I found him playing with himself; in my bed!"
    diane "No!"
    debbie "Yes."
    debbie "With my underwear!"
    diane @ e_b f_shy m_laugh "Hah!"
    show diane f_calm
    debbie f_pensive "It's not funny."
    diane @ f_horny "It's a bit funny!"
    diane "So, what did you do?!"
    debbie f_sad "Well, we talked about it."
    debbie "I tried explaining to him that I wasn't mad while also making it clear that he shouldn't do it again, but..."
    diane f_curious "But, what?"
    debbie f_worried_surprised "... I caught him again!"
    diane f_horny "Heh, really?!"
    debbie "Yes!"
    debbie f_sad "I was at my wits end with it!"
    debbie f_shy "But then he apologized and started talking about urges that he couldn't control..."
    show diane f_woozy
    debbie e_sw f_horny "... And how I dominated his every thought, and none of the girls his age could even hold a candle to me."
    diane "Oh, geez."
    diane "I bet you just ate that up."
    debbie e_w f_pensive @ -m_talk "..."
    diane f_horny "I'm just saying, it sounds like a line straight out of those trashy romance novels you used to read all the time."
    debbie e_b f_worried_surprised "Oh, god."
    diane "Go on, tell me what you did."
    debbie e_sw f_sad "I-"
    show diane f_curious
    debbie e_w f_shy "Well, I... kinda... posed for him..."
    pause
    show diane f_surprised
    debbie e_se "... So he could finish."
    diane "{i}*Gasp*{/i}"
    diane "You watched him masturbate?"
    show diane f_horny
    debbie e_w f_worried_surprised "I didn't know what else to do!"
    debbie f_sad "I thought maybe if he just got it out of his system..."
    debbie "... Things would just go back to normal."
    diane f_woozy "You naughty girl."
    debbie "But instead, things just spiralled even further."
    diane "I'm so proud of you right now."
    debbie f_pensive "Shut up."
    diane f_curious "So what else?"
    debbie e_b f_sad "{i}*Sigh*{/i}"
    diane f_horny "Spill it."
    pause
    debbie "We've started showering together."
    show debbie e_w
    diane f_surprised "Dang."
    pause
    diane f_pouty "So, how is he?"
    show diane f_surprised
    debbie f_worried_surprised "[saga.cast.diane]!!"
    diane e_b f_shy m_laugh @ -m_talk "Come on!"
    diane e_w f_pouty -m_laugh "Don't start acting like a prude now!"
    show diane f_horny
    debbie "That's not-"
    diane "We both know you're dying to tell me."
    show diane f_surprised
    debbie "It's not gone that far, and it never will!"
    diane f_pouty "You must have touched it."
    show diane f_horny
    debbie @ e_r f_bored "Ugh!"
    debbie f_pensive "Yes, okay, I did."
    diane "I knew it!"
    debbie e_se f_shy "I kinda... jerked him off."
    diane @ f_woozy "All the way?"
    debbie "Until he came, yeah."

    if saga.cast.diane < 'grope':
        pause
        diane @ f_pouty "So, seriously... how is it?"
        debbie e_w f_confused "How is what?"
        show debbie f_surprised
        diane "His {i}dick{/i}, [saga.cast.debbie]!"
        diane @ f_pouty "Is it big?"
        debbie e_se f_shy @ -m_talk "..."
        diane "Don't get shy on me now, girl... spit it out!"
        debbie e_w "[saga.cast.diane], he's got the biggest... {i}cock{/i} I've ever seen!"
        diane @ f_pouty "Hmm, you don't say."

    diane "I'm surprised you stopped there."
    debbie e_w f_worried_surprised of_none "[saga.cast.diane], he's barely old enough to vote!"
    diane @ f_pouty "Pfft, like that matters."
    debbie "I'm old enough to be his mother!"
    diane "But you're {i}not{/i} his mother, [saga.cast.debbie]!"
    debbie f_sad "Ugh, I dunno, [saga.cast.diane]..."
    debbie e_sw "... It just makes me very uncomfortable."
    diane f_curious "What are you so bent out of shape about?"
    diane f_calm "He's a big boy and capable of making his own decisions."
    debbie e_w "Please, tell me I'm not doing something terribly wrong here."
    diane "I mean, it's your decision, but..."
    diane f_happy "... If it were me, I'd go for it."
    debbie f_surprised "Really?"
    diane "Yeah, who cares about the age difference?"
    debbie f_sad "You don't think it's wrong?"
    diane f_calm "Not in the slightest."
    show debbie f_shy
    diane "As far as I can see, you're both consenting adults and what you do in the privacy of your home is nobody's business but your own."
    show debbie f_pensive
    diane f_horny "Though, I hope you'll continue to gossip about it with your poor old divorced best friend and top-tier confidante [saga.cast.diane]."
    show debbie f_surprised
    diane @ f_woozy "She could really use the spank bank material."
    show diane e_b f_shy m_laugh
    debbie @ e_r f_bored "Tsk, you're terrible!"
    show debbie f_shy
    pause
    show diane e_w f_calm -m_laugh
    debbie e_sw "It's just so... wrong."
    diane "Oh, pish posh with all that!"
    show debbie e_w
    diane "I know you've got your panties in a bunch about it being immoral and all..."
    diane "... But that's only going to make it feel better!"
    debbie a_wine_facepalm e_b "Ugh, you are such a bad influence... Why do I listen to you?"
    diane f_happy "Because you know I've got your best interest in mind."
    debbie a_wine e_w f_sad "I don't want to ruin what we have."
    diane f_calm "I'm certain you won't..."
    diane "... And who knows, this could end up being the exact thing you both need to get through all this awfulness that's surrounding you."
    debbie f_shy "Yeah, maybe you're right."
    diane f_happy "I believe I am."
    pause
    show diane a_wine_drink p_stand_drink z_b
    pause
    diane a_wine_empty p_stand z_b_ob_f_of_a @ f_pouty "Oof."
    diane f_calm "And with that... I'd best be getting home!"
    diane "It's late."
    hide diane_hand
    show diane a_gimme e_sw o_right oa_none z_reset
    debbie f_calm "Why don't you come by for dinner sometime?"
    debbie "I'd love to see you more often, and I'm sure the kids would too!"
    diane a_side e_w f_horny o_left "Heh, that might be true for [saga.cast.anon] but the only person [saga.cast.jenny] likes seeing is herself in the mirror."
    debbie @ e_r f_bored "Oh, don't start!"
    diane f_calm "I'm just saying, that girl needs a reality check."
    show debbie f_happy
    diane f_horny "But also, yes, on the dinner."
    diane "You know I can't say no to your cooking."
    debbie "I'll make your favorite."
    show debbie a_none b_none e_b m_laugh oa_none
    show diane b_debbie p_kiss_cheek at pos.debbie
    diane "Mwah."
    show diane p_stand -b_debbie at pos(.65)
    show debbie a_wine e_w f_shy oa_hand -b_none -m_laugh
    diane "Good luck, honey."
    show diane e_e at pos(.325)
    with dissolve.nowait
    debbie e_e "G-good night."

    call shot.debbie_lobby_stairs
    show debbie_lobby -debbie_kitchen
    show anon a_surprised_up_both f_surprised m_teeth o_right at left
    with fade
    anon @ -m_talk "( Crap! She's headed this way, time to bail! )"
    show anon o_left p_run_away
    pause
    hide anon with dissolve
    pause
    show diane f_horny o_right at pos(.65)
    with dissolve.nowait
    pause
    hide diane
    with dissolve

    scene debbie_landing at stage
    show anon a_tired f_confused p_bend
    with fade
    anon "Haah... haah..."
    anon a_hips e_b f_calm m_drink p_stand @ -m_talk "( Phew, that... was a lot to take in! )"
    anon a_side e_sw f_confused o_right -m_drink @ -m_talk "( [saga.cast.debbie] seems really conflicted about everything we've been doing together. )"
    anon f_happy @ -m_talk "( But she also seems to be enjoying it. )"
    anon a_think f_pensive @ -m_talk "( I wonder if [saga.cast.diane]'s encouragement will have an affect on her? )"
    hide anon with dissolve
    return


label deb20_kitchen.rails:
    scene debbie_lobby at stage
    show anon a_think e_nw f_pensive o_right with dissolve
    anon @ -m_talk "( I wonder who [saga.cast.debbie] is talking to? )"
    hide anon with dissolve
    return


label deb20_outro:
    return


label deb20_outro.debbie:
    scene debbie_yard_pool_edge
    show debbie a_down e_sw f_horny ob_pool_water p_sit_edge_bend at right
    pause
    show anon o_right p_stand_legs at pos(y=.775), blur(20), zoom(.775) with dissolve.nowait
    anon @ -m_talk "( After what I just witnessed, maybe now isn't the time. )"
    anon @ -m_talk "( Better to give [saga.cast.diane]'s words some time to sink in. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
