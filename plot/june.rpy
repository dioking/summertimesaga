label june_school_tech:
    jump june_school_tech.intro

    menu june_school_tech.choice:
        "Lenses." if saga.event.peek(choice='lenses', who=saga.cast.june):
            return saga.event.emit(choice='lenses', who=saga.cast.june)

        "Faptic engine." if saga.event.peek(choice='faptic', who=saga.cast.june):
            return saga.event.emit(choice='faptic', who=saga.cast.june)

        "Model." if saga.event.peek(choice='model', who=saga.cast.june):
            return saga.event.emit(choice='model', who=saga.cast.june)

        "Printer." if saga.event.peek(choice='copier', who=saga.cast.june):
            return saga.event.emit(choice='copier', who=saga.cast.june)
        "Nothing.":

            pass

    jump june_school_tech.outro


label june_school_tech.intro:
    if saga.cast.june < 'sex':
        jump june_school_tech.intro1

    jump june_school_tech.intro2


label june_school_tech.intro1:
    call shot.school_tech_june
    show old_june 1 at old_right
    show old_anon 14 at old_left with dissolve
    anon "Hi!"
    show old_june 3
    show old_anon 1
    june "Oh, uh, hi?"
    june "What's up?"
    show old_june 2
    jump june_school_tech.choice


label june_school_tech.intro2:
    call shot.school_tech_june
    show old_june 1 at right
    show old_anon 14 at old_left with dissolve
    show old_june 5
    anon "Hey, [saga.cast.june]!"
    show old_anon 1
    show old_june 6
    june "Hi, [saga.cast.anon]!"
    june "What's up?"
    show old_june 5
    jump june_school_tech.choice


label june_school_tech.outro:
    show old_anon 14
    anon "Oh, nothing!"
    anon "Just saying hi."
    show old_anon 1
    show old_june 4
    june "Oh, okay then..."
    show old_june 1
    show old_anon 29
    with dissolve.nowait
    anon "Err... I'll see you later!"
    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
