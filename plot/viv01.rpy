label viv01_intro(fast):
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 10 at old_left
    anon "I was wondering if you were still offering private tutoring?"
    show old_anon 5
    show old_viv 3
    viv "Oh, oui!"
    show old_viv 1
    show old_anon 14
    anon "Awesome! When would you be availa-"
    show old_anon 11
    show old_viv 2
    viv "Impressionnant! You're the first student to inquire about the tutoring!"
    show old_viv 1
    show old_anon 12
    anon "Really? That's weird..."
    show old_anon 5
    show old_viv 5
    viv "I was beginning to think nobody was interested in the special reward."
    show old_viv 1
    show old_anon 12
    anon "Oh yeah, I forgot about the special reward..."
    show old_anon 5
    show old_viv 5
    viv "Quoi? You are not desiring the reward either?!"
    show old_viv 4
    show old_anon 29 with dissolve
    anon "Err... No, I mean... A-a special reward sounds wonderful, [saga.cast.viv]."
    show old_anon 3
    show old_viv 3
    viv "Ah superbe!"
    show old_viv 2
    viv "Then we will meet after school for some one-on-one lessons, yes?"
    show old_viv 1
    show old_anon 10 with dissolve
    anon "Umm... Yeah, I think that will-"
    show old_anon 11
    show old_viv 2
    viv "Très bien!"
    viv "Just be sure to bring your French dictionary along."
    show old_viv 1

    if fast:
        show old_anon 2
        anon "You mean this dictionary?"
        show old_anon 239_240 with dissolve
        pause
        show old_anon 503 with dissolve
        show old_viv 2
        viv "Oui!"
        viv "What a clever boy." (show_lang="Quel petit futé ce garçon.")
        show old_viv 1
        show old_anon 504c
        anon "It's missing a few pages but hopefully it'll still work?"
        jump viv01_viv.merge

    show old_anon 24
    anon "Ah, crap. About that... [saga.cast.viv], I can't seem to find my French dictionary."
    show old_anon 25
    anon "It's not in my backpack, my house, or my locker..."
    show old_anon 5
    show old_viv 5
    viv "Oh non, this is not good!"
    viv "Perhaps you should stop by the library and see if they have one?"
    show old_viv 2
    viv "I would loan you mine, but I'm afraid I've recently spilled wine upon it."
    show old_viv 1
    show old_anon 14
    anon "Oh yeah, I forgot about the library!"
    show old_anon 13
    show old_viv 2
    viv "Oui, I go there quite often myself."
    show old_viv 12
    viv "I love the feel of a good book in my hands."
    viv "Cuddled up by the warm fire with some strong wine..."
    viv "C'est le paradis."
    show old_viv 13
    show old_anon 11
    anon "..."
    show old_viv 2
    viv "Oh, silly me, babbling on and on. Just let me know when you have the dictionary, yes?"
    show old_viv 1
    show old_anon 14
    anon "Sure thing, [saga.cast.viv]."
    hide old_anon
    with dissolve
    return


label viv01_intro.eve:
    anon f_confused "Are you going to sign up to be tutored by [saga.cast.viv]?"
    eve "I'm already doing pretty well, so it's not even worth trying."
    anon "Why not?"
    eve f_happy "Well, you can't really improve an A+."
    show anon f_surprised
    eve f_nervous "It's more likely she'd pick someone like you..."
    anon "Me?"
    eve "Well, yeah... You're failing right now, aren't you?"
    show anon f_worried
    eve "You've got lots of room for improvement."
    show anon e_w f_confused
    eve "Plus, [saga.cast.viv] favors boys."
    eve "You should seriously consider it."
    show anon f_worried
    return


label viv01_book:
    return


label viv01_book.jane:
    show old_anon 10
    anon "I can't seem to find a French dictionary."
    show old_anon 5
    jane "Hmm, let me see..."
    show jane e_sw
    pause
    jane "It should be over on there on shelf, next to the back room."
    show old_anon 14
    show jane e_w
    anon "Alright, I'll take a look. Thanks."
    hide old_anon
    with dissolve
    return


label viv01_book.take:
    scene library_shelf -book_dict at stage
    anon "Aha! {i}French to English dictionary{/i}!"
    anon "Great! Now I can-"
    show book_dict
    with dissolve.nowait
    anon "Wait a second..."
    anon "Some of the pages are missing!"
    anon "Now what do I do?"
    pause
    anon "Hopefully nothing important is gone."
    return


label viv01_book.viv:
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 12 at old_left
    anon "Remind me what I need to get before we can study together?"
    show old_anon 5
    show old_viv 2
    viv "You will need a French to English dictionary."
    viv "Check the library, yes?"
    show old_viv 1
    show old_anon 14
    anon "Oh, that's right!"
    anon "Thanks!"
    hide old_anon
    with dissolve
    return


label viv01_jane:
    call shot.library_lobby_jane
    show old_anon 504 at right
    with dissolve
    anon "Well, I found part of a French dictionary."
    show old_anon 503
    jane f_sad "What?"
    show old_anon 5
    show jane a_book_dict e_ssw f_annoyed
    with dissolve.nowait
    jane "Oh no!"
    jane "I'll have to order a new one but it'll take a while to arrive."
    jane e_w f_sad "Did you still want to check it out?"
    show old_anon 10
    anon "Yeah, I'm pretty desperate. I'll just have to hope I don't need those missing pages..."
    show old_anon 5
    jane "Okay, well, sorry again!"
    jane f_calm "You can just keep it. It won't be much use around here..."
    show old_anon 504
    show jane a_side
    with dissolve
    anon "Thanks!"
    show old_anon 503
    jane "No problem, have a nice day!"
    hide old_anon
    with dissolve

    scene library_lobby -library_books at stage
    with fade
    show old_anon 34 at face_right with dissolve
    anon "( I guess I should take this to [saga.cast.viv] and see what she thinks... )"
    hide old_anon
    with dissolve
    return


label viv01_viv:
    hide anon
    hide viv

    if saga.cast.viv in saga.sets.school_french:
        show old_viv 1 at old_right
        show old_anon 10 at old_left
    else:

        show old_viv 1 at old_right
        show old_anon 10 at old_left

    anon "I found a dictionary at the library but it's missing a few pages."
    show old_anon 239_240 with dissolve
    pause
    show old_anon 503 with dissolve
    pause
    label viv01_viv.merge:
    show old_anon 5
    show old_viv 22b
    with dissolve
    viv "Oh, my!"
    viv "This will make things very difficult, I think."
    viv "The French to English section is intact but you are missing many words..."
    viv "I'm afraid some of them might be crucial to the subjects we are to be studying."
    show old_viv 21b
    show old_anon 10
    anon "Ugh, I was afraid of that..."
    show old_anon 5
    show old_viv 21
    viv "Hmm, perhaps all is not lost. I'm sure a classmate of yours would be willing to let you copy the missing pages from their dictionary."
    viv "You can use the photocopier in the computer lab."
    show old_viv 22
    show old_anon 14
    anon "That's a good idea!"
    show old_anon 13
    show old_viv 2 with dissolve
    viv "Tu es le bienvenu, [saga.cast.anon]."
    viv "Be sure to get English words beginning with the letter \"B\" for our next lesson."
    show old_viv 1
    show old_anon 14
    anon "Alright, time to track down another dictionary..."
    show old_anon 13
    show old_viv 12
    viv "Working so hard already. I can tell you are desiring the special reward, very much, yes?"
    show old_viv 13
    show old_anon 10
    anon "Any thoughts on whose dictionary I should be asking to borrow?"
    show old_anon 13
    show old_viv 11
    viv "Hmm..."
    show old_viv 2
    viv "Perhaps [saga.cast.judith]?"
    viv "She shows much talent for the French tongue..."
    show old_viv 1
    show old_anon 14
    anon "Okay, I'll start with [saga.cast.judith] then."
    hide old_anon
    with dissolve
    return


label viv01_judith:
    hide anon
    hide judith
    show old_judith 1 at old_right
    show old_anon 14 at old_left
    anon "Hey there, [saga.cast.judith]! Got a minute?"
    show old_anon 13
    show old_judith 5
    judith "Sure, [saga.cast.anon]."
    show old_judith 4
    show old_anon 14
    anon "I was hoping I could borrow your French dictionary."
    anon "I need to make a quick copy of some pages and I'll return it."
    show old_anon 13
    show old_judith 3
    judith "My French dictionary?"
    show old_judith 5
    judith "Absolutely! So long as you promise to be careful with it?"
    show old_judith 4
    show old_anon 11
    anon "( What is with women and their French dictionaries? )"
    show old_anon 10
    anon "Yeah, I'll be really careful and you won't even notice it's gone."
    show old_anon 13
    show old_judith 5
    judith "Okay, I trust you, [saga.cast.anon]."
    pause
    show old_judith 43 with dissolve
    judith "Here it is..."
    show old_judith 4
    show old_anon 522
    with dissolve
    anon "Thanks, [saga.cast.judith]! I totally owe you one!"
    hide old_anon
    with dissolve
    return


label viv01_judith.viv:
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 12 at old_left
    anon "What was I supposed to do again?"
    show old_anon 5
    show old_viv 2
    viv "Copy the pages you are missing from a classmate's dictionary."
    show old_viv 1
    show old_anon 14
    anon "Oh, that's right!"
    show old_anon 13
    show old_viv 2
    viv "Check with [saga.cast.judith]. She is very good with her French."
    show old_viv 1
    show old_anon 14
    anon "And then the computer lab has the copy machine..."
    anon "Got it, thanks again!"
    hide old_anon
    with dissolve
    return


label viv01_copier:
    call shot.school_tech_printer
    show old_anon 520 at old_left with dissolve
    anon "( Okay, now I just set the book on here... )"
    anon "( And press... )"
    anon "( ... This button! )"
    anon "( ... )"
    anon "( ... )"
    anon "( PC load letter? What the heck does that mean? )"
    anon "( Maybe I should ask someone here how to get this thing to work. )"
    hide old_anon
    with dissolve
    return


label viv01_june:
    show old_anon 12
    anon "I'm having trouble with the printer. What does PC load letter mean?"
    show old_anon 5
    show old_june 4
    june "Ugh, is it doing that again?! What a piece of garbage!"
    show old_june 2
    show old_anon 10
    anon "I just need to scan a couple pages from this book and print them off."
    anon "Could you help me?"
    show old_anon 5
    show old_june 3
    june "Yeah, sure!"
    june "Not to brag or anything but I'm pretty good with electronics."
    show old_june 2
    show old_anon 14
    anon "Awesome!"
    show old_anon 13
    hide old_june
    with dissolve

    call shot.school_tech_printer
    show school_tech -erik -june
    show old_june 9 at old_right
    with fade
    show old_anon 13 at old_left with dissolve.nowait
    june "Sometimes you just need to restart it. Let me just cycle power."
    show old_june 10
    show old_anon 108
    with dissolve.nowait
    anon "Really?"
    show old_anon 5
    show old_june 9
    with dissolve.nowait
    june "Yeah, technology is picky like that."
    june "Just waiting for it to boot up..."
    show old_anon 10
    anon "Alright."
    show old_anon 5
    pause
    show old_june 10
    show old_anon 434
    with dissolve.nowait
    june "I think it should be work no-"
    show old_june 9
    show old_anon 5
    with dissolve.nowait
    june "Grr... PC load error?!"
    show old_june 15 at pos(.7)
    show old_anon 110
    with dissolve.nowait
    june "You worthless piece of-"
    show old_june 16 with vpunch
    pause
    show old_june 15 with dissolve
    june "I guess I'll have to open it up and repair it again."
    show old_anon 10
    anon "How long will that take?"
    show old_anon 5
    show old_june 19
    with dissolve.nowait
    june "It will take a while, I don't have time to deal with it today."
    show old_june 17
    show old_anon 10
    anon "Seriously?"
    show old_anon 5
    show old_june 19
    june "Yeah, this thing really is a pain in the butt..."
    show old_june 17
    label viv01_june.merge:
    show old_anon 12
    anon "Stupid technology!"
    show old_anon 518 with dissolve
    show old_anon 519 with vpunch

    if saga.cast.anon.str < 2:
        jump viv01_june.fail

    pause
    show old_anon 11 with dissolve.nowait
    anon "!!!"
    show old_june 18
    june "... Hey! It's working!"
    show old_june 17
    show old_anon 10
    anon "Really?"
    show old_anon 5
    show old_june 18
    june "Yeah! You must have the Midas touch, [saga.cast.anon]!"
    show old_june 17
    show old_anon 14
    anon "Hah, yeah. I guess so..."
    show old_anon 13
    show old_june 18
    june "Well, you can copy your pages now..."
    show old_june 17
    show old_anon 14
    anon "Thank goodness! I really need to get this book back to [saga.cast.judith] before she gets upset."
    anon "Thanks for all your help, [saga.cast.june]!"
    show old_anon 13
    show old_june 18
    june "No problem."
    hide old_june with dissolve
    show old_anon 518 with dissolve
    anon "Print!"
    show old_anon 519 with vpunch
    show old_xtra 39 with dissolve
    pause .25
    hide old_xtra with dissolve
    show old_anon 184 with dissolve
    pause
    show old_anon 510 with dissolve
    anon "( Alright! I finally have a complete French dictionary. )"
    anon "( Now I can return this book to [saga.cast.judith] and get started with those private tutoring sessions. )"
    hide old_anon
    with dissolve
    return True


label viv01_june.copier:
    call shot.school_tech_printer
    show old_anon 520 at old_left with dissolve
    anon "( It still says \"PC load letter\". )"
    anon "( Stupid thing! )"
    hide old_anon
    with dissolve
    return


label viv01_june.fail:
    $ renpy.notify(_('Insufficient {color=e40002}STR{/color}.'))
    anon "..."
    show old_anon 10 with dissolve
    anon "{i}*Sigh*{/i}"
    anon "I guess I'll check back with you tomorrow then..."
    show old_anon 5
    show old_june 19
    june "Sorry, [saga.cast.anon]."
    show old_june 17
    hide old_anon
    with dissolve
    return


label viv01_retry:
    show old_anon 10
    anon "Have you been able to fix the copy machine yet?"
    show old_anon 5
    show old_june 19
    june "No, sorry. I haven't had time to mess with it at all."
    hide old_anon
    show old_june 17
    with dissolve

    call shot.school_tech_printer
    show school_tech -erik -june
    show old_anon 13 at old_left
    with fade
    show old_june 17 at old_right with dissolve.nowait
    jump viv01_june.merge


label viv01_outro:
    call shot.school_french_front
    show old_viv 1 at old_right
    show old_anon 14 at old_left with dissolve
    anon "Okay, I'm ready to start the lesson, [saga.cast.viv]."
    show old_anon 13
    show old_viv 3
    viv "Génial!"
    show old_viv 2
    viv "Stay after class and we will begin."
    show old_viv 1
    show old_anon 14
    anon "Sure thing."
    hide old_anon
    with dissolve

    scene mono school_clock_9am
    mono "I spent the whole day trying to catch up on my studies..."

    scene mono school_clock_4pm with dissolve
    mono "... Until the bell rang."

    label viv01_outro.cookie hide:
    call shot.school_french_desks
    show old_desk 5 at old_left
    with fade
    show old_viv 7 at old_right with dissolve
    viv "Are you ready for our first lesson?"
    viv "Alone."
    viv "Together."
    show old_viv 9
    show old_desk 6
    anon "Uhh, yes?"
    show old_desk 5
    show old_viv 7
    viv "Ah ah ah, parlez-vous Français?"
    show old_viv 9
    show old_desk 6
    anon "Oh! Umm, oui?"
    show old_desk 5
    show old_viv 7
    viv "Très bien!"
    viv "Now, have you looked at the assigned terms yet?"
    show old_viv 9
    show old_desk 6
    anon "Yeah, I looked them over."
    show old_desk 5
    show old_viv 7
    viv "Which ones are troubling you?"
    show old_viv 9
    show old_desk 6
    anon "Well, I'm not very good at pronunciation."
    show old_desk 4
    anon "Like... How do you say this word?"
    show old_desk 3
    show old_viv 7 behind old_desk at pos(304), face_right with dissolve
    viv "Ah, that's vélo or la bicyclette."
    viv "It means bicycle."
    hide old_viv
    show old_desk 8
    with dissolve
    anon "!!!"
    show old_desk 9 with dissolve
    viv "Here, repeat after me [saga.cast.anon]."
    show old_desk 10 with dissolve
    viv "Vi-loo."
    show old_desk 11
    anon "... Velow."
    show old_desk 10
    viv "No VI-loo."
    show old_desk 11
    anon "Vv... Velo."
    show old_desk 10
    viv "Almost, you just need to pronounce the e now."
    show old_desk 11
    anon "... Velo."
    show old_desk 10
    viv "Très bien, mon bel homme!"
    show old_desk 9 with dissolve
    viv "You are learning very quickly."
    show old_desk 11 with dissolve
    anon "Thanks, [saga.cast.viv]. You're such a good teacher!"
    show old_desk 9 with dissolve
    viv "Ah, quel charmeur!"
    show old_desk 8 with dissolve
    viv "Such a well-mannered young man."
    show old_desk 9 with dissolve
    viv "Now, let's move on to the next word."

    scene black
    with fade
    mono ""

    call shot.school_french_desks
    show school_french dusk
    show old_viv 7 at old_right
    show old_desk 1 at old_left
    with dissolve
    viv "You did so well, [saga.cast.anon], but it's getting late."
    show old_viv 10
    viv "We should call it a day, yes?"
    show old_viv 9
    show old_desk 2
    anon "Wow, is it that late already?"
    anon "I totally lost track of time."
    show old_desk 1
    show old_viv 7
    viv "Oui, the time, it flies when you are having such fun!"
    viv "You know, [saga.cast.anon], I'm so happy you signed up for my tutoring."
    viv "It fills me with joy, helping nice young students like yourself to succeed."
    show old_viv 10
    viv "It's why I became a French teacher."
    show old_viv 9
    show old_desk 2
    anon "Yeah, I'm lucky you're my teacher, [saga.cast.viv]."
    show old_desk 1
    show old_viv 7
    viv "Ohh, tu me flattes..."
    viv "You are making me blush."
    viv "Just keep practicing and I think you'll be caught up in no time."
    viv "Who knows, you might even earn that special reward..."
    show old_viv 9
    show old_desk 2
    anon "Yes, ma'am."
    show old_desk 1
    show old_viv 7
    viv "Now get home, [saga.cast.anon]."
    show old_viv 10
    viv "Au revoir!"
    show old_viv 9
    show old_desk 2
    anon "Goodnight, [saga.cast.viv]."
    hide old_viv
    with dissolve
    return


label viv01_outro.viv:
    anon "I've got the dictionary all fixed up, [saga.cast.viv]!"
    viv "Very good, [saga.cast.anon]!"
    viv "Now make certain you bring it to your next class and we'll begin your private tutoring afterwards, yes?"
    anon "Will do."
    viv "Wonderful!" (show_lang="Merveilleuse!")
    hide anon
    with dissolve
    return


label viv01_post:
    return


label viv01_post.judith:
    hide anon
    hide judith
    show old_judith 1 at old_right
    show old_anon 14 at old_left
    anon "Hey, [saga.cast.judith]! Here's your book back."
    show old_anon 239_240 with dissolve
    pause
    show old_anon 522 with dissolve
    anon "Thanks again!"
    show old_anon 13
    show old_judith 43
    with dissolve
    judith "Oh good, I was starting to worry..."
    show old_judith 4 with dissolve
    show old_anon 14
    anon "No need to worry. It's in tip-top shape... see?"
    show old_anon 13
    show old_judith 5
    judith "Thanks for being careful with it, [saga.cast.anon]."
    judith "I dunno why I worry so much..."
    show old_judith 4
    show old_anon 14
    anon "Thanks for letting me borrow it!"
    show old_anon 13
    show old_judith 5
    judith "Anything for yo-"
    show old_judith 3
    judith "I mean... A-anytime!"
    show old_judith 1
    show old_anon 10
    anon "Okay, well, I'll see ya around."
    show old_anon 5
    show old_judith 3
    judith "Bye, [saga.cast.anon]."
    hide old_anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
