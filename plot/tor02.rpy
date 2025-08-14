label tor02_intro:
    call shot.school_science_door
    show old_tori 5 at old_right
    show anon a_pocket o_right at left with dissolve
    tori "Good, you're here. We can get started."
    show old_tori 4
    anon "Yeah, alright."
    anon "So what are we building first?"
    show old_tori 5
    tori "I'll show you."

    if saga.prop.plans_ocular in saga.cast.anon:
        tori "Hand me the blueprints."
        show old_tori 4
        show anon a_backpack e_s
        pause
        show anon a_plans_give e_w
        pause

    show anon a_side e_sw behind old_tori
    show old_tori 12 at center
    with dissolve
    tori "I call these beauties, the Okitatron Oculars."

    scene school_science base at stage(.6, .75, 15)
    show plans_ocular
    with fade
    pause
    anon "Glasses?"
    tori "Hah, not glasses..."
    tori "These are an optical head-mounted display, a true ubiquitous computer."

    call shot.school_science_door
    show anon a_pocket e_sw f_worried o_right at left
    show old_tori 13
    with fade
    anon e_w "I don't understand."
    show old_tori 9 at old_right
    with dissolve
    tori "Of course you don't. You're an imbecile."
    show old_tori 5
    tori "Let me just put it this way, the Okitatron Oculars will soon replace every smartphone on the planet."
    show old_tori 4
    anon "So it's a phone?"
    show old_tori 3
    tori "{i}*Sigh*{/i}"
    show old_tori 5
    tori "Let's just focus on building it, and once it's complete, I'll show you what it does..."
    show old_tori 4
    anon "Works for me."
    anon "How do we start?"
    show old_tori 10b with dissolve
    tori "Hmm."
    show old_tori 10c
    tori "Well, I'm missing a few components..."
    show old_tori 10b
    tori "..."
    show old_tori 5 with dissolve
    tori "I can gather most of what we need on my own."
    show old_tori 3
    tori "Could you find me a pair of lenses?"
    show old_tori 4
    anon "Lenses? Like in a telescope?"
    show old_tori 5
    tori "Not from a telescope. I need lenses from a pair of spectacles. Specifically, varifocal lenses."
    show old_tori 4
    anon @ f_confused "Varifocal?"
    show old_tori 3
    tori "Yes, that means it's a lens with two different prescriptions; a top and a bottom."
    show old_tori 4
    anon f_surprised "Like for someone who is both nearsighted and farsighted?"
    show old_tori 2
    tori "Precisely!"
    show old_tori 1
    anon "Hmm, I might be able to track something like that down."
    show old_tori 3
    tori "Might?"
    show old_tori 1
    anon "I mean, I know a few people who wear glasses. Maybe one of them have a spare set."
    show old_tori 2
    tori "Very good. Report back to me here, in the science lab, once you have them."
    show old_tori 1
    anon "Alright."
    hide anon with dissolve
    return


label tor02_judith1(when, misc):
    hide anon
    hide judith
    show old_judith 1 at old_right
    show old_anon 2 at old_left
    anon "[saga.cast.judith], are you farsighted or nearsighted?"
    show old_anon 1
    show old_judith 2
    judith "Uhh, well."
    show old_judith 3
    judith "Both..."
    show old_anon 2
    show old_judith 1
    anon "Really?!"
    show old_anon 1
    show old_judith 2
    judith "Yeah. I'm blind without my glasses..."
    show old_judith 3
    judith "Pretty dorky. I know..."
    show old_anon 2
    show old_judith 1
    anon "No, it's great!"
    show old_anon 1
    show old_judith 3
    judith "It is?"
    show old_anon 29 with dissolve
    show old_judith 1
    anon "Well, I mean, no. It sucks that you can't see without them."
    show old_anon 2 with dissolve
    anon "... But it's also a good thing, 'cause I'm looking for a pair of varifocal lenses."
    show old_anon 1
    show old_judith 5
    judith "Oh. Well, you found some."
    show old_anon 2
    show old_judith 4
    anon "You wouldn't happen to have a spare set, would you?"
    show old_anon 1
    show old_judith 5
    judith "Sure."
    show old_anon 2
    show old_judith 4
    anon "Awesome! Could I have them?"
    show old_anon 1
    show old_judith 2
    judith "Hmm, you want me to just give you my spare set?"
    show old_anon 10
    show old_judith 1
    anon "... Yes?"
    show old_anon 11
    show old_judith 3
    judith "How about a trade?"
    show old_anon 2
    show old_judith 1
    anon "Yeah, okay. What do you want?"
    show old_anon 1
    show old_judith 2
    judith "Umm, it's kinda embarrassing..."
    show old_judith 1
    anon "..."
    show old_judith 2
    judith "Well, you see, some of the other girls have been giving me a hard time..."
    show old_judith 3
    judith "... Because I've never had a boyfriend."
    show old_anon 10
    show old_judith 1
    anon "That sucks."
    show old_anon 11
    show old_judith 2
    judith "Yeah."
    judith "I was kinda wondering..."
    show old_judith 3
    judith "... Well, I was hoping you would pretend to be my boyfriend."
    show old_anon 23
    show old_judith 1
    anon "!!!" with hpunch
    show old_anon 10
    anon "You want me to pretend to be your boyfriend?"
    show old_anon 11
    show old_judith 3
    judith "Just long enough to take a couple pictures!"
    show old_anon 10
    show old_judith 1
    anon "Pictures?!"
    show old_anon 11
    show old_judith 2
    judith "Yeah."
    show old_judith 3
    judith "You meet me in the park, we take a couple pictures like we're boyfriend and girlfriend, and then I'll give you my spare set."
    judith "Deal?"
    show old_anon 10
    show old_judith 1
    anon "I uhh..."
    show old_anon 11
    show old_judith 3
    judith "Pleeeease? It would be such a huge help!"
    show old_anon 2
    show old_judith 1
    anon "Yeah, alright, I suppose I can do that."
    show old_anon 1
    show old_judith 5
    judith "You will?!"

    if when == 0:
        judith "Okay, meet me at the park! I'll be there this afternoon."
    elif when == 1:
        judith "Okay, meet me at the park! I'll be there tomorrow afternoon."
    else:
        judith "Okay, meet me at the park! I'll be there on [saga.time.dow + when] afternoon."

    show old_anon 2
    show old_judith 4

    if when == 0:
        anon "The park, this afternoon. Got it!"
    elif when == 1:
        anon "The park, tomorrow afternoon. Got it!"
    else:
        anon "The park, [saga.time.dow + when] afternoon. Got it!"

    show old_anon 1
    show old_judith 5
    judith "Great! See you there!"
    hide old_anon with dissolve
    return


label tor02_judith1.erik:
    show old_anon 2
    anon "I'm helping [saga.cast.tori] out with a project."
    show old_anon 1
    show old_erik 4
    erik "Really? Awesome!"
    erik "What kinda project is it?"
    show old_anon 2
    show old_erik 1
    anon "Uhh, I don't think I'm supposed to say..."
    show old_anon 1
    show old_erik 4
    erik "Oh, top secret research?"
    erik "Cool, can I help?"
    show old_anon 2
    show old_erik 1
    anon "Actually, yes!"
    anon "I need to find a couple of thick lenses."
    anon "You wouldn't happen to have a spare set of glasses, would you?"
    show old_anon 1
    show old_erik 4
    erik "You kidding?"
    erik "Do you know how many times [saga.cast.dexter] has broken this pair?"
    erik "I always keep a spare set close."
    show old_anon 2
    show old_erik 1
    anon "Great!!"
    anon "Would you let me have them?"
    show old_anon 1
    show old_erik 4
    erik "Sure!"
    show old_anon 2
    show old_erik 1
    anon "Thanks, man!"
    show old_anon 1
    show old_erik 4
    erik "No problem, [saga.cast.anon]! What are friends for?"
    show old_anon 10
    show old_erik 1
    anon "... Oh, wait!"
    show old_anon 29 with dissolve
    anon "I forgot, they need to be varifocal lenses..."
    show old_anon 3
    show old_erik 5
    erik "Vari-what?"
    show old_anon 10 with dissolve
    show old_erik 1
    anon "Are you farsighted or nearsighted?"
    show old_anon 11
    show old_erik 5
    erik "Nearsighted. Why?"
    show old_anon 10
    show old_erik 1
    anon "Crap! I need lenses from someone who is both."
    show old_anon 11
    show old_erik 5
    erik "Oh."
    show old_anon 24
    show old_erik 1
    anon "{i}*Sigh*{/i}"
    show old_anon 10
    anon "I guess I'll have to keep looking."
    show old_anon 11
    show old_erik 5
    erik "Sorry, [saga.cast.anon]."
    show old_anon 2
    show old_erik 1
    anon "It's alright, [saga.cast.erik]. Thanks anyways."
    show old_anon 1
    show old_erik 4
    erik "Anytime, man."
    hide old_anon with dissolve
    return


label tor02_judith1.june:
    show old_anon 2
    anon "Hey, so uhh..."
    anon "I'm kinda helping [saga.cast.tori] with a project."
    show old_anon 1
    show old_june 4
    june "[saga.cast.tori] asked you for help with her designs?"
    show old_anon 10
    show old_june 2
    anon "Yes."
    anon "... And we need some lenses, like from a pair of glasses?"
    show old_anon 11
    show old_june 4
    june "You want my glasses?"
    show old_anon 10
    show old_june 2
    anon "Well, I was hoping you might have a spare set?"
    show old_anon 11
    show old_june 4
    june "Nope, just the one."
    show old_anon 10
    show old_june 2
    anon "Maybe I could convince you to give me that pair?"
    show old_anon 11
    show old_june 4
    june "I doubt it."
    show old_anon 10
    show old_june 2
    anon "Hmm, are you farsighted or nearsighted?"
    show old_anon 11
    show old_june 3
    june "Nearsighted."
    show old_anon 29 with dissolve
    show old_june 2
    anon "Oh, never mind then."
    anon "I need a pair from someone who is both."
    show old_anon 3
    show old_june 4
    june "I can't believe [saga.cast.tori] asked {i}you{/i} to help with her projects..."
    show old_anon 29
    show old_june 2
    anon "Well, she's kinda, forcing me..."
    show old_anon 3
    show old_june 6
    june "Yeah, that sounds more like her."
    show old_june 3
    june "Well, good luck."
    show old_anon 2 with dissolve
    show old_june 2
    anon "Yeah, thanks."
    hide old_anon with dissolve
    return


label tor02_judith1.tori:
    anon "What did you want me to find again?"
    show old_tori 3
    tori "Pfft, you have one task to do and you've forgotten it?"
    show old_tori 4
    anon f_sad "I-I guess so..."
    show old_tori 9
    tori "Typical."
    show old_tori 5
    tori "I need you to find a pair of varifocal lenses."
    show old_tori 4
    anon @ a_point "Oh, right! Both farsighted and nearsighted."
    show old_tori 5
    tori "Correct."
    show old_tori 3
    tori "Perhaps I should write it backwards on your forehead, so you won't forget?"
    show old_tori 4
    anon f_worried "... No, that's alright. I've got it now."
    tori "Mmmhmm."
    hide old_tori with dissolve
    anon a_think "( Hmm, I should check around school and see if someone has a spare set of varifocal lenses. )"
    hide anon with dissolve
    return


label tor02_pause:
    return


label tor02_pause.judith(when):
    hide anon
    hide judith
    show old_judith 1 at old_right
    show old_anon 2 at old_left
    anon "Where did you want to take that picture again?"
    show old_anon 1
    show old_judith 3
    judith "Oh umm, at the park..."

    if when == 0:
        judith "... This afternoon."
    elif when == 1:
        judith "... Tomorrow afternoon."
    else:
        judith "... on [saga.time.dow + when] afternoon."

    show old_anon 2
    show old_judith 1
    anon "Alright."
    show old_anon 1
    show old_judith 3
    judith "You aren't having second thoughts, are you?"
    show old_judith 2
    judith "'Cause it's okay, we don't hav-"
    show old_anon 2
    show old_judith 1
    anon "No, [saga.cast.judith]. It's fine, really!"
    show old_judith 4
    anon "I'll meet you there!"
    show old_anon 1
    show old_judith 5
    judith "... Thanks, [saga.cast.anon]."
    hide old_anon with dissolve
    return


label tor02_pause.tori:
    anon f_calm "I've got a lead on those lenses you want."
    show old_tori 2
    tori "That's wonderful news, [saga.cast.anon]!"
    show old_tori 1
    anon e_nw f_pensive "Of course, getting them will require me posing as [saga.cast.judith]'s boyfriend for a photo op..."
    show anon e_w f_surprised
    show old_tori 3
    tori "Yeesh!"
    show old_tori 5
    tori "Say no more, [saga.cast.anon], we'll find another way."
    show old_tori 4
    anon a_up "What?! No that's-"
    show old_tori 5
    tori "While it's true that as scientists, we must be willing to sacrifice in the name of humankind's advancement..."
    show old_tori 11
    tori "... Not even I, it's most devout pupil, would demean myself in such a ludicrous way!"
    show old_tori 4
    anon a_side f_confused "It's not that big a deal, [saga.cast.tori]..."
    show old_tori 3
    anon f_shy "... I don't mind posing for a photo with her."
    show anon f_surprised
    show old_tori 11
    tori "One should {i}not{/i} negotiate with terrorists, [saga.cast.anon]."
    show old_tori 5
    show anon f_worried_surprised
    tori "Not even when they're offering fissile material at exorbitantly low prices."
    show anon f_surprised m_teeth
    tori "I learned that lesson the hard way."
    show old_tori 4
    anon @ -m_talk "..."
    anon f_worried -m_teeth "Really, it's fine."
    anon f_shy "I've got this."
    show anon f_worried_surprised
    show old_tori 5
    tori "That's just what I thought too, right before that interdimensional portal swallowed up my last lab assistant."
    show old_tori 4
    anon @ -m_talk "..."
    anon a_point_back "Erm... I just remembered I have a thing I need to-"
    show anon a_wave at pos(.175)
    anon "Bye!"
    hide anon with dissolve
    pause
    show old_tori 84
    with dissolve.nowait
    tori "Poor Trevor."
    show old_tori 83
    tori "..."
    show old_tori 95
    with dissolve.nowait
    tori "Travis?"
    show old_tori 10
    with dissolve.nowait
    pause
    show old_tori 10c
    with dissolve.nowait
    tori "Tristin?"
    show old_tori 10b
    pause
    show old_tori 10c
    tori "Trenton?"
    show old_tori 10b
    tori "..."
    show old_tori 9
    with dissolve.nowait
    tori "Eh, it's not important."
    return


label tor02_judith2:
    scene park_main -judith at stage(.15, .6, 4)
    show old_judith 5 at old_right
    show old_anon 1 at old_left with dissolve
    judith "You really came!"
    show old_anon 2
    show old_judith 4
    anon "I told you I would."
    show old_anon 1
    show old_judith 5
    judith "This is wonderful! I can't tell you how much this means to me."
    show old_anon 2
    show old_judith 4
    anon "It's no problem, [saga.cast.judith]."
    anon "What do you need me to do?"
    show old_anon 1
    show old_judith 5
    judith "... Just, come sit next to me."
    show old_anon 2
    show old_judith 4
    anon "Alright."

    scene park_bench_front
    show old_judith sitting 4
    show old_judith sitting arms 2 as judith_arms
    with fade
    show old_anon front 2
    show old_anon front arms 1 as anon_arms
    with dissolve
    anon "Like this?"
    show old_anon front 2b
    show old_judith sitting 5
    judith "No, silly."
    show old_judith sitting 8 at pos(.43)
    show old_judith sitting arms 4 as judith_arms at pos(.43)
    show old_anon front 2f
    show old_judith sitting arms 3 overlay as judith_hand at pos(.43)
    with dissolve
    judith "Like this!"
    judith "Smile!"

    scene mono park_judith_bench
    mono "I'm not sure how this picture was supposed to help [saga.cast.judith]?" with fade
    mono "... But it seemed like a small price to pay for the lenses [saga.cast.tori] wanted, though."
    mono "Plus it made [saga.cast.judith] really happy!"

    scene park_bench_front
    show old_judith sitting 6 at pos(.43)
    show old_judith sitting arms 2 as judith_arms at pos(.43)
    show old_anon front 2b
    show old_anon front arms 1 as anon_arms
    with fade
    judith "This is perfect!"
    show old_judith sitting 5
    judith "Thank you so much, [saga.cast.anon]!"
    show old_anon front 2
    show old_judith sitting 4
    anon "No problem."
    show old_anon front 2c
    anon "So about that spare set of glasses..."
    show old_judith sitting 2
    show old_judith sitting arms 1 as judith_arms
    show old_anon front 2b
    judith "Ohh, of course!"
    judith "I keep them in my locker at school."
    show old_judith sitting 3
    judith "I can write down the combination for you, just one second."
    show old_judith sitting 1
    show old_anon front 2c
    anon "That's alright, I don't need the combination."
    show old_anon front 2b
    show old_judith sitting 2
    judith "You don't?"
    show old_judith sitting 1
    show old_anon front 2c

    if saga.prop.key_school in saga.cast.anon:
        anon "I have a master key to all the lockers."
        show old_anon front 2b
        show old_judith sitting 5
        judith "Really?! How did you manage to get that?"
        show old_anon front 2c
        show old_judith sitting 4
        anon "Heh, I have my ways."
    else:

        anon "I know where [saga.cast.ursula] keeps her master key..."
        show old_anon front 2b
        show old_judith sitting 5
        judith "Really?! You're going to steal the Principal's key?"
        show old_anon front 2c
        show old_judith sitting 4
        anon "Steal?! I dunno about that... I just wanna borrow it 'til they get me a new lock."

    show old_anon front 2b
    show old_judith sitting 5
    judith "That's so awesome!"
    judith "I had no idea you were such a bad boy!"
    show old_anon front 2c
    show old_judith sitting 4
    anon "Uhh, yeah. Heh, I guess..."
    anon "Thanks for the help, [saga.cast.judith]. I'll see you around."
    show old_anon front 2b
    show old_judith sitting 5
    judith "Thank you, [saga.cast.anon]! See you soon!"
    hide old_anon
    hide anon_arms
    with dissolve
    return


label tor02_judith2.memo:
    scene school_hall1w at stage
    show anon f_confused with dissolve
    anon @ -m_talk "( That's odd... )"
    anon @ -m_talk "( ... For once, this hallway doesn't smell like egg salad and stale donuts. )"
    anon a_think e_nw f_pensive @ -m_talk "( I wonder what's going- )"
    anon a_surprised_up e_w f_surprised @ m_teeth "( Oh my god, I'm supposed to be meeting [saga.cast.judith] in the park right now!! )"
    hide anon with dissolve
    return


label tor02_flake(misc):
    if saga.cast.judith in saga.sets.school_hall1w:
        call shot.school_hall1w_judith
    else:
        scene school_art -judith at stage

    show judith a_clasp f_surprised at right
    show anon a_wave o_right at left with dissolve.nowait
    anon "Hey, [saga.cast.judith]."
    judith e_s f_sad "... H-hello."
    anon a_side f_shy "Aww, that rain cloud over your head looks darker than usual today..."
    anon "... What's going on?"

    if misc < 2:
        judith "I waited in the park for you..."
        judith "... But you never showed up."
    else:

        judith "I waited in the park for you again..."
        judith "... But you still never showed up."

    anon f_confused @ -m_talk "Hmm?"
    judith e_w "Remember, you said I could take a picture of-"
    anon f_calm "Oh, right!"
    anon a_facepalm "Sheesh, I totally forgot about that [saga.cast.judith]... my bad!"
    judith "Oh, it's okay..."
    judith "... You probably had something more important to do."
    anon a_rub f_shy "Hmm, no... not really."
    anon "Heh, it just sorta slipped my mind, ya know?"
    judith "Y-yeah, I get it."
    judith e_s "If I was in your shoes, I'd probably forget about me too."
    show anon a_handshake f_calm behind judith at pos(.475)
    show judith e_sw f_surprised
    with dissolve.nowait
    anon "Hey, c'mon... chin up!"
    show judith e_w
    pause
    show anon a_side at left
    show judith f_shy
    with dissolve
    return


label tor02_retry1(when, misc):
    anon "We can try again."
    judith f_confused "You mean, you're still willing to take a photo with me in the park?"
    anon "Sure!"
    judith f_happy @ f_surprised "Really, you will?!"
    anon "When do you want to meet?"
    show judith f_calm

    if when == 0:
        judith "Umm, this afternoon?"
    elif when == 1:
        judith "Umm, tomorrow afternoon?"
    else:
        judith "Umm, [saga.time.dow + when] afternoon?"

    anon "Sounds good."
    anon a_point "Then you can give me the lenses next time we're at school."
    judith f_sad "Oh, right... the lenses."
    show anon a_side
    anon @ f_worried "That's still okay, right?"
    judith f_shy "Of course... totally!"
    judith "Anything for a chance to-"
    judith @ e_se f_surprised "Err, I mean... uhh..."
    judith "... Y-yeah, I guess it's only fair."
    anon "Cool!"
    show judith f_calm
    anon "I'll see you then."
    judith f_happy "I can't wait!"
    hide anon with dissolve
    return


label tor02_locker:
    return


label tor02_locker.item:
    scene school_hall1w at stage
    show anon with dissolve
    anon @ -m_talk "( Hmm, pretty certain [saga.cast.judith] said she keeps her spare glasses in here. )"
    anon f_worried @ -m_talk "( I guess I could swallow my pride and ask [saga.cast.judith] ... )"
    anon a_think e_nw f_pensive @ -m_talk "( ... {i}Or{/i} maybe I could look into the master key that [saga.cast.annie] mentioned. )"
    hide anon with dissolve
    return


label tor02_locker.judith:
    anon a_point f_confused "Do you have those glasses I asked for?"
    judith e_ssw f_sad "Mhmm, they're in my locker."
    anon a_side "And it's cool if I take them?"
    judith e_w f_shy "Of course, [saga.cast.anon], you can take anything you want!"
    anon a_uneasy f_shy "Oh, umm... thanks."
    anon "Really, just need the glasses though."
    judith e_s f_sad "Right... Yeah, totally."
    pause
    judith e_w f_shy "Here, let me open it for you."
    hide judith

    if saga.cast.judith in saga.sets.school_hall1w:
        show anon a_side o_left
    else:
        show anon a_surprised o_right p_stand_away

    with dissolve.nowait
    anon "Thanks, [saga.cast.judith]."
    hide anon with dissolve
    return


label tor02_hall1w:
    jump mel01_hall1w


label tor02_hall1w.rails:
    scene camera at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( [saga.cast.judith]'s always seems so timid... )"
    anon f_confused @ -m_talk "( ... Though she does sometimes phrase things really strangely. )"
    pause
    anon f_calm @ -m_talk "( I should get out there and grab those glasses. )"
    hide anon with dissolve
    return


label tor02_specs:
    scene locker_judith
    anon "( This must be her spare set. )"
    anon "( Now, I just need to get these back to [saga.cast.tori]. )"
    return


label tor02_specs.rails:
    scene locker_judith
    anon "( I didn't go to all this trouble to {i}not{/i} collect her glasses! )"
    return


label tor02_tori:
    call shot.school_science_door
    show old_tori 4 at old_right
    show old_anon 2 at old_left with dissolve

    if saga.prop.specs_judith in saga.cast.anon:
        anon "[saga.cast.tori], I've got them!"
        anon "I've got the lenses you wanted!"
        show old_anon 1
        show old_tori 3
        tori "Let me see those!"
        show old_tori 16 with dissolve
        tori "Yes, these should do nicely."
        show old_tori 14
    else:

        anon "[saga.cast.tori], are the lenses ready?"
        show old_anon 1
        show old_tori 5
        tori "Yes, yes."
        show old_tori 14 with dissolve
        tori "I've inspected them and they should do nicely."

    show old_tori 5 at pos(.85), face_right
    with dissolve.nowait
    tori "Alright, get over here and start assembling."
    show old_anon 10
    hide old_tori
    with dissolve.nowait
    anon "Whoa, you want me to build them?"
    show old_anon 11
    show old_tori 9 at pos(.85)
    with dissolve.nowait
    tori "Obviously."
    show old_anon 10
    show old_tori 4
    anon "But I can't do that!"
    show old_anon 5
    show old_tori 5
    tori "Why not?"
    show old_anon 10
    show old_tori 4
    anon "I thought these were important? You should do it."
    show old_anon 5
    show old_tori 5
    tori "No, that's monkey work."
    show old_tori 9
    tori "[saga.cast.tori.name] [saga.cast.tori.clan] doesn't do monkey work..."
    show old_tori 4
    anon "..."
    show old_anon 10
    anon "What if I screw something up?"
    show old_anon 5
    show old_tori 5
    tori "The directions are right there!"
    show old_tori 3
    tori "Can't you follow simple directions?!"
    show old_tori 4
    show old_anon 10
    anon "... Yes."
    show old_anon 5
    show old_tori 5
    tori "Well then, show some backbone and get to work."
    show old_tori 4
    anon "..."
    show old_anon 12
    anon "Fine."

    label tor02_tori.merge:
    scene mono school_science_glasses1
    mono "So I set myself to working." with fade

    if saga.cast.anon.int < 5:
        jump tor02_tori.fail

    label tor02_tori.cookie hide:
    call shot.school_science_bench
    show old_anon 538 at old_right
    with fade
    anon "Alright!"
    show old_anon 540 with dissolve
    anon "One pair of Okitatron Oculars, ready for testing!"
    show old_anon 540b
    show old_tori 3 behind stools at pos(.4), face_right
    with dissolve
    tori "Hmm, did you check the seal on the casing?"
    show old_anon 538 with dissolve
    show old_tori 1
    anon "Oh, right! Okay, one second."
    show old_anon 538b
    show old_tori 4
    tori "..."
    show old_kevin 8 behind old_tori at pos(.15), face_right
    show old_kevin labcoat 1 as kevin_labcoat behind old_tori at pos(.15), face_right
    with dissolve
    pause
    show old_kevin 9
    kevin "Excuse me, [saga.cast.tori]?"
    show old_kevin 8
    show old_tori 5
    tori "And make sure the power unit is charged!"
    show old_kevin 9
    show old_tori 4
    kevin "Umm, [saga.cast.tori]? Could you help us with something?"
    show old_kevin 8
    show old_tori 9
    tori "Ugh."
    show old_tori 3 at face_left with dissolve
    tori "Yes, [saga.cast.kevin]. What is it?"
    show old_kevin 9
    show old_tori 4
    kevin "[saga.cast.rhonda] and I were working on the assignment you handed out during class today, and we ran into a problem."
    show old_kevin 8
    show old_tori 9
    tori "{i}*Sigh*{/i}"
    show old_tori 5
    tori "Of course you did..."
    show old_tori 3
    tori "Very well. Let's do it over by my desk. [saga.cast.anon] is working on something important for me."
    hide old_kevin
    hide kevin_labcoat
    with dissolve
    hide old_tori
    with dissolve
    pause
    anon "Hmm..."
    show old_anon 538
    anon "Everything looks good."
    show old_anon 539 with dissolve
    anon "This is cool!"

    scene school_science base at stage(.18, .49, 3)
    show old_tori 4 at pos(.7)
    show old_kevin 9 at pos(.375), face_right
    show old_kevin labcoat 1 as kevin_labcoat at pos(.375), face_right
    show rhonda c_lab f_curious o_right of_ppe at pos(.175)
    show old_xtra 38b
    with fade
    anon "Hmm, all the functions seem to be working..."
    anon "..."
    anon "Just need to test the camera."
    show old_xtra 38
    show rhonda b_xray
    show old_kevin labcoat 1b as kevin_labcoat
    show old_tori goggles xray view as tori_xray behind old_xtra at pos(.7)
    with none.nowait
    pause .25
    show old_xtra 38b
    show old_kevin labcoat 1 as kevin_labcoat
    show rhonda -b_xray
    hide tori_xray
    with none.nowait
    anon "What the-"
    show old_tori 5
    show old_kevin 8
    anon "... Did that just?"
    show old_xtra 38
    show old_kevin labcoat 1b as kevin_labcoat
    show rhonda b_xray
    show old_tori goggles xray view as tori_xray behind old_xtra at pos(.7)
    with none.nowait
    pause .25
    show old_xtra 38b
    show rhonda -b_xray
    show old_kevin labcoat 1 as kevin_labcoat
    hide tori_xray
    with none.nowait
    pause .25
    show old_xtra 38
    show rhonda b_xray
    show old_kevin labcoat 1b as kevin_labcoat
    show old_tori goggles xray view as tori_xray behind old_xtra at pos(.7)
    with none.nowait
    pause .25
    show old_xtra 38b
    show rhonda -b_xray
    show old_kevin labcoat 1 as kevin_labcoat
    hide tori_xray
    with none.nowait
    anon "They were naked for a second..."
    show old_tori 4
    show old_kevin 9
    anon "..."
    anon "Maybe if I hold down the button?"
    show old_xtra 38
    show rhonda b_xray
    show old_kevin labcoat 1b as kevin_labcoat
    show old_tori goggles xray view as tori_xray behind old_xtra at pos(.7)
    with none.nowait
    anon "!!!" with hpunch
    anon "Whoa!"
    anon "These are like for real X-ray goggles!"
    pause
    anon "... I don't think that's supposed to happen."
    pause
    show old_tori 5
    show old_kevin 8
    anon "I can see [saga.cast.tori]'s..."
    pause
    anon "... And look at the body on [saga.cast.rhonda]! She's so fit!"
    pause
    anon "..."
    show old_tori 4
    show old_kevin 9
    anon "Oh my god! I can see [saga.cast.kevin]'s..."
    pause
    show old_kevin 8 at pos(.1), face_left
    show old_kevin labcoat 1b as kevin_labcoat at pos(.1), face_left
    hide rhonda
    show old_tori 9
    with dissolve
    anon "Uh oh, I got it stuck in this mode!"
    hide old_kevin
    hide kevin_labcoat
    show old_tori 4 at pos(.85), face_right
    show old_tori goggles xray view as tori_xray at pos(.85), face_right
    with dissolve
    anon "She's coming back!!"
    hide old_tori
    hide tori_xray
    with dissolve.nowait
    anon "No, no, no!"

    call shot.school_science_bench
    show old_anon 22 at old_right
    show old_anon 541 as glasses at old_right
    with fade
    show old_tori 5 behind stools at pos(.35), face_right with dissolve
    tori "Well?"
    show old_anon 11
    show old_tori 4
    anon "..."
    show old_tori 11
    tori "[saga.cast.anon]?"
    show old_anon 10
    show old_tori 11b
    anon "Y-yeah?"
    show old_anon 11
    show old_tori 11
    tori "What's the matter with you?!"
    tori "Give me the glasses!"
    show old_anon 10
    show old_tori 11b
    anon "Oh, r-right..."
    show old_anon 540c
    hide glasses
    with dissolve
    anon "Here ya go."
    show old_anon 11
    show old_tori 103
    tori "Hmm."
    show old_tori 4
    show old_tori goggles xray3 as tori_specs at pos(.35), face_right
    with dissolve
    anon "..."
    show old_tori 3
    tori "Why is everything green?"
    show old_tori 4
    pause
    show old_tori 95
    tori "... And why are you-"
    show old_tori 94
    show old_anon 22
    pause
    show old_tori 10c with dissolve
    tori "Hmm."
    tori "That's peculiar."
    show old_anon 11
    show old_tori 10b
    anon "..."
    show old_tori 10c
    tori "... Very peculiar."
    show old_tori 10b
    pause
    $ renpy.end_replay()
    hide tori_specs
    show old_tori 104
    with dissolve
    tori "[saga.cast.anon], do you still have the code to my office?"
    show old_tori 105
    show old_anon 10
    anon "Yes, [saga.cast.tori]."
    show old_anon 73
    with dissolve.nowait
    pause
    show old_tori 94
    show old_anon 459
    with dissolve.nowait
    pause
    show old_anon 461
    show old_tori 5
    tori "Then go and wait for me upstairs in my office."
    show old_tori 4
    show old_anon 460
    anon "Huh?"
    show old_anon 461
    show old_tori 5
    tori "Right now."
    hide old_tori
    hide tori_specs
    show old_anon 11
    with dissolve
    pause
    show old_anon 10
    anon "Uh... Okay."
    show old_anon 11
    anon "( I wonder why she wants to see me in her office? )"
    hide old_anon with dissolve
    return True


label tor02_tori.fail:
    scene mono school_science_glasses2 with dissolve
    mono "In hindsight I can see how my reaction to the developing situation rapidly spiralling out of my control may not have inspired confidence..."
    mono "... But at the time it really {i}did{/i} feel like I should make certain, and the only way to do that was to ask the question..."

    call shot.school_science_door
    show old_tori 11 at old_right
    show old_anon 16 at pos(.35), face_right
    show old_anon labcoat 1 as anon_labcoat at pos(.35), face_right
    show old_anon labcoat 1b as anon_specs at pos(.35), face_right
    with fade
    tori "No, they are absolutely not supposed to be smoking!"
    show old_anon 12
    show old_tori 11b
    anon "... Well, I'm sorry!"
    anon "I told you, I'm not qualified to work on something like this!"
    show old_anon 16
    show old_tori 11
    tori "You had better figure it out and quick!"
    tori "... Otherwise, you can forget about passing my class."
    show old_anon 12
    show old_tori 11b
    anon "Ugh, fine! I'll try again next time."
    show old_anon 16
    show old_tori 9
    tori "Yes, yes. Just keep attending class and finish these soon."
    show old_tori 11
    tori "... And brighten up, will you?!"
    hide old_tori
    show old_anon 24
    with dissolve.nowait
    anon "{i}*Sigh*{/i}"
    show old_anon 25
    anon "I guess I should go home and work on my intelligence..."
    hide old_anon
    hide anon_labcoat
    hide anon_specs
    with dissolve
    return


label tor02_tori.tori:
    anon "I've got those lenses for you, [saga.cast.tori]."
    show old_tori 3
    tori "Are they varifocal, like I requested?"
    show old_tori 4
    anon "Yes, ma'am."
    show old_tori 2
    tori "Excellent."
    show old_tori 14 with dissolve
    tori "Hmm..."
    show old_tori 15
    anon f_confused "Something wrong?"
    show old_tori 14
    tori "... Oh, it's nothing, just-"
    show anon f_worried_surprised
    show old_tori 16
    with dissolve.nowait
    tori "These are probably the most visually unappealing pair of varifocals I've ever seen!"
    tori "Where did you even find them?"
    show old_tori 15
    with dissolve.nowait
    anon f_shy "They're [saga.cast.judith]'s spare set."
    show old_tori 14
    tori "Truly, astonishingly awful!"
    show old_tori 15
    pause
    show anon f_calm
    show old_tori 5
    tori "Well, I suppose they'll have to do."
    show old_tori 10c
    tori "I'll need some time to fract, refract, defract, and fractdefract them."
    show old_tori 10b
    anon a_surprised f_surprised "Wha- huh?!"
    show old_tori 11
    tori "It's all very technical, best not to think about it."
    show anon a_side f_grumpy
    show old_tori 9
    tori "Don't want you injuring that cute little monkey brain of yours."
    show old_tori 4 at pos(.85), face_right
    with dissolve
    anon "Geez, thanks."
    hide old_tori with dissolve.nowait
    pause
    anon "And you're walking away now..."
    anon "... Yeah, okay..."
    anon "... I guess we're done."
    anon a_pocket "Cool."
    hide anon with dissolve
    return


label tor02_redux:
    jump tor02_tori


label tor02_redux.tori:
    anon f_confused "How are things going with the-"
    show anon f_shocked m_open
    show old_tori 11
    tori "Shhhh!!!"
    show anon f_surprised -m_open
    show old_tori 11
    tori "Not while I'm fracting!"
    hide old_tori with dissolve.nowait
    anon a_finger "..."
    show anon a_side e_sw
    pause
    anon a_finger e_w "..."
    show anon a_side e_sw f_confused
    pause
    anon e_w "I guess I'll check back later then."
    hide anon with dissolve
    return


label tor02_retry2:
    call shot.school_science_door
    show old_tori 4 at old_right
    show old_anon 2 at old_left with dissolve
    anon "Alright, [saga.cast.tori]. I think I'll do better this time."
    show old_anon 1
    show old_tori 9
    tori "You couldn't possibly do any worse."
    show old_anon 16
    show old_tori 4
    anon "..."
    show old_anon 12
    anon "I'll get them to work this time, I know it!"
    show old_anon 16
    show old_tori 5
    tori "Well, just try not to distract the rest of the class. Go take your seat, [saga.cast.anon]."
    show old_anon 2
    show old_tori 4
    anon "I'm ready, let's do this!"
    show old_anon 1
    show old_tori 5
    tori "By all means."
    hide old_anon with dissolve
    jump tor02_tori.merge


label tor02_retry2.tori:
    anon "Everything ready for our project, [saga.cast.tori]?"
    show old_tori 2
    tori "Yes, I believe so... but you'll need to do the work during class."
    show old_tori 1
    anon "Oh?"
    show old_tori 3
    tori "Don't want that dull-witted swine of a principal to suspect anything, do we?"
    show old_tori 4
    anon "Oh."
    anon "Yeah, I suppose we don't."
    return


label tor02_office2:
    call shot.school_office2_entry
    with fade
    show old_anon 11 with dissolve
    anon "( I wonder wha- )"
    show old_anon at face_right
    show old_tori 4 at old_right
    with dissolve
    anon "..."
    show old_anon 10
    anon "You wanted to see me, ma'am?"
    show old_anon 11
    show old_tori 5
    tori "Have a seat, [saga.cast.anon]."
    show old_anon 10
    show old_tori 4
    anon "In your office chair, you sure?"
    hide old_anon
    show old_tori 65 at pos(.65)
    with dissolve.nowait
    tori "Quite sure."

    scene school_office2_chair
    pause .1
    show old_tori 67 as old_anon
    anon "Oof!" with vpunch
    show old_tori 66 as old_anon
    show old_tori 61
    with dissolve.nowait
    pause
    show old_tori 67 as old_anon
    anon "Uhh, is this about the device?"
    show old_tori 66 as old_anon
    show old_tori 62
    pause
    show old_tori 63
    tori "No, this is about something the device showed me."
    show old_tori 64
    anon "..."
    show old_tori 63
    tori "I noticed an anomaly."
    show old_tori 67 as old_anon
    anon "A what?"
    show old_tori 66 as old_anon
    show old_tori 63
    tori "... Something unusual about your biology."
    show old_tori 67 as old_anon
    show old_tori 64
    anon "Uhh, okay."
    show old_tori 66 as old_anon
    show old_tori 63
    tori "Would you unzip your pants please?"
    show old_tori 67 as old_anon
    show old_tori 64
    anon "You're serious?!"
    show old_tori 66 as old_anon
    show old_tori 63
    tori "Yes, I need to inspect your penis."
    show old_tori 64
    anon "( !!! )" with hpunch
    show old_tori 67 as old_anon
    anon "M-my penis?!"
    anon "Is there something wrong with it?"
    show old_tori 66 as old_anon
    show old_tori 63
    tori "Possibly, that's why I want to take a look."
    show old_tori 67 as old_anon
    show old_tori 64
    anon "O-okay."
    show old_tori 68 as old_anon
    pause
    show old_tori 69 as old_anon
    pause
    show old_tori 70 as old_anon
    pause
    show old_tori 71 as old_anon
    anon "Sorry for the-"
    anon "I mean..."
    anon "..."
    show old_tori 70 as old_anon
    show old_tori 63
    tori "... This is quite remarkable!"
    show old_tori 71 as old_anon
    show old_tori 64
    anon "Like good remarkable or is something wrong with it?"
    show old_tori 70 as old_anon
    show old_tori 63
    tori "It's just highly unusual..."
    show old_tori 71 as old_anon
    show old_tori 64
    anon "W-what is?"
    hide old_anon
    show old_tori 72_73
    anon "!!!" with hpunch
    show old_tori 70 as old_anon behind old_tori
    show old_tori 63
    with dissolve.nowait
    tori "Your reproductive organ..."
    tori "It exceeds the norm of average Homo sapiens."
    tori "... By quite a bit actually."
    hide old_anon
    show old_tori 72_73
    anon "Oh, uhh. Thanks, I guess?"
    pause
    show old_tori 70 as old_anon behind old_tori
    show old_tori 63
    with dissolve
    tori "There has to be an underlying cause."
    show old_tori 64
    anon "..."
    show old_tori 63
    tori "Have you been exposed to any unusual radiation?"
    hide old_anon
    show old_tori 72_73
    anon "... No?"
    show old_tori 70 as old_anon behind old_tori
    show old_tori 63
    with dissolve
    tori "Hmm, curious..."
    tori "Are you taking any medication?"
    show old_tori 71 as old_anon
    show old_tori 64
    anon "... No."
    show old_tori 70 as old_anon
    tori "..."
    show old_tori 63
    tori "Most curious."
    show old_tori 64
    anon "..."
    show old_tori 63
    tori "Alright, [saga.cast.anon], you can put it away now."
    tori "I'll have to think on this a while."
    hide old_tori with dissolve
    $ renpy.end_replay()

    scene school_office2 at stage(.75, .42, 2)
    show old_tori 4 at old_right
    with fade
    show old_anon 10 at old_left with dissolve
    anon "What about the Okitatron Oculars?"
    show old_anon 11
    show old_tori 5
    tori "Oh yes, quite the screw up."
    show old_tori 4
    anon "..."
    show old_tori 5
    tori "Though it might actually work out to my benefit."
    show old_tori 3
    tori "I'm sure there are plenty of applications for X-ray technology."
    show old_tori 5
    tori "{i}If{/i} I can isolate the cause."
    show old_anon 10
    show old_tori 4
    anon "Okay, well, what now?"
    show old_anon 11
    show old_tori 5
    tori "Head on home. I'll sort it out."
    tori "We'll work on a new device next time."
    show old_anon 2
    show old_tori 4
    anon "Alright, sounds good!"
    anon "See you then."
    show old_anon 1
    tori "Mmmhmm."
    hide old_anon with dissolve
    return


label tor02_office2.rails:
    scene camera at stage
    show anon f_confused with dissolve
    anon @ -m_talk "( Why was [saga.cast.tori] eye-balling me like that... )"
    anon @ -m_talk "( ... And what could she possibly want with me in her office?! )"
    anon f_worried @ -m_talk "( I have a bad feeling about this. )"
    hide anon with dissolve
    return


label tor02_office2.tori:
    call shot.school_science_door
    show old_tori 1 at old_right
    show anon f_worried o_right at left with dissolve
    show old_tori 2
    tori "Proceed up to my office, [saga.cast.anon]."
    tori "I'll be along momentarily."
    show old_tori 1
    anon "Are you sure that's really necessary, I-"
    show old_tori 5
    tori "And don't touch anything!"
    show old_tori 4
    anon f_tired "{i}*Sigh*{/i} Yes, ma'am."
    hide anon with dissolve
    return


label tor02_outro:
    return


label tor02_outro.block:
    call shot.school_office2_door
    show anon f_worried with dissolve
    anon @ -m_talk "( No, thanks... I've had enough poking and prodding for today! )"
    anon f_calm @ -m_talk "( Let's find literally anything else to do. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
