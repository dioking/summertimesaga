label bar06_setup:
    return


label bar06_setup.barb:
    anon f_confused "Have you heard back about the contest yet?"
    barb "Nothing yet."
    barb "I'll let you know the moment I hear something."
    anon f_calm "Alright."
    return


label bar06_art:
    call shot.school_art_barb
    show iwanka a_envelope f_happy at pos(.425)
    show old_barb 11 at old_left
    barb "Oh, yes! He's extremely talented, isn't he?"
    show old_barb 10
    show old_anon 10 at pos(.85)
    with dissolve.nowait
    anon "[saga.cast.barb]?"
    show old_anon 11
    show old_barb 11
    show iwanka o_right at pos(.375)
    with dissolve.nowait
    barb "Oh! Here he is now!"
    show old_barb 11
    barb "Come here, [saga.cast.anon]. There's someone who wants to meet you."
    show old_barb 10
    show old_anon at pos(.625)
    with dissolve.nowait
    anon "..."
    show old_barb 11
    barb "This is the mayor's daughter."
    show old_barb 10
    show old_anon 10
    anon "Wow, really?"
    show old_anon 11
    iwanka "Nice to meet you, [saga.cast.anon]!"
    iwanka "My name is [saga.cast.iwanka]."
    show old_anon 10
    anon "H-hello."
    show old_anon 11
    show old_barb 11
    barb "Aww, forgive him. He's a little shy around beautiful women!"
    show old_barb 10
    iwanka @ e_b m_laugh "That's fine!"
    show old_anon 106 behind iwanka
    iwanka a_envelope_give "My father wanted me to deliver this to you personally along with his congratulations."
    show old_anon 582
    show iwanka a_clasp behind old_anon
    with dissolve.nowait
    anon "..."
    show old_anon 584
    anon "... Is this?"
    show old_anon 583
    iwanka "That's your prize money!"
    show old_anon 584
    anon "Wait, you mean, my painting won?!"
    show old_anon 583
    iwanka "That's right! First place!"
    show old_anon 584
    anon "Awesome!"
    show old_anon 583
    iwanka "My father really loved your piece!"
    iwanka "In fact, he made a copy for his own private collection."
    iwanka "He's even considering hiring you to paint a picture of the entire Rump family."
    show old_anon 584
    anon "For real?"
    show old_anon 583
    iwanka @ -m_talk "Mmmhmm..."
    iwanka "I got your phone number from [saga.cast.barb]. I hope that's alright?"
    show old_anon 584
    anon "Y-yeah, of course!"
    show old_anon 583
    iwanka "Very good, we'll be in contact."
    iwanka "Congratulations once again and have a good day!"
    show old_anon 584
    anon "Yeah, you too!"
    hide iwanka with dissolve
    anon "I can't believe it, we won, [saga.cast.barb]!"
    show old_anon 583
    show old_barb 27
    with dissolve.nowait
    barb "You won, [saga.cast.anon]!"
    barb "... And I couldn't be more proud!"
    show old_anon 584 at center
    show old_barb 26
    with dissolve.nowait
    anon "Here, this money is for you."
    show old_anon 1
    show old_barb 33
    with dissolve.nowait
    barb "Oh my goodness!"
    show old_barb 32
    pause
    show old_barb 31
    barb "... This is just..."
    show old_barb 32
    pause
    hide old_anon
    show old_barb 21
    with dissolve.nowait
    barb "You're my hero, [saga.cast.anon]!"
    show old_barb 20
    pause
    show old_barb 21
    barb "You know..."
    show old_barb 20
    pause
    show old_barb 21
    barb "... There's one more art technique I'd like to teach you."
    show old_barb 13
    show old_anon 10 at center
    with dissolve.nowait
    anon "There is?"
    show old_anon 11
    show old_barb 12
    barb "Mmhmm..."
    show old_barb 13
    barb "... Why don't you come up to my office after class and I'll show you."
    show old_barb 12
    show old_anon 2
    anon "Okay, I'll go tell [saga.cast.mia]!"
    show old_barb 25
    show old_anon 1
    barb "No! Hold on."
    show old_barb 24
    show old_anon 11
    anon "..."
    show old_barb 25
    barb "I'm afraid, [saga.cast.mia] isn't ready for this particular technique yet."
    show old_barb 24
    show old_anon 10
    anon "Oh, it's too advanced for her?"
    show old_barb 13
    show old_anon 11
    barb "Heh, yeah. Something like that."
    barb "She'll get there someday, don't you worry..."
    show old_barb 12
    show old_anon 10
    anon "O-okay, I guess I'll see you after class?"
    show old_barb 13
    show old_anon 11
    barb "I'll be waiting."
    hide old_anon with dissolve
    return


label bar06_office3:
    call shot.school_office3_barb
    show old_barb 13 at pos (.4), face_right
    show old_anon 1 at old_right with dissolve
    barb "There's my little hero!"
    show old_barb 12
    show old_anon 2
    anon "Wow, it smells really good in here!"
    show old_barb 13
    show old_anon 1
    barb "You like that? It's my favorite incense."
    barb "It really enhances the mood, don't you think?"
    show old_barb 12
    show old_anon 10
    anon "Uhh, sure. I guess..."
    anon "What's with the giant canvas?"
    show old_anon 11
    show old_barb 13
    barb "Hehe, patience, [saga.cast.anon]. You can't rush this or the art will suffer."
    show old_anon 10
    show old_barb 12
    anon "... Oh, okay."
    show old_anon 11
    show old_barb 13
    barb "Why don't you go lock the door. We don't want anyone to disturb us..."
    show old_anon 2
    show old_barb 12
    anon "Alright."
    hide old_anon with dissolve
    pause
    show old_barb 14 with dissolve
    pause
    show old_anon 2 at old_right
    show old_barb 15
    with dissolve
    anon "... Okay, now wh-"
    show old_barb 16
    show old_anon 11
    with dissolve
    pause
    show old_anon 10
    show old_barb 17 with dissolve
    anon "... Eh?"
    show old_barb 37 with dissolve
    anon "What are you doing, [saga.cast.barb]?"
    show old_anon 11
    show old_barb 36
    barb "Oh, you'll need to undress as well..."
    barb "... We're going to be using our bodies to paint, [saga.cast.anon]."
    show old_barb 37
    show old_anon 10
    anon "... Our bodies?"
    show old_barb 48 with dissolve
    pause .5
    show old_barb paint 9 at face_right
    with dissolve
    show old_anon 11
    anon "( !!! )" with hpunch
    show old_barb paint 10
    barb "That's right!"
    barb "Don't be shy now..."
    barb "Lose those clothes!"
    show old_barb paint 9
    show old_anon 10
    anon "... O-okay."
    show old_anon 8 with dissolve
    pause
    show old_anon 261 with dissolve
    pause
    show old_anon 430 with dissolve
    show old_barb paint 10
    barb "Wonderful!"
    barb "You're such a gifted young man, [saga.cast.anon]..."
    show old_anon 430b
    show old_barb paint 9
    anon "Heh, thanks."
    show old_anon 430
    barb "Mmmhmm."
    show old_barb paint 10
    barb "Okay, for the next step..."
    barb "We're gonna need to add a little paint to the equation..."
    show old_barb paint 9
    show old_anon 430b
    anon "I'm not sure I..."
    show old_barb paint 6
    with dissolve
    show old_anon 430
    barb "Here take this."
    show old_barb paint 9
    show old_anon 613
    with dissolve
    pause
    show old_anon 614
    anon "... W-what am I painting exactly?"
    show old_barb paint 1
    with dissolve
    show old_anon 613
    barb "Hehe, me, silly!"
    barb "Don't worry, I'll show you."
    show old_barb paint 2
    pause

    scene black with fade
    barb "That's it, [saga.cast.anon]..."
    barb "Just go nuts with it!"
    anon "..."
    barb "Hehe, that tickles!"

    call shot.school_office3_barb
    show old_barb 48 at pos(.4), face_right
    show old_barb paint overlay as barb_paint at pos(.4), face_right
    show old_anon 616_615 s950 at pos(.68)
    with dissolve
    pause
    show old_barb 47
    barb "Well done, [saga.cast.anon]!"
    barb "Oh, I really love this technique!"
    hide barb_paint
    show old_anon 615
    show old_barb paint 3_4_5 pong slow
    with dissolve.nowait
    pause
    show old_anon 616_615 s950
    show old_barb 47
    show old_barb paint overlay as barb_paint at pos(.4), face_right
    with dissolve.nowait
    barb "... This feels so amazing!"
    hide barb_paint
    show old_anon 432
    show old_barb paint 3_4_5 pong slow
    with dissolve.nowait
    anon "Where did you learn this anyways?"
    show old_barb paint 10
    show old_barb paint overlay as barb_paint at pos(.4), face_right
    with dissolve
    show old_anon 431
    barb "Oh, it's just something I came up with a long time ago."
    barb "My first year of teaching actually."
    show old_barb paint 9
    show old_anon 432
    anon "Really?"
    show old_anon 431
    barb "Mmmhmm..."
    show old_barb paint 10
    barb "... But we haven't even gotten to the best part yet."
    show old_barb paint 9
    show old_anon 432
    anon "... What's the best part?"
    show old_barb paint 10
    show old_anon 431
    barb "I want you to make love to me, [saga.cast.anon]!"
    show old_anon 430
    anon "( !!! )" with hpunch
    show old_anon 430b
    show old_barb paint 9
    anon "What?!"
    show old_anon 430
    show old_barb paint 10
    barb "Make love to me! Right here on this canvas!"
    barb "Use my body to paint your masterpiece!"
    show old_anon 430b
    show old_barb paint 9
    anon "You really want to... with me?"
    hide barb_paint
    hide old_anon
    show old_barb paint 11_12 slow at pos (.5875), face_right
    with dissolve.nowait
    barb "Of course I want to!"
    barb "I've wanted this big dick of yours inside me since the moment I saw that cute little giraffe you made out of clay."
    anon "... You did?"
    barb "Oh, yes!"
    barb "Nothing turns me on more than a talented young artist!"
    anon "... This feels really good."
    barb "It's about to feel a whole lot better!"
    barb "Come lay down."

    label bar06_office3.reuse:
    scene school_office3_tarp
    show old_barb sex anon as old_anon
    show old_barb sex 1
    with fade

    if saga.cast.barb < 'sex':
        barb "Oh, I can't believe it's finally happening!"
    else:
        barb "Oh, I can't wait to feel it again!"

    barb "..."
    show old_barb sex 2 with dissolve.nowait
    barb "Oooh, wow!"
    show old_barb sex 2_3_4_5_6_7_8_9_10_11 fast
    call bar06_office3.dialogue (1)
    show old_barb sex 2_3_4_5_6_7_8_9_10_11 s100
    call bar06_office3.dialogue (2)
    show old_barb sex 2_3_4_5_6_7_8_9_10_11 s075
    call bar06_office3.dialogue (3)
    jump bar06_office3.loop


label bar06_office3.barb:
    anon f_confused "You said you had one final technique to teach me?"
    barb f_happy "Oh yes! It's a good one too!"

    if saga.cast.barb in saga.sets.school_office3:
        barb f_sad "I can't teach now though, come by my office another day after class."
    else:
        barb f_calm "I can't teach you here though. You'll have to come by my office after class."

    anon f_calm "It sounds really awesome!"

    if saga.cast.barb in saga.sets.school_office3:
        anon f_shy "I'll see you then, [saga.cast.barb]."
    else:
        anon "I'll see you there, [saga.cast.barb]."

    hide anon with dissolve
    return


label bar06_office3.cum:
    barb "I've been thinking about this all day!"
    anon "You have?"
    barb "Yes..."
    barb "... All day..."
    barb "... Just thinking about your happy little dick..."
    barb "... And how much I need it inside my happy little vagina!"
    anon "..."
    barb "Oh, I'm gonna cum!"
    barb "OH FUCK!"
    barb "AAAHHHHH!!!" with flash
    anon "I can't hold it!"
    barb "Oh, I love it! I love it! I love it!"
    pause
    hide old_anon
    show old_barb sex 12_13 norm
    anon "HNNGGG!!!" with flash
    barb "{i}*GASP*{/i}!"
    barb "Mmmph!"
    pause
    show old_barb sex anon as old_anon behind old_barb
    show old_barb sex 14
    with dissolve.nowait
    barb "Haaah... Haaah..."
    barb "Wow!"
    barb "... [saga.cast.anon]."
    barb "That was..."
    show old_barb sex 15_16 once slow with dissolve.nowait

    if saga.cast.barb < 'sex':
        barb "... I mean, I've had a lot of sex in my life..."
        barb "... A lot of good sex!"
        barb "But that was something else entirely!"
        anon "Y-yeah."
    else:

        barb "... I still can't get over how good it is..."
        barb "... Every single time!"
        barb "Sex with you is something else entirely!"
        anon "W-with you too."

    call shot.school_office3_barb
    show school_office3 t1
    show old_barb paint 10 at pos(.4), face_right
    show old_barb paint overlay as barb_paint at pos(.4), face_right
    show old_anon 8 at old_right
    with fade
    barb "We need to do that again!"
    show old_anon 1 with dissolve

    if saga.cast.barb < 'sex':
        barb "I've never came so hard before!"
    else:
        barb "I always cum so hard with you!"

    show old_barb paint 9
    anon "..."
    show old_barb paint 10

    if saga.cast.barb < 'sex':
        barb "You wouldn't mind doing it again sometime, would you, [saga.cast.anon]?"
    else:
        barb "You'd never leave your poor teacher wanting, would you, [saga.cast.anon]?"

    show old_barb paint 9
    show old_anon 2
    anon "Of course not!"
    anon "I'll do that anytime you want!"
    show old_barb paint 10
    show old_anon 1
    barb "Hehe, well, I think that's enough for today..."
    barb "I'm exhausted..."
    show old_anon 2
    show old_barb paint 9
    anon "Yeah, me too."
    show old_anon 1
    show old_barb paint 10
    barb "You come and find me in my office whenever you need another {i}private lesson{/i}. Okay?"
    show old_anon 2
    show old_barb paint 9
    anon "Heh, yes ma'am!"
    hide old_anon with dissolve
    return


label bar06_office3.dialogue(opt, rng=-1):
    if opt == 1:
        if saga.cast.barb < 'sex':
            barb "Oh my goodness! It's even better than I imagined!"
            anon "Oh, [saga.cast.barb]!"
        else:

            barb "Oh, I'm so glad you came by today!"
            barb "I really needed this!"

    elif opt == 2:
        if saga.cast.barb < 'sex':
            barb "It's never felt so good!"
            barb "This is incredible!"
            anon "Ahhh!"
            barb "Why is this so good?!"
        else:

            barb "That's it, [saga.cast.anon]!"
            barb "Oh, this is so beautiful!"
            barb "I want you to come a lot for me this time!"

    elif opt == 3:
        if saga.cast.barb < 'sex':
            if 's075' in renpy.get_attributes('old_barb'):
                barb "Oh, fuck me!"
                anon "I can't..."
                anon "You're going too fast!"

            barb "I love your dick, [saga.cast.anon]!"
            barb "Oh, I love it so much!"
        else:

            barb "Oh, I'm still a little sore from our last session..."
            anon "Should we stop?"
            barb "Don't you dare stop!"
            barb "Oh, yes!"

    elif opt == 4:
        anon "Oh, that feels so good!"
        barb "Mmm, I love this dick so much!"

    elif opt == 5:
        barb "Give it to me, [saga.cast.anon]!"
        barb "That's it!"
        barb "AAAHHH!"

    elif opt == 6:
        anon "Oh, wow!"
        anon "Ahhh!!"
        barb "That's it!"
        barb "Paint a white masterpiece on my ovarian canvas!"

    elif opt == 7:
        barb "Yes! Yes! Fuck me!"
        barb "It's so good, [saga.cast.anon]!"
        anon "Oh, [saga.cast.barb]!!!"

    pause
    return


label bar06_office3.loop:
    menu(range=('fast', 's100', 's075'), screen='old_lewd', tag='old_barb'):
        "Keep Going":
            pass
        "Cum":

            jump bar06_office3.cum

    $ renpy.dynamic(pool=saga.lewd.pool(7, max=3))

    while pool:
        call bar06_office3.dialogue (pool.pop(), rng=renpy.random.random()) from bar06_office3.pool

    jump bar06_office3.loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
