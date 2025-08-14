label jen09_kitchen:
    scene debbie_kitchen -debbie at stage
    show debbie a_mug at right
    show jenny a_fold o_right at pos(.4)
    with None
    debbie "Well, of course I'm happy that you're gonna start contributing, dear."
    debbie "I'm just curious about this new job you've got?"
    jenny e_r f_annoyed "Ugh, it's nothing special..."
    show jenny e_w f_calm
    debbie "Transcribing, you said?"
    jenny "Yeah."
    debbie "What are you transcribing?"
    jenny "I dunno, Mom..."
    pause
    jenny "... Customer service calls and stuff."
    debbie @ e_b f_happy m_laugh "Oh, that's neat!"
    jenny "Not really..."
    jenny "... It pays though."
    show anon a_pocket o_right at left with dissolve.nowait
    debbie "Well, I'm proud of you, dear."
    jenny e_r f_annoyed "Uh huh."
    show jenny e_w f_calm
    anon "What's going on?"
    debbie "[saga.cast.jenny] was just telling me about her new job."
    anon f_sceptical "Oh, really?"
    show anon f_snide
    show jenny f_angry m_teeth -o_right
    debbie "She's transcribing things over the internet."
    anon "You don't say..."
    debbie "It sounds really interesting."
    jenny f_calm o_right -m_teeth "It's not."
    debbie "Why don't you come have breakfast with [saga.cast.anon] and me?"
    debbie "You can tell us all about it."
    jenny f_annoyed "Ehh, no thanks."
    jenny "I need a shower."
    hide jenny
    with dissolve
    pause
    debbie @ f_shy "Oh, well... okay, dear."
    show debbie at center
    debbie "You'll join me, won't you [saga.cast.anon]?"
    anon f_calm "Yeah, of course."
    show anon e_s f_worried p_debbie_hug_lean at pos.debbie
    debbie b_anon e_sw p_hug_lean "Aww, you're such a good boy!"
    anon e_nw "Heh, thanks, [saga.cast.debbie]."
    anon "You go on ahead, I'll be right there."
    debbie "Okay, sweetie."
    show anon e_w -p_debbie_hug_lean at left
    hide debbie
    with dissolve
    pause
    show anon f_snide -o_right
    pause
    anon @ -m_talk "( Transcribing, huh? )"
    anon @ -m_talk "( She's so full of crap... )"
    anon @ -m_talk "( ... And she's lying to [saga.cast.debbie] about it. )"

    menu:
        "Let it go. {color=7ff7}[[Submissive]{/color}":
            pass
        "Confront her. {color=f77b}[[Dominant]{/color}":

            jump jen09_kitchen.alt

    anon a_think e_nw f_pensive o_right @ -m_talk "( Hmm, whatever. )"
    anon a_pocket e_w f_worried @ -m_talk "( {i}*Sigh*{/i} I probably shouldn't worry about it too much. )"
    anon @ -m_talk "( I mean, at least she's giving money to [saga.cast.debbie] again... )"
    anon @ -m_talk "( That's the important thing. )"
    debbie "Sweetie, are you coming?"
    anon f_calm "Yup!"
    anon @ -m_talk "( I should head to the dining room and join [saga.cast.debbie] for breakfast. )"
    hide anon
    with dissolve
    return +1


label jen09_kitchen.alt:
    show anon f_worried
    show debbie a_mug
    debbie "Sweetie, are you coming?"
    anon o_right "Actually, I just remember something I need to do."
    debbie f_sad "Oh."
    anon "Rain check?"
    debbie f_calm "Sure!"
    anon @ f_calm "Thanks, [saga.cast.debbie]."
    hide debbie
    with dissolve
    anon @ -m_talk "( [saga.cast.jenny] said she was heading upstairs to take a shower. )"
    anon @ -m_talk "( I should hurry if I wanna catch her! )"
    hide anon
    with dissolve
    return -1


label jen09_debbie:
    scene black
    with dissolve
    mono ""

    call shot.debbie_dining_breakfast
    show debbie_dining_table coffee food3 plate3 -bowl2 -bowl3 -milk as table
    show debbie a_down p_table behind table
    show anon a_down p_table behind table
    with dissolve
    anon "Mmm, that was so good [saga.cast.debbie]!"
    anon "You're the best cook in the whole world!"
    debbie @ e_b f_happy m_laugh "Aww, hehe!"
    debbie "Thanks, sweetie."
    anon "You want help with the dishes?"
    debbie "Oh, no..."
    debbie "I can handle it just fine. Don't you worry!"
    debbie "I'm in such a good mood, now that [saga.cast.jenny] found herself a job."
    debbie "I was so worried about her!"
    anon @ e_b f_happy m_laugh "Heh, yeah."
    debbie "Transcribing..."
    debbie "I didn't know she had it in her!"
    anon f_worried "Uh huh..."
    show anon e_s f_shy
    debbie "Oh, listen to me blathering on."
    debbie "I'm sure you have a million things you'd rather do than listen to me."
    anon e_w f_worried "No, not at all!"
    anon f_calm "I enjo-"
    debbie "You just run along now and have a good day, alright?"
    pause
    anon "Okay."
    pause
    anon "Thanks again for breakfast."
    debbie "My pleasure, sweetie."
    show debbie_dining_table pull3
    hide anon
    with dissolve
    pause

    scene debbie_lobby at stage
    show anon a_pocket f_worried o_right at left
    with fade
    anon @ -m_talk "( I can't believe [saga.cast.debbie] bought that transcribing story... )"
    pause
    anon a_think e_nw f_pensive @ -m_talk "( Hmm, I wonder what [saga.cast.jenny] is really up to? )"
    hide anon
    with dissolve
    return


label jen09_debbie.rails:
    scene debbie_kitchen at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( I should hurry along to the breakfast table. )"
    anon f_happy @ -m_talk "( [saga.cast.debbie] is waiting for me. )"
    hide anon
    with dissolve
    return


label jen09_jenny:
    scene debbie_landing at stage
    show jenny at left
    show anon a_pocket f_snide behind jenny with dissolve.nowait
    anon "You liar!"
    jenny a_hips f_annoyed o_right "Excuse me?!"
    anon "I know you're not transcribing online."
    jenny "Yeah, right. You don't know anything..."
    anon "Well, I know you're lying to [saga.cast.debbie]!"
    jenny "Why don't you just mind your own business, loser?!"
    anon @ -m_talk "..."
    anon f_worried "I just hope you're not doing something you're gonna regret for that money."
    jenny e_r "Ugh, whatever."
    show anon a_up f_surprised m_teeth
    show jenny a_wave_off e_w at pos(.35)
    jenny "Get out of my way, I'm taking a shower!"
    show anon f_worried o_right -m_teeth
    hide jenny
    with dissolve
    pause
    anon a_pocket @ -m_talk "( Hmm, she's hiding something for sure and I'm going to find out what! )"
    hide anon
    with dissolve
    return


label jen09_jenny.rails:
    scene camera at stage
    show anon f_snide with dissolve
    anon @ -m_talk "( I'd better hurry upstairs if I wanna confront [saga.cast.jenny]. )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
