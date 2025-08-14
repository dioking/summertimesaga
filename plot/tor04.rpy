label tor04_setup:
    return


label tor04_setup.tori:
    anon f_confused "Made any progress with the belt?"
    show old_tori 5
    tori "Not yet, I'm still working on it..."
    show old_tori 4
    anon f_calm "Alright, I guess I'll check back with you tomorrow."
    hide anon with dissolve
    return


label tor04_tori:
    hide anon
    show old_anon 2 at old_left
    anon "Have you made any progress with the belt?"
    show old_anon 1
    show old_tori 2
    tori "I've narrowed the problem down to a few possibilities. Bring me the remote off my desk and I'll show you."
    show old_anon 2
    show old_tori 1
    anon "Sure."
    hide old_anon with dissolve
    pause
    show old_tori 4
    pause
    show old_anon 536 at old_left with dissolve
    pause
    show old_anon 537
    anon "Alright, now wha-"
    show old_anon 536
    ursula "[saga.cast.tori.name]!!!" with hpunch
    ursula "Where are you, you obnoxious little know-it-all?!"
    show old_tori 3
    tori "Oh great..."
    show old_tori 5
    tori "Go sit down, [saga.cast.anon]. I'll deal with her."
    show old_tori 11
    tori "And hide that remote!"
    show old_anon 2 with dissolve
    show old_tori 11b
    anon "Okay, [saga.cast.tori]!"

    scene mono school_science_buzz1
    mono "As [saga.cast.ursula] droned on and on, my mind drifted, and in that moment I'm afraid I let curiosity get the better of me..." with fade
    mono "... But in my defense..."

    scene mono school_science_buzz2 with hpunch
    mono "... How could I have known someone was wearing the belt right then and there?!"
    mono "Poor [saga.cast.tori]."

    scene school_science base at stage(.25, .49, 3.5)
    show old_tori 11b at pos(.375), face_right
    show old_ursula 28 at old_right
    with fade
    ursula "I know you've been working on those stupid devices again behind my back!"
    show old_tori 9
    show old_ursula 29
    tori "I haven't the slightest clue what you're talking about..."
    show old_tori 11b
    show old_ursula 2
    ursula "DON'T LIE TO ME, [saga.cast.tori.name!u]!" with hpunch
    show old_ursula 28 with dissolve
    ursula "Your office is unlocked again and somebody was snooping through my drawers!"
    ursula "I know you had help and I wanna know who it was!"
    show old_tori 11
    show old_ursula 29
    tori "Do you have any-"
    show old_tori 76 with dissolve
    tori "{i}*Gasp*{/i}" with hpunch
    show old_tori 77 with dissolve
    pause
    show old_tori 80
    pause
    show old_tori 77
    tori "Do you have any..."
    show old_tori 78
    ursula "..."
    show old_ursula 27
    ursula "Any what?!"
    ursula "... What's that sound?!"
    show old_tori 79
    show old_ursula 29
    tori "Ahh..."
    show old_tori 77
    tori "Do you have any... any proof?"
    show old_ursula 27
    show old_tori 78
    ursula "Not yet!"
    show old_ursula 28 at right with dissolve
    ursula "But if there's any to be found, you'd better believe I'll find it!"
    show old_ursula 29
    tori "Mmmm."
    show old_tori 79
    tori "Oooohh, haaaaaaah..."
    show old_tori 78
    show old_ursula 27
    ursula "What the hell is the matter with you?!"
    ursula "You're acting even stranger than usual..."
    show old_ursula 29
    tori "Hmm?"
    show old_tori 77
    tori "No, nothing's..."
    show old_tori 79
    tori "... Nothing's..."
    tori "... I'm fine."
    show old_tori 81
    tori "Ooooh, wow!!!"
    show old_tori 78
    show old_ursula 28 at right with dissolve
    ursula "Do I have to remind you that nobody else would hire your arrogant ass?!"
    ursula "This is your last stop, [saga.cast.tori.name]!"
    ursula "After this you'll be working the fast food window for minimum wage!"
    ursula "Do we have an understanding here?!"
    show old_tori 79
    show old_ursula 29
    tori "Yess!! YessSssss!!!"
    show old_tori 81
    tori "AHHHHH!!!"
    tori "YESSSSSSS!!!!"
    show old_tori 81 at pos(y=1.25)
    tori "Oooohh..."
    show old_tori 79 at pos(.41, 1.35)
    ursula "( !!! )" with hpunch
    show old_tori 78
    show old_ursula 27
    ursula "What is with you today?!"
    show old_tori 77
    show old_ursula 29
    tori "Haaah, haaah..."
    tori "Nothing... I just..."
    show old_tori 78
    pause
    show old_tori 77
    tori "Haaah, haaah..."
    tori "I just... don't feel... so good..."
    tori "Need to... go lay down."
    show old_tori 78
    show old_ursula 27
    ursula "Good lord, [saga.cast.tori.name]."
    ursula "Somebody get over here and help [saga.cast.tori] to her office!"
    show old_anon 10 behind old_tori at pos(.265), face_right
    show old_ursula 29
    with dissolve.nowait
    anon "I-I'll do it."
    show old_anon 11
    anon "..."
    show old_ursula 27
    ursula "Well?! Don't just stand there! Get to it!"
    hide old_anon
    show old_ursula 29
    show old_tori 81c
    with dissolve
    pause
    show old_tori 81b at center
    with dissolve
    tori "Oooh, it's too much..."
    tori "I'm gonna..."
    hide old_tori
    show old_ursula 29 at face_right
    with dissolve
    tori "I'M GONNA!"
    show old_ursula 27
    ursula "I'll substitute for today."
    ursula "Enjoy it while it lasts, [saga.cast.tori.name]! I'll have that lock recoded by the end of the week!"
    ursula "This is your last warning and I mean it!"

    call shot.school_office2_entry
    show old_tori 81b at pos(.55)
    with fade
    tori "Haaah!!! Yess!!"
    tori "Oh, I'm gonna..."
    show old_tori 81c
    anon "What is the matter with you?"
    show old_tori 81b
    tori "The remote!!"
    tori "OOOOHHHHH!!!"
    show old_tori 81c
    anon "Huh?"
    show old_anon 11 at old_left
    show old_tori 81
    with dissolve
    tori "Turn it off! Turn it off!"
    show old_anon 10
    show old_tori 78
    anon "Turn what off?"
    show old_anon 11
    show old_tori 79
    tori "THE BELT! TURN IT OFF!"
    show old_anon 10
    show old_tori 78
    anon "You mean you're wearing it now?!"
    show old_anon 11
    show old_tori 79
    tori "YES! SHUT IT OFF! PLEASE!!!"
    show old_anon 29 with dissolve
    show old_tori 78
    anon "I uhh... Kinda left the remote downstairs in my lab coat."
    show old_anon 3
    show old_tori 81
    tori "OOOH! I CAN'T TAKE ANOTHER!"
    show old_tori 81e with dissolve
    tori "HELP ME GET IT OFF!"
    show old_tori 81d
    show old_anon 10 with dissolve
    anon "... You want me to?"
    show old_tori 81e
    tori "GET IT OFF ME NOW!"
    show old_anon 520 at pos(.304)
    show old_tori 81d
    anon "Ahh, right away, ma'am!"
    anon "..."
    anon "Wow, this thing is vibrating like crazy!"
    show old_tori 81e
    tori "HURRY UP!!"
    show old_tori 81d
    pause
    show old_tori 81f
    show old_anon 550 at left
    with dissolve
    anon "Got it!"
    show old_anon 549
    tori "Haaah... Haaah..."
    tori "That was... I've never..."
    tori "Wow!"
    tori "I'm soaked!"
    show old_anon 550
    show old_tori 83
    with dissolve
    anon "Yeah, the belt is all wet too..."
    show old_anon 549
    show old_tori 82
    tori "Haaah... Haaah..."
    tori "I can't feel my legs..."
    show old_tori 84
    tori "Haaah... Haaah..."
    tori "I need to lay down."
    show old_tori 83
    show old_anon 10
    with dissolve
    anon "Can I get you anything?"
    show old_tori 84
    show old_anon 11
    tori "Huh?"
    tori "Oh, no."
    show old_tori 83
    pause
    show old_tori 82
    tori "I'm good. {i}really{/i} good..."
    show old_tori 84
    tori "Just head on back to class. We can speak later."
    show old_anon 10
    show old_tori 83
    anon "S-sure thing."
    hide old_anon with dissolve
    return


label tor04_outro:
    return


label tor04_outro.block:
    call shot.school_office2_door
    show anon a_pocket f_worried with dissolve
    anon @ -m_talk "( I should let her rest for now. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
