label mel01_intro:
    call shot.school_music_melody
    show old_melody 1 at old_left
    show old_anon 14 at old_right with dissolve
    anon "Hey, [saga.cast.melody]."
    show old_anon 13
    show old_melody 2
    melody "Oh my goodness, [saga.cast.anon]! Is that you, sugar?"
    melody "I was starting to think you up and moved to a different school or something!"
    show old_melody 1
    show old_anon 10
    anon "Heh, no. I had some uh, \"family issues\" come up."
    show old_anon 5
    show old_melody 2
    melody "Yeah, I heard about your father passing. Such a shame..."
    melody "Is there anything I can do for you, sugar?"
    show old_melody 1
    show old_anon 10
    anon "Actually, I was hoping we could talk about getting my grade back on track?"
    show old_anon 5
    show old_melody 2
    melody "Well, I betcha we can figure something out."
    melody "Why don't you go pick out an instrument and have a seat."
    melody "We'll get you back in the groove."
    show old_melody 3
    show old_anon 11
    pause
    show old_melody 1
    show old_anon 10
    anon "Alright, any instrument in particular, [saga.cast.melody]?"
    show old_anon 5
    show old_melody 2
    melody "Hmm, how about you give those drums over there a try?"
    show old_melody 1
    show old_anon 14
    anon "Sure thing!"
    hide old_anon with dissolve

    label mel01_intro.cookie hide:
    scene mono school_music_drum1
    mono "I'd never had the chance to play the drums before." with fade

    scene mono school_music_drum2 with dissolve
    mono "It turned out to be pretty difficult to keep a steady rhythm, but also kind of fun..."

    scene mono school_music_drum3
    mono "... So much fun that I {i}may{/i} have gotten a little too over-enthusiastic about the whole thing!" with hpunch

    scene mono school_music_drum4 with dissolve
    mono "It's a good thing [saga.cast.melody] has a sense of humour..."
    more "... Otherwise it could have ended up a {i}lot{/i} more uncomfortable!"

    call shot.school_music_melody
    show old_melody 1 at old_left
    show old_anon 37 at right
    with fade
    anon "I'm so sorry, [saga.cast.melody]!"
    anon "I didn't mean to-"
    show old_anon 3
    show old_melody 2
    with dissolve.nowait
    melody "Hehehe, it's alright, sugar."
    show old_melody 17 with dissolve.nowait
    melody "You aren't the first person to try and beat out a rhythm on these lovely ladies!"
    show old_melody 3
    show old_anon 11
    with dissolve.nowait
    anon "..."
    $ renpy.end_replay()
    show old_anon 5
    show old_melody 2
    melody "Perhaps we should get you on something a little more, elegant?"
    melody "Hmm, the flute maybe..."
    show old_melody 1
    show old_anon 12
    anon "... Eh, the flute?"
    anon "That's kinda girly, isn't it?"
    show old_anon 5
    show old_melody 2
    melody "Oh, lord no, sugar!"
    melody "Men have been playing the flute since the stone ages."
    show old_melody 1
    show old_anon 10
    anon "Really?"
    show old_anon 5
    show old_melody 2
    melody "You better believe it!"
    melody "Ancient armies from all over the world used the flute to keep the rhythm in their battle lines."
    melody "Nothing girly about that, is there?"
    show old_melody 1
    show old_anon 12
    anon "No, I guess not."
    show old_anon 5
    show old_melody 2
    melody "Maybe you should give it some thought then?"
    show old_melody 1
    show old_anon 10
    anon "Maybe..."
    show old_anon 5
    show old_melody 2
    melody "Excuse me, sugar, but I'd better get this class under control."
    hide old_melody with dissolve

    scene mono school_clock_9am
    mono "I spent the whole class trying not to play off tempo..." with fade

    scene mono school_clock_4pm with dissolve
    mono "... Until finally the bell rang."

    call shot.school_music_melody
    show old_melody 2 at face_right
    with fade
    melody "Well done everybody! That was an awesome jam session!"
    melody "Now, before you all head out, I need a moment of your time!"
    show old_melody 14 with dissolve.nowait
    melody "Hey!"
    melody "[saga.cast.tyrone], eyes up front!"
    show old_melody 13
    tyrone "..."
    show old_melody 2 with dissolve.nowait
    melody "Now, I wanted to remind everybody that the musical talent show is coming up, very soon."
    melody "... And we still have a lot of open slots that need to be filled."
    show old_melody 3
    melody "Remember, I'm offering extra credit to everyone that participates."
    anon "!!!"
    show old_melody 2
    melody "I'd really like to see this year's show go off without a hitch!"
    melody "So please, don't hesitate to come and talk to me if you're interested."
    show old_melody 3
    melody "Thanks and have a groovy afternoon, everybody!"
    hide old_melody with dissolve.nowait
    pause
    show old_anon 17 at face_right with dissolve.nowait
    anon "( Extra credit is just what I need! )"
    show old_anon 13
    anon "( I'll do anything to improve my grade at this point. )"
    anon "( I should talk with [saga.cast.melody] about the talent show sometime. )"
    hide old_anon with dissolve
    return


label mel01_office:
    if saga.cast.melody in saga.sets.school_music:
        call shot.school_music_melody
        show old_melody 13 at old_left
        show old_ursula 5 at old_right
    else:

        call shot.school_office4_melody
        show old_melody 13 at old_right
        show old_ursula 5 at old_left

    ursula "You can't seriously be going forward with that pathetic talent show again!"
    show old_ursula 4 with dissolve.nowait
    ursula "Wasn't last year embarrassing enough for you?!"
    show old_ursula 26
    show old_melody 14
    with dissolve.nowait
    melody "Why do you do this every year?!"
    melody "I'm just trying to instill a love of music in these students and every year you shit all over it!"
    show old_melody 13
    show old_ursula 27
    ursula "Aww, poor little [saga.cast.melody.name]."
    ursula "At least you won't have to worry about it much longer..."
    show old_ursula 26
    show old_melody 14
    melody "Ugh, what are you on about now?"
    show old_melody 13
    show old_ursula 27
    ursula "I have a meeting with the school board later today."
    ursula "You see, I told them all about the money you wasted on that joke of a talent show last year..."
    ursula "... And when it flops again this time, they've already agreed to let me reallocate the funding towards worthier endeavors."
    show old_ursula 26
    show old_melody 14
    melody "Worthier endeavors?"
    melody "You can be a real bitch, you know that?"
    show old_melody 13
    show old_ursula 5
    with dissolve.nowait
    ursula "Ha!"
    ursula "I can't wait to see how you screw things up this time..."
    show old_ursula 26
    show old_melody 14
    with dissolve.nowait
    melody "Grrr..."

    if saga.cast.melody in saga.sets.school_music:
        melody "Just get out of my classroom, would ya?!"
    else:
        melody "Just get out of my office, would ya?!"

    show old_melody 13
    show old_ursula 38
    with dissolve.nowait
    ursula "Hahahahaah!"
    hide old_ursula
    show old_melody 12
    with dissolve.nowait
    melody "God, I hate that woman."
    return


label mel01_melody:
    show old_anon 14
    anon "I was hoping I could talk to you about joining the talent show?"
    show old_anon 13
    show old_melody 2
    melody "Oh, well, that's nic-"
    show old_melody 9
    pause
    show old_melody 11
    melody "Wait. Did you just ask about the talent show?!"
    show old_melody 9
    show old_anon 12
    anon "... Yes?"
    show old_anon 5
    show old_melody 3 with dissolve
    melody "Oh my goodness!"
    show old_melody 4 with dissolve
    show old_anon 10
    anon "Uhh, you alright, [saga.cast.melody]?"
    show old_anon 5
    show old_melody 11
    melody "I'm just a bit emotional is all."
    show old_melody 11b
    melody "Mrs. [saga.cast.ursula.clan] is looking for any excuse she can find to cancel the talent show this year."
    show old_melody 12
    melody "... And so far I only have one volunteer."
    show old_melody 10b
    show old_anon 12
    anon "Who?"
    show old_anon 5
    show old_melody 11
    melody "[saga.cast.tyrone]."
    melody "... But I can't just have him play solo the entire time!"
    show old_melody 10
    show old_anon 14
    anon "Well, I'll join and I'll ask around too!"
    show old_melody 4
    anon "Maybe I can find you more volunteers?"
    hide old_anon
    show old_melody 6 at center
    with dissolve
    melody "Oh, bless you, sugar!"
    melody "That would be wonderful!"
    show old_melody 7
    pause
    show old_melody 15

    if saga.cast.melody in saga.sets.school_music:
        show old_anon 14 at face_left, pos(.825)
    else:
        show old_anon 14 at face_right, pos(.175)

    with dissolve
    anon "Heh, it's no problem..."
    show old_anon 13
    show old_melody 3 with dissolve
    melody "Oh, [saga.cast.anon], you just flipped my day right side up again!"
    show old_melody 1
    show old_anon 14
    anon "Glad I could help make you happy!"
    show old_anon 13
    show old_melody 2
    melody "Such a sweet little man..."
    melody "What instrument did you want to play?"
    show old_melody 1
    show old_anon 14
    anon "Well, I dunno. I like the drums."
    show old_anon 13
    show old_melody 8 with dissolve
    melody "Heh, oh yeah. That was quite the little drumming session you had."
    show old_melody 15
    show old_anon 10
    anon "... Again, I'm really sorry about that."
    show old_anon 5
    show old_melody 16
    melody "Don't you worry about it, sugar."
    show old_melody 17 with dissolve
    show old_anon 11
    melody "These ladies have a habit of getting in the way."
    melody "You wouldn't believe how hard they make it for me to play the guitar."
    melody "... I think they just like the attention."
    show old_melody 15 with dissolve
    show old_anon 13
    anon "..."
    show old_melody 5
    melody "Anyway, I'm afraid [saga.cast.tyrone] already signed up to play the drums."
    show old_melody 4
    show old_anon 10
    anon "He did?"
    show old_anon 12
    anon "Hmm, I dunno what to choose..."
    show old_anon 10
    anon "What do you think?"
    show old_anon 5
    show old_melody 5
    melody "Well, how about the flute?"
    show old_melody 4
    show old_anon 12
    anon "Ugh, not this again..."
    show old_anon 5
    show old_melody 8
    melody "Oh, c'mon!"
    show old_melody 5
    melody "There's nothing finer than a man who knows how to handle his flute!"
    show old_melody 4
    anon "..."
    show old_anon 12
    anon "For real?"
    show old_anon 5
    show old_melody 5
    melody "You better believe it!"
    show old_melody 8
    melody "I'll even give you free lessons!"
    show old_melody 4
    show old_anon 10
    anon "You know how to play the flute?"
    show old_anon 5
    show old_melody 16
    melody "Oh, sugar. My skill with the flute is unrivaled!"
    melody "I can work miracles with this mouth!"
    show old_melody 15
    show old_anon 14
    anon "Well, I suppose I could try it if you're willing to give me free lessons."
    show old_anon 13
    show old_melody 16
    melody "I'm more than willing."
    show old_melody 15
    show old_anon 14
    anon "Alright, I guess I'll take the flute then."
    show old_anon 13
    show old_melody 5
    melody "Good decision, [saga.cast.anon]!"
    melody "Let me just go get it. One sec."

    if saga.cast.melody in saga.sets.school_music:
        show old_anon at face_right
    else:
        show old_anon at face_left

    hide old_melody
    with dissolve.nowait
    pause
    show old_anon 55 with dissolve.nowait
    anon "{i}*Yawn*{/i}"
    pause
    show old_anon 13 with dissolve.nowait
    pause

    if saga.cast.melody in saga.sets.school_music:
        show old_anon at face_left
        show old_melody 11 at center, face_right
    else:

        show old_anon at face_right
        show old_melody 11 at center, face_left

    with dissolve.nowait
    melody "Um, well, we did have one."
    show old_melody 11b
    melody "Hmm. I wonder where it went."
    show old_melody 11
    melody "I must have loaned it out earlier this year."
    melody "I guess they never returned it, though."
    melody "Why don't you take a peek at the sign-out sheet in the instrument cabinet."
    show old_melody 4
    show old_anon 14
    anon "Alright! I'll go and have a look!"
    show old_anon 13
    show old_melody 5
    melody "Hurry back, sugar!"
    hide old_anon with dissolve
    return


label mel01_cabinet:
    scene music_cabinet
    pause
    anon "Hmm..."
    anon "It looks like [saga.cast.judith] was the last person to check out the school's flute."
    anon "I guess I'd better track her down!"
    return


label mel01_cabinet.melody:
    show old_anon 10
    anon "Where should I start looking for the flute?"
    show old_anon 5
    show old_melody 2
    melody "Did you check the sign-out sheet in the instrument cabinet?"
    show old_melody 1
    show old_anon 14
    anon "Oh yeah!"
    anon "I'll look there for a clue!"
    show old_anon 13
    show old_melody 2
    melody "Bye, sugar!"
    hide old_anon with dissolve
    return


label mel01_judith(busy):
    hide anon
    hide judith
    show old_judith 1 at right
    show old_anon 10 at old_left
    anon "Do you still have the school's flute?"
    anon "I need it for the talent show."
    show old_anon 5
    show old_judith 2
    judith "Oh, umm..."
    show old_judith 1
    show old_anon 10
    anon "The instrument sign-out sheet had your name next to the flute."
    show old_anon 5
    show old_judith 2
    judith "{i}*Sigh*{/i}"
    show old_judith 3
    judith "I do have it."
    show old_judith 1
    show old_anon 12
    anon "I have a feeling there is a \"but\" coming?"
    show old_anon 5
    show old_judith 3
    judith "{i}But{/i}, I kinda broke it..."
    show old_judith 1
    show old_anon 10
    anon "You broke it?!"
    anon "How did that happen?"
    show old_anon 5
    show old_judith 5
    judith "Heh, well, I accidentally kinda..."
    show old_judith 6
    show old_anon 11
    anon "..."
    show old_judith 2
    judith "... Sat on it."
    show old_judith 1
    show old_anon 10
    anon "You sat on it?"
    show old_anon 11
    show old_judith 3
    judith "... Yeah."
    show old_judith 5
    judith "Which sucks 'cause I was really enjoying it!"
    show old_judith 4
    show old_anon 10
    anon "I didn't know you could play the flute?"
    show old_anon 5
    show old_judith 5
    judith "Oh, I can't play it."
    show old_judith 4
    show old_anon 12
    anon "Well then, I don't understand how you were enjoying it?"
    show old_anon 5
    judith "..."
    show old_judith 5
    judith "Heh, never mind."
    show old_judith 2
    judith "I was hoping no one would ask about it..."
    show old_judith 1
    show old_anon 10
    anon "Maybe I can fix it?"
    show old_anon 5
    show old_judith 4
    judith "..."
    show old_judith 5

    if busy:
        jump mel01_judith.busy

    judith "You can try. It's in my locker."
    label mel01_judith.merge:
    show old_anon 1
    judith "I'll open it for you."
    hide old_judith

    if saga.cast.judith in saga.sets.school_hall1w:
        show old_anon 2 at face_left
    else:

        hide old_anon
        show anon a_surprised o_right p_stand_away at left

    with dissolve.nowait
    anon "Alright, thanks, [saga.cast.judith]."
    hide anon
    hide old_anon
    with dissolve
    return


label mel01_judith.busy:
    judith "You can try. I'll bring to school for you."
    show old_judith 4
    show old_anon 2
    anon "Thanks, [saga.cast.judith]."
    hide old_anon with dissolve
    return


label mel01_judith.melody:
    show old_anon 10
    anon "So I looked at the sign-out sheet and it looks like [saga.cast.judith] had it last."
    show old_anon 5
    show old_melody 2
    melody "Well, have you asked her about it?"
    show old_melody 1
    show old_anon 29
    anon "No... not yet..."
    anon "... I guess I should do that, huh?"
    show old_anon 3
    show old_melody 2
    melody "It's what I would do."
    melody "Good luck, sugar!"
    hide old_anon with dissolve
    return


label mel01_reset:
    return


label mel01_reset.judith:
    anon f_shy "Please, remember to bring that flute to school."
    judith f_shy "O-of course."
    judith "I won't let you down!"
    show judith f_happy of_blush
    anon a_point_pocket "Heh, thanks, [saga.cast.judith], I know you won't."
    hide anon with dissolve
    pause
    judith a_cover_face @ -m_talk "!!!"
    return


label mel01_retry(busy):
    hide anon
    hide judith
    show old_judith 1 at right
    show old_anon 10 at old_left
    anon "Did you remember to bring the flute so I can try fixing it?"
    show old_anon 5

    if busy:
        jump mel01_retry.busy

    show old_judith 5
    judith "Yes, it's in my locker."
    jump mel01_judith.merge


label mel01_retry.busy:
    show old_judith 6
    judith "..."
    show old_judith 2
    judith "Sorry, [saga.cast.anon], I forgot!"
    show old_judith 3
    judith "I- I'll remember it next time, I promise."
    show old_judith 1
    show old_anon 10
    anon "Oh well, thanks, [saga.cast.judith]."
    hide old_anon
    show old_judith 10
    with dissolve.nowait
    judith "..."
    show old_judith 9 with dissolve.nowait
    judith "Great job, [saga.cast.judith]. You're so stupid."
    judith "Now he thinks you're a moron."
    judith "Stupid. Stupid. Stupid."
    return


label mel01_hall1w:
    call shot.school_hall1w_judith
    show judith a_back f_shy o_right at left
    show anon a_pocket at right with dissolve
    judith "H-hi."
    anon f_confused @ -m_talk "..."
    show judith a_clasp e_ssw -o_right at pos(.1)
    judith "Right. Let me just-"
    hide judith with dissolve.nowait
    pause
    judith "T-there you are. It's open..."
    judith "... T-take whatever you want."
    show anon a_surprised f_happy at pos(.4)
    with dissolve.nowait
    anon "Sweet! Thanks, [saga.cast.judith]!"
    hide anon with dissolve
    return


label mel01_hall1w.rails:
    scene camera at stage
    show anon f_happy with dissolve
    anon @ -m_talk "( It's nice to see [saga.cast.judith] get excited sometimes... )"
    anon f_confused @ -m_talk "( ... Even if it is over the weirdest things. )"
    pause
    anon f_calm @ -m_talk "( Don't want to keep her waiting. )"
    hide anon with dissolve
    return


label mel01_flute:
    scene locker_judith
    with dissolvefast.nowait
    anon "( That should be the flute that [saga.cast.judith] borrowed from [saga.cast.melody]. )"

    call shot.school_hall1w_judith
    show old_anon 563 at left, face_left
    with fade
    anon "Wow, this thing really got flattened..."
    anon "It's all bent up!"
    show old_anon 564 with dissolve.nowait
    pause
    show old_anon 565 with dissolve.nowait
    anon "Hmm, it smells funny too."
    show old_anon 564
    show old_erik 5 at old_right
    with dissolve.nowait
    erik "Uhh, what are you doing there, dude?"
    show old_erik 52
    show old_anon 22 at face_right
    anon "!!!" with hpunch
    show old_anon 29 with dissolve.nowait
    anon "N-nothing! You really scared me!"
    show old_anon 14 with dissolve.nowait
    anon "What are you doing?"
    show old_anon 13
    show old_erik 5
    erik "Just heading to my next class..."
    show old_erik 53
    erik "Was that a flute?"
    show old_anon 563
    show old_erik 3c
    with dissolve.nowait
    anon "Y-yeah. Well, it used to be anyways."
    show old_anon 562
    show old_erik 53
    erik "It has definitely seen better days..."
    show old_erik 3c
    show old_anon 563
    anon "I was gonna play it for [saga.cast.melody]'s talent show."
    show old_anon 13 with dissolve.nowait
    show old_erik 5
    erik "Hmm, well, maybe you could build your own?"
    show old_erik 52
    show old_anon 10
    anon "You think?"
    show old_anon 5
    show old_erik 54
    erik "Definitely!"
    show old_erik 4
    erik "I had to build a flute in a video game once."
    erik "All you need is a good piece of wood and a drill to make all the holes."
    show old_erik 1
    show old_anon 12
    anon "You built one in a video game?"
    show old_anon 5
    show old_erik 4
    erik "Totally! I used it to charm all the orc girls in the village!"
    erik "Then we had a giant orgy in the Chief's hut!"
    show old_erik 1
    show old_anon 10
    anon "Oh, that's... nice."
    show old_anon 5
    show old_erik 4
    erik "Heh, dude, it was anything but nice. I can assure you!"
    show old_anon 13
    show old_erik 54
    erik "Green chicks are crazy in the sack!"
    show old_erik 1
    show old_anon 14
    anon "I should probably get busy if I'm going to build a flute from scratch."
    show old_anon 13
    show old_erik 4
    erik "Oh, right. I hear you."
    show old_erik 1
    show old_anon 14
    anon "Thanks, [saga.cast.erik]."
    show old_anon 13
    show old_erik 4
    erik "My pleasure, dude!"
    hide old_erik with dissolve.nowait
    pause
    show old_anon 4 with dissolve.nowait
    anon "( A good piece of wood and a drill... )"

    if saga.prop.tool_drill in saga.cast.anon:
        anon "( ... Well the drill I already have... )"
    else:
        anon "( ... Pretty sure there's an old drill of Dad's in the garage at home... )"

    if saga.prop.misc_stick in saga.cast.anon:
        anon "( ... And maybe that stick I picked up on Raven Hill could work, nice! )"
    else:

        anon "( ... Not sure about the wood though. )"
        pause
        show old_anon 24 with dissolve.nowait
        anon "( Argh, I should have asked [saga.cast.erik] if he had any ideas. )"

    hide old_anon with dissolve
    return


label mel01_flute.rails:
    scene locker_judith
    anon "( The flute is right there! Although, it does look as if it's a bit... used? )"
    return


label mel01_craft:
    scene mono debbie_garage_craft1
    mono "You know, it was oddly satisfying, building a flute by hand. It actually got me pretty excited to play it!" with fade

    scene debbie_garage at stage
    show old_anon 566
    with fade
    anon "There!"
    show old_anon 567
    anon "( Doesn't look all that bad! )"
    pause
    anon "( Let's see what it does when I put my lips on it and blow... )"
    show old_anon 567d with dissolve
    pause
    show old_anon 567 with dissolve
    anon "( Hey, this thing sounds pretty good! )"
    anon "( I bet [saga.cast.melody] is gonna freak out when she sees I built a flute from scratch! )"
    hide old_anon with dissolve
    return


label mel01_craft.erik:
    show old_anon 2
    anon "Remember that thing you said about the flute?"
    show old_anon 11
    show old_erik 4
    erik "Totally! That orgy in the Chief's hut was epic!"
    erik "Flutes are OP, dude!"
    show old_erik 1
    show old_anon 29
    with dissolve.nowait
    anon "Errr... right... but I actually meant the part about how to make one."
    show old_anon 3
    show old_erik 5
    erik "Oh, well in the video game it was easy."
    erik "All you needed was an appropriately sized branch off a tree and a drill."
    show old_erik 52

    if saga.prop.misc_stick in saga.cast.anon:
        show old_anon 14
        with dissolve.nowait
        anon "I have a flute-sized stick that I found up Raven Hill."
        show old_anon 13
        show old_erik 4
        erik "Sounds ideal. You'll need a workbench you can use too."
        show old_erik 1
    else:

        show old_anon 12
        with dissolve.nowait
        anon "A branch off a tree? Can't I just use the lumber at our tree house?"
        show old_anon 5
        show old_erik 5
        erik "Well, you might be able to but I remember in the game they specifically said to look for a fallen branch."
        erik "Something about the instrument needing the spirit energy of the forest to play true."
        show old_erik 52
        show old_anon 14
        anon "That sounds like video game nonsense to me!"
        show old_anon 13
        show old_erik 5
        erik "Hmm, it could be but do you really want to chance it?"
        show old_erik 52
        show old_anon 10
        anon "... No, I guess not."
        anon "So, I should look for a fallen tree branch."

    show old_anon 12
    anon "Then what?"
    show old_anon 5
    show old_erik 5
    erik "Just drill out the center and make some holes on one side."
    show old_erik 52
    show old_anon 14
    anon "Oh yeah!"

    if saga.prop.tool_drill in saga.cast.anon:
        anon "You know, I've been carrying my Dad's old drill around and now it finally has a use!"
    else:
        anon "You know, I think I've seen a drill in our garage."

    show old_anon 13
    show old_erik 4
    erik "Sounds like you've got it all figured out then!"
    show old_erik 1
    show old_anon 14
    anon "Thanks, [saga.cast.erik]!"
    hide old_anon with dissolve
    return


label mel01_craft.item1:
    scene debbie_garage at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( I still need to find a nice piece of wood to turn into a new flute. )"
    anon a_think e_sw f_pensive @ -m_talk "( Maybe [saga.cast.erik] has an idea of where to find one. )"
    hide anon with dissolve
    return


label mel01_craft.item2:
    scene debbie_garage at stage
    show anon f_shy with dissolve
    anon @ -m_talk "( Can't turn this stick into a flute without making some holes. )"
    anon @ -m_talk "( Thankfully, there's that old drill of Dad's on the shelf... )"
    anon e_osw f_sad_happy @ -m_talk "( ... Even if it will be a little weird using it without him... )"
    hide anon with dissolve
    return


label mel01_craft.late:
    scene debbie_garage at stage
    show anon a_rub f_worried o_right at right with dissolve
    anon @ -m_talk "( Damn! I can't see a thing! )"
    anon a_think e_nw f_pensive -o_right @ -m_talk "( And the light fixture is broken! )"
    anon @ -m_talk "( I should come back and work on this during the day... )"
    hide anon with dissolve
    return


label mel01_craft.melody:
    show old_anon 10
    anon "About the flute-"
    show old_anon 11
    show old_melody 2
    melody "Did you find it yet?"
    show old_melody 1
    show old_anon 3
    with dissolve.nowait
    anon "..."
    show old_anon 29
    anon "Not yet."
    show old_anon 3
    show old_melody 2
    melody "I hope it's not lost."
    show old_melody 1
    show old_anon 14
    with dissolve.nowait
    anon "Don't worry! I'm on it!"
    show old_anon 13
    show old_melody 2
    melody "Thanks, [saga.cast.anon]!"
    show old_melody 1
    hide old_anon with dissolve
    return


label mel01_craft.stick:
    scene hill_main at stage(.275, .5, 2)
    show anon a_reach e_s p_bend with dissolve
    anon @ -m_talk "( This wood will do perfectly! )"
    anon a_backpack_01 -p_bend @ -m_talk "( I should work on making the flute in my garage. )"
    hide anon with dissolve
    return


label mel01_outro:
    call shot.school_music_melody
    show old_melody 1 at old_left
    show old_anon 14 at old_right with dissolve
    anon "Hey, [saga.cast.melody]."
    anon "About the school's flute..."
    show old_anon 13
    show old_melody 2
    melody "I knew you'd find it, sugar!"
    show old_melody 1
    show old_anon 10
    anon "... Sort of... I'm afraid it's broken beyond repair."
    show old_anon 5
    show old_melody 11b with dissolve.nowait
    melody "Broken?! What are we gonna do?"
    show old_melody 10b
    show old_anon 14
    anon "Well, I kinda, made one!"
    show old_anon 239_240 with dissolve.nowait
    pause
    show old_anon 567c with dissolve.nowait
    anon "What do you think?"
    show old_anon 567b
    show old_melody 5
    melody "Wow! You made that?!"
    show old_melody 4
    show old_anon 567c
    anon "Yeah, at home in my garage."
    show old_anon 567b
    show old_melody 16
    melody "You're really good with wood, huh?"
    show old_melody 15
    show old_anon 567c
    anon "I know right?"
    show old_anon 567b
    show old_melody 5
    melody "Mind if I take a closer look?"
    show old_melody 4
    show old_anon 567c
    anon "Sure!"
    show old_anon 13
    show old_melody 34
    with dissolve.nowait
    melody "The length and girth are..."
    melody "Perfect."
    melody "When you're done with this flute, I wouldn't mind borrowing it for a night or two!"
    show old_melody 33
    show old_anon 11
    anon "???"
    show old_melody 34
    melody "What? I like breaking in new instruments!"
    show old_melody 33
    show old_anon 14
    anon "Alright, deal."
    anon "I tried playing it earlier. It isn't too hard!"
    show old_anon 13
    show old_melody 40
    with dissolve.nowait
    melody "Great! Here's the sheet music for the concert. Your part shouldn't be too difficult."
    melody "Practice every night and you'll be ready for the concert in no time."
    show old_melody 4
    show old_anon 386
    with dissolve.nowait
    anon "Alright, [saga.cast.melody]. I will!"
    show old_anon 385
    show old_melody 5
    melody "Now, if you don't mind, let's hear what you can do! Class is just about to start."
    show old_melody 4
    show old_anon 386
    anon "Okay."
    hide old_anon with dissolve

    scene mono school_music_becca
    mono "It felt weird to not be part of the percussion section anymore..." with fade
    mono "... But I quickly came to realise that sitting with my fellow flautists in the woodwind section was not without its own unique charms."

    scene black
    with dissolve
    mono ""
    return


label mel01_outro.melody:
    show old_anon 14
    anon "I found the school's flute."
    show old_anon 13
    show old_melody 2
    melody "I knew you would, sugar!"
    show old_melody 1
    show old_anon 10
    anon "Thing is-"
    show old_anon 5
    show old_melody 2
    melody "Just bring it along to our next class and we'll get you all set up."
    melody "New blood is just what our woodwind section needs."
    show old_melody 1
    show old_anon 10
    anon "But-"
    show old_anon 5
    show old_melody 2
    melody "Now get on with you, I'm sure you've got plenty to do. I'll see you in class."
    show old_melody 1
    anon "..."
    show old_anon 36
    anon "Bye, [saga.cast.melody]."
    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
