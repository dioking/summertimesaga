label ano03_intro:
    scene debbie_bed3 at stage
    show anon a_pocket e_b f_happy m_teeth o_right with dissolve
    anon @ -m_talk "( Hmm, something smells really good! )"
    anon e_w f_calm -m_teeth @ -m_talk "( [saga.cast.debbie] must be making breakfast downstairs. )"
    anon @ -m_talk "( I should go say good morning to her. )"
    hide anon
    with dissolve
    return


label ano03_debbie:
    scene debbie_kitchen -debbie at stage
    show jenny a_juice f_annoyed at pos(.585)
    show debbie a_mug at right
    show anon a_pocket o_right at left with dissolve
    debbie "Good morning, sweetie."
    anon "Morning, [saga.cast.debbie]."
    anon "[saga.cast.jenny]."
    jenny @ e_r "Meh."
    pause
    anon "What smells so good?"
    show jenny a_juice_sip e_b f_calm m_drink
    debbie "Oh, I'm making a sausage and egg casserole."
    show jenny a_juice e_w f_annoyed -m_drink
    anon @ e_b f_happy m_laugh "That sounds amazing!"
    debbie "Well, there's plenty for everyone."
    debbie "Why don't you two go take a seat at the table and I'll bring you some."
    anon "Sweet!"
    jenny "Ugh, no thanks."
    debbie f_sad "You don't want any?"
    jenny f_angry m_teeth o_right "I just told you I'm doing a juice cleanse!"
    anon f_sceptical "Juice cleanse?"
    anon "What the heck is that?"
    jenny f_annoyed -m_teeth -o_right "It means I'm only drinking juice for the next three days, dummy."
    anon f_worried "Oh-kay..."
    anon "Why?!"
    jenny "I need to get rid of these love handles before beach season."
    anon "What love handles?"
    show debbie f_calm
    anon f_horny "You look fine."
    jenny f_disgusted "Don't be gross."
    show anon f_calm
    debbie "I don't think people do juice cleanses to lose weight, dear."
    jenny e_r f_annoyed o_right "Umm, yes they do..."
    jenny e_w "I was reading about it online."
    anon "Well, I think it sounds stupid."
    jenny f_angry m_teeth -o_right "You're stupid!"
    debbie f_annoyed "Enough!"
    show jenny f_angry_pouty -m_teeth
    show anon f_surprised
    debbie "I'm tired of you two fighting all the time!"
    jenny f_annoyed "He started it."
    anon f_worried "I did not!"
    debbie "I said, enough!"
    show anon e_osw f_sad
    "*Ding Dong*"
    show anon e_w f_worried
    debbie f_calm "Oh, that's probably the police lady coming to check in on us."
    jenny "Police lady?"
    debbie "[saga.cast.anon], would you go and let her in please?"
    anon "Yeah, okay."
    hide anon
    with dissolve
    debbie "Thanks, sweetie."
    jenny "Why are the police stopping by to check in on us?"
    debbie f_sad "{i}*Sigh*{/i}"

    scene debbie_lobby at stage with fade
    show anon a_pocket o_right with dissolve
    anon @ -m_talk "( A juice cleanse with apple juice... )"
    anon e_b f_happy m_laugh @ -m_talk "( What a moron. )"
    "*Ding Dong*"
    anon e_w f_worried -m_laugh "Yeah, yeah... I'm coming!"
    hide anon
    with dissolve
    return


label ano03_debbie.rails:
    scene camera at stage
    show anon a_pocket o_right at left with dissolve
    anon @ -m_talk "( That smell is coming from the kitchen! I can almost taste it! )"
    hide anon
    with dissolve
    return


label ano03_dimitri:
    play music villain fadeout 1 fadein 1 if_changed

    scene mono debbie_lobby_door1
    mono "When I opened the door, I was greeted not by a police lady\nbut instead a stern and ugly-looking thug all dressed in black." with fade
    mono "His tattoos and demeanor just screamed bad news."

    scene mono debbie_lobby_door2
    mono "And his greasy smile sent chills up my spine." with fade

    stop music fadeout 5

    call shot.debbie_lobby_door
    show dimitri a_clasp f_smug behind door at pos(.72)
    show anon a_pocket f_surprised o_right at left
    with fade
    anon "!!!"
    pause
    anon f_worried "C-can I help you?"
    dimitri "Nice place."
    anon "Umm..."
    anon "Thanks?"
    dimitri "Hmm, I am thinking you're [saga.cast.frank]'s son, yes?"
    anon "You knew my dad?"
    dimitri "Heh."
    dimitri "Yes, you could say this..."
    anon @ -m_talk "..."
    dimitri "Where is nice lady who takes care of you?"
    anon "Uhh, she's..."
    pause
    anon f_confused "W-who are you?"
    dimitri @ f_calm "Who am I?"
    dimitri "I am man at door."
    show anon f_worried
    dimitri "I am man asking to see nice lady responsible for you..."
    dimitri "... Lady who owes us big money."
    anon @ f_surprised "Big money?"
    anon "L-look man, we don't know anything about any of this..."
    anon "I really think you've made a mistake or something."
    dimitri "Ahh, talking, talking..."
    dimitri "Your father like talking too, you know?"
    dimitri "He talk all the way to the end."
    dimitri a_talk f_calm "\"You make mistake.\""
    dimitri "\"I no take money!\""
    dimitri f_smug "Yip, yip, yip."
    dimitri a_clasp "Like frightened little bunny."
    anon f_surprised "!!!"
    dimitri f_calm "Boss wants no more talking."
    dimitri a_point "He wants money back!"
    dimitri "You tell nice lady to be smart and pay up."
    show dimitri a_clasp
    anon "I..."
    anon "I think you should leave now."
    dimitri f_smug "Heh, so {i}this{/i} little bunny does have spine..."
    dimitri "I guess apple can fall far from tree."

    scene mono debbie_main_yumi
    mono "It was at that moment [saga.cast.harold]'s partner, [saga.cast.yumi], pulled up in her squad car." with fade

    call shot.debbie_lobby_door
    show dimitri a_clasp behind door at pos(.72)
    show anon a_pocket f_worried o_right at left
    with fade
    dimitri "Tsk, Tsk, police involvement not so good for you..."
    pause
    dimitri f_smug "Not so good idea for nice lady either."
    anon @ -m_talk "..."
    dimitri a_point f_calm "You give her message."
    dimitri @ a_throat "You tell her I come back here and things will get ugly."
    dimitri "Da?"
    anon @ -m_talk "..."
    show dimitri a_clasp e_e f_angry
    show yumi a_cautious f_sceptical behind dimitri at pos(.85)
    with dissolve.nowait
    yumi "E-excuse me?"
    show dimitri e_w
    show yumi o_right at pos(.425)
    yumi "Who are you?"
    dimitri f_smug @ a_out "Me?"
    dimitri "I am just old friend of family, come to pay respects."
    yumi "I'd like to ask you a few questions..."
    dimitri "Bah, I've no time for questions."
    dimitri "Much to do."
    dimitri @ a_stop "I go now."
    show dimitri a_side o_right at pos(.74)
    yumi f_angry "Now you hold on just one second!"
    pause
    dimitri a_out -o_right "Oh, are you planning to arrest me, Officer?"
    yumi f_sceptical "N-no, but-"
    dimitri a_side "Hmm, I did not think so..."
    show yumi f_angry
    pause
    dimitri a_point "See you soon, little bunny."
    hide dimitri with dissolve
    yumi @ -m_talk "..."
    pause
    yumi f_worried "Lock the door, kid."
    show anon a_reach at pos(.7)
    with dissolve

    scene debbie_lobby at stage
    show anon a_pocket at right
    show yumi e_b m_blow o_right
    with fade
    pause
    show yumi e_w -m_blow
    debbie "What's going on?!"
    show debbie a_mug f_sad o_right at pos(.15) with dissolve
    show yumi -o_right
    debbie "W-who was that?"
    yumi "Bad news, is who that was..."
    anon "Pretty sure it's the guy who's been threatening you on the phone."
    debbie a_shock f_surprised "!!!"
    yumi "I need to call this in."
    hide yumi with dissolve
    show debbie b_anon p_hug_away behind anon at pos.anon
    show anon e_osw f_sad p_debbie_hug_away
    debbie "Oh my goodness, are you alright?!"
    debbie "He didn't try and hurt you, did he?"
    anon "N-no, I'm fine."
    show debbie a_clasp f_sad -b_anon -p_hug_away at center
    show anon e_w f_worried -p_debbie_hug_away
    debbie "What did he say?"
    anon "He wanted money and... He..."
    anon e_osw f_sad "... Mentioned Dad."
    debbie @ a_shock "Oh, sweetie!"
    anon "[saga.cast.debbie], I think he had something to do with Dad's death."
    show debbie b_anon p_hug_away at pos.anon
    show anon p_debbie_hug_away
    debbie "Shh, it's okay... He's gone now."
    debbie "Everything is going to be alright."
    pause
    show debbie -b_anon -p_hug_away at center
    show anon e_w f_worried -p_debbie_hug_away
    debbie "C'mon, let's go sit down in the living room and see what the police officer can tell us."
    anon "Y-yeah, okay."
    hide debbie
    hide anon
    with dissolve

    scene debbie_lounge at stage(.675, .44, 2.2)
    show yumi a_phone_talk f_worried at left
    with fade
    show debbie a_mug f_sad at pos(.8)
    show anon a_pocket f_worried at pos(.6)
    with dissolve
    yumi "That's correct, sir."
    pause
    yumi f_angry "He can't have gone far."
    pause
    yumi f_sceptical "What?!"
    pause
    yumi "No, I don't understand, sir!"
    pause
    yumi "We can't just-"
    pause
    yumi f_worried "Y-yes."
    pause
    yumi "{i}*Sigh*{/i} Yes, sir."
    pause
    yumi "Very well."
    show yumi a_phone_close
    pause
    debbie "What's happening?"
    show yumi a_side f_calm o_right
    anon "Yeah, shouldn't you be calling for backup or something?"
    yumi "We put out an APB to our patrolmen, they're looking for the car now."
    yumi "I need to get a statement from you..."
    debbie "A statement?"
    anon "You mean you're not going after that guy?!"
    yumi f_worried "No, I've been expressly ordered not to pursue him."
    debbie @ -m_talk "..."
    anon "But he was making threats!"
    yumi "I know..."
    yumi "... And I'm sorry."
    pause
    yumi "{i}*Sigh*{/i} Look, it's very important that you tell me exactly what he said to you."
    anon "Uhh, I'm not sure..."
    anon "Everything happened so fast."
    yumi "That's understandable."
    yumi "This is a very stressful situation."
    show debbie a_none at pos.anon.hold
    show anon a_debbie_hold
    yumi "Let's just take a moment to breathe and calm down, alright?"
    anon @ e_b f_calm m_smoke "Y-yeah, okay."
    pause
    yumi a_notes e_ssw f_calm "Very good."
    yumi e_w "Now I need you to focus, [saga.cast.anon]."
    anon @ -m_talk "Mmhmm."
    yumi "What did the man say to you when you opened the door?"
    anon "He said, \"Nice place.\""
    yumi @ e_ssw "Okay, good."
    yumi "Then what did he say?"
    anon "He said I looked like my father, and then he asked after [saga.cast.debbie]."
    yumi @ e_ssw "Good."
    yumi "What next?"
    anon "He said his boss was done talking."
    anon "A-and that they wanted their money back."
    debbie "Pfft, how can we give back something we never took?!"
    yumi "You said he mentioned his boss?"
    anon "Yes."
    yumi "Did he say a name?"
    anon e_osw f_sad "N-no."
    yumi "{i}*Sigh*{/i} Alright."
    yumi "Anything else?"
    anon "Yeah, he said if we didn't pay up, he'd be back..."
    anon "... And that next time, things would get ugly."
    show debbie a_shock f_surprised at right
    show anon a_side
    debbie "!!!"
    yumi "Is that all he said?"
    anon e_w f_worried "I think so."
    show yumi a_side
    pause
    yumi "Thank you for your cooperation."
    debbie a_clasp f_sad "Are you going to tell us who that man was?!"
    yumi f_worried "{i}*Sigh*{/i} Truthfully ma'am, we don't know who he is."
    yumi "All I can tell you is that he's part of a criminal organization that's recently set up shop here, in Summerville."
    debbie f_surprised "Criminal organization?!"
    yumi "We're still trying to get a grip on the situation; but for now, my best advice for you both is to remain calm and stay vigilant."
    yumi "If they call, just hang up."
    yumi "If anyone suspicious comes knocking on your door, do not answer and phone the police immediately."
    anon f_sceptical "That's your advice?!"
    yumi "Lay low and don't give them any incentive."
    yumi "I'm going to personally be monitoring your neighborhood while my partner [saga.cast.harold] gets to the bottom of all this, okay?"
    debbie @ -m_talk "..."
    anon f_worried "I don't like this."
    yumi "Everything is going to be fine."
    yumi "We'll keep you safe, I assure you."
    debbie f_sad @ -m_talk "..."
    yumi "Ma'am, can you help me set up a schedule?"
    debbie @ -m_talk "Hmm?"
    yumi "Just the overview of everyone's weekly routine?"
    debbie "Y-yeah, sure."
    yumi "Thank you."
    hide yumi
    hide debbie
    with dissolve
    pause
    anon e_osw f_sad @ -m_talk "( I don't like this one bit. )"
    anon @ -m_talk "( {i}*Sigh*{/i} I need some air. )"
    hide anon
    with dissolve
    return


label ano03_dimitri.rails:
    scene debbie_lobby at stage
    show anon a_pocket o_right with dissolve
    "*Ding Dong*"
    anon @ -m_talk "( I should answer the door. )"
    hide anon
    with dissolve
    return


label ano03_outro:
    return


label ano03_outro.debbie:
    scene debbie_kitchen -debbie at stage
    show debbie a_mug f_sad at right
    show yumi a_notes o_right at pos(.35)
    debbie "[saga.cast.jenny] and I have a hair appointment on Tuesday."
    yumi "Down at Cindi Kim's?"
    show anon a_pocket f_worried o_right behind yumi at pos(.15) with dissolve
    debbie "Is that going to be a problem?"
    yumi "No, that'll be fine."
    pause
    yumi "Does your daughter go out much at night?"
    yumi "Like dancing with friends or anything?"
    debbie f_calm @ e_b f_happy m_laugh "Oh, goodness no!"
    debbie "She spends most of her time on the phone, or upstairs with that computer of hers."
    show debbie f_sad
    yumi "Okay."
    pause
    show yumi e_e
    anon "I guess I'm heading to school..."
    show yumi e_w
    debbie @ -m_talk "Hmm?"
    debbie "Oh, no you're not!"
    debbie "You're not leaving this house with that maniac running around."
    show yumi e_e
    anon "[saga.cast.debbie], I'm already months behind in my classes."
    anon "You really want me to miss more?"
    yumi a_side e_w "He's right, ma'am."
    yumi "You can't let these crazies prevent you and your family from living your lives."
    debbie "Y-yeah, but-"
    yumi "I assure you, we have a lot of patrols out combing the city for this guy."
    yumi "He will be perfectly safe."
    debbie @ -m_talk "..."
    debbie "Alright, just-"
    debbie "Be careful, okay?"
    show yumi e_e
    anon "I will be."
    hide anon with dissolve
    show yumi e_w
    debbie "This whole thing is making me a nervous wreck..."
    yumi f_worried "Everything is going to be fine, ma'am."
    pause
    yumi a_notes "Now then, where were we?"

    scene debbie_lobby at stage with fade
    show anon a_pocket f_worried o_right at left with dissolve
    anon @ -m_talk "( I don't like this one bit. )"
    anon e_osw f_sad @ -m_talk "( {i}*Sigh*{/i} I need some air. )"
    hide anon
    with dissolve
    return


label ano03_outro.jenny:
    scene debbie_landing at stage
    show jenny a_hips f_annoyed o_right at left
    show anon a_pocket f_worried at right with dissolve
    jenny "What's going on down there?"
    anon @ -m_talk "Hmm?"
    anon "Oh, some guy was at our door demanding money."
    jenny f_surprised "Huh?!"
    jenny "What guy?"
    anon "I don't know."
    anon "Some creepy guy with a bunch of tattoos and a crazy accent."
    jenny f_sad "Is he still down there?"
    anon "No, the cops showed up and he left."
    anon "[saga.cast.debbie] is down there talking to the police officer now."
    jenny "Do you think it was the same guy who's been calling her on the phone?"
    anon "Yeah, probably."
    pause
    jenny a_fold f_annoyed "Ugh, great."
    jenny "First your dad dies, sticking us with you..."
    jenny "... And now we're all going to be murdered."
    anon f_sceptical "Nobody is going to be murdered."
    anon "Quit being a bitch."
    jenny @ e_r "Whatever."
    jenny "I'm going to my room."
    hide jenny
    show anon f_worried
    with dissolve
    pause
    anon e_osw f_sad "( I don't like this one bit. )"
    anon "( {i}*Sigh*{/i} I need some air. )"
    hide anon
    with dissolve
    return


label ano03_outro.kitchen:
    scene debbie_lobby at stage
    show anon a_pocket f_worried o_right at left with dissolve
    anon @ -m_talk "( I shouldn't interrupt them.. )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
