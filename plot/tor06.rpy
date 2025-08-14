label tor06_setup:
    return


label tor06_setup.tori:
    show anon f_worried
    anon "You doing okay, ma'am?"
    anon f_confused "Notice any side effects with your serum yet?"
    show old_tori 7
    tori "I'm still testing."
    tori "... I appreciate you checking in with me though."
    show old_tori 6
    anon f_sceptical "... You do?"
    show old_tori 7
    tori "Of course!"
    show old_tori 2b
    tori "It makes me feel all warm and fuzzy!"
    show old_tori 6
    anon f_confused @ -m_talk "..."
    anon f_worried "Okay, seriously! You are acting really weird!"
    show old_tori 7
    tori "Am I?"
    show old_tori 2b
    tori "I don't know what to tell you. I feel great!"
    show old_tori 6
    anon f_confused "Okay, well, just be careful, I guess."
    show old_tori 7
    tori "Will do, handsome!"
    show old_tori 2b
    show anon f_worried_surprised
    tori "Hehehe!"
    anon f_worried @ -m_talk "..."
    hide anon with dissolve
    return


label tor06_tori:
    show anon f_worried
    anon "Any results from the serum yet?"
    show old_tori 7
    tori "Actually, [saga.cast.anon], I was hoping you could help me test my newest invention?"
    show old_tori 6
    anon "Oh man, you want me to build something else?"
    show old_tori 3
    tori "Hmm? No, no!"
    show old_tori 7
    tori "I built this one myself. It's revolutionary!"
    show old_tori 6
    anon "You built it?"
    anon "But building is monkey work. I thought you didn't do monkey work?"
    show old_tori 7
    tori "I made an exception this time because..."
    tori "Well, I made this invention for you, as a surprise."
    show old_tori 6
    anon "For me?"
    show old_tori 7
    tori "Yeah, come to my office this evening after school and I'll show you."
    show old_tori 7
    anon "This is starting to worry me..."
    anon "What are you up to?"
    show old_tori 2b
    tori "Don't be a baby! You have to come and see!"
    show old_tori 6
    anon "Fine."
    show old_tori 7
    tori "You promise?"
    show old_tori 6
    anon "Uhh, yeah."
    anon "... I promise."
    show old_tori 2b
    tori "Yay!"
    show old_tori 7
    tori "See you soon, [saga.cast.anon]!"
    show old_tori 6
    anon @ -m_talk "..."
    hide anon with dissolve
    return


label tor06_tori.area:
    jump tor06_setup.tori


label tor06_office2:
    call shot.school_office2_entry
    show old_anon 10 with dissolve
    anon "Alright, I'm here."
    show old_anon 11
    show old_tori 7 at old_left
    with dissolve.nowait
    tori "[saga.cast.anon], I'm so happy you came!"
    show old_anon 10
    show old_tori 6
    anon "Where's this invention you were telling me about?"
    show old_anon 11
    show old_tori 32
    with dissolve.nowait
    tori "It's right here..."
    show old_anon 10
    show old_tori 33
    anon "That little thing?"
    show old_anon 30
    anon "What does it do?"
    show old_anon 113
    show old_tori 89 at pos(.346)
    with dissolve.nowait
    tori "Shh, I'm trying to show you..."
    tori "This is a Sensory A.R. Device."
    anon "A sensory wha-"
    show old_anon 23
    show old_tori 6 at old_left
    show old_tori MC eyes2 as anon_eyes
    with dissolve
    anon "( !!! )" with hpunch
    show old_anon 15
    anon "What the hell?!"
    anon "That hurt!"
    show old_tori 39 with dissolve.nowait
    anon "Get this thing-"
    show old_anon 10
    show old_tori 40
    with dissolve.nowait
    anon "..."
    show old_anon 11
    show old_tori 41
    with dissolve.nowait
    pause
    show old_tori 42
    show old_anon 10
    with dissolve.nowait
    anon "Uhhh..."
    show old_anon 83
    show old_tori 43
    with dissolve
    anon "What are you doing?"
    show old_anon 82
    show old_tori 44 with dissolve
    pause
    show old_tori 45
    tori "Preparing for the next part."
    show old_tori 44
    show old_anon 83
    anon "The next part?"
    anon "What next part?!"
    show old_anon 82
    show old_tori 45
    tori "It should activate itself any second now..."
    show old_tori 44
    pause
    show old_anon 83
    anon "... Huh?"
    anon "What happens when it-"
    show old_tori MC eyes as anon_eyes
    show old_anon 81
    anon "( !!! )" with hpunch

    scene school_office2_chair space -chair
    show old_anon 368b
    with flash
    pause
    show old_anon 367b
    anon "What the hell!"
    show old_anon 368b at face_right with dissolve
    anon "..."
    show old_anon 368b at face_left with dissolve.nowait
    pause
    show old_anon 367b
    anon "Where am I?!"
    show old_anon 368b
    show old_tori 44b behind old_anon at pos(.8)
    with dissolve.nowait
    pause
    show old_tori 45b at pos(.582)
    with dissolve
    tori "Welcome to Augmented Reality."
    show old_tori 44b
    show old_anon 367b at face_right, pos(.41)
    with dissolvefast.nowait
    anon "[saga.cast.tori]?"
    anon "Where are-"
    anon "Wait."
    anon "Did you just say Augmented Reality?"
    show old_anon 368b
    tori "Mmmhmm."
    show old_anon 367b
    anon "So none of this is real?"
    show old_anon 368b
    show old_tori 45b
    tori "That would depend upon how you define real..."
    show old_tori 44b
    anon "..."
    show old_anon 367b
    anon "... Why are we naked?"
    show old_anon 368b
    show old_tori 45b
    tori "We have no need for clothes here."
    show old_anon 367b
    show old_tori 44b
    anon "I am so confused..."
    show old_anon 368b
    show old_tori 45b
    tori "Shhhh..."
    tori "Just calm down."
    tori "We're in a shared Augmented Reality that I built just for us."
    tori "Isn't it beautiful, [saga.cast.anon]?"
    show old_anon 367b
    show old_tori 44b
    anon "Y-yeah, I suppose."
    anon "... But what is the purpose of all this?"
    show old_anon 368b
    show old_tori 45b
    tori "We're about to experience something that no other person ever has."
    show old_tori 44b
    anon "..."
    show old_tori 45b
    tori "You see, [saga.cast.anon]. The device I attached to your head..."
    tori "... The one that brought you to this wonderful place."
    tori "It was designed to link its user's nervous systems together."
    show old_tori 44b
    anon "..."
    show old_anon 367b
    anon "... Which means?"
    show old_anon 368b
    tori "..."
    show old_tori 86b with dissolve
    show old_anon 367b
    anon "What are you-"
    show old_tori 85b
    show old_anon 430c with dissolve
    anon "( !!! )"
    show old_anon 430d
    show old_tori 86b
    pause
    show old_anon 430c
    anon "I can feel that!"
    show old_anon 430d
    show old_tori 45b with dissolve
    tori "Precisely!"
    tori "So long as we are in this Augmented Reality, we will share our sensations."
    show old_anon 430c
    show old_tori 46b with dissolve
    anon "... That's incredible!"
    show old_anon 430d
    tori "Mmmhmm."
    show old_anon 430c
    anon "So what kind of tests are we going to run?"
    show old_anon 430d
    show old_tori 50b with dissolve
    tori "We're going to copulate."
    show old_anon 430c
    show old_tori 51b
    anon "Copu-what?!"
    show old_anon 430d
    show old_tori 50b
    tori "We're going to have sexual intercourse."
    show old_anon 430c
    show old_tori 51b
    anon "Like for real?"
    show old_anon 430d behind old_tori
    show old_tori 50b at pos(.508)
    with dissolve.nowait
    tori "Just relax, [saga.cast.anon]."
    tori "You're going to enjoy this!"
    show old_tori 51b
    anon "{i}*Gulp*{/i}"
    show old_anon 430c
    anon "... Uh huh."
    hide old_anon
    show old_tori sex 1b_2b_3b_4b_5b_6b_7b_8b_9b_10b s150
    with flash
    pause
    tori "Oh wow!"
    tori "This is so fascinating..."
    pause
    tori "It's almost like scratching at an itch that won't go away."
    anon "..."
    pause
    anon "Y-yeah, fascinating."
    anon "This feels really-"
    tori "Amazing!"
    pause
    anon "Yeah!"
    anon "... And weird! Really, really weird!"
    pause
    anon "It's so deep!"
    tori "AH!!"
    tori "Yes it is."
    tori "So deeeep!"
    pause
    tori "... And warm."
    pause
    anon "... And tight!"
    pause
    anon "It's so tight! It's squeezing me!"
    pause
    tori "Harder!"
    show old_tori sex 1b_2b_3b_4b_5b_6b_7b_8b_9b_10b s100
    tori "AAAHHH!!"
    pause
    anon "This is the best invention ever!!"
    tori "Yeah it is!"
    pause
    show old_tori sex 1b_2b_3b_4b_5b_6b_7b_8b_9b_10b s075
    tori "Oh, yes!"
    tori "I'm getting close, [saga.cast.anon]!"
    anon "... I can feel it!"
    anon "OH WOW!!"
    jump tor06_office2.loop


label tor06_office2.cum:
    if 'space' in renpy.get_attributes('school_office2_chair'):
        anon "God, I love these devices!"
        tori "... I love your dick, [saga.cast.anon]!"
        pause
        anon "Call me Neo!"

        if saga.cast.tori < 'sex':
            tori "Huh?"
        else:
            tori "Seriously?"

        anon "Call me Neo!!"

        if saga.cast.tori < 'sex':
            tori "Neo?!"
        else:
            tori "NEO!!"

        show old_tori sex 11b_12b norm
        anon "HNNNNGGGGG!!!" with flash
        pause
    else:

        tori "This is incredible!"
        tori "It feels like I'm about to boil over!"
        anon "I can't hold it anymore!"
        tori "Don't you dare stop!"
        tori "Don't you-"
        show old_tori sex 11_12 norm
        tori "YEESSSSSS!!!" with flash
        tori "Aaaah, I can't feel my legs!"

    scene black
    with dissolve
    mono ""

    call shot.school_office2_entry
    show school_office2 t1
    show old_anon 21
    show old_tori 75 at old_left
    with dissolve

    if saga.cast.tori < 'sex':
        anon "That was..."
        show old_anon 28
        show old_tori 74
        tori "Mind-blowing!"
        show old_anon 10
        show old_tori 75
        anon "I was gonna say weird..."
        show old_anon 21
        anon "... But yeah, mind-blowing works too!"
        show old_anon 28
        show old_tori 74
        tori "Hehehe."
        tori "I think you've earned your A."
        show old_anon 21
        show old_tori 75
        anon "Really?!"
        show old_anon 28
        show old_tori 74
        tori "Definitely!"
        tori "I've never experienced anything so intense before!"
        show old_anon 21
        show old_tori 75
        anon "Me neither..."
        show old_anon 28
        show old_tori 74
        tori "I think this device is gonna need more testing."
        show old_anon 21
        show old_tori 75
        anon "Oh?"
        show old_anon 28
        show old_tori 74
        tori "A {i}lot{/i} more testing!"
        show old_anon 21
        show old_tori 75
        anon "You mean we can do this again?"
    else:

        anon "Haaah... Haaah..."
        show old_anon 11
        show old_tori 74
        tori "That... really wasn't any less intense..."
        tori "... At some point it {i}must{/i} normalise!"
        show old_anon 10
        show old_tori 75
        anon "So... more testing?"

    show old_anon 28
    show old_tori 74
    tori "Absolutely!"
    tori "Just come visit me in my office when you have time for testing."
    show old_anon 21
    show old_tori 75
    anon "Alright, will do."
    hide old_anon
    with dissolve
    return


label tor06_office2.dialogue(opt, rng=-1):
    if opt == 1:
        if saga.cast.tori > 'sex':
            anon "I'm not sure I'll ever get used to feeling both sides of this."

        tori "It's pretty intense, huh?"
        anon "Y-yeah!"

        if rng < .5:
            tori "Just relax and let me do the work."
            anon "Haaahh..."

        if rng < .8:
            tori "Amazing!"
            tori "AAAaahh!!"

    elif opt == 2:
        tori "You can go deeper if you want..."
        anon "... No. I really think it's deep enou-"
        anon "AAAh!!! Fuck!"

        if rng < .5:
            anon "I can't believe how big it is!"
            tori "I know, right?"
            tori "It kinda hurts but in a really good way..."
            anon "Y-yeah, just don't stop-"

        if rng < .7:
            tori "AAAhhhh!!"
            tori "It's so good!"

    elif opt == 3:
        tori "Fuck me!"
        tori "Oooh!!"

        if rng < .6:
            tori "Fuck me harder!"
            anon "..."
            tori "HARDER!"

        tori "AAAAhhhh!!"

    pause
    return


label tor06_office2.loop:
    menu(range=('s150', 's100', 's075'), screen='old_lewd', tag='old_tori'):
        "Keep Going":
            pass
        "Cum":

            jump tor06_office2.cum
        "Switch":

            if 'space' in renpy.get_attributes('school_office2_chair'):
                show school_office2_chair chair -space
                show old_tori sex 1_2_3_4_5_6_7_8_9_10
            else:

                show school_office2_chair space -chair
                show old_tori sex 1b_2b_3b_4b_5b_6b_7b_8b_9b_10b

            with flash

    $ renpy.dynamic(pool=saga.lewd.pool(3, max=1))

    while pool:
        call tor06_office2.dialogue (pool.pop(), rng=renpy.random.random()) from tor06_office2.pool

    jump tor06_office2.loop


label tor06_office2.tori:
    anon f_confused "So, you've been working on a new invention, huh?"
    show old_tori 7
    tori "Oh, yes!"
    tori "It's revolutionary! You absolutely have to come and see it after class!"
    show old_tori 6
    anon f_shy "Heh, okay! I'll meet you in your office."
    show old_tori 2b
    tori "You have to promise you'll come and see!"
    show old_tori 6
    anon "..."
    anon "... Yeah. I promise."
    show old_tori 2b
    show anon f_worried
    tori "I can't wait!"
    show old_tori 6
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
