label tor05_intro:
    if saga.cast.anon in saga.sets.school_science:
        call shot.school_science_door
        show old_tori 1 at right
        show anon a_wave o_right at left with dissolve
    else:
        call shot.school_office2_tori
        show old_tori 1 at face_right
        show anon a_wave at right with dissolve

    anon "Hey, [saga.cast.tori]! Are you feeling any better?"
    show old_tori 2
    tori "Never mind that, [saga.cast.anon]."
    show anon a_pocket f_confused
    tori "I'm glad you're here, there's work to be done!"
    show old_tori 1
    anon f_worried @ f_sad "{i}*Sigh*{/i} You never let up, do you?"
    show old_tori 5
    tori "I'll let up when my inventions are published and those Cuntech creeps are eating a big bowl of crow!"
    show old_tori 4
    anon "... Fine."
    anon "What crazy invention are we working on this time?"
    show old_tori 10c with dissolve
    tori "Hmm, we'll have to take a detour from the inventions for the time being."
    tori "At least until we get [saga.cast.ursula] off of my case!"
    show old_tori 10b
    anon "How are we supposed to accomplish that?"
    show old_tori 10c
    tori "I've been pondering that myself..."
    show old_tori 2 with dissolve
    tori "I think a simple mind wipe serum is our best course."
    show old_tori 1
    anon f_surprised "{i}Mind wipe{/i}? That doesn't sound good..."
    show old_tori 2
    tori "Bah, it's perfectly safe! So long as you follow my directions to the letter!"
    tori "The only thing she'll forget is her aversion to my experiments."
    show old_tori 1
    anon f_worried "You're sure?"
    show old_tori 3
    tori "Well, there's no way to be entirely sure without proper testing..."
    show old_tori 4
    anon @ -m_talk "..."
    show old_tori 9
    tori "She'll be fine!"
    show old_tori 4
    anon "... What do you need me to do?"
    show old_tori 5
    tori "You'll start by gathering the ingredients we need."
    show old_tori 4
    anon "Ugh, alright. How many?"
    show old_tori 5
    tori "We'll need five in total."
    show old_tori 9
    with dissolve.nowait
    tori "I had prepared a list, but someone decided to take some artisic liberties..."
    show anon e_sw behind old_tori
    show old_tori 12 at center
    with dissolve
    tori "... So we'll have to make do with these blueprints instead."

    if saga.cast.anon in saga.sets.school_science:
        scene school_science base at stage(.6, .75, 15)
    else:
        scene school_office2 base at stage(.5, .9, 5)

    show plans_serum
    with fade
    pause
    anon "Falicum mushroom, horny toad extract, psychotropic euphorbia, base liquid..."

    if saga.cast.anon in saga.sets.school_science:
        call shot.school_science_door
        show anon a_pocket e_sw f_worried o_right at left
        show old_tori 13 at center
    else:
        call shot.school_office2_tori
        show anon a_pocket e_sw f_worried at right
        show old_tori 13 at face_right, center

    with fade
    anon "I've never even heard of these things before!"
    show anon a_plans e_ssw
    show old_tori 2 behind anon
    with dissolve
    tori "Well, falicum mushrooms grow in the forest here in Summerville."
    show old_tori 3
    show anon e_w
    tori "They are easy to spot because of their phallic shape."
    show old_tori 1
    anon f_disgusted "... Gross."
    show old_tori 2
    tori "The horny toad and psychotropic euphorbia can also be found in the forest."
    show old_tori 1
    anon f_confused "Psychotropic what?"
    show old_tori 2
    tori "It's a luminescent flower... You might know it as the \"forget-me-not\" blossom."
    show old_tori 1
    anon f_worried "Nope, never heard of it."
    show old_tori 3
    tori "Really?"
    show old_tori 2
    tori "You'll only find it in dark places. Your best bet would be a cave."
    show old_tori 1
    anon f_surprised "There are caves in Summerville?"
    show old_tori 3
    tori "Of course."
    show anon f_worried
    show old_tori 2
    tori "As for the horny toad, it's their breeding season. So look for a pond or stream."
    tori "They should be easily identifiable by their lumpy purple backsides."
    show old_tori 1
    anon "Okay, that's not too bad..."
    anon @ e_ssw "... But what about this base liquid?"
    anon "What is that?"
    show old_tori 2
    tori "We just need something mild to act as a base for the serum. Vegetable stock would work best."
    tori "You should be able to pick some up at Consum-R."
    show old_tori 1
    show anon e_ssw
    pause
    anon f_surprised "What about this last ingredient?"
    anon e_w "[saga.cast.ursula]'s DNA?!"
    anon f_confused "How the heck am I supposed to get that?!"
    show old_tori 3
    tori "... Yeah, that's gonna be the difficult one."
    show old_tori 2
    tori "A hair or saliva sample would work best."
    tori "I'm sure you'll figure something out..."
    show old_tori 1
    anon a_plans_give e_sw f_worried "Great..."
    anon a_backpack_01 e_s "Well, I guess I had better get started."
    show old_tori 2
    tori "Come talk to me if you need help finding any of the ingredients."
    show anon a_side e_w
    show old_tori 5
    tori "... And hurry up! We gotta get this done before [saga.cast.ursula] changes the code to my office again!"
    hide anon with dissolve
    return


label tor05_take:
    return


label tor05_take.annie1:
    call shot.school_office1_door
    show old_annie 1 at old_right
    show old_anon 10 at old_left with dissolve
    anon "[saga.cast.annie], what are you doing here?"
    show old_anon 11
    show old_annie 3
    annie "I'm guarding [saga.cast.ursula]'s office while she's away."
    show old_anon 10
    show old_annie 1
    anon "... Why?"
    show old_anon 11
    show old_annie 3
    annie "Umm, because she asked me too? Duh."
    show old_annie 1
    anon "..."
    show old_annie 3
    annie "She said someone keeps sneaking in and going through her stuff."
    show old_annie 5
    annie "You wouldn't happen to know anything about that, would you?!"
    show old_anon 10
    show old_annie 6
    anon "M-me? No, I don't know anything about that!"
    show old_anon 11
    show old_annie 5
    annie "Uh huh..."
    show old_annie 3
    annie "Well, whoever it is, they aren't getting past {i}me{/i}!"
    show old_anon 10
    anon "Okay, well, good luck with that..."
    hide old_anon with dissolve

    scene school_hall3 at stage with fade
    show old_anon 4 with dissolve
    anon "( I have to figure out into that office... )"
    show old_anon 34
    anon "( Perhaps I can trick her somehow? )"
    hide old_anon with dissolve
    return


label tor05_take.annie2:
    call shot.school_office1_door
    show old_annie 3 at old_right
    show old_anon 11 at pos(.4), face_right with dissolve
    annie "Nobody is getting past me, [saga.cast.anon]!"
    show old_annie 1

    if saga.cast.anon.chr < 7:
        jump tor05_take.fail

    show old_anon 2
    anon "I just overheard your thief bragging downstairs near the boys' locker room..."
    show old_anon 1
    show old_annie 3
    annie "What? Really?!"
    show old_annie 1
    show old_anon 2
    anon "Yup and if you hurry you might still catch him..."
    show old_anon 1
    show old_annie 3
    annie "[saga.cast.ursula] will definitely reward me for that!"
    annie "Would you mind watching this door for me?"
    show old_annie 1
    show old_anon 2
    anon "Not at all. Go get him!"
    show old_anon 1 behind old_annie at face_left
    show old_annie 16 at pos(.2)
    with dissolve.nowait
    annie "Ahahahahaah!"
    hide old_annie
    with dissolve.nowait
    show old_anon 1
    anon "( Well, that should keep her busy for a while... )"
    anon "( Now to search the office for something with [saga.cast.ursula]'s DNA on it. )"
    hide old_anon with dissolve
    return True


label tor05_take.brook:
    scene forest_brook at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( Wow, this place is beautiful! )"
    anon @ -m_talk "( ... And it looks like the perfect spot to look for that horny toad [saga.cast.tori] wants. )"
    show anon a_salute e_sw
    pause
    show anon a_tired f_confused p_bend at left
    pause
    show anon a_side f_grumpy -p_bend
    pause
    show anon o_right

    if saga.prop.misc_toad.hide:
        anon a_pocket e_w f_worried @ -m_talk "( Can't see one at the moment though, perhaps I should try again later. )"
    else:

        pause
        show anon a_surprised f_surprised
        pause
        anon a_finger f_confused p_bend @ -m_talk "( Hah! What do you know, there's one right here! )"

    hide anon with dissolve
    return


label tor05_take.fail:
    show old_anon 10
    anon "O-okay..."
    anon "... I was just looking for [saga.cast.ursula]."
    show old_anon 11
    show old_annie 3
    annie "Yeah, well, she isn't here."
    show old_annie 4
    annie "So beat it!"
    show old_annie 1
    show old_anon 12
    anon "Alright, sheesh! You don't have to get your panties in a bunch!"
    hide old_anon with dissolve
    return


label tor05_take.flower:
    scene cave_nest at stage
    show old_anon 558 with dissolve
    anon "( It's... glowing! )"
    anon "( I need to get this back to [saga.cast.tori]. )"
    hide old_anon with dissolve
    return


label tor05_take.glade:
    scene forest_glade at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( Alright, so the mushroom should be here somewhere. )"
    anon @ -m_talk "( ... And she said to look for the toad near water and the flower in a cave. )"
    hide anon with dissolve
    return


label tor05_take.hall3:
    scene school_hall3 at stage
    show anon a_pocket f_worried with dissolve
    anon @ -m_talk "( Hmm, I need to get into [saga.cast.ursula]'s office again to look for some kind of DNA sample... )"
    anon @ -m_talk "( I should go in when she's not there. )"
    hide anon with dissolve
    return


label tor05_take.nest:
    scene cave_nest at stage
    show anon a_pocket f_worried o_right with dissolve
    anon @ -m_talk "( Hmm, it looks like something is nesting in here! )"
    anon @ -m_talk "( I'd better grab that flower and get out before whatever it is comes home. )"
    hide anon with dissolve
    return


label tor05_take.rails:
    scene school_office1 at stage
    show anon a_pocket f_worried o_right at left with dissolve
    anon @ -m_talk "( I can't leave without that DNA, who knows when I'll get another shot... )"
    hide anon with dissolve
    return


label tor05_take.shroom:
    scene cave_passage at stage

    if saga.camera.last is saga.sets.forest_brook:
        show old_anon 497 at face_right with dissolve
    else:
        show old_anon 497 with dissolve

    anon "( Well, it certainly {i}is{/i} phallic. )"
    hide old_anon with dissolve
    return


label tor05_take.tissue:
    scene school_office1 at stage
    show old_anon 528 with dissolve
    pause
    show old_anon 529
    anon "Ugh, oh man..."
    anon "Gross!"
    show old_anon 528
    pause
    anon "( I think this will work... )"

    if saga.cast.annie.plan[0] == 'tor05':
        anon "( I'd better get outta here before [saga.cast.annie] comes back. )"

    hide old_anon with dissolve
    return


label tor05_take.toad:
    scene forest_brook at stage
    show old_anon 531b with dissolve
    anon "Yup, I was right."
    anon "That is one ugly frog!"
    hide old_anon with dissolve
    return


label tor05_take.tori(pool):
    anon f_worried "About those items you needed..."

    menu tor05_take.help:
        "Mushroom." if saga.prop.food_shroom_x2 in pool:
            anon "What was it you said about the mushroom?"
            show old_tori 2
            tori "Falicum mushrooms grow in the forest here in Summerville."
            tori "They like shaded areas with a little moisture..."
            show old_tori 3
            tori "... And are easy to spot because of their phallic shape."
            show old_tori 1
            anon @ f_disgusted "... Gross."
            jump tor05_take.help

        "Horny toad." if saga.prop.misc_toad in pool:
            anon "I can't find a toad anywhere!"
            show old_tori 2
            tori "It's breeding season for the horny toad. So look for a pond or stream."
            tori "They should be easily identifiable by their lumpy purple backsides."
            show old_tori 1
            anon "Sounds like one ugly frog..."
            jump tor05_take.help

        "Flower." if saga.prop.flower_cave in pool:
            anon "Where did you say the flower liked to grow?"
            show old_tori 2
            tori "The psychotropic euphorbia is a luminescent flower that grows only in dark places."
            tori "Your best bet would be a cave, the deeper the better."
            show old_tori 1
            anon @ a_think e_nw f_pensive "Hmm, a cave..."
            jump tor05_take.help

        "Base liquid." if saga.prop.food_stock in pool:
            anon "Why do we need a base liquid?"
            show old_tori 2
            tori "Something has to act as a base for the serum. Vegetable stock would work best."
            tori "You should be able to pick some up at Consum-R."
            show old_tori 1
            anon "... At least one of the ingredients is simple."
            jump tor05_take.help

        "[saga.cast.ursula]'s DNA." if saga.prop.misc_tissue in pool:
            anon "How on Earth am I going to get [saga.cast.ursula]'s DNA?"
            show old_tori 2
            tori "A hair or saliva sample would work best."
            show old_tori 1
            anon "Yeah, okay, but how am I supposed to {i}get{/i} that?"
            show old_tori 9
            tori "... I'm sure you'll think of something."
            show old_tori 4
            anon @ e_osw f_sad -m_talk "..."
            jump tor05_take.help
        "That's all.":

            pass

    anon "I'll get back to collecting those items then."
    hide anon with dissolve
    return


label tor05_take.vee:
    show old_anon 2
    anon "I'm looking for vegetable stock. Do you guys have any?"
    show old_anon 1
    vee f_calm "I'm afraid we're all sold out at the moment."
    show old_anon 10
    anon "Oh man..."
    show old_anon 11
    vee "Would chicken stock work? We have plenty of that."
    show old_anon 10
    anon "I don't know..."
    anon "Is there a delivery coming soon or something?"
    show old_anon 11
    vee "We get deliveries daily but I have no idea when that particular item will be restocked."
    show old_anon 10
    anon "Crap..."
    anon "Alright, thank you."
    hide old_anon with dissolve

    scene store_aisle at stage(.7, .525, 2) with fade
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( Hmm, I guess chicken stock will have to do. )"

    if saga.prop.food_stock not in saga.cast.anon:
        anon a_side e_w f_calm @ -m_talk "( I should buy some and take it to [saga.cast.tori]. )"

    hide anon with dissolve
    return


label tor05_tori1(when):
    anon "I think I've got everything."
    show old_tori 3
    tori "... You think?"
    show old_tori 1
    anon a_backpack e_s f_worried "Well, there is one little issue..."
    show anon a_stock e_w
    show old_tori 94
    pause
    show old_tori 95
    tori "... Is that chicken stock?"
    show old_tori 1
    anon "Yeah. It's all Consum-R had..."
    anon @ f_confused "I thought, maybe chicken stock would still work?"
    show old_tori 2b
    tori "Hah, yeah. That should be fine..."
    show old_tori 6
    anon a_pocket @ -m_talk "..."
    show old_tori 7
    tori "Looks like everything else is in order."

    if when == 0:
        tori "Meet me in my office this evening, and we'll start mixing."
    elif when == 1:
        tori "Meet me in my office tomorrow evening, and we'll start mixing."
    else:
        tori "Meet me in my office on [saga.time.dow + when] evening, and we'll start mixing."

    show old_tori 6

    if when == 0:
        anon "Tonight?"
    elif when == 1:
        anon "Tomorrow?"
    else:
        anon "[saga.time.dow + when]?"

    show old_tori 3
    tori "Problem?"
    show old_tori 4
    anon "No! ... No. I'll see you then."
    hide anon with dissolve
    return


label tor05_pause1:
    return


label tor05_pause1.tori(when=when):
    anon f_worried "So, we have everything we need to make your serum?"
    label tor05_pause1.merge:
    show old_tori 5
    tori "... Uhh, yeah. Isn't that what I already told you?!"

    if when == 0:
        tori "Meet me in my office this evening, and we'll work on it."
    elif when == 1:
        tori "Meet me in my office tomorrow evening, and we'll work on it."
    else:
        tori "Meet me in my office on [saga.time.dow + when] evening, and we'll work on it."

    show old_tori 4
    anon "... O-okay."
    hide anon with dissolve
    return


label tor05_delay1:
    scene camera at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( It's time for my work with [saga.cast.tori]. )"

    if saga.cast.anon in saga.sets.school_office2:
        anon o_right @ -m_talk "( She should be here any minute. )"
        pause
        anon e_osw f_sad @ -m_talk "( Probably won't even notice I got here early... )"
    else:

        anon @ -m_talk "( She'll be waiting for me in her office. )"

    hide anon with dissolve
    return


label tor05_delay1.tori(when):
    jump tor05_pause1.tori


label tor05_office2(when):
    call shot.school_office2_entry
    show old_anon 2 with dissolve
    anon "[saga.cast.tori]?"
    show old_anon 1
    show old_tori 1 at old_left
    with dissolve
    show old_tori 2
    tori "You ready to get started?"
    show old_tori 1
    show old_anon 2
    anon "As ready as I'll ever be."
    show old_anon 11
    anon "..."
    show old_anon 10
    anon "... Wait a second, why are you set up to make two serums?"
    show old_anon 11
    show old_tori 2
    tori "I'm afraid I haven't been completely honest with you, [saga.cast.anon]."
    show old_tori 1
    anon "..."
    show old_tori 2
    tori "You've actually been collecting ingredients for two separate serums..."
    show old_anon 10
    show old_tori 1
    anon "Separate?! What's the second one for?"
    show old_anon 11
    show old_tori 2
    tori "... It's for me."
    show old_anon 10
    show old_tori 1
    anon "Huh?"
    show old_anon 11
    show old_tori 7
    tori "... The other day. With the Okitatron Belt in class..."
    show old_anon 10
    show old_tori 6
    anon "I said I was sorry for that!"
    show old_anon 11
    show old_tori 2
    tori "Calm down, [saga.cast.anon]. It didn't upset me."
    show old_anon 11 at face_right
    show old_tori 10c at right
    with dissolve.nowait
    tori "In fact, it intrigued me!"
    show old_anon 10
    show old_tori 10b
    anon "What?"
    show old_anon 11
    show old_tori 10c
    tori "You see, I've never felt anything like that before..."
    show old_anon 10
    show old_tori 10b
    anon "You mean you've never..."
    show old_anon 11
    show old_tori 10c
    tori "... Orgasmed."
    show old_anon 10
    show old_tori 10b
    anon "Like, never? How is that possible?"
    show old_anon 11
    tori "..."
    show old_tori 3 at face_left
    with dissolve
    label tor05_office2.cookie hide:
    tori "I'm asexual."
    show old_anon 10
    show old_tori 4
    anon "I don't know what that is..."
    show old_anon 11
    show old_tori 9
    tori "It means I don't have a sex drive."
    show old_anon 10
    show old_tori 4
    anon "... Well, how did that happen?"
    show old_anon 11
    show old_tori 8
    tori "..."
    show old_tori 9
    tori "{i}*Sigh*{/i} I was born that way, dummy."
    show old_anon 10
    show old_tori 4
    anon "... Oh. S-sorry."
    show old_anon 11
    show old_tori 5
    tori "It's alright. I've never given it much thought to be honest."
    show old_tori 7
    tori "... But the other day."
    tori "I can't stop thinking about those sensations..."
    tori "... And I wanna experience more!"
    show old_anon 10
    show old_tori 6
    anon "So, the second serum?"
    show old_anon 11
    show old_tori 7
    tori "I designed it to simulate a sex drive."
    show old_anon 10
    show old_tori 6
    anon "You can do that?"
    show old_anon 11
    show old_tori 7
    tori "Of course."
    tori "We're still missing one last ingredient though..."
    show old_anon 10
    show old_tori 6
    anon "Seriously?! Why didn't you have me get it earlier, when I was fetching everyth-"
    hide old_anon
    show old_tori 65 at pos(.65)
    with dissolve.nowait
    tori "It's already here, [saga.cast.anon]."

    scene school_office2_chair
    pause .1
    show old_tori 67 as old_anon
    anon "... Oh!!" with vpunch
    show old_tori 66 as old_anon
    show old_tori 7 behind old_anon at old_right
    with dissolve
    tori "I just need a sample."
    show old_tori 67 as old_anon
    show old_tori 6
    anon "A sample of what?"
    show old_tori 66 as old_anon
    show old_tori 7
    tori "Your semen."
    show old_tori 67 as old_anon
    show old_tori 6
    anon "WHAT?!" with hpunch
    anon "You want my semen?!"
    show old_tori 66 as old_anon
    tori "Mmhmm."
    show old_tori 67 as old_anon
    anon "... Why?"
    show old_tori 66 as old_anon
    show old_tori 7
    tori "I theorize that your semen will be the key ingredient in my serum."
    tori "You see, you show characteristics of having an overactive sex drive."
    show old_tori 67 as old_anon
    show old_tori 6
    anon "I do?"
    show old_tori 66 as old_anon
    show old_tori 7
    tori "Hence, the impressive size of your sexual organ. I imagine a few of your family members might display similar characteristics..."
    show old_tori 67 as old_anon
    show old_tori 6
    anon "Hmm, you think it's because I have an overactive sex drive?"
    show old_tori 66 as old_anon
    show old_tori 47 with dissolve
    tori "Mmmhmm."
    show old_tori 67 as old_anon
    anon "I just figured it was good genes..."
    show old_tori 66 as old_anon
    show old_tori 48 with dissolve
    tori "Do any of your male relatives possess a similar sized reproductive organ?"
    show old_tori 67 as old_anon
    show old_tori 49
    anon "How should I know?!"
    show old_tori 66 as old_anon
    show old_tori 48
    tori "Well, I'm going to assume my theory is correct then, and proceed as planned."
    show old_tori 67 as old_anon
    show old_tori 49
    anon "So how is this going to work then?"
    show old_tori 66 as old_anon
    show old_tori 48
    tori "Let's see it."
    show old_tori 67 as old_anon
    show old_tori 49
    anon "I dunno about this..."
    show old_tori 66 as old_anon
    show old_tori 48
    tori "Come now, [saga.cast.anon]. This could change my life in a profound and meaningful way."
    tori "Would you truly deny me that, just to save yourself a bit of embarrassment?"
    show old_tori 49
    anon "..."
    show old_tori 67 as old_anon
    anon "{i}*Sigh*{/i} No, I guess not."
    show old_tori 68 as old_anon with dissolve
    pause
    show old_tori 69 as old_anon with dissolve
    pause
    show old_tori 70 as old_anon with dissolve
    anon "..."
    show old_tori 48
    tori "It really is quite impressive, [saga.cast.anon]."
    show old_tori 71 as old_anon
    show old_tori 49
    anon "T-thanks."
    show old_tori 70 as old_anon
    show old_tori 48
    tori "Now, I want you to just lay back and relax while I perform the procedure."
    show old_tori 71 as old_anon
    show old_tori 49
    anon "... Procedure?"
    show old_tori 70 as old_anon
    show old_tori 48
    tori "Shh. No talking, please."
    tori "I need to concentrate."
    hide old_anon
    show old_tori 52_53 slow at center
    with dissolve
    anon "Oh, my..."
    pause 4
    tori "Am I doing this correctly?"
    anon "Y-yeah..."
    pause 6
    tori "... And this feels good?"
    anon "Mmmhmm..."
    pause 3
    tori "Is it going to result in climax?"
    anon "Uhh."
    anon "You'll have to speed up if you want me to cum..."
    tori "Oh, really?"
    show old_tori 52_53 norm
    tori "I had no idea the pace mattered..."
    pause 6
    tori "Is this better?"
    anon "Oh yeah!"
    pause 4
    tori "Are you getting close?"
    anon "I think so."
    jump tor05_office2.loop


label tor05_office2.cum:
    tori "This is all so fascinating!"
    anon "Oh! I'm gonna!"
    anon "I'm gonna!"
    show old_tori 54
    anon "Hnnngg!!" with hpunch
    show old_tori 55
    with dissolve
    pause

    call shot.school_office2_lab
    show old_tori 87
    with fade
    tori "I'm sure you don't comprehend just how exciting this is."
    show old_anon 27 at old_right with dissolve
    tori "What I hold in my hand could be the key to unlocking experiences I've never even dared to dream of."
    show old_anon 26
    show old_tori 88
    anon "Uh huh..."
    show old_tori 87
    show old_anon 25
    tori "You should begin mixing immediately!"
    $ renpy.end_replay()
    show old_anon 24
    show old_tori 88
    anon "Haaah... Haaah..."
    show old_anon 26
    anon "Yeah, okay. Sure."
    anon "Just gimme a second to catch my breath..."
    show old_anon 24
    show old_tori 4 at face_right
    with dissolve.nowait
    anon "Whew!"
    show old_anon 26
    anon "That was amazing."
    show old_anon 1
    show old_tori 5
    tori "Yes, I'm sure it was."
    show old_tori 3
    tori "Can we begin now please?"
    show old_tori 4
    show old_anon 10
    anon "Alright, how do I do this?"
    show old_anon 11
    label tor05_office2.merge:
    show old_tori 7
    tori "It's very simple. The pink serum is for me and the blue is for [saga.cast.ursula]."
    tori "That means the pink serum needs the falicum mushroom, horny toad extract, and your... {i}*ahem*{/i} contribution..."
    show old_tori 6
    anon "..."
    show old_tori 7
    tori "... And the blue serum will require the base liquid, psychotropic euphorbia, and [saga.cast.ursula]'s DNA."
    tori "Do you think you can handle that?"
    show old_tori 6

    menu:
        "Yes.":
            pass
        "Could you repeat that?":

            anon "Um..."
            show old_tori 9
            tori "Unbelievable."
            jump tor05_office2.merge

    show old_anon 2
    anon "Yeah, let's do this."

    call mini.serum

    if not _return:
        jump tor05_office2.fail

    call shot.school_office2_lab
    show old_anon 2 at face_right
    with fade
    anon "I think I did it!"
    show old_anon 1
    show old_tori 5 at old_right
    with dissolve.nowait
    tori "Let me see!"
    show old_tori 35
    tori "..."
    show old_tori 34
    tori "It looks correct!"
    tori "Oh, this is so exciting!"
    show old_anon 2
    anon "Thanks, I-"
    show old_tori 36 at pos(.8) with dissolve
    show old_anon 23
    anon "( !!! )" with hpunch
    show old_anon 10
    anon "Wow, you're just gonna... Okay."
    show old_tori 37 at right
    tori "Hmmph!"
    show old_tori 38
    tori "That actually tastes pretty good!"
    show old_anon 10
    show old_tori 6
    anon "... That had my..."
    show old_anon 11
    anon "..."
    show old_anon 10
    anon "So, is that it? Are we done?"
    show old_anon 11
    show old_tori 7
    tori "Almost!"
    tori "Just one last thing to do."
    show old_tori 28
    anon "..."
    show old_tori 29
    tori "You just need to make sure [saga.cast.ursula] ingests this."
    show old_anon 10
    show old_tori 30
    anon "What?!"
    anon "How am I supposed to do that?"
    show old_anon 11
    show old_tori 29
    tori "You'll come up with something..."
    show old_tori 5
    show old_anon 535
    with dissolve.nowait
    tori "You always do."
    show old_tori 4
    show old_anon 534
    anon "Wonderful..."
    show old_anon 535
    show old_tori 3
    tori "Just slip it into her food or something."
    show old_tori 4
    show old_anon 10
    anon "Then I get my A?"
    show old_anon 11
    hide old_tori with dissolve
    tori "Hmm, we'll discuss it."
    show old_anon 1
    with dissolve.nowait
    anon "( Alright, I can do this. )"
    hide old_anon with dissolve
    return True


label tor05_office2.dialogue(opt, rng=-1):
    if opt == 1:
        anon "Oh, god!"
    elif opt == 2:
        anon "I can't-"

    pause
    return


label tor05_office2.fail:
    call shot.school_office2_lab
    show old_anon 11
    show old_anon labcoat 1 as anon_labcoat
    show old_anon labcoat 1b as anon_specs
    with fade
    show old_tori 11 at old_right
    with dissolve.nowait
    tori "No, no, NO!"
    show old_anon 11 at face_right
    show old_anon labcoat 1 as anon_labcoat at face_right
    show old_anon labcoat 1b as anon_specs at face_right
    with dissolve.nowait
    tori "How do you always manage to screw these things up?!"
    show old_anon 10
    show old_tori 11b
    anon "Sorry, I got confused..."
    show old_anon 11
    show old_tori 9
    tori "Ugh..."
    show old_tori 11
    tori "Well, we don't have time to start over today. You'll have to come back."
    show old_tori 11b
    show old_anon 10
    anon "O-okay."
    anon "I guess I'll see you tomorrow evening then?"
    show old_anon 11

    if when > 1:
        show old_tori 10
        pause
        show old_tori 95
        tori "No.... That won't work..."
        show old_tori 11
        tori "Come back on [saga.time.dow + when] evening."

    show old_tori 11
    tori "Try not to fail me next time!"
    hide old_anon
    hide anon_labcoat
    hide anon_specs
    with dissolve
    return


label tor05_office2.hall1:
    scene school_hall1 at stage
    show anon a_pocket f_confused at right with dissolve
    anon @ -m_talk "( Hmm, I guess [saga.cast.tori] must have left the door unlocked so we could complete our work. )"
    anon f_happy @ -m_talk "( Nice! )"
    hide anon with dissolve
    return


label tor05_office2.loop:
    menu(range=('norm', 's300', 's250'), screen='old_lewd', tag='old_tori'):
        "Keep Going":
            pass
        "Cum":

            jump tor05_office2.cum

    $ renpy.dynamic(pool=saga.lewd.pool(2, max=1))

    while pool:
        call tor05_office2.dialogue (pool.pop(), rng=renpy.random.random()) from tor05_office2.pool

    jump tor05_office2.loop


label tor05_office2.rails:
    scene camera at stage
    show anon a_pocket f_shy at right with dissolve

    if saga.cast.anon in saga.sets.school_office2:
        anon @ -m_talk "( I can't believe she didn't notice me at all... )"
        anon @ -m_talk "( ... Classic [saga.cast.tori]. )"
    else:

        anon @ -m_talk "( I should hurry up to [saga.cast.tori]'s office. )"
        anon @ -m_talk "( Don't wanna keep her waiting. )"

    hide anon with dissolve
    return


label tor05_pause2:
    return


label tor05_pause2.tori(when=when):
    anon f_worried "So, we need to try again to make your serum?"
    jump tor05_pause1.merge


label tor05_delay2:
    scene camera at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( It's time to try making that serum again for [saga.cast.tori]. )"

    if saga.cast.anon in saga.sets.school_office2:
        anon f_worried o_right @ -m_talk "( Just as well that I got here early, don't want to give her any more reasons to flunk me! )"
    else:
        anon a_surprised f_surprised m_teeth @ -m_talk "( Better get to her office quickly, don't want to give her any more reasons to flunk me! )"

    hide anon with dissolve
    return


label tor05_delay2.tori(when):
    jump tor05_pause2.tori


label tor05_retry(when):
    call shot.school_office2_entry
    show old_anon 2 with dissolve
    anon "[saga.cast.tori]?"
    show old_anon 1
    show old_tori 3 at old_left
    with dissolve.nowait
    tori "Ready to try again?"
    show old_tori 6
    show old_anon 2
    anon "Yeah, I'll get it this time for sure!"
    jump tor05_office2.merge


label tor05_retry.hall1:
    scene school_hall1 at stage
    show anon a_pocket at right with dissolve
    anon @ -m_talk "( [saga.cast.tori] left the door unlocked for me again. )"
    anon f_happy @ -m_talk "( Sweet! )"
    hide anon with dissolve
    return


label tor05_retry.rails:
    scene camera at stage
    show anon a_pocket f_shy at right with dissolve

    if saga.cast.anon in saga.sets.school_office2:
        anon @ -m_talk "( [saga.cast.tori] didn't seem to notice me waiting here at all... )"
        anon @ -m_talk "( ... I guess I should let her know I'm here. )"
    else:

        anon @ -m_talk "( [saga.cast.tori] will be waiting in her office. )"
        anon @ -m_talk "( Best get it right this time! )"

    hide anon with dissolve
    return


label tor05_coffee:
    scene mono school_lounge_coffee
    mono "This seemed like the best course of action." with fade
    mono "I knew [saga.cast.ursula] drank coffee from this pot every afternoon."
    mono "And since it was synthesized using her DNA, it shouldn't affect anybody else."
    mono "At least, that's what I hoped."

    call shot.school_lounge_coffee
    show anon a_pocket f_smug
    with fade
    anon @ -m_talk "( Job done! )"
    anon f_worried @ -m_talk "( I should get out of here before anyone catches me... )"
    anon @ -m_talk "( ... And let [saga.cast.tori] know it's done. Who even knows what happens next... )"
    hide anon with dissolve
    return


label tor05_coffee.busy:
    call shot.school_lounge_coffee
    show anon e_nw f_confused with dissolve
    pa "Any students currently attempting to take advantage of staff-only facilities {i}will{/i} be brought to justice."
    anon a_surprised_shrug e_w f_surprised m_teeth @ -m_talk "( Shit! Shit! They know! )" with hpunch
    hide anon
    show old_anon 669 at left
    with dissolvefast.nowait
    anon "( Abort mission! )"
    hide old_anon with dissolve

    scene school_hall2 at stage
    with fade
    show anon a_tired f_worried m_talk p_bend with dissolve
    anon "Haah... haah..."
    anon "( How could they know?! )"
    pause
    anon "( I'll have to try again later. )"
    hide anon with dissolve
    return


label tor05_coffee.hall2:
    scene school_hall2 at stage
    show anon a_pocket e_nw f_pensive with dissolve
    anon @ -m_talk "( Hmm, I think [saga.cast.ursula] goes into the teachers' lounge to drink coffee in the afternoons. )"
    hide anon with dissolve
    return


label tor05_coffee.late:
    call shot.school_lounge_coffee
    show anon a_think e_sw f_pensive with dissolve
    anon @ -m_talk "( No point dosing the coffee this late in the day. )"
    anon @ -m_talk "( I'm sure they'll brew a fresh pot tomorrow morning. )"
    hide anon with dissolve
    return


label tor05_coffee.lounge:
    scene school_lounge at stage
    show anon a_pocket f_worried_surprised with dissolve
    anon @ -m_talk "( There she is! Drinking coffee just like I thought. )"
    anon @ -m_talk "( I just need to dose the coffee pot! )"
    hide anon with dissolve
    return


label tor05_coffee.near:
    call shot.school_lounge_coffee
    show anon a_pocket f_worried_surprised o_right with dissolve
    anon @ -m_talk "( I can't do it while she's sitting there... )"
    hide anon with dissolve
    return


label tor05_coffee.soon:
    call shot.school_lounge_coffee
    show anon a_pocket e_sw f_disgusted with dissolve
    anon @ -m_talk "( Eugh, someone forgot to toss out the coffee before the weekend. )"
    anon @ -m_talk "( I should wait for them to brew a fresh pot on monday. )"
    hide anon with dissolve
    return


label tor05_coffee.tori:
    anon f_worried "Are you sure this serum-"
    show anon f_worried_surprised
    show old_tori 5
    tori "You still haven't dosed [saga.cast.ursula]?!"
    show old_tori 4
    anon f_sad @ -m_talk "..."
    show old_tori 5
    tori "What are you waiting for?"
    show old_tori 4
    anon f_worried "This isn't exactly easy you know!"
    anon "Can't you give me some advice or something?!"
    show old_tori 3
    tori "Here's some advice: hurry up and do it already!"
    show old_tori 5
    tori "All you have to do is slip it into her food or something."
    show old_tori 4
    anon "Alright, alright. I'll be back."
    hide anon with dissolve
    return


label tor05_reset:
    return


label tor05_reset.coffee:
    call shot.school_lounge_coffee
    show anon e_sw f_worried_surprised with dissolve
    pause
    show anon a_reach
    pa "Students are strongly discourged from consuming caffeinated beverages during school hours."
    anon a_surprised_shrug e_w f_surprised @ m_teeth "!!!" with hpunch
    show anon a_surprised_up f_worried_surprised o_right with dissolvefast
    pause
    show anon -o_right with dissolvefast
    pause
    hide anon
    show old_anon 669 at left
    with dissolvefast.nowait
    anon "( Nope! )"
    hide old_anon with dissolve

    scene school_hall2 at stage
    with fade
    show anon a_tired f_worried m_talk p_bend with dissolve
    anon "Haah... haah..."
    anon "( There's no way. )"
    hide anon with dissolve
    return


label tor05_tori2:
    call shot.school_science_door
    show old_tori 6 at right
    show anon a_pocket o_right at left
    anon "Alright, [saga.cast.tori]. It's done."
    show old_tori 7
    tori "Wonderful!"
    tori "Now we just wait to see the effects..."
    show old_tori 6
    anon "How long should it take?"
    show old_tori 7
    tori "It'll work fast. Why don't you stick around, and we'll check on her after class?"
    show old_tori 6
    anon "Sure."
    pause 1

    scene black
    with dissolve
    mono ""

    scene school_lounge -melody -ursula at stage
    show old_ursula 33 at right, face_right
    with fade
    show old_tori 5 at pos(.45), face_right
    show anon a_pocket f_worried o_right at pos(.15)
    with dissolve
    tori "{i}*Ahem*{/i}"
    show old_tori 4
    show old_ursula 32 at face_left
    with dissolve
    ursula "Hmm? Oh, hello there [saga.cast.tori.name]..."
    ursula "How's little Miss Know-it-all today?"
    show old_ursula 31
    tori "... Hmmph."
    show old_tori 3
    tori "I was just checking on the status of my office?"
    show old_tori 4
    show old_ursula 32
    ursula "Your office?"
    show old_tori 5
    show old_ursula 31
    tori "Well, the other day you seemed pretty adamant about changing the locks."
    show old_tori 4
    show old_ursula 32
    ursula "Was I?"
    ursula "That's funny... I don't recall."
    show old_tori 3
    show old_ursula 31
    tori "Oh, really?"
    ursula "..."
    show old_ursula 30b with dissolve
    ursula "Bawk bawk."
    show old_ursula 31 with dissolve
    show old_tori 8
    tori "..."
    show old_tori 3
    tori "... Are you alright?"
    show old_tori 4
    show old_ursula 32
    ursula "... Huh?"
    ursula "I'm fine, why?"
    show old_tori 5
    show old_ursula 31
    tori "You were saying something, regarding the lock on my office?"
    show old_tori 4
    show old_ursula 32
    ursula "Was I?"
    ursula "That's funny... I don't-"
    show old_ursula 30b with dissolve
    ursula "BAWK!!! Bawk bawk bawk..."
    show old_ursula 31 with dissolve
    show old_tori 6
    anon "Uhh..."
    show old_tori 9
    tori "Shh!"
    show old_ursula 33 with dissolve
    tori "Don't interrupt us [saga.cast.anon]."
    show old_tori 4
    show old_ursula 32 with dissolve
    ursula "... This coffee tastes funny."
    show old_ursula 31
    anon @ -m_talk "..."
    show old_tori 7
    tori "Did I tell you about the new invention I was working on?"
    show old_tori 6
    show old_ursula 32
    ursula "Invention?"
    ursula "No, I don't think yo-"
    show old_ursula 30b with dissolve
    ursula "Bawk bawk..."
    ursula "Bawk bawk BAWK!!"
    show old_ursula 31 with dissolve
    show old_tori 7
    tori "I'll have to bring it by your office sometime. It's really fascinating!"
    show old_ursula 32
    show old_tori 6
    ursula "Sure, okay!"
    show old_tori 7
    show old_ursula 31
    tori "Oh my, look at the time."
    tori "We should really be going."
    show old_tori 7 at center with dissolve
    tori "Come along, [saga.cast.anon]."
    hide old_tori with dissolve
    anon @ -m_talk "..."
    show old_ursula 32
    hide anon with dissolve
    ursula "... This coffee tastes funny."

    call shot.school_science_door
    show old_tori 7 at old_right
    show anon a_pocket f_worried o_right at left
    with fade
    tori "So, I guess that chicken stock created a bit of a side effect after all..."
    show old_tori 2b
    tori "Pffft, hahaha!!"
    show old_tori 6
    anon "How is this funny?!"
    anon "We screwed with her head, and she's in there clucking like a chicken!"
    show old_tori 2b
    tori "Yeah she is! Hahaha!"
    show old_tori 7
    tori "Oh, would you relax?"
    tori "It's only temporary."
    show old_tori 9
    tori "... I think."
    show old_tori 6
    anon f_surprised "You think?!"
    show old_tori 9
    tori "I mean, I'm pretty sure."
    show old_tori 7
    tori "Look the important thing here is that the serum worked!"
    tori "She's completely impartial to my experiments now!"
    tori "... And she didn't even remember wanting to lock me out of my office!"
    show old_tori 6
    anon f_worried "Yeah, but she's clucking like a chicken!"
    show old_tori 2b
    tori "Pffftt, hahahaaaah!"
    anon "Well, I'm glad you think it's so funny..."
    show old_tori 6
    anon "So, what now?"
    show old_tori 7
    tori "Now, I need some time to study the effects of the other serum."
    show old_tori 6
    anon "Oh, I completely forgot about the other serum!"
    anon "Are you feeling any different?"
    show old_tori 7
    tori "Mmm, maybe..."
    show old_tori 2b
    tori "Hehehe!"
    anon "You do seem kinda, different."
    show old_tori 7
    tori "How so?"
    show old_tori 6
    anon "You're like... Giddy."
    show old_tori 2b
    tori "Hehehe! I'm just happy."
    anon "It's kinda freaking me out to be honest."
    show old_tori 7
    tori "... And hot."
    show old_tori 3
    tori "Are you hot? It's hot in here!"
    show old_tori 6
    anon "No, I'm fine."
    show old_tori 7
    tori "Alright, well, I'm gonna head up to my office and get some work done."
    tori "Come see me in a few days."
    show old_tori 6
    anon "Umm, okay."
    show old_tori 2b
    tori "Byeee, [saga.cast.anon]!"
    tori "Hehehehe..."
    hide old_tori with dissolve
    anon "I hope she's gonna be okay..."
    hide old_anon with dissolve
    return


label tor05_tori2.rails:
    scene camera at stage
    show anon e_nw f_pensive with dissolve
    anon @ -m_talk "( I should inform [saga.cast.tori] that I've dosed [saga.cast.ursula]'s afternoon coffee. )"
    hide anon with dissolve
    return


label tor05_outro:
    return


label tor05_outro.block:
    call shot.school_office2_door
    show anon a_think f_worried with dissolve
    anon @ -m_talk "( She's been acting awful strange since she started taking that serum... )"
    anon a_pocket @ -m_talk "( ... Probably best I just leave her be. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
