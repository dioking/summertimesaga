label tori_school_office2:
    jump tori_school_office2.intro

    menu tori_school_office2.choice:
        "Grades." if saga.event.peek(choice='grades', who=saga.cast.tori):
            return saga.event.emit(choice='grades', who=saga.cast.tori)

        "Lenses." if saga.event.peek(choice='lenses', who=saga.cast.tori):
            return saga.event.emit(choice='lenses', who=saga.cast.tori)

        "Faptic engine." if saga.event.peek(choice='faptic', who=saga.cast.tori):
            return saga.event.emit(choice='faptic', who=saga.cast.tori)

        "Belt." if saga.event.peek(choice='belt', who=saga.cast.tori):
            return saga.event.emit(choice='belt', who=saga.cast.tori)

        "Serum." if saga.event.peek(choice='serum', who=saga.cast.tori):
            return saga.event.emit(choice='serum', who=saga.cast.tori)

        "Fool around." if saga.event.peek(choice='office', who=saga.cast.tori):
            return saga.event.emit(choice='office', who=saga.cast.tori)
        "Bye.":

            pass

    jump tori_school_office2.outro


label tori_school_office2.intro:
    if saga.cast.tori < 'serum':
        jump tori_school_office2.intro1

    jump tori_school_office2.intro2


label tori_school_office2.intro1:
    call shot.school_office2_tori
    show old_tori 1 at face_right
    show anon a_pocket at right with dissolve
    anon "[saga.cast.tori]?"
    show old_tori 2
    tori "What do you want, [saga.cast.anon]?"
    show old_tori 1
    jump tori_school_office2.choice


label tori_school_office2.intro2:
    call shot.school_office2_tori
    show old_tori 6 at face_right
    show anon a_pocket at right with dissolve
    anon "Hey, [saga.cast.tori]."
    show old_tori 2b
    tori "[saga.cast.anon]!"
    show old_tori 7
    tori "How nice of you to visit!"
    tori "What can I help you with?"
    show old_tori 6
    jump tori_school_office2.choice


label tori_school_office2.outro:
    if saga.cast.tori < 'serum':
        jump tori_school_office2.outro1

    jump tori_school_office2.outro2


label tori_school_office2.outro1:
    jump tori_school_science.outro


label tori_school_office2.outro2:
    show old_tori 6
    anon "Nothing, I just wanted to say hi!"
    show old_tori 5
    tori "That's nice of you."
    tori "Although, I'm busy working on some new designs at the moment."
    show old_tori 7
    tori "Come see me in the science classroom if you want to help me."
    show old_tori 6
    hide anon with dissolve
    return


label tori_school_science:
    jump tori_school_science.intro

    menu tori_school_science.choice:
        "Grades." if saga.event.peek(choice='grades', who=saga.cast.tori):
            return saga.event.emit(choice='grades', who=saga.cast.tori)

        "Lenses." if saga.event.peek(choice='lenses', who=saga.cast.tori):
            return saga.event.emit(choice='lenses', who=saga.cast.tori)

        "Faptic engine." if saga.event.peek(choice='faptic', who=saga.cast.tori):
            return saga.event.emit(choice='faptic', who=saga.cast.tori)

        "Belt." if saga.event.peek(choice='belt', who=saga.cast.tori):
            return saga.event.emit(choice='belt', who=saga.cast.tori)

        "Serum." if saga.event.peek(choice='serum', who=saga.cast.tori):
            return saga.event.emit(choice='serum', who=saga.cast.tori)

        "Invention." if saga.event.peek(choice='invention', who=saga.cast.tori):
            return saga.event.emit(choice='invention', who=saga.cast.tori)

        "Fool around." if saga.event.peek(choice='office', who=saga.cast.tori):
            return saga.event.emit(choice='office', who=saga.cast.tori)
        "Never mind.":

            pass

    jump tori_school_science.outro


label tori_school_science.intro:
    call shot.school_science_door
    show old_tori 1 at old_right
    show anon a_pocket o_right at left with dissolve
    anon "Hey, [saga.cast.tori]."
    show old_tori 2
    tori "What is it, [saga.cast.anon]?"
    show anon f_worried
    tori "I'm very busy ..."
    show old_tori 1
    jump tori_school_science.choice


label tori_school_science.outro:
    anon "Eh, doesn't matter."
    hide anon
    show old_tori 9
    with dissolve.nowait
    tori "Hopeless."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
