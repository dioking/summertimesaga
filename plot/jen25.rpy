label jen25_lobby:
    scene debbie_lobby -debbie at stage
    show anon a_pocket o_right at left with dissolve
    debbie "Sweetie, could you come in here for a second?"
    show anon f_surprised
    pause
    anon f_calm "Sure."

    call shot.debbie_kitchen_hob
    show debbie_kitchen pan
    show debbie a_mug o_right -p_stand_away
    with fade
    show anon a_pocket at pos(.6) with dissolve.nowait
    anon "What's up, [saga.cast.debbie]?"
    debbie "Would you mind poking your head outside and asking [saga.cast.jenny] if she wants some of this breakfast?"
    anon f_worried "Ehh, I don't mind."
    anon "She's just gonna say no..."
    debbie @ e_b f_happy m_laugh "Hehe, probably."
    show debbie b_anon e_sw p_hug_lean at pos(.4)
    show anon e_s p_debbie_hug_lean at pos.debbie
    debbie "Thanks, sweetie."
    anon @ e_nw "No problem."
    show debbie e_w -b_anon -p_hug_lean at pos(.275)
    show anon a_side e_w f_calm -p_debbie_hug_lean at pos(.6)
    pause
    hide anon with dissolve
    show debbie_kitchen -pan
    show debbie a_pan p_stand_away -o_right
    with dissolve
    return


label jen25_jenny:
    call shot.debbie_yard_jenny
    show jenny f_calm with none.nowait
    show anon a_wave at right with dissolve
    anon "Good morning."
    jenny "Hey."
    pause
    show jenny a_side e_se f_surprised
    anon a_uneasy e_se f_surprised @ -m_talk "..."
    jenny @ -m_talk "..."
    anon a_point e_w f_shy "You want me to move that umbrella so you can get some sun?"
    jenny e_w f_confused "What?"
    show anon a_side
    jenny e_sw f_calm -o_right "Oh, nah..."
    anon f_worried "B-but-"
    jenny e_b m_laugh o_right @ -m_talk "I'm not out here to tan, you dork..."
    jenny e_w -m_laugh "Just trying to relax."
    anon f_calm "Oh."
    jenny e_r f_annoyed "Besides, I don't tan."
    show jenny e_w f_calm
    anon f_worried "N-no?"
    jenny "I just burn."
    anon e_b f_happy m_laugh @ -m_talk "Heh, me too."
    show anon e_w f_calm -m_laugh
    pause
    anon f_worried "So, uhh... [saga.cast.debbie] wanted me to ask you-"
    show jenny f_confused
    anon f_surprised @ -m_talk "..."
    show anon a_point f_sceptical
    jenny e_sw f_annoyed "What are you-"
    show jenny e_w
    anon "Who's that?"
    jenny -o_right @ -m_talk "Hmm?"

    scene mono debbie_yard_bubbles1
    mono "The interloper in the hedge seemed visibly alarmed as [saga.cast.jenny] turned to focus on him." with fade

    call shot.debbie_yard_jenny
    show jenny f_angry m_teeth -o_right
    show anon f_surprised at right
    with fade
    jenny "Again, you creepy motherfucker?!"
    jenny "This is the third time, this month!"
    jenny "My boyfriend is gonna kick your stalker ass!"

    scene mono debbie_yard_bubbles2
    mono "His alarm rapidly turned to panic, and he started to flee!" with fade

    call shot.debbie_yard_jenny
    show jenny f_angry m_teeth
    show anon f_surprised at right
    with fade
    jenny "Don't just stand there, go punch that guy!"
    anon a_think "D-did you just call me your boyfriend?"
    jenny f_disgusted -m_teeth "Seriously?!"
    jenny f_angry m_teeth "There's some pervert spying on me and you're worried about that?!"
    anon a_surprised "R-right... Sorry."
    jenny "Hurry up before he gets away!"
    hide anon with dissolve

    scene mono debbie_yard_bubbles3
    mono "I rushed to the spot where the stalker had been, but he was already well on his way." with fade
    mono "He was faster than he looked... and there was no way I was going to catch him."

    scene debbie_main -debbie_mail at stage(.9, .65, 5)
    show anon a_tired f_worried m_talk o_right p_bend at right
    with fade
    anon "Haah... Haah..."
    show jenny c_swim f_angry m_teeth o_right at pos(.4) with dissolve
    jenny "Where is that bastard?!"
    anon "He took off..."
    jenny e_r f_annoyed -m_teeth "Ugh, damn it!"
    show jenny e_w
    anon a_side f_confused -m_talk -p_bend "Who was that guy?!"
    show anon -o_right
    jenny "I dunno, just some weirdo who keeps spying on me when I'm out by the pool..."
    show anon f_worried
    pause
    jenny "Man, I'd like to teach that creep a lesson!"
    show jenny f_angry_pouty
    pause
    show anon a_pocket f_horny
    show jenny f_disgusted
    pause
    jenny f_annoyed "Why are you looking at me like that?!"
    anon e_b f_happy m_teeth @ m_laugh "You called me your boyfriend."
    jenny a_fold "Oh my god..."
    jenny "I was just trying to scare that guy off!"
    show jenny f_disgusted
    anon e_w -m_teeth "Hehe, sure you were..."
    jenny a_upset e_r f_annoyed "Ugh, in your dreams, loser."
    hide jenny with dissolve
    anon "Well, that's not a very nice thing to say to your boyfriend..."
    jenny "Screw you, [saga.cast.anon]!"
    anon @ e_b m_laugh "Hahahaah!"
    pause
    anon e_sw f_surprised @ -m_talk "( Hmm? )"
    show anon a_reach e_s f_calm m_talk p_bend at pos(.6)
    pause
    anon a_stub e_sw f_surprised -m_talk -p_bend "( I guess it's some promotional thing from the local theater... )"
    anon f_sceptical o_right @ e_w -m_talk "( I wonder if that guy dropped it? )"
    show anon f_pensive
    pause
    anon @ -m_talk "( Perhaps, I'll find him there? )"
    hide anon with dissolve
    return


label jen25_jenny.rails:
    scene camera at stage
    show anon a_think e_nw f_pensive o_right with dissolve
    anon @ -m_talk "( I promised [saga.cast.debbie] that I'd ask [saga.cast.jenny] about wanting breakfast. )"
    anon f_worried @ -m_talk "( Even though we both know she's going to say no. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
