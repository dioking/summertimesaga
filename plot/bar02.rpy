label bar02_intro:
    anon f_calm "Ready to get started?"
    barb "Just about..."
    barb "... But there's actually something I wanted to discuss with you first."
    anon "Oh?"
    barb "I think we should get you a partner for these sessions, what do you think?"
    anon f_confused "A partner?"
    barb "Yeah, somebody to work alongside you and bounce ideas back and forth!"
    anon f_calm "Sure, okay."
    anon f_confused "Did you have anyone in mind?"
    barb a_think e_ssw f_pensive @ -m_talk "Hmm..."
    barb "Well, my initial thought is [saga.cast.eve]. She's a talented artist just like yourself..."
    barb "... But I doubt she'd have time with all her musical studies."
    pause
    barb a_side e_w f_curious "Do you think [saga.cast.mia] would be interested?"
    show anon f_surprised
    barb f_calm "She's just such a cutie pie, isn't she?"
    anon f_shy "Err, yeah. I suppose."
    barb @ f_happy "Great! Well, why don't you go talk to her?"
    barb "Tell her I said to get her cute butt in here!"
    anon f_surprised @ -m_talk "..."
    hide anon with dissolve
    return


label bar02_intro.area:
    anon a_fists_low "I'm anxious to get started on our art projects, [saga.cast.barb]!"
    barb "I appreciate your enthusiasm, dear... but I'm afraid it'll have to wait until after class."
    show anon a_side f_worried
    barb "Come see me in my office, alright?"
    anon f_shy "R-right. Will do!"
    hide anon with dissolve
    return


label bar02_mia:
    show old_anon 10
    anon "Hey, so uhh... [saga.cast.barb] asked me to come talk to you."
    show old_anon 11
    show old_mia 10
    mia "Really?"
    show old_anon 10
    show old_mia 7
    anon "Yeah, she wants you to be my partner for some private art sessions."

    if saga.cast.anon.chr < 3:
        jump bar02_mia.fail

    anon "I'd really like you to come help, [saga.cast.mia]."
    show old_anon 5
    show old_mia 12
    mia "You would?"
    show old_mia 8
    show old_anon 29 with dissolve
    anon "Totally."
    show old_anon 3
    show old_mia 8b
    mia "Hmm..."
    pause
    show old_mia 10
    mia "Okay!"
    show old_anon 13
    with dissolve.nowait
    mia "I'll come, for you."
    show old_mia 7
    show old_anon 14
    anon "Sweet! Thanks, [saga.cast.mia]!"
    show old_anon 13
    show old_mia 9
    mia "Hehe, no problem."
    show old_mia 7
    show old_anon 14
    anon "So, I'll see you there?"
    show old_anon 13
    show old_mia 10
    mia "You bet!"
    hide old_mia
    hide mia_labcoat
    with dissolve
    anon "( I'm glad [saga.cast.mia] agreed to help. )"
    anon "( I should let [saga.cast.barb] know. )"
    hide old_anon with dissolve
    return True


label bar02_mia.barb:
    anon f_calm "About that art contest-"
    barb f_confused "Where's [saga.cast.mia]?"
    anon f_worried "Oh, uhh... I haven't convinced her yet."
    barb f_calm "Well, get a move on, [saga.cast.anon]!"
    barb "We need her enthusiasm if we're gonna win this thing!"
    hide anon with dissolve
    return


label bar02_mia.fail:
    anon "She's pretty adamant it needs to be you."
    show old_anon 11
    show old_mia 12
    mia "... But I'm not even very good at art."
    show old_anon 10
    show old_mia 8
    anon "You can't be that bad..."
    show old_anon 11
    show old_mia 12
    mia "Trust me, I'm really bad!"
    mia "You should find somebody else."
    mia "Besides, my mom would just say no."
    show old_anon 10
    show old_mia 8
    anon "Oh, okay then."
    hide old_anon with dissolve
    return


label bar02_barb(when):
    anon f_calm "[saga.cast.mia] has agreed to be my partner for your lessons."
    barb "Oh, that's wonderful news!"
    barb "Well done, [saga.cast.anon]."

    if when == 1:
        barb "I'll be expecting you both after class tomorrow."
    else:
        barb "I'll be expecting you both after class on [saga.time.dow + when]."

    anon "Y-yes, ma'am."
    hide anon with dissolve
    return


label bar02_barb.mia:
    show old_anon 2
    anon "Thanks again for agreeing to be my partner in art class."
    show old_anon 1
    show old_mia 10
    mia "You're welcome."
    show old_mia 7
    show old_anon 2
    anon "I'm really glad [saga.cast.barb] chose you."
    show old_anon 1
    show old_mia 10
    mia "Aww, really?"
    mia "Then I'm glad too!"
    show old_mia 7
    return


label bar02_pause:
    return


label bar02_pause.barb(when):
    anon f_confused "When did you say [saga.cast.mia] and I should come for the private lesson?"

    if when == 1:
        barb "I'm expecting you both after class tomorrow."
    else:
        barb "I'm expecting you both after class on [saga.time.dow + when]."

    anon f_calm "We'll be there!"
    return


label bar02_pause.mia(when):
    show old_anon 2

    if when == 1:
        anon "Tomorrow afternoon should be interesting."
    else:
        anon "[saga.time.dow + when] afternoon should be interesting."

    show old_anon 1
    show old_mia 12

    if when == 1:
        mia "Tomorrow afternoon?"
    else:
        mia "[saga.time.dow + when] afternoon?"

    show old_mia 8
    show old_anon 2
    anon "Our private lession with [saga.cast.barb]."
    show old_anon 1
    show old_mia 10
    mia "Oh, right, of course."
    show old_mia 7
    show old_anon 2
    anon "Not getting cold feet are you?"
    show old_anon 1
    show old_mia 10
    mia "No way! I'll be there."
    show old_mia 7
    return


label bar02_delay:
    scene camera at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( It's time for my art lesson with [saga.cast.barb]. )"
    anon a_side e_w f_calm @ -m_talk "( I should head on over to her classroom. )"
    hide anon with dissolve
    return


label bar02_delay.bag:
    scene park_main at stage(.65, .575, 7)
    show anon a_pocket e_sw f_confused at right with dissolve
    anon @ -m_talk "( Hmm, what's this backpack doing out here? )"
    show anon a_reach e_s f_calm p_bend
    pause
    anon a_backpack_eve_give e_sw -p_bend @ -m_talk "( I think this belongs to [saga.cast.eve]... )"
    anon @ -m_talk "( ... Perhaps I should return it to her. )"
    hide anon with dissolve
    return


label bar02_delay.barb:
    anon f_confused "You ready to get to work, [saga.cast.barb]?"
    barb @ f_happy "Heh, love the enthusiasm ..."
    barb "... But a good artist also requires patience."
    show anon a_rub
    barb a_finger "Take this time to reflect upon the mighty oak tree..."
    barb "... So full of patience and resilience."
    show barb a_hip
    pause
    barb "It will illustrate the importance of grounding oneself in the present."
    anon a_side "Umm, okay?"
    barb "The present being too early for our private lessons."
    anon f_shy "Oh, I see."
    barb a_palette_hold "Return here this afternoon, okay?"
    anon f_calm "Can do!"
    return


label bar02_delay.eve:
    anon f_shy "Hey, so... I found this in the park."
    anon "It's yours, right?"
    eve f_surprised "You've got my bag!"
    eve f_happy "Awesome, [saga.cast.anon]... thank you so much!"
    anon f_calm "You're welcome."
    eve f_nervous "Now I just hope no one stole anything."
    return


label bar02_delay.mia:
    show old_anon 2
    anon "Don't forget, we've got that private lesson with [saga.cast.barb] this afternoon."
    show old_anon 1
    show old_mia 10
    mia "Do I need to bring anything?"
    show old_mia 7
    show old_anon 2
    anon "Just yourself, I think."
    show old_anon 1
    show old_mia 10
    mia "Hehe, okay."
    show old_mia 7
    return


label bar02_art1:
    call shot.school_art_barb
    show old_barb 2 at old_left
    with None
    show old_mia 7 at old_right, pos(.59)
    show old_anon 1 at old_right
    with dissolve
    barb "Hey there, cutie pie!"
    show old_barb 1
    show old_mia 56 with dissolve
    mia "... Oh, umm. H-hello."
    show old_barb 2
    show old_mia 55
    barb "I'm so glad, [saga.cast.anon] convinced you to join us!"
    show old_barb 1
    show old_mia 56
    mia "Hehe, yeah... He said you guys really needed my help?"
    show old_barb 2
    show old_mia 55
    barb "We surely do!"
    show old_barb 1
    show old_anon 2
    show old_mia 8b with dissolve
    anon "So are we ready to start now?"
    show old_anon 1
    show old_barb 11 with dissolve
    barb "Yup! Why don't you both get out your art pads and have a seat opposite each other."
    show old_anon 2
    show old_barb 10
    anon "Okay."
    show old_mia 8
    show old_anon 596 with dissolve
    mia "..."
    show old_mia 12
    mia "Umm, question..."
    show old_mia 8
    show old_barb 11
    barb "Yes, dear?"
    show old_mia 12
    show old_barb 10
    mia "What if I don't have an art pad?"
    show old_mia 8
    show old_barb 25
    barb "Oh, right."
    show old_barb 25b
    barb "Well, usually I'd provide you with one of those..."
    show old_barb 25
    barb "... But I'm afraid we've exhausted our stores."
    show old_barb 24
    show old_anon 598
    anon "That sucks!"
    show old_anon 596
    show old_mia 12b
    mia "Oh well, it's no big deal. I'm not very good at drawing anyways..."
    show old_mia 10
    mia "I'll just watch."
    show old_mia 7
    show old_barb 11
    barb "Nonsense!"
    barb "We'll get you one!"
    show old_barb 27 with dissolve
    barb "[saga.cast.anon], why don't you go ask [saga.cast.eve] if we can borrow one of hers."
    show old_barb 26
    show old_anon 598
    anon "... Y-yeah, okay!"
    show old_barb 27
    show old_anon 596
    barb "See, [saga.cast.anon] to the rescue!"
    show old_anon 1
    show old_barb 11
    with dissolve
    barb "We'll just stay here and have some girl talk."
    show old_barb 13
    barb "Right, cutie pie?"
    show old_barb 12
    show old_mia 56 with dissolve
    mia "Heh, okay..."
    show old_mia 55
    show old_anon 2
    anon "Be right back."
    hide old_anon with dissolve
    return


label bar02_art1.rails:
    scene camera at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( Don't want to keep them waiting... )"
    anon @ -m_talk "( ... Best hurry to the art room. )"
    hide anon with dissolve
    return


label bar02_eve1:
    call shot.school_hall1e_eve
    show eve a_shy at right
    show anon a_wave o_right at left with dissolve
    anon "Hey [saga.cast.eve]."
    anon "I need to ask you for a favor."
    show anon a_side
    eve f_confused "Oh?"
    anon "You see, I'm kinda helping [saga.cast.barb] with something, and we need your art pad."

    if saga.prop.bag_eve in saga.cast.eve:
        eve a_backpack e_s f_happy "I should have one right here in my bag..."
        label bar02_eve1.merge:
        pause
        show anon e_w f_confused
        eve f_pensive ".. Unless..."
        show anon e_sw
        pause
        show anon e_w f_worried
        eve a_backpack_01 "... Hmm, it's not here."
        show eve a_backpack_shy e_w f_calm
        anon f_confused "No?"
        jump bar02_eve2.merge

    eve f_calm "Well, that's no problem."
    eve "You just have to help me find my backpack first."

    if saga.prop.bag_eve in saga.cast.anon:
        anon f_surprised @ -m_talk "Hmm."
        show anon a_backpack e_s f_calm
        show eve f_confused
        pause
        show eve e_sw f_surprised
        anon a_backpack_eve_give e_w "... Look what I found in the park this morning!"
        show eve e_w
        pause
        eve e_sw "How did-"
        show anon f_confused
        show eve e_w
        pause
        eve f_happy "Duuuude!"
        show anon a_side f_calm
        eve a_backpack_hold "Thanks, [saga.cast.anon]!"
        anon "No worries."
        show anon e_sw
        eve a_backpack e_s "I should have an artpad in here..."
        jump bar02_eve1.merge

    anon f_worried "You lost your backpack?"
    eve e_ssw f_nervous "Yeah..."
    eve e_w f_calm "My art pad should be inside it."
    anon "Where was the last place you remember having it?"
    eve @ e_nnw f_sad_pensive -m_talk "Hmm..."
    eve "Well, I think I had it when I went to hang out with the guys in the park last night."
    anon f_calm "Alright, I'm on it!"
    hide anon with dissolve
    return


label bar02_eve1.art:
    jump bar02_eve1.fence


label bar02_eve1.barb:
    call shot.school_art_barb
    show old_barb 13 at old_left
    show old_mia 55 at old_right, pos(.45)
    show old_anon 1 at old_right with dissolve
    barb "... You know, [saga.cast.mia]. I used to be friends with a girl who looked just like you!"
    show old_barb 12
    show old_mia 56
    mia "Really?"
    show old_barb 13
    show old_mia 55
    barb "Absolutely! Her name was Starchild, and we used to follow our favorite band all over the country."
    show old_barb 12
    show old_mia 12b with dissolve
    mia "Well, that sounds pretty neat!"
    show old_barb 13
    show old_mia 8b
    barb "Oh, it was!"
    barb "That girl always had the best drugs!"
    show old_barb 11
    barb "... And what a kisser! She could do things with her tongue that woul-"
    show old_anon 10
    show old_barb 10
    show old_mia 55 with dissolve
    anon "{i}*Ahem*{/i} Am I interrupting something?"
    show old_anon 11
    show old_mia 12 at face_right with dissolve
    mia "[saga.cast.anon], you're back!"
    show old_mia 12b
    mia "Thank goodness!"
    show old_mia 8b
    show old_barb 11
    barb "Did you manage to get [saga.cast.eve]'s art pad?"
    show old_anon 10
    show old_barb 10
    anon "No, sorry. I'm still working on it."
    show old_anon 11
    show old_barb 11
    barb "Tsk, well shoo then! We're having girl talk here..."
    show old_barb 10
    show old_anon 10
    anon "... A-alright. I'll be back."
    hide old_anon with dissolve
    show old_mia 12 at pos(.55) with dissolve
    mia "No! Wait! Hold up!"
    show old_mia 8
    pause
    show old_barb 13 at pos(.4) with dissolve
    barb "Now where was I?"
    show old_barb 12
    show old_mia 8b at face_left with dissolve
    mia "..."
    show old_barb 13
    barb "Oh, right! She could do things with her tongue that would make a whore blush!"
    show old_barb 12
    show old_mia 56 with dissolve
    mia "... Oh my."
    return


label bar02_eve1.fence:
    scene camera at stage
    show anon a_think f_pensive with dissolve
    anon @ -m_talk "( [saga.cast.eve] should still be hanging around the school somewhere... )"
    anon @ -m_talk "( Hopefully she'll have an extra art pad that [saga.cast.mia] can borrow. )"
    hide anon with dissolve
    return


label bar02_bag:
    scene park_main at stage(.65, .575, 7)
    show anon a_pocket e_sw f_confused at right with dissolve
    anon @ -m_talk "( Hmm... )"
    show anon a_reach e_s f_calm p_bend
    pause
    anon a_backpack_eve_give e_sw -p_bend @ -m_talk "( This is defintely [saga.cast.eve]'s backpack... )"
    show anon a_backpack_eve e_s
    pause
    anon a_backpack_eve_01 f_confused @ -m_talk "( ... I don't see her art pad though. )"
    anon a_backpack_eve_give e_sw @ -m_talk "( I should ask her about it when I return this. )"
    hide anon with dissolve
    return


label bar02_bag.eve:
    call shot.school_hall1e_eve
    show eve a_shy at right
    show anon a_rub f_confused o_right at left with dissolve
    anon "Where did you leave your backpack, again?"
    eve @ f_confused "I'm not entirely sure. I remember having it with me at the park last night."
    anon a_side f_calm "Okay, I'll check there!"
    hide anon with dissolve
    return


label bar02_bag.rails:
    scene camera at stage
    show anon a_think e_sw f_pensive with dissolve
    anon @ -m_talk "( [saga.cast.eve] said the last place she remembers having her bag was last night in the park. )"
    anon a_side e_w f_calm @ -m_talk "( I should head there and check it out. )"
    hide anon with dissolve
    return


label bar02_eve2:
    call shot.school_hall1e_eve
    show eve a_shy at right
    show anon a_pocket o_right at left with dissolve
    show anon a_backpack e_s
    show eve f_confused
    pause
    show eve e_sw f_surprised
    anon a_backpack_eve_give e_w "Look what I found!"
    show eve e_w
    pause
    eve e_sw "Did you just-"
    show anon f_confused
    show eve e_w
    pause
    eve f_happy "Niiiice!"
    show anon a_side f_calm
    eve a_backpack_hold "Thanks, dude!"
    anon "No worries. I couldn't find your art pad though."
    eve f_confused "It wasn't in my bag?"
    anon "Nope."
    label bar02_eve2.merge:
    eve a_backpack_shy f_calm "Weird."
    eve @ f_confused "I wonder if [saga.cast.chad] snatched it again?"
    anon f_worried "[saga.cast.chad]?"
    eve "Yeah, he digs my art."
    anon "Interesting..."
    anon f_calm "I'll go ask him."
    eve "Cool. See ya, [saga.cast.anon]."
    anon "See ya, [saga.cast.eve]."
    hide anon with dissolve
    return True


label bar02_eve2.rails:
    scene camera at stage
    show anon a_backpack_eve_give e_sw f_worried with dissolve
    anon @ -m_talk "( Hopefully [saga.cast.eve] will have some other idea where her artpad might be... )"
    anon f_happy @ -m_talk "( ... At least she'll be happy to have this back though. )"
    hide anon with dissolve
    return


label bar02_chad:
    call shot.school_hall1e_chad
    show chad a_fold o_right at left
    show old_anon 2 at old_right with dissolve
    anon "Hey man, I'm trying to find [saga.cast.eve]'s art pad."
    anon "She said you might have it."
    show old_anon 1
    chad "Yeah, that's right."
    show old_anon 10
    anon "So, could I get it from you?"
    show old_anon 11
    chad @ a_open "Tch, not for free, yo."
    anon "..."
    show old_anon 10
    anon "What do you want?"
    show old_anon 11
    chad f_happy "Man, [saga.cast.eve]'s a pretty dope artist, you know what I'm sayin'?"
    show old_anon 10
    anon "Yeah, so I hear."
    show old_anon 11
    chad "She's got this one drawin'..."
    chad "Shit is lit as fuck, man!"

    if saga.prop.sketch_waifu in saga.cast.anon:
        jump bar02_chad.alt

    chad "I thought it would be in her art pad but no dice."
    chad @ a_open "You gotta get me that drawin', dawg!"
    show old_anon 10
    anon "... And if I do, you'll give me the art pad?"
    show old_anon 11
    chad @ e_b m_laugh "Haaah, that's the deal, yo."
    chad "You down?"
    show old_anon 10
    anon "Sure. What's the drawing look like?"
    show old_anon 11
    chad "Ah, it's this self-portrait she did."
    chad "S'pose to be like an anime girl or somethin'."
    chad @ a_open "All I know is... it's fuckin' sexy, yo!"
    show old_anon 10
    anon "Any idea where it could be?"
    show old_anon 11
    chad f_calm "Mmm, man if I had to guess..."
    chad "I betcha she's keepin' that shit in her locker."
    show old_anon 2
    anon "Alright, I'll go take a look."
    show old_anon 1
    chad "Hurry back, man."
    hide old_anon with dissolve
    return


label bar02_chad.alt:
    show old_anon 612 with dissolve.nowait
    anon "You mean this one?"
    show old_anon 611
    chad "Lemme see that shit!"
    show old_anon 1
    show chad a_paper e_sw
    with dissolve
    pause
    chad "Doooope!"
    chad "Damn! Now that's a woman, yo!"
    show old_anon 2
    anon "Can I have that art pad now?"
    show old_anon 1
    chad e_w "Ah, yeah. My bad! I'm all over here droolin' and shit!"
    chad a_pad @ f_calm "Here ya go."
    show old_anon 598
    show chad a_paper e_sw
    with dissolve
    anon "Thanks, [saga.cast.chad]."
    show old_anon 596
    chad "Pleasure doin' business with ya."
    hide old_anon with dissolve
    return True


label bar02_chad.eve:
    call shot.school_hall1e_eve
    show eve a_shy at right
    show anon f_worried o_right at left with dissolve
    anon "Where did you say that art pad was again?"
    eve @ e_r f_annoyed "Oh, [saga.cast.chad] probably has it."
    eve "He digs my art."
    anon f_calm "Gotcha, thanks!"
    hide anon with dissolve
    return


label bar02_chad.rails:
    scene camera at stage
    show anon a_pocket o_right with dissolve
    anon @ -m_talk "( Guess I should go speak with [saga.cast.chad] regarding [saga.cast.eve]'s art pad. )"
    anon @ -m_talk "( I'm sure he's skulking around here somewhere. )"
    hide anon with dissolve
    return


label bar02_eve3:
    call shot.school_hall1e_eve
    show eve a_shy at right
    show anon a_uneasy f_worried o_right at left
    anon "Hey, so... umm, [saga.cast.chad] is kinda, holding your art pad hostage..."
    eve f_confused "Huh?!"
    anon f_shy "Yeah."
    anon a_side f_confused "He wants to trade it for some self portrait you did of yourself."
    eve f_disgusted "Ugh, he's so gross!"
    eve f_nervous "One second."
    hide eve with dissolve.nowait
    eve "Hey [saga.cast.chad], c'mere a sec."
    show school_hall1e -chad
    with dissolve.nowait
    chad "Yo, wha-"
    show anon a_surprised f_surprised
    chad "Ouch!" with hpunch
    show anon a_surprised_up m_teeth
    chad "What the-" with hpunch
    chad "W-what did I do?!"
    eve "You know what you did!"
    show anon a_surprised_up_both f_afraid
    eve "Give me back the art pad!"
    show anon a_shy_down m_talk
    pause
    show anon e_b f_hurt m_teeth
    chad "Oww!!!" with hpunch
    show anon e_w f_afraid
    chad "Alright, alright... here!"
    show anon f_surprised -m_teeth
    eve "Good."
    show anon a_side
    eve "And don't take it again, you creeper!!"
    chad "Fuckin' alright, sheesh!"
    show anon a_rub
    pause
    show eve a_artpad at pos(.6) with dissolve
    eve a_artpad_show "Here you go."
    anon "Wow, that was-"
    pause
    show anon e_sw
    pause
    show anon a_artpad_rub e_s
    show eve a_side
    pause
    anon a_artpad_catch e_w f_shy "I didn't know you could be so scary!"
    eve a_wave "Yeah, that was nothing."
    eve f_horny "He's lucky I'm not my sister; he'd be icing more than his balls right now."
    show eve a_side
    anon a_artpad_side "Heh, still that was impressive."
    eve a_shy f_happy "Thanks, [saga.cast.anon]."
    anon "N-no, thank you!"
    eve "Good luck with your art project."
    hide anon with dissolve
    return


label bar02_eve3.chad:
    call shot.school_hall1e_chad
    show chad a_fold o_right at left
    show old_anon 10 at old_right with dissolve
    anon "What did you want for that art pad again?"
    show old_anon 11
    chad "You forget or somethin'?"
    show old_anon 10
    anon "Yeah, kinda."
    show old_anon 11
    chad "Tch, I want that self-portrait [saga.cast.eve] did."
    chad @ a_open "She's probably got it under wraps in her locker, know what I'm sayin'?"
    show old_anon 10
    anon "Alright."
    hide old_anon with dissolve
    return


label bar02_eve3.locker:
    scene school_hall1e at stage(.25, .5, 2)
    show anon with dissolve

    if saga.prop.key_school in saga.cast.anon:
        anon @ -m_talk "( My sneak could be one hundred and I'd still be noticed... )"
    else:
        anon @ -m_talk "( I couldn't open it even if I wanted to... )"

    anon @ -m_talk "( ... Maybe I should speak with [saga.cast.eve] about this [saga.cast.chad] situation. )"
    hide anon with dissolve
    return


label bar02_eve3.rails:
    scene camera at stage
    show anon a_pocket o_right with dissolve
    anon @ -m_talk "( I should probably speak with [saga.cast.eve] about this [saga.cast.chad] situation. )"
    hide anon with dissolve
    return


label bar02_art2:
    call shot.school_art_barb
    show old_barb 46 at old_left
    show old_mia 55 at old_right, pos(.435)
    show old_anon 11 at old_right with dissolve
    barb "... Hmm, I think my favorite one is the {i}Praia do Abricó{/i}."
    show old_barb 11 with dissolve
    barb "It's back home in Rio de Janeiro."
    show old_barb 10
    show old_mia 56
    mia "Oh, I dunno..."
    mia "... I don't think I'm brave enough for a nude beach."
    show old_barb 13
    show old_mia 55
    barb "Oh, sure you are, cutie pie!"
    barb "Nobody should be ashamed of their body. The human form is a work of art after all..."
    show old_barb 13
    barb "... Especially yours."
    barb "You're just absolutely gorgeous, [saga.cast.mia]!"
    show old_barb 12
    show old_mia 56
    mia "Wow, I... uhh..."
    show old_anon 10
    anon "{i}*Ahem*{/i}"
    show old_anon 11
    show old_mia 12b at old_left, pos(.435) with dissolve
    mia "Oh, [saga.cast.anon], thank goodness you're back!"
    show old_mia 8b at old_right, pos(.59) with dissolve
    show old_anon 2
    anon "You guys having fun?"
    show old_anon 1
    show old_barb 11
    barb "We're having a blast!"
    barb "I assume you got the art pad?"
    show old_barb 10
    show old_anon 598 with dissolve
    anon "Yup, I got it right here."
    show old_anon 596
    show old_barb 11 with dissolve
    barb "Good work, [saga.cast.anon]!"
    barb "We should get started now."
    barb "I want both of you to take a seat opposite one another."
    show old_barb 58 with dissolve
    barb "... Because today you're going to be drawing portraits of each other using pencil and paper."
    show old_anon 598
    show old_barb 10 with dissolve
    anon "So you want me to draw [saga.cast.mia]?"
    show old_anon 596
    show old_barb 11
    barb "That's right and [saga.cast.mia], I want you to draw [saga.cast.anon]."
    show old_barb 10
    show old_mia 12b
    mia "I'll try..."
    show old_barb 13
    show old_mia 8b
    barb "You're just too adorable, aren't you?"
    show old_barb 12
    show old_mia 55
    with dissolve
    barb "Don't worry, there's no such thing as bad art!"
    show old_mia 56
    mia "... If you say so."
    show old_mia 55
    show old_barb 11
    barb "Now let's get started."

    scene mono school_art_mia_drawing
    mono "I'd always enjoyed art, but drawing a live model was a totally different experience." with fade
    mono "I still feel so lucky that [saga.cast.barb] chose [saga.cast.mia] to be my partner..."
    mono "... She was really cute!"

    call shot.school_art_barb
    show old_mia 8b at old_right
    show old_barb 11 at old_right, pos(.5)
    show old_anon 1 at old_left
    with fade
    barb "Well done, both of you!"
    barb "It's such a beautiful drawing, [saga.cast.anon]!"
    show old_barb 28 at pos(.48) with dissolve
    barb "I'm feeling very good about our chances in this art contest..."
    barb "You should show [saga.cast.mia]."
    show old_barb 12 at face_right, pos(.425)
    show old_anon 560
    show old_mia 69
    with dissolve.nowait
    mia "{i}*Gasp*{/i}"
    show old_mia 10
    mia "Wow! It's so good!"
    show old_mia 7
    show old_barb 11
    barb "Isn't it?"
    show old_barb 13
    barb "It's almost as beautiful as the real thing!"
    show old_barb 13c
    barb "Don't you think, [saga.cast.anon]?"
    show old_anon 561
    show old_barb 12b
    anon "Y-yeah, almost..."
    show old_anon 560
    show old_barb 12
    show old_mia 56 with dissolve
    mia "Aww, thanks, [saga.cast.anon]."
    show old_mia 55
    show old_barb 13
    barb "Alright then, let's see how you did [saga.cast.mia]?"
    show old_mia 59b with dissolve
    mia "Mmm, no. That's okay. I'd rather not."
    show old_barb 11
    show old_mia 59d
    barb "Oh, pish posh! Don't play so hard to get!"
    barb "Remember, there's no such thing as bad art..."
    show old_barb 10
    show old_mia 59e
    mia "... Okay."
    show old_mia 59c
    show old_barb 24
    barb "..."
    show old_mia 59
    mia "I told you, I'm not very good..."
    show old_mia 59c
    show old_barb 25
    barb "Well no, it's... interesting..."
    show old_barb 11
    barb "There's definitely room for improvement."
    show old_anon 561
    show old_barb 10
    anon "I like it, [saga.cast.mia]!"
    show old_anon 560
    show old_mia 57
    mia "You do?"
    show old_anon 561
    show old_mia 58
    anon "Yeah, it's really cute!"
    show old_anon 560
    show old_barb 11
    barb "There, now see, [saga.cast.mia]. [saga.cast.anon] likes it!"
    show old_barb 10
    mia "..."
    show old_barb 11
    barb "Well, I think we had better call it there for today."
    barb "We made some really good progress, you two!"
    show old_barb 58 with dissolve
    barb "Make sure you both get lots of rest and don't forget to do those meditations I taught you!"
    show old_barb 10 with dissolve
    show old_anon 2
    with dissolve
    anon "Alright, I'll try, [saga.cast.barb]."
    anon "See ya, [saga.cast.mia]!"
    show old_anon 1
    show old_mia 56 with dissolve
    mia "Bye, [saga.cast.anon]."
    hide old_anon with dissolve
    return


label bar02_art2.rails:
    scene camera at stage
    show anon a_artpad e_sw with dissolve
    anon @ -m_talk "( Man, what a hassle! )"
    anon a_artpad_side e_w @ -m_talk "( Time to return to [saga.cast.mia] and [saga.cast.barb]. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
