label viv_school_french:
    jump viv_school_french.intro

    menu viv_school_french.choice:
        "Tutoring sessions." if saga.event.peek(choice='tutor', who=saga.cast.viv):
            return saga.event.emit(choice='tutor', who=saga.cast.viv)

        "French dictionary." if saga.event.peek(choice='vocab', who=saga.cast.viv):
            return saga.event.emit(choice='vocab', who=saga.cast.viv)

        "Assignment." if saga.event.peek(choice='work', who=saga.cast.viv):
            return saga.event.emit(choice='work', who=saga.cast.viv)

        "Help." if saga.event.peek(choice='help', who=saga.cast.viv):
            return saga.event.emit(choice='help', who=saga.cast.viv)

        "[saga.cast.roxxy]." if saga.event.peek(choice='roxxy', who=saga.cast.viv):
            return saga.event.emit(choice='roxxy', who=saga.cast.viv)

        "Exam." if saga.event.peek(choice='exam', who=saga.cast.viv):
            return saga.event.emit(choice='exam', who=saga.cast.viv)

        "Fool around." if saga.event.peek(choice='office', who=saga.cast.viv):
            return saga.event.emit(choice='office', who=saga.cast.viv)
        "Not really.":

            pass

    jump viv_school_french.outro


label viv_school_french.intro:
    call shot.school_french_viv
    show viv a_note_front at right
    show anon a_pocket o_right at left with dissolve
    viv "Hi, [saga.cast.anon]!"
    anon @ f_happy "Hi, [saga.cast.viv]!"
    viv @ a_note_finger "Have you been able to catch up on your studies?"
    viv "I really hope you do!"
    viv "Now, is there something you wanted to talk about?"
    jump viv_school_french.choice


label viv_school_french.outro:
    anon f_calm "No. I just wanted to say hello."
    viv f_calm "Well, take a seat. Class will be starting soon!"
    viv @ e_b f_happy m_laugh "I've got an exciting lesson planned for today!"
    anon "Sounds good, [saga.cast.viv]."
    hide anon
    with dissolve
    return


label viv_school_office5:
    jump viv_school_office5.intro

    menu viv_school_office5.choice:
        "Tutoring sessions." if saga.event.peek(choice='tutor', who=saga.cast.viv):
            return saga.event.emit(choice='tutor', who=saga.cast.viv)

        "French dictionary." if saga.event.peek(choice='vocab', who=saga.cast.viv):
            return saga.event.emit(choice='vocab', who=saga.cast.viv)

        "Assignment." if saga.event.peek(choice='work', who=saga.cast.viv):
            return saga.event.emit(choice='work', who=saga.cast.viv)

        "Help." if saga.event.peek(choice='help', who=saga.cast.viv):
            return saga.event.emit(choice='help', who=saga.cast.viv)

        "[saga.cast.roxxy]." if saga.event.peek(choice='roxxy', who=saga.cast.viv):
            return saga.event.emit(choice='roxxy', who=saga.cast.viv)

        "Exam." if saga.event.peek(choice='exam', who=saga.cast.viv):
            return saga.event.emit(choice='exam', who=saga.cast.viv)

        "Fool around." if saga.event.peek(choice='office', who=saga.cast.viv):
            return saga.event.emit(choice='office', who=saga.cast.viv)
        "Not really.":

            pass

    jump viv_school_office5.outro


label viv_school_office5.intro:
    if saga.cast.viv < 'sex':
        jump viv_school_office5.intro1

    jump viv_school_office5.intro2


label viv_school_office5.intro1:
    call shot.school_office5_viv
    show viv a_note_front at right
    show anon a_wave o_right at left with dissolve
    anon "Hey, [saga.cast.viv]?"
    viv "Oui?"
    show anon a_side
    viv "Oh, hello [saga.cast.anon]."
    viv "Are you needing something?"
    jump viv_school_office5.choice


label viv_school_office5.intro2:
    scene school_office5 -viv at stage(.545, .46, 2.4)
    show old_viv 28 at face_right, pos(.35)
    show anon a_wave at right with dissolve
    anon "Bonjour, [saga.cast.viv]."
    show old_viv 29
    viv "Oh, [saga.cast.anon]!"
    show anon a_side
    viv "You are 'ere for more {i}tutoring{/i}?"
    show old_viv 28
    jump viv_school_office5.choice


label viv_school_office5.outro:
    if saga.cast.viv < 'sex':
        jump viv_school_office5.outro1

    jump viv_school_office5.outro2


label viv_school_office5.outro1:
    anon f_calm "Nope. Just saying hi."
    viv f_calm "Ah, well... make certain you are showing up on time for class tomorrow."
    viv "I've got an exciting lesson planned."
    anon "Sounds good, [saga.cast.viv]."
    hide anon
    with dissolve
    return


label viv_school_office5.outro2:
    anon a_uneasy f_shy "Not right now."
    show old_viv 30
    viv "C'est la vie!"
    hide anon
    show old_viv 31
    with dissolve.nowait
    viv "Au revoir!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
