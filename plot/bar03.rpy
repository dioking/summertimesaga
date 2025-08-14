label bar03_barb1:
    anon f_calm "When do you wanna do our next lesson, [saga.cast.barb]?"
    barb f_sad "Right, about that..."
    barb "... Before we can schedule the next lesson, I'll need you to round up some magazines for me."
    anon f_surprised "Magazines?!"
    anon f_confused "What kind of magazines?"
    barb f_calm "Oh, any old magazines will do."
    barb "Just make sure to grab about two dozen or so."
    anon f_calm "Alright."
    pause
    anon a_rub f_shy "Umm, where do you think I should look for them?"
    barb f_confused "For magazines?"
    anon a_side "Yeah."
    barb f_calm "It shouldn't be too hard to find magazines, [saga.cast.anon]... I see them all the time around the school..."
    barb "... And you could always try the library as well; they have a huge selection to choose from."
    anon f_calm "School and library."
    anon a_salute "Got it!"
    barb "Thank you, dear."
    hide anon with dissolve
    return


label bar03_mags:
    return


label bar03_mags.barb:
    anon f_confused "Where did you say I should look again?"
    barb f_confused "For the magazines?"
    barb f_calm "Try the library."

    if saga.prop.mags_lewd not in saga.cast.anon:
        anon f_calm "Library, got it!"
    else:

        anon f_worried "I did manage to find some there, but not enough."
        barb @ -m_talk "Hmmm..."
        barb "... In that case you could try looking around school."

        if saga.prop.mags_buff not in saga.cast.anon:
            barb "Maybe you can ask some of your friends too."

        anon f_calm "Thanks, [saga.cast.barb], I'll do that."

    hide anon with dissolve
    return


label bar03_mags.fail:
    show old_anon 10
    show old_melody lounge 2
    anon "Err... Instrument's have families?"
    show old_anon 11
    show old_melody lounge 3
    melody "Heh, well, that's something you'd better figure out if you want these magazines."
    melody "Come back when you know the answer."
    show old_melody lounge 2
    show old_anon 10
    anon "Ah, man..."
    hide old_anon with dissolve
    return


label bar03_mags.fashion(misc=0):
    scene school_lounge -brownies -mags_fashion -table at stage(.7, .6, 3)
    show anon e_sw f_surprised o_right at pos(.25, .95)
    show school_lounge brownies mags_fashion table as table at stage(.7, .6, 3, b=0)
    anon @ -m_talk "( Ooooh, fashion mags! )"
    anon f_shy @ -m_talk "( These should work great for whatever [saga.cast.barb] is planning. )"
    show school_lounge -mags_fashion as table
    show anon a_backpack_01 e_s at pos(.4)
    with dissolve.nowait
    call bar03_mags.mags
    hide anon with dissolve
    return


label bar03_mags.jane1:
    show old_anon 2
    anon "I'm doing a project for art class and I need some old magazines."
    anon "Could you show me where to find some?"
    show old_anon 1
    jane "You're out of luck I'm afraid. We stopped carrying those a few months ago."
    show old_anon 10
    anon "You don't have any?"
    show old_anon 1
    jane "If we have any they'll be in the function room, but I think we sent all the ones we had off to be recycled."
    show old_anon 10
    anon "Oh man..."
    anon "Thanks anyways."
    show old_anon 11
    jane "Sorry."
    hide old_anon with dissolve

    call shot.library_lobby_center
    with fade
    show anon a_think e_sw f_pensive o_right with dissolve.nowait
    anon @ -m_talk "( What am I gonna do now? )"
    anon @ -m_talk "..."
    anon a_side e_w f_worried @ -m_talk "( I guess I'll check out the function room just in case... )"
    anon @ -m_talk "( ... Then maybe head back to school and look around. )"
    anon f_calm @ -m_talk "( There's gotta be some magazines somewhere. )"
    hide anon with dissolve
    return


label bar03_mags.jane2:
    show old_anon 10
    anon "So you don't have a single magazine around here?"
    show old_anon 11
    jane "Not if there are none in the function room."
    jane "We canceled the subscriptions and tossed most of what we had out."
    show old_anon 10
    anon "Okay, thanks anyways."
    hide old_anon with dissolve

    call shot.library_lobby_center
    with fade
    show anon a_pocket f_tired o_right with dissolve.nowait
    anon "{i}*Sigh*{/i}"
    show anon f_worried
    pause
    anon @ -m_talk "( I guess I should head back to school and look around there. )"
    anon f_shy @ -m_talk "( Maybe I'll get lucky? )"
    hide anon with dissolve
    return


label bar03_mags.kevin(misc=0):
    call shot.school_cafe_kevin
    show old_kevin 29b at old_right
    show old_anon 2 at old_left with dissolve
    anon "Hey, [saga.cast.kevin]!"
    show old_anon 1
    show old_kevin 30
    kevin "What's up, [saga.cast.anon]?"
    show old_anon 2
    show old_kevin 29b
    anon "Not much. What are you reading?"
    show old_anon 1
    show old_kevin 30b
    kevin "Oh, just some workout magazines I got from the gym."
    show old_anon 2
    show old_kevin 29b
    anon "Cool, you trying a new workout or something?"
    show old_anon 1
    show old_kevin 30
    kevin "No, why?"
    show old_anon 11
    show old_kevin 29
    anon "..."
    show old_kevin 31 with dissolve
    kevin "Come check out this beefcake, [saga.cast.anon]!"
    show old_anon 10
    show old_kevin 31b
    anon "... Beefcake?"
    show old_anon 11
    anon "..."
    show old_anon 10
    anon "Uh, right... you think I could take some of these magazines?"
    show old_anon 11
    show old_kevin 30 with dissolve
    kevin "Heh, I didn't know you were a fellow connoisseur of the masculine form..."
    show old_anon 10
    show old_kevin 29
    anon "Actually, I'm making a collage."
    show old_anon 11
    show old_kevin 30b
    kevin "Oh, right. Collage."
    show old_kevin 31 with dissolve
    kevin "I gotcha, bro! Say no more!"
    kevin "Take all you need! This one will keep me busy for a while."
    show old_anon 2
    show old_kevin 31b
    anon "Awesome! Thanks, uhh, bro..."
    show old_anon 1
    show old_kevin 31c
    kevin "Daaaamn, he's glistening..."
    show old_anon 10
    anon "..."
    hide old_anon with dissolve

    scene school_cafe at stage(.312, .54, 1.6) with fade
    show anon a_backpack_01 e_s with dissolve
    call bar03_mags.mags
    hide anon with dissolve
    return


label bar03_mags.lewd(misc=0):
    scene library_social at stage(.856, .545, 3.55)
    show old_anon 5b at face_right with dissolve
    anon "( Hey, alright... there {i}are{/i} some magazines here! )"
    show old_anon 184 with dissolve.nowait
    call bar03_mags.mags
    show old_anon 579c with dissolve.nowait
    anon "( Whoa... These are- )"
    pause
    anon "( Why are there nudie mags in the library function room?! )"
    show old_anon 578 with dissolve.nowait
    anon "( Well, she did say that any old magazine would do. )"
    hide old_anon with dissolve
    return


label bar03_mags.mags:
    if misc == 0:
        anon @ -m_talk "( I'll definitely need more than this but it's a start at least. )"
    elif misc == 1:
        anon @ -m_talk "( I still need a few more, but I'm definitely getting there. )"
    else:
        anon @ -m_talk "( Sweet! This should be more than enough for [saga.cast.barb]! )"

    return


label bar03_mags.melody(misc=9):
    call shot.school_lounge_sofa
    show old_melody lounge 5
    show old_anon 11 at old_left with dissolve
    pause
    show old_melody lounge 1
    show old_anon 10
    with dissolve
    anon "Oh, hi there, [saga.cast.melody]."
    show old_anon 11
    show old_melody lounge 3
    with dissolve.nowait
    melody "[saga.cast.anon]? You're not supposed to be in here..."
    show old_anon 10
    show old_melody lounge 2
    anon "Yeah, sorry."
    show old_anon 2
    anon "[saga.cast.barb] has me looking for old magazines."
    anon "We're making a collage!"
    show old_anon 1
    show old_melody lounge 3
    melody "Collage, huh?"
    melody "I used to make those all the time when I was younger!"
    show old_anon 2
    show old_melody lounge 2
    anon "What are you snacking on?"
    show old_anon 1
    show old_melody lounge 3b
    with dissolve
    melody "Oh this?"
    show old_melody lounge 3 with dissolve
    melody "It's one of [saga.cast.barb.name]'s {i}special{/i} brownies."
    show old_anon 2
    show old_melody lounge 2
    anon "I didn't know [saga.cast.barb] could bake?"
    show old_anon 1
    show old_melody lounge 3
    melody "She makes the {i}best{/i} brownies!"
    melody "I just can't get enough!"
    show old_anon 2
    show old_melody lounge 2
    anon "... Neat!"
    anon "So, do you think I could have a few of those magazines there on the table?"
    show old_anon 1
    show old_melody lounge 3
    melody "I don't see why not."
    show old_anon 2
    show old_melody lounge 2
    anon "Awes-"
    show old_anon 11
    show old_melody lounge 6
    with dissolve.nowait
    melody "If you can answer a question off my next test!"
    show old_anon 10
    show old_melody lounge 2
    with dissolve.nowait
    anon "Really?"
    show old_anon 11
    show old_melody lounge 3
    melody "Nothing's free in life, [saga.cast.anon]."
    melody "Now let's see..."
    melody "The flute is a member of which instrumental family?"

    if saga.cast.anon.int < 4:
        jump bar03_mags.fail

    show old_anon 2 at old_left
    show old_melody lounge 2
    anon "That's easy! Woodwind."
    show old_anon 1
    show old_melody lounge 3
    melody "Very good, [saga.cast.anon]!"
    melody "I guess you've been paying attention in class after all."
    show old_melody lounge 4 with dissolve
    melody "Go ahead and take as many magazines as you need."
    show old_anon 2
    show old_melody lounge 2
    with dissolve.nowait
    anon "Thanks, but the ones on the table should be enough."
    hide old_anon with dissolve.nowait
    anon "Enjoy your brownie, [saga.cast.melody]!"
    show old_melody lounge 1b with dissolve
    melody "Ohm, so good! Mmm..."

    scene school_lounge at stage(.45, .5, 3) with fade
    show anon a_backpack_01 e_s with dissolve
    call bar03_mags.mags
    hide anon with dissolve
    return True


label bar03_barb2(when):
    anon f_calm "I've got those magazines you requested."
    show anon a_backpack e_s
    barb @ f_curious "Were you able to find a couple dozen?"
    anon a_mags_stack e_w "Yes, ma'am."
    barb "See, I knew you could do it!"
    barb "You can do anything, [saga.cast.anon]... so long as you believe in yourself."
    anon f_confused "Right, okay."
    barb "You can just pop them on the floor for the moment."
    show anon a_reach e_s f_calm p_bend
    pause
    anon a_side e_w -p_bend "There ya go."
    barb "Thank you, dear."

    if when == 1:
        barb "I'll see you after class tomorrow for our next session."
    else:
        barb "I'll see you after class on [saga.time.dow + when] for our next session."

    anon "Okay."
    hide anon with dissolve
    return


label bar03_pause:
    return


label bar03_pause.barb(when):
    anon f_calm "When did you wanna get together for our next lesson?"

    if when == 1:
        barb "After class tomorrow afternoon."
    else:
        barb "After class on [saga.time.dow + when] afternoon."

    anon "Cool, thanks."
    return


label bar03_pause.mia(when):
    show old_anon 14

    if when == 1:
        anon "Did [saga.cast.barb] tell you we're meeting tomorrow afternoon?"
    else:
        anon "Did [saga.cast.barb] tell you we're meeting on [saga.time.dow + when] afternoon?"

    show old_anon 13
    show old_mia 10
    mia "Yeah, she let me know."
    show old_mia 7
    show old_anon 14
    anon f_calm "Coolio."
    show old_anon 13
    return


label bar03_delay:
    scene camera at stage
    show anon f_surprised with dissolve
    anon @ -m_talk "( It's time for another art lesson with [saga.cast.barb]. )"
    anon f_calm @ -m_talk "( [saga.cast.mia] is probably already there waiting for me. )"
    hide anon with dissolve
    return


label bar03_delay.barb:
    anon f_calm "Are you ready to start work on that college thingey?"
    barb "Heh, it's \"collage\", dear."
    anon f_shy "Oh."
    barb "And I'm afraid it'll have to wait until I've finished with classes for the day."
    barb "I can't very well deny my students their lessons."
    show anon f_confused
    barb "Imagination, like a garden, requires daily watering if you want it to grow."
    anon "Yeah, okay."
    return


label bar03_delay.mia:
    show old_anon 14
    anon "I wonder if we're going to be doing a mural or something..."
    anon "... How else could we be working on the college?"
    show old_anon 13
    show old_mia 10
    mia "Umm, I think it's pronounced \"collage\"."
    show old_mia 7
    show old_anon 10
    anon "Oh."
    show old_anon 5
    show old_mia 10
    mia "And I have no idea..."
    mia "... I'm just hoping it isn't anything too messy."
    show old_mia 7
    show old_anon 2
    anon "Aww, but messy can be fun!"
    show old_anon 1
    return


label bar03_art1:
    call shot.school_art_barb
    show old_mia 2 at pos(.55), face_right
    show old_anon 2 at old_right with dissolve
    anon "You ready for another session with [saga.cast.barb]?"
    show old_anon 1
    show old_mia 6
    mia "Yeah, I guess..."
    show old_anon 10
    show old_mia 2
    anon "You don't seem very excited about it."
    anon "I thought you loved art?"
    show old_anon 11
    show old_mia 6
    mia "I do love art."
    mia "... And I really like watching you and [saga.cast.barb] work."
    show old_mia 6b
    mia "It's just..."
    show old_mia 6
    mia "[saga.cast.barb] makes me feel a little self-conscious."
    show old_anon 10
    show old_mia 2
    anon "She does?"
    show old_anon 11
    show old_mia 6
    mia "She's being very forward with me, don't you think?"
    show old_anon 2
    show old_mia 2
    anon "Yeah, but she's like that with everyone."
    show old_anon 1
    show old_mia 6
    mia "Is she?"
    mia "I dunno, she's lived such an adventurous life, and she's so full of experience..."
    show old_mia 6b
    mia "She makes me feel so boring."
    show old_anon 2
    show old_mia 2
    anon "I don't think you're boring, [saga.cast.mia]."
    show old_anon 1
    show old_mia 4
    mia "You don't?"
    show old_mia 1
    show old_anon 2
    anon "Not at all."
    anon "I think you just need to relax and keep an open mind."
    anon "I betcha [saga.cast.barb] can teach us a lot of cool stuff!"
    show old_mia 5
    show old_anon 1
    mia "..."
    show old_mia 3
    mia "Yeah, maybe you're right, [saga.cast.anon]!"
    show old_mia 4
    mia "I coul-"
    show old_mia 1
    show old_anon 11
    show old_barb 11 behind old_anon at old_left with dissolve
    barb "There's my favorite students!"
    show old_mia 8b at pos(.59), face_left with dissolve
    barb "What are you two lovebirds talking about?"
    show old_mia 55 with dissolve
    show old_anon 10
    anon "Lovebirds?"
    show old_mia 56
    show old_anon 11
    mia "We were just wondering what todays session would be about?"
    show old_mia 55
    show old_barb 13
    barb "Straight to business, huh?"
    barb "You little firecracker, I love it!"
    show old_barb 12
    mia "..."
    show old_barb 58 with dissolve
    barb "Today you're each going to make a collage!"
    show old_barb 10 with dissolve
    show old_mia 12b with dissolve
    mia "Collage? I don't even know what that means..."
    show old_mia 8b
    show old_barb 27 with dissolve
    barb "Oh, they are so much fun! You're going to love them [saga.cast.mia]!"
    barb "We're going to cut pictures out of magazines and glue them together to make art."
    show old_barb 26
    show old_anon 2
    show old_mia 7
    anon "Sounds like fun to me."
    show old_anon 1
    show old_mia 10
    mia "Yeah, it really does."
    show old_mia 7
    show old_barb 11 with dissolve
    barb "Alright, well, I've got just about everything we need right here. We're just missing the magazines that I left in my office."
    barb "Why don't you go and grab them for us, [saga.cast.anon]?"
    show old_barb 10
    show old_anon 2
    anon "In your office?"
    anon "I can do that!"
    show old_anon 1
    show old_mia 10b
    mia "I'll help!"
    show old_mia 8
    show old_barb 11
    barb "Oh, no... [saga.cast.anon] can handle it."
    show old_barb 13
    barb "Let's have us another gal to gal chat while we wait, hmm?"
    show old_barb 12
    show old_mia 12
    mia "Oh, umm... okay, I suppose."
    show old_mia 8
    show old_anon 2
    anon "Have fun you two."
    hide old_anon
    show old_mia 12 at face_right
    with dissolve.nowait
    mia "Hurry back!!"
    show old_mia 8
    pause
    return


label bar03_art1.rails:
    jump bar02_art1.rails


label bar03_take:
    call shot.school_office3_barb
    show anon a_reach e_s p_bend with dissolve
    anon @ -m_talk "( Here they are. )"
    anon a_mags_stack e_sw f_surprised -p_bend @ -m_talk "( Man, this is so many magazines! )"
    hide anon with dissolve
    return


label bar03_take.barb:
    call shot.school_art_barb
    show old_mia 8b at pos(.42)
    show old_barb 11 at old_left
    barb "... Goodness no, with the right amount of lubricant it will slide right in, dear."
    show old_barb 10
    show old_mia 12b
    mia "Doesn't it hurt though?"
    show old_barb 11
    show old_mia 8b
    barb "Not if do things right. Preheat the oven a bit and take things slow."
    show old_barb 13
    barb "It can feel extremely pleasurable!"
    show old_barb 12
    show old_mia 12b
    mia "Yeah, but the Bible says-"
    show old_barb 13
    show old_mia 8
    barb "Oh pish posh!"
    barb "If God didn't want us sticking things up there, he would have given the anus a gag reflex..."
    show old_barb 10
    show old_anon 1 behind old_barb at old_right with dissolve
    barb "..."
    show old_barb 11
    barb "Hey there, [saga.cast.anon]."
    show old_barb 10
    show old_mia 56 at old_left, pos(.4) with dissolve
    mia "[saga.cast.anon]!"
    mia "Oh my gosh, how long have you been standing there?!"
    show old_anon 2
    show old_mia 55
    anon "Not long, why?"
    show old_anon 1
    show old_barb 11
    barb "Did you get the magazines already?"
    show old_anon 2
    show old_barb 10
    anon "No, not yet."
    show old_anon 1
    show old_barb 11
    barb "Oh, well shoo! We're having girl talk here!"
    show old_anon 10
    show old_barb 10
    anon "My bad."
    hide old_anon with dissolve

    scene school_hall1w at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( I wonder what they were talking about... )"
    pause
    anon e_b f_happy @ m_teeth "( ... Maybe it was me! )"
    anon a_side e_w @ -m_talk "( I should go grab those magazines and hurry back. )"
    hide anon with dissolve
    return


label bar03_take.rails:
    scene camera at stage
    show anon o_right with dissolve
    anon @ -m_talk "( [saga.cast.barb] said she left the magazines we need upstairs in her office. )"
    anon @ -m_talk "( I should hurry up and retrieve them! )"
    hide anon with dissolve
    return


label bar03_art2:
    call shot.school_art_barb
    show school_art -table
    show old_xtra 22b as basket at pos(.6)
    show old_xtra 22c at pos(.6)
    show old_barb 13 at pos(.35), face_right
    show old_mia 60
    barb "... You know the female body can have upwards of thirty different erogenous zones."
    show old_barb 12
    show old_mia 61
    mia "Really?"
    show old_barb 13
    show old_mia 60
    barb "Oh, absolutely!"
    show old_anon 594 at pos(.85)
    show old_barb 56
    show old_mia 60b
    with dissolve.nowait
    barb "We're complex creatures, [saga.cast.mia]."
    barb "You wouldn't believe how powerful the orgasms can get if the right buttons are being pressed."
    show old_barb 56b
    mia "..."
    show old_barb 56
    barb "I could show you sometime, if you're interested?"
    show old_barb 56b
    show old_mia 61b
    mia "Oh, I don't know..."
    mia "I don't think I'm ready fo-"
    show old_mia 60b
    show old_anon 595
    anon "{i}*Ahem*{/i} ... I'm back!"
    show old_barb 11
    show old_mia 60b at pos(.2), face_right
    with dissolve
    show old_anon 594
    barb "Hey, alright!"
    barb "Did you have any trouble finding them?"
    show old_barb 10
    show old_anon 595
    anon "N-no, it all went pretty smooth..."
    anon "... Err, mostly."
    show old_barb 46
    show old_anon 1
    with dissolve
    barb "Let's see what we have here."
    barb "Cooking, masculine workout, and..."
    show old_mia 61c
    show old_barb 51
    with dissolve
    barb "... Oh, hello!"
    show old_barb 52
    show old_anon 10
    anon "Yeah, sorry."
    show old_anon 11
    show old_barb 53
    barb "Haha, don't be sorry, [saga.cast.anon]!"
    barb "Sex is a natural and important part of life."
    show old_barb 53b
    barb "[saga.cast.mia] and I are big girls, we can handle it. Right [saga.cast.mia]?"
    show old_barb 52b
    pause
    show old_barb 53b
    barb "... {i}*Ahem*{/i} Right, [saga.cast.mia]?!"
    show old_barb 52b
    show old_mia 61b
    mia "Huh? Oh!"
    mia "Heh, umm... Y-yeah, of course."
    show old_barb 53b
    show old_mia 60b
    barb "Hehe..."
    show old_mia 60b
    show old_barb 11 with dissolve
    barb "... We should probably get started on those collages, huh?"
    show old_barb 10
    show old_anon 2
    anon "Sounds good."
    show old_anon 1
    show old_mia 60
    show old_barb 57 at pos(.46) with dissolve
    barb "So, I want you guys to take a look at this..."
    hide old_xtra 22c
    show old_barb 29 at pos(.403)
    with dissolve
    pause
    show old_barb 12 at pos(.35) with dissolve
    mia "..."
    show old_anon 10
    anon "Fruit?"
    show old_anon 11
    show old_barb 13
    barb "Isn't it beautiful?"
    show old_barb 13c
    barb "Just look at the girth on that banana, [saga.cast.mia]!"
    show old_barb 12b
    show old_mia 60b
    mia "..."
    show old_barb 13c
    barb "He's a thick one, isn't he?"
    show old_barb 13
    barb "... And [saga.cast.anon]. What do you think of that succulent peach?"
    show old_barb 12
    show old_anon 10
    anon "Umm, I don't know?"
    show old_barb 13
    show old_anon 11
    barb "It's so juicy looking... Don't you just want to give it a little nibble?"
    show old_barb 12
    show old_anon 10
    anon "... I guess?"
    show old_barb 13
    show old_anon 11
    barb "That's alright, you can take all the time you need."
    show old_barb 13c
    barb "I want you both to look very closely..."
    show old_barb 13
    barb "... And the instant you think you're ready..."
    show old_barb 58 with dissolve
    barb "... We'll start on the collages!"
    barb "I want you to capture exactly how these, shapely and delicious fruits, make you feel."
    show old_barb 12 with dissolve
    show old_anon 10
    anon "... Okay."
    show old_anon 11
    show old_barb 12b
    show old_mia 61b
    mia "Yes, ma'am."
    show old_barb 58 with dissolve
    barb "Very good! Just do whatever feels natural."

    scene mono school_art_magazine
    mono "I wasn't entirely sure what [saga.cast.barb] was hoping the fruits would make me feel..." with fade
    mono "... But I had a ton of fun working on my collage!"

    call shot.school_art_barb
    show school_art -table
    show old_xtra 22b at pos(.6)
    show old_barb 27 at pos(.44)
    show old_anon 604 at old_left
    with fade
    barb "This is truly remarkable work, [saga.cast.anon]!"
    barb "You have such a vivid imagination!"
    show old_anon 605
    show old_barb 26
    anon "Thanks, [saga.cast.barb]."
    show old_anon 604
    show old_barb 27 at face_right
    with dissolve
    barb "How are you doing over there [saga.cast.mia]?"
    show old_barb 26
    show old_mia 12b at old_right
    show old_mia scraps 1 as scraps at old_right, pos(.568)
    with dissolve
    mia "Uhh..."
    mia "... I'm just, sorta making a mess, really..."
    show old_mia 8b
    show old_barb 27
    barb "Hehe, you just can't help but be adorable, can you?"
    show old_barb 26
    show old_mia 8
    mia "..."
    show old_barb 11 with dissolve
    barb "What do you think of [saga.cast.anon]'s collage?"
    show old_barb 10
    show old_mia 8b
    mia "..."
    show old_mia 10
    mia "It's very... umm... captivating?"
    show old_barb 11
    show old_mia 8b
    barb "That's a very good choice of words, dear!"
    show old_barb 10
    show old_mia 12
    mia "I should probably go take a shower..."
    show old_barb 11
    barb "Hehe, that's a good idea."
    show old_barb 13
    show old_mia 8b
    barb "Would you like me to come with and wash your back?"
    show old_barb 12
    show old_mia 56 with dissolve
    mia "N-no, that's okay. I'd prefer to shower alone."
    show old_barb 13
    show old_mia 55
    barb "Suit yourself, cutie pie."
    show old_barb 12
    show old_mia 56
    mia "See ya, [saga.cast.anon]."
    show old_mia 55
    show old_anon 605
    anon "Bye, [saga.cast.mia]."
    hide old_mia
    hide scraps
    with dissolve
    pause
    show old_barb 4 at center, face_left
    show old_anon 1
    with dissolve
    label bar03_art2.cookie hide:
    barb "You know, I'm very pleased with your progress, [saga.cast.anon]."
    show old_barb 3
    show old_anon 2
    anon "Yeah, I'm having a good time!"
    show old_anon 1
    show old_barb 4
    barb "I've always found it so exciting, watching a young artist at work!"
    barb "Girls are really drawn to men with talent."
    show old_anon 2
    show old_barb 3
    anon "They are?"
    show old_anon 1
    show old_barb 4
    barb "Oh yes! You keep coming to me for sessions and you'll have to fight them off with a stick."
    show old_barb 5 with dissolve
    show old_anon 12
    anon "Heh, I dunno..."
    show old_barb 6 with dissolve
    pause
    show old_barb 7
    pause
    show old_barb 9 with dissolve
    barb "{i}*Gulp*{/i}"
    show old_anon 23
    show old_barb 12 with dissolve
    anon "( !!! )" with hpunch
    show old_anon 10
    anon "... Did you just swallow that entire thing?"
    show old_anon 11
    show old_barb 13
    barb "... Maybe."
    show old_barb 12
    show old_anon 10
    anon "Where did you learn to do that?!"
    show old_anon 11 behind old_barb
    show old_barb 57 at pos(.46)
    with dissolve
    barb "Oh, honey. I have lots of talents you don't know about."
    barb "I spent a year in India studying Tantric sex with Buddhist monks."
    barb "They taught me how to overcome my gag reflex."
    show old_anon 10
    show old_barb 56b behind old_anon at pos(.41)
    with dissolve.nowait
    anon "That's pretty cool!"
    show old_anon 11
    show old_barb 56
    barb "Isn't it?"
    show old_barb 11 at center with dissolve
    barb "Oh my, it's getting late."
    barb "You'd better get yourself home."
    show old_barb 10
    show old_anon 2
    anon "Yeah, that's probably a good idea."
    anon "Thanks for the lesson, [saga.cast.barb]."
    show old_anon 1
    show old_barb 58 with dissolve
    barb "Oh, remember to pick up some of that quinoa I mentioned next time you're at the store!"
    barb "It's really healthy for you, [saga.cast.anon], and I want you to try it!"
    show old_anon 2
    show old_barb 10 with dissolve
    anon "Okay, [saga.cast.barb]."
    show old_barb 10 at face_right, pos(.55)
    hide old_anon
    with dissolve
    pause
    return


label bar03_art2.hall1:
    scene school_hall1 at stage(.32, .475, 2.35)
    show anon a_mags_stack o_right at left with dissolve
    pause
    becca "What are you doin-"
    show anon f_surprised m_teeth
    show becca e_sw f_disgusted_surprised at right with dissolve.nowait
    becca "Eeeewwwww!!!"
    becca e_w f_disgusted "Are you just walking around with those, you perv?!"
    anon f_confused -m_teeth "What?!"
    show anon e_s
    pause
    anon e_w f_worried_surprised "No! I mean, they're not- These are for an art proj-"
    becca "Whatever. You're disgusting!"
    hide becca
    with dissolve.nowait
    anon e_osw f_sad "{i}*Sigh*{/i}"
    hide anon with dissolve
    return


label bar03_art2.rails:
    scene camera at stage
    show anon a_mags_stack e_s o_right with dissolve
    anon @ -m_talk "( I should hurry back to art class with these magazines. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
