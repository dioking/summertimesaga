label tor03_intro:
    call shot.school_science_door
    show old_tori 4 at old_right
    show anon a_pocket o_right at left with dissolve
    anon "Hey, [saga.cast.tori]. Have you solved the problem with the glasses?"
    show old_tori 3
    tori "You mean the Okitatron Oculars?"
    show old_tori 4
    anon "Yeah, sorry. T-that's what I meant."
    show old_tori 5
    tori "Yes, I sorted it out. I'm in the process of patenting them now."
    show old_tori 4
    anon "That's good news, right?"
    show old_tori 5
    tori "It's good for a start."
    show old_tori 3
    tori "... But never mind the Oculars, [saga.cast.anon]!"
    tori "Yesterday's news!"
    show old_tori 1
    anon @ e_b f_happy m_laugh "... O-okay."
    show old_tori 2
    tori "Today I've got something truly innovative!"
    show old_tori 1
    anon f_sceptical "More innovative than X-ray glasses?"
    show old_tori 3
    tori "Oh, please. X-ray technology hasn't been innovative since the 1980s."
    show old_tori 1
    anon f_confused @ -m_talk "..."
    show anon e_sw behind old_tori at center
    show old_tori 12
    with dissolve
    tori "I call this, the Okitatron Belt."

    scene school_science base at stage(.6, .75, 15)
    show plans_belt
    with fade
    pause
    anon "... Belt?"
    tori "Yeah, the name could use some work..."

    call shot.school_science_door
    show anon a_pocket e_sw f_worried o_right
    show old_tori 12 at old_right
    with fade
    tori "But I'll worry about that later!"
    tori "For now, let's focus on what the device does."
    show anon e_w
    show old_tori 2
    with dissolve
    tori "The Okitatron Belt is gonna revolutionize the way people keep in shape!"
    show old_tori 1
    anon f_confused @ -m_talk "..."
    anon "You mean it's a workout device?"
    show old_tori 2
    tori "No. This is going to make exercise a thing of the past!"
    tori "It targets all of the major muscle groups with undetectable micro-vibrations!"
    tori "It stimulates muscle growth so you'll never have to workout again!"
    show old_tori 1
    anon f_calm "That sounds incredible!"
    show old_tori 9
    tori "Well, of course it's incredible! Who do you think you're talking to?"
    show old_tori 1
    anon @ -m_talk "..."
    show old_tori 2
    tori "However, I'm missing a key component."
    show old_tori 1
    anon @ e_b f_happy m_laugh "... Which is where I come in?"
    show old_tori 2
    tori "Precisely!"
    show old_tori 3
    tori "These micro-vibrations have to be fine-tuned to a very specific frequency otherwise, it won't work."
    show old_tori 1
    anon "Okay, so how do we do that."
    show old_tori 2
    tori "We'll need a faptic engine."
    show old_tori 1
    anon f_worried @ f_sceptical "... Huh?"
    show old_tori 3
    tori "A faptic engine."
    show old_tori 1
    anon a_think e_b f_hurt m_teeth @ -m_talk "..."
    show old_tori 9
    tori "{i}*Sigh*{/i}"
    show old_tori 5
    show anon a_pocket e_w f_worried -m_teeth
    tori "Go find [saga.cast.june]. She's helped me out with tough projects in the past."
    tori "Tell her I sent you for a faptic engine."
    tori "She'll know what to do."
    show old_tori 4
    anon a_rub f_calm "A faptic engine. Alright, I'll be back."
    hide anon
    show old_tori 9
    with dissolve
    tori "Poor kid is dumber than a box of rocks..."
    return


label tor03_june1:
    show old_anon 2
    anon "[saga.cast.tori] wants me to get her something called a faptic engine. She told me you could help?"
    show old_anon 1
    show old_june 4
    june "What the heck does she want with one of those?"
    show old_anon 2
    show old_june 2
    anon "She says she needs it for her newest invention."
    show old_anon 1
    show old_june 4
    june "Hah. What crazy thing has she come up with this time?"
    show old_anon 2
    show old_june 2
    anon "It sounds pretty neat actually, it's a-"
    show old_anon 1
    show old_june 3
    june "No, don't tell me! I'm sure I don't wanna know."
    show old_anon 11
    show old_june 2
    anon "..."
    show old_anon 10
    anon "Can you help me or not?"
    show old_anon 11
    show old_june 4
    june "I doubt it. Does it need to be authentic?"
    show old_anon 10
    show old_june 2
    anon "Err, I assume so."
    show old_anon 11
    show old_june 4
    june "Well, that's gonna be hard to come by."
    show old_anon 10
    show old_june 2
    anon "What is a faptic engine anyways?"
    show old_anon 11
    show old_june 3
    june "Oh, you don't know?"
    june "It's a tiny piece of machinery that provides tactile sensations. They just started putting them in the top-of-the-line smartphones."
    show old_anon 10
    show old_june 2
    anon "Tactile sensations?"
    show old_anon 11
    show old_june 4
    june "Sensations you feel with your skin. In this case, vibrations."
    show old_anon 2
    show old_june 2
    anon "Oh, I get it now."
    anon "So why is it so hard to get?"
    show old_anon 1
    show old_june 3
    june "Well, putting aside the fact that those phones are super expensive..."
    show old_anon 11
    show old_june 4
    june "They are currently sold out, like everywhere!"
    show old_anon 10
    show old_june 2
    anon "How expensive are we talking?"
    show old_anon 11
    show old_june 4
    june "Around two thousand dollars."
    show old_anon 23
    show old_june 2
    anon "!!!" with hpunch
    show old_anon 10
    anon "What?! For a phone?!"
    show old_anon 11
    show old_june 4
    june "I told you they are top-of-the-line."
    show old_june 3
    june "It really doesn't matter though, didn't you hear me? They are completely sold out."
    show old_anon 10
    show old_june 2
    anon "Well shoot! What am I gonna tell [saga.cast.tori]?"
    show old_anon 11
    show old_june 3
    june "It's a shame she wants authentic. There are some pretty good quality knock-off versions that you might be able to get your hands on."
    show old_anon 10
    show old_june 2
    anon "Hmm, would it work as well as the authentic ones?"
    show old_anon 11
    show old_june 4
    june "Well, no, but pretty close. It would depend on what you're using it for."
    show old_june 3
    june "In most cases, I'd say the knock-off would do the trick."
    show old_june 2
    anon "..."
    show old_anon 10
    anon "Alright, where would I get the knock-off version?"
    show old_anon 11
    show old_june 3
    june "Well, they were putting them into those Master Blaster controllers a few years ago."
    show old_anon 10
    show old_june 2
    anon "Master Blaster? Like the video game?"
    show old_anon 11
    show old_june 3b
    june "Yeah! I always wanted one but my parents couldn't afford it."
    show old_anon 2
    show old_june 2
    anon "You know what? I think [saga.cast.erik] used to have one of those!"
    show old_anon 1
    show old_june 6
    june "Does he still have it?"
    show old_anon 2
    show old_june 5
    anon "No idea."
    show old_anon 1
    show old_june 6
    june "Well, if you manage to get your hands on one, I could take the faptic engine out for you."
    show old_anon 2
    show old_june 2
    anon "Great! I'll go talk to [saga.cast.erik] and see if he still has it."
    anon "Thanks for the info, [saga.cast.june]."
    hide old_anon
    show old_june 3
    with dissolve.nowait
    june "Good luck!"
    return


label tor03_june1.tori:
    anon f_worried "Where am I supposed to get this faptic engine thingy again?"
    show old_tori 3
    tori "You don't have it yet?"
    show old_tori 9
    tori "{i}*Sigh*{/i}"
    show old_tori 5
    tori "Just go talk to [saga.cast.june], she will explain."
    show old_tori 4
    anon f_calm @ e_b f_happy m_laugh "Oh, right! I'll be right back."
    hide anon with dissolve
    return


label tor03_erik:
    show old_anon 2
    anon "You remember that Master Blaster game [saga.cast.tammy] bought you for Christmas a few years ago?"
    show old_anon 1
    show old_erik 4
    erik "Of course, man! We spent the entire summer playing on that thing!"
    show old_anon 2
    show old_erik 1
    anon "Do you still have it?"
    show old_anon 1
    show old_erik 5
    erik "Yeah, I think so. Haven't used it in a long time..."
    show old_erik 4
    erik "In fact, I think it's just collecting dust in our old tree house."
    show old_anon 2
    show old_erik 1
    anon "Would you mind if I take it?"
    show old_anon 1
    show old_erik 4
    erik "Sure, no problem."
    show old_anon 2
    show old_erik 1
    anon "Thanks, [saga.cast.erik]!"
    hide old_anon with dissolve
    return


label tor03_erik.gamepad:
    scene meadow_treehouse at stage
    show old_anon 502b with dissolve
    anon "( There it is! )"
    anon "( Man, [saga.cast.erik] sure did love this thing... )"
    pause
    anon "( I should speak to him about it first though, I don't want to just take it. )"
    hide old_anon with dissolve
    return


label tor03_erik.june:
    show old_anon 2
    anon "What was the name of that controller again?"
    show old_anon 1
    show old_june 4
    june "The Master Blaster."
    show old_june 3
    june "Didn't you say you thought [saga.cast.erik] had one?"
    show old_anon 2
    show old_june 2
    anon "Yeah, he used to..."
    anon "I'll go ask him about it."
    anon "Thanks, [saga.cast.june]."
    show old_anon 1
    show old_june 3
    june "Good luck!"
    hide old_anon with dissolve
    return


label tor03_erik.tori:
    anon f_worried "So I spoke with [saga.cast.june] about that engine thingy and she thinks we could get a knock-off to save-"
    show old_tori 3
    tori "You don't need to update me with every minute detail, [saga.cast.anon]..."
    show anon a_finger at pos(.3)
    show old_tori 4 at face_right, pos(.8)
    with dissolve.nowait
    anon "Okay, but I really think-"
    show old_tori 9
    tori "{i}*Sigh*{/i}"
    show old_tori 5 at old_right
    with dissolve.nowait
    tori "... Just get it done!"
    show old_tori 4
    anon a_side f_tired "Alright, sheesh!"
    hide anon with dissolve
    return


label tor03_gamepad:
    scene meadow_treehouse at stage
    show old_anon 502b with dissolve
    anon "( It's nice of [saga.cast.erik] to let me take this. )"
    show old_anon 502
    anon "( I'd best get it to [saga.cast.june]. )"
    hide old_anon with dissolve
    return


label tor03_gamepad.erik:
    show old_anon 2
    anon "Where did you say that controller was again?"
    show old_anon 1
    show old_erik 5
    erik "I think I left it in our old tree house."
    show old_anon 2
    show old_erik 1
    anon "Ah, that's right. Thanks, [saga.cast.erik]!"
    show old_anon 1
    show old_erik 4
    erik "No problem, dude!"
    show old_erik 1
    return


label tor03_gamepad.june:
    show old_anon 2
    anon "So it turns out that [saga.cast.erik] does still have a Master Blaster..."
    anon "... And he said we can have it!"
    show old_anon 1
    show old_june 3b
    june "Nice! Where is it?"
    show old_june 2
    show old_anon 2
    anon "In our old treehouse."
    show old_anon 1
    show old_june 4
    june "Umm, well not much I can do with it from here, dude."
    show old_anon 5
    show old_june 3
    june "Let me know when you have it and we can see about extracting that faptic engine."
    show old_june 1
    show old_anon 10
    anon "Right."
    show old_anon 14
    anon "Thanks, [saga.cast.june], I'll be back."
    hide old_anon with dissolve
    return


label tor03_june2:
    show old_anon 502
    with dissolve
    anon "Is this the thing you were talking about?"
    show old_anon 1
    show old_june 11
    with dissolve
    june "Hey, you actually got one. Awesome!"
    show old_anon 2
    show old_june 12
    anon "So, you can take the faptic engine out of this?"
    show old_anon 1
    show old_june 11
    june "Absolutely."
    june "Just give me a few minutes to take it apart."
    show old_anon 2
    show old_june 12
    anon "Alright."
    show old_anon 1
    show old_june 11
    june "This is so cool!"

    scene black
    with dissolve
    mono ""

    call shot.school_tech_june
    show old_anon 1 at old_left
    show old_june 13 at old_right
    with dissolve
    june "There we go, one knock-off faptic engine."
    show old_anon 2
    show old_june 14
    anon "That's it? It's so tiny..."
    show old_anon 505
    show old_june 18
    with dissolve
    june "Yup, it's a little thing but it packs a punch."
    show old_anon 506
    show old_june 17
    anon "Alright, I'd better get this to [saga.cast.tori]."
    show old_anon 505
    show old_june 19
    june "Say, [saga.cast.anon]?"
    june "Would you mind if I keep the controller?"
    show old_anon 2 with dissolve
    show old_june 17
    anon "No, not at all. Knock yourself out!"
    show old_anon 1
    show old_june 18
    june "Sweet! Thanks, [saga.cast.anon]!"
    hide old_anon with dissolve
    return


label tor03_tori1:
    anon "Okay..."
    show old_tori 8
    anon "... I've got that Faptic Engine thing you wanted."
    show old_tori 2
    tori "Already?"
    tori "Great work, [saga.cast.anon]!"
    show old_tori 1
    anon f_shy "Yeah, thanks."
    show old_tori 10c
    tori "Now I just need to weave the piezoelectric fibers into a suitable lining and we're in business."
    show old_tori 10b
    anon f_calm "You should probably know that it's not an authentic-"
    show old_tori 5
    tori "Yes, yes... I'll take it from here, [saga.cast.anon]."
    show old_tori 10b
    anon f_worried "B-but-"
    show old_tori 10c
    tori "I'll need to make certain the school's power grid can handle the manufacturing process."
    show old_tori 10b
    anon a_finger "Umm, [saga.cast.tori]?"
    show old_tori 10c
    tori "Come back later, [saga.cast.anon]!!"
    show old_tori 10
    anon a_side f_tired "... Okay."
    anon @ -m_talk "( I guess she's got this... probably. )"
    hide anon with dissolve
    return


label tor03_delay:
    return


label tor03_delay.tori:
    anon f_confused "Making any progress with the belt?"
    show old_tori 2
    tori "It's nearly there, just a few small hurdles left to clear."
    show old_tori 1
    anon "Anything I can help with?"
    show old_tori 2b
    tori "Hah, I highly doubt it!"
    anon f_pouty @ -m_talk "..."
    show old_tori 2
    tori "Just make certain you're ready to work once I've ironed out the kinks."
    tori "Mistakes at this stage could prove rather... volatile."
    show old_tori 1
    anon a_surprised f_worried_surprised "This thing isn't going to explode, is it?"
    show old_tori 9
    tori "Don't be ridiculous, [saga.cast.anon]."
    show old_tori 4
    anon a_side f_shy "Okay, phew!"
    show old_tori 5
    tori "It just might pulverize your bones into tapioca pudding."
    show old_tori 4
    anon a_surprised_up f_surprised "What?!"
    show old_tori 2
    tori "Oh, relax..."
    show anon a_side
    tori "... should that highly unlikely event come to pass, your demise will be instantaneous and completely painless."
    show old_tori 10b
    anon f_pouty "That does {i}not{/i} make me feel better!"
    hide anon with dissolve
    return


label tor03_tori2:
    call shot.school_science_door
    show old_tori 3 at old_right
    show old_anon 1 at old_left with dissolve
    tori "Did you bring it?"
    show old_anon 506 with dissolve
    show old_tori 4
    anon "I've got it right here, [saga.cast.tori]..."
    show old_anon 505
    show old_tori 3
    tori "Hmm, something looks off..."
    show old_tori 5
    tori "This is what [saga.cast.june] had you get?"
    show old_tori 4
    show old_anon 10 with dissolve
    anon "Err, yes ma'am."
    show old_anon 11
    show old_tori 10b with dissolve
    tori "..."
    show old_tori 5 at right with dissolve
    tori "Perhaps it's just my imagination then."
    anon "..."
    show old_tori 4
    tori "Very well, you can go ahead and get started on the belt."
    show old_anon 10
    show old_tori 5
    anon "Okay."
    show old_anon 11
    show old_tori 3
    tori "Just follow the directions..."
    show old_tori 5
    tori "... And try not to screw it up."
    show old_tori 4
    show old_anon 25
    anon "{i}*Sigh*{/i} Yes, ma'am."

    scene mono school_science_belt1
    mono "So it was that I set to work. Fastidiously adhering to the detailed blueprints, brimming with confidence that having already built X-ray goggles there was no way a belt could best me." with fade

    label tor03_tori2.merge:
    if saga.cast.anon.int < 8:
        jump tor03_tori2.fail

    call shot.school_science_bench
    show old_anon 550 at old_right
    with fade
    anon "That's it! I've got it!"
    show old_anon 549
    show old_tori 5 behind stools at old_left with dissolve
    tori "Let's see it."
    show old_anon 1
    show old_tori 23
    with dissolve
    pause
    show old_tori 22
    tori "Hmm, yes... It all looks correct."
    show old_tori 23
    pause
    show old_tori 22
    tori "Let's head up to my office for this next part, [saga.cast.anon]."
    tori "Testing will require a bit of privacy..."
    show old_anon 10
    show old_tori 23
    anon "... Privacy?"
    hide old_tori with dissolve
    show old_anon 11
    pause
    show old_anon 10
    anon "I wonder what she meant by that?"
    hide old_anon with dissolve
    return True


label tor03_tori2.fail:
    scene mono school_science_belt2 with dissolve
    mono "A cynic may have labelled me delusional, but I still prefer view it as having been ever so slightly unjustifiably optimistic."

    call shot.school_science_door
    show old_anon 11 at old_left
    show old_anon labcoat 1 as anon_labcoat at old_left
    show old_anon labcoat 1b as anon_specs at old_left
    show old_tori 11 at old_right
    with fade
    tori "Seriously, again?!"
    show old_anon 10
    show old_tori 11b
    anon "I-I'm sorry, I dunno what-"
    show old_anon 11
    show old_tori 11
    tori "Grr... Well, you had better figure it out!"
    tori "I need this thing working!"
    tori "... Otherwise, you can forget about passing my class."
    show old_anon 12
    show old_tori 11b
    anon "Ugh, fine! I'll try again tomorrow."
    show old_anon 16
    show old_tori 9
    tori "Yes, yes. Just get back here and finish this soon."
    show old_tori 11
    tori "... And brighten up, will you?!"
    hide old_tori
    show old_anon 24
    with dissolve
    anon "I should go home and work on my intelligence again."
    hide old_anon
    hide anon_labcoat
    hide anon_specs
    with dissolve
    return


label tor03_retry:
    call shot.school_science_door
    show old_tori 4 at old_right
    show old_anon 2 at old_left with dissolve
    anon "Hi, [saga.cast.tori]. I'll definitely do better this time."
    show old_anon 1
    show old_tori 9
    tori "Well it would be difficult for you to do any worse."
    show old_anon 16
    show old_tori 4
    anon "..."
    show old_anon 12
    anon "I'll get it right this time, I know it!"
    show old_anon 16
    show old_tori 5
    tori "Well, just try not to start any fires. I don't need {i}another{/i} visit from the fire marshal."
    show old_anon 2
    show old_tori 4
    anon "No to fire. Got it!"
    show old_anon 1
    show old_tori 5
    tori "Then by all means."
    hide old_anon with dissolve

    scene mono school_science_belt1
    mono "I could feel it. This was it. I was in the zone. Nothing and no one was going to prevent me constructing that belt and impressing [saga.cast.tori] this iime." with fade
    jump tor03_tori2.merge


label tor03_retry.tori:
    anon a_point f_calm "I'm ready to take another crack at that belt of yours."
    show old_tori 3
    tori "A crack?"
    show anon a_surprised f_surprised m_teeth
    show old_tori 5
    tori "You're not trying to hit a baseball here, [saga.cast.anon]... This is delicate work!"
    show old_tori 4
    anon a_uneasy f_shy -m_teeth "Well, yeah... I know that, it's just-"
    show anon f_surprised
    show old_tori 5
    tori "It's academic..."
    show anon a_side f_confused
    show old_tori 11
    tori "... Any work we do at this time of day will undoubtedly run afoul of that meddling heathen of a principal."
    show old_tori 4
    anon f_worried "Oh, right."
    show old_tori 5
    tori "We can continue our work during class time."
    show old_tori 4
    anon "Yes, ma'am."
    hide anon with dissolve
    return


label tor03_office2:
    scene school_office2 -tori at stage(.45, .45, 1.75)
    show old_tori 2 at old_left
    show old_anon 11 at pos(.7) with dissolve
    tori "There you are, ready to test this thing?"
    show old_anon 10
    show old_tori 1
    anon "Yeah, I guess... What do you need me to do?"
    show old_anon 11
    show old_tori 99 at pos(.35) with dissolve
    tori "Take your pants off and put this on."
    show old_anon 10
    show old_tori 100
    anon "Take my pants off?! Like everything?"
    show old_anon 11
    show old_tori 99
    tori "Yes, the device needs to be in direct contact with your skin to work."
    show old_anon 10
    show old_tori 100
    anon "I dunno about this..."
    show old_anon 11
    show old_tori 99
    tori "Pfft, what's the problem? I've already seen it, remember?"
    show old_anon 10
    anon "Of course I remember! I just..."
    show old_anon 11
    anon "..."
    show old_tori 99
    tori "Time is wasting here, [saga.cast.anon]."
    show old_anon 10
    show old_tori 100
    anon "{i}*Sigh*{/i} Fine!"
    show old_anon 261b with dissolve
    pause
    show old_anon 63
    show old_anon belt 3 as anon_belt at pos(.7)
    show old_tori 10c
    with dissolve
    tori "How does it feel?"
    show old_anon 64
    show old_tori 10b
    anon "..."
    show old_anon 367
    anon "I don't feel anything."
    show old_anon 64
    show old_tori 9 with dissolve
    tori "Well, of course not, you dolt, I haven't turned it on yet..."
    show old_tori 3
    tori "I meant, is it comfortable?"
    show old_anon 367
    show old_tori 4
    anon "Yeah, I suppose."
    show old_tori 26 with dissolve
    show old_anon 64
    pause
    show old_tori 27
    pause
    hide anon_belt
    show old_anon belt 1
    show old_tori 26
    anon "Whoa!!!" with hpunch
    show old_tori 25
    tori "Feeling something now?"
    show old_anon 367 behind old_tori
    show old_anon belt 2 as anon_belt behind old_tori at pos(.7)
    show old_tori 4
    with dissolve
    anon "Y-yeah! It's vibrating! A {i}lot{/i}!"
    show old_anon 64
    show old_tori 3
    tori "Hmm, you should just be feeling a slight pressure exerted on your muscles..."
    show old_anon 367
    show old_tori 4
    anon "No, this definitely feels like vibrations! Really strong vibrations!"
    show old_anon 64
    show old_tori 11
    tori "Well, what did you do?!"
    show old_anon 367
    show old_tori 11b
    anon "Nothing, I built it exactly like the blueprint said!"
    show old_anon 64
    show old_tori 11
    tori "Grr, let me see!"
    show old_tori 91b at pos(.49, 1.145) with dissolve
    anon "..."
    tori "..."
    show old_anon 367
    anon "Uhh..."
    anon "... [saga.cast.tori], this isn't really-"
    show old_anon 64
    show old_tori 91
    tori "Shh!!"
    tori "I'm trying to think..."
    show old_tori 91b
    pause
    show old_tori 92 with dissolve
    anon "..."
    tori "..."
    show old_tori 93
    tori "Drats!"
    show old_tori 3 at pos(.35, 1.) with dissolve
    tori "Alright, take it off..."
    show old_tori 5
    tori "And put your pants back on!"
    hide anon_belt
    show old_anon 261b
    show old_tori 22
    with dissolve
    tori "I just don't understand..."
    show old_anon 11
    with dissolve
    tori "Everything looks correct!"
    show old_tori 23
    pause
    show old_tori 22
    tori "... Grr."
    show old_tori 23
    pause
    show old_tori 22
    tori "I'll tinker with it."
    tori "You're excused, [saga.cast.anon]."
    show old_anon 10
    show old_tori 23
    anon "Should I come back tomorrow?"
    show old_anon 11
    show old_tori 22
    tori "Yes, yes, tomorrow."
    hide old_anon with dissolve
    return


label tor03_office2.rails:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( [saga.cast.tori] asked me to meet her in her office. )"
    anon @ -m_talk "( Best not keep her waiting. )"
    hide anon with dissolve
    return


label tor03_outro:
    return


label tor03_outro.block:
    jump tor02_outro.block
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
