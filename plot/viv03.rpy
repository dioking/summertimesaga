label viv03_setup:
    return


label viv03_setup.viv:
    jump viv02_setup.viv


label viv03_french:
    call shot.school_french_viv
    show old_viv 2 at old_right
    show old_anon 13 at old_left with dissolve
    viv "Bonjour, [saga.cast.anon]!"
    show old_viv 1
    show old_anon 14
    anon "Bonjour, [saga.cast.viv]."
    show old_anon 13
    show old_viv 2
    viv "Comment allez-vous?"
    show old_viv 1
    show old_anon 14
    anon "Oh umm, I'm doing good."
    show old_anon 13
    show old_viv 3
    viv "Wonderful!"
    show old_viv 2
    viv "You're learning the French so quickly!"
    show old_viv 1
    show old_anon 14
    anon "Yeah, I think your tutoring is really helping."
    show old_anon 13
    show old_viv 12
    viv "Ah, we must continue with the lessons then, yes?"
    show old_viv 13
    show old_anon 14
    anon "I'd love to!"
    show old_anon 13
    show old_viv 12
    viv "I am thinking you will enjoy this next assignment..."
    show old_viv 13
    show old_anon 14
    anon "Oh, really?"
    show old_anon 13
    show old_viv 12
    viv "Oui, beaucoup..."
    viv "Are you familiar with French romance?"
    show old_viv 13
    show old_anon 10
    anon "N-no, not really..."
    show old_anon 11 behind old_viv
    show old_viv 16 at pos(.465)
    with dissolve.nowait
    viv "On apprend alors!"
    viv "The French make the best lovers in all the world!"
    show old_viv 17
    show old_anon 26
    anon "... Oh? I didn't know that..."
    show old_anon 13
    show old_viv 16
    viv "Oh oui, [saga.cast.anon], it is known!"
    viv "So to give you insight into this... You are to be writing a romantic poem en Français!"
    show old_viv 17
    show old_anon 10
    anon "Err, I dunno, ma'am. I've never written anything like that before."
    anon "I wouldn't even know how to begin..."
    show old_anon 13
    show old_viv 25 at pos(.446)
    with dissolve
    viv "Ridicule!"
    show old_viv 26 with dissolve
    viv "You're a natural, I have the faith in you, [saga.cast.anon]!"
    show old_viv 27 with dissolve
    show old_anon 14
    anon "Heh. O-okay, [saga.cast.viv]."
    show old_anon 13
    show old_viv 25 with dissolve
    viv "Très bien, mon bel homme!"
    show old_viv 26 with dissolve
    viv "I know you will write something that melts the heart!"
    show old_viv 16 with dissolve
    viv "Return to me when it is done."
    viv "Perhaps you will finally earn the reward you've been seeking, yes?"
    show old_viv 17
    show old_anon 11
    anon "{i}*Gulp*{/i}"
    show old_anon 26
    anon "Y-yeah! Okay!"
    show old_anon 13
    show old_viv 16
    viv "Ça m'excite!"
    show old_viv 17
    show old_anon 14
    anon "I'll be back real soon, [saga.cast.viv]."
    show old_anon 13
    show old_viv 16
    viv "Au revoir, [saga.cast.anon]."
    hide old_viv with dissolve
    show old_anon 3 with dissolve
    anon "( Wow!!! )"
    anon "( Okay, I guess I should head to the library and see what I can find about French poetry and romance. )"
    hide old_anon with dissolve
    return


label viv03_library:
    scene library_lobby at stage
    show old_anon 31 at face_right with dissolve
    anon "( Is that [saga.cast.mia]? )"
    show old_anon 13 with dissolve
    anon "( I wonder what she's doing here? )"
    anon "( I should go and say hi! )"
    hide old_anon with dissolve
    return


label viv03_library.jane:
    show old_anon 10
    anon "Do you have any French poetry?"
    show old_anon 5
    jane @ e_sw "Hmm..."
    jane "Actually..."
    jane "Some girls were here reading something like that yesterday afternoon."
    show old_anon 10
    anon "Really?"
    show old_anon 12
    anon "Did they check it out?"
    show old_anon 5
    jane "No."
    show old_anon 10
    anon "Do you know where it is?"
    show old_anon 5
    jane @ e_sw -m_talk "..."
    jane f_sad "No..."
    jane "But, maybe they'll be here again this afternoon."
    jane "You could ask one of them where they put it."
    show old_anon 12
    show jane f_calm
    anon "Thanks."
    hide old_anon
    with dissolve
    return


label viv03_library.viv:
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 10 at old_left
    anon "Remind me, what was the assignment again?"
    show old_anon 5
    show old_viv 2
    viv "Lequel? Tu as déjà oublié?"
    viv "You are to be writing a romantic poem en Français!"
    show old_viv 1
    show old_anon 14
    anon "Oh, right!"
    anon "Thanks, [saga.cast.viv]."
    show old_anon 13
    show old_viv 2
    viv "Return to me once it's complete."
    viv "Don't keep me waiting, mon bel homme."
    hide old_anon with dissolve

    if saga.prop.book_love in saga.cast.anon:
        scene camera at stage with fade
        show anon a_think e_nw f_pensive with dissolve
        anon @ -m_talk "( Hmm, I should type something up on my computer. )"
        hide anon with dissolve

    return


label viv03_library.work:
    jump viv02_jane.work


label viv03_mia:
    scene library_lobby -mia at stage(.857, .59, 3.5)
    show old_mia 7 at old_left
    show old_anon 14 at old_right with dissolve
    anon "Hey, [saga.cast.mia]! What are you up to?"
    show old_anon 13
    show old_mia 10
    mia "Oh, hello, [saga.cast.anon]! I was just about to study for the upcoming chemistry test."
    show old_mia 7
    show old_anon 12
    anon "I thought your mom didn't allow you to do anything after school?"
    show old_anon 13
    show old_mia 12
    mia "She usually doesn't but..."
    show old_mia 10
    mia "I told her [saga.cast.tori] would write me an academic recommendation if I did well on our next test."
    show old_mia 7
    show old_anon 14
    anon "Will she really do that?"
    show old_anon 13
    show old_mia 10
    mia "Probably not but it doesn't hurt to try, right?"
    mia "And I actually get to hang out with [saga.cast.judith] outside of my house too!"
    show old_mia 7
    show old_anon 14
    anon "Yeah, I suppose not."
    show old_anon 13
    show old_mia 10
    mia "What are you doing here?"
    show old_mia 7
    show old_anon 14
    anon "[saga.cast.viv] gave me an assignment. I thought maybe I could get some inspiration here."
    show old_anon 13
    show old_mia 10
    mia "Oh yeah? What's the assignment?"
    show old_mia 7
    show old_anon 10
    anon "Well, it's kinda embarrassing..."
    show old_anon 5
    show old_mia 9
    mia "Hehe, really?! Well, you have to tell me now!"
    show old_mia 7
    show old_anon 10
    anon "{i}*Sigh*{/i} I'm supposed to write a romantic poem in French."
    show old_anon 5
    show old_mia 10
    mia "That's not embarrassing!"
    show old_mia 7
    show old_anon 12
    anon "No?"
    show old_anon 5
    show old_mia 10
    mia "No! We all had to do that!"
    show old_mia 12
    mia "Well, everyone but [saga.cast.roxxy]... She never does the homework."
    show old_mia 7
    show old_anon 14
    anon "I didn't know. What was your poem about?"
    show old_anon 13
    show old_mia 12
    mia "Oh, I..."
    show old_mia 56 with dissolve
    mia "... You know, this and that, hehe..."
    show old_mia 55
    show old_anon 14
    anon "Aha! See, it is embarrassing!"
    show old_anon 13
    show old_mia 10 with dissolve
    mia "Yeah, I guess it is a little bit."
    show old_mia 7
    show old_anon 10
    anon "I don't even know how to begin writing this thing!"
    anon "I should probably look around for a book on French romance..."
    show old_anon 13
    show old_mia 10
    mia "You know, [saga.cast.judith] and I found a really informative one."
    show old_mia 7
    show old_anon 10
    anon "Oh really?"
    show old_anon 13
    show old_mia 10
    mia "Yeah, it was pretty graphic though..."
    show old_mia 7
    show old_anon 12
    anon "Do you remember what it was called?"
    show old_anon 13
    show old_mia 12
    mia "Hmm, no, not really."
    show old_mia 10
    mia "[saga.cast.judith] had it last, but she left just before you arrived."
    mia "She was using it in the back room there, I think."
    show old_mia 7
    show old_anon 10
    anon "Huh, you think she might have left it in there?"
    show old_anon 13
    show old_mia 10
    mia "Maybe."
    show old_mia 7
    show old_anon 14
    anon "I guess I'll go take a look then. Thanks for the help, [saga.cast.mia]!"
    show old_anon 13
    show old_mia 10
    mia "No problem! Good luck, [saga.cast.anon]!"
    show old_mia 7
    show old_anon 14
    anon "You too!"
    hide old_anon with dissolve
    return


label viv03_mia.rails:
    scene library_lobby at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( I should speak with [saga.cast.mia]... )"
    anon @ -m_talk "( ... She's here quite often and might be able to help me find a book on French Poetry. )"
    hide anon with dissolve
    return


label viv03_book:
    scene library_study -chair at stage(.475, .465, 2, b=0)
    show anon a_think e_sw f_pensive at pos(.75, .85) with dissolve
    anon @ -m_talk "( This must be the book- )"
    anon a_surprised_shrug f_shocked m_open @ -m_talk "!!!" with hpunch

    scene library_study base at stage(.45, .475, 4.2)
    show book_love
    with fade
    anon "Whoa!"
    anon "[saga.cast.mia] was right. This thing is really graphic!"
    anon "Hmm, I wonder what [saga.cast.judith] was doing with it back here in this dark room by herself?"
    anon "..."
    anon "Alright, I had better take this home to my computer and get to writing on that poem for [saga.cast.viv]."
    pause
    return


label viv03_book.rails:
    scene camera at stage
    show anon a_pocket o_right with dissolve

    if saga.cast.anon in saga.sets.library_lobby:
        anon @ -m_talk "( I should check the back room for that book [saga.cast.mia] was talking about. )"
    else:
        anon @ -m_talk "( Well there's certainly {i}a{/i} book here, let's take a look. )"

    hide anon with dissolve
    return


label viv03_jane:
    call shot.library_lobby_jane
    show anon at right with dissolve
    jane "Hey, you managed to find it."
    anon f_happy "Yup."
    anon f_confused "[saga.cast.judith] had it squirreled away in the back room... for some reason."
    jane f_horny "Heh, I bet I know the reason."
    anon @ -m_talk "Hmm?"
    jane f_calm "Enjoy!"
    anon a_wave f_shy "Y-yeah, thanks."
    hide anon with dissolve

    call shot.library_lobby_center
    with fade
    show anon a_backpack_01 e_s f_shy o_right with dissolve
    anon @ -m_talk "( Alright, I had better take this home and start writing that poem. )"
    hide anon with dissolve
    return


label viv03_jane.book:
    scene library_books
    anon "( Yep, that's the book I need to do my French assignment. )"
    anon "( Just need to speak with [saga.cast.jane] to check it out now. )"
    return


label viv03_jane.lobby:
    call shot.library_lobby_center
    show old_mia 10 at old_right
    show old_anon 13 at old_left with dissolve
    mia "Any luck finding it?"
    show old_mia 7
    show old_anon 10
    anon "Yeah, I found it..."
    show old_anon 14
    anon "You weren't kidding, it's really graphic!"
    show old_anon 13
    show old_mia 56 with dissolve
    mia "... Yeah."
    show old_mia 55
    show old_anon 10
    anon "I wonder what [saga.cast.judith] was doing with it back there by herself."
    show old_anon 5
    show old_mia 56
    mia "Heh, y-yeah, I dunno..."
    mia "... But I've gotta get home, I've got bible study in twenty minutes."
    show old_mia 55
    show old_anon 14
    anon "Oh, right! Sorry!"
    anon "Thanks again, [saga.cast.mia]."
    show old_anon 13
    show old_mia 56
    mia "No problem, [saga.cast.anon]."
    hide old_mia with dissolve
    return


label viv03_jane.rails:
    scene camera at stage
    show anon f_worried o_right with dissolve
    anon @ -m_talk "( I need to check the book out so I can take it home. )"
    anon @ -m_talk "( [saga.cast.jane] should be able to take care of that for me. )"
    hide anon wtih dissolve
    return


label viv03_work:
    if saga.time.dusk:
        scene mono debbie_study_night
    else:
        scene mono debbie_study_day

    mono "Writing that poem proved to be unexpectedly difficult. I really struggled to maintain my focus..." with fade
    mono "... But after a several hours and a few... {i}breaks{/i}, I finally managed to put something on paper!"

    scene black
    with dissolve
    return


label viv03_work.dark:
    jump viv02_work.dark


label viv03_printer:
    call shot.school_tech_printer
    show old_anon 518 at old_left with dissolve
    anon "Print!"
    show old_anon 519 with vpunch
    show old_xtra 39 with dissolve
    pause .25
    hide old_xtra with dissolve
    show old_anon 184 with dissolve
    pause
    show old_anon 386 with dissolve
    anon "Alright! Now to hand in my French poem."
    show old_anon 385
    hide old_anon with dissolve
    return


label viv03_printer.viv:
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 14 at old_left
    anon "I finished the poem, [saga.cast.viv]."
    show old_anon 13
    show old_viv 2
    viv "Great, let me see!"
    show old_viv 1
    show old_anon 10
    anon "Oh, I need to print it out first..."
    show old_anon 5
    show old_viv 2
    viv "Well, the printer is in the computer lab, yes?"
    show old_viv 1
    show old_anon 14
    anon "Yup, be right back!"
    hide old_viv
    return


label viv03_viv:
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 386 at old_left
    with dissolve
    anon "Here, [saga.cast.viv]. I finished the poem."
    show old_anon 13
    show old_viv 23
    with dissolve
    viv "Superbe!"
    viv "Oh, comme c'est beau!"
    viv "Yes, this will do nicely."
    viv "The class is in for a treat."
    show old_viv 24
    show old_anon 10
    anon "Huh? What do you mean?"
    show old_anon 5
    show old_viv 2 with dissolve
    viv "Well, you are to be reciting it for the class, yes?"
    show old_viv 1
    show old_anon 11
    anon "!!!" with hpunch
    show old_anon 10
    anon "No way!"
    show old_anon 11
    show old_viv 12
    viv "Quoi? Come now, [saga.cast.anon]."
    viv "Your words are beautiful... It would be wrong not to share such a thing, yes?"
    show old_viv 13
    show old_anon 10
    anon "Absolutely not! I'd be way too embarrassed!"
    show old_anon 22
    show old_viv 2
    viv "Aww, do not be so self-conscious, [saga.cast.anon]."
    show old_viv 11
    pause
    show old_viv 2
    viv "I know! I will be giving you a partner to read with!"
    viv "This is less embarrassing, yes?"
    show old_viv 1
    show old_anon 12
    anon "... Not really."
    show old_anon 23
    show old_viv 19 at face_right with dissolve.nowait
    viv "[saga.cast.roxxy], wake up!"
    show old_anon 22
    show old_viv 18
    roxxy "Hmm?"
    show old_viv 19
    viv "Fille paresseuse! Wake up, I said!"
    show old_viv 18
    roxxy "What?!"
    show old_viv 19
    viv "Come here!"
    show old_viv 20
    pause
    show old_roxxy 27 behind old_anon at face_right, pos(.45)
    show old_anon 24
    show old_viv 19 at face_left
    with dissolve
    viv "Since you cannot be bothered to write a poem for class, you will be reciting one with [saga.cast.anon] here."
    show old_viv 18
    show old_roxxy 30
    roxxy "Uhh, no I won't."
    show old_roxxy 29
    show old_anon 22
    show old_viv 19
    viv "Yes, you will!"
    show old_viv 18
    show old_roxxy 30
    roxxy "I don't care about this stupid assignment!"
    show old_roxxy 29
    show old_viv 19
    viv "Quoi?! Comment oses-tu!"
    viv "You will get up there and read or I will be giving you detention until the end of the term!"
    viv "Comprenez vous?!"
    show old_viv 20
    show old_roxxy 30
    roxxy "Seriously?!"
    show old_roxxy 29
    show old_viv 19
    viv "Now!"
    show old_viv 18
    show old_roxxy 30
    roxxy "Grrr, fine!"
    hide old_roxxy with dissolve
    show old_anon 10 at old_left
    anon "Umm, [saga.cast.viv]?"
    show old_anon 5
    show old_viv 2
    viv "Yes, [saga.cast.anon]?"
    show old_viv 1
    show old_anon 10
    anon "I uhh, really don't want to do this..."
    show old_anon 5
    show old_viv 2
    viv "Aww, but it is so beautiful..."
    show old_anon behind old_viv
    show old_viv 16 at pos(.465) with dissolve
    viv "Do it for me, mon bel homme!"
    show old_viv 26 at pos(.446) with dissolve
    viv "... I'll give you a special reward if you do it..."
    show old_viv 27
    show old_anon 25
    anon "{i}*Sigh*{/i}"
    show old_anon 24
    anon "... Alright, I'll do it."
    show old_anon 5
    show old_viv 12 with dissolve
    viv "Très bien!"
    viv "I'm so proud!"
    show old_viv 1 at face_right
    hide old_anon
    with dissolve
    pause
    show old_viv 2
    viv "Now let's begin! En Français!"
    hide old_viv with dissolve

    scene mono school_french_poem1
    mono "I wasn't exactly excited to recite my poem in front of the class, but, contrary to my expectations, [saga.cast.roxxy]'s involvement took a lot of the pressure off." with fade
    mono "Nobody cared how sappy the poem was; not with [saga.cast.roxxy] busy stumbling over every other word."

    scene mono school_french_poem2 with dissolve
    mono "By the time we reached the end of the recital, [saga.cast.roxxy] was beyond embarrassed; well on her way to a full blown apoplectic fit."
    mono "The dying giggles of our classmates, spawned by her persistently poor pronunciation, only served to further incense her."
    mono "She was incandescent! I don't recall ever seeing her so angry..."

    call shot.school_french_front
    show old_anon 13 at pos(.4), face_right
    show old_roxxy 29 at old_left
    show old_viv 2 at old_right
    with fade
    viv "Très bien!"
    viv "[saga.cast.anon], your French was perfect!"
    show old_viv 1
    show old_anon 14
    anon "Thanks, [saga.cast.viv]."
    show old_anon 13
    show old_viv 19
    viv "... And [saga.cast.roxxy]..."
    viv "... Well, you tried."
    show old_viv 18
    roxxy "Grrr..."
    show old_viv 2 at face_right with dissolve.nowait
    viv "Very well, that is it for today everybody."
    viv "Remember to be completing your homework, and I'll be seeing you tomorrow, yes?!"
    hide old_viv
    with dissolve
    show old_anon 25 at center, face_left with dissolve
    anon "... [saga.cast.roxxy], I'm sorry this-"
    show old_anon 11
    show old_roxxy 3

    if saga.cast.roxxy < 'sex':
        roxxy "Shut up!"
    else:
        roxxy "I HATE HER!!!"

    show old_roxxy 29
    show old_anon 10

    if saga.cast.roxxy < 'sex':
        anon "... I'm just trying to apolo-"
    else:
        anon "... [saga.cast.roxxy], seriously! You have to calm down..."

    show old_anon 11
    show old_roxxy 31

    if saga.cast.roxxy < 'sex':
        roxxy "I SAID SHUT YOUR MOUTH!"
        roxxy "I cannot believe she made me read that sappy bullshit in front of the entire class!"
    else:

        roxxy "CALM DOWN?!"
        roxxy "I'm not gonna calm down!"

    show old_roxxy 30
    show old_anon 24

    if saga.cast.roxxy < 'sex':
        roxxy "Ugh, and with YOU of all people!"
        roxxy "Disgusting!"
        roxxy "You're lucky I don't kick your ass right here and now!"
    else:

        roxxy "That mush mouth bitch gets some kind of sick pleasure out of embarrassing me!"
        roxxy "French skank!"
        roxxy "She's lucky I don't kick her ass right here and now!"

    show old_roxxy 29
    show old_viv 19 at old_right with dissolve
    viv "Que se passe t-il?"
    viv "What is all this yelling?!"
    show old_viv 18
    show old_anon 22 at pos(.4), face_right
    show old_roxxy 30
    with dissolve.nowait
    roxxy "I cannot believe you made me do that!"

    if saga.cast.roxxy < 'sex':
        roxxy "Do you know how embarrassing that was?!"
    else:
        roxxy "Do you know how embarrassed I am?!"

    show old_roxxy 29
    show old_viv 12
    viv "Bah, don't be such a baby..."
    viv "[saga.cast.anon] wrote a beautiful poem!"
    show old_viv 19
    viv "You should be apologizing to him for your clumsy reciting."
    show old_viv 13
    show old_roxxy 31

    if saga.cast.roxxy < 'sex':
        roxxy "Apologize?! To him?! You're outta your damn mind!"
    else:
        roxxy "WHAT?! He's not the one you set up to look ridiculous!"

    show old_roxxy 3
    show old_viv 19
    viv "Shush toi!!"

    if saga.cast.roxxy < 'sex':
        viv "It is not our fault you embarrass yourself with your poor French!"
    else:
        viv "It is not my fault you embarrass yourself with your poor French!"

    viv "You are the one who refuses to do your studies!"
    show old_viv 18
    show old_roxxy 30
    roxxy "Grrrr!!!"
    roxxy "I won't forget this!"
    hide old_roxxy
    show old_anon at face_left
    show old_viv 19
    with dissolve.nowait
    viv "Good! Remember it, as a reason to be taking your studies more seriously!"
    show old_viv 18
    show old_anon 25
    anon "Wow, I've never seen her that mad before..."
    show old_viv 12

    if saga.cast.roxxy < 'sex':
        show old_anon 5 at face_right
        with dissolve.nowait
        viv "Do not concern yourself with her, [saga.cast.anon]."
        viv "She'll get over this."
    else:

        viv "You should speak with her, [saga.cast.anon]."
        viv "Teach her to be more in controlling of her temper..."

    show old_viv 13
    show old_anon 34
    anon "..."
    show old_viv 12

    if saga.cast.roxxy < 'sex':
        show old_anon 5
        viv "Now, I think it's time we start your tutoring, yes?"
    else:

        viv "... But first, we start your tutoring, yes?"
        show old_anon at face_right
        with dissolve.nowait

    show old_viv 13
    show old_anon 14
    anon "Y-yeah! Okay!"
    show old_anon 13
    show old_viv 12
    viv "Très bien! Come and sit with me!"
    show old_anon at face_left
    hide old_viv
    with dissolve

    scene black
    with dissolve
    mono ""

    label viv03_viv.cookie hide:
    call shot.school_french_desks
    show school_french dusk
    show old_desk 16 at old_left
    with dissolve
    viv "Your progress with the French is most impressive, [saga.cast.anon]."
    viv "I think you will do very well on the big exam."
    show old_desk 15
    anon "I hope so! I really need to pass this class."
    show old_desk 19 with dissolve.nowait
    viv "Aww, mon bel homme..."
    show old_desk 20 with dissolve.nowait
    viv "Do not be so anxious..."
    anon "{i}*Gulp*{/i}"
    show old_desk 16 with dissolve.nowait
    viv "You know, I seem to recall promising you a special reward for reciting today, yes?"
    show old_desk 15
    anon "Y-yeah..."
    show old_desk 16
    viv "Your poem really was beautiful, you know?"
    viv "The French language was made for poetry. Don't you think?"
    show old_desk 15
    anon "Y-yes, ma'am."
    show old_desk 16
    viv "I really liked the part you wrote about the kissing."
    show old_desk 15
    anon "Oh... that part?"
    show old_desk 16
    viv "Did you know the French kiss in a special way?"
    show old_desk 15
    anon "Mmm... huh? I mean, they do?"
    show old_desk 16
    viv "Oui, they call it the French kiss and everything..."
    show old_desk 15
    anon "Oh yeah, I've heard of that."
    show old_desk 16
    viv "Have you tried the French kissing before?"
    show old_desk 15

    if saga.cast.debbie < 'kiss':
        anon "N-no..."
        show old_desk 16
        viv "Oh, je dois t'apprendre!"
        show old_desk 15
        anon "... You want to teach me?"
    else:

        anon "Y-yeah, a little bit."
        show old_desk 16
        viv "Oh vraiment?"
        viv "You must show me what you know!"
        show old_desk 15
        anon "Really?"

    show old_desk 16
    viv "Oui."
    show old_desk 27 with dissolve
    pause
    show old_desk 28 with dissolve
    pause
    show old_desk 31_32 with dissolve
    pause
    show old_desk 30 with dissolve

    if saga.cast.debbie < 'kiss':
        viv "Très bien, [saga.cast.anon]..."
        viv "You are a natural at this too it seems."
    else:

        viv "[saga.cast.anon]!"
        viv "I am most impressed!"
        viv "Where did you learn to kiss like this?"

    show old_desk 29

    if saga.cast.debbie < 'kiss':
        anon "Y-yeah, thanks!"
    else:

        anon "Oh, uhh... You know... Here and there..."
        show old_desk 30
        viv "Hehe, fine. Keep your secrets. Just so long as you give me more kisses!"

    show old_desk 31_32 with dissolve
    pause
    viv "Mmm..."
    show old_desk 30 with dissolve
    viv "Mon bel homme..."
    viv "You are getting me all excited..."
    anon "{i}*Gulp*{/i}"
    show old_desk 31_32 with dissolve
    pause
    show old_desk 30 with dissolve
    viv "Perhaps we should be taking this-"
    show old_desk 33 with hpunch
    "*Bzzt*"
    ursula "[saga.cast.viv.name!u]!"
    "*Bzzt*{w=.2} *Bzzt*"
    ursula "Where are you? Did you forget about our meeting?!"
    ursula "Don't make me come down there and drag your scrawny ass to my office!"
    ursula "GET UP HERE THIS INSTANT!"
    "*Bzzt*"
    show old_desk 30
    viv "Sacrebleu! What does she want now?!"
    viv "{i}*Ahem*{/i} I'm sorry, [saga.cast.anon]. It seems we must cut this short once more."
    show old_desk 29
    anon "It's alright, [saga.cast.viv]. I understand."
    show old_desk 31_32 with dissolve
    pause
    show old_desk 30 with dissolve
    viv "Mmm, ta bouche est magique!"
    show old_desk 29
    anon "Huh?"
    show old_desk 30
    viv "Your mouth is magical!"
    show old_desk 29
    anon "Oooh, bouche means mouth?"
    show old_desk 30
    viv "Oui."
    show old_desk 27 with dissolve
    pause
    show old_viv 10 at right
    show old_desk 5
    with dissolve
    viv "I want you to come to my office after classes."
    viv "There's one more thing I want your help with before the exam."
    show old_viv 9
    show old_desk 6
    anon "Sure thing."
    anon "I'll see you later, [saga.cast.viv]."
    show old_desk 5
    show old_viv 10
    viv "Au revoir, mon bel homme."
    hide old_viv with dissolve
    anon "..."
    show old_desk 34
    anon "Phew, that was awesome!"
    return


label viv03_viv.busy:
    jump viv02_viv.busy


label viv03_outro:
    return


label viv03_outro.block:
    call shot.school_office1_door
    show anon a_up f_worried o_right at left with dissolve
    anon @ -m_talk "( Hmmm, no. I'm good. )"
    anon f_worried_surprised @ -m_talk "( I've heard more than enough. )"
    hide anon with dissolve
    return


label viv03_outro.office1:
    call shot.school_office1_door
    show anon f_confused o_right with dissolve
    viv "Madame [saga.cast.ursula.clan], surely this isn't necessary..."
    ursula "Your forgetfulness has inconvenienced me for the last time..."
    show anon f_worried
    ursula "... And I'm afraid, corrective measures must be taken!"
    viv "N-non, madame... this is too much..."
    show anon f_confused
    viv "... I am a grown woman, you cannot-"
    show anon f_worried
    ursula "Grown women don't shirk their responsibilities and inflict endless headaches upon their betters!"
    ursula "In truth, [saga.cast.viv.name], you're nothing but a little girl!"
    show anon f_surprised
    ursula "A stupid, forgetful, {i}bad{/i} little girl!"
    ursula "And what do we do with bad girls, Miss [saga.cast.annie.clan]?"
    show anon a_surprised
    annie "We punish them, [saga.cast.ursula]."
    ursula "Correct."
    show anon a_surprised_up m_teeth
    ursula "Now get your skinny ass over my knee and hike up that skirt!"
    viv "You can't be ser-"
    ursula "Now, [saga.cast.viv.name]... or find yourself a new job!"
    viv "{i}*Sigh*{/i} This is ridiculous." (show_lang="{i}*Sigh*{/i} C'est ridicule.")
    viv "Watch the hosiery it is French sat-"
    show anon a_surprised_up_both f_shocked m_open
    "*Riiiiiip*"
    show anon f_surprised m_teeth
    viv "You bitch!" (show_lang="Connasse!")
    ursula "Be silent and take your medicine!"
    show anon a_rub f_afraid
    "*Whap*"
    viv "Ooff!!"
    ursula "Next time..."
    show anon a_side f_surprised
    "*Whap*"
    viv "Ungh!!"
    ursula "... I give you..."
    show anon a_hug_self e_b f_hurt
    "*Whap*"
    viv "Ow, that hurts!!" (show_lang="Ow, ça fait mal!")
    ursula "... a deadline..."
    show anon e_w f_worried -m_teeth
    "*Whap*"
    viv "Ahhh!!"
    ursula "... you meet it!"
    show anon a_facepalm f_sad
    "*Whap*"
    viv "All right, okay, I'm sorry!!" (show_lang="D'accord, OK, je suis désolé!")
    ursula "Embarrass me in front of the board..."
    show anon a_side
    "*Whap*"
    viv "Ahhh!!"
    ursula "... And this is what happens!"
    show anon f_tired
    "*Whap*"
    viv "No more!" (show_lang="Pas plus!")
    ursula "How many is that?"
    show anon f_surprised
    annie "Oh, was I supposed to be counting?"
    ursula "..."
    annie "Sorry, [saga.cast.ursula]... I think it was five or six?"
    show anon m_teeth
    ursula "Ugh, forget it... We'll just begin again from one."
    viv "W-what?!"
    show anon a_hug_self e_b f_hurt
    "*Whap*"
    show anon e_w f_worried_surprised -m_teeth
    viv "Noooo!!!"
    anon a_side -o_right @ -m_talk "( Holy crap! )"
    anon @ -m_talk "( I guess even the teachers aren't beyond [saga.cast.ursula]'s disciplinary methods! )"
    show anon e_b f_hurt m_teeth
    "*Whap*"
    show anon e_w f_worried_surprised -m_teeth
    viv "{i}*Whimpers*{/i}"
    anon e_osw f_sad @ -m_talk "( Ugh, I can't listen to this anymore... )"
    anon @ -m_talk "( ... Let's get out of here. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
