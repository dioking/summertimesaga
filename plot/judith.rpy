label judith_school_art:
    jump judith_school_art.intro

    menu judith_school_art.choice:
        "French dictionary." if saga.event.peek(choice='vocab', who=saga.cast.judith):
            return saga.event.emit(choice='vocab', who=saga.cast.judith)

        "Flute." if saga.event.peek(choice='flute', who=saga.cast.judith):
            return saga.event.emit(choice='flute', who=saga.cast.judith)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.judith):
            return saga.event.emit(choice='talent', who=saga.cast.judith)

        "Lenses." if saga.event.peek(choice='lenses', who=saga.cast.judith):
            return saga.event.emit(choice='lenses', who=saga.cast.judith)

        "Photos." if saga.event.peek(choice='photos', who=saga.cast.judith):
            return saga.event.emit(choice='photos', who=saga.cast.judith)

        "Specs." if saga.event.peek(choice='specs', who=saga.cast.judith):
            return saga.event.emit(choice='specs', who=saga.cast.judith)

        "Bathroom fun." if saga.event.peek(choice='stall', who=saga.cast.judith):
            return saga.event.emit(choice='stall', who=saga.cast.judith)

        "Model." if saga.event.peek(choice='model', who=saga.cast.judith):
            return saga.event.emit(choice='model', who=saga.cast.judith)
        "Leave.":

            pass

    jump judith_school_art.outro


label judith_school_art.intro:
    scene school_art -judith at stage
    show judith a_clasp at right
    show anon a_pocket f_shy o_right at left with dissolve
    anon "Enjoying art, [saga.cast.judith]?"
    judith @ f_happy "Yeah!"
    judith "It's one of my favorite subjects."
    anon "Yeah, mine too!"
    judith f_shy "I like it because no matter how bad my drawings are, it's still considered art!"
    anon @ e_b f_happy m_laugh "Heh, good one."
    jump judith_school_art.choice


label judith_school_art.outro:
    hide old_anon
    hide old_judith
    show judith a_clasp at right
    show anon a_wave o_right at left
    anon "See you later, [saga.cast.judith]."
    judith "Bye, [saga.cast.anon]."
    hide anon with dissolve
    return


label judith_school_hall1w:
    jump judith_school_hall1w.intro

    menu judith_school_hall1w.choice:
        "French dictionary." if saga.event.peek(choice='vocab', who=saga.cast.judith):
            return saga.event.emit(choice='vocab', who=saga.cast.judith)

        "Flute." if saga.event.peek(choice='flute', who=saga.cast.judith):
            return saga.event.emit(choice='flute', who=saga.cast.judith)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.judith):
            return saga.event.emit(choice='talent', who=saga.cast.judith)

        "Lenses." if saga.event.peek(choice='lenses', who=saga.cast.judith):
            return saga.event.emit(choice='lenses', who=saga.cast.judith)

        "Photos." if saga.event.peek(choice='photos', who=saga.cast.judith):
            return saga.event.emit(choice='photos', who=saga.cast.judith)

        "Specs." if saga.event.peek(choice='specs', who=saga.cast.judith):
            return saga.event.emit(choice='specs', who=saga.cast.judith)

        "Bathroom fun." if saga.event.peek(choice='stall', who=saga.cast.judith):
            return saga.event.emit(choice='stall', who=saga.cast.judith)

        "Model." if saga.event.peek(choice='model', who=saga.cast.judith):
            return saga.event.emit(choice='model', who=saga.cast.judith)
        "Leave.":

            pass

    jump judith_school_hall1w.outro


label judith_school_hall1w.intro:
    call shot.school_hall1w_judith
    show judith a_clasp f_shy at right
    show anon a_pocket o_right at left with dissolve
    anon "Hey, [saga.cast.judith]!"
    judith "Oh, hey, [saga.cast.anon]."
    judith "How are you doing?"
    anon "Pretty good. How are you?"
    judith f_sad @ e_ssw -m_talk "..."
    judith "Alright I guess."
    jump judith_school_hall1w.choice


label judith_school_hall1w.outro:
    hide old_anon
    hide old_judith
    show judith a_clasp f_shy at right
    show anon a_pocket f_worried o_right at left
    anon @ -m_talk "..."
    judith e_ssw f_sad @ -m_talk "..."
    anon a_uneasy f_calm "Well... I'd better get going!"
    judith e_w f_shy "See you later, [saga.cast.anon]."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
