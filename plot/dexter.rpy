label dexter_court_main:
    jump dexter_court_main.intro

    menu dexter_court_main.choice:
        "Model." if saga.event.peek(choice='model', who=saga.cast.dexter):
            return saga.event.emit(choice='model', who=saga.cast.dexter)

        "Overdue book." if saga.event.peek(choice='book', who=saga.cast.dexter):
            return saga.event.emit(choice='book', who=saga.cast.dexter)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.dexter):
            return saga.event.emit(choice='talent', who=saga.cast.dexter)
        "Nothing.":

            pass

    jump dexter_court_main.outro


label dexter_court_main.intro:
    call shot.court_main_dexter
    show old_dexter 2 at old_right
    show old_anon 10 at old_left with dissolve
    anon "Hey, umm, [saga.cast.dexter]..."
    show old_anon 5
    show old_dexter 4
    with dissolve.nowait
    dexter "What do you want, twerp?"
    show old_dexter 2
    with dissolve.nowait
    jump dexter_court_main.choice


label dexter_court_main.outro:
    show old_anon 10
    anon "I was just leaving."
    hide old_anon
    show old_dexter 3
    with dissolve.nowait
    dexter "Ya, you better run."
    dexter "NERRRRD!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
