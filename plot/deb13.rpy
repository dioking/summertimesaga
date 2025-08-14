label deb13_lobby:
    call shot.debbie_lobby_stairs
    show debbie at right
    show anon f_tired o_right at left with dissolve
    debbie "Good morning, sweetie."
    show debbie f_sad
    anon @ a_fist_mouth e_b m_yawn "{i}*Yawn*{/i}"
    anon @ -m_talk "Mhmm."
    debbie a_nervous "Oh my, you look exhausted!"
    anon "Yeah, I-"
    anon "... Haven't really been sleeping all that well."
    debbie f_sceptical "Aww, how come?"
    anon "I dunno, just... weird dreams, I guess."
    debbie a_clasp f_sad "My poor baby."
    debbie f_sceptical "What kind of dreams?"
    anon f_worried "Ehh, I'd rather not get into it..."
    anon "... It's embarrassing."
    debbie f_shy "Well, you don't ever have to feel embarrassed with me, sweetie."
    anon "Yeeeaaah, you say that..."
    anon "... But based on recent events, I think it's best I don't get into specifics."
    debbie f_surprised "Ohhh."
    debbie f_curious "This has got to do with those anxieties you were telling me about."
    anon a_pocket e_s "Uh huh."
    debbie f_shy "Aww, shoot... I'm so sorry, sweetie... I-"
    anon @ -m_talk "..."
    debbie "I wish, I could do... something."
    anon e_w "Yeah, it's... Don't worry about it."
    debbie f_calm "You know, boys your age... they're supposed to have {i}those{/i} sort of dreams..."
    debbie a_hips "... The girls too in fact!"
    debbie "It's perfectly natural."
    show debbie f_sceptical
    anon e_se "{size=*.65}Mm, not {i}these{/i} dreams.{/size}"
    debbie a_side "What's that, sweetie?"
    anon e_w "N-no, nevermind."
    anon f_calm "So, ehh... what do you have going on?"
    debbie f_curious "Me?"
    debbie a_clasp f_shy "Actually, I was coming to ask you for help with something."
    anon f_confused "Oh?"
    debbie "The bakery up the road is running a promotion today and I thought it might be nice to have some donuts for breakfast."
    anon f_calm "Yeah, that sounds wonderful."
    debbie f_sad "Unfortunately, I can't seem to get the car started!"
    show anon f_confused
    debbie a_mimic_cables "I think it needs that zapper thing."
    anon f_snide "Heh, zapper thing?"
    anon "You mean jump pack?"
    debbie a_side @ e_r f_bored "Oh, whatever it's called!"
    debbie "That was your father's department... I never had to mess with that stuff."
    show anon a_think e_nw f_pensive
    pause
    show debbie f_shy
    anon e_w f_calm "Yeah, I think I remember how it all works."
    show debbie f_calm
    anon a_side "Just gimme a minute and I'll have you on your way to donut city."
    show anon f_happy
    debbie a_nervous f_happy "Oh, now that sounds like a place I'd like to book a vacation!"
    show debbie a_up b_anon e_sw f_calm p_hug_lean at pos(.4)
    show anon e_s f_worried p_debbie_hug_lean at pos.debbie
    debbie "Thank you, sweetie."
    anon @ -m_talk "( Aww, man... not the hug. )"
    debbie f_shy "I dunno what I'd do without you."
    anon e_b @ -m_talk "( Hng! Bum Bum scented torture! )"
    anon e_nw "Uh huh."
    anon "It's still out by the car, right?"
    show anon e_w f_confused p_stand behind debbie at left
    debbie a_side e_w f_curious p_stand -b_anon "What's that?"
    anon "The jump pack, it's-"
    anon f_calm "Never mind, I'll check it out."
    hide anon with dissolve.nowait
    debbie "Do you need help?"
    anon "Nope. I've got it!"

    scene debbie_hall with fade
    show anon a_pocket f_pouty with dissolve
    anon @ -m_talk "( Here I am, getting jerked off by evil clowns and she's just piling it on with the hugs... )"
    anon @ -m_talk "( ... Honestly, I don't even wanna imagine what comes next. )"
    anon @ -m_talk "( Evil clowns should be the end game!! )"
    hide anon with dissolve
    return


label deb13_engine:
    scene debbie_car
    anon "( !!! )"
    anon "( Holy hell. )"
    anon "( A jump pack is {i}not{/i} going to fix that. )"

    call shot.debbie_garage_car
    show anon e_sw f_surprised o_right at pos(.35)
    with fade
    pause

    if saga.cast.raz < 'defeat':
        anon @ a_think e_nw f_pensive -m_talk "( It looks like somebody worked the engine over with a hammer or something, but who- )"
        anon f_worried @ -m_talk "( Aww, man... I bet those Russian assholes did this! )"
    else:

        anon @ a_think e_nw f_pensive -m_talk "( It looks like it exploded or something, but how- )"
        anon f_worried @ -m_talk "( [saga.cast.debbie] really needs to get this thing serviced more often! )"

    anon @ -m_talk "( {i}*Sigh*{/i} What am I supposed to do now?! )"
    anon e_osw f_sad @ -m_talk "( We'll just have to take it to a mechanic, I guess... )"
    anon @ -m_talk "( ... Better let [saga.cast.debbie] know the bad news. )"
    hide anon with dissolve
    return


label deb13_engine.rails:
    scene camera at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( I should go jump the car like [saga.cast.debbie] asked me to. )"
    hide anon with dissolve
    return


label deb13_kitchen:
    call shot.debbie_kitchen_island
    show debbie at right
    show anon f_worried o_right at left with dissolve
    anon "Well, I looked at the engine."
    debbie f_curious "And?"
    anon "And it's a lot worse than a dead battery, [saga.cast.debbie]..."
    show debbie f_sad
    anon "... There's no way I can fix it on my own."
    debbie "Oh, no."
    anon "Yeah, in fact, I think you might have to replace the whole engine."
    show debbie a_embarrassed f_surprised
    anon "It's all busted up."
    debbie "B-but, we can't afford something like that!"
    anon "Y-yeah, I know."
    show debbie a_side e_s f_sad
    pause
    show anon f_surprised
    debbie a_surprised e_w f_calm "Oh, wait... I think we have a warranty!"
    anon f_confused "Warranty?"
    debbie a_nervous "Yeah, your father paid extra for a five year warranty when he bought the car for me."
    anon @ f_calm "Hey, that could work."
    anon "It hasn't been more than five years, has it?"
    debbie f_sad "N-no, I don't think so."
    show anon f_calm
    debbie a_clasp f_sceptical "Do you think the dealership will cover the repairs?"
    anon "Maybe."
    debbie f_sad "Oh, this could be real bad..."
    debbie f_sceptical "... How are we going to make it without a car, [saga.cast.anon]?"
    anon "Don't worry, [saga.cast.debbie]."
    anon a_point_self "I'll call up the dealership and speak with them."
    debbie f_surprised "You will?"
    anon a_side "Of course."
    debbie f_sad "Oh, sweetie... I don't wanna put any burden on you, especially with all the-"
    anon a_calm_down "No, no... it's fine."
    anon "I'm sure I can sort this out."
    debbie "Y-you're sure?"
    anon a_hips f_smug "Absolutely."
    anon "In fact, I'll head back to the car and call them right now."
    debbie "O-okay, if you're certain you can handle it."
    anon "Leave it to me."
    hide anon with dissolve
    return


label deb13_kitchen.rails:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( I should report back to [saga.cast.debbie] before doing anything else. )"
    hide anon with dissolve
    return


label deb13_car:
    call shot.debbie_garage_car
    show anon a_phone e_s f_shy at left with dissolve
    show anon a_phone_talk e_w f_calm with dissolve
    "*Ring* *Ring*"

    call shot.car_shop_phoneright
    show josie p_desk_lean_in behind desk onlayer aux at pos.desk
    call phoneright.answer
    pause
    "*Ring* *Ring*"
    anon f_worried @ -m_talk "( I hope I have the correct number... )"
    "*Ring* *Ring*"
    show josie a_phone e_ssw f_angry p_stand at right
    josie @ e_r f_bored "Urgh..."
    "*Ring* *Ri-*"
    show josie a_landline_talk_phone with dissolve

    if saga.cast.josie < 'met':
        josie f_bored "{i}*Sigh*{/i} Hello?"
        anon "Hello?"
        anon f_sceptical "Is this the Saga Car Dealership?"
        josie @ -m_talk "Mhmm."
    else:

        josie f_bored "Hello?"
        anon "[saga.cast.josie]?"

        if saga.cast.josie > 'blowjob':
            jump deb13_car.friends

        josie f_calm @ -m_talk "Hmm?"

    show josie f_calm
    anon f_calm @ e_b f_smug "Oh, good."
    anon "I was worried I might have the wrong number."
    josie @ -m_talk "..."
    show anon f_worried
    pause
    anon "Are you still there?"
    josie "Can I help you with something?"
    anon "My friend's car needs a new engine and I'd like you to check the warranty."
    show josie at pos(.925) with dissolve.aux
    josie "Name?"
    anon "My name is [saga.cast.anon]."
    josie f_bored @ e_r "Not {i}your{/i} name..."
    josie "I need the name on the account."
    anon @ f_shy "Oh, sorry."
    anon f_calm "It's [saga.cast.debbie] Cummings."
    josie a_landline_talk f_calm "Jeez..."
    pause
    josie "You still at 240 Cookie Street?"
    anon "Uh huh."
    pause
    josie @ -m_talk "Hmm."
    josie "License plate, \"DTF M0M\"..."
    josie f_bored "Seriously?"
    anon @ e_b f_happy m_teeth "..."
    josie f_calm "It looks like the warranty expired three months ago."
    anon f_worried "Ah, crap."
    anon "Are you sure?"
    josie f_bored "What, do you think I can't read an expiration date?"
    show josie a_landline_talk_phone f_calm
    pause

    if saga.cast.josie < 'met':
        anon "Well, is there anything you can do, Miss... Umm?"
        josie "[saga.cast.josie]."
        anon "Oh, that's a nice name."
        josie @ -m_talk "..."
        anon "Is there anything you can do, [saga.cast.josie]?"
    else:

        anon "Well, is there anything you can do?"

    josie "We can have our mechanic swing by to take a look but it'll cost you an arm and a leg..."
    anon "How much?"
    josie f_bored "Dude, I dunno..."
    pause
    josie f_calm @ e_r f_bored "... For an entirely new engine, probably in the neighborhood of eight thousand dollars."
    anon f_shocked m_open @ -m_talk "Eight thousand dollars?!"
    anon @ -m_talk "[saga.cast.debbie] can't afford that!"
    show anon f_surprised m_teeth
    josie @ -m_talk "..."
    anon e_osw f_sad -m_teeth "Great."
    anon "Thanks for all the help..."
    show anon a_phone e_sw with dissolve
    call phoneright.hangup
    show anon a_pocket e_osw
    pause
    anon @ -m_talk "( What the heck am I going to do now? )"
    anon @ -m_talk "( I might have to bite the bullet and pay for the engine repairs myself... )"
    anon e_nw f_pensive @ -m_talk "( ... Or maybe I can convince her to help me? )"
    pause
    anon e_w f_worried @ -m_talk "( Either way, I'll have to call back her to sort this out. )"
    hide anon
    with dissolve
    return


label deb13_car.busy:
    call shot.debbie_garage_car
    show anon a_phone e_s f_shy at left with dissolve
    show anon a_phone_talk e_w f_calm with dissolve
    "*Ring* *Ring*"

    call shot.car_shop_phoneright
    call phoneright.answer
    "*Ring* *Ring*"
    pause
    "*Ring* *Ring*"
    pause
    show anon f_confused
    "*Ring* *Ring*"
    pause
    show anon f_pensive
    "*Ring* *Ring*"
    show anon a_phone e_sw
    call phoneright.hangup
    show anon a_pocket e_w
    pause
    anon @ -m_talk "( Hmm, I guess nobody is there. )"
    anon @ -m_talk "( I'll have to try again later. )"
    hide anon with dissolve
    return


label deb13_car.dark:
    call shot.debbie_garage_car
    show anon a_pocket f_worried o_right at left
    anon @ -m_talk "( There's not much point calling now. )"
    anon @ -m_talk "( They're closed. )"
    hide anon with dissolve
    return


label deb13_car.debbie:
    if saga.cast.debbie in saga.sets.debbie_kitchen:
        call shot.debbie_kitchen_island
    else:
        call shot.debbie_utility_laundry

    show debbie f_curious at right
    show anon o_right at left with dissolve
    debbie "Any luck with the dealership, sweetie?"
    anon f_confused @ -m_talk "Hmm?"
    anon f_worried_surprised "Oh, right!"
    debbie f_sceptical "Did you forget?"
    anon f_shy "Nope, I'll take care of it right now."
    anon a_point_back "I'll call from the garage in case they need any details."
    debbie f_shy "Thanks, sweetheart."
    hide anon with dissolve
    return


label deb13_car.friends:
    josie e_w f_horny "[saga.cast.anon]?"
    anon "Hey."
    josie a_landline_talk "I wasn't expecting you to be on the other end of this line..."
    josie "What's going on?"
    anon "Well, actually... I've got a bit of a problem I was hoping you could help me with?"
    josie "Heh, I've never been propositioned over the phone before..."
    anon f_confused @ -m_talk "Hmm?"
    josie "Is this like a phone sex thing?"
    anon f_surprised "No, nothing like that!"
    pause
    anon f_shy "I mean, maybe later... That would be awesome!"
    josie "Hehe, what's the problem then?"
    anon f_worried "My friend's car needs a new engine and I'd like you to check the warranty."
    josie f_calm "Okay, that's easy enough."
    show josie at pos(.925) with dissolve.aux
    josie e_ssw "Name?"
    anon "[saga.cast.anon]?"
    anon f_calm "What, did you forget?"
    josie e_r f_bored "Not {i}your{/i} name..."
    josie @ e_w f_horny "I need the name on the account, stupid."
    anon "Oh, right..."
    anon "Sorry."
    anon "It's [saga.cast.debbie] Cummings."
    show josie e_ssw f_calm
    pause
    josie "You still at 240 Cookie Street?"
    anon "Uh huh."
    pause
    josie @ -m_talk "Hmm."
    josie "License plate, \"DTF M0M\"..."
    josie e_w f_bored "Seriously?"
    anon @ e_b f_happy m_teeth "..."
    josie e_ssw f_calm "It looks like the warranty expired three months ago."
    anon f_worried "Ah, crap."
    anon "Are you sure?"
    josie "That's what the computer says."
    anon "What am I gonna do now?"
    label deb13_car.merge:
    josie "You know what?"
    josie "I've got this."
    anon f_surprised "Huh?"
    josie "Yeah, I'll just extend the warranty."
    anon "You can do that?"
    josie f_horny "Bitch, I can do whatever the hell I want!"
    josie "What's my dad gonna do, fire me?"
    show josie f_calm
    anon f_calm "That's exactly what you want him to do."
    pause
    josie "There."

    if saga.time.dusk:
        josie f_horny "Someone will be out to service the car first thing tomorrow."
    else:
        josie f_horny "Someone will be out to service the car later today."

    anon "You're amazing, [saga.cast.josie]."
    josie e_w @ e_b f_happy m_laugh "I know."
    josie "Anything else?"
    anon "Nope, that was it."
    josie "You can repay me by coming back to the dealership and keeping me company."
    anon "Can do."
    anon "See you soon."
    josie "Later, [saga.cast.anon]."
    show josie a_desk e_ssw
    show anon a_phone e_sw f_happy
    with dissolve
    call phoneright.hangup
    anon a_pocket e_b m_teeth @ -m_talk "( It really is all about who you know! )"
    hide anon with dissolve
    return


label deb13_retry:
    call shot.debbie_garage_car
    show anon a_phone e_sw f_worried at left with dissolve
    anon @ -m_talk "( Maybe we can work something out this time? )"
    show anon a_phone_talk e_w with dissolve
    "*Ring* *Ring*"

    call shot.car_shop_phoneright
    show josie p_desk_lean_in behind desk onlayer aux at pos.desk
    call phoneright.answer
    pause
    "*Ring* *Ring*"
    josie @ -m_talk "..."
    "*Ring* *Ring*"
    show josie a_phone e_ssw f_angry p_stand at right
    josie @ e_r f_bored "Urgh..."
    "*Ring* *Ri-*"
    show josie a_landline_talk_phone with dissolve
    josie "Hello?"
    anon "[saga.cast.josie]?"

    if saga.cast.josie > 'blowjob':
        jump deb13_retry.friends

    josie @ -m_talk "Hmm?"
    anon f_calm "Oh, good."
    anon "Hey, it's me again..."
    josie @ -m_talk "..."
    show anon f_worried
    pause
    anon "You know, the guy who needed the engine repair on my friend's vehicle?"
    josie @ f_bored "Do you have the money?"

    menu:
        "Transfer money. ($8,000)":
            jump deb13_retry.cash
        "Are you sure there's nothing you can do?":

            pass

    anon "Are you sure there's nothing you can do?"
    josie e_w f_worried "Like what?"
    anon @ e_osw f_sad "I don't know."
    anon f_sceptical "Can't you like, extend the warranty or something?"
    josie f_calm "Heh, I mean, I {i}could{/i} do that..."
    josie e_ssw "But why should I?"

    menu:
        "To stick it to the man!"(saga.cast.anon.chr >= 8, '{chr}'):
            pass
        "Um... funsies?":

            jump deb13_retry.fail

    anon "Because it will piss off your boss?"
    show josie e_r f_bored

    if saga.cast.josie < 'met':
        josie "Nice try-"
    else:
        josie "Nice try, bowl-"

    josie a_landline_talk e_ssw f_surprised "Wait, what did you say?"
    anon f_calm "You obviously don't like working there..."
    josie f_calm "No, I fucking hate it!"
    anon "Yeah, I can tell."
    anon "Why not stick it to the company then?"
    josie @ -m_talk "..."
    josie f_horny "You know what?"
    josie "Why not."
    josie "Screw this place!"
    show josie f_calm
    anon f_happy @ e_b m_laugh "Heh, awesome."

    if saga.time.dusk:
        josie "I'll have someone out there first thing tomorrow."
    else:
        josie "I'll have someone out there later today."

    anon "Thank you so much!"
    show anon a_phone e_sw
    show josie a_desk
    with dissolve
    call phoneright.hangup
    hide anon with dissolve
    return


label deb13_retry.busy:
    jump deb13_car.busy


label deb13_retry.cash:
    if saga.cast.anon.bank < 8000:
        jump deb13_retry.poor

    anon f_calm "Yes?"
    show anon a_phone e_sw
    josie a_landline_talk e_w f_confused "Wait, you do?"
    anon f_happy @ e_b m_laugh "Uh huh."
    "*Ding*"
    anon a_phone_talk e_w "... And sent."
    show josie e_ssw f_calm at pos(.925) with dissolve.aux
    pause
    show josie f_surprised
    pause
    josie "I wasn't expecting that..."
    anon f_calm "When can we expect the mechanic?"
    show josie f_calm

    if saga.time.dusk:
        josie "I'll have someone out there first thing tomorrow."
    else:
        josie "I'll have someone out there later today."

    anon "Thanks."
    show josie a_desk
    show anon a_phone e_sw
    with dissolve
    call phoneright.hangup
    show anon a_pocket e_w
    pause
    anon f_worried @ -m_talk "( Geez, spending eight thousand dollars on this is going to sting! )"
    anon f_calm @ -m_talk "( Oh, well... it's for a good cause and I know [saga.cast.debbie] will appreciate it. )"
    hide anon with dissolve
    return 8000


label deb13_retry.dark:
    jump deb13_car.dark


label deb13_retry.debbie:
    jump deb13_car.debbie


label deb13_retry.fail:
    anon f_shy "B-because you're a nice lady?"
    josie @ f_bored "Wrong."
    anon f_worried "Ah, man..."
    josie "Better luck next time."
    show josie a_phone with dissolve
    call phoneright.hangup
    anon a_phone e_sw f_surprised @ -m_talk "( She hung up! )"
    anon a_pocket e_osw f_sad @ -m_talk "( Oh well... It was worth a shot... )"
    hide anon
    with dissolve
    return False


label deb13_retry.friends:
    josie e_w f_horny "[saga.cast.anon]?"
    anon "Hey."
    josie a_landline_talk "I wasn't expecting you to be on the other end of this line..."
    josie "What's going on?"
    anon "Remember when I called about the warranty on my friend's car?"
    josie "Oh right..."
    josie @ e_b f_happy m_laugh "\"DTF M0M\" ..."
    anon "That's the one-"
    show josie e_ssw at pos(.925) with dissolve.aux
    jump deb13_car.merge


label deb13_retry.poor:
    anon f_confused "You said it was eight thousand?"
    josie @ f_bored "Yup."
    show anon a_phone e_sw
    pause
    show anon f_worried
    pause
    anon a_phone_talk e_osw f_sad "Alright, I don't think I have that much in my account..."
    anon "... I'll call back when I do."
    show anon a_phone e_sw with dissolve
    call phoneright.hangup
    hide anon with dissolve
    return False


label deb13_delay:
    scene camera at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( Oh, the mechanic should have arrived by now. )"
    anon a_side e_w f_calm @ -m_talk "( I'd better go meet him and make sure he does a good job. )"
    hide anon with dissolve
    return


label deb13_delay.debbie:
    if saga.cast.debbie in saga.sets.debbie_kitchen:
        call shot.debbie_kitchen_island
    else:
        call shot.debbie_utility_laundry

    show debbie f_curious at right
    show anon o_right at left with dissolve
    debbie "Any luck with the dealership, sweetie?"
    anon "They're sending someone over as soon as possible."
    debbie a_nervous f_happy "Oh wonderful! Thanks, sweetheart."
    hide anon with dissolve
    return


label deb13_outro:
    scene debbie_garage at stage
    show debbie a_clasp o_right at pos(.375)
    show jiang at right
    jiang "And that should just about do 'er!"
    debbie "Really? That was fast!"
    jiang a_towel "Yes, ma'am... like greased lightnin'."
    jiang "You just gimme a call if you have any more trouble, ya hear?"
    jiang f_horny "Makin' a perty little lady's engine purr is my specialty, ya know what I mean?"
    show jiang e_sw
    debbie f_sad "Ehh."
    jiang e_w "And you just all sorts of perty, now ain'tcha?"
    debbie f_sceptical "Riiight."
    show anon a_pocket f_sceptical o_right at pos(.2)
    anon "Hey, [saga.cast.debbie]... Everything alright out here?"
    debbie a_relieved f_calm o_left "Oh, hey sweetie!"
    anon "Did he get the car all fixed up and running?"
    show debbie a_side o_right
    jiang "Yessir, I did!"
    show anon f_calm
    jiang "Had to replace the whole damn engine, but yeah... she's runnin' like a crackhead to the welfare office!"
    show anon f_confused
    show debbie f_confused
    jiang @ e_b f_happy m_laugh "Hyuk hyuk!"
    anon "That's... good?"
    jiang "Well I best be off."
    show anon e_sw
    show debbie e_sw f_surprised
    jiang a_invoice "Got yer invoice for ya right ch'ere..."
    show anon e_w f_calm
    show debbie a_invoice e_w f_calm
    jiang a_side f_calm "... Everything paid in full, mind!"
    debbie a_side f_shy "Oh, alright."
    show anon f_confused
    jiang f_horny "And one quick peek under yer hood real quick and make sure I didn't leave my tool in her."
    anon @ -m_talk "..."
    debbie @ -m_talk "..."
    jiang f_calm "Naw, I'm just playin'!"
    jiang @ e_b f_happy m_laugh "Hyuk hyuk!"
    jiang "A little mechanic humor for ya."
    debbie "{i}*Ahem*{/i} Yes, well... thanks again!"
    jiang f_horny "My pleasure, sweetcheeks."
    hide jiang with dissolve.nowait
    show debbie f_confused
    pause
    anon "He's a weird guy, huh?"
    debbie "Yeah."
    pause
    debbie f_happy o_left "Shall we fire it up and see how it runs?"
    anon f_happy "Definitely!"
    hide anon
    hide debbie
    with dissolve

    scene debbie_car_inside garage invoice
    show anon a_side_knee p_car_turn
    show debbie p_car_turn
    show debbie_car_inside wheel as wheel
    with fade
    debbie "Alright, here we go!"
    show anon e_owsw
    debbie p_car_ignition "..."
    show anon e_w
    debbie p_car @ e_oe "Hey, it works!"
    show debbie p_car_turn
    anon "Yeah, it sounds good too."
    debbie "Phew, that is such a relief!"
    debbie f_happy "I was so worried we were gonna be stuck without a car for the foreseeable future!"
    anon e_ow f_happy p_car "Heh, right?"
    show debbie_car_inside -invoice
    show debbie a_invoice e_ossw f_curious p_car
    anon "That would have sucked."
    show anon a_surprised e_w f_surprised p_car_turn
    debbie e_osw f_surprised "{i}*Gasp*{/i}"
    show anon e_wsw
    pause

    if saga.cast.debbie > 'car.paid':
        show anon m_teeth

    debbie "Oh my-"
    debbie "Sweetie, this says eight thousand dollars!"

    if saga.cast.debbie > 'car.paid':
        show anon f_worried_surprised m_idle
    else:
        show anon a_side_knee e_w f_smug

    debbie e_w f_worried_surprised p_car_turn "You didn't-"

    if saga.cast.debbie > 'car.paid':
        jump deb13_outro.paid

    anon e_w "Relax, [saga.cast.debbie]..."
    anon "... I took care of it."
    show anon a_side_knee
    debbie e_ossw f_shy p_car "But-"
    debbie e_w f_sceptical p_car_turn "Where did you get the money for this?!"

    if saga.cast.josie < 'blowjob':
        anon "The person I spoke with at the dealership was willing to waive the fee for us."
        debbie f_surprised "Really?"
        show debbie_car_inside invoice
        debbie a_side f_confused "Why would they do that?"
        anon "I got the impression they were very displeased with the current management."
        debbie f_shy "Oh, dear."
        debbie f_curious "So that's it, they just waived it?"
        anon f_calm "Well, it took a little convincing but... in the end, yeah."
        debbie f_calm "I had no idea you'd turned into such a charmer!"
    else:

        anon "We paid nothing."
        anon "I have a friend who works at the dealership who was able to pull some strings."
        show debbie_car_inside invoice
        debbie a_side "A friend that can pull eight thousand dollar strings?"
        anon f_shy "Heh, yeah."
        show debbie f_curious
        anon "She's the manager's daughter and a bit of an eccentric."
        debbie "Interesting."
        debbie f_calm "I had no idea you'd turned into such a social butterfly."

    anon a_uneasy f_shy "Oh, I dunno if I'd go that far."

    if saga.cast.josie < 'blowjob':
        anon "I just saw an opportunity and seized it."
    else:
        anon "She's just someone I met through work."

    label deb13_outro.cookie hide:
    debbie "Well, I'm proud of you."
    anon a_side_knee f_calm "Thanks, [saga.cast.debbie]."
    anon "I couldn't have you going without a car, could I?"
    label deb13_outro.merge:
    show debbie f_shy
    anon a_shy f_shy p_car "It's my job to look after you guys now."
    show anon e_sse
    debbie a_touch_anon_knee "Aww, sweetie."
    show anon e_e
    debbie "I'm the one who's supposed to be looking after you!"
    anon "You do look after me!"
    anon of_blush "Every day."
    show anon e_w
    debbie "Aww!!"
    pause
    show anon a_up f_surprised p_car_turn
    show debbie e_o f_calm p_car_lean_close
    pause
    show anon f_shy
    debbie @ p_car_peck_anon_cheek "{i}*Muah*{/i}"
    debbie "I just don't know..."
    show anon f_horny
    debbie @ p_car_peck_anon_forehead "{i}*Muah*{/i}"
    debbie "... What I did..."
    show anon f_horny_smug
    debbie @ p_car_peck_anon_nose "{i}*Muah*{/i}"
    debbie "... to deserve such a wonderful boy!"
    pause
    show debbie p_car_peck_anon_mouth
    anon a_surprised e_sse_ssw f_surprised @ -m_talk "( !!! )" with hpunch
    show anon e_b f_calm m_drink
    debbie "Mmm."
    show debbie p_car_lean_close
    anon a_wait e_w f_worried -m_drink "W-wait a second."
    anon f_confused "I thought you said we shouldn't do that anymore?"
    debbie a_side e_s f_shy of_blush p_car "Yeah, I know I did..."
    show anon a_side_knee
    debbie "... It's just-"
    show anon f_shy
    debbie e_w p_car_turn "Sometimes, I-"
    pause
    hide anon
    show debbie p_car_peck s_600ms
    pause
    show anon a_wait f_horny p_car_turn z_b_f behind debbie
    show mimic anon at pos.anon
    debbie a_touch_anon_knee f_horny p_car_turn "Oh, sweetie."
    pause
    hide mimic
    hide anon
    debbie p_car_peck "Mmm."
    show debbie p_car_kiss
    pause
    hide anon
    show debbie p_car_peck
    pause
    show anon a_wait f_horny of_blush p_car_turn z_b_f_of behind debbie
    show debbie p_car_turn
    show mimic anon at pos.anon
    anon "You are such a good kisser!"
    hide mimic
    show anon a_side_knee f_shy z_reset
    debbie a_side f_shy "Heh, you're not supposed to say stuff like that to your landlady."
    anon f_confused of_none "Why not?"
    show debbie e_s p_car
    anon "It's true."
    debbie @ -m_talk "..."
    debbie e_w p_car_turn "T-thanks, sweetie."
    anon f_shy "So, you think I could kiss you more now?"
    debbie f_sceptical of_none "You really want to?"
    anon f_happy "More than anything!"
    debbie f_shy "{i}*Sigh*{/i} I suppose it's okay, when it's just the two of us..."
    debbie @ e_e "... And we're somewhere [saga.cast.jenny] won't catch us."
    anon f_confused "Like here in the car?"
    debbie f_happy "Yes."
    anon a_fistpump f_happy "Sweet!"
    debbie @ e_b m_laugh "Hehe!"
    show anon a_side_knee
    debbie "You're so adorable."
    hide anon
    show debbie p_car_kiss
    pause
    debbie "Mmm."
    show debbie d_anon_hard
    pause
    show anon a_wait d_hard f_horny_smug p_car_turn z_b_f_of behind debbie
    show debbie a_touch_anon_knee f_shy of_blush p_car_turn
    show mimic anon at pos.anon
    pause
    hide mimic
    show anon z_reset
    debbie a_side e_sw f_surprised @ -m_talk "( !!! )"
    debbie "Oh, sweetie... wow."
    anon a_surprised e_s f_surprised p_car "Ah, geez!" with hpunch
    show debbie e_w f_shy
    anon a_cover_dick e_w f_worried p_car_turn "S-sorry, [saga.cast.debbie]... I just-"
    show anon e_s f_confused
    debbie a_touch_anon_knee of_none "N-no, no... it's okay."
    show anon e_w
    pause
    show debbie a_stroke_02 e_sw f_calm p_car_lean
    anon a_surprised d_none e_s f_surprised p_car @ -m_talk "( !!! )"
    debbie e_w "This is nothing to be ashamed of, sweetie..."
    show anon e_e
    pause
    show anon e_s
    debbie "... It's something that's out of your control."
    show debbie a_stroke e_b s_1
    anon "Haah!"
    anon e_wsw f_shy p_car_turn "Y-you're-"
    show debbie e_sw
    with dissolve
    show anon f_confused
    show debbie a_stroke_02 f_surprised
    with hpunch
    pause
    show debbie e_w f_worried_surprised
    pause
    show anon a_wait d_hard e_w f_worried_surprised
    debbie a_side p_car_turn "Sorry, sweetie."
    debbie "I wish I could help you with this..."
    debbie f_sad "... But it wouldn't be right."
    show anon a_side_knee e_s f_worried
    debbie a_touch_anon_knee "You understand that, don't you?"
    anon e_w "Y-yeah, of course."
    anon f_shy "I'll just... wait for it to go down."
    show anon e_sse
    pause
    show anon e_w
    debbie a_touch_anon_neck "Tsk, my poor baby."
    pause
    show anon f_confused
    debbie a_side f_calm "How about I make it up to you, hmm?"
    anon "Oh?"
    debbie f_happy "I grabbed some ice cream at the mall the other day."
    show anon f_surprised
    debbie "I'll bet I could whip us up some nice, big, banana splits in no time!"
    anon f_happy "Ooh, yeah... that does sound good."
    debbie "I think we've even got some of those little cherries that you like."
    anon "You're the best, [saga.cast.debbie]!"
    debbie @ e_b m_laugh "Hehe!"
    debbie "I'll head on inside and get started then."
    debbie f_shy @ e_sw "You just come along once you're ready..."
    debbie "... Okay?"
    show debbie f_calm
    anon "Definitely!"
    debbie "Alright, sweetie."
    show anon p_car_twist_away
    show debbie_car_inside -base
    show debbie_car_inside base garage as base behind debbie_car_inside
    show debbie p_stand behind debbie_car_inside at pos(.725, .5), blur(10), zoom(.5)
    with dissolve.nowait
    pause
    show debbie p_stand_away at pos(.1), blur(10), zoom(.5)
    anon e_s f_shy p_car @ -m_talk "( Man, I can't believe she touched my {i}thing{/i}... )"
    hide debbie with dissolve.nowait
    anon a_facepalm e_b f_worried_surprised @ -m_talk "( ... Argh, if only she'd been willing to go further! )"
    pause
    anon a_side e_s f_shy @ -m_talk "( Oh well, at least I'm getting some ice cream outta the deal. )"
    anon f_confused @ -m_talk "( Assuming it ever goes down, that is. )"
    pause
    anon f_pensive "C'mon, you stupid thing..."
    anon "... We're missing ice cream time!"
    anon e_n f_shy "{i}*Sigh*{/i}"
    $ renpy.end_replay()

    scene black
    with dissolve
    mono ""

    call shot.debbie_lobby_stairs
    show debbie_lobby t1
    with dissolve
    show anon a_pocket f_happy with dissolve
    anon @ -m_talk "( Mmm, [saga.cast.debbie] makes the best banana split sundays... )"
    anon e_b m_teeth @ -m_talk "( ... And it seems like she's finally gotten over her scruples when it comes to kissing me. )"
    anon @ -m_talk "( I just have to make certain to only broach the subject when we're alone and there's no chance of anyone catching us. )"
    anon a_think e_nw f_pensive -m_teeth @ -m_talk "( Hmm. )"
    anon @ -m_talk "( Maybe there's a good opportunity to be found when she goes on her shopping trips? )"
    hide anon with dissolve
    return


label deb13_outro.paid:
    anon a_facepalm e_n f_shy p_car "Aww, man..."
    show anon e_b
    pause
    anon e_e "... You weren't supposed to see that!"
    show anon a_side_knee e_w p_car_turn
    show debbie_car_inside invoice
    debbie a_side f_confused "[saga.cast.anon], where in the world did you get that kind of money?"
    anon "Relax, [saga.cast.debbie]."
    anon "I've been doing odd jobs here and there for a while now."
    debbie f_worried_surprised "Yeah, okay... but eight thousand dollars?!"
    anon f_smug "What can I say?"
    anon "I'm good with my money."
    show anon f_shy
    debbie f_sad "{i}*Sigh*{/i} I'd much rather you put this towards your tuition next year."
    debbie f_sceptical "What about your future, sweetie?"
    anon "I'll manage."
    show debbie f_shy
    anon f_calm "Besides, you and [saga.cast.jenny] are going to be a big part of that future regardless of what I do."
    jump deb13_outro.merge


label deb13_outro.rails:
    scene camera at stage
    show anon with dissolve
    anon @ -m_talk "( I should go meet the mechanic in the garage. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
