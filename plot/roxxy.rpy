label roxxy_school_french:
    jump roxxy_school_french.intro

    menu roxxy_school_french.choice:
        "Model." if saga.event.peek(choice='model', who=saga.cast.roxxy):
            return saga.event.emit(choice='model', who=saga.cast.roxxy)

        "French exam." if saga.event.peek(choice='exam', who=saga.cast.roxxy):
            return saga.event.emit(choice='exam', who=saga.cast.roxxy)

        "Pom-poms." if saga.event.peek(choice='poms', who=saga.cast.roxxy):
            return saga.event.emit(choice='poms', who=saga.cast.roxxy)

        "[saga.cast.jenny]." if saga.event.peek(choice='tutor', who=saga.cast.roxxy):
            return saga.event.emit(choice='tutor', who=saga.cast.roxxy)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.roxxy):
            return saga.event.emit(choice='talent', who=saga.cast.roxxy)
        "Leave.":

            pass

    jump roxxy_school_french.outro


label roxxy_school_french.intro:
    if saga.cast.roxxy < 'talk':
        jump roxxy_school_french.intro1

    if saga.cast.roxxy < '2':
        jump roxxy_school_french.intro2

    if saga.cast.roxxy < '3':
        jump roxxy_school_french.intro3

    if saga.cast.roxxy < '4':
        jump roxxy_school_french.intro4

    jump roxxy_school_french.intro5


label roxxy_school_french.intro1:
    call shot.school_french_roxxy
    show roxxy a_lolipop_suck f_scary at right
    show anon a_pocket f_worried o_right at left with dissolve
    roxxy a_lolipop "Ugh, gross..."
    roxxy "Get away from me, nerd!"
    hide anon with dissolve
    return


label roxxy_school_french.intro2:
    call shot.school_french_roxxy
    show old_roxxy 11 at old_right
    show old_anon 5 at old_left with dissolve
    roxxy "[saga.cast.anon]..."
    roxxy "What do you want now?"
    show old_roxxy 7 with dissolve
    jump roxxy_school_french.choice


label roxxy_school_french.intro3:
    call shot.school_french_roxxy
    show old_roxxy 1b at old_right
    show old_anon 13 at old_left with dissolve
    roxxy "Hey, [saga.cast.anon]."
    roxxy "What's up?"
    show old_roxxy 1
    jump roxxy_school_french.choice


label roxxy_school_french.intro4:
    call shot.school_french_roxxy
    show old_roxxy 33 at old_right
    show old_anon 5 at old_left with dissolve
    roxxy "Hey, [saga.cast.anon]."
    show old_roxxy 32
    show old_anon 10
    anon "Hey, [saga.cast.roxxy]."
    show old_anon 5
    show old_roxxy 33
    roxxy "Any sign of [saga.cast.dexter]?"
    show old_roxxy 32
    show old_anon 12
    anon "Don't worry, I'll handle [saga.cast.dexter]."
    show old_anon 5
    roxxy "..."
    show old_roxxy 33
    roxxy "Just, don't do anything stupid."
    roxxy "I don't want anything to happen to you..."
    show old_roxxy 32
    anon "..."
    jump roxxy_school_french.choice


label roxxy_school_french.intro5:
    call shot.school_french_roxxy
    show old_roxxy 1b at old_right
    show old_anon 13 at old_left with dissolve
    roxxy "[saga.cast.anon]!"
    hide old_anon
    show old_roxxy 92 at pos(.3935)
    with dissolve
    pause
    show old_roxxy 59d at pos(.5925) with dissolve
    roxxy "How's it going, handsome?"
    show old_roxxy 59e
    anon "Uhh, hehe."
    anon "What's gotten into you?"
    show old_roxxy 59d
    roxxy "I'm just happy to see my man is all!"
    show old_roxxy 59e
    anon "Well, I'm happy to see you too."
    show old_roxxy 59d
    roxxy "Of course you are!"
    roxxy "So, are you coming over tonight?!"
    show old_roxxy 59e
    anon "You want me to?"
    show old_roxxy 59d
    roxxy "Yeah, duh!"
    show old_anon 13 at old_left
    show old_roxxy 1g at center
    with dissolve
    jump roxxy_school_french.choice


label roxxy_school_french.outro:
    if saga.cast.roxxy < '2':
        jump roxxy_school_french.outro2

    if saga.cast.roxxy < '3':
        jump roxxy_school_french.outro3

    if saga.cast.roxxy < '4':
        jump roxxy_school_french.outro4

    jump roxxy_school_french.outro5


label roxxy_school_french.outro2:
    show old_anon 10
    anon "Oh, I don't need anything."
    anon "Just saying hi."
    show old_anon 5
    show old_roxxy 10 with dissolve.nowait
    roxxy "Ugh, well, do you have to do it with so many people around?!"
    show old_roxxy 7 with dissolve.nowait
    anon "..."
    hide old_anon with dissolve
    return


label roxxy_school_french.outro3:
    show old_anon 14
    anon "I'm just heading to class."
    show old_anon 10
    anon "You wanna walk together?"
    show old_anon 13
    show old_roxxy 1b
    roxxy "Oh man, I totally would but I'm supposed to meet [saga.cast.becca] and [saga.cast.missy] soon."
    roxxy "Sorry, [saga.cast.anon]..."
    show old_roxxy 1
    show old_anon 14
    anon "No worries."
    anon "See ya, around."
    show old_anon 13
    hide old_anon with dissolve
    return


label roxxy_school_french.outro4:
    show old_roxxy 32
    show old_anon 12
    with dissolve.nowait
    anon "Don't worry."
    anon "I'm not going to let anything happen to you or your friends."
    show old_anon 90
    show old_roxxy 33
    roxxy "Yeah, but what about you?!"
    show old_roxxy 32
    show old_anon 12
    anon "I'll be fine."
    anon "I promise."
    hide old_anon
    show old_roxxy 59 at pos(.5925)
    with dissolve.nowait
    roxxy "Just be careful."
    return


label roxxy_school_french.outro5:
    show old_anon 14
    anon "I should get going to class."
    show old_anon 13
    show old_roxxy 1b
    roxxy "Yeah, okay."
    hide old_anon
    show old_roxxy 59d at pos(.5925)
    with dissolve.nowait
    roxxy "Let's walk together then!"
    show old_roxxy 59e
    anon "Sure."
    hide old_roxxy with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
