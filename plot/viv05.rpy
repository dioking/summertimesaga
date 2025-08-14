label viv05_setup:
    return


label viv05_setup.roxxy:
    jump viv04_viv.roxxy


label viv05_setup.viv:
    anon f_shy "So about this exam..."
    viv f_worried "You said [saga.cast.roxxy] was to be showing up, yes?"
    anon f_worried "... I mean, she told me she would."
    viv "Hmm, then we can only hope she is not telling lies."
    anon @ -m_talk "..."
    hide anon with dissolve
    return


label viv05_french:
    call shot.school_french_front
    show old_viv 2
    viv "Take your seats, everyone. The test will begin shortly."
    show old_viv 1
    pause
    show old_viv 2
    viv "Alright, class."
    viv "Match the French word with the corresponding object on your test."
    show old_viv 1
    pause
    show old_viv 2
    viv "C'est plutôt facile, non?"
    viv "Let's begin!"

    call mini.french

    if not _return:
        jump viv05_french.fail

    scene mono school_french_cheat_roxxy
    mono "I breezed right through the test, making sure my paper was visible to [saga.cast.roxxy]." with fade
    more "She wasn't very subtle about copying me but [saga.cast.viv] didn't seem to notice."
    mono "I was excited to be done with French and claim my special reward from [saga.cast.viv]."

    scene black
    with dissolve
    mono ""

    call shot.school_french_viv
    show old_anon 5 at old_left
    show old_viv 3 at old_right
    with dissolve
    viv "Toutes mes félicitations, [saga.cast.anon]!"
    show old_viv 1
    show old_anon 38 with dissolve.nowait
    anon "I passed?!"
    show old_anon 13 with dissolve.nowait
    show old_viv 2
    viv "You got a perfect score!"
    show old_viv 1
    show old_anon 14
    anon "Awesome!"
    show old_anon 13
    show old_viv 2
    viv "I'd say you earned your A."
    show old_viv 1
    show old_anon 14
    anon "Thank you so much [saga.cast.viv]!"
    show old_anon 13
    show old_viv 12
    viv "My pleasure, [saga.cast.anon]!"
    show old_viv 25 at pos(.446) with dissolve.nowait
    viv "We should celebrate, yes?"
    show old_viv 27 with dissolve.nowait
    show old_anon 14
    anon "Sure, what did you have in mind?"
    show old_anon 13
    show old_viv 26 with dissolve.nowait
    viv "Hmm, why don't you join me in my office this afternoon?"
    show old_viv 16 with dissolve.nowait
    viv "Perhaps we could sample that French wine I told you about?"
    show old_viv 17
    show old_anon 26
    anon "O-okay. I've never had wine before."
    show old_anon 13
    show old_viv 26 with dissolve.nowait
    viv "Well then, you are in for a real treat, jeune homme!"
    show old_viv 27 with dissolve.nowait
    show old_anon 14
    anon "I'll see you later then."
    show old_anon 13
    show old_viv 12 with dissolve.nowait
    viv "Au revoir, [saga.cast.anon]."
    hide old_anon with dissolve
    return True


label viv05_french.fail:
    scene black
    with dissolve
    mono ""

    call shot.school_french_viv
    show old_anon 5 at old_left
    show old_viv 5 at old_right
    with dissolve
    viv "Oh no. [saga.cast.anon], I thought you were prepared for this?"
    show old_viv 4
    show old_anon 10
    anon "You mean I didn't pass?"
    show old_anon 5
    show old_viv 5
    viv "I'm afraid not..."
    show old_viv 4
    show old_anon 37 with dissolve
    anon "I'm so sorry, [saga.cast.viv]!"
    show old_anon 5 with dissolve
    show old_viv 5
    viv "You must come back another day and retake it."
    show old_viv 4
    show old_anon 12
    anon "Alright, I can do that!"
    show old_anon 5
    show old_viv 5
    viv "I suggest you study harder this time, yes?"
    show old_viv 4
    show old_anon 24
    anon "Yes, ma'am."
    hide old_anon with dissolve
    return


label viv05_office5:
    scene school_office5_desk
    show old_viv 29
    show old_anon 13 at old_left with dissolve
    viv "Ahh, [saga.cast.anon]! I was beginning to think you weren't coming!"
    show old_viv 28
    show old_anon 10
    anon "Did you start without me?"
    show old_anon 5
    show old_viv 29
    viv "{i}*Hic*{/i} Oui, mon bel homme!"
    viv "I just popped the cork on my second bottle."
    show old_viv 30 with dissolve
    viv "Let me pour yo- {i}*hic*{/i}"
    show old_viv 31 with dissolve
    viv "Ça me saoûle."
    show old_viv 33 with dissolve
    show old_anon 13
    viv "Ah you see {i}*hic*{/i} the French make the best wine!"
    show old_viv 32
    show old_anon 17
    anon "Hehe, if you say so."
    show old_anon 13
    show old_viv 33
    viv "Tsk! It's true!"
    viv "The best wine..."
    viv "And the best lovers..."
    show old_viv 32
    show old_anon 11
    anon "{i}*Gulp*{/i}"
    show old_viv 33
    viv "I still owe you a special reward, yes?"
    show old_viv 32
    show old_anon 26
    anon "Y-yeah..."
    show old_anon 13
    show old_viv 33
    viv "Well, it's waiting for you, over here..."
    viv "Why don't you come and unwrap it?"
    label viv05_office5.reuse:
    show old_anon 523 at face_right, center
    show old_viv 34
    with dissolve
    pause
    show old_anon 525
    show old_viv 35
    with dissolve
    pause
    show old_anon 524
    show old_viv 37
    with dissolve
    pause
    show old_anon 525
    show old_viv 38
    with dissolve
    pause

    if saga.cast.viv < 'sex':
        show old_viv 39
        viv "You like?"
        show old_viv 38
        show old_anon 526
        anon "I do."

    show old_anon 527
    anon "You're beautiful."
    show old_anon 525
    show old_viv 39
    viv "Don't be shy, kiss them."
    hide old_anon
    show old_viv 39b
    with dissolve
    viv "Mmm..."
    viv "Remember to use your tongue, [saga.cast.anon]."
    show old_viv 39b_39c_39d
    viv "Oh, mon bel homme..."
    viv "You are making- {i}*hic*{/i}"
    viv "You are making me melt with those kisses!"
    pause
    show old_anon 83c at pos(.4), face_right
    show old_viv 39
    with dissolve
    viv "I know you are hiding something large in those pants of yours..."
    viv "I show you mine. You show me yours, yes?"
    show old_viv 38
    show old_anon 83b
    anon "Sure!"
    show old_anon 261b with dissolve
    pause
    show old_anon 263c with dissolve
    show old_viv 39

    if saga.cast.viv < 'sex':
        viv "Oh mon dieu! Elle est magnifique!"
    else:
        viv "Oh mon dieu! C'est beau..."

    viv "Give it to me, [saga.cast.anon]!"

    if saga.cast.viv < 'sex':
        show old_viv 38
        show old_anon 262b
        anon "You mean... You want me to..."
        show old_anon 263c
        show old_viv 39
        viv "S'il te plaît!"
        viv "Your reward is just beginning."

    show old_viv 40 at pos(.65) with dissolve
    pause
    show old_viv 41 with dissolve
    pause
    show old_viv 42 with dissolve
    pause
    show old_viv 43 with dissolve
    show old_anon 263b

    if saga.cast.viv < 'sex':
        viv "I can't begin to describe how much I've been looking forward to this."

    pause
    show old_viv 44 with dissolve
    pause
    show old_viv 45 with dissolve
    pause
    show old_anon 263c
    show old_viv 46
    viv "You like my French body, yes?"
    show old_viv 45
    show old_anon 262b
    anon "Yes!"
    show old_anon 263c
    show old_viv 46
    viv "Excellent!"
    show old_viv 47 at center with dissolve
    show old_anon 263b
    pause
    show old_viv 48

    if saga.cast.viv < 'sex':
        viv "Come! Let me teach you about French lovemaking!"
        show old_viv 50 with dissolve
        viv "I'm ready for you."
    else:

        viv "Ah, ma chatte toute serrée a envie de ta grosse bite bien juteuse."
        show old_viv 47
        show old_anon 262b
        anon "What?"
        show old_anon 263c
        show old_viv 50
        with dissolve
        viv "I've been waiting for you."

    hide old_anon
    show old_viv 51
    with dissolve
    viv "Enter me, [saga.cast.anon]."
    show old_viv sex 1 with dissolve
    viv "Ohh, elle est si grosse!"
    viv "Aaaah!"
    show old_viv sex 1_2_3_4_5_6_7 fast
    pause
    call viv05_office5.dialogue (1)
    call viv05_office5.dialogue (2)

    if saga.cast.viv < 'sex':
        viv "I was wrong!"
        viv "No Frenchman ever fucked me like this!"

    jump viv05_office5.loop


label viv05_office5.cum:
    viv "Oh, oui!"
    viv "I'm going to cum, [saga.cast.anon]!"
    anon "Me too!"
    viv "Don't stop!"
    viv "Don't-"
    viv "AAAAAAAHHHHH!!!!"

    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 14_15 norm
    else:
        show old_viv 52_53 norm -sex

    anon "Hnnngg!!!" with flash

    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 16 with dissolve.nowait
        pause
        show old_viv sex chair 17 with dissolve.nowait
        pause
        show old_viv sex chair 18 with dissolve.nowait
    else:

        show old_viv 54 with dissolve.nowait

    viv "Haah... Haah..."

    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 1 with dissolve.nowait
    else:
        show old_viv 55 with dissolve.nowait

    viv "[saga.cast.anon]..."
    viv "That was magnificent!"

    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 2
    else:
        show old_viv 56

    anon "Haah... Yeah."

    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 1
    else:
        show old_viv 55

    viv "We must do this again, yes?"

    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 2
    else:
        show old_viv 56

    anon "Absolutely!"

    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 1
    else:
        show old_viv 55

    viv "Très bien, mon bel homme!"

    if 'chair' in renpy.get_attributes('old_viv'):
        viv "Now then, stay there."
    else:
        viv "Now then, have a seat."

    viv "I'll prepare you some fromage to go with your wine..."

    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 2
    else:
        show old_viv 56

    anon "Okay..."
    $ renpy.end_replay()

    scene black
    with dissolve
    mono ""

    scene school_office5_desk dusk
    show old_viv 46 at pos(.65)
    show old_anon 13 at old_left
    with dissolve

    if saga.cast.viv < 'sex':
        viv "So, you will return again another time?"
        show old_viv 45
        show old_anon 26
        anon "You bet I will!"
        show old_anon 403
        show old_viv 46
        viv "I cannot wait!"
        show old_viv 45
        show old_anon 36 with dissolve.nowait
        anon "See you soon, [saga.cast.viv]!"
        show old_anon 426 with dissolve.nowait
        show old_viv 46
        viv "Au revoir, [saga.cast.anon]!"
    else:

        viv "That was wonderful."
        show old_viv 45
        show old_anon 26
        anon "Yeah, it was."
        show old_anon 13
        show old_viv 46
        viv "Would you like another session tomorrow?"
        show old_viv 45
        show old_anon 14
        anon "Maybe, I'll let you know."
        show old_anon 13
        show old_viv 46
        viv "Very well. Au revoir, [saga.cast.anon]!"
        show old_viv 45
        show old_anon 36 with dissolve.nowait
        anon "Au revoir, [saga.cast.viv]!"

    hide old_anon with dissolve
    return


label viv05_office5.dialogue(opt, rng=-1):
    if opt == 1:
        viv "Ohhhh!!!"

    elif opt == 2:
        viv "C'est incroyable!"

    elif opt == 3:
        viv "Aaaaaahh!! Don't stop!"
        viv "Harder! Fuck me harder!"

    pause
    return


label viv05_office5.loop:
    menu(range=('fast', 's100', 's075'), screen='old_lewd', tag='old_viv'):
        "Keep Going":
            pass
        "Cum":

            jump viv05_office5.cum
        "Switch":

            jump viv05_office5.switch

    $ renpy.dynamic(pool=saga.lewd.pool(3, max=2))

    while pool:
        call viv05_office5.dialogue (pool.pop(), rng=renpy.random.random()) from viv05_office5.pool

    jump viv05_office5.loop


label viv05_office5.rails:
    scene camera at stage
    show anon a_wtf f_worried_surprised with dissolve
    anon @ -m_talk "C'mon man, stop screwing around..."
    anon @ -m_talk "... I worked hard for this reward and it's time to collect!"
    anon a_fists_low e_b f_happy m_teeth @ -m_talk "Let's hurry upstairs and experience some French delicacies!"
    hide anon with dissolve
    return


label viv05_office5.switch:
    if 'chair' in renpy.get_attributes('old_viv'):
        show old_viv sex chair 16 with dissolve.nowait

        if renpy.random.random() < .5:
            viv "You like doing me on the table, yes?"
        else:
            viv "Back to the table?"

        show old_viv sex chair 2 with dissolve.nowait
        anon "Oui oui!"
        show old_viv 51 with dissolve.nowait
        viv "Ohh, elle est toujours aussi grosse!"
        show old_viv sex 1_2_3_4_5_6_7 fast with dissolve.nowait
        viv "Mmmmm!"
    else:

        show old_viv sex chair 1 with dissolve.nowait
        viv "Let's try on the chair, we should be more comfortable."
        show old_viv sex chair 2 with dissolve.nowait
        anon "You know best. You're the teacher!"
        show old_viv sex chair 3 with dissolve.nowait
        viv "Oh, mon bel homme..."
        show old_viv sex chair 16 with dissolve.nowait
        pause
        show old_viv sex chair 4 with vpunch
        viv "Aaaah!"
        show old_viv sex chair 4_5_6_7_8_9_10_11_12_13 fast with dissolve.nowait
        viv "Yesss!"

    jump viv05_office5.loop


label viv05_outro:
    call shot.school_french_viv
    show old_viv 1 at old_right
    show old_ursula 27 at old_left
    ursula "I don't know how you managed it but the grade point average is increasing."
    show old_ursula 26
    show old_viv 2
    viv "I told you I could inspire them!"
    show old_viv 1
    show old_ursula 27
    ursula "Yeah, well. Don't think it's an excuse to start slacking off!"
    show old_ursula 26
    show old_viv 2
    viv "Don't worry, my students give me one hundred and ten percent!"
    show old_viv 1
    show old_anon 14 behind old_ursula at face_right, pos(.4)
    with dissolve.nowait
    anon "Good morning, [saga.cast.viv]."
    show old_anon 113
    anon "... And [saga.cast.ursula]."
    show old_anon 13
    show old_viv 12
    viv "Bonjour, [saga.cast.anon]."
    show old_viv 13
    show old_anon 114
    show old_ursula 29
    ursula "Hmph."
    hide old_anon
    show old_ursula 26
    show old_viv 12
    with dissolve.nowait
    viv "... Some give me even more than one hundred and ten percent!"
    show old_viv 13
    show old_ursula 29
    ursula "..."
    show old_ursula 28
    with dissolve.nowait
    ursula "Just remember, I've got my eye on you!"
    hide old_ursula with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
