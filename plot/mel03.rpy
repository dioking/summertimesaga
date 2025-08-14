label mel03_setup:
    return


label mel03_setup.melody:
    "TODO"
    return


label mel03_music:
    scene school_music -melody at stage(.3, .5, 3)
    show old_kevin 23 at pos(.775)
    show old_melody 1 at old_left
    with None
    show old_anon 13 behind old_kevin at pos(.6)
    show old_melody 2
    with dissolve
    melody "Oh good, you're here, [saga.cast.anon]."
    melody "I was just handing out the music sheets."
    show old_melody 1
    show old_anon 10
    anon "Music sheets?"
    show old_anon 5
    show old_melody 2
    melody "For the finale, remember?"
    show old_melody 1
    show old_anon 17
    anon "Oh, right. Yeah, I remember."
    show old_anon 380
    show old_kevin 26
    with dissolve.nowait
    kevin "It's actually a pretty cool song!"
    show old_anon 13
    show old_kevin 23
    with dissolve.nowait
    show old_melody 2
    melody "Heh, well of course it is!"
    show old_melody 3
    melody "Look at who you're working with here, mister!"
    show old_melody 1
    show old_anon 10
    anon "Shouldn't [saga.cast.eve] be here?"
    show old_anon 13
    show old_kevin 24
    kevin "She's here..."
    kevin "... Or well, she was."
    show old_kevin 23
    show old_melody 2
    melody "She went to grab something from her locker."
    show old_melody 1
    show old_anon 14
    anon "Did she like the song too?"
    show old_anon 13
    show old_melody 2
    melody "You better believe it!"
    show old_melody 1
    show old_anon 14
    anon "Looks like everything is going to work out then, huh?"
    show old_anon 13
    show old_melody 2
    melody "Yeah, all thanks to you, sugar!"
    show old_melody 4
    with dissolve.nowait
    show old_kevin 24
    kevin "I can't wait to get up there and start playing! The crowd is gonna love this!"
    show old_kevin 23
    show old_anon 11
    show old_melody 9
    eve "[saga.cast.melody]!"
    show eve a_wtf f_surprised behind old_anon at pos(.425)
    with dissolvefast.nowait
    eve "Guys, come quick! You're not going to believe this!"
    show old_melody 11
    melody "What's that matter, sweetie?"
    show old_melody 10
    eve a_cover f_sad "Someone vandalized the auditorium!"
    show old_kevin 24
    show old_anon 23
    show old_melody 11b
    melody "What?!"
    show old_melody 10b
    eve "Yeah, there's graffiti everywhere!"
    show old_kevin 24 behind old_anon at face_right
    show old_anon 22 at face_right
    show eve o_right
    hide old_melody
    with dissolve.nowait
    pause
    eve a_calm_down f_surprised "C'mon guys!"
    hide old_anon
    hide eve
    hide old_kevin
    with dissolve

    scene mono school_gym_graffiti
    mono "The state of the assembly hall was beyond my wildest imagination..." with fade

    scene school_gym_stage at stage(.5, .75, 2)
    show old_melody 11b at pos(.6)
    show old_anon 22 at face_right, pos(.275)
    show eve a_shy f_sad o_right behind old_anon at pos(.425)
    show old_kevin 23 at face_right, pos(.1)
    with fade
    melody "This is unbelievable!"
    show old_melody 10b
    show old_anon 10
    with dissolve.nowait
    anon "Holy crap, what a mess..."
    show old_anon 11
    show old_melody 11b
    with dissolve.nowait
    melody "It's ruined! I just..."
    melody "I can't believe it!"
    show old_melody 10b
    show old_anon 35b
    show old_kevin 24
    kevin "Who would have done this?"
    show old_kevin 23
    show old_anon 11
    show old_melody 14
    melody "Mrs. [saga.cast.ursula.clan] that's who!"
    show old_melody 13
    show old_kevin 24
    kevin "You think the principal snuck in here and spray painted a dick on the wall?"
    show old_kevin 23
    show old_melody 14
    melody "No."
    melody "... But I betcha that bitch is behind it somehow!"
    melody "She'll do anything she can to get my show canceled!"
    show old_melody 13
    show old_ursula 27 at pos(.85)
    with dissolve.nowait
    ursula "What in the world is going on in here?"
    show old_ursula 26
    show old_melody 14 at face_right
    with dissolve.nowait
    melody "Speak of the devil."
    show old_melody 13
    show old_ursula 27
    ursula "{i}*Gasp*{/i} Who is responsible for this mess?!"
    show old_ursula 26
    eve "We're not sure, ma'am. We just came in and found it this way."
    show old_ursula 27
    ursula "Tsk, I bet it was that one and her little band of hooligans!"
    show old_ursula 26
    eve f_angry @ f_surprised "What?! I didn't have anything to do with this!"
    show old_melody 14
    melody "Mmmhmm."
    melody "You think you're slick but I know you're behind this!"
    show old_melody 13
    show old_ursula 27
    ursula "Why [saga.cast.melody.name], what an awful thing to say!"
    ursula "You think I would vandalize my own school?"
    show old_ursula 26
    show old_anon 16
    show old_melody 14
    melody "Hell yeah, you would!"
    show old_melody 13
    show old_ursula 27
    ursula "Oh, don't be so dramatic..."
    ursula "I'll try and organize a cleaning crew."
    ursula "Though, I'm afraid I won't be able to get one in time for your show."
    ursula "Such a pity..."
    show old_ursula 26
    show old_melody 14
    melody "Grrr!!!"
    show old_melody 13
    show old_ursula 27
    ursula "Oh well, no use crying over spilled milk..."
    ursula "You all have a good day now."
    show old_ursula 38
    ursula "Hahahahaha!"
    hide old_ursula with dissolve.nowait
    melody "..."
    eve f_sad "I swear, I didn't do this, [saga.cast.melody]."
    show old_anon 5
    show old_melody 11b at face_left with dissolve.nowait
    melody "I know, sweetie."
    show old_melody 9f with dissolve.nowait
    pause
    show old_melody 9d with dissolve.nowait
    melody "I just..."
    melody "Excuse me, I need to go collect myself..."
    hide old_melody
    show old_anon 11
    with dissolve.nowait
    eve @ -m_talk "..."
    show old_kevin 24
    show old_anon behind eve at face_left
    show eve o_left at pos(.45)
    with dissolve.nowait
    kevin "Aww, I feel so bad for her."
    show old_kevin 23
    eve "Yeah, me too."
    show old_anon 12
    anon "You guys think Mrs. [saga.cast.ursula.clan] is behind this?"
    show old_anon 5
    show old_kevin 24
    with dissolve.nowait
    kevin "Probably, but what can we do about it?"
    show old_kevin 23
    show eve o_right
    show old_anon 4
    with dissolve.nowait
    pause
    show eve f_surprised a_cover_mouth at pos(.7)
    show old_kevin 20
    with dissolve.nowait
    pause
    hide eve with dissolve.nowait
    eve "No way..."
    show old_anon 10 at face_right
    show old_kevin 24b
    with dissolve.nowait
    anon "What's up [saga.cast.eve]?"
    show old_anon 5
    eve "Come up here!"
    hide old_anon
    hide old_kevin
    with dissolve

    scene school_gym_stage -podium at stage(.65, .375, 2.5, b=0)
    show eve a_hip f_surprised at pos(.8)
    with fade
    show old_kevin 23 at face_right, pos(.45)
    show old_anon 5 at old_left
    with dissolve
    eve a_point "This is water based paint!"
    show old_anon 10
    anon "It is?"
    show old_anon 5
    show old_kevin 24
    kevin "What does that mean?"
    show old_kevin 23
    eve f_happy a_hips "It means, we can wash it off!"
    show old_kevin 24
    kevin "Whoa, really?"
    show old_kevin 23
    eve @ e_b m_laugh "Yeah."
    show old_anon 10
    anon "It'll take a lot of scrubbing though..."
    show old_anon 5
    eve "Which means, we'll need help."
    eve "And I've got an idea!"
    eve "[saga.cast.anon], can you meet me at the park this evening?"
    show old_anon 10
    anon "Yeah, I guess so but why?"
    show old_anon 5
    eve "I think I know where we can get some help!"
    show old_anon 10
    anon "O-okay?"
    show old_anon 5
    eve "Cool, I'll catch you later then."
    hide eve with dissolve
    show old_kevin 24 at face_left with dissolve.nowait
    kevin "I wonder what she's up to?"
    show old_kevin 23
    show old_anon 10
    anon "No idea..."
    show old_anon 5 behind old_kevin
    show old_kevin 19
    with dissolve.nowait
    kevin "Hey, look at this!"
    show old_kevin 20
    show old_anon 108 at face_left
    with dissolve.nowait
    anon "What is it?"
    show old_anon 109
    show old_kevin 21
    kevin "Whoever did this was stupid enough to step in some paint before leaving."
    show old_kevin 19 at face_right with dissolve.nowait
    kevin "Tch, there's a trail."
    show old_kevin 20 behind old_anon
    show old_anon 111 at face_right
    with dissolve.nowait
    anon "You're right!"
    show old_anon 14
    anon "Let's follow it and see where it goes!"
    show old_anon 13
    show old_kevin 9b at face_left with dissolve.nowait
    kevin "Right behind you."
    hide old_anon
    hide old_kevin
    with dissolve
    return


label mel03_music.gym:
    scene school_hall1e at stage(.6, .58, 5)
    show anon a_think f_confused o_right with dissolve
    anon @ -m_talk "( Weird, I've never seen the gym locked before... )"
    anon @ -m_talk "( ... Maybe it's related to the talent show, I should ask [saga.cast.melody]. )"
    hide anon with dissolve
    return


label mel03_catch:
    return


label mel03_catch.rails:
    scene camera at stage
    show anon a_think e_sw f_confused with dissolve
    anon @ -m_talk "( I'm kinda curious about the gym being locked. )"
    anon a_side f_calm e_w @ -m_talk "( [saga.cast.melody] will know if it's about the talent show... )"
    anon @ -m_talk "( She'll almost certainly be in the music room right now. )"
    hide anon with dissolve
    return


label mel03_office1:
    call shot.school_office1_peek
    show old_annie spying 1 behind desk
    show old_ursula spying 2 behind gap
    ursula "You should have seen their faces!"
    ursula "Complete and utter devastation!"
    ursula "Hahaha!"
    show old_ursula spying 1
    show old_annie spying 2
    annie "So, did they believe it was [saga.cast.tyrone] and his gang like you planned?"
    show old_annie spying 1
    show old_ursula spying 2
    ursula "Nah, [saga.cast.melody.name] knows I had something to do with it, but she can't prove anything."
    show old_ursula spying 1
    show old_annie spying 3
    annie "I'm sorry, ma'am. I tried my best to make it look like a bunch of hooligans did it."
    show old_annie spying 1
    show old_ursula spying 2
    ursula "Yes, yes, I'm sure you did."
    ursula "I just can't get that image out of my mind!"
    ursula "Poor little [saga.cast.melody.name] on the verge of tears."
    ursula "Her silly talent show in shambles!"
    show old_ursula spying 3
    ursula "Mmm..."
    show old_ursula spying 2
    ursula "It's actually getting me kinda worked up."
    ursula "Why don't you come over here and help me out."
    show old_ursula spying 1
    show old_annie spying 3
    annie "Of course, ma'am."
    show old_annie spying 4
    show old_ursula spying 4
    with dissolve
    pause
    show old_annie spying 5 with dissolve
    pause
    show old_ursula spying 3
    ursula "Ahh, that's it."
    ursula "Good girl..."
    ursula "Hehehehe, I can't wait to see the look on her face when I tell her the board has pulled her funding!"

    call shot.school_office1_door
    show old_kevin 24 at old_left
    show old_anon 107 at pos(y=1.2), face_right
    with fade
    kevin "Bro, Mrs. [saga.cast.ursula.clan] {i}was{/i} behind it!"
    show old_kevin 23
    anon "..."
    show old_kevin 24
    kevin "What a mega bitch!"
    kevin "We have to say something!"
    show old_kevin 23
    anon "..."
    show old_kevin 24
    kevin "[saga.cast.anon]?"
    kevin "[saga.cast.anon]?!"
    show old_kevin 23
    pause 1
    show old_kevin 25 at pos(.35) with hpunch
    kevin "Bro!"
    show old_kevin 23
    show old_anon 12 at pos(.6, 1.), face_left
    with dissolve.nowait
    anon "Hey! Chill out, man!"
    show old_anon 5
    show old_kevin 24
    kevin "I'm trying to talk to you!"
    show old_kevin 23
    show old_anon 12
    anon "Well, I'm sorry but did you see what they're doing in there right now?!"
    show old_anon 5
    show old_kevin 24
    kevin "Uh, yeah and it's super gross!"
    kevin "Mrs. [saga.cast.ursula.clan] is the devil man, I bet her coochie smells like brimstone and sulfur!"
    show old_kevin 33
    show old_anon 107 at pos(.5, 1.2), face_right
    with dissolve.nowait
    anon "[saga.cast.annie] doesn't seem to mind..."
    show old_kevin 33b
    kevin "C'mon, it's getting late and you're supposed to meet [saga.cast.eve] in the park, remember?!"
    show old_kevin 33
    anon "Uh huh, just five more minutes..."
    show old_kevin 36
    kevin "Let's go, before we get caught, ya perv!"
    hide old_kevin
    hide old_anon
    with dissolve
    return


label mel03_office1.rails:
    scene camera at stage
    show anon a_pocket f_sceptical o_right at left with dissolve
    anon @ -m_talk "( The trail doesn't lead that way. )"
    hide anon with dissolve
    return


label mel03_outro:
    call shot.school_office4_melody
    show old_melody 9f at old_right
    show old_anon 10 at old_left with dissolve
    anon "[saga.cast.melody], you in here?"
    show old_anon 11
    show old_melody 9d
    with dissolve
    melody "Yeah, I'm right here, sugar."
    show old_melody 9c
    show old_anon 10
    anon "You alright?"
    show old_anon 11
    show old_melody 9d
    melody "Oh, I'll be okay. I'm just a little down in the dumps at the moment."
    show old_melody 9f
    show old_anon 25
    with dissolve
    anon "( Hmm, I guess I should give her some space for the time being. )"
    hide old_anon with dissolve
    return


label mel03_outro.office1:
    call shot.school_office1_peek
    show old_annie spying 5 behind desk
    show old_ursula spying 3
    ursula "You're getting pretty good at this, my little pet."
    ursula "Mmm, right there!"
    ursula "Ahh!"
    return


label mel03_outro.rails:
    scene camera at stage
    show anon a_pocket e_nw f_pensive o_right at left with dissolve
    anon @ -m_talk "( I should check on [saga.cast.melody]. )"
    hide anon with dissolve
    return


label mel03_post:
    return


label mel03_post.block:
    scene camera at stage
    show anon a_pocket e_nw f_pensive o_right at left with dissolve
    anon @ -m_talk "( I'm sure [saga.cast.melody] will bounce back, she just needs a little time. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
