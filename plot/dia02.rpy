label dia02_diane:
    scene diane_yard -diane at stage
    show diane a_shovel_hip at right
    show old_anon 203 at old_left with dissolve
    diane "Oh, there you are. Thank goodness!"
    diane "I was starting to think you weren't coming by today."
    show old_anon 2
    anon "Hi, [saga.cast.diane]!"
    anon "Is everything alright?"
    show old_anon 203
    diane "Everything's fine. You've been doing a great job with my garden, [saga.cast.anon]!"
    diane "In fact, you're doing so well, that we have a ton of leftover waste!"
    show old_anon 17
    anon "Sorry about that. Haha."
    show old_anon 203
    diane "No need to be sorry, handsome!"
    diane "I just need help moving it."
    diane "I loaded it all up in this wheelbarrow..."
    diane "... But I'm afraid it's too much for my poor back."
    label dia02_diane.merge:
    diane "Do you think you could help me out?"
    show old_anon 14
    anon "Of course!"
    anon "That's why I'm here!"
    show old_anon 13
    diane "Just be careful, it's really heavy!"
    show old_anon 2
    anon "No problem!"
    anon "I'll take care of it!"

    if saga.cast.anon.str < 2:
        jump dia02_diane.fail

    show old_anon 255 with dissolve.nowait
    anon "There we go."
    anon "See, I can handle it!"
    show old_anon 254
    diane e_b f_shy m_laugh of_blush @ -m_talk "!!!" with hpunch
    diane @ -m_talk "Wow... You lifted it like it was nothing!"
    show diane e_w f_horny -m_laugh
    pause
    show old_anon 254
    diane of_none "Strong and handsome..."
    diane "I bet you have to fight those young girls at school off with a stick, don't you?!"
    show old_anon 255
    anon "Hah, no... Not really."
    show old_anon 254
    diane e_b f_shy m_laugh @ -m_talk "Oh, come now! I don't believe that for one second!"
    diane e_w f_horny -m_laugh "In my younger years, I'd have been all over you in an instant!"
    show old_anon 255
    show old_xtra 21 at old_left with dissolve
    anon "Hehe."
    anon "I uhh..."
    anon "... Where would you like me to dump this?"
    show old_anon 254
    diane "Hmm?"
    diane e_n f_calm m_talk "Oh, right!"
    diane e_w -m_talk "Just follow me, handsome."
    diane "I keep a compost heap just over here, behind the house."
    show old_anon 255
    hide old_xtra with dissolve
    anon "Compost?"
    anon "Like, garbage?"
    show old_anon 254
    diane e_b f_shy m_laugh @ -m_talk "What? Hehe, no!"
    diane e_w f_calm -m_laugh "Compost is a valuable resource for a gardener, [saga.cast.anon]!"
    diane "All that organic matter decomposes and creates a nutrient rich fertilizer for the soil."
    show old_anon 255
    anon "Really? So it helps the plants grow?"
    show old_anon 254
    diane "That's right!"
    diane "It's what makes my vegetables so..."
    diane f_horny "Girthy."
    show old_anon 255
    anon "Awesome!"
    anon "I'm learning so much from you, [saga.cast.diane]!"

    scene mono diane_dumping
    mono "The compost pile behind her house was so far! I barely made it; the wheelbarrow kept slipping out of my hands."
    mono "It felt good though, moving all that waste for [saga.cast.diane]. ... And I was learning a lot about gardening!"

    scene diane_yard -diane at stage
    show old_anon 18 at old_left
    show diane a_shovel_hip e_b f_shy m_laugh of_blush at right
    with fade
    diane @ -m_talk "I can't believe you did it with such ease!"
    show old_anon 17
    show diane e_w f_calm -m_laugh
    anon "It was pretty hard, actually. Haha!"
    show old_anon 203
    diane of_none "Well, I sure am glad you were here..."
    diane "I don't know what I would have done without you!"
    show old_anon 2
    anon "It's no big deal."
    anon "I like the exercise!"
    show old_anon 203
    diane f_pouty m_talk "I bet you do..."
    diane "... You must exercise all the time."
    show old_anon 11
    show diane f_horny -m_talk
    anon "..."
    show old_anon 21
    anon "What do you mean?"
    show old_anon 13
    diane e_b f_shy m_laugh @ -m_talk "C'mon, what's your secret? You're so lean and fit!"
    show old_anon 11
    diane e_ne f_pensive -m_laugh @ -m_talk "I try to stay active as often as possible but I can't seem to get rid of all this fat."
    show old_anon 10
    show diane e_w f_calm
    anon "Fat?! What fat?"
    show diane f_surprised
    show old_anon 29 with dissolve
    anon "You look great, [saga.cast.diane]."
    show diane a_shovel_cheek e_b f_shy m_laugh with dissolve
    show old_anon 13 with dissolve
    diane @ -m_talk "Aww. You say that now. But if you saw me without clothes on, you'd be singing a different tune!"
    show old_anon 11
    show diane e_w f_surprised of_blush -m_laugh
    anon "..."
    diane a_shovel_hip e_b f_shy m_laugh @ -m_talk "Err... Anyway!"
    diane e_w f_pouty m_talk of_none "... You gonna tell me your trick or not?"
    diane "Have you been working out?"
    show old_anon 21
    show diane f_horny -m_talk
    anon "A little."
    show old_anon 35
    anon "I try going to the gym sometimes."
    show old_anon 13
    diane f_calm "Really?!"
    diane "That's great!"
    diane a_shovel_finger e_b "You know, there are many good advantages to staying in shape."
    show diane a_shovel_hip e_w f_pouty m_talk with dissolve
    show old_anon 11
    diane "Women love guys who are lean, strong, and full of vigor."
    show diane f_horny -m_talk
    anon "..."
    diane "Let's see that six-pack!"
    show old_anon 22
    anon "!!!" with hpunch
    show old_anon 21
    anon "You want to see my..."
    show old_anon 11
    diane "Your abs! Yes."
    diane "Give this old lady a show!"
    show old_anon 10
    anon "O-okay..."
    show diane f_surprised
    show old_anon 249 with dissolve
    diane a_shovel_cheek e_b f_shy m_laugh @ -m_talk "Whooo!"
    diane a_shovel_hip e_w f_horny -m_laugh "Look at that sexy body!"
    diane f_pouty m_talk "How can you not be popular with the girls at school?"
    show old_anon 250
    show diane f_horny -m_talk
    anon "Heh, I dunno..."
    show diane f_surprised
    hide anon
    show old_anon 108 at left
    anon "There are guys much bigger than me at school."
    anon "I'm definitely not one of the cool guys..."
    show old_anon 109
    diane f_pouty m_talk "Aww, well, that's okay, [saga.cast.anon]."
    show old_anon 13 at old_left
    diane e_ne f_pensive -m_talk @ -m_talk "The girls will grow out of that phase sooner than you think..."
    diane e_b f_shy m_laugh @ of_blush -m_talk "... Just give it some time!"
    show old_anon 17
    show diane f_happy -m_laugh
    anon "Thanks, [saga.cast.diane]."
    show old_anon 203
    diane e_w f_horny "No problem, stud!"
    show old_xtra 21 at old_left with dissolve
    anon "..."
    diane f_calm "..."
    label dia02_diane.cookie hide:
    diane a_shovel_cheek e_ne f_pensive @ -m_talk "Boy, it sure is hot out here, isn't it?"
    show old_anon 14
    show diane e_w f_calm
    hide old_xtra with dissolve
    anon "Heh, yeah. I'm sweating like crazy!"
    show old_anon 13
    diane a_shovel_finger "Well, I bet I can come up with a solution to that..."
    show diane e_sw f_pouty m_talk p_bend_hose with dissolve
    show old_anon 10
    anon "Oh?"
    show old_anon 12
    anon "What are you-"
    show diane a_hose e_b f_elated m_teeth p_stand with dissolve
    show old_anon 11
    anon "..."
    show old_anon 10
    anon "You aren't gonna-"
    show old_anon 668
    show diane a_hose_spray
    anon "!!!" with hpunch
    pause
    anon "Whoa! That's freezing!"
    hide old_anon
    show old_anon 669 behind diane at pos(.35) with dissolve
    diane f_shy m_laugh @ -m_talk "Oh, no you don't! You aren't getting away that easily!"
    hide old_anon with dissolve
    diane f_happy m_talk p_run_hose "Hahaha!"

    scene mono diane_water
    mono "[saga.cast.diane] and I wrestled with that hose, spraying one another and giggling like school children." with fade
    mono "We didn't get a lot accomplished in the garden that day but we did have a lot of fun!"

    scene diane_yard dusk -diane at stage
    show old_anon 677 at old_left
    show diane a_cheek c_farm_wet e_b f_shy m_laugh at right
    with fade
    diane @ -m_talk "Okay, okay! I submit!"
    diane e_w f_calm -m_laugh "I can't keep up with you..."
    show diane a_hip e_b f_elated m_teeth with dissolve
    show old_anon 678
    anon "I win?!"
    show old_anon 677
    diane e_w f_calm -m_teeth "Yeah, yeah... You win!"
    show old_anon 679 with dissolve
    anon "Hahaha! Victory!"
    diane e_b f_shy m_laugh @ -m_talk "Hehehe!"
    show old_anon 677 with dissolve
    show diane e_n f_calm m_talk
    pause
    diane "Sheesh, is it getting dark already?"
    diane e_w -m_talk "You should get on home, [saga.cast.anon]."
    diane "I have some other work to do tonight."
    show old_anon 678
    anon "Anything I can help with?"
    show old_anon 677
    diane f_surprised @ -m_talk "Hmm?"
    diane f_horny "Nah, I think not. I appreciate the offer, but this is work I'm better off doing alone..."
    show old_anon 678
    anon "O-okay..."
    show old_anon 677
    diane f_calm "Thanks again for all your help today, stud!"
    diane "Tell [saga.cast.debbie] I said, \"Hi.\""
    show old_anon 678
    anon "Alright."
    anon "See ya soon, [saga.cast.diane]."
    hide old_anon with dissolve
    return True


label dia02_diane.fail:
    show old_anon 253 with dissolve.nowait
    pause
    show old_anon 256 with dissolve.nowait
    anon "Ughhh...!"
    anon "Ghhh..."
    show old_anon 27 with dissolve
    anon "I... I can't do it..."
    anon "I'm sorry..."
    show old_anon 3
    diane "Oh..."
    diane "It's... Okay. I really did pack it way too full..."
    diane "I'll just take some out, and we can do it little by little."
    show old_anon 23
    anon "No, wait... I can do it!"
    show old_anon 256 with dissolve
    diane @ -m_talk "..."
    show old_anon 10 with dissolve
    anon "I'm just tired today, that's all..."
    anon "Let me rest and get some strength. I'll come back and do it another day, I promise."
    show old_anon 3
    diane @ -m_talk "..."
    show old_anon 5
    diane e_b f_shy m_laugh @ -m_talk "Oh? Well, if you say so..."
    diane e_w f_calm -m_laugh "I'll see you again soon?"
    show old_anon 2
    anon "Yeah, I'll be back real soon."
    anon "Thanks, [saga.cast.diane]!"
    hide old_anon with dissolve
    return


label dia02_retry:
    hide anon
    show old_anon 2 at old_left
    anon "Still need help moving that wheelbarrow?"
    show old_anon 203
    diane "Oh! Yes please..."
    diane "... I'm afraid it's too much for my poor back."
    jump dia02_diane.merge
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
