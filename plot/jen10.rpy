label jen10_lobby:
    call shot.debbie_lobby_stairs
    show jenny a_phone c_casual e_ssw f_snide o_right at right
    show anon a_pocket f_worried o_right at left with dissolve
    pause
    anon "Where are you going?"
    jenny e_wsw f_annoyed "Out."
    show jenny e_ssw f_snide
    anon "Uhh, okay?"
    pause
    anon f_sceptical "Care to elaborate?"
    jenny e_wsw f_annoyed "Tch, I need to pick up some things from the mall..."
    show jenny e_ssw f_snide
    pause
    anon f_worried "What kind of things?"
    jenny e_r f_annoyed "None of your business, loser!"
    jenny "I don't know why you've always gotta have your nose in {i}my business{/i}?!"
    show jenny e_wsw f_disgusted
    pause
    show anon f_annoyed
    show jenny e_ne f_angry_pouty
    pause
    jenny a_fold e_w f_annoyed o_left "How much money do you have?"
    anon f_worried "Huh?"
    jenny "Give me two hundred dollars."
    anon @ f_sceptical "No way, I've given you tons of money already!"
    jenny e_r "Psh! Yeah, and you got stuff in return!"
    jenny e_w "Don't act like I haven't been more than fair with you..."

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen10_lobby.alt

    anon f_snide "Y-yeah, okay, but-"
    show anon f_surprised
    jenny "Quit being such a little bitch, [saga.cast.anon]!"
    jenny "You make plenty of money."
    jenny "Besides, you owe me for that little screw up with the toy the other day."
    anon a_think e_nw f_pensive @ -m_talk "( Ugh, I guess she's right about that... )"
    anon @ -m_talk "( ... And this might be a good opportunity to learn more about what she's doing for that money. )"
    jenny "Umm, hello?!"
    jenny "Earth to loser!"
    anon a_pocket e_w f_tired "{i}*Sigh*{/i} Fine."
    anon f_worried "You said two hundred?"
    jenny f_snide "Yup."

    if saga.cast.anon.cash < 200:
        anon a_uneasy "Erm, I don't have two hundred right now..."
        jenny f_annoyed "Ugh, you are worthless..."
        show anon a_side
        pause
        jenny "Well, go and get it!"
        anon a_wtf f_worried_surprised "Seriously?"
        jenny a_hips f_angry m_teeth "Yes!!"
        anon a_side f_tired "*Sigh* Fine, I'll be back."
        hide jenny
        with dissolve.nowait
        jenny "Hurry up!"
        hide anon
        with dissolve
        return

    label jen10_lobby.merge1:
    anon a_cash "Here."
    show anon a_side
    jenny a_money e_w f_annoyed "It's about freaking time..."
    show jenny a_money_count e_ssw f_snide
    pause
    anon "Can I go with you?"
    jenny a_hips e_w f_annoyed "What?! NO!"
    anon f_annoyed "C'mon!"
    jenny "Absolutely not!"
    jenny "I'm not going out in public with a loser like you..."
    show jenny f_disgusted
    anon "... But I've given you so much money and-"
    jenny f_annoyed "You are such a pain in my ass."
    anon a_respect p_bow "P-please?!"
    pause
    jenny e_r "{i}*Sigh*{/i} Fine, just quit whining."
    show jenny e_w
    anon a_pocket f_calm p_stand "Sweet!"
    jenny o_right "And don't walk too close! I don't want people thinking we're together."
    hide jenny
    with dissolve
    anon f_worried "O-okay."

    if saga.cast.anon in saga.sets.debbie_bed2:
        show anon a_side
        pause
        show jenny c_casual at pos(.6)
        with dissolve
        show anon o_left
        hide jenny
        with dissolve

    hide anon
    with dissolve
    return True


label jen10_lobby.alt:
    anon "Alright, so what do I get this time?"
    jenny a_hips "Tsk, you ain't getting shit."
    anon f_annoyed "Fine."
    show jenny f_confused
    anon e_e o_left "Have fun shopping."
    hide anon
    with dissolve
    jenny a_side f_annoyed "W-wait!"
    pause
    show anon a_pocket f_snide o_right at left
    show jenny a_fold f_angry_pouty
    with dissolve
    pause
    jenny f_annoyed "Grr, damn it!"
    show jenny f_angry m_teeth
    pause
    jenny a_hips f_annoyed -m_teeth "Why won't you just do what I fucking ask?!"
    anon f_worried @ f_sceptical "Why don't you ever ask me nicely?"
    jenny "C'mon, [saga.cast.anon]!"
    jenny "You owe me for that screw up with the toy the other day."
    anon a_think e_nw f_pensive @ -m_talk "( Man, screw her. She's lucky I bought her that toy at all... )"
    anon @ -m_talk "( ... Then again, this might be a good opportunity to learn more about what she's doing for that money. )"
    jenny "So are you gonna give me the money or not?"
    anon a_pocket e_w f_worried @ f_sceptical "Yeah, I guess... if you say please."
    jenny @ f_worried "Ugh..."
    jenny a_side @ e_r "... Please?"
    show jenny e_ne f_angry_pouty

    if saga.cast.anon.cash < 200:
        anon a_uneasy f_shy "Actually, I don't have two hundred on me right now..."
        show anon a_pocket
        jenny a_hips e_w f_angry m_teeth "Are you fucking kidding me?"
        show anon f_surprised
        pause
        jenny a_point "Well, go and get it!"
        anon f_grumpy "Yeah, yeah..."
        jenny a_fold "I'm serious!"
        anon "I'll get it, just chill out."
        hide jenny
        with dissolve.nowait
        jenny "Hurry up!"
        hide anon
        with dissolve
        return

    label jen10_lobby.merge2:
    anon a_cash "Here."
    show jenny a_palm e_w f_confused
    anon a_cash_protect f_smug "... But I'm coming with you."
    jenny a_surprised f_surprised "What?!"
    jenny a_upset f_angry m_teeth "No fucking way!"
    anon f_snide "You want the money or not?"
    jenny a_side f_angry_pouty -m_teeth @ -m_talk "..."
    anon a_fold f_smug "I'm coming."
    jenny a_fold f_annoyed "Fine!"
    show anon a_cash
    pause
    show anon a_side
    jenny a_money "You are such a pain in my ass..."
    jenny a_side o_right "... And don't walk too close! I don't want people thinking we're together."
    hide jenny
    show anon a_wtf
    with dissolve
    anon "Yeah, whatever."

    if saga.cast.anon in saga.sets.debbie_bed2:
        show anon a_side
        pause
        show jenny c_casual at pos(.6)
        with dissolve
        show anon o_left
        hide jenny
        with dissolve

    hide anon
    with dissolve
    return True


label jen10_retry:
    anon f_shy @ -m_talk "..."
    jenny f_confused "Have you got my money yet?"

    if saga.cast.anon in saga.sets.debbie_bed2:
        if saga.cast.jenny.dom < saga.cast.jenny.sub:
            jump jen10_lobby.merge2

        jump jen10_lobby.merge1

    anon f_calm "Yup."
    jenny f_calm "Fucking finally!"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny e_s p_table_rise

    jenny "I hope they haven't sold out already."
    hide jenny

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon e_w
        show debbie_dining_table pull2
    else:

        show anon o_right

    with dissolve.nowait
    anon f_confused "Sold out of what?"
    pause
    anon f_worried "Hey, you forgot the money!"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show debbie_dining_table pull3

    hide anon
    with dissolve
    return


label jen10_retry.alt:
    anon f_grumpy "Money doesn't grow on trees, you know?"
    jenny "Don't try lecture me!"
    anon "Then don't act like a spoiled child!"
    jenny "I'm not-"
    show jenny f_angry_pouty
    pause
    jenny f_annoyed "Grr, just hurry up!"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show debbie_dining_table pull3

    hide anon
    with dissolve
    anon f_calm "Yeah, yeah."
    return


label jen10_retry.busy:
    anon f_shy "Ready for that mall trip?"
    jenny "Not today."
    anon f_confused "What do you mean, \"not today.\"?"
    jenny a_fold f_annoyed "It means exactly what it sounds like..."
    jenny "... Come back another time, doofus!"
    anon f_surprised "You're serious?"
    jenny @ -m_talk "Mhmm."
    show anon f_confused
    pause

    if 'debbie_dining_table' not in renpy.get_showing_tags():
        show jenny a_point

    jenny f_disgusted "Umm, this is the part where you leave!"
    anon f_grumpy "Ugh, fine."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show debbie_dining_table pull3

    hide anon
    with dissolve
    return


label jen10_retry.cash:
    anon f_shy @ -m_talk "..."
    jenny f_confused "Have you got my money yet?"
    anon "Not yet."
    jenny f_annoyed "Ugh, what is taking so long?!"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen10_retry.alt

    anon f_worried "I'm working on it."
    jenny "Well, work faster!!"
    anon f_grumpy "Alright, sheesh."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show debbie_dining_table pull3

    hide anon
    with dissolve
    jenny f_disgusted "Ugh, broke guys are so gross."
    return


label jen10_depart:
    call shot.debbie_lobby_stairs
    show anon a_pocket at pos(.3)
    pause
    show jenny a_wave_off c_casual o_right at pos(.15) with dissolve.nowait
    jenny "Out of my way, limp dick!"
    show jenny a_side at right
    anon f_snide o_right "Umm, aren't you forgetting something?"
    jenny f_confused o_left @ -m_talk "Hmm?"
    show anon f_smug
    pause
    jenny f_worried "Oh, right."
    show jenny e_sw f_horny

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jump jen10_lobby.merge2

    jump jen10_lobby.merge1


label jen10_depart.rails:
    scene camera at stage
    show anon f_confused
    anon @ -m_talk "( Did [saga.cast.jenny] seriously just leave without the money? )"
    anon f_shy @ -m_talk "( I suppose I'd better chase her down before she makes an ass out of herself. )"
    hide anon
    with dissolve
    return


label jen10_grace:
    scene mall_hall1 at stage
    show anon a_pocket f_worried o_right at pos(.55)
    show jenny a_fold c_casual f_annoyed o_right at right
    with dissolve
    anon "Would you slow down?!"
    pause
    anon f_sceptical "[saga.cast.jenny]!"
    jenny "Don't talk to me."
    anon f_grumpy "Ugh, why do you always have a stick up your butt?"
    anon "Can't you just be chill for a little while?"
    jenny "No, I can't be chill. Not when I have a loser shadowing my every move."
    anon f_worried "Nobody is even looking at us, [saga.cast.jenny]!"
    jenny e_r "Whatever."
    show jenny e_w
    pause
    anon "Where are we going anyways?"
    pause
    anon f_grumpy "I'm just gonna keep asking, you know?"
    pause
    anon f_pouty "[saga.cast.jenny], where are we-"
    show anon f_surprised
    jenny f_angry m_teeth o_left "Grr, we're going to Pink on the second floor, okay?!"
    anon f_worried "More sex toys?"
    jenny f_annoyed -m_teeth "I swear to god, if you don't shut up, the only place you're going is the hospital."
    jenny "To get my foot surgically removed from your ass."
    anon f_pouty @ f_bored "Heh, good one."
    show jenny o_right
    pause
    anon f_worried "I don't know what you're so bent out of shape for anyways..."
    anon "Like I said, nobody here cares if we're tog-"

    if saga.cast.eve < 'cheer':
        grace "[saga.cast.jenny]?!"
    else:
        grace "[saga.cast.anon]?!"

    show anon f_surprised
    show jenny f_surprised
    pause
    show anon o_left
    show jenny f_sad o_left
    show grace a_hip o_right at left
    with dissolve

    if saga.cast.eve < 'cheer':
        jenny "[saga.cast.grace]?"
    else:
        anon "[saga.cast.grace]?"

    show anon f_calm

    if saga.cast.eve < 'cheer':
        grace "Oh my god, it is you!"
        grace "I haven't seen you since high school!"
        jenny f_annoyed @ e_r "Ehh, yeah..."

    if saga.cast.eve < 'games':
        grace "How have you been?"
        jenny "I'm fine."
        grace "Well, that's good."
        pause
        grace "I'm doing great too."
        grace "I opened up my own tattoo parlor, over on the north side of town."
        grace "Sugar Tats."
        grace "You heard of it?"
        jenny "No."
        grace "Oh, you have to come check it out!"
        grace "We get pretty busy in the evenings but if you came before that we'd have time to chat and catch up."
        jenny "Yeah, no thanks [saga.cast.grace]..."
        grace "Ah, you're probably busy, huh?"
        grace "What are you doing for work nowadays?"

        if saga.cast.jenny.dom < saga.cast.jenny.sub:
            anon f_snide @ e_b f_happy m_laugh "Heh, yeah [saga.cast.jenny]... what are you doing for work?"
            jenny f_sad "I uhh..."
        else:

            jenny f_surprised "I uhh..."
            anon f_worried "H-hi, I'm [saga.cast.anon]."
            show jenny f_calm

        grace "Oh, I'm sorry. I didn't know you two were together."
        grace "I'm [saga.cast.grace]."
        anon f_calm "Nice to meet you."
        grace @ e_b f_happy m_laugh "Wow, [saga.cast.jenny]! Your boyfriend is cuuuute!"
        show jenny f_angry m_teeth
        anon f_worried "Oh, I'm not-"
        show anon f_surprised
        jenny f_annoyed -m_teeth "Ugh, he is {i}not{/i} my boyfriend!"
        anon f_worried "I'm her roommate."
        grace "Oh, I see."

    elif saga.cast.eve < 'cheer':
        anon "Hello, [saga.cast.grace]."
        grace "Hey, [saga.cast.anon]."
        grace "What are you-"
        pause
        grace f_surprised "Wait a minute, you two aren't... together, are you?!"
        anon f_surprised m_teeth @ -m_talk "!!!"
        jenny f_disgusted "Umm, fuck no!"
        anon e_osw f_sad -m_teeth "..."
        jenny "Gross!!"
        anon e_w f_worried "[saga.cast.jenny] is my roommate."
        grace "O-oh."
        grace f_calm @ e_b f_happy m_laugh "Phew, that's a relief!"
        pause
        grace "So..."
    else:

        grace "Fancy meeting you here."
        grace "[saga.cast.eve] isn't with you?"
        jenny f_annoyed "What the fuck?"
        grace @ e_b f_happy m_laugh "Whoa!!"
        grace "Is that, [saga.cast.jenny]?!"
        jenny f_angry m_teeth "Who's [saga.cast.eve]?"
        grace "I haven't seen you since high school!"
        grace "What are you-"
        pause
        grace f_sad "Wait a minute, you two aren't... together, are you?!"
        show anon f_surprised m_teeth
        jenny f_annoyed -m_teeth @ e_r "Pfft, like I would ever-"
        anon f_worried -m_teeth "No, no, no!!"
        show jenny f_angry m_teeth
        anon "We are definitely not together, I promise you!"
        pause
        show anon e_e
        pause
        anon "What?"
        show anon e_w
        jenny "He's my roommate."
        grace "O-oh."
        grace @ f_calm "Phew, I was worried I'd have to kick your ass for a second there, [saga.cast.anon]..."
        grace "Umm, y-you know... for [saga.cast.eve]'s sake."
        show grace f_calm
        pause
        grace "So, [saga.cast.jenny]..."

    grace "You're still living at home then?"
    jenny e_r f_annoyed m_idle "N-not because I have to or anything..."
    jenny e_w "They're just... having money problems and I'm helping them out, you know?"
    anon @ -m_talk "..."
    grace "Oh, I can totally relate."
    grace "I took my sister in a couple years ago, after our parents died."

    if saga.cast.eve > 'cheer':
        jenny "[saga.cast.eve], I assume?"
        anon @ e_e "Yup."

    grace "She's been living with me ever since."
    grace "Family comes first, right?"
    jenny "I didn't know you have a sister..."
    grace "Oh, yeah... she's younger than us."

    if 'games' < saga.cast.eve < 'cheer':
        anon f_calm "She's in my class."

    jenny e_r "Yeah, that's great..."
    show jenny e_w
    show anon f_worried
    pause

    if saga.cast.eve < 'games':
        jump jen10_grace.merge

    if saga.cast.eve < 'cheer':
        grace "You know, [saga.cast.jenny], you're welcome to come meet her."
    else:
        grace "You're welcome to come meet her... if you want?"

    grace "My tattoo parlor is over on the north side of town."

    if saga.cast.eve < 'cheer':
        grace "Maybe we could all hang out sometime?"
    else:
        grace "I'm sure she'd love to-"

    jenny "You own a tattoo parlor?"
    grace @ e_b f_happy m_laugh "Yup!"
    grace "Sugar Tats."
    grace "You haven't heard of it?"
    jenny "No."
    anon f_calm "It's really awesome!"
    grace @ e_b f_happy m_laugh "Hehe, thanks [saga.cast.anon]!"
    jenny @ e_r "Eugh..."

    if saga.cast.eve < 'cheer':
        grace "We get pretty busy in the evenings but if you came before that we'd have time to chat and catch up."
    else:

        grace "Just come with [saga.cast.anon] next time."
        grace "We'll rent a movie or something."

    jenny "Yeah, no thanks [saga.cast.grace]..."
    grace "Ah, you're probably busy, huh?"
    grace "What are you doing for work nowadays?"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon e_b f_happy m_laugh @ -m_talk "Heh, yeah [saga.cast.jenny]... what are you doing for work?"
        jenny f_angry m_teeth "Shut up, [saga.cast.anon]!!!"
        anon @ -m_talk "Haha!"
        show anon e_w f_calm -m_laugh
        jenny f_sad -m_teeth "I uhh..."
        pause
        jenny f_angry m_teeth "Tsk, who asked you to be so nosy, anyways?"
        grace f_sad "Oh, umm... my bad."
        grace "I was just trying to catch up."
        jenny f_annoyed -m_teeth @ e_r "Eugh."
    else:

        jenny f_surprised "I uhh..."
        show jenny f_sad
        show anon f_worried
        pause

        if saga.cast.eve < 'cheer':
            anon f_shy "H-hey, [saga.cast.grace]... Umm, how is [saga.cast.odette] doing?"
            show jenny f_calm
            grace @ -m_talk "Hmm?"
            grace "Oh, you know her, she's a handfull."
            anon f_calm @ e_b f_happy m_laugh "Heh, totally."
            grace "Her newest thing is trying to convince me into taking some yoga classes at the gym."
            grace @ e_r f_annoyed "Like we can afford that..."
        else:

            anon f_shy "H-hey, [saga.cast.grace]... What brings you here?"
            grace @ -m_talk "Hmm?"

            if saga.cast.grace < 'nuru':
                grace "[saga.cast.odette] used up the last of my massage oil the other day."
            else:

                grace "Oh, I used up the last of my massage oil the other day, when you and I-"
                show jenny f_annoyed
                show grace f_surprised
                show anon f_surprised m_teeth
                pause
                grace "{i}*Ahem*{/i} I mean, when [saga.cast.odette] and I..."

            jenny f_angry m_teeth @ -m_talk "..."
            anon f_shy m_idle "I'm surprised you didn't send her to pick some up."
            grace f_calm @ e_b f_happy m_laugh "Hah, I can't trust her to get the right stuff."
            grace @ e_r f_annoyed "Last time she brought home some strawberry flavored off brand... it was awful!"
            anon f_calm @ e_b f_happy m_laugh "Haha!"
            jenny f_annoyed -m_teeth @ e_r "Eugh."

    if saga.cast.eve < 'cheer':
        grace f_calm "Oh, that reminds me..."

    label jen10_grace.merge:
    if saga.cast.eve < 'cheer':
        grace "Oh, I ran into [saga.cast.cedric] the other day."
        grace "He mentioned you guys had broken up."
        jenny "Yeah, I need someone more motivated than boring old [saga.cast.cedric]."
        grace "Aww, I always thought he was kinda sweet..."
        show jenny f_angry m_teeth
        grace "... But I imagine you're looking for bigger fish, eh?"
        grace "You always were popular with the guys."
        jenny f_annoyed -m_teeth "You know, [saga.cast.grace]... this has been fun and all, but I'm really busy, so if you don't mind?"

        if saga.cast.eve < 'games':
            grace "Oh, right... sorry."
            grace @ e_b f_happy m_laugh "I could jabber on all day, hehe."
        else:

            grace "Y-yeah, okay."
    else:

        jenny "You know, [saga.cast.grace]... this has been fun and all, but we're busy, so if you don't mind?"
        grace f_calm "Y-yeah, okay."

    pause
    grace "Why don't I give you my card, in case you change your mind-"
    jenny "NO, no... that's okay."
    jenny "I won't."
    show grace f_sceptical
    jenny "Come on, loser."
    hide jenny
    with dissolve
    pause
    show anon o_right
    pause
    anon o_left "S-sorry about that."
    grace f_calm "It's alright. I wasn't expecting anything different."
    grace "She hasn't changed one bit since high school."
    anon "Yeah."

    if saga.cast.eve > 'cheer':
        grace "It's hard to believe you live together."
        anon @ e_b f_happy m_laugh "Heh, tell me about it."

        if False:
            grace f_horny "You coming by the house later?"
            show grace f_surprised
            pause 1
            grace f_nervous "Y-you know, to see my sister?"
            anon "Yeah, of course."
            grace f_calm "Cool."
            pause

    anon "I should probably catch up with her."
    grace @ e_b f_happy m_laugh "Hehe, good luck."
    anon f_calm "Thanks."
    hide grace
    with dissolve
    pause
    show anon a_salute f_sceptical o_right at pos(.65)
    anon @ -m_talk "( Hmm, now where did [saga.cast.jenny] go? )"
    anon @ -m_talk "( She said she was headed towards, Pink... I should check there. )"
    hide anon
    with dissolve
    return


label jen10_grace.rails:
    scene camera at stage with None
    show jenny a_hips f_annoyed at right
    show anon
    with dissolve
    jenny "Umm, hello?!"
    anon f_confused o_right @ -m_talk "Hmm?"
    jenny "Are you coming to the mall with me or not?!"
    hide jenny with dissolve.nowait
    anon f_shy "Yup, I'm right behind you."
    hide anon with dissolve
    return


label jen10_shop:
    scene toy_shop at stage
    show jenny a_fold c_casual f_annoyed at right
    show anon a_pocket f_sceptical o_right at left with dissolve
    anon "There you are."
    show anon f_worried
    jenny @ -m_talk "..."
    anon f_pouty "You just took off on me."
    jenny "I can't stand that stupid bitch!"
    anon f_worried "Really?"
    anon "She was just being nice."
    jenny "Yeah right, trying to rub all her success in my face!"
    jenny "She's always been jealous of me."

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon f_pouty "Yeah, you're probably right."
        anon "I mean, you're a broke, boyfriendless, college dropout..."
        anon "... Who's stuck living at home with your mother."
        anon "Who wouldn't be jealous?"
        jenny f_angry m_teeth "{i}*Gasp*{/i} Fuck you!!"
        jenny "Grr!"
        jenny f_annoyed -m_teeth "Just-"
    else:

        anon "[saga.cast.jenny], she was just trying to be friendly..."
        show anon f_surprised
        jenny f_angry m_teeth "No, fuck her!"
        jenny f_annoyed -m_teeth "I don't even want to talk about it."

    jenny "Just help me find these stupid toys."
    anon f_worried "Okay, what are we looking for?"
    jenny "I need the UltraVibe 2000 annnnnd..."
    jenny a_toy_plug f_snide "... This!"
    anon a_surrender e_sw f_shocked m_open @ -m_talk "!!!"
    anon a_think f_sceptical -m_open "Is that a butt plug?"
    show anon e_w
    jenny f_annoyed "Umm, yeah?"
    anon a_surprised_up f_worried_surprised "It's huge!"
    anon "You're not really going to stick that in your ass, are you?"
    show anon a_side
    jenny e_r "They said to get something big."
    show jenny e_w
    show anon f_confused
    pause
    anon "They?"
    show jenny f_worried
    anon "Who's they?"
    jenny a_side f_annoyed "Never you mind!"
    jenny "Quit being a nosy perv and go find that UltraVibe 2000!"

    if saga.prop.toy_vibe in saga.cast.anon:
        show anon a_think e_nw f_pensive
        pause
        show anon a_backpack e_s
        pause
        anon a_toy_vibe e_w f_confused "You mean one of these?"
        jenny f_confused "Umm, why do you own one of those?"
        anon f_worried "I just thought-"
        show anon f_worried_surprised
        jenny a_wave_off f_disgusted "You know what, nevermind..."
        jenny a_side "... I don't wanna know."
        jump jen10_toy.merge

    anon a_point_self f_surprised "M-me?!"
    anon a_pocket f_sceptical "It's your toy, why don't you go find it?!"
    show anon f_surprised
    show jenny a_hips f_angry m_teeth
    pause
    anon e_osw f_sad "Ugh, fine."
    hide anon
    with dissolve
    pause
    show jenny a_toy_plug e_ssw f_snide -m_teeth
    pause
    jenny e_w f_sad @ -m_talk "( Maybe I {i}should{/i} get more lube while I'm here... )"
    hide jenny
    with dissolve
    return


label jen10_shop.rails:
    scene camera at stage
    show anon with dissolve
    anon @ -m_talk "( I should catch up with [saga.cast.jenny]. )"
    anon @ -m_talk "( She said she was heading towards Pink on the second floor. )"
    hide anon
    with dissolve
    return


label jen10_toy:
    scene toy_shop at stage
    show jenny a_toy_plug c_casual f_annoyed at right
    show anon a_toy_vibe f_worried o_right at left with dissolve
    anon "I think this is the right one?"
    jenny "Ugh, it's not that hard to figure out, dummy... everything is labeled."
    label jen10_toy.merge:
    show anon e_sw f_worried
    "*Click*"
    show anon f_surprised
    "*BZZZZZZ*{nw=1}"
    show jenny f_angry m_teeth
    anon @ f_shocked m_open "!!!" with hpunch
    anon "Whoa!"
    anon "This thing is crazy!"

    if saga.prop.toy_vibe in saga.cast.anon:
        show jenny a_toy_vibe
    else:
        show jenny a_toy_plug_vibe

    show jenny f_annoyed -m_teeth at pos(.65)
    show anon a_surrender e_w
    with dissolvefast
    jenny "Give me that!"
    jenny "You're hopeless."
    anon a_pocket f_worried "What are you doing with all this stuff [saga.cast.jenny]?!"
    jenny "None of your business, loser."
    anon @ f_sceptical "I'm going to find out eventually, you know?"
    jenny "Whatever."
    hide jenny
    with dissolve

    call shot.toy_shop_ivy
    show jenny a_toy_plug_vibe c_casual o_right at pos(.375)
    with fade

    if saga.prop.toy_vibe in saga.cast.anon:
        jenny "I'll take this."
        show jenny a_toy_vibe
    else:

        jenny "I'll take these."
        show jenny a_side

    ivy "Oh, those UltraVibes are great!"

    if saga.prop.toy_vibe in saga.cast.anon:
        show jenny e_s

    ivy "Crazy powerful."

    if saga.prop.toy_vibe in saga.cast.anon:
        show jenny a_side

    jenny e_w "Uh huh, could you just ring me up, please?"
    ivy f_shy @ -m_talk "..."
    show anon o_right at pos(.175)
    ivy a_toy_plug "Have you ever used one of these before?"
    jenny f_sad "No, why?"
    ivy "You should really start with something smaller, sweetie..."
    show ivy a_clasp
    jenny a_fold f_annoyed "Nah, it's fine... I've got lube."
    show jenny a_money
    show anon f_surprised
    pause
    show ivy a_money
    jenny a_hips f_snide "Besides, it's for him."
    show ivy a_clasp
    anon m_teeth @ -m_talk "!!!" with hpunch
    ivy f_happy "Oh, really?"
    anon @ f_shocked m_open "It's not for me!"
    show ivy a_giggle e_b m_laugh
    jenny e_b f_calm m_laugh @ -m_talk "Hahahahaaah!"
    anon f_grumpy -m_teeth "Not funny."
    show ivy a_clasp e_w f_shy -m_laugh
    jenny e_w f_snide o_left -m_laugh "C'mon loser, let's go home."
    show anon e_e
    hide jenny
    with dissolve
    pause
    anon a_uneasy e_w f_worried "Seriously, that's not for me."
    ivy f_happy @ e_b m_laugh "Hehe, there's no need to be embarrassed... I think it's hot."
    anon a_pocket e_osw f_sad "{i}*Sigh*{/i}"
    hide anon
    with dissolve
    return True


label jen10_toy.ivy:
    call shot.toy_shop_ivy
    show anon a_think e_nw f_worried at left with dissolve
    anon @ -m_talk "..."
    ivy "Can I help you find something, cutie?"
    anon a_uneasy e_w f_shy o_right "Oh, umm... an Ultra Vibe 2000, please."
    ivy "Aww, is it a gift for your girlfriend?"
    anon f_worried_surprised "Err, no... it's for my-"
    show anon a_surprised o_left
    pause
    show anon a_whisper o_right at pos(.4)
    anon "{size=-8}My roommate.{/size}"
    ivy a_listen f_confused p_lean_in "Sorry, I didn't catch that..."
    anon a_side f_worried @ e_e -m_talk "..."
    show anon a_whisper at pos(.55)
    anon "It's for my roommate."
    show anon a_side
    ivy f_surprised "Your roommate?!"
    ivy f_horny "My, what a lucky girl."
    show anon f_shy
    ivy a_clasp f_happy p_stand "Check the wall just behind you."
    ivy "Blue and purple toy, ribbed for her pleasure."
    anon "R-right, thanks."
    hide anon
    with dissolve
    return


label jen10_toy.other:
    scene toy_shop at stage(.3125, .5, 1.6)
    show anon f_surprised at pos(.6)
    anon @ -m_talk "( Man, there's so many toys in here... )"
    anon a_think e_nw f_pensive o_right @ -m_talk "( ... But which one is the UltraVibe 2000? )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
