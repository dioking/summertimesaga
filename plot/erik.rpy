label erik_school_science:
    jump erik_school_science.intro

    menu erik_school_science.choice:
        "Overdue book." if saga.event.peek(choice='book', who=saga.cast.erik):
            return saga.event.emit(choice='book', who=saga.cast.erik)

        "Flute." if saga.event.peek(choice='flute', who=saga.cast.erik):
            return saga.event.emit(choice='flute', who=saga.cast.erik)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.erik):
            return saga.event.emit(choice='talent', who=saga.cast.erik)

        "Karaoke." if saga.event.peek(choice='karaoke', who=saga.cast.erik):
            return saga.event.emit(choice='karaoke', who=saga.cast.erik)

        "Guitar." if saga.event.peek(choice='guitar', who=saga.cast.erik):
            return saga.event.emit(choice='guitar', who=saga.cast.erik)

        "Beer." if saga.event.peek(choice='beer', who=saga.cast.erik):
            return saga.event.emit(choice='beer', who=saga.cast.erik)

        "Lenses." if saga.event.peek(choice='lenses', who=saga.cast.erik):
            return saga.event.emit(choice='lenses', who=saga.cast.erik)

        "Master Blaster." if saga.event.peek(choice='gamepad', who=saga.cast.erik):
            return saga.event.emit(choice='gamepad', who=saga.cast.erik)

        "Model." if saga.event.peek(choice='model', who=saga.cast.erik):
            return saga.event.emit(choice='model', who=saga.cast.erik)
        "Not much.":

            pass

    jump erik_school_science.outro


label erik_school_science.intro:
    call shot.school_science_class
    show old_erik 1 at old_right
    show old_erik labcoat 1 as erik_labcoat at old_right
    show old_anon 2 at old_left with dissolve
    anon "Hey, [saga.cast.erik]!"
    show old_anon 1 at left
    show old_erik 5 at right
    erik "Hey [saga.cast.anon]! What's up?"
    show old_erik 1 at right
    jump erik_school_science.choice


label erik_school_science.outro:
    show old_anon 2
    anon "Oh, not much."
    show old_anon 17
    anon "Just dropping by to say hi!"
    show old_anon 1
    show old_erik 4
    erik "Oh, okay then..."
    show old_erik 1
    show old_anon 29
    with dissolve
    anon "Err... I'll see you later!"
    hide old_anon with dissolve
    return


label erik_tammy_bed2:
    jump erik_tammy_bed2.intro

    menu erik_tammy_bed2.choice:
        "Overdue book." if saga.event.peek(choice='book', who=saga.cast.erik):
            return saga.event.emit(choice='book', who=saga.cast.erik)

        "Flute." if saga.event.peek(choice='flute', who=saga.cast.erik):
            return saga.event.emit(choice='flute', who=saga.cast.erik)

        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.erik):
            return saga.event.emit(choice='talent', who=saga.cast.erik)

        "Karaoke." if saga.event.peek(choice='karaoke', who=saga.cast.erik):
            return saga.event.emit(choice='karaoke', who=saga.cast.erik)

        "Guitar." if saga.event.peek(choice='guitar', who=saga.cast.erik):
            return saga.event.emit(choice='guitar', who=saga.cast.erik)

        "Beer." if saga.event.peek(choice='beer', who=saga.cast.erik):
            return saga.event.emit(choice='beer', who=saga.cast.erik)

        "Lenses." if saga.event.peek(choice='lenses', who=saga.cast.erik):
            return saga.event.emit(choice='lenses', who=saga.cast.erik)

        "Master Blaster." if saga.event.peek(choice='gamepad', who=saga.cast.erik):
            return saga.event.emit(choice='gamepad', who=saga.cast.erik)

        "Model." if saga.event.peek(choice='model', who=saga.cast.erik):
            return saga.event.emit(choice='model', who=saga.cast.erik)
        "Not much.":

            pass

    jump erik_tammy_bed2.outro


label erik_tammy_bed2.intro:
    call shot.tammy_bed2_erik
    show old_erik 1 at old_right
    show old_anon 2 at old_left with dissolve
    anon "Hey, [saga.cast.erik]!"
    show old_anon 1 at left
    show old_erik 5 at right
    erik "Hey [saga.cast.anon]! What's up?"
    show old_erik 1 at right
    jump erik_tammy_bed2.choice


label erik_tammy_bed2.outro:
    jump erik_school_science.outro
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
