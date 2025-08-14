label kevin_school_cafe:
    jump kevin_school_cafe.intro

    menu kevin_school_cafe.choice:
        "Model." if saga.event.peek(choice='model', who=saga.cast.kevin):
            return saga.event.emit(choice='model', who=saga.cast.kevin)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.kevin):
            return saga.event.emit(choice='talent', who=saga.cast.kevin)

        "Guitar." if saga.event.peek(choice='guitar', who=saga.cast.kevin):
            return saga.event.emit(choice='guitar', who=saga.cast.kevin)
        "Gotta go.":

            pass

    jump kevin_school_cafe.outro


label kevin_school_cafe.intro:
    if 'mags' in saga.cast.kevin.tags:
        jump kevin_school_cafe.mags

    if saga.cast.kevin < 'gym':
        jump kevin_school_cafe.intro1

    jump kevin_school_cafe.intro2


label kevin_school_cafe.intro1:
    call shot.school_cafe_kevin
    show old_kevin 2 at old_right
    show old_anon 13 at old_left with dissolve
    kevin "Sup, bro?!"
    show old_kevin 1
    show old_anon 14
    anon "Hey, [saga.cast.kevin]."
    show old_anon 13
    show old_kevin 2
    kevin "You here to scrub some pots?"
    show old_kevin 1
    show old_anon 17
    anon "Heh, no way man!"
    show old_anon 13
    show old_kevin 2
    kevin "Ugh, this cafeteria duty sucks dick, bro!"
    show old_kevin 1
    pause
    show old_kevin 2
    kevin "... And not the cool kind, either."
    show old_kevin 1
    show old_anon 29 with dissolve.nowait
    anon "Eh, right..."
    show old_anon 3
    pause
    show old_anon 5 with dissolve
    jump kevin_school_cafe.choice


label kevin_school_cafe.intro2:
    call shot.school_cafe_kevin
    show old_kevin 1 at old_right
    show old_anon 14 at old_left with dissolve
    anon "Hey, [saga.cast.kevin]!"
    show old_anon 13
    show old_kevin 2
    kevin "Hello, [saga.cast.anon]."
    show old_kevin 1
    show old_anon 14
    anon "What's up?"
    show old_anon 13
    show old_kevin 2
    kevin "Not much. Yesterday was glutes day for me."
    kevin "My ass is sore!"
    kevin "Feel how tight it is though!"
    show old_kevin 1
    show old_anon 10
    anon "Uhhh... No thanks dude."
    show old_anon 13
    show old_kevin 2
    kevin "Your loss!"
    jump kevin_school_cafe.choice


label kevin_school_cafe.mags:
    call shot.school_cafe_kevin
    show old_kevin 29b at old_right
    show anon f_shy o_right at pos(.15) with dissolve
    anon @ -m_talk "( Eh, I don't want to bother him during his \"me\" time... )"
    anon @ -m_talk "( ... He works so hard afterall. )"
    show old_kevin 31b with dissolve.nowait
    pause
    anon a_rub f_worried_surprised @ -m_talk "( I can't believe [saga.cast.ursula] has given him {i}everyone's{/i} cafeteria duty! )"
    hide anon with dissolve
    return


label kevin_school_cafe.outro:
    show old_anon 14
    anon "Anyways, I gotta go."

    if saga.cast.kevin < 'gym':
        anon "Keep your spirits up, man."
        show old_anon 13
        show old_kevin 2
        kevin "Yeah, alright bro."
        kevin "See ya around."
    else:

        show old_anon 13
        show old_kevin 2
        kevin "I'd better see you at the gym tomorrow, bro!"
        kevin "Bright and early! Am I right?"
        show old_kevin 1
        show old_anon 14
        anon "Maybe..."

    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
