label barb_school_art:
    jump barb_school_art.intro

    menu barb_school_art.choice:
        "Contest." if saga.event.peek(choice='contest', who=saga.cast.barb):
            return saga.event.emit(choice='contest', who=saga.cast.barb)

        "Partner." if saga.event.peek(choice='partner', who=saga.cast.barb):
            return saga.event.emit(choice='partner', who=saga.cast.barb)

        "Lessons." if saga.event.peek(choice='lessons', who=saga.cast.barb):
            return saga.event.emit(choice='lessons', who=saga.cast.barb)

        "Magazines." if saga.event.peek(choice='mags', who=saga.cast.barb):
            return saga.event.emit(choice='mags', who=saga.cast.barb)

        "Collage." if saga.event.peek(choice='collage', who=saga.cast.barb):
            return saga.event.emit(choice='collage', who=saga.cast.barb)

        "Easels." if saga.event.peek(choice='easels', who=saga.cast.barb):
            return saga.event.emit(choice='easels', who=saga.cast.barb)

        "Model." if saga.event.peek(choice='model', who=saga.cast.barb):
            return saga.event.emit(choice='model', who=saga.cast.barb)

        "Linens." if saga.event.peek(choice='linens', who=saga.cast.barb):
            return saga.event.emit(choice='linens', who=saga.cast.barb)

        "Costumes." if saga.event.peek(choice='costumes', who=saga.cast.barb):
            return saga.event.emit(choice='costumes', who=saga.cast.barb)

        "Portrait." if saga.event.peek(choice='portrait', who=saga.cast.barb):
            return saga.event.emit(choice='portrait', who=saga.cast.barb)

        "Technique." if saga.event.peek(choice='tech', who=saga.cast.barb):
            return saga.event.emit(choice='tech', who=saga.cast.barb)

        "Fool around." if saga.event.peek(choice='office', who=saga.cast.barb):
            return saga.event.emit(choice='office', who=saga.cast.barb)
        "I should go.":

            pass

    jump barb_school_art.outro


label barb_school_art.intro:
    if saga.cast.barb < 'sex':
        jump barb_school_art.intro1

    jump barb_school_art.intro2


label barb_school_art.intro1:
    call shot.school_art_barb
    show barb a_palette_hold o_right at left
    show anon a_pocket at right with dissolve
    barb "Hello, [saga.cast.anon]..."
    barb "... Have you done something to make yourself happy today?"
    anon f_confused "Ehh."
    jump barb_school_art.choice


label barb_school_art.intro2:
    call shot.school_art_barb
    show barb a_palette_hold o_right at left
    show anon a_pocket at right with dissolve
    barb "There's my little hero!"
    anon "Heh, hey, [saga.cast.barb]."
    barb "Are you busy tonight?"
    barb f_horny "I was hoping you might be interested in some more... {i}private{/i} lessons?"
    barb "I'm just aching to teach you more..."

    menu:
        "Yes.":
            pass
        "No.":

            jump barb_school_art.nope

    anon f_shy "Sure, that sounds awesome!"
    barb f_happy "Wonderful!"
    barb "Just come visit me in my office later today."
    anon "I can't wait!"
    barb f_calm "Now, is there anything else I can help you with?"
    jump barb_school_art.choice


label barb_school_art.nope:
    anon a_rub f_worried "Oh, I can't tonight, [saga.cast.barb]..."
    show barb f_sad
    anon "... I have other plans."
    barb "Aww, that's too bad."
    show anon a_side
    barb "... Just let me know if anything changes."
    show anon f_calm
    barb f_calm "I'll always make time for you, [saga.cast.anon]."
    barb "Is there anything else I can help you with?"
    jump barb_school_art.choice


label barb_school_art.outro:
    anon f_shy "I should probably get a move on."
    barb f_curious "Aww, leaving so soon?"
    anon "Ya, I've got stuff to do."
    barb f_calm "Alright, go in peace, [saga.cast.anon]..."
    hide anon with dissolve.nowait
    barb "... And remember that there's an artist in all of us!"
    return


label barb_school_office3:
    jump barb_school_office3.intro

    menu barb_school_office3.choice:
        "Contest." if saga.event.peek(choice='contest', who=saga.cast.barb):
            return saga.event.emit(choice='contest', who=saga.cast.barb)

        "Partner." if saga.event.peek(choice='partner', who=saga.cast.barb):
            return saga.event.emit(choice='partner', who=saga.cast.barb)

        "Lessons." if saga.event.peek(choice='lessons', who=saga.cast.barb):
            return saga.event.emit(choice='lessons', who=saga.cast.barb)

        "Magazines." if saga.event.peek(choice='mags', who=saga.cast.barb):
            return saga.event.emit(choice='mags', who=saga.cast.barb)

        "Collage." if saga.event.peek(choice='collage', who=saga.cast.barb):
            return saga.event.emit(choice='collage', who=saga.cast.barb)

        "Easels." if saga.event.peek(choice='easels', who=saga.cast.barb):
            return saga.event.emit(choice='easels', who=saga.cast.barb)

        "Model." if saga.event.peek(choice='model', who=saga.cast.barb):
            return saga.event.emit(choice='model', who=saga.cast.barb)

        "Linens." if saga.event.peek(choice='linens', who=saga.cast.barb):
            return saga.event.emit(choice='linens', who=saga.cast.barb)

        "Costumes." if saga.event.peek(choice='costumes', who=saga.cast.barb):
            return saga.event.emit(choice='costumes', who=saga.cast.barb)

        "Portrait." if saga.event.peek(choice='portrait', who=saga.cast.barb):
            return saga.event.emit(choice='portrait', who=saga.cast.barb)

        "Technique." if saga.event.peek(choice='tech', who=saga.cast.barb):
            return saga.event.emit(choice='tech', who=saga.cast.barb)

        "Fool around." if saga.event.peek(choice='office', who=saga.cast.barb):
            return saga.event.emit(choice='office', who=saga.cast.barb)
        "Nothing right now.":

            pass

    jump barb_school_office3.outro


label barb_school_office3.intro:
    if saga.cast.barb < 'sex':
        jump barb_school_office3.intro1

    jump barb_school_office3.intro2


label barb_school_office3.intro1:
    call shot.school_office3_barb
    show barb at right
    show anon o_right at left with dissolve
    barb "Well, hello there, [saga.cast.anon]."
    barb "Nice of you to visit me!"
    anon a_wave "Hey, [saga.cast.barb]."
    barb @ f_curious "What can I do for you?"
    show anon a_side
    jump barb_school_office3.choice


label barb_school_office3.intro2:
    call shot.school_office3_barb
    show barb o_right at left
    show anon a_wave at right with dissolve
    anon "Hey, [saga.cast.barb]!"
    barb a_clasp f_happy "[saga.cast.anon]! It's so good to see you!"
    show anon a_side f_shy
    barb f_horny "... I hope you're here for another private lesson?"
    show barb a_side
    jump barb_school_office3.choice


label barb_school_office3.outro:
    anon f_shy "Oh, I don't need anything."
    anon "Sorry to bother you."
    barb f_calm "It's no bother, [saga.cast.anon]!"
    barb "Helping talented young artists is my specialty after all!"
    anon a_uneasy "Heh, okay."
    anon "I should get going..."
    barb "Aww, alright."
    hide anon with dissolve.nowait
    barb "Bye, [saga.cast.anon]."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
