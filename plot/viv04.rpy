label viv04_office:
    call shot.school_office5_viv
    show old_viv 2 at old_right
    show old_anon 13 at old_left with dissolve
    viv "Bonjour, [saga.cast.anon]!"
    show old_viv 1
    show old_anon 14
    anon "Hello, [saga.cast.viv]."
    show old_anon 17
    anon "I like your office! It's very... umm... French."
    show old_anon 13
    show old_viv 3
    viv "Merci beaucoup!"
    show old_viv 1
    show old_anon 35
    anon "So, why did you want to see me in your office?"
    show old_anon 13
    show old_viv 5
    viv "Well, [saga.cast.anon], I am worrying about the upcoming exam."
    show old_viv 4
    show old_anon 33
    anon "Huh? You don't need to worry, [saga.cast.viv]."
    show old_anon 14
    anon "I've never felt this prepared for a test before. I'm gonna ace it for sure!"
    show old_anon 13
    show old_viv 5
    viv "Oui, [saga.cast.anon]! You are by far my best student, and I am so very proud of you!"
    viv "It's [saga.cast.roxxy] that is worrying me so..."
    show old_viv 4
    show old_anon 12
    anon "[saga.cast.roxxy]?"
    show old_anon 5
    show old_viv 5
    viv "Oui! Assuming she even shows up for the exam, there is no way she will make a passing grade."
    show old_viv 4
    show old_anon 10
    anon "What happens if she doesn't take the test?"
    show old_anon 5
    show old_viv 5
    viv "Ce serait ennuyeux..."
    viv "If [saga.cast.roxxy] doesn't show up for the exam, it will bring down the average for all the students."
    show old_viv 15 with dissolve
    viv "I'm afraid Mrs. [saga.cast.ursula.clan] will have my head!"
    show old_viv 14
    show old_anon 10
    anon "You mean she'll fire you?!"
    show old_anon 5
    show old_viv 5 with dissolve
    viv "Oui..."
    show old_viv 4
    show old_anon 24
    anon "..."
    show old_anon 12
    anon "Well, I'm not gonna let that happen!"
    show old_anon 14
    anon "I'll find a way to convince [saga.cast.roxxy] to show up for the test, I promise!"
    show old_anon 13
    show old_viv 2
    viv "Oh, [saga.cast.anon]! Tu es mon héros!"
    show old_viv 12
    viv "If you do this for me, I will be giving you the best special reward you can imagine, yes?"
    show old_viv 13
    show old_anon 29 with dissolve
    anon "Y-yeah!"
    show old_anon 13 with dissolve
    show old_viv 2
    viv "Très bien! Good luck, [saga.cast.anon]!"
    show old_viv 1
    show old_anon 14
    anon "Thanks, [saga.cast.viv]."
    hide old_anon with dissolve

    scene school_hall3 at stage with fade
    show anon a_pocket e_nw f_pensive at right with dissolve
    anon @ -m_talk "( Hmm, this is gonna be tough... )"
    anon @ -m_talk "( It's one thing convincing [saga.cast.roxxy] to show up for the exam. )"
    anon @ -m_talk "( But she will also have to pass it somehow... )"
    anon a_rub @ -m_talk "..."
    anon e_w f_snide @ -m_talk "( ... I'm sure I'll think of something. )"
    hide anon with dissolve
    return


label viv04_office.viv:
    hide anon
    hide viv
    show old_anon 10 at old_left
    show old_viv 1 at old_right
    anon "[saga.cast.viv], what did you need me to do?"
    show old_anon 5
    show old_viv 12
    viv "Oh, [saga.cast.anon]. Not here. Come see me in my office after class, yes?"
    show old_viv 13
    show old_anon 14
    anon "Okay, I'll meet you there."
    hide old_anon with dissolve
    return


label viv04_roxxy1:
    show old_anon 10
    anon "Recovered from that poem recital yet?"
    show old_anon 5

    if saga.cast.roxxy < 'sex':
        show old_roxxy 30
        roxxy "Gross, go away!"
        show old_roxxy 29
        show old_anon 10
        anon "C'mon, [saga.cast.roxxy]. I didn't intend for you to recite that speech with me."
        show old_anon 5
        show old_roxxy 31
        roxxy "Ugh, don't remind me!"
        roxxy "You're lucky I don't beat the shit out of you for that."
        show old_roxxy 30
        roxxy "I was completely humiliated!"
        show old_roxxy 29
        show old_anon 12
        anon "Yeah, well, I didn't want to read it either!"
        show old_anon 5
        show old_roxxy 30
        roxxy "Who cares what you want?!"
        show old_roxxy 29
        show old_anon 22
        anon "..."
        show old_anon 10
        anon "Listen, I'm sorry, alright..."
        anon "I want to make it up to you!"
        show old_anon 5
        show old_roxxy 30
        roxxy "Oh really?"
        roxxy "How do you think you're going to do that?"
        show old_roxxy 29
        show old_anon 10
        anon "Well, we have that French exam coming up. I thought maybe I could help you study for it?"
        show old_anon 5
        show old_roxxy 14
        roxxy "..."
        show old_roxxy 3
        roxxy "Why would I want to study for that stupid class?"
        show old_roxxy 29
        show old_anon 12
        anon "Don't you care about your grades?"
        show old_anon 5
        show old_roxxy 2
        roxxy "Pfft, no."
        show old_roxxy 28
        roxxy "The only thing I cared about was the cheer squad but that's all over now..."
        show old_roxxy 27
        show old_anon 12
        anon "Huh? You're not on the cheer squad anymore?"
        show old_anon 5
        show old_roxxy 32 with dissolve
        roxxy "..."
        show old_anon 10
        anon "What happened?"
    else:

        show old_roxxy 3
        roxxy "{i}*Sigh*{/i} Sorry, about all the yelling [saga.cast.anon]..."
        roxxy "I wasn't mad at you or anything... Just that stupid mush mouth bitch!"
        show old_roxxy 29
        show old_anon 10
        anon "I know that [saga.cast.roxxy] but you shouldn't let her get you so worked up..."
        show old_anon 5
        show old_roxxy 31
        roxxy "Ugh, I can't help it!"
        roxxy "You know I hate feeling embarrassed..."
        show old_roxxy 30
        roxxy "... And that was utterly humiliating!"
        show old_roxxy 29
        show old_anon 12
        anon "Seriously, it wasn't that bad. Something else must be bothering you."
        anon "What happened?"
        show old_anon 5
        show old_roxxy 30
        roxxy "{i}*Sigh*{/i} I don't wanna talk about it."
        show old_roxxy 29
        show old_anon 22
        anon "..."
        show old_anon 10
        anon "[saga.cast.roxxy]... Don't be like that."
        anon "I'm your boyfriend, remember?"
        anon "You can depend on me."
        show old_anon 5
        show old_roxxy 1b
        roxxy "Look, I appreciate what you're saying, [saga.cast.anon], but there's nothing you can do to help me this time."
        show old_roxxy 30
        roxxy "I just, don't even wanna think about this stupid school and its dumb teachers."
        show old_roxxy 29
        show old_anon 10
        anon "Alright, well, what about that French exam we have coming up? Do you wanna study for it, together?"
        show old_anon 5
        show old_roxxy 14
        roxxy "..."
        show old_roxxy 3
        roxxy "Ugh, [saga.cast.anon]... Seriously-"
        show old_roxxy 29
        show old_anon 12
        anon "[saga.cast.roxxy], you have to keep your grades up!"
        show old_anon 5
        show old_roxxy 31
        roxxy "It's too late, okay?!"
        show old_roxxy 1l
        roxxy "I screwed up..."
        show old_roxxy 1o
        show old_anon 12
        anon "Huh? What happened?!"
        show old_anon 5
        show old_roxxy 33b with dissolve
        roxxy "..."
        show old_anon 10
        anon "How did you screw up?"

    show old_anon 5
    show old_roxxy 33
    roxxy "Ugh, that stupid dyke, [saga.cast.bridget]..."
    roxxy "She got all pissy the other day, yelling about how I don't listen to her or something..."
    show old_roxxy 30 with dissolve
    roxxy "I dunno, I wasn't really paying attention."
    show old_roxxy 29
    show old_anon 37 with dissolve
    anon "..."
    show old_roxxy 28
    roxxy "But she took my pom-poms and suspended me."
    show old_roxxy 27
    show old_anon 10 with dissolve
    anon "For how long?"
    show old_anon 5
    show old_roxxy 28
    roxxy "Until the State Championship..."
    show old_roxxy 30
    roxxy "How am I supposed to practice without my pom-poms?"
    show old_roxxy 29
    show old_anon 34
    anon "..."
    show old_anon 35
    anon "What if I got them back for you?"
    show old_anon 5
    show old_roxxy 2
    roxxy "Pfft, yeah right."
    show old_roxxy 1
    show old_anon 12
    anon "I'm serious!"

    if saga.cast.roxxy < 'sex':
        anon "That would make up for embarrassing you the other day, wouldn't it?"
    else:
        anon "Then you could practice again and [saga.cast.bridget] wouldn't even know they're gone."

    show old_anon 5
    show old_roxxy 27
    roxxy "..."
    show old_roxxy 28

    if saga.cast.roxxy < 'sex':
        roxxy "I guess."
    else:
        roxxy "I guess that could work."

    show old_roxxy 27

    if saga.prop.pompom_roxxy in saga.cast.anon:
        show old_anon 239_240
        with dissolve.nowait
        pause
        show old_roxxy 2b
        show old_anon 515 at pos(.45)
        with dissolve.nowait
        anon "Voila!"
        show old_anon 513
        show old_roxxy 2c
        roxxy "You had them all along..."
        show old_roxxy 3b
        pause
        show old_anon 13
        show old_roxxy 44
        show old_roxxy 45 as roxxy_poms at old_right
        with dissolve
        roxxy "Well at least I have them back, I guess..."
        show old_roxxy 1c
        show old_anon 14
        jump viv04_roxxy2.merge

    show old_anon 33
    anon "Then consider it done!"

    if saga.cast.roxxy < 'sex':
        pass
    else:

        show old_roxxy 2c
        roxxy "For real?!"
        show old_roxxy 2b

    show old_anon 14
    anon "I'll be right back with those pom-poms."
    show old_anon 13

    if saga.cast.roxxy < 'sex':
        show old_roxxy 1l
        roxxy "Whatever..."
    else:

        show old_roxxy 1b
        roxxy "Alright, well... Just be careful!"
        roxxy "I don't want you getting in trouble too."

    hide old_anon with dissolve

    call shot.school_french_door
    with fade
    show anon a_pocket e_nw f_pensive with dissolve
    anon @ -m_talk "( Hmm, [saga.cast.roxxy]'s pom-poms... )"
    anon @ -m_talk "( I bet [saga.cast.bridget] has them stashed away in her office somewhere. )"
    hide anon with dissolve
    return


label viv04_roxxy1.viv:
    anon f_confused "Couldn't you just {i}give{/i} [saga.cast.roxxy] a passing grade for this test?"
    viv f_sad "Non, [saga.cast.anon]... I'm afraid Madame [saga.cast.ursula.clan] will be watching like the hawk!"
    viv "If she suspects trickery, I'll be looking at further punishment..."

    if saga.cast.viv > 'spank':
        show anon f_surprised
    else:
        show anon f_worried

    viv f_worried "... possibly dismissal."
    anon a_rub "Oof, well we don't want that."

    if saga.cast.viv > 'spank':
        anon f_calm "You're not a bad girl, [saga.cast.viv]..."
        anon a_side f_happy "... You're great!"
        viv "Oui, I tell her this but-"
        show viv f_surprised
        pause
        viv "Wait, what are you meaning?!"
        anon a_uneasy e_e f_shy "Err, nothing!"
        pause

    anon e_w "I'm on it, [saga.cast.viv]..."
    anon a_side "... Don't you worry about a thing!"

    if saga.cast.viv > 'spank':
        viv f_worried "Umm, okay."

    viv f_calm "Thank you, [saga.cast.anon]." (show_lang="Merci, [saga.cast.anon]!")
    return


label viv04_office6:
    scene school_office6 at stage
    show anon a_pocket o_right with dissolve
    anon @ -m_talk "( Alright, she's not in here. )"
    anon f_happy @ -m_talk "( This is my chance to find those pom-poms! )"
    anon a_uneasy f_sceptical -o_right @ -m_talk "..."
    anon a_rub f_pensive o_right @ -m_talk "( Now, where could they be? )"
    hide anon with dissolve
    return


label viv04_office6.near:
    call shot.school_office6_locker
    show anon a_finger e_sw f_confused p_bend at pos(.375) with dissolve
    pause
    show school_office6 -bridget
    show bridget e_sw f_sceptical at right
    with dissolve.nowait
    pause
    show anon a_surprised_up_both e_w f_shocked m_open -p_bend
    bridget e_w "Can I help you?" with hpunch
    anon a_shy_down e_s f_surprised m_teeth @ -m_talk "( I think a little pee came out! )"
    pause
    anon e_w f_worried_surprised o_right -m_teeth "Err, umm..."
    bridget "Yes?"
    anon f_shy "No, I was just..."
    bridget @ -m_talk "..."
    show anon a_uneasy of_blush
    with dissolve.nowait
    anon "Excuse me, I need to use the restroom!"
    show bridget o_right
    hide anon
    with dissolve
    bridget "What a weirdo..."
    return


label viv04_office6.roxxy:
    show old_roxxy 1 at old_right
    show old_anon 10 at old_left
    with dissolve
    anon "Hey, so about your pom-pom-"
    show old_anon 5
    show old_roxxy 2
    roxxy "Did you get them?"
    show old_roxxy 1
    show old_anon 10
    anon "Not yet."

    if saga.cast.roxxy < 'sex':
        show old_anon 11
        show old_roxxy 2
        roxxy "Well then, why are you talking to me?"
        show old_roxxy 3
        roxxy "Get lost!"
    else:

        show old_anon 13
        show old_roxxy 1b
        roxxy "Alright, well... just be careful!"
        roxxy "I don't want you getting in trouble too."
        show old_anon 14
        anon "R-right..."

    hide old_anon with dissolve

    call shot.school_french_door
    with fade
    show anon f_horny_smug with dissolve
    anon @ -m_talk "( Mmm, [saga.cast.roxxy]'s pom-poms... )"
    pause
    anon a_surprised f_worried_surprised "{i}*Ahem*{/i}"
    anon @ -m_talk "( I mean... )"
    anon a_think e_sw f_pensive @ -m_talk "( I bet [saga.cast.bridget] has them stashed away in her office somewhere. )"
    hide anon with dissolve
    return


label viv04_locker:
    scene locker_bridget
    anon "There they are!"
    return


label viv04_locker.fence:
    scene school_office6 at stage
    show anon f_sceptical with dissolve
    anon @ -m_talk "( I'm not going to get a better opportunity to seach this place... )"
    anon @ -m_talk "( ... I need to find those pom-poms! )"
    hide anon with dissolve
    return


label viv04_pompoms(busy):
    scene locker_bridget
    with dissolvefast.nowait
    anon "Awesome!"

    scene school_office6 at stage
    show old_anon 13 at face_right
    with fade

    if busy:
        anon "( Now, I just need to get these back to [saga.cast.roxxy]. )"
        hide old_anon with dissolve
        return

    if saga.cast.roxxy.name[:3] == 'Rox':
        anon "( Now, I just need to get these back to Rox- )"
    else:
        anon "( Now, I just need to get these back to- )"

    show old_anon 11
    bridget "Yeah, yeah! Just head to the track and I'll meet you there."
    bridget "I need to change first."
    show old_anon 23
    anon "!!!" with hpunch
    show old_anon 22
    anon "( Oh crap! She's coming! )"
    anon "( I'm so dead! What am I gonna do?! )"
    anon "( I gotta hide somewhere! )"
    hide old_anon with dissolve
    return


label viv04_pompoms.rails:
    scene locker_bridget
    anon "( Now that I've found them, it'd be kinda daft to just leave them here... )"
    anon "( ... And earning extra brownie points with [saga.cast.roxxy] is never a bad idea. )"
    return


label viv04_hide:
    call shot.school_office6_locker
    show anon a_surprised e_sw f_worried at pos(.45) with dissolve
    anon @ -m_talk "( This is the only place to hide! )"
    show anon a_finger f_confused p_bend at pos(.375)
    anon @ -m_talk "( I just have to hope she doesn't look in here. )"

    scene mono school_bridget_hide
    mono "It was a tight fit but I managed to squeeze inside the locker and close the door in the nick of time. [saga.cast.bridget] entered office scant seconds later!" with fade

    scene mono school_bridget_locker
    mono "Completely unable to move, my only option was to stay silent and hope against hope she wouldn't find a reason to open the locker." with fade

    scene school_office6_case -peek
    show bridget a_fold
    show school_office6_case peek as peek
    with fade
    anon "( There she is! )"
    anon "( Please don't look in here... )"
    pause
    bridget "Man, it sure is cookin' out there."
    bridget "I'm sweating like a whore in church!"
    pause
    show bridget a_bottom_off_01
    pause
    show bridget p_bottom_off_02
    anon "( She's undressing! )"
    anon "( I am so dead if she finds me! )"
    pause
    show bridget a_top_off c_undies -p_bottom_off_02
    pause
    bridget a_hips e_s f_smug "Mmm, I hope you're paying attention!"
    anon "( Does she know?! )"
    pause
    bridget a_flex e_isw "I'd hate for you to miss the gun show!"
    anon "( ... )"
    pause
    bridget "Damn girl!"
    bridget "Better put those away before they hurt somebody."
    show bridget a_top_off
    anon "( What a weirdo... )"
    show bridget c_gym p_bottom_off_02
    pause
    show bridget a_bottom_off_01 e_b -p_bottom_off_02
    pause
    show bridget a_side e_e f_sceptical
    pause
    bridget e_w "Huh. Thought I heard something."
    bridget "Must have been my imagination..."
    hide bridget with dissolve
    pause
    anon "( I think she's gone. )"
    return


label viv04_hide.block:
    scene school_hall1e at stage
    show anon a_finger f_pensive with dissolve
    anon @ -m_talk "( It'd probably be wise to avoid [saga.cast.bridget] for now after that debacle. )"
    anon @ -m_talk "( No need to show my face and remind her I was snooping. )"
    hide anon with dissolve
    return


label viv04_hide.hall:
    scene school_office6 at stage
    show anon a_surprised f_worried o_right at pos(.4)
    pause
    show anon -o_right
    pause
    show anon a_up f_surprised m_teeth o_right
    show bridget a_fold f_angry at right
    with dissolve.nowait
    bridget "What are you doing in here?"
    anon f_worried_surprised -m_teeth "I... Uh..."
    anon a_uneasy f_shy "... Would you believe I was looking for the restroom?"
    show anon f_surprised m_teeth
    bridget @ e_b m_yell "Get your scrawny ass out of here!"
    anon a_salute f_worried_surprised -m_teeth "On my way!"
    hide anon
    show bridget a_side f_sceptical o_right
    with dissolve.nowait
    bridget "Weirdo."

    scene school_hall1e at stage
    with fade
    show anon a_wipe e_sw f_tired m_talk o_right with dissolve
    anon "( Holy... )"
    pause
    anon a_side e_w f_shy -m_talk @ -m_talk "( I can't believe I got away with that. )"
    anon @ -m_talk "( I should get these pom-poms to [saga.cast.roxxy] once I'm done hyper ventilating... )"
    hide anon with dissolve
    return


label viv04_roxxy2:
    show old_anon 14
    anon "I got your pom-poms!"
    show old_anon 13
    show old_roxxy 2
    roxxy "No you didn't..."
    show old_roxxy 1
    show old_anon 14
    anon "Seriously! Here ya go."
    show old_anon 239_240 with dissolve
    pause
    show old_anon 514 at pos(.45) with dissolve
    anon "See?"
    show old_anon 13
    show old_roxxy 44
    show old_roxxy 45 as roxxy_poms at old_right
    with dissolve
    roxxy "You really got 'em..."
    show old_anon 14

    if saga.cast.roxxy < 'sex':
        anon "I told you I would!"
    else:
        anon "Heh, I told you I would."

    label viv04_roxxy2.merge:
    if saga.cast.roxxy < 'sex':
        anon "So, do you forgive me for the other day?"
    else:
        anon "I know how to take care of my girl!"

    show old_anon 13
    show old_roxxy 28

    if saga.cast.roxxy < 'sex':
        roxxy "Yeah, sure."
    else:
        roxxy "You're like, the best boyfriend ever!"

    show old_roxxy 27
    show old_anon 14

    if saga.cast.roxxy < 'sex':
        anon "... And you'll show up for the French exam?"
    else:
        anon "That's right. Now let's go study for that French exam..."

    show old_anon 13
    show old_roxxy 3
    hide roxxy_poms
    with dissolve
    roxxy "Whoa, hold on now!"
    show old_roxxy 2

    if saga.cast.roxxy < 'sex':
        roxxy "That wasn't part of the agreement!"
    else:
        roxxy "I'm not doing anything for that stupid French skank!"

    show old_roxxy 1
    show old_anon 5
    anon "..."
    show old_anon 12
    anon "C'mon [saga.cast.roxxy]..."
    show old_anon 11
    show old_roxxy 2
    roxxy "Absolutely not!"
    show old_roxxy 1
    show old_anon 10
    anon "... But [saga.cast.viv] could get fired if you skip out."
    show old_anon 5
    show old_roxxy 2

    if saga.cast.roxxy < 'sex':
        roxxy "Awesome, that's even more reason for me to blow it off!"
        roxxy "I hate that third-world bitch!"
    else:

        roxxy "Why do you care so much?!"
        roxxy "It would serve her right! Embarrassing me the way she did..."

    show old_roxxy 1
    show old_anon 35

    if saga.cast.roxxy < 'sex':
        anon "Huh? France isn't third world..."
    else:
        anon "[saga.cast.roxxy], she's a good teacher, and she's trying really hard."

    show old_anon 34
    show old_roxxy 2

    if saga.cast.roxxy < 'sex':
        roxxy "Pfft, whatever."
    else:
        roxxy "Psh yeah, she's trying really hard to get her hands on some student dick..."

    show old_roxxy 1b

    if saga.cast.roxxy < 'sex':
        roxxy "I'll be glad to see her gone."
    else:
        roxxy "She's so transparent."

    show old_roxxy 1
    show old_anon 5
    anon "..."
    show old_anon 10

    if saga.cast.roxxy < 'sex':
        anon "There has to be something I can do?"
    else:
        anon "I can't do nothing and watch her get fired, [saga.cast.roxxy]."

    show old_anon 5
    show old_roxxy 2

    if saga.cast.roxxy < 'sex':
        roxxy "I don't think so, dweeb!"
    else:
        roxxy "{i}*Sigh*{/i} You are such a sap for charity cases..."

    show old_roxxy 1b

    if saga.cast.roxxy < 'sex':
        roxxy "Now scram, I gotta start thinking up a new routine for the State Championship."
    else:

        roxxy "Look, I'll try. That's all I can promise."
        roxxy "Right now, I need to focus on preparing for the State Championship."

    show old_roxxy 1
    show old_anon 4 with dissolve
    anon "..."
    show old_anon 14 with dissolve
    anon "Wait, that's it!"
    show old_anon 13

    if saga.cast.roxxy < 'sex':
        show old_roxxy 2
        roxxy "Ugh, what now?"
        show old_roxxy 14
    else:

        show old_roxxy 1b
        roxxy "What?"
        show old_roxxy 1

    show old_anon 33
    anon "I could help you with your routine!"
    show old_anon 13
    show old_roxxy 4
    roxxy "Hah! Yeah right."
    show old_roxxy 2
    roxxy "What do you know about cheering?"
    show old_roxxy 1
    show old_anon 14
    anon "... Nothing."
    show old_anon 13
    show old_roxxy 2

    if saga.cast.roxxy < 'sex':
        roxxy "Yeah, that's what I thou-"
    else:
        roxxy "Haha, then how are you-"

    show old_roxxy 1
    show old_anon 33
    anon "But [saga.cast.jenny] does!"
    show old_anon 14
    anon "She was head cheerleader at her college!"
    show old_anon 13

    if saga.cast.roxxy < 'sex':
        show old_roxxy 2
    else:
        show old_roxxy 1b

    roxxy "... Who?"

    if saga.cast.roxxy < 'sex':
        show old_roxxy 14
    else:
        show old_roxxy 1

    show old_anon 14
    anon "A girl that lives at the same house as me."
    anon "Her squad won State a bunch of times in high school."
    anon "I could get her to help you with your routine!"
    show old_anon 13
    show old_roxxy 2

    if saga.cast.roxxy < 'sex':
        roxxy "Hmm, you aren't lying?"
    else:
        roxxy "Hmm, a bunch of times?"

    show old_roxxy 1
    show old_anon 14

    if saga.cast.roxxy < 'sex':
        anon "Nope!"
    else:
        anon "At least three..."

    show old_anon 13

    if saga.cast.roxxy < 'sex':
        show old_roxxy 14
        roxxy "..."

    show old_roxxy 2

    if saga.cast.roxxy < 'sex':
        pass
    else:
        roxxy "Hmm, that does sound promising..."

    roxxy "Alright. If you can get her to help, I'll show up for the stupid test."
    show old_roxxy 2
    roxxy "... But I'm copying all the answers off you!"
    show old_roxxy 1
    show old_anon 14
    anon "That's fine by me!"
    show old_anon 13
    show old_roxxy 5 with dissolve
    roxxy "..."
    show old_roxxy 6
    show old_anon 1
    anon "..."
    show old_roxxy 10 with dissolve

    if saga.cast.roxxy < 'sex':
        roxxy "Well, go ask her already!"
    else:
        roxxy "Well, get your cute butt moving!"

    show old_anon 11
    show old_roxxy 11

    if saga.cast.roxxy < 'sex':
        roxxy "Sheesh, you're such a loser!"
    else:
        roxxy "I've got a lot of work to do."

    show old_roxxy 6 with dissolve
    show old_anon 10
    anon "I'm going!"
    hide old_anon with dissolve
    return True


label viv04_jenny:
    anon "I need your help with something..."
    show jenny e_w f_snide
    jenny "How much are you paying me?"
    anon f_sceptical "I haven't even told you what it is yet!"
    show anon f_worried
    jenny "Hmm, good point... I should hear all the details before I set the price!"
    anon @ f_tired "{i}*Sigh*{/i}"
    anon "There's this girl at school who needs help with her cheerleading routine."
    jenny "Is this some girl you're trying to bang?"
    anon f_sceptical "Huh? NO!"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_spoon
    else:
        show jenny a_hips

    jenny "Why not? Is she ugly?"
    anon "No, she's gorgeous, but a total bitch!"
    jenny "Hmm, I like her already."
    anon @ -m_talk "..."
    anon f_confused "So you'll help her with the routine?"
    jenny a_fold "Five hundred dollars."
    anon f_surprised "What?! Are you nuts?"
    jenny f_annoyed "That's the price."
    jenny "Pay up or get out."
    anon f_sceptical "Couldn't you just help me out?"
    jenny @ e_b f_calm m_laugh "Hahahaha, good one, [saga.cast.anon]!"
    jenny a_palm f_snide "Five hundred dollars."
    anon "{i}*Sigh*{/i} Fine!"

    menu:
        "Pay. ($500)" if saga.cast.anon.cash >= 500:
            pass
        "Don't pay.":

            jump viv04_jenny.fail

    label viv04_jenny.merge:
    anon a_cash f_sceptical "Here."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon a_down
    else:
        show anon a_side

    jenny a_money f_snide "Perfect."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_spoon
    else:
        show jenny a_side

    jenny "Tell {i}whatshername{/i} she can come see me in the afternoon sometime."
    anon "Her name is [saga.cast.roxxy]."
    jenny a_wave_off f_disgusted "Whatever."
    hide anon with dissolve
    return True


label viv04_jenny.fail:
    show jenny a_fold
    anon "I'll come back when I've got the money..."
    hide anon with dissolve
    return


label viv04_jenny.roxxy:
    show old_anon 10
    anon "You remember our deal, right?"
    show old_anon 5
    show old_roxxy 2
    with dissolve.nowait
    roxxy "What did [saga.cast.jenny] say?"
    show old_roxxy 1
    show old_anon 10
    anon "I haven't asked her yet."
    show old_anon 5

    if saga.cast.roxxy < 'sex':
        show old_roxxy 3c
        roxxy "Well, what are you waiting for?!"
        show old_roxxy 3d
        show old_anon 12
        anon "I'll ask her, just chill out!"
        show old_anon 5
        show old_roxxy 3
        roxxy "Arrghh, you're such a loser!"
        show old_roxxy 3b
    else:

        show old_roxxy 1b
        roxxy "Well, don't wait too long. There's a lot of work to do!"
        show old_roxxy 1
        show old_anon 12
        anon "I'll ask her, just relax!"
        show old_anon 5
        show old_roxxy 1b
        roxxy "I hope she's as good as you made her out to be..."
        show old_roxxy 1

    hide old_anon with dissolve
    return


label viv04_retry:
    anon f_worried "So, about [saga.cast.roxxy]'s routine..."
    show jenny e_w f_annoyed
    jenny "Did you bring the money?"

    menu:
        "Pay. ($500)" if saga.cast.anon.cash >= 500:
            pass
        "Don't pay.":

            jump viv04_retry.fail

    jump viv04_jenny.merge


label viv04_retry.fail:
    show jenny a_fold
    anon "I don't have it yet."
    jenny "Well then, beat it, I'm busy."
    hide anon with dissolve
    return


label viv04_retry.roxxy:
    show old_anon 10
    anon "You'll definitely show up if I get [saga.cast.jenny] to help, right?"
    show old_anon 5
    show old_roxxy 2
    with dissolve.nowait
    roxxy "What did she say?"
    show old_roxxy 1
    show old_anon 10
    anon "Don't worry, I'm working on it."
    show old_anon 5

    if saga.cast.roxxy < 'sex':
        show old_roxxy 3c
        roxxy "So she said \"no\"?"
        show old_roxxy 3d
        show old_anon 12
        anon "I'll get her on board, just chill out!"
        show old_anon 5
        show old_roxxy 3
        roxxy "Arrghh, I can't believe I believed you!"
        show old_roxxy 3b
    else:

        show old_roxxy 1b
        roxxy "Well, don't wait too long. The State Championship won't wait forever!"
        show old_roxxy 1
        show old_anon 12
        anon "I've got this, just relax!"
        show old_anon 5
        show old_roxxy 1b
        roxxy "I really hope she lives up to your hype..."
        show old_roxxy 1

    hide old_anon with dissolve
    return


label viv04_roxxy3(when):
    show old_anon 10
    anon "[saga.cast.jenny] said to pick an afternoon, and she'll help you with your routine."
    show old_anon 5

    if saga.cast.roxxy < 'sex':
        show old_roxxy 3 with dissolve.nowait
        roxxy "At {i}your{/i} house?"
        roxxy "Ugh, this better be worth it..."
        show old_roxxy 1
        show old_anon 12
        anon "It will be! Just remember you promised to show up for the test!"
        show old_anon 5
        show old_roxxy 2
        roxxy "Yeah, yeah..."
        roxxy "... If this [saga.cast.jenny] actually helps, I will."

        if when == 1:
            roxxy "I'll come by tomorrow."
        else:
            roxxy "I'll come by on [saga.time.dow + when]."

        show old_roxxy 3
        roxxy "Now get out of here before somebody sees me talking to you."
    else:

        show old_roxxy 1b with dissolve.nowait
        roxxy "Your house?"
        roxxy "Alright!"
        show old_anon 13

        if when == 1:
            roxxy "Tomorrow works for me."
        else:
            roxxy "[saga.time.dow + when] works for me."

        show old_roxxy 1
        show old_anon 14
        anon "I'm positive she can help you with your routine!"
        show old_anon 13
        show old_roxxy 1h
        roxxy "Awesome!"
        roxxy "She and I can knock this routine out, and then maybe afterwards, you can come back to my place for a little {i}study{/i} session?"
        show old_roxxy 1g
        show old_anon 14
        anon "We aren't going to get much studying done, are we?"
        show old_anon 13
        show old_roxxy 4
        roxxy "Haha, definitely not!"
        show old_roxxy 1h
        roxxy "Trust me, after I finish with you, studying will be the last thing on your mind!"

    hide old_anon with dissolve
    return


label viv04_roxxy3.jenny:
    anon f_worried "Don't forget you have to tutor-"
    jenny f_annoyed @ e_r "Yeah, yeah... the thing with {i}whatsherface{/i}. I got it."
    jenny "She had better not be annoying..."
    anon "She's not, she basically yo-"
    show anon f_pouty
    jenny e_w f_disgusted "... or fat."
    anon @ -m_talk "..."
    jenny f_sad "Oh, god... she's ginormous isn't she?!"
    anon "No, [saga.cast.jenny]... she's not fat."
    jenny f_annoyed @ e_r "Pfft, yeah right."
    jenny "I hope you realize, if this ends up being a hassle, I'm totally gonna boot her ass to the curb!"
    anon f_tired "Ugh, why can't anything ever be simple with you?!"
    hide anon with dissolve
    return


label viv04_roxxy3.viv:
    anon f_smug "I think I've just about got this [saga.cast.roxxy] thing handled [saga.cast.viv]."
    viv @ f_surprised "Truly?" (show_lang="Vraiment?")
    viv "Magnificent, [saga.cast.anon]!" (show_lang="Magnifique, [saga.cast.anon]!")
    viv "I was so worried this was to be the end of my time teaching the students here in America."
    anon a_point_self f_calm "Not if I have anything to say about it, [saga.cast.viv]!"
    viv "Aww, you beautiful boy!"
    show anon a_side f_happy
    viv "I could cover you in kisses!"
    hide anon with dissolve
    return


label viv04_pause:
    return


label viv04_pause.jenny(when):
    if when == 1:
        anon "[saga.cast.roxxy] said she'll be by tomorrow afternoon for that cheerleading thing."
    else:
        anon "[saga.cast.roxxy] said she'll be by [saga.time.dow + when] afternoon for that cheerleading thing."

    jenny e_w f_confused @ -m_talk "Mhmm."
    anon f_confused "So, this is for sure happening then?"
    show anon f_surprised

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_spoon
    else:
        show jenny a_hips

    jenny f_annoyed "Oh. My. God."
    jenny "YES!"
    jenny "Now would you go away and stop bugging me about it?!"
    show anon f_worried_surprised
    jenny e_r "Sheesh!"
    anon @ -m_talk "..."
    hide anon with dissolve
    return


label viv04_pause.roxxy(when):
    show old_anon 10
    anon "When are you coming by to meet with [saga.cast.jenny]?"
    show old_anon 5
    show old_roxxy 3c with dissolve.nowait

    if when == 1:
        roxxy "Umm, tomorrow afternoon?"
    else:
        roxxy "Umm, [saga.time.dow + when] afternoon?"

    show old_roxxy 3d
    show old_anon 29
    with dissolve.nowait
    anon "Right. Yeah, okay."
    show old_anon 3
    show old_roxxy 3c
    with dissolve.nowait
    roxxy "Should I write it backwards on your forehead?"
    show old_roxxy 3d
    show old_anon 10
    with dissolve.nowait
    anon "N-no?"
    hide old_anon with dissolve
    return


label viv04_delay:
    scene camera at stage
    show anon a_surprised f_surprised with dissolve
    anon @ -m_talk "( Didn't [saga.cast.roxxy] say, she'd stop by to see [saga.cast.jenny] today? )"
    anon @ -m_talk "( I should make sure [saga.cast.jenny] holds up her end of the deal. )"
    hide anon with dissolve
    return


label viv04_delay.bell:
    scene camera at stage
    "*Ding Dong*"
    show anon a_surprised f_surprised with dissolve
    anon @ -m_talk "( That must be [saga.cast.roxxy]. )"
    anon @ -m_talk "( I should go and introduce her to [saga.cast.jenny]. )"
    hide anon with dissolve
    return


label viv04_delay.jenny:
    anon f_calm "Don't forget, [saga.cast.roxxy] is coming over this afternoon."
    jenny f_annoyed @ e_r "Yeah, yeah."
    jenny e_w f_confused "What kinda stupid name is that anyway?"
    show anon f_confused
    jenny f_disgusted "\"[saga.cast.roxxy]\"."
    anon f_worried "I dunno."
    jenny "Sounds kinda trashy... all I'm saying."
    anon "Be nice."
    jenny a_wave_off f_annoyed "Ya, whatever."
    hide anon with dissolve
    return


label viv04_delay.roxxy:
    show old_anon 10
    anon "You're still coming by this afternoon?"
    show old_anon 5
    show old_roxxy 11
    with dissolve.nowait
    roxxy "Ya."
    show old_roxxy 7
    show old_anon 2
    with dissolve.nowait
    anon "Cool! Cool, cool."
    show old_anon 1
    show old_roxxy 11
    with dissolve.nowait
    roxxy "Why are you being so weird?"
    show old_anon 5
    roxxy "It's not like I'm coming by to see you."
    show old_roxxy 9
    show old_anon 10
    anon "Yeah, no... I know!"
    show old_anon 29
    with dissolve.nowait
    anon "I just, umm... enjoy helping people."
    show old_anon 3
    show old_roxxy 10
    roxxy "Ugh, you're such a geek."
    show old_roxxy 6
    hide old_anon
    with dissolve
    return


label viv04_lobby:
    call shot.debbie_lobby_center
    show debbie a_vaccuum e_sw f_shy o_right p_bend s_1 at left
    pause
    show anon a_pocket at right with dissolve
    show debbie e_w p_stand
    with dissolve.nowait
    debbie @ f_surprised "Oh! Hi, [saga.cast.anon], You snuck up on me!."
    anon f_shy "Heh, sorry, [saga.cast.debbie]. Has anyone-"
    show anon e_e f_surprised
    show debbie f_curious
    "*Ding dong*"
    anon f_shy "Aha!"
    show anon e_w f_calm
    debbie f_calm "Can you get that while I put this away, please, sweetie?"
    anon f_shy "Sure thing, [saga.cast.debbie]!"
    hide debbie
    show anon a_surprised o_right at pos(.9)
    with dissolve.nowait
    pause
    hide anon with dissolve.nowait
    label viv04_lobby.merge:
    anon "Hey [saga.cast.roxxy]! You here for your session with [saga.cast.jenny]?"
    show old_roxxy 2 at face_right, pos(.4)
    show anon a_pocket at pos(.675)
    with dissolve.nowait

    if saga.cast.roxxy < 'sex':
        show anon f_worried
        roxxy "Duh. What, do you think I'm here to see you or something?!"
        show old_roxxy 1
        anon a_uneasy f_shy "... No."
        show old_roxxy 2
        roxxy "Good, 'cause there is no fucking way-"
    else:

        roxxy "Yup. It's still on, right?"
        show old_roxxy 1
        anon a_wtf f_shy "Absolutely."
        show old_roxxy 2
        roxxy "Awesome! I'm so excited to-"

    show old_roxxy 1 with None
    show anon a_side f_surprised
    show jenny a_fold f_snide at pos(.85)
    with dissolve.nowait
    jenny "{i}*Ahem*{/i}"
    show anon e_e
    pause
    show anon f_shy
    jenny "Is this that girl you wanted me to help?"
    show anon a_surprised f_shocked m_open
    show old_roxxy 1i
    with dissolvefast.nowait
    jenny "You know, the one you're trying to bang?"
    anon e_w @ -m_talk "!!!"

    if saga.cast.roxxy < 'sex':
        show old_roxxy 3
        roxxy "EXCUSE ME?!" with hpunch
    else:

        show old_roxxy 4
        roxxy "... Hahaha!"

    show old_roxxy 14
    show anon e_e f_worried_surprised -m_open

    if saga.cast.roxxy < 'sex':
        anon "N-no!!"
    else:
        anon "I didn't-"

    anon a_side e_w "[saga.cast.roxxy], I swear I never said-"

    if saga.cast.roxxy < 'sex':
        show old_roxxy 2
        roxxy "As if you even have a shot... Not even in your dreams, twerp!"
        show anon a_facepalm e_nnw f_tired
    else:

        show anon f_surprised
        show old_roxxy 1h
        roxxy "What exactly have you been telling them, [saga.cast.anon]?"
        show anon a_fold e_e f_horny

    show old_roxxy 1
    with dissolve.nowait

    if saga.cast.roxxy < 'sex':
        jenny "Aww, too bad little pervert."
        jenny "I guess you're stuck with your hand and a bottle of lotion."
        show anon a_side e_w f_pouty
        show old_roxxy 4
        roxxy "Hah! Yeah, and I feel sorry for the lotion..."
    else:

        jenny a_side f_confused "Wait a second..."
        show anon a_fold e_e f_horny
        jenny f_surprised "You mean, you... a-and him?!"
        show old_roxxy 4
        roxxy "Uhh, yeah?!"
        show jenny f_calm
        roxxy "So long as he keeps taking good care of me..."
        show anon a_side e_w f_pouty
        show jenny f_snide
        roxxy "... And doesn't get fat or lose his hair, yuck!"

    show anon e_e
    show old_roxxy 1
    jenny a_hips @ e_b f_calm m_laugh "Hahaha!"
    jenny f_happy "Oh, I like you! [saga.cast.roxxy], was it?"
    show anon e_w
    show old_roxxy 1b
    roxxy "Yeah, and you're [saga.cast.jenny]?"
    show anon e_e
    show old_roxxy 1
    jenny "That's right."

    if saga.cast.roxxy < 'sex':
        jenny f_snide "C'mon, [saga.cast.roxxy]. We can ditch the dweeb and get started in my room."
        show old_roxxy 1b
        show anon e_w
        roxxy "Gladly."
        show old_roxxy 2
        roxxy "See ya, dweeb!"
    else:

        jenny "C'mon, [saga.cast.roxxy]. We'll do this in my room."
        show old_roxxy 1b
        show anon e_w
        roxxy "Alright."
        show old_roxxy 2
        roxxy "Thanks again, [saga.cast.anon]."

    hide old_roxxy
    hide jenny
    with dissolve.nowait
    pause
    anon @ -m_talk "..."
    anon @ -m_talk "( I have a bad feeling about this. )"

    scene mono debbie_lobby_stairs cheer
    mono "Those two had formed a connection almost instantly." with fade
    more "In hindsight, I guess [saga.cast.jenny] and [saga.cast.roxxy] did have a lot in common."
    mono "They were both captains of the cheer squad, popular, beautiful, and both of them had mastered the art of being a bitch."
    mono "As that realisation continued to dawn, the already gaping chasm in the pit of my stomach seem to grow ever deeper. I'm pretty sure this is how people get ulcers."

    call shot.debbie_lobby_center
    show anon p_stand_away at right
    with fade
    show debbie a_mug f_curious o_right at left
    with dissolve.nowait

    if saga.cast.roxxy < 'sex':
        debbie "Who was that?"
        anon f_worried p_stand "Just a girl from my school. [saga.cast.jenny] agreed to help her with some cheerleading stuff."
    else:

        debbie "So, did I hear correctly, you two are dating now?"
        anon p_stand "Heh, yeah. [saga.cast.jenny] agreed to help her with some cheerleading stuff."

    show anon f_calm
    debbie "[saga.cast.jenny] is helping somebody?"
    debbie f_calm @ e_b f_happy m_laugh "That's a new one."
    anon a_fold f_grumpy "Yeah, because I paid her..."
    debbie f_sad "Ah."
    debbie "Sweetie, you really shouldn't let [saga.cast.jenny] take advantage of you like that..."
    anon e_sw f_pensive "Yeah, I know."
    anon @ -m_talk "..."
    debbie f_curious "Something else on your mind?"
    anon a_palm e_w f_worried "I've just never seen [saga.cast.jenny] hit it off with someone like that..."
    anon f_shy "Kinda freaks me out, to be honest."
    show anon a_side
    debbie f_calm "Well, I think it's a good thing she's made a new friend."
    debbie "I worry about her sitting upstairs by herself all day..."
    debbie f_sad "I'm sure she gets lonely."
    anon e_r f_bored "I doubt it."
    anon @ -m_talk "..."
    show anon e_nw f_surprised
    show debbie e_nw f_pensive
    jenny "Hahahaha!!"
    show debbie e_w f_curious
    anon a_finger f_worried "... Maybe I should go check on them?"
    show anon e_w
    debbie "Maybe."
    show anon a_side
    debbie f_shy "... Just be careful, sweetie."
    hide debbie
    show anon o_right
    with dissolve.nowait
    pause
    roxxy "Hehehe!!"
    anon a_think e_nw f_pensive o_left @ -m_talk "( They really didn't waste any time, I can hear them in [saga.cast.jenny]'s room. )"
    hide anon with dissolve
    return


label viv04_lobby.alt:
    call shot.debbie_lobby_center
    show anon a_surprised o_right at right with dissolve
    "*Ding dong*"
    hide anon with dissolve.nowait
    pause
    jump viv04_lobby.merge


label viv04_lobby.rails:
    scene camera at stage
    show anon a_surprised f_surprised with dissolve

    if saga.cast.anon in saga.zone.debbie_inside:
        "*Ding dong*"
        anon @ -m_talk "( That's gotta be [saga.cast.roxxy]. )"
        anon @ -m_talk "( Keeping her waiting seems like a bad idea. )"
    else:

        anon @ -m_talk "( I need to get home so I can introduce [saga.cast.roxxy] to [saga.cast.jenny]. )"

    hide anon with dissolve
    return


label viv04_bed2:
    scene debbie_bed2_bed -laptop at stage
    show jenny a_down c_cheer p_bed_sit w_normal
    show old_roxxy 36
    show old_roxxy 41b as roxxy_cheer
    show old_roxxy 41 as roxxy_poms
    show old_xtra 41
    roxxy "Thanks again for letting me borrow your old uniform."
    show old_roxxy 35
    jenny "Not a problem!"
    jenny "It doesn't fit me anyways."
    jenny "Shit, this college uniform barely fits..."
    show old_roxxy 37
    roxxy "Haha, yeah."
    show old_roxxy 36
    roxxy "It looks like your tits are gonna spill out, like, any second..."
    show old_roxxy 35
    jenny @ e_b m_laugh "Hehe!"
    jenny "... That's what I'm saying though! The judges totally give extra points for sex appeal."
    jenny "That's why I never wear a bra during competitions."
    show old_roxxy 36
    roxxy "Y-yeah, I never thought about it."
    roxxy "You're like, a total genius!"
    show old_roxxy 35
    jenny "Tell me something I don't know..."
    jenny "These ladies won me three consecutive state championships!"
    show old_roxxy 36
    roxxy "... They are really nice..."
    show old_roxxy 38
    jenny "Thanks!"
    jenny e_sw f_horny "Yours are nice too."
    show old_roxxy 36
    roxxy "Yeah, but mine aren't as big as yours..."
    show old_roxxy 38
    jenny e_w "Mmm, maybe not but I betcha they're perkier than mine."
    show old_roxxy 37
    roxxy "Hehe, maybe..."
    show old_roxxy 35
    jenny "Lemme have a look at those puppies."
    hide old_roxxy
    hide roxxy_cheer
    show jenny b_old_roxxy_cheer e_sw p_bed_lift
    roxxy "Whoa!! What are you-"
    show old_roxxy 34b behind roxxy_poms
    jenny e_w f_calm p_bed_sit -b_old_roxxy_cheer "Calm down!"
    jenny "It's just us girls here."
    show jenny e_sw f_horny
    roxxy "..."
    show old_roxxy 34
    roxxy "I-I dunno..."
    show old_roxxy 34b
    jenny "Here."
    show jenny e_s f_calm p_bed_sit_top_up
    pause
    jenny a_up c_cheer_up f_happy p_bed_sit "See, nothing to be embarrassed about!"
    show jenny e_sw f_horny
    show old_roxxy 40
    show old_roxxy 41d as roxxy_cheer behind roxxy_poms
    with dissolve.nowait
    roxxy "... Y-yeah, I guess..."
    hide old_roxxy
    hide roxxy_cheer
    show jenny b_old_roxxy_cheer_up p_bed_grope_01
    with none.nowait
    roxxy "!!!" with hpunch
    jenny "I was right, they are perkier than mine..."
    jenny "I'm kinda jealous!"
    show jenny p_bed_grope_02
    roxxy "... Thanks."
    jenny p_bed_grope_01 "You've got cute little nipples too!"
    roxxy "..."
    jenny e_w f_calm "Aww, she's shy!"
    show jenny p_bed_grope_02
    roxxy "I'm not-"
    jenny p_bed_grope_01 "So adorable!"
    jenny "Don't you wanna feel mine?"
    show jenny p_bed_grope_02
    roxxy "You want me to-"
    show jenny e_sw f_horny p_bed_grab
    with none.nowait
    roxxy "!!!" with hpunch
    jenny "See, not so bad..."
    show jenny b_old_roxxy_cheer_up_talk
    roxxy "Your skin is so soft..."
    jenny b_old_roxxy_cheer_up "I know, right?"
    jenny "It's this special lotion I use. I'll hook you up!"
    show jenny b_old_roxxy_cheer_up_talk
    roxxy "Thanks, [saga.cast.jenny]!"
    show old_roxxy 39 behind roxxy_poms
    show old_roxxy 41d as roxxy_cheer behind roxxy_poms
    jenny a_down p_bed_sit -b_old_roxxy_cheer_up_talk @ e_b f_calm m_laugh "Damn girl! You've got a bangin' body!"
    show old_roxxy 40
    roxxy "You think the judges will notice?"
    show old_roxxy 39
    jenny e_w f_calm "Totally!"

    if saga.cast.roxxy < 'sex':
        jenny "I can see why that dweeb downstairs wants to hit that."
        show old_roxxy 40
        roxxy "I can't believe you two live together!"
        roxxy "You're so awesome, and he's such a dork!"
    else:

        jenny "I can't believe [saga.cast.anon] is hitting that!"
        show old_roxxy 40
        roxxy "Hehe, well, I really made him work for it."
        roxxy "He's a pretty tenacious guy..."

    show old_roxxy 39

    if saga.cast.jenny < 'seen' and saga.cast.roxxy < 'sex':
        jenny "I know right!"
        jenny "I tell everybody he's the maintenance boy..."
        show old_roxxy 37
        roxxy "Hahaha!"
        show old_roxxy 40
        roxxy "Yeah, my boyfriend threatens to kick his ass all the time."
        show old_roxxy 39
        jenny "You have a boyfriend?"
        show old_roxxy 40
        roxxy "Well, kinda..."
        roxxy "Let's just say, he thinks he's my boyfriend."
        show old_roxxy 39
        jenny "I like your style, [saga.cast.roxxy]!"
        show old_roxxy 40
        roxxy "Hehe, thanks!"
        show old_roxxy 39
        jenny "Is he packing?"
        show old_roxxy 40
        roxxy "What do you mean?"
        show old_roxxy 39
        jenny "You know, down south..."
        jenny "Is he big?"
        show old_roxxy 42
        roxxy "Pfft..."
        show old_roxxy 43 with dissolve
        jenny @ e_b m_laugh "He's small?!"
        show old_roxxy 40 with dissolve
        roxxy "Real tiny."
        show old_roxxy 39
        jenny @ e_b m_laugh "Hahaha!"
        show old_roxxy 40
        roxxy "Yeah, I don't keep him around for the sex."
        show old_roxxy 39
        jenny "I wouldn't think so..."

    elif saga.cast.jenny < 'seen' and saga.cast.roxxy > 'sex':
        jenny "Not hard enough, [saga.cast.roxxy]!"
        jenny "He'd have to kiss my feet and grovel like a dog before I let him in my panties..."
        show old_roxxy 37
        roxxy "Hahaha! Sheesh, you're a hardcore bitch, [saga.cast.jenny]!"
        show old_roxxy 40
        roxxy "Lucky for him, you aren't interested, huh?"
        roxxy "Otherwise, I could totally see him trying..."
        show old_roxxy 39
        jenny "... Yeah. Lucky for him..."
        jenny "... So, is he any good?"
        show old_roxxy 40
        roxxy "What do you mean? Like, in bed?"
        jenny "Yeah."
        roxxy "He's amazing!"
        show old_roxxy 39
        jenny "Amazing? You're joking."
        show old_roxxy 40
        roxxy "No, I'm completely serious!"
        roxxy "He's like an idiot savant or something..."
        roxxy "... And he's got that massive cock!"
        show old_roxxy 39
        jenny f_sad "Huh? What do you mean by massive?"
        show old_roxxy 43b
        hide roxxy_cheer
        with dissolve
        roxxy "..."
        show old_roxxy 39
        show old_roxxy 41d as roxxy_cheer behind roxxy_poms
        with dissolve
        jenny f_calm "You're joking!"
        show old_roxxy 40
        roxxy "Not even a little bit."
        show old_roxxy 39
        jenny f_sad "Holy shit..."
        show old_roxxy 40
        roxxy "It's super crazy!"
        show old_roxxy 39
        jenny f_calm @ e_b m_laugh "Hahaha!"
        show old_roxxy 40
        roxxy "I swear, he's like an orgasm machine!"
        show old_roxxy 39
        jenny "Interesting..."

    elif saga.cast.jenny > 'seen' and saga.cast.roxxy < 'sex':
        jenny "He's not so bad..."
        jenny "He can be pretty useful to have around."
        show old_roxxy 40
        roxxy "... Yeah, I guess he has been pretty helpful recently."
        show old_roxxy 39
        jenny "Also, just between you and me..."
        jenny "He's hung like a horse!"
        show old_roxxy 40
        roxxy "Really?! You mean you've seen his dick?"
        show old_roxxy 39
        jenny "Oh, I've seen it plenty of times."
        jenny "We do live together after all."
        show old_roxxy 40
        roxxy "I guess that's true..."
        roxxy "So it's big, huh?"
        show old_roxxy 39
        jenny @ e_b m_laugh "Huge!"
        show old_roxxy 42
        roxxy "Interesting."
        show old_roxxy 39
        jenny "Is your boyfriend packing?"
        show old_roxxy 40
        roxxy "[saga.cast.dexter]?"
        show old_roxxy 42
        roxxy "Pfft."
        show old_roxxy 43 with dissolve
        jenny @ e_b m_laugh "Hahaha!"
        show old_roxxy 39 with dissolve
        jenny "Tiny, eh? That's too bad."
    else:

        jenny "Yeah, he can be really stubborn..."
        jenny "He's resourceful though, I'll give him that."
        show old_roxxy 40
        roxxy "Plus, he's got that huge cock!"
        show old_roxxy 39
        jenny "I know right?!"
        jenny "He's hung like a freaking horse!"
        show old_roxxy 40
        roxxy "Whoa, wait... You mean you've seen it?"
        show old_roxxy 39
        jenny "Oh, I've seen it plenty of times."
        jenny "Kind of unavoidable really. Living in close proximity like this."
        show old_roxxy 40
        roxxy "Yeah, I guess that makes sense."
        roxxy "It must be annoying living with some random dude..."
        show old_roxxy 39
        jenny @ e_b m_laugh "Hehe, I dunno. It has its perks."
        roxxy "..."
        jenny "Was your last boyfriend packing?"
        show old_roxxy 40
        roxxy "[saga.cast.dexter]?"
        show old_roxxy 42
        roxxy "Pfft."
        show old_roxxy 43 with dissolve
        jenny @ e_b m_laugh "Hahaha!"
        show old_roxxy 39 with dissolve
        jenny "Tiny, eh? That's too bad."
        show old_roxxy 35e
        roxxy "Yeah, he turned out to be a huge douchebag too."
        show old_roxxy 39

    roxxy "..."
    jenny "Well, anyways... You ready to learn some moves?"
    show old_roxxy 37
    roxxy "Hell yeah!"
    show old_roxxy 39
    jenny @ e_b m_laugh "Cool, let's do it!"
    $ renpy.end_replay()

    scene debbie_landing at stage with fade
    show anon a_pocket f_horny_smug o_right at left with dissolve
    anon @ -m_talk "( Wow!!! )"
    anon @ -m_talk "( Maybe this wasn't such a bad idea after all! )"
    hide anon with dissolve

    scene black
    with dissolve
    mono ""

    scene debbie_bed3 dusk at stage
    with dissolve
    show anon f_happy o_right with dissolve
    anon @ -m_talk "( [saga.cast.roxxy] seemed pretty happy as she left. )"
    anon @ -m_talk "( Hopefully she'll hold up her end and show up for the exam now. )"
    anon a_cheer e_b m_teeth @ -m_talk "( [saga.cast.viv] will be so happy when I tell her! )"
    hide anon with dissolve
    return


label viv04_bed2.rails:
    scene camera at stage
    show anon f_worried o_right with dissolve
    anon @ -m_talk "( I should really go check on [saga.cast.jenny] and [saga.cast.roxxy]... )"
    hide anon with dissolve
    return


label viv04_viv:
    hide anon
    hide viv
    show old_anon 14 at old_left
    show old_viv 1 at old_right
    anon "I convinced [saga.cast.roxxy] to show up for the test!"
    show old_anon 13
    show old_viv 2
    viv "Truly?!"
    show old_viv 1
    show old_anon 17
    anon "Yup!"
    show old_viv 25 at pos(.446) with dissolve
    viv "Tu me sauves la vie!"
    show old_viv 26 with dissolve
    viv "Whatever would I do without you?!"
    show old_viv 27
    show old_anon 29
    with dissolve
    anon "Heh, it's no big deal..."
    show old_anon 13
    show old_viv 16
    with dissolve
    viv "Now be sure to study the words we learned over your past assignments, yes?"
    show old_viv 17
    show old_anon 14
    anon "I will! Don't worry!"
    show old_anon 13
    show old_viv 16
    viv "Très bien! Soon we will have the test."
    show old_viv 17
    show old_anon 14
    anon "Alright, [saga.cast.viv]!"
    show old_viv 1
    hide old_anon
    with dissolve
    return


label viv04_viv.roxxy:
    show old_anon 14
    anon "Don't forget about the French exam."
    show old_anon 1
    anon a_point "You promised me you wouldn't ditch."
    show old_anon 2
    show old_roxxy 1d
    with dissolve.nowait
    roxxy "If I show, you're gonna lemme copy off you, right?"
    show old_roxxy 1k
    show old_anon 10
    anon "Yeah, sure... whatever."
    show old_anon 12
    anon "Just be there!"
    show old_anon 5
    show old_roxxy 3
    with dissolve.nowait
    roxxy "Ugh, fine."
    roxxy "You're lucky you have such an awesome roommate."
    show old_roxxy 3b
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
