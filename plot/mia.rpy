label mia_school_science:
    jump mia_school_science.intro

    menu mia_school_science.choice:
        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.mia):
            return saga.event.emit(choice='talent', who=saga.cast.mia)

        "Art partner." if saga.event.peek(choice='art', who=saga.cast.mia):
            return saga.event.emit(choice='art', who=saga.cast.mia)

        "Collage." if saga.event.peek(choice='collage', who=saga.cast.mia):
            return saga.event.emit(choice='collage', who=saga.cast.mia)

        "Model." if saga.event.peek(choice='model', who=saga.cast.mia):
            return saga.event.emit(choice='model', who=saga.cast.mia)

        "Contest." if saga.event.peek(choice='contest', who=saga.cast.mia):
            return saga.event.emit(choice='contest', who=saga.cast.mia)

        "Portrait." if saga.event.peek(choice='portrait', who=saga.cast.mia):
            return saga.event.emit(choice='portrait', who=saga.cast.mia)
        "Bye.":

            pass

    jump mia_school_science.outro


label mia_school_science.intro:
    call shot.school_science_class
    show old_mia 7 at old_left
    show old_mia labcoat 1 as mia_labcoat at old_left
    show old_anon 2 at old_right with dissolve
    anon "Hey, [saga.cast.mia]!"
    anon "How are you?"
    show old_anon 13
    show old_mia 10
    mia "I'm doing okay."
    show old_mia 12
    mia "Not really looking forward to my next class."
    show old_mia 7
    show old_anon 17
    anon "Yeah. I hear ya."
    show old_anon 13
    show old_mia 10
    mia "Is there something you wanted to talk about?"
    show old_mia 7
    jump mia_school_science.choice


label mia_school_science.outro:
    show old_anon 10
    anon "Actually, I'd better get back to class."
    show old_anon 5
    show old_mia 12
    mia "Oh, okay... Talk to you later then!"
    show old_mia 8b
    show old_anon 14
    anon "See ya!"
    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
