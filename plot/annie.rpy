label annie_school_hall2:
    jump annie_school_hall2.intro

    menu annie_school_hall2.choice:
        "Model." if saga.event.peek(choice='model', who=saga.cast.annie):
            return saga.event.emit(choice='model', who=saga.cast.annie)
        "Hi.":

            pass

    jump annie_school_hall2.outro


label annie_school_hall2.intro:
    call shot.school_hall2_annie
    show annie a_behind o_right at left
    show anon a_wave f_shy at right with dissolve
    anon "Hey [saga.cast.annie]!"
    annie f_annoyed "Make it quick!"
    show anon a_side
    jump annie_school_hall2.choice


label annie_school_hall2.outro:
    anon f_calm "Oh, nothing... I was just saying hi!"
    annie @ f_angry "I'm on hall monitoring duty... and you're wasting my time."
    anon f_surprised @ -m_talk "..."
    anon f_sceptical "All right. Sorry to bother you. Sheesh!"
    hide anon with dissolve
    return


label annie_school_music:
    scene school_music -annie at stage(.7, .5, 2)
    show annie a_behind at right
    show anon a_pocket o_right at left with dissolve
    anon "Hey, [saga.cast.annie]."
    annie f_annoyed "I'm trying to concentrate."
    anon a_uneasy f_worried @ -m_talk "..."
    anon f_shy "Sorr-"
    show anon f_worried_surprised
    annie @ f_angry "I'M CONCENTRATING!" with hpunch
    anon a_pocket f_calm -o_right "And I'm leaving!"
    anon "Jeez..."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
