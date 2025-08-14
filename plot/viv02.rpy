label viv02_setup:
    return


label viv02_setup.viv:
    anon f_confused "Ready for another one-on-one tutoring session, [saga.cast.viv]?"
    viv "Non, [saga.cast.anon]... there is simply too much to be doing, I'm afraid."
    show anon f_shy
    viv "Keep up with your studies and we will get back to our tutoring soon, yes?"
    anon "Y-yeah, okay."
    hide anon with dissolve
    return


label viv02_french:
    call shot.school_french_viv
    show old_viv 4 at old_right
    show old_ursula 28 at old_left
    ursula "[saga.cast.viv], I was expecting your midterm report on my desk this morning."
    show old_ursula 29
    show old_viv 15
    with dissolve
    viv "Je suis désolée! It completely slipped my mind!"
    show old_viv 4 with dissolve
    show old_ursula 27
    ursula "Yes, well, I want it in my hands by the end of the day!"
    show old_ursula 28 with dissolve
    ursula "... And there had better be an improvement over last term's grade point average!"
    ursula "The city isn't going to keep funding us if our students are all failing their classes!"
    show old_ursula 29 with dissolve
    show old_viv 5
    viv "Oui, Madame [saga.cast.ursula.clan]. I've devised a new method to inspire the students."
    viv "Surely, it will raise their interest in the French class."
    show old_viv 4
    show old_ursula 27
    ursula "Hah! You couldn't inspire a dog to bark..."
    show old_ursula 29
    show old_viv 19
    viv "Mais, madame... Surely you-"
    show old_viv 18
    show old_ursula 27
    ursula "Just get me that report or I'll ship your smelly ass back to whatever French shithole you crawled out of!"
    show old_ursula 28 with dissolve
    ursula "Am I understood?!"
    show old_ursula 29 with dissolve
    show old_viv 5
    viv "... O-oui, Madame [saga.cast.ursula.clan]."
    hide old_ursula with dissolve
    show old_viv 20
    pause
    show old_viv 19 at center with dissolve
    viv "Vieille chienne en colère!"
    show old_viv 18 at face_right with dissolve
    pause
    show old_anon 10 at old_left with dissolve
    anon "[saga.cast.viv]?"
    show old_anon 5
    show old_viv 5 at face_left
    with dissolvefast.nowait
    viv "Oh mon dieu!"
    show old_viv 1
    show old_anon 11
    anon "..."
    show old_viv 3
    viv "[saga.cast.anon], you frightened me!"
    show old_viv 1
    show old_anon 10
    anon "Sorry..."
    show old_anon 12
    anon "Is everything alright?"
    show old_viv 4
    anon "I could hear Mrs. [saga.cast.ursula.clan] from down the hall..."
    show old_anon 5
    show old_viv 5
    viv "Oui. She is just wanting to see you students take more interest in the French."
    show old_viv 4
    show old_anon 12
    anon "Well, she didn't have to be so mean about it."
    show old_anon 5
    show old_viv 3
    viv "Oh, [saga.cast.anon]. You're always so sweet to me..."
    show old_viv 17 at pos(.465)
    show old_anon 11 behind old_viv
    with dissolve.nowait
    anon "!!!"
    show old_viv 16
    viv "You know, I've been wanting to speak with you about the next assignment for your tutoring sessions."
    show old_viv 17
    anon "{i}*Gulp*{/i}"
    show old_anon 10
    anon "Alright, what did you have in mind?"
    show old_anon 5
    show old_viv 16
    viv "I want you to write a few paragraphs about your favorite food, en Français."
    viv "Then we will go over it together, yes?"
    show old_viv 17
    show old_anon 14
    anon "Sounds good to me."
    show old_anon 13
    show old_viv 16
    viv "... And if you write well..."
    viv "Perhaps, I will be giving you a taste of my special reward, yes?"
    show old_viv 17
    show old_anon 14
    anon "Y-yeah, okay!"
    show old_anon 13
    show old_viv 3
    with dissolve.nowait
    viv "Très bien! You had best be getting started then."
    viv "Au revoir, [saga.cast.anon]!"
    hide old_viv with dissolve
    show old_anon 4 with dissolve.nowait
    anon "( I wonder what the reward could be? )"
    anon "..."
    show old_anon 34 with dissolve
    anon "( ... And what food should I write about? )"
    show old_anon 13 with dissolve
    anon "( Time to visit the library again, I guess. )"
    anon "( That librarian was really helpful. Maybe she could find a book about French food for me? )"
    hide old_anon with dissolve
    return


label viv02_jane:
    show old_anon 14
    anon "I was wondering if you had any books in French about food?"
    show old_anon 13
    show jane f_happy
    jane @ e_b m_laugh "That's an interesting subject..."
    show jane f_calm
    show old_anon 14
    anon "Yeah, I need it for a school assignment."
    show old_anon 13
    jane "Alright, let me look and see what we have."
    jane e_sw @ -m_talk "..."
    show old_anon 11
    anon "..."
    show old_anon 5
    jane "Hmm, we don't appear to have anything like that."
    show jane e_w
    show old_anon 12
    anon "Nothing?"
    show old_anon 5
    jane e_sw "No... Oh, wait a second!"
    jane "It's saying our sister branch has a French book about cheese."
    jane e_w "Would that work?"
    show old_anon 14
    anon "Sure, I love cheese! Where do I need to pick it up?"
    show old_anon 13
    jane "I can request them to send it here. Should only take a few days..."
    jane "In the meantime, I wonder if you could you help me out with something?"
    show old_anon 10
    anon "... Sure, I suppose. What is it you need?"
    show old_anon 5
    jane "Some of your classmates have overdue books I'd like returned."
    jane "I've been sending letters to their homes but that doesn't seem to be working."
    jane "I'd hate to lose the books."
    show old_anon 10
    anon "Yeah, I could try speaking with them. What are their names?"
    show old_anon 5
    jane e_sw "Hmm, the first is a Miss [saga.cast.camila.clan]."
    jane "The second is a Mr. [saga.cast.erik.clan]-"
    show jane e_w
    show old_anon 14
    anon "[saga.cast.erik] has a book out?!"
    anon "Those should be easy."
    show old_anon 13
    jane e_sw "... And finally..."
    jane "Huh. It just says [saga.cast.dexter]."
    jane "Ring any bells?"
    show jane e_w
    show old_anon 12
    anon "Oh man, not [saga.cast.dexter]... You're sure?"
    show old_anon 11
    jane "That's what the log says..."
    show old_anon 12
    anon "Crap! Alright, I'll see what I can do."
    show old_anon 5
    jane @ e_b f_happy m_laugh "Thanks, I really appreciate this!"
    hide old_anon with dissolve

    call shot.library_lobby_center
    with fade
    show anon f_sceptical o_right with dissolve
    anon @ -m_talk "( Ugh, why did it have to be [saga.cast.dexter]? )"
    pause
    anon e_osw f_sad "{i}*Sigh*{/i}"
    hide anon with dissolve
    return


label viv02_jane.viv:
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 10 at old_left
    anon "What was my next assignment?"
    show old_anon 5
    show old_viv 2
    viv "I want you to write a few paragraphs about your favorite food, en Français."
    viv "Then we will go over it together, yes?"
    show old_viv 1
    show old_anon 14
    anon "Oh, yeah!"
    anon "Thanks, [saga.cast.viv]!"
    hide old_anon with dissolve

    scene camera at stage with fade
    show anon a_think e_nw f_pensive with dissolve

    if saga.prop.book_cheese in saga.cast.anon:
        anon @ -m_talk "( Hmm, I should type something up on my computer. )"
    else:

        anon @ -m_talk "( Perhaps I should visit that librarian again... )"
        anon @ -m_talk "( ... Maybe she could find a book about French food for me. )"
        pause
        anon a_side e_w f_calm @ -m_talk "( Then I can type something up at my computer. )"

    hide anon with dissolve
    return


label viv02_jane.work:
    scene debbie_bed3 at stage
    show old_anon 73 with dissolve
    anon "( I first need to get the right book before I can finish my homework... )"
    anon "( I can probably find it at the local library. )"
    hide old_anon with dissolve
    return


label viv02_books(test):
    if test == 2:
        show anon f_worried with dissolve
        anon @ -m_talk "( Well, two more books to go. )"

    elif test == 1:
        show anon f_shy with dissolve
        anon @ -m_talk "( Just one book left. )"
    else:

        show anon f_happy with dissolve
        anon @ -m_talk "( Great! That's the last book! )"
        anon @ -m_talk "( Now, I just need to return them to the library! )"

    hide anon with dissolve
    return


label viv02_books.bag:
    scene mono school_shower_spy
    mono "My heart raced as I quietly snuck the book out of [saga.cast.camila]'s backpack. The certainty that they would tear me to pieces if I was caught did nothing for the stability of my hands." with fade

    scene mono school_shower_latinas1
    mono "A final cursory glance into the shower revealed that I needn't have worried. It seemed the girls were quite happy to create their own distraction!" with fade

    scene mono school_shower_latinas2 with dissolve
    mono "Of course, if they found out I was watching I truly would be dead..."
    more "... But it wasn't an easy scene to walk away from!"
    mono "They really did do {i}everything{/i} together..."

    scene school_boys at stage(.75, .5, 2)
    with fade
    show anon f_worried with dissolve
    anon "( ... I had better get out of here before they notice me. )"
    anon "( I hope I got the right book... )"
    $ renpy.end_replay()

    scene school_boys base at stage(.1, .9, 5)
    show book_style
    with fade
    anon "Chola's Tricks?"
    anon "..."
    anon "What the heck is a chola?!"

    call shot.school_hall1w_boys
    with fade
    return


label viv02_books.block:
    call shot.school_hall1w_boys
    show anon a_surprised f_surprised m_teeth o_right with dissolve
    anon @ -m_talk "( As steamy as that was, it's not worth getting murdered over! )"
    anon a_surprised_shrug f_afraid @ -m_talk "( I can only imagine the hell they'd put me through if I got caught! )"
    hide anon with dissolve
    return


label viv02_books.boys:
    scene school_boys at stage
    show old_anon 13 at face_left with dissolve
    anon "( Aha, there's [saga.cast.camila]'s backpack! )"
    anon "( They must be showering... )"
    anon "..."
    anon "( This is my chance. )"
    anon "( Remember, [saga.cast.anon], sneaky! )"
    hide old_anon with dissolve
    return


label viv02_books.dexter:
    show old_anon 10

    if saga.cast.dexter < 'book':
        anon "I was hoping you still had the library book you checked out..."
    else:
        anon "Did you remember where you left the library book you checked out..."

    show old_anon 5
    show old_dexter 8
    dexter "Library book?"

    if saga.cast.dexter < 'book':
        show old_dexter 6
        show old_anon 11
        with dissolve.nowait
        dexter "Do I look like the kinda guy who would be reading library books?"
        dexter "... What do you think I'm some kinda nerd like you and your douchebag ginger friend?"
        show old_dexter 2
        show old_anon 10
        with dissolve.nowait
        anon "What? No, I didn't..."

    show old_anon 11
    show old_dexter 4
    with dissolve.nowait

    if saga.cast.dexter < 'book':
        dexter "You better get outta here, [saga.cast.anon], before I feed you a knuckle sandwich!"
    else:

        dexter "Didn't I tell you to get outta here, [saga.cast.anon]?"
        dexter "Or do you want a knuckle sandwich!"

    show old_dexter 2
    show old_anon 12
    with dissolve.nowait
    anon "Alright, alright, I'm going!"
    hide old_anon with dissolve

    scene court_main at stage with fade
    show old_anon 11 at face_right with dissolve
    anon "( I wonder if the librarian made a mistake? )"
    show old_anon 5
    anon "..."
    show old_anon 4
    anon "( He could be lying. I should check his locker! )"
    show old_anon 5
    anon "( Hopefully it's in there, otherwise, I dunno what I'm gonna do... )"
    hide old_anon with dissolve
    return


label viv02_books.erik:
    show old_anon 10
    anon "I'm trying to check out a book for school but the librarian has me running errands."
    anon "She said you had a book that's overdue, and I was hoping I could get it from you."
    show old_anon 5
    show old_erik 3b
    erik "I do?"
    show old_erik 3
    erik "I don't remember-"
    show old_erik 4
    erik "Ohhh wait, that's right!"
    erik "I did check one out..."
    show old_erik 3b
    erik "... I have no idea where it could be though. Crap!"
    show old_erik 2

    if renpy.showing('erik_labcoat'):
        show old_erik labcoat 2 as erik_labcoat

    with dissolve.nowait
    pause
    show old_erik 3b

    if renpy.showing('erik_labcoat'):
        show old_erik labcoat 1 as erik_labcoat

    with dissolve.nowait

    if saga.cast.erik in saga.sets.tammy_bed2:
        erik "I remember reading it in here..."
    else:
        erik "I remember reading it in my room..."

    show old_erik 3
    erik "... Urrgh, but I have no idea where it could have gotten to."
    show old_erik 3b
    erik "Sorry, [saga.cast.anon]."
    show old_erik 52
    show old_anon 14
    anon "It's alright, I'll look around for it."
    show old_anon 13
    show old_erik 4
    erik "Okay, good luck, dude!"
    hide old_anon with dissolve
    return


label viv02_books.hall1w:
    call shot.school_hall1w_judith
    show camila a_backpack at pos(.65)
    show val a_hips f_annoyed at pos(.8)
    show anon a_pocket f_worried o_right at left with dissolve
    anon "Hey, [saga.cast.camila]?"
    camila "... What do you want, culo?"
    val "Yeah! What do you want?"
    anon "Uhh, I heard you had a book that's overdue from the library."
    camila f_angry "What, are you stalking me or something, white boy?"
    anon "Huh? No, the librarian sent me!"
    val "So, you're just the librarian's little bitch?"
    show anon f_confused
    camila @ e_b f_happy m_laugh "Haha!"
    show camila f_calm
    anon "What? No, she ordered a book for me and asked if I could talk to you guys in return."
    camila f_angry "Whatever, bitch! We ain't got time for this..."
    show anon e_sw f_surprised
    show camila f_calm p_stand_back at pos(.625)
    show val f_calm behind camila
    camila "C'mon, [saga.cast.val]. We gotta get ready for gym class."
    val "Sure thing, [saga.cast.camila]."
    show anon e_w
    hide camila
    with dissolve.nowait
    val f_annoyed "Later, culo!"
    hide val with dissolve.nowait
    val "Hahaha!"
    pause
    anon a_think e_sw f_pensive @ -m_talk "( I bet that was it in her backpack! )"
    anon e_w @ -m_talk "( I should try and grab it while they are showering. They probably wouldn't even realize it's gone. )"
    anon a_side e_b f_happy m_teeth @ -m_talk "( I just have to be sneaky... )"
    hide anon with dissolve
    return


label viv02_books.jane:
    show old_anon 10
    anon "What were the students names again?"
    anon "You know, the ones with the overdue books."
    show old_anon 5
    jane "One second..."
    jane @ e_sw "Hmm, Miss [saga.cast.camila.clan], Mr. [saga.cast.erik.clan], and a \"[saga.cast.dexter]\"."
    show old_anon 14
    anon "Ahh, [saga.cast.camila], [saga.cast.erik], and [saga.cast.dexter]..."
    anon "Alright, I'm on it."
    hide old_anon with dissolve
    return


label viv02_books.maths:
    scene locker_dexter at stage
    show book_maths
    with dissolvefast
    anon "( Quick mafs? )"
    anon "( This is a book for little kids... )"
    anon "( Hah, I guess it matches his mafs- )"
    anon "( Math level! )"
    anon "( I need to get out of here! )"
    anon "( Something about being next to [saga.cast.dexter] or his stuff is making me dumber! )"

    scene school_hall1e at stage with fade
    return


label viv02_books.oedipus:
    scene erik_bed at stage
    show book_oedipus
    with dissolve
    anon "Sweet, this is it!"
    anon "{i}Oedipuss{/i}?"
    anon "{i}Doin' it the Ancient Way{/i}..."
    anon "Why in the world would [saga.cast.erik] want this?"

    scene tammy_bed2 at stage with fade
    return


label viv02_books.rails:
    scene camera at stage

    if saga.cast.anon in saga.sets.school_hall1w:
        show anon a_pocket f_pouty o_right with dissolve
        anon @ -m_talk "( I'll bet that book hanging out of her bag was the one the librarian wants returned. )"
        anon f_pensive @ -m_talk "( Let's scope out what they're doing in the locker room and maybe I'll get a chance to snag it. )"
    else:

        show anon a_point with dissolve
        anon @ -m_talk "( The book is right there, this is my chance! )"
        anon f_happy @ -m_talk "( Let's grab it! )"

    hide anon with dissolve
    return


label viv02_give:
    show old_anon 14
    anon "I found all the overdue books!"
    show old_anon 239_240 with dissolve
    pause
    show old_anon 507 with dissolve
    jane "Really? Let's see..."
    show old_anon 13
    jane a_books "You did it! Thanks a lot!"
    jane "I've got something for you too."
    show old_anon 10
    anon "You do?"
    jane a_book_cheese "Yup, that book you ordered came in."
    pause
    show old_anon 521
    show jane a_side
    with dissolve
    anon "Thanks!"
    anon "{i}My cheese and me{/i}..." (show_lang="{i}Mon fromage et moi{/i}...")
    show old_anon 5 with dissolve
    jane "Will that work?"
    show old_anon 10
    anon "Err, I'll have to make do."
    show old_anon 14
    anon "Thanks again!"
    show old_anon 13
    jane @ e_b f_happy m_laugh "Come back and see us!"
    hide old_anon
    with dissolve
    return


label viv02_work:
    if saga.time.dusk:
        scene mono debbie_study_night
    else:
        scene mono debbie_study_day

    mono "The book contained anything anyone could ever want to know about cheese. Everything from making, to preparing, to cooking, and even eating all kinds of cheeses..." with fade
    mono "Eventually I managed to piece a few paragraphs together, with the hope that it might be enough to please [saga.cast.viv]."

    scene black
    with dissolve
    return


label viv02_work.dark:
    scene anon_pc
    anon "( Ugh, need sleep... )"
    anon "( ... Brain not workey! )"
    return


label viv02_viv:
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 14 at old_left
    anon "I finished the assignment!"
    anon "I wrote about fromage."
    show old_anon 13
    show old_viv 2
    viv "Oh! You like the French cheese?"
    show old_viv 1
    show old_anon 14
    anon "All cheese really..."
    show old_anon 13
    show old_viv 2
    viv "Hehe, you know what goes well with cheese, don't you?"
    show old_viv 1
    show old_anon 10
    anon "... Umm, crackers?"
    show old_anon 5
    show old_viv 3
    viv "No silly, French wine!"
    show old_viv 12
    viv "Maybe someday we could sample a bottle together?"
    viv "But first we must continue practicing your French."
    viv "Stay after class today, and we should have the room all to ourselves."
    viv "Just you and I, yes?"
    show old_viv 13
    show old_anon 26
    show old_xtra 21 at old_left
    anon "Y-yes, ma'am."
    show old_anon 13
    show old_viv 2
    viv "Oh, and before you sit down, add fromage to the blackboard."
    viv "I'll have the other students write their favorites as well."
    hide old_anon
    hide old_xtra
    with dissolve

    scene mono school_french_board
    mono "I felt like I was actually getting pretty good with French. I was understanding more and more each day, even if my vocabulary still left a little something to be desired." with fade
    mono "The private lessons with [saga.cast.viv] had definitely made the language more interesting."

    scene mono school_clock_9am
    mono "I took my seat and tried to focus as another day of lessons began." with fade

    scene mono school_clock_4pm with dissolve
    mono "An eternity later, the bell {i}finally{/i} rang."

    label viv02_viv.cookie hide:
    call shot.school_french_desks
    show old_desk 12 at old_left
    with fade
    viv "I'm really proud of your latest assignment."
    viv "You're becoming quite... fluent."
    show old_desk 13
    anon "Yeah? I'm glad you liked it. I worked really hard on it."
    show old_desk 12
    viv "I'm sure you did, mon bel homme."
    viv "Are you ready for your next tutoring lesson?"
    show old_desk 13
    anon "Yes."
    show old_desk 12
    viv "Let's go over some more words then."

    scene black
    with dissolve
    mono ""

    call shot.school_french_desks
    show school_french dusk
    show old_desk 16 at old_left
    with dissolve
    viv "Your pronunciation is getting so good, [saga.cast.anon]."
    viv "I think you have definitely earned it..."
    show old_desk 19 with dissolve
    viv "... And I'm so proud of you."
    show old_desk 20 with dissolve
    viv "Oh mon dieu!"
    viv "All this new knowledge growing..."
    viv "Ce qu'il est énorme ce lapin..."
    show old_desk 19 with dissolve
    anon "..."
    show old_desk 14 with dissolve
    viv "What's the matter, [saga.cast.anon]?"
    show old_desk 15
    anon "What if someone..."
    show old_desk 14
    viv "Aww, tellement mignon..."
    show old_desk 17 with dissolve
    viv "Do not be worrying."
    show old_desk 18 with dissolve
    viv "Here."
    viv "These should be taking your mind off your worries..."
    anon "{i}*Gulp*{/i}"
    show old_desk 24 with dissolve
    anon "Y-yeah..."
    show old_desk 25_26 slow with dissolve
    pause
    show old_desk 23 with dissolve
    viv "Oh, oui! Joue avec mes seins, [saga.cast.anon]!"
    show old_desk 24 with dissolve
    anon "You're sure Mrs. [saga.cast.ursula.clan] won't come in?"
    show old_desk 5 at old_left
    show old_viv 10c at old_right
    with dissolve
    viv "Oh non! J'ai oublié!"
    viv "I forgot to turn in the midterm report!"
    viv "Forgive me, [saga.cast.anon]. I'm afraid we must stop for today."
    show old_viv 10b
    show old_desk 6
    anon "Okay, [saga.cast.viv]..."
    show old_desk 5
    show old_viv 10c
    viv "We'll resume this next time, yes?"
    viv "I'll have a new assignment waiting for you tomorrow."
    show old_viv 10b
    show old_desk 6
    anon "Sure thing, [saga.cast.viv]."
    show old_desk 5
    show old_viv 10
    viv "Au revoir, mon petit lapin!"
    show old_viv 9
    show old_desk 6
    anon "Au revoir."
    hide old_viv with dissolve
    return


label viv02_viv.busy:
    anon "I've got that assignment finished, [saga.cast.viv]."
    viv "Excellent work, [saga.cast.anon]!" (show_lang="Bien joué, [saga.cast.anon]!")

    if saga.cast.viv in saga.sets.school_french:
        viv "But there is much to cover for today's lessons... I'm afraid there might not be time."
        anon "O-oh, okay."
        viv "Perhaps next time, no?"
        anon "Sure thing!"
    else:

        viv "You must be bringing it to class and we shall look it over, yes?"
        anon "Y-yeah, okay."

    hide anon with dissolve
    return


label viv02_outro:
    return


label viv02_outro.block:
    call shot.school_office1_door
    show anon f_worried o_right with dissolve
    ursula "Lower, slave."
    anon f_surprised @ -m_talk "..."
    annie "Mrs. [saga.cast.ursula.clan], I-"
    ursula "No backchat. Just do as I tell you."
    pause
    show anon m_teeth
    annie "Yes, my Queen..."
    show anon a_up at left with dissolve.nowait
    pause
    hide anon with dissolve
    return


label viv02_outro.office1:
    call shot.school_office1_door
    show anon f_confused o_right with dissolve
    viv "But Madame... I have it here!"
    show anon f_worried
    ursula "Don't you \"Madame\" me..."
    show anon a_facepalm f_tired
    ursula "... The deadline was yesterday, and I've been telling you that for weeks!"
    viv "Please, it simply slipped my mind... You see, I've been so busy wi-"
    show anon a_side f_surprised
    ursula "Yes, yes... easy to understand when speaking about a mind as small as yours, [saga.cast.viv.name]..."
    show anon f_grumpy
    annie "Heh, good one [saga.cast.ursula]."
    ursula "... But a deadline is a deadline."
    show anon f_pouty
    ursula "Surely you don't expect me to sacrifice my precious time covering for {i}your{/i} mistakes!"
    viv "Madame, this is no discussion for a student to be hearing, perhaps-"
    show anon f_pensive
    ursula "Never you mind Miss [saga.cast.annie.clan], she's my personal aide and you're not wiggling your way out of this one!"
    ursula "You're on very thin ice, [saga.cast.viv.name]!"
    show anon f_surprised
    ursula "One more screw up and I'm tossing you out on your little French tooshie, you got me?!"
    viv "{i}*Sigh*{/i}"
    viv "Yes, Madame [saga.cast.ursula.clan]." (show_lang="Oui, Madame [saga.cast.ursula.clan].")
    ursula "Good."
    show anon a_surprised_up f_shocked m_open
    ursula "Now scram... you're ruining my massage."
    anon @ -m_talk "( ?!? )"
    show anon a_surprised_up_both f_surprised m_teeth
    "*Footsteps*"
    anon @ -m_talk "( Uh oh, time to go! )"
    hide anon with dissolvefast

    scene school_cafe at stage with fade
    show anon a_tired f_worried m_talk p_bend with dissolve
    anon "( Man, that was close! Poor [saga.cast.viv]... )"
    anon "( ... I feel like she's trying her best but [saga.cast.ursula] seems to enjoy ragging on her. )"
    anon a_side o_right -p_bend @ -m_talk "( Perhaps if I continue on with her tutoring sessions, I'll discover some way to be of help? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
