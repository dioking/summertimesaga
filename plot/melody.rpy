label melody_school_lounge:
    call shot.school_lounge_sofa
    show old_melody lounge 5
    show anon a_pocket e_wsw o_right at pos(.25, .95) with dissolve
    anon "Hi there, [saga.cast.melody]."
    show old_melody lounge 3 with dissolve
    melody "[saga.cast.anon]? You know you're not supposed to be in here..."
    show old_melody lounge 2
    anon a_uneasy f_shy "Sorry, just wanted to say \"hi\"."
    show old_melody lounge 3
    melody "Well that's very nice of you, but you had better get out of here before [saga.cast.ursula] sees you..."
    melody "... That woman has no chill."
    show old_melody lounge 2
    anon @ f_worried "Right."
    anon a_wave "I'll see you later!"
    hide anon
    show old_melody lounge 1
    with dissolve
    pause
    show old_melody lounge 1b
    with dissolve
    pause
    return


label melody_school_music:
    jump melody_school_music.intro

    menu melody_school_music.choice:
        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.melody):
            return saga.event.emit(choice='talent', who=saga.cast.melody)

        "Flute." if saga.event.peek(choice='flute', who=saga.cast.melody):
            return saga.event.emit(choice='flute', who=saga.cast.melody)

        "Dress code." if saga.event.peek(choice='hairdye', who=saga.cast.melody):
            return saga.event.emit(choice='hairdye', who=saga.cast.melody)

        "Fool around." if saga.event.peek(choice='office', who=saga.cast.melody):
            return saga.event.emit(choice='office', who=saga.cast.melody)
        "Bye.":

            pass

    jump melody_school_music.outro


label melody_school_music.intro:
    call shot.school_music_melody
    show old_melody 1 at old_left
    show old_anon 2 at old_right with dissolve
    anon "Hi, [saga.cast.melody]."
    show old_melody 2
    show old_anon 1
    melody "Hello, [saga.cast.anon]!"
    melody "Ready to groove with us today?"
    show old_melody 1
    show old_anon 33
    anon "Of course!"
    show old_melody 2
    show old_anon 13
    melody "Is there anything you want to talk about?"
    show old_melody 1
    show old_anon 34
    jump melody_school_music.choice


label melody_school_music.outro:
    show old_anon 10
    anon "Not really..."
    anon "Just hoping I can catch up."
    show old_melody 2
    show old_anon 5
    melody "Oh, honey. You'll be just fiiine!"
    show old_anon 13
    melody "Pick an instrument and take a seat!"
    melody "We'll get you back in the groove..."
    show old_melody 1
    show old_anon 14
    anon "Thanks, [saga.cast.melody]..."
    hide old_anon with dissolve
    return


label melody_school_office4:
    jump melody_school_office4.intro

    menu melody_school_office4.choice:
        "Talent show." if saga.event.peek(choice='talent', who=saga.cast.melody):
            return saga.event.emit(choice='talent', who=saga.cast.melody)

        "Flute." if saga.event.peek(choice='flute', who=saga.cast.melody):
            return saga.event.emit(choice='flute', who=saga.cast.melody)

        "Dress code." if saga.event.peek(choice='hairdye', who=saga.cast.melody):
            return saga.event.emit(choice='hairdye', who=saga.cast.melody)

        "Fool around." if saga.event.peek(choice='office', who=saga.cast.melody):
            return saga.event.emit(choice='office', who=saga.cast.melody)
        "Bye.":

            pass

    jump melody_school_office4.outro


label melody_school_office4.intro:
    call shot.school_office4_melody
    show old_melody 1b at old_right
    show old_anon 14 at old_left with dissolve
    anon "Hello, [saga.cast.melody]."
    show old_anon 13
    show old_melody 2b
    melody "Hey there, [saga.cast.anon]!"
    melody "Did you need something?"
    show old_melody 1b
    jump melody_school_office4.choice


label melody_school_office4.outro:
    show old_anon 14
    show old_melody 1b
    anon "Not at the moment."
    show old_anon 13
    show old_melody 2b
    melody "Alright. Well, have an awesome day!"
    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
