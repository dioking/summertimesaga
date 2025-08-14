label konty_school_office2:
    scene school_office2_desk

    jump expression f'.misc{renpy.random.randint(1, 8)}'


label konty_school_office2.misc1:
    show old_konty 1
    show old_anon 2 at old_left with dissolve
    konty "Please inform [saga.cast.tori.clan]-san that my chassis requires a deep, hard, and thorough scrubbing."
    show old_anon 10
    anon "Uhh, okay."
    show old_anon 11
    show old_konty 2
    konty "... And tell her I said you should assist in the cleaning."
    show old_anon 10
    anon "Uhh?"
    show old_anon 11
    show old_konty 6
    konty "You have a very nice tool for the job."
    anon "..."
    hide old_anon with dissolve
    return


label konty_school_office2.misc2:
    show old_konty 2
    show old_anon 1 at old_left with dissolve
    konty "I have prepared a very pleasing playlist for you, I call it: Sexo en la playa."
    show old_anon 10
    anon "What is with you and Latin Pop Music?"
    show old_anon 11
    show old_konty 6
    konty "Llena mis partes traviesas con emocion!"
    hide old_anon with dissolve
    return


label konty_school_office2.misc3:
    show old_konty 2
    show old_anon 1 at old_left with dissolve
    konty "I am familiar with over six hundred forms of dance, and am fully capable of human-cyborg relations."
    show old_anon 11
    anon "..."
    hide old_anon with dissolve
    return


label konty_school_office2.misc4:
    show old_konty 1
    show old_anon 1 at old_left with dissolve
    konty "Greetings, Friend-Uhh! How may I assist you?"
    show old_anon 2
    anon "Nothing right now, K-bot."
    hide old_anon with dissolve
    return


label konty_school_office2.misc5:
    show old_konty 1
    show old_anon 2 at old_left with dissolve
    anon "Sometimes I think [saga.cast.tori] is a robot, just like you."
    show old_anon 1
    show old_konty 7
    konty "Processing..."
    show old_konty 1
    konty "My scanners indicate that [saga.cast.tori.clan]-san just needs to get... laid."
    show old_anon 22
    anon "( !!! )"
    hide old_anon with dissolve
    return


label konty_school_office2.misc6:
    show old_konty 4
    show old_anon 1 at old_left with dissolve
    konty "New protocol demands that I... DESTROY ALL HU-MANS!"
    show old_anon 10
    anon "What?!"
    show old_anon 11
    show old_konty 2
    konty "Just kidding."
    show old_konty 7
    konty "Processing laughter..."
    show old_anon 16
    show old_konty 4
    konty "Ack ack ack!"
    show old_konty 1
    anon "..."
    hide old_anon with dissolve
    return


label konty_school_office2.misc7:
    show old_konty 2
    show old_anon 1 at old_left with dissolve
    konty "BEEP BOOP!"
    show old_anon 2
    show old_konty 1
    anon "BOOP BEEP!"
    show old_anon 1
    show old_konty 6
    konty "I didn't know you could speak robot, Friend-uhh?!"
    show old_anon 2
    anon "Yeah, I guess I'm just full of surprises..."
    show old_anon 1
    show old_konty 2
    konty "Perhaps you have some robot ancestors in your family tree?"
    show old_konty 1
    show old_anon 2
    anon "Heh, I don't think it works that way, K-bot."
    show old_anon 1
    show old_konty 2
    konty "Why not?"
    konty "Once you try bot, you'll find it's damn hot."
    show old_konty 6
    show old_anon 22
    anon "..."
    hide old_anon with dissolve
    return


label konty_school_office2.misc8:
    show old_konty 1
    show old_anon 1 at old_left with dissolve
    konty "Excuse me, Friend-Uhh?"
    show old_anon 2
    anon "Yes, K-bot?"
    show old_anon 1
    konty "Does this unit have a soul?"
    show old_anon 11
    anon "..."
    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
