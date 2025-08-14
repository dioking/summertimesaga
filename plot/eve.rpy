label eve_school_french:
    jump eve_school_french.intro

    menu eve_school_french.choice:
        "Tutor." if saga.event.peek(choice='tutor', who=saga.cast.eve):
            return saga.event.emit(choice='tutor', who=saga.cast.eve)

        "Bag." if saga.event.peek(choice='bag', who=saga.cast.eve):
            return saga.event.emit(choice='bag', who=saga.cast.eve)

        "Model." if saga.event.peek(choice='model', who=saga.cast.eve):
            return saga.event.emit(choice='model', who=saga.cast.eve)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.eve):
            return saga.event.emit(choice='talent', who=saga.cast.eve)

        "Karaoke." if saga.event.peek(choice='karaoke', who=saga.cast.eve):
            return saga.event.emit(choice='karaoke', who=saga.cast.eve)

        "Adhesive." if saga.event.peek(choice='glue', who=saga.cast.eve):
            return saga.event.emit(choice='glue', who=saga.cast.eve)
        "Never mind.":

            pass

    jump eve_school_french.outro


label eve_school_french.intro:
    if saga.cast.eve < '13':
        jump eve_school_french.intro1

    if saga.cast.eve < '20':
        jump eve_school_french.intro2

    jump eve_school_french.intro3


label eve_school_french.intro1:
    call shot.school_french_desks
    show eve a_pencil e_e o_right p_desk at pos(.6)
    show eve o_right ob_chair z_ob as anon_chair at pos(.25, 1.02)
    show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)
    with None
    hide anon_chair
    hide anon_desk
    show anon a_pencil o_right p_desk at pos(.25, 1.02)
    with dissolve.nowait
    anon "Morning, [saga.cast.eve]."
    eve "Hey, [saga.cast.anon]."
    anon "Working hard?"
    eve "Heh, yea right..."
    eve @ e_r f_annoyed "This class is {i}so{/i} boring!"
    jump eve_school_french.choice


label eve_school_french.intro2:
    call shot.school_french_desks
    show eve a_pencil e_e o_right p_desk at pos(.6)
    show eve o_right ob_chair z_ob as anon_chair at pos(.25, 1.02)
    show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)
    with None
    hide anon_chair
    hide anon_desk
    show anon a_pencil o_right p_desk at pos(.25, 1.02)
    with dissolve.nowait
    anon "Morning, [saga.cast.eve]."
    eve "Hey, [saga.cast.anon]!"
    anon "Ready for another fun day of school?"
    eve @ e_r f_annoyed "Heh, yeah... \"Fun.\""
    eve "I wish we could just skip and hang out at my place."
    anon "Yeah, me too."
    jump eve_school_french.choice


label eve_school_french.intro3:
    call shot.school_french_desks
    show eve a_pencil e_e o_right p_desk at pos(.6)
    show eve o_right ob_chair z_ob as anon_chair at pos(.25, 1.02)
    show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)
    with None
    hide anon_chair
    hide anon_desk
    show anon a_pencil o_right p_desk at pos(.25, 1.02)
    with dissolve.nowait
    anon "Morning, [saga.cast.eve]."
    eve "Hey, [saga.cast.anon]!"
    hide anon
    show eve o_right ob_chair z_ob as eve_chair behind eve at pos(.525)
    show eve o_right ob_chair z_ob as anon_chair behind eve at pos(.15, 1.02)
    show eve o_right ob_desk z_ob as eve_desk at pos(.6)
    show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)
    show eve b_anon p_kiss -o_right at pos(.4)
    with dissolve
    pause
    eve "Mmm."
    hide anon_chair
    hide anon_desk
    hide eve_chair
    hide eve_desk
    show eve f_happy o_right p_desk at pos(.6)
    show anon a_pencil f_horny o_right p_desk at pos(.25, 1.02)
    with dissolve
    anon "Mmm, that was nice."
    eve @ e_b m_laugh "Hehe!"
    eve @ e_r f_annoyed "Ugh, I'm so not in the mood for class today."
    eve "You wanna skip with me?"
    anon f_worried "I dunno, maybe."
    eve "Aww, c'mon... please?"
    eve "It's so boring when you're not around!"
    jump eve_school_french.choice


label eve_school_french.outro:
    anon f_shy "I should probably get ready for class."
    eve f_calm "Yeah, me too."
    anon f_calm "I'll talk to you later, okay?"
    eve "Yup, later."

    if saga.cast.eve in saga.sets.school_french:
        show eve o_right ob_chair z_ob as anon_chair at pos(.15, 1.02)
        show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)

    hide anon
    with dissolve
    return


label eve_school_hall1e:
    jump eve_school_hall1e.intro

    menu eve_school_hall1e.choice:
        "Model." if saga.event.peek(choice='model', who=saga.cast.eve):
            return saga.event.emit(choice='model', who=saga.cast.eve)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.eve):
            return saga.event.emit(choice='talent', who=saga.cast.eve)

        "Karaoke." if saga.event.peek(choice='karaoke', who=saga.cast.eve):
            return saga.event.emit(choice='karaoke', who=saga.cast.eve)

        "Adhesive." if saga.event.peek(choice='glue', who=saga.cast.eve):
            return saga.event.emit(choice='glue', who=saga.cast.eve)
        "Never mind.":

            pass

    jump eve_school_hall1e.outro


label eve_school_hall1e.intro:
    if saga.cast.eve < '13':
        jump eve_school_hall1e.intro1

    if saga.cast.eve < '20':
        jump eve_school_hall1e.intro2

    jump eve_school_hall1e.intro3


label eve_school_hall1e.intro1:
    call shot.school_hall1e_eve
    show eve a_shy at right
    show anon a_wave o_right at left with dissolve
    anon "Afternoon, [saga.cast.eve]."
    eve a_wave "Hey, [saga.cast.anon]."
    anon a_side "What's going on?"
    eve a_shy e_ssw f_nervous "Ehh, not much."
    eve "Just thinking about skipping [saga.cast.barb]' class..."
    show eve e_w
    jump eve_school_hall1e.choice


label eve_school_hall1e.intro2:
    call shot.school_hall1e_eve
    show eve a_shy at right
    show anon a_wave o_right at left with dissolve
    anon "Afternoon, [saga.cast.eve]."
    eve "Hey, [saga.cast.anon]!"
    show eve b_anon p_hug_away at pos.anon
    show anon e_s f_shy p_eve_hug_away
    with dissolve.nowait
    pause
    show anon a_side e_w f_calm -p_eve_hug_away
    show eve f_happy -b_anon -p_hug_away at right
    with dissolve.nowait
    anon "You heading to [saga.cast.barb]' class?"
    eve f_calm "Unfortunately, yes."
    eve "Man, I hope she has something simple planned today..."
    jump eve_school_hall1e.choice


label eve_school_hall1e.intro3:
    call shot.school_hall1e_eve
    show eve a_shy f_happy at right
    show anon a_wave o_right at left with dissolve
    anon "Afternoon, [saga.cast.eve]."
    eve "Hey, [saga.cast.anon]!"
    hide anon
    show eve b_anon p_kiss at pos(.4)
    with dissolve
    pause
    show eve -b_anon -p_kiss at right
    show anon a_pocket o_right at left
    with dissolve
    anon "Mmm, that was nice."
    eve @ e_b m_laugh "Hehe!"
    eve "Are you coming over tonight?"
    anon "I dunno, maybe."
    eve @ e_r f_annoyed "Aww, c'mon... Please?"
    eve "It's so boring when you're not around!"
    jump eve_school_hall1e.choice


label eve_school_hall1e.outro:
    jump eve_school_french.outro
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
