label jen17_intro:
    scene mall_hall1 at stage
    show old_anon 11 at old_right with dissolve
    anon "( What the- )"
    anon "( There's a crowd of people outside Cosmic Cumics! )"
    show old_anon 31 with dissolve
    anon "( Is that [saga.cast.erik]? )"
    hide old_anon with dissolve
    return


label jen17_intro.jenny:
    anon f_shy "..."
    jenny a_fold f_annoyed "Did you get it?"
    anon f_confused "Did I get what?"
    jenny @ e_r "The mask, dummy?!"
    anon f_calm "Oh, right."
    anon f_shy "Nah, I'm still working on that."
    jenny a_point "Ugh, well, get out of my room then!"
    show anon f_worried
    pause
    hide anon with dissolve

    call shot.debbie_bed2_door
    with fade
    show anon a_think e_nw f_pensive with dissolve.nowait
    anon @ -m_talk "( Hmm, I wonder what she's planning to do for the stream? )"
    pause
    anon @ -m_talk "( I'll have to get a mask if I wanna find out... )"
    anon @ -m_talk "( I should head to the mall and look around for one. )"
    hide anon with dissolve
    return


label jen17_shop:
    scene mall_hall1 at stage(.362, .513, 15)
    show erik o_right at pos(.45)
    show karl o_right at pos(.65)
    show justin o_right at pos(.85)
    show old_anon 10 at old_left with dissolve
    anon "[saga.cast.erik]?"
    show old_anon 5
    erik @ -m_talk "Hmm?"
    show karl -o_right
    erik -o_right "[saga.cast.anon]?"
    show justin -o_right
    with dissolve
    show old_anon 14
    anon "What's going on?"
    show old_anon 13
    erik "I didn't know you're a wrestling fan."
    show old_anon 10
    anon "Wrestling?"
    show old_anon 13
    erik "Yeah, aren't you here to pick up the new game?"
    show old_anon 10
    anon "What new game?"
    show old_anon 5
    karl f_curious "You don't know about WPWF?"
    show old_anon 10
    anon "Excuse me?"
    show old_anon 5
    karl "Uhh, Women's Professional Wrestling Federation?"
    karl f_angry "Psh, who is this joker?"
    erik o_right "Whoa, calm down Brutalitops!"
    erik "[saga.cast.anon] is an ally."
    justin "Is he here to join our merry band?"
    karl "C'mon, we don't need this guy."
    erik "Eh, [saga.cast.anon] doesn't really play WoO."
    karl @ e_r f_annoyed "Laaaaame."
    justin "That's too bad, because our guild could really use some new members."
    karl f_nervous "I bet he doesn't even have a class."
    erik "We could give him one."
    justin "How about a bard?"
    justin "That would suit our party's needs perfectly."
    karl "Yeah, or a druid maybe..."
    karl "... Then we'd have bark armor and thorns!"
    show old_anon 10
    anon "[saga.cast.erik], who are these guys?"
    show old_anon 5
    show karl f_calm
    erik -o_right "Heh, these are my guildmates from {i}World of Orcette{/i}."
    show old_anon 10
    anon "Oh."
    show old_anon 5
    erik o_right "This here is [saga.cast.karl]."
    karl a_fists f_angry "Only my friends know me as [saga.cast.karl]."
    karl e_o f_crazy m_talk "You have to call me Brutalitops!"
    karl "Master of the Seven Sided Strike and defender of goblin maidens!"
    show karl a_side e_w f_calm -m_talk with dissolve
    show old_anon 30
    anon "Goblin maidens?"
    show old_anon 5
    erik -o_right "He's our Fury Monk."
    show erik at pos(.4)
    erik @ a_whisper "Hence the anger issues."
    show erik at pos(.45)
    with dissolve
    show old_anon 10
    anon "O-okay..."
    show old_anon 5
    erik o_right "And this is [saga.cast.justin] the Wise, our guild leader and the most talented wizard in all the lands."
    justin "Oh, please... he's exaggerating."
    karl o_right "No way, man!"
    karl "The way you charmed that demoness the other day..."
    erik "Yeah, it was incredible!"
    justin a_point_self e_b f_smug "That was nothing."
    justin "The real magic didn't happen until we retired to my bed chambers for the night."
    justin e_w f_calm "If you catch my drift?"
    show justin a_side
    show karl -o_right
    show old_anon 10
    anon "Ehh..."
    show old_anon 5
    justin "Pleasure to meet you, [saga.cast.anon]."
    justin "Any friend of [saga.cast.erik] the Mighty is a friend to me as well."
    show erik -o_right
    with dissolve
    show old_anon 14
    anon "Y-yeah, thanks."
    anon "So all these people are here to buy a wrestling game?"
    show old_anon 13
    erik "Pretty much."
    justin "Not me, I'm here to meet the Pink Cyclone in the flesh!"
    justin "She's always been my favorite."
    show old_anon 14
    anon "Who?"
    show old_anon 13
    karl "Pink Cyclone, man!"
    karl "You've seriously never heard of her?!"
    show old_anon 14
    anon "Nope, sorry."
    show old_anon 13
    karl f_curious "Sheesh, you need to get out more."
    erik "She's the undefeated champion of the WPWF!"
    show old_anon 14
    anon "Oh, really?"
    show old_anon 13
    justin "More like the undefeated champion of my heart."
    karl e_r f_annoyed m_talk "Well, she's not exactly undefeated..."
    show karl e_w f_calm -m_talk
    erik o_right "C'mon man, Nikita totally cheated!"
    erik "The commissioner even declared the match no contest."
    karl f_curious "Doesn't matter, the Pink Cyclone lost the belt."
    erik "Only because Nikita shattered her knee with a chair!"
    karl "Yeah, leaving her incapable of defending the title."
    erik "She's still 34-0."
    karl f_nervous "You mean, 34-0-1."
    erik "It was a no contest!"
    karl "She hasn't wrestled since, man... and that was three years ago!"
    show old_anon 14
    anon "So this Pink Cyclone lady is here today?"
    show old_anon 13
    show karl f_calm
    erik -o_right "Yeah, she's inside signing autographs to promote the video game."
    erik "You wanna come with us and meet her?"
    show old_anon 29 behind erik with dissolve
    anon "Eh, sure... I guess."
    show erik behind old_anon
    show old_anon 13
    with dissolve
    justin e_b f_smug "I'm totally gonna declare my love to her."
    show erik o_right
    karl o_right "Don't you have enough women, [saga.cast.justin]?!"
    show justin e_w f_calm
    karl "With the new demoness and those elven twins, you've basically got a harem!"
    show old_anon 17
    justin "There's no such thing as enough women, [saga.cast.karl]..."
    show old_anon 13
    karl "I dunno, I'm happy with what I've got."
    justin "Hah, you and your goblin maidens..."
    justin "... I just don't see the appeal."
    erik "I think he's got a midget fetish!"
    show old_anon 11
    karl e_o f_crazy m_talk -o_right "What?!"
    karl e_w f_angry -m_talk "That's not it at all, you guys!"
    anon "..."

    scene black
    with dissolve
    mono ""

    scene mall_hall1 at stage(.38, .513, 15)
    show erik o_right at pos(.45)
    show old_anon 9 at old_left
    show justin o_right at pos(.85)
    show karl o_right at pos(.65)
    with dissolve
    karl "Alright, we're next!"
    justin e_b f_smug "Wish me luck, fellas."
    hide karl
    hide justin
    with dissolve
    erik "That crazy bastard."
    show old_anon 14 with dissolve
    anon "You definitely have some colorful friends, [saga.cast.erik]."
    show old_anon 13
    erik "Yeah, we get along pretty well."
    erik -o_right "You really can join our guild, you know?"
    show old_anon 14
    anon "Eh, I'm not sure I would fit in with those guys."
    show old_anon 13
    erik "Dude, what are you talking about?!"
    erik "You're awesome!"
    erik "We'd all be ecstatic if you joined."
    show old_anon 14
    anon "Heh, thanks for saying that [saga.cast.erik]."
    anon "I'll think about it."
    show old_anon 13
    erik "Okay."
    karl "HAHAHAAH!"
    show justin a_neck f_hurt at pos(.7)
    show karl a_game_side f_nervous at pos(.9)
    show erik o_right
    with dissolve
    karl "Dude, that was hilarious!"
    justin e_e "Shut up, [saga.cast.karl]!"
    justin "It wasn't funny!"
    karl "Pfft, hahahaha!!"
    show justin e_w
    erik "What happened?"
    karl "Romeo over here confessed his undying love to the Pink Cyclone and then tried to hug her."
    show old_anon 14
    anon "So, what's funny about that?"
    show old_anon 13
    karl "Before he got within two steps, she lashed out and put him in a headlock!"
    show old_anon 11
    erik f_surprised "Really?!"
    karl "Haha, yeah, and she wouldn't let him go until he apologized!"
    erik f_calm "You okay, [saga.cast.justin]?"
    justin a_point_self e_b f_smug "Are you kidding?"
    justin e_w f_hurt "I've never been better!"
    show justin a_side behind erik
    show old_anon 10
    anon "Huh?"
    show old_anon 5
    justin e_b f_smug "She smelled so good, man!"
    show old_anon 37 with dissolve
    justin "I would have stayed in that headlock all day if they had let me."
    show old_anon 13
    karl "Dude, you almost passed out..."
    justin e_w f_calm o_right "All part of the act, my friend."
    karl "Yeah, right!"
    justin -o_right "She was crazy strong though!"
    karl a_game_up f_calm "Welp, I got my game and my autograph."
    karl "I can't wait to crack this sucker open and PWN some noobs!"
    karl "C'mon, let's go [saga.cast.justin]."
    show karl a_game_side
    justin a_neck f_hurt @ e_e "Yeah okay, I might need to pay my chiropractor a visit..."
    karl "Later, [saga.cast.erik]."
    hide karl
    hide justin
    with dissolve
    erik -o_right @ a_whisper "See ya online, guys!"
    show old_anon 14
    anon "I guess we're next, huh?"
    show old_anon 13 at center
    show erik o_right at pos(.7)
    erik "This is going to be awesome!"
    hide old_anon
    hide erik
    with dissolve

    scene comic_shop -lily at stage
    show bridget c_lucha o_right of_lucha at pos(.7)
    show lily at pos(.9)
    with fade
    show erik f_surprised o_right at pos(.35)
    show old_anon 13 at pos(.15), face_right
    with dissolve
    lily "Are you sure you don't want me to call the cops?"
    pink "Oh, there's no reason to get the cops involved."
    pink "I took care of it."
    lily "O-okay."
    pink "Besides, he's long gone by now."
    pink "How many more copies are left?"
    lily "Just the one."
    pink "Good, my time is almost up here."
    show old_anon 29 with dissolve
    anon "H-hello?"
    show old_anon 13
    show bridget a_hips -o_right
    show lily behind bridget
    with dissolve
    pink "Nice to mee-"
    show bridget f_surprised
    pause
    pink f_angry "W-what are you two doing here?!"
    show old_anon 5
    anon "Hmm?"
    pink "Did somebody put you up to this?"
    pink "'Cause I'm not laughing!"
    show old_anon 10
    anon "N-nobody pu-"
    show erik e_n f_woozy m_talk behind bridget
    hide old_anon
    show bridget a_seize_old_anon at pos(.465)
    with dissolve
    pink "You better start talking, right now!"
    show erik a_faint
    pause
    show erik p_fall with dissolve
    show erik p_feet with dissolve
    pink f_surprised @ -m_talk "!!!" with vpunch
    hide erik
    show bridget a_seize_old_anon_talk
    anon "W-we just want an autograph!"
    show bridget a_seize_old_anon
    pause
    show old_anon 22 behind lily at old_left
    pink a_side f_calm "Oh."
    show bridget behind lily at pos(.7)
    pink "Sorry about that, I guess I mistook you for someone else..."
    show old_anon 10
    anon "{i}*Gulp*{/i} S-sure, no problem."
    show old_anon 5
    pink "Is he alright?"
    show old_anon 10
    anon "[saga.cast.erik]?"
    show old_anon 184 at pos(.05), zoom(.9) with dissolve
    pause
    hide old_anon
    show erik b_old_anon_help o_right p_pickup behind bridget at left
    with dissolve
    pause
    show old_anon 5 behind bridget at pos(.1), face_right
    show erik f_woozy -b_old_anon_help -p_pickup at pos(.3)
    with dissolve
    erik "W-what happened?!"
    show old_anon 10
    anon "You fainted, dude."
    show old_anon 5
    erik "I did?"
    show erik a_faint
    lily @ e_b f_happy m_laugh "Hehe, that's so adorable!"
    show old_anon 13
    pink a_hips "You boys are big fans, huh?"
    erik a_side f_calm "Oh, totally!"
    erik "That time you knocked out Lioness in the royal rumble!"
    erik "Or when you tapped out Rebecca Savage in that cage match!"
    erik "Oh and your moonsault off the top rope onto-"
    pink "Okay, okay, I get it..."
    pink @ e_b f_amused m_laugh "Hah, you two really {i}are{/i} big fans."
    erik "The BIGGEST!"
    pink "Well, I've got something special for you two then."
    erik "R-really?!"
    show erik e_sw
    pink p_pickup "Mmhmm."
    show erik e_w
    pink a_poster -p_pickup "Here you go."
    show bridget a_poster_show
    erik e_sw f_surprised "WHOA!!!"
    show old_anon 735
    show bridget a_hips
    erik a_poster f_calm "[saga.cast.justin] is going to be so jealous..."
    erik "... This is like, the coolest thing ever!"
    show old_anon 14 with dissolve
    anon "Thank you, miss... uhh, Pink Cyclone."
    show old_anon 13
    pink "You're very welcome, boys."
    pink o_right "Now, unless there's anything else?"
    pink "I should really head out."
    lily "Nope, you've already done so much."
    lily a_lucha_point "These replica masks are going to be a huge hit with our cosplay community!"
    show old_anon 11
    lily "I can't wait to get home and start working on my costume."
    show lily a_side
    pink "Oh, you'll have to e-mail me a picture of that."
    lily e_b f_happy m_laugh @ -m_talk "Will do!"
    show lily e_w f_calm -m_laugh
    show old_anon 29 with dissolve
    anon "E-excuse me?"
    show bridget -o_right
    anon "A-are you selling those?"
    show old_anon 3
    lily "No, sorry."
    lily "It's a promotional item that comes with each copy of the game."
    show bridget a_side
    show lily b_bridget_lucha p_hug_side at pos.bridget
    show old_anon 13
    lily "Thanks again for coming out."
    pink "My pleasure, sweetie."
    hide lily
    with dissolve
    pink "I'll see you two at schoo-"
    show old_anon 10
    show bridget f_surprised
    anon "Huh?"
    show old_anon 5
    pink a_rub_hands f_calm "I err, meant to say..."
    pink "Stay in school!"
    pink @ e_b f_amused m_laugh "Heh, you know... don't be a fool, stay in school!"
    pink "That's what... I was..."
    show erik e_w
    pink "... {i}*Ahem*{/i} Goodbye boys."
    hide bridget with dissolve.nowait
    erik "Bye, Pink Cyclone!"
    show old_anon 10
    show erik e_sw
    anon "That was weird."
    show old_anon 13
    erik "That was awesome!"
    erik "Check out this poster, dude!"
    erik "She's so hot!"
    show old_anon 14
    anon "Heh, yeah."
    show comic_shop lily with dissolve
    show old_anon 13
    erik a_side e_w -o_right "Alright, time to snag that last copy of the game."
    show old_anon 14
    anon "You'd better hurry."
    show old_anon 13
    hide erik
    with dissolve.nowait
    erik "Woo hoo!!"
    show old_anon 36
    with dissolve.nowait
    anon "I'll see you later."
    hide old_anon with dissolve

    scene mall_hall1 at stage(.38, .513, 15) with fade
    show anon a_think e_sw f_pensive with dissolve
    anon "( Damn, that mask would have worked perfectly for [saga.cast.jenny]'s camshows... )"
    anon "( ... Hmm, I guess I'll have to keep looking. )"
    show anon a_side e_w f_calm
    pause
    anon @ -m_talk "( Maybe I can- )"
    erik "Wait!!"
    anon a_surprised f_surprised o_right @ -m_talk "Hmm?"
    show anon a_side
    show erik f_worried at pos(.755)
    erik "[saga.cast.anon]!!!"
    anon f_confused "[saga.cast.erik]?"
    erik "You left."
    anon f_worried "Yeah, sorry... I've got some stuff I need to take care of."
    erik a_lucha_give "Here."
    show anon e_s f_surprised
    erik "You were asking about these inside..."
    show anon e_w
    erik f_shy "... And I figured since I got the last game, it's only fair you get the mask."
    anon "Wow, really?"
    anon f_confused "Are you sure?"
    erik f_calm "Yup!"
    show anon a_lucha e_s f_shy
    erik a_proud "Pink isn't really my color anyways..."
    anon e_w "Thanks, man!"
    show anon a_backpack_02 e_s
    erik a_side "No problem."
    show anon a_side e_w f_calm
    erik "Now, I'm off to conquer the ring!"
    anon a_wave "Good luck!"
    hide erik with dissolve.nowait
    erik "Muahahaah!"
    anon a_side f_happy -o_right @ -m_talk "( Well, that worked out rather nicely... )"
    anon @ e_b m_teeth "( ... Almost like it was scripted! )"
    anon f_calm @ -m_talk "( Well, no sense looking a gift horse in the mouth. )"
    anon @ -m_talk "( This should work great for [saga.cast.jenny]'s camshows. )"
    anon f_worried @ -m_talk "( I guess I should meet her in her room and see what she thinks. )"
    hide anon with dissolve
    return


label jen17_shop.rails:
    scene mall_hall1 at stage
    show anon with dissolve
    anon "( I should go say hi to [saga.cast.erik] and see what he's doing here. )"
    hide anon with dissolve
    return


label jen17_jenny(when):
    scene debbie_bed2 -jenny at stage
    show jenny a_fold f_annoyed at right
    show anon a_pocket o_right at left with dissolve
    jenny "Did you get it?"
    anon "Yup."
    show anon a_backpack e_s f_shy
    pause
    anon a_lucha e_w f_calm "What do you think?"
    show anon a_side
    jenny a_lucha e_wsw f_disgusted "It's pink."
    anon "So?"
    jenny e_w f_annoyed "It's kinda girly, don't you think?"
    anon f_worried "Does that really matter?"
    jenny e_r "I guess not."
    show jenny a_lucha_throw e_w
    anon f_calm "So when do we start?"
    jenny a_hips "I need to promote a little first."

    if when == 1:
        jenny "Come back tomorrow afternoon, alright?"
    else:
        jenny "Come back on [saga.time.dow + when] afternoon, alright?"

    anon "Got it."
    jenny f_angry m_teeth "And you had better put on a good show!"
    jenny "I've got a lot riding on this!"
    anon f_worried "O-okay."
    hide jenny
    show debbie_bed2 jenny
    with dissolve
    pause

    if when == 1:
        anon e_b f_happy m_teeth @ -m_talk "( I guess I'll come back tomorrow afternoon then... )"
    else:
        anon e_b f_happy m_teeth @ -m_talk "( I guess I'll come back on [saga.time.dow + when] afternoon then... )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
