label jen08_intro:
    call shot.debbie_bed3_sleep
    with fade
    jenny "[saga.cast.anon]!"
    anon @ -m_talk "{i}*ZZzz*{/i}..."
    show debbie_bed3_visit open -bed -computer
    show jenny e_ose f_angry m_talk p_bed3_door behind anon
    show debbie_bed3_visit bed computer as computer behind anon
    show anon p_bed3_lay
    with none.nowait
    jenny "HEY DOOFUS!" with hpunch
    show jenny f_snide q_tod -m_talk
    anon a_down e_w f_surprised p_bed3_sit @ m_teeth "!!!"
    anon f_tired_annoyed "What the-"
    anon "What's your problem?!"
    jenny "I need you for something."
    anon "Can't it wait?!"
    anon "I'm trying to sleep!"
    jenny "No, it can't wait."
    jenny "Hurry up, loser!"
    show debbie_bed3_visit -open
    show anon e_b f_hurt m_teeth
    hide jenny
    with none.nowait
    with hpunch
    pause
    anon f_calm p_bed3_sleep -m_teeth "( Ugh, I'm so tired... )"
    pause
    show debbie_bed3_visit open
    show jenny e_ose f_angry m_talk p_bed3_door behind computer
    show anon p_bed3_lay
    with none.nowait
    jenny "Don't go back to sleep either!" with hpunch
    jenny "Get up, put some pants on, and get your lazy ass in gear!"
    show jenny f_snide q_tod -m_talk
    anon e_w f_tired_annoyed p_bed3_sit "Yeah, yeah... I'm coming."
    anon "Sheesh."
    hide jenny
    show debbie_bed3_visit ajar -open
    anon @ p_bed3_stretch "{i}*Yawn*{/i}"
    anon "This had better be worth it..."
    return


label jen08_bed2:
    scene debbie_bed2 -jenny at stage
    show jenny a_fold at right
    show anon a_pocket f_worried o_right at left with dissolve
    anon "Alright, I'm here."
    anon "What do you want?"
    jenny a_hips "I found another way to make money."
    jenny "{i}Way{/i} better than that stupid Sluttygram site."
    anon "Okay."
    anon "What is it?"
    jenny "None of your business, loser."
    anon @ -m_talk "..."
    show jenny a_fold f_annoyed

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen08_bed2.alt

    anon "{i}*Sigh*{/i} C'mon, [saga.cast.jenny]..."
    jenny "Would you just shut up and listen!"
    anon @ -m_talk "..."
    jenny f_calm "I need you to go to the mall and buy something for me."
    anon @ f_sceptical "Why does it always come down to money with you?"
    jenny "Umm, because you have nothing else to offer me?"
    jenny "It's not that big a deal, it's only one hundred dollars..."
    show anon f_surprised
    pause
    anon f_worried "Another one hundred?!"
    anon "I dunno, that's a lot of money!"
    jenny f_annoyed "If you buy me this, I'll take everything off for you."
    anon f_confused "You'll get completely naked?"
    jenny "For two minutes..."
    show anon f_surprised
    jenny f_angry m_teeth "But no touching!"
    show jenny f_annoyed -m_teeth
    anon a_think e_nw f_pensive @ -m_talk "..."
    anon a_pocket e_w f_sceptical "Alright, fine."
    anon "I guess that's worth one hundred."
    show anon f_worried
    jenny e_r "It's worth a lot more than one hundred!"
    jenny e_w "You're lucky I'm feeling generous..."
    label jen08_bed2.merge:
    anon f_worried "So what am I buying?"
    jenny "I need you to go to the mall and look on the second floor for a store called Pink."
    anon "Pink, huh?"
    anon "Okay..."
    jenny "The toy I want is called The Electro Clit."
    anon "Toy?"
    anon "Aren't you a little old for toys?"
    jenny "It's a sex shop, dummy..."
    anon f_shocked m_open @ -m_talk "!!!" with hpunch
    anon a_point_self f_worried -m_open "You expect me to go into a sex shop?!"
    anon a_pocket "No freaking way!"
    jenny f_snide "Aww, is the little virgin afraid of a big scary sex shop?"
    anon "W-what, no..."
    anon "I just... Why can't you go?!"
    anon "I'll give you the money and you can-"
    jenny e_r f_annoyed "I have other stuff I need to do!"
    jenny e_w "Just man up and go, doofus."
    anon "F-fine."
    show jenny e_r
    pause
    hide jenny
    with dissolve
    pause
    anon @ -m_talk "( I can't believe she's making me do this... )"
    anon a_facepalm f_tired "( Ugh, let's just get it over with. )"
    hide anon
    with dissolve
    return


label jen08_bed2.alt:
    show jenny f_confused
    anon e_e -o_right "Okay, see ya."
    show jenny f_sad
    hide anon
    with dissolve
    pause
    jenny a_upset "No, wait!"
    pause
    show anon a_pocket f_horny_smug o_right at left
    show jenny a_fold f_angry_pouty
    with dissolve
    pause
    jenny f_sad "I don't want to say, it's embarrassing..."
    anon f_sceptical "Really?"
    anon "I don't think I've ever seen you embarrassed about anything before."
    show anon f_worried
    jenny "Can you just help me, please?"
    anon "{i}*Sigh*{/i} Fine."
    anon f_smug "... But only because you asked me so nicely."
    jenny e_r f_annoyed "Yeah, yeah, whatever."
    jenny e_w "I need you to go to the mall and buy something for me."
    anon f_pouty "Why does it always come down to money with you?"
    jenny "Don't be an asshole, you know I need the money."
    jenny "It's not that big a deal, it's only one hundred dollars..."
    anon f_shocked m_open @ -m_talk "That's a lot of money, [saga.cast.jenny]!"
    show anon f_surprised -m_open
    jenny e_r "Don't be stupid, one hundred dollars is nothing."
    show jenny e_w
    anon f_sceptical "{i}*Sigh*{/i} What's in it for me?"
    jenny "I dunno, I guess... I'll take everything off for you?"
    anon "You'll get completely naked in front of me, but you won't tell me what you're planning for money?"
    jenny a_hips f_angry m_teeth "You wanna see me naked or not?"
    anon a_think e_nw f_pensive @ -m_talk "..."
    anon a_pocket e_w f_calm "Alright..."
    anon f_horny "... But I get to look as long as I want."
    jenny a_side e_r f_annoyed -m_teeth "Ugh, fine... Within reason."
    jenny a_fold e_w "... And don't even think about touching because that's not happening, perv!"
    anon "Yeah, yeah..."
    jump jen08_bed2.merge


label jen08_bed2.rails:
    scene camera at stage
    show anon f_tired with dissolve
    anon @ -m_talk "( Ugh. )"
    anon @ -m_talk "( What could she possibly want this early in the morning? )"
    hide anon
    with dissolve
    return


label jen08_shop:
    return


label jen08_shop.ivy:
    anon "I'm looking for something called an electrum-"
    anon a_think e_nw f_pensive "No, that's not right..."
    anon e_w f_confused "... Electoral collage?"
    ivy f_confused "Electroclit?"
    anon f_happy "Yeah, that's it!"
    anon a_point f_calm "I'll take one of those, please and thank you."
    ivy f_shy "I'm afraid we're all sold out."
    anon a_side e_sw f_worried "Aww, man... seriously?"
    anon e_w "Are you getting more in stock anytime soon?"
    ivy f_happy "I certainly hope so..."
    ivy "... They've been our best seller for months now!"
    anon "Hmm, I guess I'll have to come back and check another day."
    return


label jen08_shop.jenny:
    show anon a_pocket f_worried o_right at left
    show jenny a_fold f_annoyed at right
    anon "What toy did you want me to get for you again?"
    jenny "Did you forget or something?!"
    anon "N-no, I didn't for-"
    pause
    anon f_sceptical "Ugh, just tell me!"
    jenny "You are worthless, you know that?"
    show jenny f_disgusted
    show anon f_worried
    pause
    jenny f_annoyed "Go to Pink on the second floor of the mall, and look for the Electro Clit."
    anon "Alright."
    jenny "Do I need to write it backwards on your forehead so you won't forget again?"
    anon e_b f_smug m_talk "No, I've got it this time."
    show anon e_w f_calm -m_talk
    jenny e_r "Psh, yeah right."
    show jenny e_w
    return


label jen08_shop.toy:
    scene toy_shop at stage
    show anon a_pocket f_worried with dissolve
    anon "( Sold out? )"
    anon "( That's not good, [saga.cast.jenny] is gonna flip out. )"
    pause
    anon a_think e_nw f_pensive "( Perhaps I should speak with the clerk about this... )"
    hide anon
    with dissolve
    return


label jen08_ivy:
    call shot.toy_shop_desk
    show jane a_toy_electro f_angry o_right at pos(.55)
    show ivy a_clasp f_shy at pos(.85)
    show anon a_pocket o_right at pos(.2) with dissolve.nowait
    jane "Yeah, okay, but this Electro Clit Light is terrible..."
    show anon a_phone e_s
    jane "... I can barely feel it!"
    ivy "I'm sorry that it failed to meet your expectations, but we do have a strict \"no returns\" policy on all our sex toys."
    ivy "I hope you can understand."
    jane "No, I don't understand!"
    show ivy f_confused
    jane f_sad "Listen, I'm currently battling a sex addiction and it's very important to my sobriety that I have a toy capable of getting me off!"
    jane "This could cause me to relapse!"
    ivy f_shy "Aww, I really wish I could help you but it's not up to me."
    jane f_angry "You seriously can't take this piece of shit back?"
    ivy "The boss would have my head if I did..."
    jane a_side @ f_curious "Well, could I get store credit or something?"
    ivy "No, I'm afraid not."
    pause
    ivy "I {i}can{/i} give you a coupon for five dollars off your next purchase..."
    ivy "... Does that help?"
    jane "No, it doesn't help!"
    pause
    jane @ f_sad "{i}*Sigh*{/i} Fine, give me the coupon..."
    jane "... {i}and{/i} I want a real Electro Clit!"
    jane "Not this crappy 'light' version!"
    ivy "Unfortunately, we're all sold out of the original right now..."
    jane "Ugh, seriously?!"
    ivy "... Again, I'm really sorry for the inconvenience, ma'am."
    jane "Oh my god... I am so gonna end up fucking some random guy that walks into the library, I just know it..."
    anon a_pocket e_w f_surprised @ -m_talk "( !!! )"
    anon a_wave f_shy @ -m_talk "( Hey, I'm a random guy who could walk into the library! )"
    show anon a_side e_b f_happy m_laugh
    ivy "You know, we do offer a fine selection of... {i}*ahem*{/i} massage options, that might interest you..."
    show anon e_w f_shy -m_laugh
    jane "Massage options?"
    ivy a_flyer f_happy "Why don't you have a look at our flyer?"
    show ivy a_clasp
    jane a_flyer_pink e_sw f_calm "Tsk, how exactly is a massage supposed to help me with my sex addiction-"
    jane "Oh!"
    jane f_horny "Oh, wow... okay!"
    pause
    jane a_side e_w "And will you be the one administering this \"massage?\""
    ivy f_horny "Mhmm."
    ivy "Assuming that's agreeable?"
    jane f_curious "Yeeeaah, umm..."
    show jane p_stand_turn
    show anon f_worried_surprised
    pause 1
    show anon a_shy_neck e_sw -o_right
    jane -p_stand_turn "... Actually..."
    show anon e_e f_worried
    show jane a_come_closer f_horny
    pause
    show anon a_side f_confused
    show ivy a_listen f_curious p_lean_in at pos(.78)
    show jane a_whisper p_lean_in
    ivy @ -m_talk "Hmm?"
    jane "..."
    ivy f_horny "Oh?"
    jane "..."
    show jane a_side -p_lean_in
    show ivy a_clasp -p_lean_in at pos(.85)
    show anon a_think
    ivy "Are you sure?"
    jane "Oh, definitely!"
    ivy a_giggle e_b f_happy m_laugh @ -m_talk "Heh!"
    ivy a_clasp e_w f_horny -m_laugh "I've never had anyone request that before!"
    hide ivy
    show jane m_lip
    with dissolve.nowait
    pause
    show jane f_curious p_stand_turn -m_lip
    show anon a_surprised_up f_surprised
    pause 1
    hide anon
    with dissolve
    jane @ -m_talk "..?"
    show ivy a_towel f_happy behind desk at pos(.825)
    with dissolve.nowait
    ivy "Come on back and we'll see where things go."
    jane a_hand_out f_horny -p_stand_turn "After you, Red."

    scene toy_shop at stage(.25, .525, 2)
    show anon a_surprised f_surprised o_right at left
    with fade
    anon @ -m_talk "( Did that seriously just happen or am I dreaming right now? )"
    anon a_think e_b f_happy @ e_nw f_pensive -m_talk "( I wonder if I could sneak a peek? )"
    pause
    show anon a_side e_w f_shy
    pause
    anon a_surprised f_surprised @ -m_talk "( !!! )"
    anon @ -m_talk "( Hey look, they left that toy sitting there on the counter! )"
    hide anon with dissolve
    return


label jen08_ivy.rails:
    scene toy_shop at stage
    show anon f_surprised o_right with dissolve
    anon @ -m_talk "( I think they're discussing the toy [saga.cast.jenny] wants! )"
    anon e_nw f_pensive @ -m_talk "( Maybe if I listen in I can find out where she got it. )"
    hide anon with dissolve
    return


label jen08_ivy.toy:
    jump jen08_shop.toy


label jen08_toy:
    call shot.toy_shop_desk
    show toy_shop -toy_electro
    show old_anon 287 with dissolve
    anon "( Hmm, it's not exactly what [saga.cast.jenny] wanted but it's pretty close. )"
    anon "( ... Maybe she won't notice the difference? )"
    show old_anon 3 with dissolve
    pause
    show old_anon 3 at face_left with dissolve
    pause
    show old_anon 3 at face_right with dissolve
    anon "( I probably shouldn't just take this thing without leaving her some money... )"

    if saga.cast.anon.cash:
        show old_anon 638b with dissolve
        anon "( ... She was looking for refund after all, so I think it will be fine. )"
    else:

        show old_anon 97b with dissolve
        anon "All I have is this lollipop..."
        show old_anon 93 with dissolve
        anon "Slightly used..."

    show old_anon 17 with dissolve
    anon "( Alright, now to get this thing home to [saga.cast.jenny] and claim my reward! )"
    hide old_anon
    with dissolve
    return


label jen08_toy.rails:
    scene toy_shop -ivy at stage
    show anon a_pocket f_worried o_right at left with dissolve
    anon @ -m_talk "Sold out?! I can't go back to [saga.cast.jenny] empty handed..."
    show anon a_think e_nw f_pensive
    pause
    anon a_point e_w f_calm @ -m_talk "... But maybe that toy on the counter would satisfy her?"
    hide anon
    with dissolve
    return


label jen08_stock:
    return


label jen08_stock.once:
    scene toy_shop_bed_side
    show ivy b_jane c_naked p_finger_anim s_12
    with fade
    ivy "Mmm, I've never had a customer offer to give {i}me{/i} the massage before..."
    jane "Does it feel good?"
    ivy "Yes, it certainly does."
    anon "( Oh wow, they're naked! )"
    pause
    anon "( And [saga.cast.jane] is fingering [saga.cast.ivy]!! )"
    ivy "You're quite skilled with your hands."
    jane "Heh, I've had a lot of practice at this."
    pause
    jane "How do you keep your pussy so tight in your line of work anyway?"
    jane "I can barely get two fingers inside you."
    ivy "Haah, it takes..."
    ivy "... A lot of work."
    jane "Yeah, I'll bet."
    pause
    ivy "Oh, that's the spot!"
    jane "Yeah, you like that?"
    ivy "Ngh, right there!!"
    pause
    anon "( Dang, [saga.cast.ivy] is close to cumming already? )"
    anon "( [saga.cast.jane] must really know what she's doing down there! )"
    pause
    jane "So how many free sessions do I get for that Electro Clit?"
    ivy "I don't know, I-"
    show ivy s_24
    jane "Hmm?"
    ivy "Oh, god!!"
    ivy "I-"
    pause
    ivy "Fuck, as many as you want!!"
    jane "Hehe, good answer."
    pause
    anon "( I'd best get out of here before they finish... )"
    anon "( .. don't wanna get caught. )"
    return


label jen08_stock.redo:
    scene toy_shop_bed_side
    show ivy b_jane c_naked p_finger_anim s_18
    with fade
    ivy "Too many! I can't-"
    jane "Of course you can."
    pause
    jane "Now cum for me."
    jane "Again!"
    ivy "NGGHHH!!!"
    return


label jen08_jenny:
    anon f_calm "I've got your toy."
    jenny a_hips f_annoyed "It's about time!"
    show anon a_backpack e_s f_shy
    pause
    anon a_toy_electro e_w f_calm "This is it, right?"
    jenny "Lemme see that!"
    show jenny a_palm

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen08_jenny.alt

    pause
    show anon a_pocket f_surprised
    jenny a_toy_electro e_wsw f_disgusted "..."
    jenny e_w f_angry m_teeth "This is an Electro Clit Light!"
    anon f_worried "Is that a bad thing?"
    jenny "Yes, it's a bad thing!"
    jenny "How stupid are you?"
    anon "I'm not-"
    jenny "There's no way this thing is going to get me off!"
    jenny "Why didn't you get me the original model, you idiot?!"
    anon f_tired "They were sold out..."
    jenny f_annoyed -m_teeth "Yeah, right. Sure they were."
    show jenny f_angry m_teeth
    anon f_worried "I'm serious!"
    jenny a_fold f_annoyed -m_teeth "I'm thinking, the deal is off..."
    anon "What?! C'mon [saga.cast.jenny], I spent good money on that!"
    jenny "That's not my problem."
    anon a_respect p_bow "Please?"
    jenny f_surprised "!!!"
    jenny f_snide "Oh, I like that... Beg me some more!"
    anon a_pocket -p_bow "Seriously?"
    jenny "Beg or the deal is off."
    anon a_respect p_bow "{i}*Sigh*{/i} Please, can I see you naked?"
    jenny "You have to say, \"I'm a pathetic little loser and I'll be a virgin forever.\""
    anon a_pocket f_sceptical -p_bow "What?! I'm not gonna-"
    show anon f_surprised
    jenny f_angry m_teeth "Do it or get out!"
    anon e_osw f_sad "..."
    anon "I'm a pathetic little loser and I'll be a virgin forever."
    jenny e_b f_calm m_laugh @ -m_talk "Hahahahaha!"
    show anon e_w
    jenny e_w f_snide -m_laugh "Alright, so long as you admit it."
    jenny "I guess you've earned a treat."
    show jenny f_annoyed p_top_off_01 with dissolve
    show anon f_calm
    jenny "You're only looking for one minute though!"
    jenny p_top_off_02 "Bringing me this stupid piece of crap toy..."
    show jenny p_top_off_03 with dissolve
    show jenny p_top_off_04
    pause
    show jenny a_pants_off_01 c_naked e_s f_calm -p_top_off_04
    pause
    show jenny e_b p_pants_off_02
    pause
    jenny a_hips e_w f_snide -p_pants_off_02 "There ya go, perv."
    anon f_surprised "!!!"
    show anon e_sw f_horny
    jenny f_annoyed "Try not to drool on my rug."
    show jenny f_disgusted
    anon e_w "W-wow, you shave down there..."
    show anon e_sw
    jenny f_annoyed "No shit?"
    jenny "Only old ladies and losers let their shit grow wild."
    pause
    jenny f_snide "Is this the first vagina you've ever seen?"
    anon a_uneasy e_w f_sceptical "Well, actually I-"
    show anon e_sw f_horny
    jenny e_r f_annoyed "Yeah, of course it is. What a stupid question to ask."
    show anon a_pocket
    jenny e_w f_snide "It'll probably be the last one you ever see too."
    jenny "Loser."
    pause
    jenny f_annoyed "Alright, times up!"
    anon e_w f_worried "Aww, c'mon [saga.cast.jenny]... Just a little more!"
    jenny f_angry m_teeth "No!"
    jenny f_annoyed -m_teeth "Screw ups like you don't get to ask for more!"
    jenny "Next time, do exactly what I tell you!"
    anon "{i}*Sigh*{/i} Fine."
    show anon e_sw f_horny
    pause
    jenny f_angry m_teeth "Now get out!"
    hide anon
    with dissolve
    $ renpy.end_replay()

    call shot.debbie_bed2_door
    with fade
    show anon a_pocket f_confused with dissolve
    anon @ -m_talk "( Sheesh, that was demeaning... )"
    anon @ e_b f_happy m_teeth "( I got to see her naked though. )"
    anon f_horny_smug @ -m_talk "( So, I guess it was worth it? )"
    pause
    anon a_think e_nw f_pensive @ -m_talk "( I wonder what she's planning to do for money now? )"
    hide anon
    with dissolve
    return


label jen08_jenny.alt:
    anon a_toy_electro_protect f_snide "Ah, ah!"
    anon "We had a deal, remember?"
    jenny a_hips f_angry m_teeth @ -m_talk "..."
    anon @ f_sceptical "You're a little overdressed, don't you think?"
    jenny e_r f_annoyed -m_teeth "{i}*Sigh*{/i} Fine."
    show jenny e_ssw f_snide p_top_off_01
    pause
    show jenny p_top_off_02
    pause
    show anon e_sw f_horny
    show jenny p_top_off_03 with dissolve
    show jenny p_top_off_04
    pause
    show jenny a_pants_off_01 c_naked -p_top_off_04
    pause
    show jenny e_b f_calm p_pants_off_02
    pause
    jenny a_hips e_w f_annoyed -p_pants_off_02 "There."
    jenny "Now let me see it!"
    anon e_w "Alright, here's your toy."
    show jenny a_toy_electro e_wsw f_disgusted
    show anon a_pocket
    pause
    jenny "Hey, this is the light version..."
    jenny e_w f_angry m_teeth "I wanted the original!"
    anon "Sorry, that's the only one they had."
    jenny "Well, what the fuck [saga.cast.anon]!"
    jenny "This thing is never gonna get me off!"
    anon "Like I said, it's the only thing they had."
    anon "Trust me, you're lucky to be getting that."
    anon "I had to jump through some hoops to get my hands on it."
    anon "Now stop bitching, you're ruining this for me!"
    show anon e_sw
    jenny e_r f_annoyed -m_teeth "Ugh, whatever..."
    show jenny a_hips e_w
    anon @ e_w "I really like that you shave down there..."
    jenny e_s f_happy "Y-you do?"
    jenny e_w f_angry m_teeth "I mean, shut up!"
    jenny "I don't care what you like, loser!"
    show jenny f_angry_pouty -m_teeth
    anon @ e_w "If you say so..."
    pause
    show anon d_hard z_b_f_a_d
    jenny e_wsw f_surprised "!!!"
    jenny "Is that-"
    anon e_w @ -m_talk "Hmm?"
    anon f_shy @ e_s "Oh, sorry."
    anon "I'm not used to-"
    anon e_sw f_horny "Well, you're really hot, you know?"
    jenny "That can't be your dick..."
    anon e_w f_confused "Uhh, yes?"
    jenny e_w f_annoyed "No fucking way!"
    jenny e_wsw "It's hu-"
    show jenny a_mute e_w f_surprised m_talk of_blush with dissolvefast.nowait
    pause
    anon f_horny "It's what?"
    show anon e_b f_happy m_teeth
    jenny a_hips f_angry m_teeth "Nothing."
    jenny "Are we done here?"
    anon e_w f_horny -m_teeth "Yeah, I guess that's good enough."
    show anon e_sw
    jenny f_annoyed -m_teeth @ e_r "Thank god."
    anon e_w "Are you blushing?"
    jenny f_angry m_teeth "N-no!"
    jenny "Get out!"
    anon e_e -o_right "Yeah, yeah... I'm going."
    hide anon
    with dissolve
    $ renpy.end_replay()

    call shot.debbie_bed2_door
    with fade
    show anon a_pocket d_hard f_horny z_b_f_a_d with dissolve
    anon @ -m_talk "( Well, that was hot! )"
    anon @ -m_talk "( She really seems to respond to me when I'm stern with her and don't take her crap. )"
    pause
    anon @ -m_talk "( I wonder what she's planning for money? )"
    hide anon
    with dissolve
    return


label jen08_jenny.area:
    anon f_calm "I've got that toy you wanted."
    jenny f_annoyed "Not here you ignoramus!"
    show anon f_worried
    jenny "Bring it to my room this afternoon."
    anon "Oh, right. Will do!"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
