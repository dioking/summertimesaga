label bar01_intro:
    call shot.school_art_barb
    show old_anon 2 at old_right
    show old_barb 1 at old_left
    anon "Hey, [saga.cast.barb]."
    show old_anon 1
    show old_barb 2
    barb "Well, hello there, [saga.cast.anon]!"
    show old_barb 25 with dissolve
    barb "I heard about your father passing..."
    barb "You poor thing, I've been praying for you."
    show old_barb 24
    show old_anon 2
    anon "Uhh, thanks!"
    show old_anon 1
    show old_barb 25
    barb "Oh, it's no problem, honey."
    barb "You let me know if there's ever anything I can do for you."
    show old_anon 2
    show old_barb 24
    anon "Well, actually, there might be something you can do."
    anon "I need a way to improve my art grade."
    show old_anon 1
    show old_barb 25
    barb "Oh yes, it dropped quite a bit during your absence."
    barb "It's really too bad. You were top of the class before you left..."
    show old_anon 10
    show old_barb 24
    anon "I was?!"
    show old_anon 11
    show old_barb 11
    barb "Aww, don't be modest, [saga.cast.anon]! You have such a talent for art!"
    show old_anon 2
    show old_barb 10
    anon "Heh, yeah, I guess..."
    show old_anon 1
    show old_barb 11
    barb "I'm certain we can come up with some way to improve your grade."
    show old_barb 2 with dissolve
    barb "Hmm, why don't we talk about it after class today?"
    show old_anon 2
    show old_barb 1
    anon "That sounds great! Thanks so much, [saga.cast.barb]!"
    show old_anon 1
    show old_barb 2
    barb "Well, go grab a slab of clay, and take a seat, so we can start the pre-class meditation."
    show old_anon 10
    show old_barb 1
    anon "Meditation?"
    show old_anon 11
    show old_barb 2
    barb "Of course! We have to relax our minds and align our chakras if we want our creativity to flow correctly!"
    show old_anon 10
    show old_barb 1
    anon "Ugh. Yes, ma'am."
    hide old_anon with dissolve
    return


label bar01_clay:
    scene mono school_art_clay1
    mono "Pre-class preditation aside, it felt good to be back in art class again." with fade
    mono "I'd always had a bit of a knack for it, something about it just... {i}clicked{/i}."

    scene mono school_art_clay2 with dissolve
    mono "Sadly, the same couldn't be said for my friends..."

    scene mono school_art_clay3
    more ""

    call shot.school_art_barb
    show old_anon 547 at old_right
    show old_barb 27 at old_left
    with fade
    barb "Goodness, what a cute little giraffe, [saga.cast.anon]!"
    show old_anon 548
    show old_barb 26
    anon "You think so?"
    show old_anon 547
    show old_barb 27
    barb "Simply adorable!"
    show old_barb 13 with dissolve
    barb "It's certainly very... Gifted. Isn't it?"
    show old_anon 10 with dissolve
    show old_barb 12
    anon "Huh?"
    show old_anon 11
    show old_barb 13
    barb "I just mean it's so {i}long{/i} and {i}thick{/i}..."
    show old_anon 2
    show old_barb 12
    anon "... Oh, you mean the neck!"
    show old_anon 1
    show old_barb 11
    barb "Hehe, yeah that too. It's very well done!"
    show old_barb 10
    anon "..."
    show old_barb 11
    barb "So, what are we going to do about these low grades of yours?"
    show old_barb 13
    barb "I can think of more than a few uses for those talented hands..."
    show old_anon 11
    show old_barb 12
    anon "..."
    show old_barb 13
    barb "Maybe we should start with a little after scho-"
    show old_barb 12
    ursula "[saga.cast.barb.clan]!!!" with hpunch
    show old_barb 24
    show old_anon 22
    ursula "Where are you, you quack?!"
    show old_anon 11 at face_right, pos(.37) with dissolve
    show old_ursula 2 at face_left, pos(.9) with dissolve.nowait
    ursula "You'd better not be doing naked meditation agai-"
    show old_ursula 3b at old_right with dissolve.nowait
    pause
    show old_ursula 27 at old_right with dissolve.nowait
    ursula "Oh, there you are!"
    show old_barb 23
    show old_ursula 26
    barb "Excuse me, I'm with a student right now..."
    show old_barb 22
    show old_ursula 27
    ursula "Pfft. He's just gonna have to wait."
    ursula "I need to talk to you about all this stuff you ordered."
    show old_barb 25
    show old_ursula 26
    barb "You mean the art supplies?"
    show old_barb 24
    show old_ursula 27
    ursula "I don't know! Whatever this stuff is, it's not happening!"
    show old_barb 25b
    show old_ursula 26
    barb "B-but..."
    show old_barb 24
    show old_ursula 27
    ursula "Look, it's just not in the budget, [saga.cast.barb.name]."
    ursula "You're going to have to make do without this stuff."
    show old_barb 25
    show old_ursula 26
    barb "[saga.cast.ursula.name], we need those supplies! Our equipment is in shambles!"
    show old_barb 24
    show old_ursula 27
    ursula "I can't give you what I don't have, now can I?"
    show old_ursula 26
    barb "..."
    show old_ursula 28 at old_right with dissolve
    ursula "Just be thankful you still have any budget at all."
    ursula "Do you have any idea how hard it is to sell this hippie crap you teach to the school board?"
    show old_barb 25b
    show old_ursula 26 at old_right with dissolve
    barb "... But art is important to an individual's growth!"
    show old_barb 24
    show old_ursula 27
    ursula "Yeah, sure it is..."
    ursula "The answer is {i}no{/i}, [saga.cast.barb.name]!"
    ursula "You're just gonna have to tough it out."
    hide old_ursula
    with dissolve
    pause
    show old_anon 11 at old_right
    show old_barb 23
    with dissolve
    barb "Arrghh!"
    barb "Every year it gets worse and worse!"
    show old_barb 22
    pause
    show old_mia 12b behind old_anon at pos(.59) with dissolve
    mia "You alright, [saga.cast.barb]?"
    show old_barb 11
    show old_mia 8b
    barb "Oh, hello, [saga.cast.mia] dear."
    show old_barb 10
    show old_mia 12b
    mia "I heard [saga.cast.ursula] yelling at you..."
    show old_mia 8b
    show old_anon 10
    anon "Yeah, it definitely didn't sound good."
    show old_anon 11
    show old_barb 25
    barb "There's just so little budget for art."
    show old_barb 25b
    barb "It gets smaller and smaller each year."
    show old_barb 25
    barb "I'm afraid I might not have a job soon..."
    show old_barb 24
    show old_mia 12b
    mia "Seriously?"
    mia "They can't just cut art class, can they?"
    show old_barb 25
    show old_mia 8b
    barb "I wouldn't put it past [saga.cast.ursula]. She has no respect for the things I teach."
    show old_barb 25b
    barb "If only I could find a way to increase the funding a little..."
    show old_barb 24
    show old_anon 10
    anon "Hmm, how much money would you need?"
    show old_barb 25
    show old_anon 11
    barb "I'm not sure."
    show old_barb 24
    pause
    show old_mia 12b
    mia "Would a thousand dollars help?"
    show old_mia 8b
    show old_barb 25
    barb "Huh? Yeah, that would be plenty to order new equipment, restock the art shelves, and maybe even hire some real models for you kids to paint."
    barb "... But where would we get that kind of money?"
    show old_barb 24
    show old_mia 62 with dissolve
    mia "You could enter the mayor's art contest!"
    show old_mia 63
    show old_barb 11
    barb "[saga.cast.ronald] is hosting an art contest?"
    show old_mia 62
    show old_barb 10
    mia "Yeah, take a look."

    scene school_art base at stage(.2, .685, 14)
    show item_art_flyer
    with fade
    pause
    anon "First place is a thousand dollars, huh?"

    call shot.school_art_barb
    show old_mia 62 at pos(.59)
    show old_anon 2 at old_right
    show old_barb 10 at old_left
    with fade
    anon "[saga.cast.barb], you should enter!"
    show old_anon 1
    show old_barb 27 with dissolve
    barb "Oh heavens, no! I wouldn't have a chance of winning something like that..."
    show old_barb 26
    show old_mia 7 with dissolve
    barb "..."
    show old_barb 27
    barb "... But [saga.cast.anon] might."
    show old_barb 26
    show old_anon 10
    anon "What?!"
    anon "No way! I'm not talented enough for something like that."
    show old_barb 11 with dissolve
    show old_anon 11
    barb "Nonsense! You're the most talented student I've had in a long time!"
    barb "With me guiding you, it's practically a sure thing!"
    show old_barb 10
    show old_mia 9
    mia "Hehe, this is so exciting!"
    show old_mia 10b
    mia "You can do it, [saga.cast.anon]!"
    show old_mia 7
    show old_barb 11
    barb "See, [saga.cast.mia] here believes in you! Let's give it a shot!"
    show old_anon 10
    show old_barb 10
    anon "I dunno..."
    show old_anon 11
    show old_barb 27 with dissolve
    barb "What if I promised to raise your grades?"
    show old_anon 10
    show old_barb 26
    anon "You'd raise my grades?"
    show old_anon 11
    show old_barb 27
    barb "All you have to do is stay late to practice your techniques with me for a few weeks and enter something into the contest."
    barb "You do that and I'll give you an A+!"
    show old_anon 10
    show old_barb 26
    anon "An A+?!"
    anon "Just for entering?"
    show old_anon 11
    show old_barb 27
    barb "That's right. Do we have a deal?!"
    show old_barb 26
    pause
    show old_anon 2
    anon "Yeah, okay. I'll do it!"
    show old_anon 1
    show old_mia 9
    mia "Yay!"
    show old_mia 7
    hide old_anon
    show old_barb 21 at pos(.425)
    with dissolve.nowait
    barb "Oh, I knew you wouldn't let me down, [saga.cast.anon]!"
    barb "Come see me in my office after class, and we'll get started!"
    show old_barb 11
    show old_anon 11 behind old_barb at old_right
    with dissolve
    barb "Alright, [saga.cast.anon]?"
    show old_barb 10
    show old_anon 10
    anon "Okay, [saga.cast.barb]. I'll see you then."
    hide old_anon with dissolve
    return


label bar01_clay.barb:
    call shot.school_art_barb
    show barb a_palette_hold o_right at left
    show anon a_finger at right with dissolve
    anon "I-"
    barb "Go grab a slab of clay, [saga.cast.anon], so we can get started."
    anon f_shy "Yes, ma'am."
    hide anon with dissolve
    return


label bar01_clay.rails:
    scene school_art at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( [saga.cast.barb] wants me to grab a slab of clay and take my seat. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
