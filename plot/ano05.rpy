label ano05_dimitri:
    scene mono debbie_main_car1
    mono "Hmm, why is that car driving so slow?" with fade
    mono "Wait a second..."

    scene mono debbie_main_car2
    mono "It's that creepy guy with the strange accent who was making the threats!" with fade
    mono "This is bad!"

    scene debbie_main at stage(.57, .65, 3.0)
    show anon f_surprised o_right at pos(.55)
    with fade
    anon "I need to tell [saga.cast.debbie] about this!"
    anon "Right now!"
    hide anon
    with dissolvefast

    scene debbie_lobby -debbie at stage with fade
    show anon f_surprised at right with dissolvefast
    anon "[saga.cast.debbie]!"
    pause
    anon a_uneasy "Where are you?!"
    show debbie a_mug f_sad o_right at left with dissolvefast.nowait
    debbie "Sweetie?!"
    debbie "What's the matter?"
    anon a_side "I just saw that guy again!"
    debbie a_shock f_surprised "Y-you did?"
    debbie "Where?!"
    anon f_worried @ a_point_back "He and another guy just drove by in a black car."
    debbie a_mug f_sad "Did they say anything to you?"
    anon "No, they just kept on driving."
    anon "He was staring right at me though!"
    debbie "I think we'd better stay inside the house for a while..."
    debbie "... I'll go phone the police."
    anon "Y-yeah, okay."
    hide debbie
    with dissolve
    pause
    anon f_angry @ -m_talk "( I'm getting really sick of these assholes. )"
    hide anon
    with dissolve

    scene debbie_kitchen -debbie at stage
    show debbie a_phone_talk f_sad at right
    with fade
    debbie "Yes, just now."
    pause
    show anon a_pocket f_worried o_right at pos(.45) with dissolve
    debbie "No, they didn't stop."
    pause
    debbie "A-alright."
    pause
    debbie "Thank you."
    show debbie a_phone_side
    pause
    anon "What did they say?"
    debbie "[saga.cast.yumi] is on her way over."
    anon "Have they made any progress?"
    debbie "She didn't say."
    anon f_pouty @ a_facepalm "Of course she didn't."
    anon "You know, I'm starting to think the cops in this town are pretty useless..."
    debbie "Don't say that, sweetie."
    show anon f_worried
    debbie "They're doing their best."
    show jenny a_fold f_annoyed o_right at pos(.15) with dissolve
    anon "Yeah, a lot of good that's doing us."
    show anon e_e
    jenny "Now what's happening?"
    jenny "Those creepy guys come by again?"
    anon "Yes."
    show anon e_w
    debbie "I'm sure it's nothing, dear..."
    debbie "The police are on their way, everything is going to be fine."
    debbie "We just need to stay inside for a while."
    show anon e_e
    jenny "Are they going to actually do something this time?"
    show anon e_w
    debbie "Don't you start too."
    pause
    debbie "Why don't you take [saga.cast.anon] upstairs and play a board game or something?"
    show anon e_e
    jenny f_disgusted "Eugh, you must be joking..."
    show anon e_w
    debbie "No, I think it would be good if you two spent some time together bonding."
    show anon e_e
    jenny f_annoyed @ e_r "First of all, we're not little kids... we don't play board games."
    anon f_confused "You don't want to play a board game?"
    anon f_calm "I'd play a board game."
    jenny @ a_facepalm "{i}*Sigh*{/i} Secondly, I'd rather coat my labia in honey and sit on an anthill."
    show anon e_nw f_pensive
    debbie f_annoyed "[saga.cast.jenny]!"
    anon e_e f_horny "That was oddly specific."
    show anon e_w f_calm
    show jenny f_horny
    debbie "... And disgusting."
    show anon e_e
    jenny "Maybe, but it's true."
    jenny f_annoyed "I'm going upstairs to watch a movie."
    hide jenny
    with dissolve
    jenny "Don't bother me!"
    pause
    show anon e_w
    debbie f_calm "Well, you can wait here with me if you'd like?"
    debbie "I'll cook you something."
    anon "Nah, that's okay [saga.cast.debbie]."
    anon "I'll just head to my room and catch up on some homework or something."
    debbie "Oh, that's a good idea!"
    show debbie b_anon p_hug_away at pos.anon
    show anon p_debbie_hug_away
    debbie "You're such a good boy!"
    anon "Y-yeah, thanks [saga.cast.debbie]."
    show debbie a_clasp -b_anon -p_hug_away at right
    show anon -p_debbie_hug_away
    debbie "I'll whip you up something to snack on!"
    anon "Sounds great."

    scene mono debbie_study_day
    mono "I had a literal mountain of homework piled up from the time I missed at school..." with fade
    mono "... But try as I might, I just couldn't get anything accomplished."

    scene mono intro5
    mono "I was too worried to focus." with fade
    mono "How had my dad managed to get us into this mess?!"
    mono "What in the world could I do to get us out of it?"

    scene debbie_bed3 t1 at stage
    show debbie a_mug f_sad o_right at left
    with fade
    debbie "Sweetie?"
    debbie "It's awfully quiet in here..."
    show anon a_pocket f_worried at right with dissolve
    anon "Are the police still downstairs?"
    debbie "Just [saga.cast.yumi]."
    debbie "She's gonna stick around while the patrols are out looking for that car."
    anon @ e_osw f_sad "Yeah, great."
    pause
    show debbie at pos(.35)
    debbie "Are you doing okay?"
    anon "Ehh, I'm fine."
    debbie "You sure?"
    debbie "I hope you know you can talk to me... if you need to?"
    anon "Y-yeah, I know."
    pause
    anon "I just-"
    anon "I'm worried something bad might happen and..."
    anon "... I want to be able to protect you and [saga.cast.jenny], you know."
    show debbie b_anon e_sw p_hug_lean at center
    show anon e_s p_debbie_hug_lean at pos.debbie
    debbie "Ahh, sweetie."
    debbie "It's not your responsibility to protect us."
    debbie "You've got enough worries, just being the age you are..."
    debbie "... Getting through school..."
    debbie "... Finding a nice girlfriend..."
    show anon e_w -p_debbie_hug_lean at right
    debbie e_w -b_anon -p_hug_lean "You should focus on things like that, you know?"
    anon "I'm not sure I can do that, [saga.cast.debbie]."
    debbie f_calm "Tsk, of course you can!"
    debbie "All this other stuff... it's for me to solve, not you."
    debbie "It's my responsibility."
    debbie "You hear me?"
    anon "Yes."
    anon "B-but I don't think-"
    show anon e_nw p_debbie_hug_lean at pos.debbie
    debbie b_anon e_sw p_hug_lean "No buts!"
    debbie "I'm gonna take care of it, okay?"
    debbie "Everything is going to be fine."
    show anon e_w -p_debbie_hug_lean at right
    show debbie e_w -b_anon -p_hug_lean
    pause
    debbie "Why don't you get out of the house for a while and do something fun?"
    debbie "Go see what new games [saga.cast.erik] is playing?"
    anon @ -m_talk "..."
    debbie "Maybe spend some time with that cute girl next door?"
    anon a_uneasy f_shy "[saga.cast.debbie]..."
    debbie @ e_b f_happy m_laugh "Hehe, or you could always go help [saga.cast.diane] with her garden."
    anon a_pocket "{i}*Sigh*{/i} Yeah, alright."
    debbie "That's my boy!"
    hide anon
    show debbie -o_right
    with dissolve
    debbie "Get your mind off all this nonsense!"
    pause
    debbie a_nervous f_sad "I'll handle everything."
    show debbie a_facepalm e_b
    pause

    call shot.debbie_main_mailbox
    show debbie_main t1
    with fade
    show anon at pos(.3) with dissolve
    anon @ -m_talk "( [saga.cast.debbie] is right, it doesn't do any good to sit around worrying about this stuff. )"
    anon @ -m_talk "( Best I get my mind off it. )"
    anon e_b f_happy m_teeth @ -m_talk "( I've got the whole town full of adventures in front of me. )"
    hide anon
    with dissolve
    return


label ano05_outro:
    return


label ano05_outro.block:
    scene debbie_main at stage
    show anon f_happy with dissolve
    anon @ -m_talk "( [saga.cast.debbie] is right, I've got a whole world to explore out here! )"
    anon @ -m_talk "( No sense wasting time sitting around the house. )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
