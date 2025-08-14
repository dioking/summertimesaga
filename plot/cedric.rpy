label cedric:
    call shot.gym_workout_cedric
    show old_anon 13 at old_right with dissolve
    cedric "What's up, little buddy?"
    show old_anon 14
    anon "Oh, hey [saga.cast.cedric]."
    show old_anon 13
    cedric "You here to bulk up?"

    menu cedric.choice:
        "[saga.cast.jenny]." if saga.event.peek(choice='jenny', who=saga.cast.cedric):
            return saga.event.emit(choice='jenny', who=saga.cast.cedric)
        "What have you been up to?":

            jump cedric.what
        "Can you spot me?":

            jump cedric.spot
        "See ya!":

            pass

    show old_anon 14
    anon "I should get going."
    show old_anon 13
    cedric "Yeah, alright."
    cedric "See you around, little buddy."
    hide old_anon
    with dissolve.nowait
    cedric "Don't go skipping leg day now, heh!"
    return


label cedric.intro:
    call shot.gym_workout_cedric
    show old_anon 13 at old_right with dissolve
    cedric "Whoa, [saga.cast.anon]?"
    show old_anon 14
    anon "Oh, hey [saga.cast.cedric]."
    show old_anon 13
    cedric "I haven't seen you for a while, little buddy."
    show old_anon 14
    anon "Uh huh."
    show old_anon 13
    cedric a_point "You finally decide to hit the gym and bulk up?"
    show cedric a_hips with dissolve
    show old_anon 29 with dissolve
    anon "Y-yeah, something like that..."
    show old_anon 13 with dissolve
    cedric "How's [saga.cast.jenny]?"
    show old_anon 12
    anon "Umm, I dunno... bitchy?"
    show old_anon 13
    cedric "Hahaha, good one!"
    jump cedric.choice


label cedric.spot:
    show old_anon 10
    anon "Can you spot me?"
    show old_anon 13
    cedric a_reject "No can do, little buddy."
    show old_anon 5
    cedric "You're not ready to workout with the big boys yet."
    show cedric a_hips
    anon "..."
    cedric a_point "I don't wanna see you drop a nut or blow out your o-ring."
    show old_anon 10
    show cedric a_hips
    anon "Uh huh, thanks for nothing."
    show old_anon 5
    cedric "Aww, no need to get sore about it."
    cedric "You'll get there soon enough."
    cedric "Check this out!"
    show old_anon 13
    show cedric a_flex
    pause
    cedric "I'm getting pretty ripped, huh?"
    show old_anon 14
    anon "Sure, [saga.cast.cedric]..."
    show old_anon 13
    cedric a_hips "Heh, oh yeah!"
    jump cedric.choice


label cedric.what:
    show old_anon 14
    anon "What have you been up to?"
    show old_anon 13
    cedric "Oh, things have been great!"
    cedric "Since I finally got that harpy roommate of yours off my back, I can finally focus on my workouts."
    show old_anon 4
    anon "Huh."
    show old_anon 14 with dissolve
    anon "Well, that's good... I guess."
    show old_anon 13
    cedric "It's real good, little buddy!"
    cedric a_point_self "You wanna come watch me do some dead lifts?"
    cedric "I'm up to four hundred and five pounds!"
    show cedric a_hips
    show old_anon 29 with dissolve
    anon "Ehh, maybe some other time..."
    show old_anon 13 with dissolve
    cedric "Suit yourself."
    jump cedric.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
