label mel02_intro:
    call shot.school_music_melody
    show old_melody 2 at old_left
    show old_anon 13 at old_right with dissolve
    melody "Well, hello there, [saga.cast.anon]."
    melody "Have you been practicing those fingerings I taught you?"
    show old_melody 1
    show old_anon 10
    anon "F-fingerings?"
    show old_anon 11
    show old_melody 8
    with dissolve.nowait
    melody "You know, on the flute, silly."
    show old_melody 4
    show old_anon 17
    anon "O-oh yeah! I think I'm getting pretty good."
    show old_anon 14
    anon "You're a great teacher, [saga.cast.melody]!"
    show old_anon 13
    show old_melody 5
    melody "Well, you're a fast learner, sugar."
    show old_melody 11
    melody "I just hope we get more students to sign up soon, otherwise, we might have to cancel the show."
    show old_melody 10
    show old_anon 12
    anon "You still haven't had any volunteers?"
    show old_anon 5
    show old_melody 11b
    melody "Nope, not a one."
    show old_melody 12
    melody "I'm starting to get worried, [saga.cast.anon]..."
    show old_melody 10b
    show old_anon 14
    anon "There's still time, [saga.cast.melody]."
    anon "I'll bet I can round up a few people for you!"
    show old_anon 13
    show old_melody 11
    melody "You'd really do that?"
    show old_melody 10
    show old_anon 33
    anon "Absolutely!"
    show old_anon 13
    show old_melody 5
    melody "Oh, you're so sweet!"
    show old_melody 4
    show old_anon 14
    anon "Heh, lemme go see who I can convince."
    show old_anon 13
    show old_melody 3
    with dissolve.nowait
    melody "Good luck, sugar!"
    hide old_anon with dissolve

    scene school_hall1 at stage(.5, .585, 4.5) with fade
    show old_anon 4 at old_right with dissolve
    anon "( I wonder who I should talk to first? )"
    show old_anon 9 with dissolve.nowait
    pause
    show old_anon 22
    show old_annie 4 at old_left
    with hpunch
    annie "[saga.cast.anon], stop loitering in the hallway!"
    show old_annie 1
    show old_anon 12
    anon "[saga.cast.annie], I just stepped into the hallway..."
    show old_anon 5
    show old_annie 5
    annie "Whatever. Hurry to your next class before I write you up!"
    show old_annie 6
    show old_anon 12
    anon "Alright! Sheesh..."
    show old_anon 10
    anon "Oh, hey! Wait a second!"
    anon "You don't happen to play an instrument or sing, do you?"
    show old_anon 5
    show old_annie 3
    annie "I do. What of it?"
    show old_annie 1
    show old_anon 10
    anon "Well, you see, [saga.cast.melody] is looking for people to play in the talent show."
    show old_anon 5
    show old_annie 5
    annie "Yes, I'm well aware."
    show old_annie 6
    anon "..."
    show old_anon 10
    anon "Would you maybe like to be a part of it?"
    show old_anon 5
    show old_annie 9
    annie "Pfft, absolutely not!"
    show old_annie 5
    annie "You do realize, Mrs. [saga.cast.ursula.clan] is trying to get that stupid show canceled, right?"
    show old_annie 6
    show old_anon 12
    anon "Yeah, I heard."
    show old_anon 5
    show old_annie 3
    annie "So there's no way I could participate in it!"
    show old_annie 1
    show old_anon 12
    anon "You don't always have to listen to Mrs. [saga.cast.ursula.clan], [saga.cast.annie]."
    show old_anon 5
    show old_annie 5
    annie "I am head of the disciplinary committee, official hall monitor, and Mrs. [saga.cast.ursula.clan]'s second in command!"
    show old_annie 3
    annie "It's my sworn duty to follow her orders."
    show old_annie 1
    show old_anon 12
    anon "This isn't the military, [saga.cast.annie]..."
    show old_anon 11
    show old_annie 7
    annie "SILENCE!"
    show old_annie 1
    show old_anon 10
    anon "But-"
    show old_anon 11
    show old_annie 5
    annie "Mrs. [saga.cast.ursula.clan] wants that show canceled and plans have been set in motion."
    show old_annie 6
    show old_anon 12
    anon "... Plans?"
    show old_anon 5
    show old_annie 9
    annie "Grr, I've said too much."
    show old_annie 1
    show old_anon 11
    anon "..."
    show old_annie 5
    annie "I suggest you just give up on the talent show. It's not going to happen, I assure you."
    show old_annie 8
    annie "Now, get out of my way so I can finish my patrol!"
    hide old_annie
    show old_anon 90
    with dissolve.nowait
    anon "( What a whack job... )"
    hide old_anon with dissolve
    return


label mel02_intro.melody:
    show old_anon 10
    anon "I'm really not sure about this whole flute thing."
    show old_anon 5
    show old_melody 2
    melody "Nonsense, sugar, you've got so much potential!"
    show old_melody 1
    show old_anon 10
    anon "But-"
    show old_anon 5
    show old_melody 2
    melody "Just keep coming to class and we'll have you up to speed in no time."
    melody "Our woodwind section is much stronger with you in it!"
    show old_melody 1
    show old_anon 10
    anon "I'm not-"
    show old_anon 5
    show old_melody 2
    melody "There are no shortcuts to greatness mind..."
    melody "... And I'm expecting big things from you, [saga.cast.anon]."
    show old_melody 1
    anon "..."
    show old_anon 25
    anon "Yes, [saga.cast.melody]."
    hide old_anon with dissolve
    return


label mel02_ask:
    return


label mel02_ask.dexter:
    show old_anon 10
    anon "I don't suppose you play any instruments?"
    show old_anon 5
    show old_dexter 8
    dexter "Huh?"
    show old_dexter 2
    show old_anon 12
    anon "In{w}stru{w}ments."
    anon "You know, like for music? Do you play any?"
    show old_anon 5
    show old_dexter 8
    dexter "Do I look like some kinda band geek to you?!"
    show old_dexter 2
    show old_anon 12
    anon "Ehh, no? I just thought maybe you had a hidden talent for banging the drums or something?"
    show old_anon 5
    show old_dexter 6 with dissolve
    dexter "I'd like to bang on your stupid face with my fists..."
    dexter "You think that would make some music?"
    show old_dexter 5
    show old_anon 29 with dissolve
    anon "Heh, I was just leaving..."
    show old_anon 3
    show old_dexter 4 with dissolve
    dexter "Yeah, you better!"
    hide old_anon with dissolve
    return


label mel02_ask.erik:
    show old_anon 14
    anon "You play guitar, right?"
    show old_anon 13
    show old_erik 3b
    erik "Huh?"
    erik "No. What gave you that idea?"
    show old_erik 51
    show old_anon 10
    anon "Well, aren't those your guitars hanging up in your basement..."
    anon "I just assumed-"
    show old_anon 5
    show old_erik 4
    erik "Oh, right! Yeah, those are Mr. [saga.cast.larry.clan]'s old guitars."
    show old_erik 3
    erik "He never allowed me near them."
    erik "Didn't want me to break them, he said."
    show old_erik 3c
    erik "..."
    show old_erik 3b
    erik "Sometimes, I think he loved those guitars more than [saga.cast.tammy]."
    show old_erik 3c
    show old_anon 25
    anon "Yikes."
    show old_anon 5
    show old_erik 4
    erik "Tell me about it."
    erik "Anyways, I have much better hobbies than music!"
    show old_erik 1
    show old_anon 14
    anon "You mean your video games?"
    show old_anon 13
    show old_erik 4
    erik "Heck yeah, dude!"
    show old_erik 1
    show old_anon 14
    anon "Heh, no surprises there!"
    show old_anon 36 with dissolve.nowait
    anon "Later, [saga.cast.erik]."
    hide old_anon with dissolve
    return


label mel02_ask.judith:
    hide anon
    hide judith
    show old_judith 1 at right
    show old_anon 10 at old_left
    anon "I was wondering if you wanted to participate in the upcoming talent show?"
    show old_anon 5
    show old_judith 3
    judith "No thanks, [saga.cast.anon]. I don't really know how to play an instrument."
    show old_judith 2
    judith "... And I'm way too embarrassed to get up on stage in front of the entire school."
    show old_judith 1
    show old_anon 10
    anon "Well, what if we played together?"
    show old_anon 5
    show old_judith 5
    judith "You and me?"
    show old_judith 4
    show old_anon 14
    anon "Sure, why not?"
    show old_anon 13
    show old_judith 6
    judith "Hmm..."
    show old_judith 2
    judith "No, I'm sorry, [saga.cast.anon]."
    show old_judith 3
    judith "As much as I'd enjoy playing with you; just the thought of being in the spotlight like that..."
    show old_judith 8
    show old_anon 11
    with dissolve.nowait
    judith "..."
    show old_judith 9
    with dissolve.nowait
    judith "Excuse me, I just need a minute!"
    hide old_judith
    show old_anon 5
    with dissolve.nowait
    anon "( Dang, I thought for a second she was going to agree. )"
    anon "( Guess I'd better keep looking... )"
    hide old_anon with dissolve
    return


label mel02_ask.mia:
    show old_anon 10
    anon "Do you play any instruments or sing?"
    show old_anon 5
    show old_mia 9
    mia "Yeah, I sing in the choir at church all the time!"
    show old_mia 7
    show old_anon 14
    anon "You do? Awesome!"
    anon "You should sing in [saga.cast.melody]'s talent show!"
    anon "We really need more people to volunteer."
    show old_anon 13
    show old_mia 12
    mia "Oh, umm."
    mia "I'd like to but I can't."
    show old_mia 8
    show old_anon 10
    anon "Huh? Why not?"
    show old_anon 5
    show old_mia 12
    mia "My mom won't even let me go to the talent show, much less participate."
    show old_mia 8
    show old_anon 12
    anon "How come?"
    show old_anon 5
    show old_mia 12
    mia "She doesn't want me listening to rock or rap music..."
    mia "She's afraid it will taint my young mind or something like that."
    show old_mia 8
    show old_anon 12
    anon "That sucks!"
    show old_anon 5
    show old_mia 12
    mia "Yeah. Sorry."
    show old_mia 8
    show old_anon 10
    anon "That's alright, [saga.cast.mia]. Thanks anyways!"
    hide old_anon with dissolve
    return


label mel02_ask.rhonda:
    anon f_shy "I don't suppose you'd be interested in volunteering for [saga.cast.melody]'s musical talent show?"
    rhonda @ f_curious "Musical talent?"
    rhonda "No, I would not be interested."
    anon f_confused "Are you sure? You don't play any instruments or sing at all?"
    rhonda f_serious "Umm, can't you see I have more important things to focus on. Like track and swimming..."
    show anon f_worried
    rhonda @ f_sceptical "Stuff you should be focusing on as well!"
    rhonda "You're never gonna make the team if you keep ignoring your training!"
    anon f_sceptical "You know, there's more to life than sports, [saga.cast.rhonda]..."
    hide anon with dissolve
    rhonda e_r f_annoyed "Pfft, yeah right."
    return


label mel02_ask.roxxy:
    hide old_anon
    show anon a_think f_pensive o_right at left
    anon @ -m_talk "( I don't think she has a musical bone in her body... )"
    anon f_horny_smug @ -m_talk "( ... Though with a body like that, I guess she doesn't really need one. )"

    if saga.cast.roxxy < 'meth':
        show old_roxxy 6b
        pause
        show anon a_surprised_up_both f_surprised m_teeth
        show old_roxxy 10
        with none.nowait
        roxxy "What are you staring at, creep?!" with hpunch
        show old_roxxy 3b with dissolve.nowait
        anon e_wsw f_worried -m_teeth "I was..."
        anon a_surrender e_w f_worried_surprised "I mean, I wasn't-"
        show old_roxxy 3
        roxxy "Just get lost before I sic [saga.cast.dexter] on you!"
        show old_roxxy 3b
        anon "I was just trying to find some volunteers for [saga.cast.melody]'s talen-"
        show anon a_up f_surprised m_teeth
        show old_roxxy 31
        with none.nowait
        roxxy "[saga.cast.dexter!u]!" with hpunch
        show old_roxxy 3b
        anon -m_teeth "Alright, alright! I'm leaving! Calm your tits!"
        show anon f_worried
        roxxy "Hmmph!"
        hide anon with dissolve
        return

    show old_roxxy 6
    pause
    show anon f_surprised
    show old_roxxy 5
    with dissolve.nowait
    roxxy "Cat got your tongue?"
    show old_roxxy 6 with dissolve.nowait
    anon a_side f_shy "N-no, I'm just trying to find some volunteers for [saga.cast.melody]'s talent show."
    show old_roxxy 10 with dissolve.nowait
    roxxy "Talent show?"
    show old_roxxy 7 with dissolve.nowait
    anon "Yeah, would you be interested?"
    show old_roxxy 11 with dissolve.nowait
    roxxy "Pfft, no fucking way!"
    show old_roxxy 9
    anon f_confused "Why not?"
    show old_roxxy 11
    roxxy "I don't play an instrument and I definitely don't sing."
    show old_roxxy 9
    anon a_rub f_shy "You could dance?"

    if saga.cast.roxxy < 'sex':
        show old_roxxy 5 with dissolve.nowait
        roxxy "I bet you'd like that, huh?"
        anon a_side "Definitely."
        show old_roxxy 4 with dissolve.nowait
        roxxy "Hah!"
        show old_roxxy 5 with dissolve.nowait
        roxxy "In your dreams, [saga.cast.anon]."
        show old_roxxy 6 with dissolve.nowait
        anon "Fine, be that way."
        hide anon with dissolve
        return

    show old_roxxy 11
    roxxy "You want me to dance... In front of the entire school?"
    show old_roxxy 9
    anon a_side "Sure, it'll be fun."
    show old_roxxy 11
    roxxy "I dunno, that sounds super embarrassing..."
    show old_roxxy 9
    anon "It's not much different than cheerleading, is it?"
    show old_roxxy 7 with dissolve.nowait
    roxxy "..."
    show anon f_happy
    show old_roxxy 5
    with dissolve.nowait
    roxxy "No, I suppose not."
    show old_roxxy 6 with dissolve.nowait
    anon a_fists_low "So you'll do it?"
    show old_roxxy 6b
    roxxy "..."
    show anon f_worried
    show old_roxxy 1l
    with dissolve.nowait
    roxxy "{i}*Sigh*{/i} [saga.cast.anon], I really don't want to!"
    show old_roxxy 1k
    show anon a_side e_s
    pause
    anon e_w "Alright, no problem."
    show old_roxxy 1l
    roxxy "You're not mad?"
    show old_roxxy 1k
    anon f_shy "Of course not."
    show old_roxxy 1h with dissolve.nowait
    roxxy "Good."
    roxxy "'Cause I don't mind dancing for you, [saga.cast.anon]... But like, in private, you know?"
    show old_roxxy 1g
    anon a_think f_happy "Oh?"
    show old_roxxy 1h
    roxxy "Yeah."
    show old_roxxy 1g
    anon a_pocket f_horny "I like the sound of that!"
    show old_roxxy 1h
    roxxy "I thought you might."
    show old_roxxy 1g
    hide anon with dissolve
    return


label mel02_eve_ask(when, misc):
    anon f_confused "Do you play any instruments?"
    eve "No, I don't play any instruments. I've always wanted to learn but I just haven't had the time, you know?"
    anon f_worried "Okay, well, how about singing?"
    eve e_ssw f_nervous "Oh, umm..."
    eve "Yeah, I like to sing I guess... I dunno if I'm any good though."

    if saga.cast.eve < 'e4':
        anon f_calm "I bet you are! You should sign up for the talent show with me!"
    else:
        anon f_calm "Oh, c'mon! I've heard you singing at the park before, you're great!"

    if saga.cast.eve in saga.sets.school_french:
        show eve e_e
    else:
        show eve e_w

    if saga.cast.eve < 'e4':
        anon "We're really hurting for more volunteers."
        eve f_sad "... Yeah, I dunno."
        eve f_confused "You want me to sing in front of the entire school? That sounds pretty embarrassing..."
    else:

        anon "We're really hurting for more volunteers."
        eve f_surprised "Y-you really think I'm a good singer?"
        pause
        eve f_confused "I don't know if I can sing in front of the entire school? That sounds pretty embarrassing..."

    if saga.cast.eve in saga.sets.school_french:
        show eve a_hair

    if saga.cast.eve < 'e4':
        eve e_ssw f_nervous "... And I haven't sung in a while. Not since my karaoke machine broke."
    else:
        eve e_ssw f_nervous "I've never sung for a crowd before."

    if saga.cast.eve in saga.sets.school_french:
        show eve e_e
    else:
        show eve e_w

    eve "I'm quite out of practice."

    if saga.cast.eve in saga.sets.school_french:
        show eve a_pencil f_confused
    else:

        show eve f_confused
        show anon a_think

    anon e_nw f_pensive @ -m_talk "Hmm..."
    pause

    if saga.cast.eve not in saga.sets.school_french:
        show anon a_side

    anon e_w f_shy "You know, I think [saga.cast.erik] has a karaoke machine in his basement."
    eve f_nervous "Oh, yeah?"
    anon @ e_b f_happy m_laugh "Totally!"

    if saga.cast.eve < 'e4':
        anon "You should come over sometime and practice!"
    else:
        anon "You could practice there and build your confidence up!"

    eve f_happy @ e_b m_laugh "Heh, you want me to sing for you and [saga.cast.erik]?"

    if when == 0:
        anon "Nah, we can all sing together! C'mon, we'll do it tonight, it'll be fun!"
    elif when == 1:
        anon "Nah, we can all sing together! C'mon, we'll do it tomorrow night, it'll be fun!"
    else:
        anon "Nah, we can all sing together! C'mon, we'll do it [saga.time.dow + when] night, it'll be fun!"

    eve f_nervous @ -m_talk "..."

    if saga.cast.eve not in saga.sets.school_french:
        show eve a_wtf

    eve f_happy "Alright, I guess I can stop by for a little while."
    anon f_happy "Awesome!"

    if saga.cast.eve not in saga.sets.school_french:
        show eve a_side

    if when == 0:
        anon f_calm "I'll meet you at [saga.cast.erik]'s house tonight."
    elif when == 1:
        anon f_calm "I'll meet you at [saga.cast.erik]'s house tomorrow night."
    else:
        anon f_calm "I'll meet you at [saga.cast.erik]'s house on [saga.time.dow + when] night."

    if saga.cast.eve in saga.sets.school_french:
        show eve o_right ob_chair z_ob as anon_chair at pos(.15, 1.02)
        show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)

    hide anon with dissolve

    if saga.cast.eve in saga.sets.school_french:
        call shot.school_french_door
    else:
        scene camera at stage

    with fade
    show anon a_surprised f_surprised with dissolve
    anon @ -m_talk "( Crap! I totally got carried away and didn't even think to check with [saga.cast.erik]! )"
    anon a_phone e_sw f_worried @ -m_talk "( I'll text him real quick, hopefully he's cool with it... )"
    pause
    anon a_pocket e_w f_shy @ -m_talk "( ... He normally gets back to me pretty qui- )"
    show anon e_s f_surprised
    "*Ding*"
    anon a_phone e_sw f_shy @ -m_talk "( Heh, right on cue... )"
    anon f_happy @ -m_talk "( \"[misc.what!t]\" )"
    anon a_wipe e_b f_calm m_drink @ -m_talk "( Nice, we're still in business! )"
    hide anon with dissolve
    return


label mel02_eve_pause:
    return


label mel02_eve_pause.erik(when):
    show old_anon 2

    if when == 1:
        anon "Thanks for agreeing to host karaoke tomorrow."
    else:
        anon "Thanks for agreeing to host karaoke on [saga.time.dow + when]."

    anon "Hopefully it'll help me convince [saga.cast.eve] to join the talent show."
    show old_anon 1
    show old_erik 4
    erik "Of course, dude."
    erik "Mi casa es su casa!"
    show old_erik 1
    show old_anon 2
    anon "Thanks, [saga.cast.erik]!"
    hide old_anon with dissolve
    return


label mel02_eve_pause.eve(when):
    if when == 1:
        anon f_confused "Excited for karaoke tomorrow?"
    else:
        anon f_confused "Excited for karaoke on [saga.time.dow + when]?"

    eve f_nervous "Eh, probably not the word I'd choose."
    anon e_w f_shy "Come ooon, it'll be fun!"
    eve f_happy "Yeah, yeah. I'll be there."

    if saga.cast.eve in saga.sets.school_french:
        show eve o_right ob_chair z_ob as anon_chair at pos(.15, 1.02)
        show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)

    hide anon with dissolve
    return


label mel02_eve_delay:
    scene camera at stage
    show anon a_fists_low with dissolve
    anon @ -m_talk "( Time to help give [saga.cast.eve] the confidence boost she needs to join the talent show... )"
    anon a_cheer e_b f_happy m_teeth @ -m_talk "( ... Karaoke party at [saga.cast.erik]'s house here I come! )"
    hide anon with dissolve
    return


label mel02_eve_delay.erik:
    show old_anon 10
    anon "Thanks again for hosting karaoke tonight."
    show old_anon 29 with dissolve.nowait
    anon "Sorry I kinda sprang it on you."
    show old_anon 3
    show old_erik 4
    erik "No problem, dude, what are friends for?"
    show old_anon 1 with dissolve.nowait
    erik "Be cool to have a few people for karaoke again."
    show old_erik 54
    erik "It's not the same without an audience, even it is more comfortable in just my underwear-"
    show old_erik 51
    show old_anon 11
    erik "!!!" with hpunch
    show old_erik 4b
    erik "Not... that... I sing karaoke on my own wearing only..."
    show old_erik 59
    show old_anon 11
    anon "..."
    show old_anon 10
    anon "... I'll... see you later."
    hide old_anon
    show old_erik 7

    if renpy.showing('erik_labcoat'):
        show old_erik labcoat 6 as erik_labcoat

    with dissolve.nowait
    anon "Later, dude."
    show old_erik 2

    if renpy.showing('erik_labcoat'):
        show old_erik labcoat 2 as erik_labcoat

    with dissolve.nowait
    pause
    return


label mel02_eve_delay.eve:
    anon f_confused "Still on for later?"
    eve f_confused "What's later?"
    anon f_worried_surprised "The karaoke?"
    pause
    anon "At [saga.cast.erik]'s?!"
    pause
    show anon f_surprised
    eve f_happy @ e_b m_laugh "Bahahaha!"
    eve "Oh, man... your face!"
    eve "Of course I'll be there."
    anon f_shy "Wow... you totally had me going..."
    eve @ e_b m_laugh "Hehehe!"
    anon "... I'll see you later then."

    if saga.cast.eve in saga.sets.school_french:
        show eve o_right ob_chair z_ob as anon_chair at pos(.15, 1.02)
        show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)

    hide anon with dissolve
    return


label mel02_eve_den(test=False):
    scene tammy_den dusk -erik at stage
    show eve a_shy at pos(.55)
    show old_erik 1 at pos(.7)
    show anon a_pocket f_shy o_right at left with dissolve
    eve "Hey, it's about time! I was starting to think you flaked on me!"
    show eve f_happy
    show anon a_uneasy with dissolve.nowait
    anon "Sorry, I got held up! Hey [saga.cast.erik]!"
    label mel02_eve_den.merge:
    show old_erik 4
    erik "Hey, [saga.cast.anon]! I was just telling [saga.cast.eve] about my guild on {i}World of Orcette{/i}."
    show old_erik 1
    show anon a_side
    eve e_r f_annoyed "Yeah, it was riveting."
    anon "Heh, I see."
    anon "Thanks for letting us come over tonight, [saga.cast.erik]."
    show old_erik 4
    erik "Yeah, no problem, dude! You're lucky my guild canceled the raid tonight."
    show old_erik 1
    anon f_confused "Raid?"
    eve e_w f_surprised "No, don't ask!"
    show anon f_surprised
    show old_erik 51
    erik "..."
    show eve o_left

    if not test:
        show eve e_e

    eve f_happy "Is that booze over there?"
    show anon f_shy
    show old_erik 53
    erik "Y-yeah, why?"
    show old_erik 52
    eve @ e_b m_laugh "'Cause I have a feeling I'm gonna need some tonight!"
    anon "That's not a bad idea. It'll loosen us up for the karaoke."
    show old_erik 54
    erik "Oh yeah, I guess that makes sense."
    show old_erik 52
    show eve e_w
    pause
    eve "Hey, you've got bourbon, very classy!"

    if not test:
        show eve o_right

    eve "Why don't you go and grab us some glasses while [saga.cast.anon] and I get comfortable on the couch."
    show old_erik 54
    erik "... Sure, okay!"
    hide old_erik
    with dissolve
    show tammy_den erik

    if test:
        show eve o_right
    else:
        show eve o_left

    show eve p_surprised
    show anon f_surprised
    with dissolve.nowait
    eve "Can you believe [saga.cast.erik]'s basement is sooo cool?"

    if test:
        show anon a_eve_grab e_e at pos(.675)
    else:
        show anon a_eve_grab e_e o_left at pos(.325)

    show eve a_none o_left -p_surprised at pos.anon.grab
    eve "C'mon [saga.cast.anon], let's look at the other room!"
    hide anon
    hide eve
    with dissolve

    scene tammy_snug -anon -erik at stage(.5, .5, 2) with fade
    show anon f_shy at pos(.525)
    show eve a_shy f_surprised o_right at left
    with dissolve
    eve "Wow... This is so awesome..."
    anon "I know right? This is the perfect party house."
    eve f_happy "So have you ever had bourbon before?"
    anon f_confused "I don't think so..."
    eve "Get ready to have your mind blown!"
    show anon f_shy
    show old_erik 15 at pos(.7)
    with dissolve.nowait
    erik "I was wondering where you guys went."
    show anon o_right at pos(.435)
    erik "Will these work?"
    show old_erik 15b
    show anon e_sw
    show eve e_sw f_horny
    pause
    show anon e_e
    eve @ e_w f_happy "Sure."
    show anon e_sw
    show old_erik 16
    with dissolve.nowait
    pause
    show old_erik 15b
    with dissolve.nowait
    pause
    show anon a_shot
    show old_erik 16
    with dissolve.nowait
    pause
    show old_erik 15b
    with dissolve.nowait
    pause
    show anon e_e
    show eve a_whisky e_w
    show old_erik 17
    with dissolve.nowait
    eve "Bottoms up!"
    show anon a_shot_chug e_b f_calm m_drink
    show eve a_whisky_swig e_b f_calm m_drink
    show old_erik 19
    with dissolve.nowait
    pause
    show anon a_shot f_disgusted m_blow
    show old_erik 18
    show eve a_whisky e_ssw f_nervous -m_drink
    with dissolve.nowait
    erik "{i}*Cough* *Cough*{/i} It went down the wrong way! {i}*Cough*{/i}"
    show old_erik 17
    eve f_happy @ e_b m_laugh "Mmmhmm, that's some good shit right there!"
    show eve e_w
    anon @ e_sw "Wow!!! That's really strong!"
    eve "Don't puss out on me yet, boys!"
    show old_erik 18
    erik "Sure..."
    show anon a_side e_w f_shy -m_blow
    show eve a_shy
    show old_erik 15b
    pause
    show anon e_sw
    show eve e_sw f_horny
    show old_erik 16
    with dissolve.nowait
    pause
    show old_erik 15b
    with dissolve.nowait
    pause
    show anon a_shot
    show old_erik 16
    with dissolve.nowait
    pause
    show old_erik 15b
    with dissolve.nowait
    pause
    show eve a_whisky e_w
    show old_erik 17
    with dissolve.nowait
    pause
    show anon f_pensive
    eve "Drink!"
    show anon a_shot_chug e_b f_calm m_drink
    show eve a_whisky_swig e_b f_calm m_drink
    show old_erik 19
    with dissolve.nowait
    pause
    show old_erik 17
    with dissolve.nowait
    eve a_whisky @ f_happy m_laugh "Whooooo!"
    show anon a_shot e_sw f_disgusted
    show eve e_w f_happy -m_drink
    with dissolve.nowait
    anon "Damn!"
    anon @ e_b m_blow "..."
    anon f_worried "Alright, we should probably get this karaoke machine started up."
    hide anon with dissolve
    show tammy_snug anon
    show old_erik 18
    with dissolve.nowait
    erik "It's hot in here, is anybody else hot?"
    show old_erik 17
    eve "Heh, it's the booze, it warms up your insides..."
    anon "[saga.cast.erik], how the heck do you work this thing?"
    show eve a_whisky_swig e_b f_calm m_drink
    hide old_erik
    with dissolve.nowait
    erik "I'll do it, move."
    show tammy_snug erik erik -anon
    with dissolve
    pause
    show anon f_shy at right
    show eve a_whisky e_w f_happy -m_drink
    with dissolve
    anon "You ready to stretch those pipes of yours?"
    eve "Yeah, I'm gonna need a lot more booze before I'm ready to sing."
    eve "Why don't you guys get started without me?"
    anon a_rub "... Oh, ehh. Alright."
    show anon e_sw f_surprised
    erik "It's ready!"
    show eve f_surprised
    anon a_cheer e_w f_happy "Let's get this party started!"

    label mel02_eve_den.retry:
    call mini.rhythm

    if not _return:
        jump mel02_eve_den.fail

    label mel02_eve_den.cookie hide:
    scene tammy_snug -anon -erik at stage(.5, .5, 2)
    show old_erik 1 at face_right, pos(.4)
    show anon f_shy o_right at pos(.22)
    show eve a_point f_happy at right
    with fade
    eve "I'll show you amateurs how it's done!"
    eve @ a_calm_down "Out of my way, boys!"
    show old_erik 5
    show anon a_surprised f_surprised
    show eve a_hoodie_top_off c_casual_bottom
    pause
    hide eve with dissolve

    scene mono tammy_eve_sing
    mono "I guess the booze did its job because [saga.cast.eve] rocked that mic with some serious confidence!\nShe was amazing! I was completely blown away by how beautiful her voice was!" with fade
    mono "Perhaps I should have stopped her at three glasses though...\n... As it ended up being quite the show!"

    scene tammy_den -erik at stage
    show old_erik 57 at pos(.4), face_right
    show old_anon 83c at pos(.22), face_right
    show eve a_surprised c_casual_bottom e_b f_happy m_laugh at right
    with fade
    eve "WHOOOOO!!!"
    show eve a_shy e_w f_horny -m_laugh with dissolve
    show old_anon 83b
    anon "Damn girl, you rock!"
    show old_anon 83c
    eve "Thanks! I guess- {i}*Hic*{/i} I guess it isn't that bad singing in front of others."
    show old_anon 83b
    anon "Does that mean you'll sing in the talent show?!"
    show old_anon 83c
    eve @ e_nnw f_sad_pensive -m_talk "..."
    eve @ e_b f_happy m_laugh "Sure, why not!"
    show old_anon 83b
    anon "You're awesome!"
    anon "Maybe keep your clothes on for the talent show though."
    show old_anon 83c
    eve @ a_surprised e_ssw f_nervous "Hmm?"
    eve @ e_b f_happy m_laugh "Oh! Pfft!"
    eve @ e_b f_happy m_laugh "Hahahahaha!"
    eve "Whoopsie. Guess I- {i}*Hic*{/i} Guess I got carried away..."
    show old_erik 58
    show eve a_hoodie_top_off
    erik "Heh, it's okay. We don't mind."
    show old_erik 57
    eve a_shy c_casual @ f_surprised "Oh right, {i}*Hic*{/i} [saga.cast.erik]'s here..."
    eve @ e_b f_happy m_laugh "I completely forgot, hehehe."
    erik "..."
    show old_anon 79 with dissolve
    anon "I should probably help you get home."
    show old_anon 83c
    with dissolve
    eve f_happy @ e_b m_laugh "Aww, such a- {i}*Hic*{/i} such a gentleman!"
    eve "I'll just text my sis- {i}*Hic*{/i} She'll pick me up."
    show eve a_fold f_horny with dissolve
    show old_erik 58
    erik "I'll see you guys later."
    show old_erik 57
    show old_anon 83b
    anon "Thanks for the party, [saga.cast.erik]."
    show old_anon 83c
    eve @ a_wtf e_b f_happy m_laugh "Yeah, party! Whooooo!"
    show old_anon 83b
    show eve a_side
    anon "Heh, c'mon drunkie. Let's go home!"
    show old_anon 83c
    eve "I was really good wasn't- {i}*Hic*{/i} wasn't I, [saga.cast.anon]?"
    show old_anon 83b
    anon "You sure were."
    show old_anon 83c
    eve @ e_b f_happy m_laugh "Hehehe."
    hide eve
    hide old_anon
    with dissolve
    $ renpy.end_replay()

    scene black
    with dissolve
    mono ""
    return


label mel02_eve_den.alt(test=True):
    scene tammy_den dusk -erik at stage
    show anon a_pocket f_shy o_right at pos(.6) with dissolve
    pause
    show anon -o_right
    show eve a_shy o_right at pos(.3)
    show old_erik 1 at face_right, pos(.15)
    with dissolve
    anon "Hey, it's about time! I was starting to think you flaked on me!"
    eve f_confused "Wait..."
    eve f_surprised "... You were down here this entire time?"
    show eve f_angry
    show anon a_uneasy with dissolve.nowait
    anon @ -m_talk "..."
    jump mel02_eve_den.merge


label mel02_eve_den.fail:
    scene tammy_snug -anon -erik at stage(.5, .5, 2)
    show old_erik 3c at face_right, pos(.4)
    show anon f_worried o_right at pos(.22)
    show eve a_whisky f_happy at right
    with fade
    eve "Boo! You guys suck!"
    show anon f_pouty
    eve @ e_b m_laugh "Hahaha!"
    anon "I didn't know the words to that song!"
    anon f_pensive "[saga.cast.erik], pick another!"
    show old_erik 3b
    erik "Alright..."
    show old_erik 3c
    anon f_shy "Here we go!"
    jump mel02_eve_den.retry


label mel02_eve_den.rails:
    scene camera at stage
    show anon f_happy o_right with dissolve

    if saga.cast.anon in saga.sets.tammy_lobby:
        anon @ -m_talk "( The karaoke set-up is downstairs. )"
        anon e_nw f_pensive @ -m_talk "( I wonder if [saga.cast.eve] is already here. )"
    else:

        anon @ -m_talk "( It sure was nice of [saga.cast.erik] to agree to host tonight... )"
        anon a_uneasy e_e f_nervous m_teeth @ -m_talk "( ... Especially since I practically sprang it on him! )"

    hide anon with dissolve
    return


label mel02_kevin_ask:
    show old_anon 10
    anon "I'm helping [saga.cast.melody] find volunteers for the talent show."
    anon "Didn't you used to play the guitar?"
    show old_anon 5

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 2
    else:
        show old_kevin 9

    kevin "Yeah, I used to."

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 1
    else:
        show old_kevin 8

    show old_anon 10
    anon "What happened?"
    show old_anon 5

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 2
    else:
        show old_kevin 9

    kevin "Ah, my ex kinda smashed it after I broke up with him."

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 1
    else:
        show old_kevin 8

    show old_anon 12
    anon "Him?"
    show old_anon 11

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 2d with dissolve.nowait
    else:
        show old_kevin 11b with dissolve.nowait

    kevin "Did I say him? Sorry, I meant her."
    kevin "... Yeah, {i}she{/i} smashed it to pieces."

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 1 with dissolve.nowait
    else:
        show old_kevin 8 with dissolve.nowait

    show old_anon 14
    anon "Huh, you got a thing for the crazy girls, huh?"
    show old_anon 13

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 2d with dissolve.nowait
    else:
        show old_kevin 11b with dissolve.nowait

    kevin "Heh, you know it! Crazy girls, I'm waaaaay into them! Totally..."

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 1 with dissolve.nowait
    else:
        show old_kevin 8 with dissolve.nowait

    label mel02_kevin_ask.merge:
    show old_anon 14
    anon "So, if you had a guitar, would you play in the talent show?"
    show old_anon 13

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 2
    else:
        show old_kevin 9

    kevin "Yeah, I wouldn't mind."
    kevin "Where am I gonna get a guitar though? They are super expensive!"

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 1
    else:
        show old_kevin 8

    if saga.prop.guitar_fake in saga.cast.anon:
        show old_anon 34
        anon "( I need to switch my custom-made guitar with one in [saga.cast.erik]'s basement! )"
    else:

        show old_anon 35
        anon "Hmm, maybe I can find you one..."
        show old_anon 34
        anon "( [saga.cast.erik] has a bunch in his basement. Maybe I can borrow one? )"

    show old_anon 14
    anon "I'll be back!"
    show old_anon 13

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 2
    else:
        show old_kevin 9

    kevin "Alright."

    if saga.cast.kevin in saga.sets.school_cafe:
        show old_kevin 1
    else:
        show old_kevin 8

    hide old_anon with dissolve
    return


label mel02_kevin_erik:
    show old_anon 2
    anon "Hey man, I need a favor!"
    show old_anon 13
    show old_erik 4
    erik "Sure, what's up, dude?"
    show old_erik 1
    show old_anon 14
    anon "You know those guitars in your basement?"
    show old_anon 13
    show old_erik 5
    erik "Yeah."
    show old_erik 1
    show old_anon 10
    anon "You think I could borrow one for the talent show?"
    show old_anon 5
    show old_erik 5
    erik "... You wanna borrow one of Mr. [saga.cast.larry.clan]'s guitars?"
    show old_erik 52
    show old_anon 14
    anon "Yeah, if it's alright?"
    anon "I'll bring it back after the talent show."
    show old_anon 13
    show old_erik 50
    erik "Hmm."
    show old_erik 5
    erik "Well, I don't mind but I'm not sure [saga.cast.tammy] would like the idea of me loaning out Mr. [saga.cast.larry.clan]'s old stuff."
    show old_erik 52
    show old_anon 10
    anon "Really?"
    show old_anon 5
    show old_erik 5
    erik "Yeah, especially his guitars. They were his babies."
    show old_erik 52
    show old_anon 34
    anon "Hmm..."
    show old_anon 12
    anon "What if she didn't know?"
    show old_anon 5
    show old_erik 4
    erik "I'm pretty sure she'll notice if one is missing off the wall, [saga.cast.anon]. She isn't blind."
    show old_erik 52
    show old_anon 33
    anon "Not if I replace it with a fake."
    show old_anon 13
    erik "..."
    show old_erik 5
    erik "Seriously?"
    erik "Where are you gonna get a fake guitar?"
    show old_erik 52
    show old_anon 14
    anon "... I'll make one!"
    show old_anon 13
    show old_erik 5
    erik "Dude, have you lost your mind?"
    show old_erik 52
    show old_anon 14
    anon "No, trust me this will work."
    anon "She won't even notice it's gone, I promise!"
    show old_anon 13
    show old_erik 5
    erik "... If you say so. Just make sure nothing happens to the real guitar!"
    erik "[saga.cast.tammy] would kill me!"
    show old_erik 52
    show old_anon 14
    anon "I'll be careful, [saga.cast.erik]. I promise."
    label mel02_kevin_erik.merge:
    show old_anon 13
    hide erik_labcoat
    hide old_erik
    with dissolve

    if saga.cast.erik in saga.sets.school_science:
        show school_science erik
    else:
        show tammy_bed2 erik

    show old_anon 4
    with dissolve.nowait

    if saga.prop.misc_planks in saga.cast.anon or saga.prop.misc_planks_x2 in saga.cast.anon:
        anon "( Hmm, I should be able to make a fake guitar using the planks I already collected... )"
    else:
        anon "( Hmm, I should be able to make a fake guitar using the leftover planks from our treehouse... )"

    if saga.prop.paint_red in saga.cast.anon:
        anon "( ... And this can of paint I decided to carry around for some reason. )"
    else:
        anon "( ... And some paint. Pretty sure we have some in the garage at home. )"

    hide old_anon with dissolve
    return


label mel02_kevin_erik.kevin:
    jump mel02_kevin_ask.merge


label mel02_kevin_craft:
    scene mono debbie_garage_craft2
    mono "You know, I was really starting to dig all this hands-on woodworking. The school didn't offer any vocational courses, but perhaps they should have." with fade
    mono "As I continued, my mind began to drift, imagining my future life as a renouned carpenter, revered for my realistic creations."

    scene debbie_garage at stage
    show old_anon 575 at face_right
    with fade
    anon "Yikes! Maybe I'm not quite as ready for the big time as I thought!"
    anon "I hope this is good enough to fool [saga.cast.tammy] though."
    hide old_anon with dissolve
    return


label mel02_kevin_craft.erik:
    show old_anon 10
    anon "You're sure I can't just borrow one of Mr. [saga.cast.larry.clan]'s guitars?"
    anon "I'll bring it right back after the talent show."
    show old_anon 5
    show old_erik 3b
    erik "[saga.cast.tammy] would definitely notice the empty spot on the wall, dude."
    erik "What about your crazy plan to make a fake guitar?"
    show old_erik 1
    show old_anon 14
    anon "Still a work in progress."
    show old_anon 13
    show old_erik 5
    erik "Well, just be careful with the real guitar, please."
    show old_erik 1
    show old_anon 14
    anon "Will do!"
    jump mel02_kevin_erik.merge


label mel02_kevin_craft.item1:
    scene debbie_garage at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( I still need to find a decent amount of wood if I want to build a fake guitar. )"
    anon a_think e_sw f_pensive @ -m_talk "( I think there was some left over from our treehouse. )"
    hide anon with dissolve
    return


label mel02_kevin_craft.item2:
    scene debbie_garage at stage
    show anon f_shy o_right with dissolve
    anon @ -m_talk "( No one is going to be fooled by an obviously wooden guitar! )"
    anon e_nw @ -m_talk "( The red paint up on that shelf can help with that... )"
    anon a_fists e_b f_happy m_teeth @ -m_talk "( ... I'll paint it so well no one will be able to tell the difference! )"
    hide anon with dissolve
    return


label mel02_kevin_craft.late:
    jump mel01_craft.late


label mel02_kevin_craft.paint:
    scene debbie_garage at stage
    show old_anon 588 at face_right with dissolve
    anon "Paint: check!"
    show old_anon 587
    anon "( This looks like it'll be perfect for making a fake guitar indistinguishable from the original! )"
    hide old_anon with dissolve
    return


label mel02_kevin_craft.planks:
    call shot.meadow_main_planks
    show old_anon 585 with dissolve
    anon "Yeah, this should work."
    show old_anon 586
    pause
    anon "( With some tools and a little paint, I can make a fake guitar no problem. )"
    hide old_anon with dissolve
    return


label mel02_kevin_guitar(busy):
    scene tammy_den at stage(.55, .52, 3.5, b=0)
    show old_anon 575 at face_right with dissolve
    anon "( Hmm. )"
    show old_anon 574
    anon "( It's not that noticeable. )"
    show old_anon 575
    with dissolve.nowait
    anon "( ... Yeah, I think this might actually work! )"
    hide old_anon
    show anon a_surprised o_right p_stand_away at pos(.7)
    with dissolve.nowait
    pause
    show tammy_den -- guitar_fake -guitar_real
    with dissolve.nowait
    pause
    hide anon
    show old_anon 577 at face_right
    with dissolve.nowait
    anon "Mission accomplished!"
    show old_anon 576

    if busy:
        hide old_anon with dissolve
        return

    show old_tammy 14 at pos(.2), face_right
    with dissolve.nowait
    anon "( Now, I just need to get the real guitar out of here without [saga.cast.tammy] seeing me. )"
    with dissolve.nowait
    show old_tammy 19b
    tammy "What the hell is that?"
    show old_tammy 19c
    show old_anon 577d at pos(.675), face_left
    anon "!!!" with hpunch
    show old_anon 577c
    anon "H-hey, [saga.cast.tammy]..."
    anon "I didn't hear you come down."
    show old_anon 577b
    show old_tammy 19
    tammy "Did you make that thing, [saga.cast.anon]?"
    show old_tammy 50
    show old_anon 577c
    anon "Y-yeah. Do you like it?"
    show old_anon 577b
    show old_tammy 49
    tammy "Hehehe, is this so I won't notice you walking off with my ex-husband's guitar?"
    show old_tammy 50
    show old_anon 577c
    anon "... I just need to borrow it for the school talent show and [saga.cast.erik] thought you might get upset."
    show old_anon 577b
    show old_tammy 18
    tammy "Did he?"
    show old_tammy 49
    tammy "Aww, he's such a sweet young man to care about my feelings so much."
    show old_tammy 50
    show old_anon 577c
    anon "So, would you mind if I borrowed this guitar for a little while?"
    show old_anon 577b
    show old_tammy 18
    tammy "Pfft, not at all, honey."
    show old_tammy 49
    tammy "I never understood why that good for nothing ex of mine loved them so much. He wasn't even very good at playing them."
    tammy "You can keep the thing for all I care!"
    tammy "It's just sitting down here gathering dust after all."
    show old_tammy 50
    show old_anon 577
    anon "Really?"
    show old_anon 576
    show old_tammy 49
    tammy "Well, sure! You've been such a good friend to [saga.cast.erik]!"
    tammy "It's the least I can do!"
    show old_tammy 50
    show old_anon 577
    anon "Thank you so much, [saga.cast.tammy]!"
    show old_anon 576
    show old_tammy 49
    tammy "No problem, honey!"
    tammy "Just come back real soon and tell me all about this talent show of yours!"
    show old_tammy 50
    show old_anon 577
    anon "Yeah, okay! See you soon [saga.cast.tammy]!"
    hide old_anon with dissolve
    return


label mel02_kevin_give:
    show old_anon 14
    anon "I found a guitar for you!"
    show old_anon 13
    show old_kevin 3
    kevin "Really?"
    show old_kevin 1
    show old_anon 239_240
    with dissolve.nowait
    pause
    show old_anon 577 with dissolve.nowait
    anon "What do you think?"
    show old_anon 576
    show old_kevin 2d
    with dissolve.nowait
    kevin "Holy crap, bro! One sec!"
    hide old_kevin
    show old_anon 577b
    with dissolve.nowait
    anon "..."
    show old_kevin 9b at old_right with dissolve.nowait
    kevin "Where did you get that?"
    show old_anon 13
    show old_kevin 16
    with dissolve.nowait
    kevin "This thing is really high end!"
    show old_kevin 14
    show old_anon 10
    anon "It is?"
    show old_anon 5
    show old_kevin 15
    kevin "Uhh, yeah bro!"
    kevin "I hope you didn't steal it or something."
    show old_kevin 14
    show old_anon 14
    anon "Borrowed it actually, from a friend of mine. So be careful with it, yeah?"
    hide old_anon
    show old_kevin 27 at pos(.3895)
    with dissolve
    kevin "No problems there!"
    kevin "I'll treat this beauty with the respect it deserves!"
    show old_kevin 28
    anon "Cool, so you're down to play it for the talent show."
    show old_kevin 27
    kevin "I'm down!"
    show old_kevin 28
    anon "Awesome! I'll see you in [saga.cast.melody]'s class soon for practice then!"
    show old_kevin 27
    kevin "Sounds good, bro!"
    show old_anon 13 at old_left
    show old_kevin 16 at center, face_right
    with dissolve.nowait
    kevin "I'm gonna call you... Devin."
    show old_kevin 16 at right
    with dissolve.nowait
    kevin "Would you like that beautiful?"
    show old_anon 11
    hide old_kevin
    with dissolve.nowait
    anon "..."
    return


label mel02_outro:
    show old_anon 14
    anon "I found two more volunteers for the talent show!"
    show old_anon 13
    show old_melody 5
    melody "Really?! Who did you find and what do they play?"
    show old_melody 4
    show old_anon 14
    anon "Well, it turns out that [saga.cast.eve] is a singer."
    show old_anon 13
    show old_melody 5
    melody "You don't say! Is she any good?"
    show old_melody 4
    show old_anon 14
    anon "She's got a voice like an angel, you won't believe it!"
    show old_anon 13
    show old_melody 5
    melody "That's wonderful! Who else did you get?"
    show old_melody 4
    show old_anon 14
    anon "[saga.cast.kevin] is gonna play the guitar."
    show old_anon 13
    show old_melody 5
    melody "Well, now you're getting me excited! I've heard [saga.cast.kevin] play before, and he's very talented."
    show old_melody 4
    show old_anon 14
    anon "Yeah, I've heard good things."
    show old_anon 13
    show old_melody 5
    melody "Lord, [saga.cast.anon]! You've got the makings of your very own band!"
    show old_melody 8
    melody "As a matter of fact! That's not a bad idea!"
    show old_melody 4
    show old_anon 10
    anon "Huh?"
    show old_anon 5
    show old_melody 5
    melody "For the finale of the show, we should have all three of you play something together!"
    show old_melody 4
    show old_anon 10
    anon "Really?"
    show old_anon 11
    show old_melody 8
    melody "Absolutely! It's perfect!"
    show old_melody 4
    show old_anon 14
    anon "Heh, okay. If that's what you want?"
    show old_anon 13
    show old_melody 5
    melody "Oh, yay!! I can't wait to see this show!"
    show old_melody 23_22_23_22_27 once
    show old_anon 11
    with dissolve.nowait
    pause
    show old_anon 23
    show old_melody 24
    anon "!!!" with hpunch
    show old_anon 11
    show old_melody 25
    with dissolve.nowait
    melody "Oh! Shit!"
    melody "My bad, [saga.cast.anon]..."
    melody "My girls are trying to celebrate too!"
    show old_anon 14
    anon "Heh, it's alright. I don't mind."
    show old_anon 13
    show old_melody 16
    with dissolve.nowait
    melody "Oh, I bet you don't, sugar!"
    melody "I guess you can consider that a little extra reward for all your hard work."
    melody "If we manage to pull this talent show off, I might let you have a private viewing."
    show old_melody 15
    show old_anon 11
    anon "{i}*Gulp*{/i}"
    show old_melody 8
    melody "Aww, you're such a cutie!"
    show old_melody 4
    show old_anon 14
    anon "I should probably get back to practicing."
    show old_anon 13
    show old_melody 5
    melody "Now that's a good idea. Thanks again, [saga.cast.anon]."
    show old_melody 4
    show old_anon 36
    with dissolve.nowait
    anon "Bye, [saga.cast.melody]."
    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
