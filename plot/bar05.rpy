label bar05_setup:
    return


label bar05_setup.barb:
    anon f_worried "Are we still going to be able to enter the contest?"
    barb f_sad "Yes, I think so..."
    barb "... I just need a little time to prepare things."
    barb f_calm "Come see me tomorrow."
    return


label bar05_barb1(when):
    anon f_confused "So we're all set to go on the contest painting?"
    barb "There's still a few small preparations that need to be done..."

    if when == 1:
        barb "... Let's say we all get together tomorrow afternoon and we can sort it all out."
    else:
        barb "... Let's say we all get together on [saga.time.dow + when] afternoon and we can sort it all out."

    anon f_calm "Alright, sounds good."
    return


label bar05_pause1:
    return


label bar05_pause1.barb(when):
    if when == 1:
        anon f_confused "We're still meeting tomorrow afternoon, right?"
    else:
        anon f_confused "We're still meeting on [saga.time.dow + when] afternoon, right?"

    barb @ -m_talk "Mhmm."
    anon f_calm "Cool cool."
    return


label bar05_pause1.mia(when):
    show old_anon 10

    if when == 1:
        anon "Did [saga.cast.barb] speak with you about tomorrow afternoon?"
    else:
        anon "Did [saga.cast.barb] speak with you about [saga.time.dow + when] afternoon?"

    show old_anon 1
    show old_mia 10
    mia "Yup, I'll be there."
    show old_mia 7
    return


label bar05_delay1:
    scene camera at stage
    show anon a_think e_sw f_pensive with dissolve
    anon @ -m_talk "( I'd better get to art class so we can begin preparations on the contest painting. )"
    anon a_side e_w f_worried @ -m_talk "( I hope it's nothing too complicated. )"
    hide anon with dissolve
    return


label bar05_delay1.barb:
    anon f_confused "You wanted to meet here this afternoon, right?"
    barb "That's correct."
    anon f_calm "Okay, sounds good."
    return


label bar05_delay1.mia:
    show old_anon 2
    anon "I wonder what kind of preparations are needed before I can start painting?"
    show old_anon 1
    show old_mia 12b
    mia "Who knows?"
    show old_mia 8b
    show old_anon 2
    anon "Yeah, I guess we'll find out this afternoon, huh?"
    show old_anon 1
    return


label bar05_art1:
    call shot.school_art_barb
    show old_anon 11 at face_left, pos(.6) with dissolve
    anon "( Huh? Where is everyone... )"
    show old_anon 5 at face_left, pos(.25) with dissolve.nowait
    pause
    show old_mia 6 at pos(.45) with dissolve.nowait
    mia "Sorry, I'm-"
    show old_mia 2
    show old_anon 11 at face_right, pos(.25)
    with dissolve.nowait
    mia "..."
    show old_anon 10
    anon "Hi [saga.cast.mia], I thought we were doing the contest painting today?"
    show old_anon 5
    show old_mia 6
    mia "That's what [saga.cast.barb] said."
    show old_mia 2
    show old_anon 10
    anon "Hmm, well, where is she?"
    show old_anon 5
    show old_mia 6
    mia "I dunno."
    show old_mia 2
    anon "..."
    show old_mia 6
    mia "Hey, [saga.cast.anon]..."
    show old_mia 2
    show old_anon 10
    anon "Yeah?"
    show old_anon 5
    show old_mia 6b
    mia "I wanted to apologize for the other day."
    show old_mia 2
    show old_anon 10
    anon "Huh?"
    show old_anon 5
    show old_mia 6
    mia "You know, the whole naked thing..."
    show old_mia 6b
    mia "... And the honking."
    show old_mia 2
    anon "..."
    show old_mia 6
    mia "I really don't know what got into me!"
    show old_mia 2
    show old_anon 2
    anon "It's alright, [saga.cast.mia]. I had a good time."
    show old_anon 1
    show old_mia 6
    mia "You did?"
    show old_mia 1
    show old_anon 2
    anon "Yeah!"
    anon "I thought you were having fun, too?"
    show old_anon 1
    show old_mia 4
    mia "Heh, yeah. It was fun..."
    show old_mia 6b
    mia "... It's just..."
    show old_mia 6
    mia "... It wasn't very ladylike."
    mia "So, I'm sorry, [saga.cast.anon]."
    show old_mia 2
    show old_anon 2
    anon "[saga.cast.mia], really, it's okay."
    anon "I like that side of you."
    show old_anon 1
    show old_mia 4
    mia "You do?"
    show old_mia 1
    show old_anon 2
    anon "Yeah, we were all just having fun!"
    anon "There's nothing wrong with that."
    show old_anon 1
    show old_mia 3
    mia "... Yeah, I guess you're right."
    show old_mia 4
    mia "Thanks, [saga.cast.anon]!"
    show old_mia 1
    show old_anon 2
    anon "Oh, here she comes!"
    show old_mia 4 behind old_anon at face_right, pos(.42)
    show old_barb 24 at old_right
    show old_anon 1
    with dissolve.nowait
    mia "Hey, [saga.cast.barb]!"
    mia "Everything alright?"
    show old_mia 1
    show old_barb 25
    barb "Hey, cutie pie."
    show old_barb 25b
    barb "Ugh, I was just in Mrs. [saga.cast.ursula.clan]'s office..."
    show old_barb 25
    barb "She was going on and on about that portrait we promised her."
    show old_barb 24
    show old_anon 10
    anon "You mean we're really doing that?"
    show old_anon 11
    show old_barb 25b
    barb "I'm afraid so."
    show old_barb 25
    barb "She's got some really specific demands too..."
    show old_barb 24
    show old_mia 6
    mia "... But what about the contest?"
    mia "[saga.cast.anon]'s still gonna paint something for that, right?"
    show old_mia 2
    show old_barb 23
    barb "I'm afraid not... urgh, I had it all planned out too!"
    show old_barb 25b
    barb "The perfect theme."
    show old_barb 25
    barb "The perfect model."
    show old_mia 5
    barb "It was a sure-fire winner!"
    show old_barb 23
    barb "But Mrs. [saga.cast.ursula.clan] has gone and thrown a wrench into the whole thing."
    show old_mia 1
    show old_barb 22
    show old_anon 10
    anon "So, what are we gonna do, we don't have time to do two paintings!"
    show old_anon 11
    show old_barb 25
    barb "We'll just have to roll with the punches and hope that Mrs. [saga.cast.ursula.clan]'s painting will be good enough to win the contest."
    show old_anon 10
    show old_barb 24
    anon "We're gonna submit a painting of Mrs. [saga.cast.ursula.clan] to the contest?!"
    show old_anon 11
    show old_mia 2
    show old_barb 25b
    barb "Just do your best, [saga.cast.anon]."
    show old_mia 6
    show old_barb 24
    mia "At least this should be interesting to watch."
    barb "..."
    show old_mia 2
    show old_barb 25
    barb "Unfortunately, cutie pie. You and I are gonna have to sit this one out."
    barb "Only [saga.cast.anon] is allowed to be in the room."
    show old_barb 25b
    barb "That's another one of Mrs. [saga.cast.ursula.clan]'s stipulations."
    show old_anon 10
    show old_barb 24
    anon "Seriously?!"
    show old_barb 25
    show old_anon 11
    barb "Believe me, I'm not happy about it either."
    show old_barb 23
    barb "Damn it!"
    barb "I was just starting to feel secure about my job again and this had to go and happen."
    show old_barb 22
    show old_mia 3
    mia "Don't worry, [saga.cast.barb]. I'm sure [saga.cast.anon] will find a way to make it work!"
    show old_mia 5
    anon "..."
    show old_barb 25
    barb "I hope you're right."
    show old_mia 1
    show old_barb 25b
    barb "We'd best start with the preparations."
    show old_barb 24
    show old_anon 10
    anon "Preparations?!"
    show old_barb 25
    show old_anon 11
    barb "Oh yes, we have a lot of work to do before you can start painting."
    show old_barb 25b
    barb "Our supply shelves are completely barren!"
    show old_barb 25
    barb "We're gonna need some paint and a canvas."
    show old_anon 10
    show old_barb 24
    anon "Where are we supposed to find stuff like that?"
    mia "..."
    show old_barb 25
    barb "Well, I could probably make us a canvas with enough white linens."
    show old_barb 24
    show old_anon 10
    anon "For real?"
    show old_anon 11
    show old_mia 4
    mia "I know where we can get that!"
    show old_anon 10
    show old_mia 1
    anon "Huh?"
    show old_barb 25
    show old_anon 11
    barb "Really?"
    show old_mia 3
    mia "Yeah, not a problem. My church has a {i}ton{/i} of white linens."
    show old_mia 5
    show old_anon 10
    anon "... And you think they'd just let us have some?"
    show old_mia 3
    show old_anon 11
    mia "Yeah, I think so!"
    mia "Giving to the needy is a pretty big principle of Catholicism after all."
    show old_mia 5
    show old_anon 10
    anon "Huh, well, that's convenient!"
    show old_mia 4
    show old_anon 11
    mia "I'll get right on it."
    show old_mia 1
    show old_barb 25
    barb "No, hold on."
    barb "[saga.cast.anon] can handle the linens."
    show old_barb 24
    show old_anon 10
    anon "... I can?"
    show old_barb 25
    show old_anon 11
    barb "Sure, just tell the church people [saga.cast.mia] sent you."
    show old_barb 28b with dissolve.nowait
    barb "[saga.cast.mia], if I give you the last of my school funds, do you think you can get us some basic paint colors?"
    show old_barb 24
    show old_mia 66
    with dissolve.nowait
    mia "M-me?"
    show old_mia 68
    show old_barb 25
    with dissolvefast.nowait
    barb "You might have to charm the proprietor a bit to get them at an affordable price."
    show old_barb 24
    show old_mia 67
    mia "Oh, umm... I dunno..."
    mia "... I've never had to do anything like that!"
    show old_mia 68
    show old_barb 11
    barb "Are you kidding?"
    show old_mia 8b
    with dissolve.nowait
    barb "For a cutie pie like you, it'll be a piece of cake!"
    show old_barb 10
    mia "..."
    show old_barb 28 behind old_mia at face_left, pos(.62)
    show old_mia 70
    with dissolve.nowait
    barb "I know you can do it, [saga.cast.mia]. So certainly, if I know it, you know it too!"
    show old_barb 10
    show old_mia 12b
    with dissolve.nowait
    mia "A-alright, I'll try."
    show old_mia 8b
    show old_barb 11
    barb "Atta girl!"
    show old_barb 10
    hide old_mia
    show old_anon 10
    with dissolve.nowait
    anon "Should I go with her?"
    show old_anon 5
    show old_barb 25
    barb "There's no time, [saga.cast.anon]!"
    barb "Focus on the linens."
    show old_barb 24
    show old_anon 10
    anon "Ugh, fine."
    hide old_anon with dissolve
    return


label bar05_art1.rails:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( No time to dawdle! )"
    anon @ -m_talk "( Let's hurry to the art room. )"
    hide anon with dissolve
    return


label bar05_ang:
    show old_anon 2
    anon "Umm, I'm doing an art project for school, and we need some white linens."
    anon "My friend [saga.cast.mia] said you might be willing to spare some."
    show old_anon 1
    show old_ang 2
    ang "Hmm, [saga.cast.mia] sent you?"
    ang "She's such a devout young woman."
    ang "I suppose I could give you some of our old baptismal robes. They're fraying anyways..."
    show old_ang 1
    show old_anon 2
    anon "That should work just fine! Thank you so very much."
    show old_anon 1
    show old_ang 2
    ang "If you want to thank me, start showing up for service on Sundays."
    show old_ang 1
    show old_anon 5
    anon "..."
    show old_ang 2
    ang "Now wait here while I go and get them."
    hide old_ang
    show old_anon 11 at face_left
    with dissolve.nowait
    anon "( Huh, well, that was easy. )"
    anon "..."
    show old_anon 4 at face_right
    with dissolve.nowait
    anon "( I thought for sure she'd want something in return... )"
    pause
    show old_anon 11
    show old_ang 40 at pos(.63)
    with dissolve
    pause
    show old_ang 41
    ang "Here ya go."
    show old_ang 2
    show old_anon 592
    with dissolve
    ang "Tell [saga.cast.mia] I expect to see her early for next service! She's long past due for confession."
    show old_anon 593
    show old_ang 1
    anon "O-okay, I'll let her know."
    show old_anon 592
    ang "Hmm!"
    hide old_anon with dissolve

    scene church_nave at stage with fade
    show old_anon 591 at old_left with dissolve
    anon "... [saga.cast.mia] might end up fronting the bill on this one."
    anon "I'd better get these linens back to [saga.cast.barb]."
    hide old_anon with dissolve
    return


label bar05_ang.barb:
    anon f_confused "What did we need linens for again?"
    barb f_confused "To use as a canvas, did you bring them?"
    anon a_uneasy f_worried "No, I haven't gotten them yet."
    barb f_sad "There's no time to waste, [saga.cast.anon]!"
    barb "We gotta hurry up and get them from [saga.cast.mia]'s church if we wanna submit the painting in time for the contest!"
    show barb f_calm
    anon a_salute f_shy "Don't worry, I'm on it!"
    hide anon with dissolve
    return


label bar05_barb2:
    show anon a_backpack e_s f_calm
    pause
    show anon a_linens e_w f_worried
    barb f_curious @ e_wsw "Are those the linens?"
    anon "Yup, they're a little frayed. I hope that's okay?"
    barb f_calm "Ah, it shouldn't be a problem. Plenty of usable material there."
    anon a_side f_shy "Thank goodness."
    anon "So, now what?"
    barb f_sad "Now I have a very special task for you."
    barb "I need you to run down to Cosmic Cumics at the mall and pick up the costumes that [saga.cast.ursula] ordered."
    anon f_surprised "{i}Costumes{/i}?! As in plural?!"
    anon "I thought I was just painting [saga.cast.ursula]?"
    barb f_annoyed "Ugh, who knows what that crazy old witch is plotting?!"
    show anon f_worried
    barb f_sad "But whatever it is, you'd better hurry..."
    barb "... I've gotta get started making this canvas right away."
    anon "Okay."
    hide old_anon with dissolve
    return


label bar05_lily:
    anon "So, I was sent here to pick up some costumes for a [saga.cast.ursula]."
    lily f_happy "Ugh, thank god... I was worried that evil hag would be coming in herself to get them!"
    anon "You know [saga.cast.ursula]?"
    lily @ e_r f_bored "Well, duh."
    lily "She's only been the principal at school for the past two decades."
    anon "Oh, so you went there too?"
    lily @ -m_talk "Mhmm."
    lily f_shy "And lemme tell you, I was more than a little surprised when I saw her ordering something like this..."
    lily f_curious "... What kind of weird shit is she getting into over there?"
    anon f_worried "Oh, umm... [saga.cast.barb] has me painting a portrait of her for her office."
    lily f_surprised "No shit?!"
    anon "No shit."
    lily f_horny "I guess that would make you her {i}special project{/i} this year, huh?"
    anon f_confused "Yeah, I suppose so."
    lily f_curious "So how in the heck did she manage to rope [saga.cast.ursula] into her twisted little sexcapades?"
    anon f_surprised "... Wait, what?!"
    lily f_happy "Oh, you don't know?!"
    anon f_confused "Know what?"
    lily f_horny "How every few years, [saga.cast.barb] selects a talented young art student to {i}groom{/i} into her dirty little sex puppet?"
    anon a_surprised f_surprised @ -m_talk "( !!! )" with hpunch
    anon "Y-you, mean she wants to-"
    show lily e_b f_happy m_laugh
    anon a_point_self "W-with me?!"
    lily @ m_laugh "Hahahaha!"
    lily e_w -m_laugh "Ga-doy!!"
    anon a_uneasy f_worried of_blush "N-no, that can't be right..."
    anon "... She's just trying to help me cultivate my artistic talent!"
    lily @ e_b m_laugh "{i}*Snort*{/i}"
    lily "Yeah, right."
    lily f_horny "Has she had you {i}feel her shapes{/i} yet?"
    anon a_surprised_up_both -of_blush @ f_shocked m_open "{i}*Gasp*{/i}"
    show anon e_e f_surprised
    pause
    anon a_whisper e_w f_confused "How do you know about that?!"
    lily "Because she pulled the same stuff on me my senior year."
    anon a_side f_worried_surprised "Whoa, really?"
    pause
    lily f_curious "Who'd she choose to be your partner?"
    anon f_worried "My friend, [saga.cast.mia]."
    lily f_happy "Yup, always a girl and a boy together."
    anon f_confused "She did the same for you?"
    lily e_nw f_horny "Mhmm, Robbie [saga.cast.rhonda.clan]..."
    show anon f_worried_surprised
    lily of_blush "... He wasn't much to look at but boy did he ever have a great tongue!"
    anon a_rub f_worried "This is crazy!"
    lily e_w f_happy "Oh, don't get bent out of shape about it..."
    lily f_horny "... [saga.cast.barb] knows her stuff."
    show anon a_side f_shy
    lily @ e_b_w "You're in for a real treat!"
    pause
    show anon a_shy_neck e_ese f_surprised
    lily e_nw "I still think about our sessions sometimes, when the mood strikes."
    pause
    show anon a_side e_w f_shy
    lily e_w f_calm -of_blush "{i}*Ahem*{/i} Anyways!"
    lily @ f_happy "I'll be right back with those costumes."
    show lily o_right at pos(.95)
    pause
    hide lily
    with dissolve.nowait
    pause
    anon e_nw f_pensive @ -m_talk "( Now that I think about it, we {i}have{/i} been doing a lot of weird stuff with [saga.cast.barb] in those lessons... )"
    anon a_think f_shy of_blush @ -m_talk "( ... And that stuff with [saga.cast.mia] and [saga.cast.judith]. )"
    show anon d_hard
    pause
    anon f_pensive -of_blush @ -m_talk "( Nah, this is silly! )"
    anon e_sw @ -m_talk "( There's no way she'd wanna do... {i}that{/i} with a guy like me! )"
    anon a_surprised e_s f_surprised @ -m_talk "( !!! )"
    show anon e_w
    pause
    anon a_shy_down @ m_teeth "( Crap! She's coming over here! )"
    show lily a_costume_pharaoh_give at pos(.775)
    show anon f_worried_surprised
    lily "Here you are, sir."
    show lily a_side e_sw f_horny
    anon a_bag_comic_hold f_shy "Umm, thanks."
    anon f_confused "Do I owe you anything?"
    show anon f_worried
    lily e_w f_happy "Nope, it's all paid in full."
    lily "Tell [saga.cast.barb] that [saga.cast.lily] Padbury says, 'Hi.'"
    anon "Y-yeah, okay..."
    anon "... Um, bye!"
    hide anon
    with dissolve.nowait
    lily a_wave e_b m_laugh @ -m_talk "Hehehe!"
    hide lily with dissolve

    scene comic_shop at stage(.25, .5, 2) with fade
    show anon a_bag_comic_hold f_worried with dissolve
    pause
    show anon a_backpack_01 e_s
    pause
    show anon a_surprised f_confused
    pause
    show anon a_wipe f_shy
    pause
    anon a_side e_w @ -m_talk "( I should hurry back to [saga.cast.barb] with these costumes. )"
    hide anon with dissolve
    return


label bar05_lily.barb:
    anon f_confused "Where was I going to pick up those costumes from again?"
    barb "It's a place called Cosmic Cumics down at the mall."
    barb "Tell them you're there to pick up a package for [saga.cast.ursula]."
    anon f_calm "Okay, thanks."
    hide anon with dissolve
    return


label bar05_lily.mia:
    show old_anon 10
    anon "Any luck with those paints for [saga.cast.ursula]'s portrait?"
    show old_anon 5
    show old_mia 12
    mia "Not yet."
    show old_mia 12b
    mia "But I'll have it done soon, I promise."
    show old_mia 8b
    show old_anon 2
    anon "Oh, alright."
    show old_anon 1
    return


label bar05_barb3(when):
    show anon a_backpack e_s f_shy
    pause
    show barb e_sw
    anon a_bag_comic_give e_w "Here's the costumes for [saga.cast.ursula]."
    show anon a_reach e_s f_calm p_bend
    barb e_w f_curious @ e_wsw "Did you take a look at them?"
    anon a_side e_w f_worried -p_bend "I tried to give them a peek but I couldn't make heads or tails of any of it."
    anon f_confused "It just looks like a bunch of thin white satin and colorful jewelry to me."
    barb a_hip "What in the world is she playing at, I wonder?"
    anon "Any word from [saga.cast.mia]?"
    barb f_calm "Yeah, it's all ordered and taken care of..."
    barb "... She did so well, she even brought me back some change!"
    anon f_calm "Coolio!"
    pause
    anon "By the way, the girl at Cosmic Cumics asked me to tell you, \"Hello\"..."
    anon "... Said her name was [saga.cast.lily] Padbury."
    barb a_clasp f_happy "Oh, [saga.cast.lily]... I haven't spoken with her in years!"
    barb "How is she doing?"
    show barb a_hip
    anon a_rub f_confused "I dunno, she was dressed as an elf or something."
    barb f_calm "Heh, she always did have a wonderful imagination!"
    show anon a_surprised f_surprised
    barb f_horny "And such a pretty little petite body too!"
    barb "Did she say anything else?"
    anon a_uneasy e_se f_worried "Well, she may have.. umm..."
    pause
    anon a_side e_w f_shy "{i}*Ahem*{/i} ... N-no, nothing really."
    barb @ f_calm "Well, I'll have to go down and visit her!"
    barb "Who knows, Maybe {i}rekindle{/i} some of our old memories together?"
    anon f_worried_surprised "{i}*Gulp*{/i} Uh huh."
    pause

    if when == 0:
        barb f_calm "As for you... Come back this afternoon, okay?"
    elif when == 1:
        barb f_calm "As for you... Let's plan on meeting up for your painting tomorrow afternoon, okay?"
    else:
        barb f_calm "As for you... Let's plan on meeting up for your painting on [saga.time.dow + when] afternoon, okay?"

    show anon f_shy
    barb "[saga.cast.mia] should hopefully have the paint by then."
    anon "Sounds good!"
    barb "Thanks, [saga.cast.anon]!"
    show anon a_wave
    pause
    hide anon with dissolve
    return


label bar05_pause2:
    return


label bar05_pause2.barb(when):
    anon a_uneasy f_confused "So I'm really going to be painting [saga.cast.ursula]?"
    barb f_sad "And someone else too, apparently."

    if when == 1:
        anon "I suppose we won't know who the other person is until tomorrow afternoon when we meet, huh?"
    else:
        anon "I suppose we won't know who the other person is until [saga.time.dow + when] when we meet, huh?"

    barb "I'd say that's a safe bet."
    show anon a_side
    return


label bar05_pause2.mia(when):
    show old_anon 10

    if when == 1:
        anon "You're coming by the art room tomorrow afternoon, right?"
    else:
        anon "You're coming by the art room on [saga.time.dow + when], right?"

    show old_anon 5
    show old_mia 10
    mia "Of course."
    mia "I have to drop off the paint, remember?"
    show old_mia 7
    show old_anon 10
    anon "Oh, right."
    show old_anon 2
    anon "Good job with that by the way!"
    show old_anon 1
    show old_mia 10
    mia "Hehe, thanks!"
    show old_mia 7
    return


label bar05_delay2:
    scene camera at stage
    show anon a_fists_low f_happy with dissolve
    anon @ -m_talk "( Alright, it's time to paint my masterpiece... )"
    anon a_surprised f_calm @ -m_talk "( ... Of [saga.cast.ursula]... )"
    anon a_side f_worried @ -m_talk "( ... Ugh, this is going to go terribly!!! )"
    hide anon with dissolve
    return


label bar05_delay2.barb:
    anon a_hug_self f_worried "Ugh, I'm really nervous about this afternoon."
    barb "Don't be, [saga.cast.anon]... You're going to do great!"
    show anon a_side
    return


label bar05_delay2.mia:
    show old_anon 10
    anon "Man, I wish you and [saga.cast.barb] could stay with me while I paint this afternoon."
    show old_anon 5
    show old_mia 12
    mia "Yeah, me too."
    show old_mia 12b
    mia "I'd love to see how you manage creating something beautiful using [saga.cast.ursula] as the model."
    show old_mia 8b
    show old_anon 10
    anon "Oh, man... this is gonna be tough, huh?!"
    show old_anon 5
    return


label bar05_art2:
    call shot.school_art_barb
    show old_barb 10 at face_right, pos(.2)
    show old_anon 10 at face_left, pos(.45) with dissolve
    anon "Ugh, I'm not gonna lie, this whole thing is making me feel super anxious, [saga.cast.barb]."
    hide old_anon
    show old_barb 21 at face_right, pos(.275)
    with dissolve.nowait
    barb "Everything is going to be fine, [saga.cast.anon]."
    show old_barb 20
    pause
    show old_barb 21
    barb "Just take a deep breath and picture yourself in nature..."
    show old_barb 20
    pause
    show old_barb 21
    barb "... Surrounded by blue sky and friendly clouds... and happy little trees!!"
    show old_barb 20
    anon "Errp!"
    show old_barb 21
    barb "With all of nature's cute little critters frolicking about your feet, playing silly games and making merry."
    show old_barb 20
    pause
    show old_barb 10
    show old_anon 14 at face_left, pos(.45)
    with dissolve.nowait
    anon "Right, okay... Yeah, this is kinda working."
    show old_anon 13
    show old_barb 11
    barb "Now imagine your anxiety is just a tiny little acorn in your pocket..."
    barb "... I want you to take it out and hold it in the palm of your hand."
    show old_barb 10
    show old_anon 734
    with dissolve.nowait
    anon "..."
    show old_barb 57
    with dissolve.nowait
    barb "How could such a silly little thing cause you so much worry, huh?"
    barb "Let's just-"
    show old_barb 10
    show old_mia 12b at face_left, pos(.85)
    with dissolve.nowait
    mia "Alright, I'm here with the paints, [saga.cast.barb]!"
    show old_mia 8b
    show old_barb 11 at face_right, pos(.65)
    with dissolve.nowait
    barb "Oh, perfect timing cutie pie... let's see what you brought us!"
    show old_barb 45
    show old_anon 469 at face_right, pos(.45)
    with dissolve.nowait
    anon "Wait, what am I supposed to do with this acorn full of anxiety?!"
    show old_anon 468
    show old_barb 46
    barb "Hmm, I see red, blue, yellow, and white..."
    show old_barb 25
    with dissolve.nowait
    barb "... Where's the rest?!"
    show old_barb 24
    show old_anon 24
    show old_mia 12
    with dissolve.nowait
    mia "Umm, this is all we could afford."
    show old_anon at face_left, pos(.175)
    with dissolve.nowait
    mia "The guy at the store said we can mix these to make any color in the rainbow."
    show old_anon 296
    show old_mia 8
    show old_barb 58
    with dissolve.nowait
    barb "Right, yeah... of course!"
    show old_barb 2b at face_left, pos(.45)
    with dissolve.nowait
    barb "[saga.cast.anon], take this palette and get to mixing!"
    show old_barb 1b
    show old_anon 10 at face_right
    with dissolve.nowait
    anon "What, me?!"
    anon "You're the artist aren't you?!"
    show old_anon 5
    pause
    show old_anon 10
    anon "Okay, okay... I'm on it!"

    label bar05_art2.retry:
    call mini.paint

    if not _return:
        call shot.school_art_barb
        show old_anon 730c at face_right, pos(.175)
        show old_barb 24 at pos(.45)
        show old_mia 9 at pos(.575)
        with fade
        mia "Don't worry, [saga.cast.anon]. Try again, you've got this!"
        show old_mia 7
        show old_anon 29
        anon "Thanks, [saga.cast.mia]."
        anon "I'm so glad you agreed to be my partner for all this!"
        show old_anon 3
        show old_mia 10
        mia "... Me too!"
        show old_mia 7
        show old_barb 25
        barb "Hurry [saga.cast.anon], [saga.cast.ursula] will be here any second!"
        jump bar05_art2.retry

    call shot.school_art_barb
    show old_barb 10 at face_left, pos(.45)
    show old_mia 9 at face_left, pos(.575)
    show old_anon 1 at face_right, pos(.175)
    with fade
    mia "You did it!"
    show old_barb 11
    show old_mia 11
    barb "Well done, [saga.cast.anon]!"
    show old_mia 8
    show old_barb 24
    show old_anon 22
    ursula "WHAT ARE YOU TWO STILL DOING HERE?" with hpunch
    show old_anon 22
    show old_barb at face_right, pos(.35)
    show old_mia behind old_barb at face_right, pos(.475)
    with dissolve.nowait
    pause
    show old_annie outfit 2 at face_left, pos(.65)
    show old_ursula outfit 1 at face_left, pos(.8)
    with dissolve.nowait
    annie "I told them they weren't allowed to be here, ma'am."
    show old_annie outfit 1
    show old_barb 25
    barb "I was just giving my student a bit of last minute advice."
    show old_anon 11
    barb "... But I really think this would go a lot smoother if you allowed me to stay and supervise..."
    show old_barb 24
    show old_ursula outfit 2
    ursula "NO!"
    show old_barb 23
    show old_ursula outfit 1
    barb "Really, Mrs. [saga.cast.ursula.clan], I must protest."
    barb "This is-"
    show old_barb 22
    show old_ursula outfit 2b
    ursula "ABSOLUTELY NOT!"
    show old_ursula outfit 1
    show old_annie outfit 2
    annie "You heard the principal, beat it!"
    show old_annie outfit 1
    show old_mia 12b at face_left, pos(.45)
    with dissolve.nowait
    mia "Good luck, [saga.cast.anon]!"
    hide old_mia with dissolve
    show old_barb 23
    barb "Ugh, fine..."
    show old_barb 25 at face_left, pos(.325)
    with dissolve.nowait
    barb "You can do this, [saga.cast.anon]."
    barb "Just remember everything I taught you!"
    show old_barb 24
    show old_annie outfit 2
    annie "Would you get out already!"
    show old_barb 22 at face_right, pos(.35)
    show old_annie outfit 1
    with dissolve.nowait
    barb "..."
    hide old_barb with dissolve.nowait
    label bar05_art2.cookie hide:
    pause
    show old_ursula outfit 3 at face_left, pos(.5) with dissolve.nowait
    pause
    show old_ursula outfit 4
    ursula "Lock the door please, [saga.cast.annie]."
    show old_ursula outfit 3
    show old_annie outfit 2
    annie "Yes, ma'am."
    show old_ursula outfit 4
    show old_annie outfit 1
    ursula "Ah, ah, ah! Remember what we discussed..."
    show old_ursula outfit 3
    show old_annie outfit 9
    show old_annie outfit overlay as annie_cloak behind old_ursula at face_left, pos(.65)
    annie "Oh, right!"
    annie "Umm, yes, my Queen."
    hide annie_cloak
    hide old_annie
    with dissolve.nowait
    anon "..."
    show old_ursula outfit 4
    with dissolve.nowait
    ursula "Much better."
    show old_ursula outfit 3
    pause
    show old_annie outfit 1 at face_left, pos(.675)
    with dissolve.nowait
    pause
    show old_ursula outfit 4 at face_right, pos(.825)
    with dissolve.nowait
    ursula "Now, inform this one as to what is about to happen here."
    show old_ursula outfit 3
    show old_annie outfit 2
    annie "Right away, my Queen."
    show old_annie outfit 1
    show old_anon 10
    anon "... What is happening right now?"
    show old_anon 22
    show old_annie outfit 7 at face_left, pos(.4)
    show old_annie outfit overlay as annie_cloak at face_left, pos(.4)
    annie "DO NOT SPEAK!" with hpunch
    hide annie_cloak
    show old_annie outfit 2
    annie "You, peasant, will have the honor of capturing our beloved Queen in all her glory."
    show old_anon 11
    annie "However, there are a few rules that we must go over before you begin."
    show old_annie outfit 1
    pause
    show old_annie outfit 2
    annie "Rule 1..."
    annie "From this moment onwards you will only refer to Mrs. [saga.cast.ursula.clan] as {i}our queen{/i}, {i}Her Royal Highness{/i}, or {i}Her Majesty{/i}."
    show old_annie outfit 1
    anon "..."
    show old_annie outfit 2
    annie "You don't want to forget rule 1, trust me!"
    show old_annie outfit 1
    pause
    show old_annie outfit 2
    annie "Rule 2..."
    annie "You must not address our Queen directly."
    annie "If you have any questions, you will ask me and I will answer."
    show old_annie outfit 1
    anon "..."
    show old_annie outfit 2
    annie "And rule 3..."
    annie "After we have finished here, you will never, {i}ever{/i}, reveal what transpired in this room."
    annie "Do so and I assure you, your life will be forfeit!"
    annie "Is that understood?!"
    show old_annie outfit 1
    anon "..."
    show old_annie outfit 2
    annie "You may talk, peasant."
    show old_annie outfit 1
    show old_anon 10
    anon "Uhh, sure. Yeah, I got it."
    show old_annie outfit 2
    show old_anon 11
    annie "Very good!"
    show old_annie outfit 2 at face_right, center with dissolve.nowait
    annie "I believe the filthy peasant is ready to begin, my Queen."
    show old_annie outfit 1
    show old_ursula outfit 4
    ursula "It's about time."
    show old_ursula outfit 3
    pause
    show old_ursula outfit 4
    ursula "It's so hard to find good peasants these days."
    show old_ursula outfit 3
    show old_annie outfit 2
    annie "Yes, my Queen it certainly is..."
    show old_annie outfit 1
    show old_ursula outfit 4
    ursula "Very well, slave. You may begin..."
    show old_ursula outfit 3
    show old_annie outfit 2
    annie "Right away, Your Majesty!"
    show old_annie outfit 1 at face_left, pos(.475)
    with dissolve.nowait
    pause
    show old_annie outfit 4 with dissolve
    pause
    show old_annie outfit 5 with dissolve
    show old_anon 23
    anon "( !!! )" with hpunch
    anon "( Holy shit! )"
    show old_annie outfit 7 with dissolve
    annie "IS THERE A PROBLEM?!"
    show old_annie outfit 7b
    show old_anon 10
    anon "N-nooo..."
    show old_anon 11
    show old_annie outfit 7
    annie "Then stop ogling me, you pathetic-"
    show old_annie outfit 7b
    show old_ursula outfit 2b
    ursula "Attend me, slave, before I lose my patience!"
    show old_ursula outfit 3
    show old_annie outfit 10
    with dissolve.nowait
    pause
    show old_annie outfit 9
    annie "Yes, my Queen..."
    show old_annie outfit 9 at face_right, center
    with dissolve.nowait
    annie "... Please, forgive me."
    hide old_annie
    show old_ursula outfit 5
    with dissolve.nowait
    pause
    show old_ursula outfit 6
    show old_anon 23
    anon "( !!! )" with hpunch
    show old_ursula outfit 7
    show old_annie outfit 8 behind old_ursula at face_right, pos(.5892)
    with dissolve.nowait
    anon "( I can see everything! )"
    pause
    show old_anon 11
    pause
    show old_anon 10
    anon "... Am I supposed to start painting now?"
    show old_anon 11
    show old_annie outfit 7 at face_left, pos(.475)
    with dissolve.nowait
    annie "NO!"
    annie "We have to get into position first!"
    show old_annie outfit 6 at face_right, center with dissolve.nowait
    annie "... Stupid peasant..."

    scene mono school_art_smith
    mono "I couldn't decide whether to laugh or crap my pants in terror..." with fade
    more "... So instead, I just focused on trying not to pop a boner."
    mono "Not an easy task, given the outfits Mrs. [saga.cast.ursula.clan] had chosen!"
    mono "Ooops! Did I say Mrs. [saga.cast.ursula.clan]?"
    more "I meant, our beloved queen! Heh, what a weird day..."

    call shot.school_art_barb
    show school_art -table
    show old_xtra 45b at face_right, pos(.35)
    show old_anon 10 at face_right, pos(.15)
    show old_ursula outfit 7 at pos(.75)
    show old_annie outfit 5 at pos(.68, 1.35)
    with fade
    anon "I think that should do it..."
    show old_anon 11
    show old_annie outfit 6
    annie "Does that mean you're finished?"
    show old_anon 10
    show old_annie outfit 5
    anon "Y-yes?"
    show old_anon 11
    show old_annie outfit 9 at pos(.64, 1.2)
    with dissolve.nowait
    annie "Thank god, my butt is killing me!"
    show old_annie outfit 5 at pos(.6, 1.)
    show old_ursula outfit 8
    with dissolve.nowait
    ursula "{i}*Ahem*{/i}"
    show old_ursula outfit 7
    show old_annie outfit 9 at face_right, pos(.55)
    with dissolve.nowait
    annie "Oh! Sorry, my Queen!"
    show old_annie outfit 8
    show old_ursula outfit 13
    with dissolve.nowait
    ursula "Ugh, I'll discipline you later, slave!"
    show old_ursula outfit 12
    show old_annie outfit 9 behind old_ursula at face_left, pos(.6)
    with dissolve.nowait
    annie "Of course, Your Majesty!"
    show old_annie outfit 8
    show old_ursula outfit 14
    ursula "Spin the painting around so I can see it, peasant!"
    show old_ursula outfit 12
    pause
    show old_anon 518 behind old_xtra at face_right, pos(.175) with dissolve.nowait
    pause
    show old_xtra 45b at face_left, pos(.325) with dissolve.nowait
    pause
    show old_anon 11
    show old_annie outfit 5
    with dissolve.nowait
    ursula "..."
    show old_xtra behind old_anon
    show old_anon at face_right, pos(.2)
    with dissolve.nowait
    anon "( Please, like it!!! )"
    show old_anon 11
    show old_ursula outfit 10
    with dissolve.nowait
    ursula "..."
    show old_ursula outfit 11
    ursula "IT'S MARVELOUS!"
    show old_ursula outfit 11b
    ursula "Finally, an accurate portrayal of my true self!"
    show old_ursula outfit 10
    show old_annie outfit 9b
    with dissolve.nowait
    annie "You look beautiful, Your Majesty."
    show old_ursula outfit 9
    show old_annie outfit 8
    with dissolve.nowait
    ursula "SILENCE!"
    show old_ursula outfit 12 with dissolve.nowait
    ursula "..."
    show old_ursula outfit 13
    ursula "Ugh, you've ruined the moment, slave..."
    show old_ursula outfit 12
    annie "..."
    show old_ursula outfit 11 with dissolve.nowait
    ursula "Peasant?"
    show old_ursula outfit 10
    anon "..."
    show old_ursula outfit 11
    ursula "Peasant?! You may address me, just this once."
    show old_ursula outfit 10
    show old_anon 10
    anon "Oh, that's me, isn't it?"
    show old_ursula outfit 12 with dissolve.nowait
    anon "Sorry, uhh... Yes, my Queen?"
    show old_anon 11
    ursula "..."
    show old_ursula outfit 11 with dissolve.nowait
    ursula "You did very well!"
    show old_anon 43
    ursula "Your Queen is pleased."
    show old_anon 13
    ursula "Tell your teacher I want this painting framed and delivered to my office as soon as possible!"
    show old_ursula outfit 13 with dissolve.nowait
    ursula "Understood?"
    show old_ursula outfit 12
    show old_anon 14
    anon "Yes, ma'am."
    show old_anon 22
    ursula "..."
    show old_anon 29
    with dissolve.nowait
    anon "Sorry, I meant {i}my Queen{/i}."
    show old_anon 3
    ursula "Hmph!"
    show old_ursula outfit 13
    ursula "Very good."
    show old_anon 13
    show old_ursula outfit 9
    with dissolve.nowait
    ursula "Slave?!"
    show old_ursula outfit 7
    show old_annie outfit 6 at face_right, pos(.55)
    with dissolve.nowait
    annie "Right here, Your Majesty!"
    show old_annie outfit 5
    show old_ursula outfit 8
    ursula "Gather up our robes and let us be off."
    show old_anon 11
    show old_ursula at face_right, pos(.8)
    with dissolve.nowait
    ursula "I think I'll have you give me a bath this evening..."
    hide old_ursula outfit
    show old_annie outfit 6
    with dissolve.nowait
    annie "Of course, Your Majesty! It would be my honor!"
    show old_annie outfit 5
    ursula "... And don't think I've forgotten your blunder earlier!"
    show old_annie outfit 8 with dissolve.nowait
    ursula "I'll see that you're disciplined after you've finished bathing me."
    show old_annie outfit 9
    annie "Yes, my Queen..."
    hide old_annie outfit with dissolve.nowait
    pause
    show old_anon 11 with dissolve.nowait
    anon "..."
    show old_anon 10
    anon "What."
    anon "The."
    anon "F-"
    $ renpy.end_replay()
    show old_anon 11
    barb "[saga.cast.anon]!"
    show old_anon 5
    show old_mia 8b at pos(.625)
    show old_barb 25 at old_right
    with dissolve.nowait
    barb "How did the painting go?"
    show old_barb 24
    mia "..."
    barb "..."
    show old_anon 10
    anon "Yeah, imagine the weirdest thing you can."
    anon "Then multiply it times a thousand!"
    anon "You still won't even come close to how weird my night was..."
    show old_anon 5
    show old_mia 12b
    mia "What did they say?"
    show old_anon 10
    show old_mia 8b
    anon "I uhh, can't tell you."
    show old_anon 5
    show old_mia 12b
    mia "Huh?"
    show old_anon 10
    show old_mia 8b
    anon "I'm pretty sure Mrs. [saga.cast.ursula.clan] would have me murdered in my sleep if I said anything more."
    show old_anon 5
    show old_mia 12b
    mia "Sheesh, alright."
    show old_mia 9
    mia "The painting looks nice though!"
    show old_mia 11
    show old_anon 10
    anon "You haven't said anything yet, [saga.cast.barb]?"
    show old_anon 5
    barb "..."
    show old_anon 11
    show old_mia 7
    show old_barb 34
    with dissolve.nowait
    barb "... It's beautiful."
    show old_barb 34b
    show old_mia 10b
    mia "Are you crying?"
    show old_barb 34
    show old_mia 11
    barb "Sorry, I'm just so proud!"
    show old_anon 13
    show old_barb 34b
    show old_mia 9
    mia "Aww..."
    show old_mia 11
    show old_barb 34
    barb "Come here, both of you!"
    show old_barb 34b
    show old_anon 11
    show old_mia 7 at face_right, pos(.6)
    with dissolve.nowait
    pause
    show old_mia 8 at face_left, pos(.575)
    with dissolve.nowait
    pause
    show old_mia 50b behind old_anon at face_left, pos(.37)
    show old_anon 626
    with dissolve.nowait
    pause
    show old_mia at face_left, pos(.585)
    show old_anon 731 at face_right, pos(.4)
    with dissolve.nowait
    pause
    hide old_anon
    hide old_mia
    show old_barb 54
    with dissolve.nowait
    barb "I think you just saved my job, [saga.cast.anon]!"
    barb "Thanks, you guys..."
    show old_barb 55
    mia "I'm just happy I got to be a part of all this!"
    show old_barb 10
    show old_mia 7 at face_right, pos(.6)
    show old_anon 10 at face_right, pos(.45)
    with dissolve
    anon "Mrs. [saga.cast.ursula.clan] said she wants it framed and delivered to her office right away."
    show old_anon 11
    show old_barb 11
    barb "Well, she's gonna have to wait!"
    barb "We have a contest to win!"
    show old_barb 10
    show old_mia 9
    mia "Oh, yay!"
    show old_mia 11
    show old_anon 10
    anon "Won't she get upset?"
    show old_anon 11
    show old_barb 11
    barb "Probably."
    show old_mia 7
    barb "... But she'll get over it pretty quick when I tell her the art class won't be needing funding next year."
    show old_anon 2
    show old_barb 10
    anon "You really think we'll win?"
    show old_anon 1
    show old_barb 27 with dissolve
    barb "I do!"
    barb "Your painting is really remarkable, [saga.cast.anon]!"
    show old_barb 26
    show old_anon 2
    anon "Thanks!"
    show old_anon 1
    show old_barb 27
    barb "You know, we should celebrate!"
    barb "... I think I've got some party favors upstairs if you guys-"
    show old_barb 25 with dissolve
    barb "Oh, crap! It's getting really late, isn't it?"
    show old_barb 25b
    barb "You kids must be exhausted!"
    show old_barb 25
    barb "Get on home and get some sleep. I'll make sure the painting gets framed and sent off to the contest."
    show old_barb 24
    show old_anon 2
    anon "Okay. Goodnight, you two!"
    show old_anon 1
    show old_mia 9
    mia "Sweet dreams, [saga.cast.anon]!"
    hide old_anon with dissolve
    return


label bar05_art2.rails:
    scene camera at stage
    show anon f_tired with dissolve
    anon @ -m_talk "( Let's just head to the art class and get this over with, yeah? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
