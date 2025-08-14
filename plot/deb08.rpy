label deb08_lobby(busy):
    call shot.debbie_lobby_bench
    show debbie a_clasp c_casual o_right
    show anon a_pocket at right with dissolve
    debbie "Morning, sweetheart."
    anon "Hey, [saga.cast.debbie]."
    anon "Don't you look nice today..."
    anon "... Going somewhere?"
    debbie "Oh, I just need to run to the mall and pick up a few things for dinner this week."
    label deb08_lobby.merge:
    debbie @ -m_talk "..."

    if busy:
        jump deb08_lobby.busy

    if saga.cast.debbie < 'mall.pre':
        debbie "Say, why don't you join me?"
        anon f_surprised "What, really?"
        debbie "Yeah, come on!"
        debbie "It'll be nice to spend the day together, don't you think?"
        anon f_happy "Yeah, it would."
        debbie "Plus, you can help me with the loading and unloading."
        anon f_smug "Ahh, so there's the truth of it."
        anon a_hips @ e_b "You just want me along for my muscle!"
        debbie f_happy @ e_b m_laugh "Hehe!"
        debbie "No... of course not!"
        anon a_fold f_sceptical "Uh huh."
        debbie a_hips f_shy "Ohh, don't be like that..."
        debbie "... Won't you come and help your poor old landlady out?"
    else:

        debbie "Say, why don't you come and help your poor old landlady out?"

    show anon e_nw f_pensive

    menu:
        "Yes.":
            pass
        "No.":

            jump deb08_lobby.bail

    show debbie f_curious
    anon a_finger e_w f_sceptical "Okay, first off..."
    show debbie f_happy
    anon "... You are not old..."
    anon a_fingers_two f_calm "... And secondly, I'd love to help!"
    anon "I've really been enjoying our time together recently."
    show anon a_surprised f_happy_surprised behind debbie
    show debbie a_touch_anon_face f_calm at pos.anon.touch_face
    debbie "Aww, me too, sweetie!"
    debbie "Me too."
    pause
    anon a_side f_shy "So, ehh... did you wanna go now?"
    debbie a_embarrassed f_surprised "Oh, right... yes!"

    if 'o_right' in renpy.get_attributes('debbie'):
        show debbie o_left at center
    else:
        show debbie o_right at center

    debbie a_purse_02 e_s f_shy of_blush "{i}*Ahem*{/i} Let me just-"
    debbie a_purse s_800ms "Tsk, where did I put those darn keys?!"
    show anon f_confused
    pause
    debbie a_purse_02 e_e "You go on ahead, sweetie."
    debbie "I'll meet you in the car."
    show debbie a_purse e_s
    anon f_shy "Alright, sounds good."
    hide anon with dissolve
    return True


label deb08_lobby.bail:
    anon a_side e_w f_worried "Sorry [saga.cast.debbie], I have something else planned for today."
    debbie a_clasp f_sad "Oh."
    show anon a_uneasy e_se
    debbie @ e_sw -m_talk "..."
    debbie f_shy "That's okay, sweetie... just stay safe and be home for dinner."
    anon e_w f_shy "Sure thing."
    hide debbie with dissolve.nowait
    pause
    anon a_think e_nw f_pensive @ -m_talk "( Maybe I should go with her next time... )"
    anon @ -m_talk "( ... It might help ease the tension between us. )"
    hide anon with dissolve
    return


label deb08_lobby.busy:
    debbie "I'll see you this evening, okay?"
    hide debbie

    if 'o_right' in renpy.get_attributes('anon'):
        show anon o_left

    with dissolve.nowait
    anon f_worried_surprised "Oh, alright."
    anon a_wave f_confused "Later, [saga.cast.debbie]."
    pause
    anon a_pocket e_nw f_pensive @ -m_talk "( Hmm, perhaps I should have offered to go with her... )"
    anon e_w f_calm o_right @ -m_talk "( ... Oh well, there's always next time. )"
    hide anon with dissolve
    return


label deb08_reject:
    jump deb_mall_garage


label deb08_reset:
    return


label deb08_reset.debbie:
    anon f_confused "Hey, did you still need to go shopping?"
    anon f_calm "I'm free now."
    debbie f_shy "Not right this moment, sweetie."
    debbie f_calm "I'll be going again later in the week, just look for me in the mornings."
    anon "Okay, will do!"
    return


label deb08_retry(busy):
    call shot.debbie_lobby_bench
    show debbie a_clasp c_casual
    show anon a_pocket o_right at left with dissolve
    anon "Hey, [saga.cast.debbie]."
    debbie "Hey, sweetie."
    anon f_confused "Going shopping again?"
    debbie "Yup."
    show anon f_calm
    jump deb08_lobby.merge


label deb08_car:
    scene mono debbie_car_outing1
    mono "So we hopped in the car and made our way to the mall." with fade
    mono "I found that time passed quickly when I was with [saga.cast.debbie]..."

    scene mono debbie_car_outing2
    mono "... Her pleasant company and infectious smile never failed to brighten my mood." with fade

    scene mall_hall1 noon at stage
    with fade
    show debbie a_clasp c_casual oa_purse at pos(.695)
    show anon a_pocket at pos(.85)
    with dissolve.nowait
    anon "I can't believe you worked at a FunBiz Pizzeria Pub."
    show debbie a_hips o_right at pos(.55)
    debbie "Hey, I was sixteen and it was my first job!"
    anon "Isn't that the one that had the anthropomorphic animal band?"
    debbie f_curious "Uhh, they were called Rock-a-Billy Pants Explosion..."
    show anon f_surprised
    debbie a_fists f_elated "... And they were awesome!"
    anon f_confused "You sure?"
    anon a_hug_self f_afraid "Because it sounds like nightmare fuel."
    show anon f_worried_surprised
    debbie a_clasp f_calm "No, you would have loved them!"
    debbie "[saga.cast.jenny] certainly did."
    anon a_wave f_confused "Wait, wait, wait..."
    anon f_sceptical "... [saga.cast.jenny]?"
    anon a_fold "In a FunBiz Pizzeria Pub?!"
    debbie "For her fifth {i}and{/i} sixth birthday."
    anon a_side f_surprised "N-no!"
    debbie "Yeah."
    debbie "I'm pretty sure we even have a picture of her somewhere on stage singing with Billy-bear."
    anon f_happy_surprised "Oh my god, I never knew how much I needed that in my life until this moment..."
    anon f_happy "... You've gotta let me borrow it!"
    debbie f_happy @ e_b m_laugh "Hehe!"
    debbie "Alright... I'll see if I can find it when we get home."
    anon "Man, I cannot wait to rub this in her face!"
    debbie f_sad "Tsk, sweetheart... she's your roommate, you shouldn't be rubbing {i}anything{/i} in her face."
    anon a_wtf f_pouty "Yeah, yeah..."
    pause
    anon a_side f_worried "... You know, I really do try and get along with her but she just insists on making things hard."
    debbie @ e_r f_bored "Oh believe me, I understand."
    pause
    anon f_confused "So did you bring a list of the groceries you need?"
    show anon e_sw
    debbie a_purse_02 e_s f_calm oa_none @ -m_talk "Mhmm."
    debbie @ a_purse_01 "I've got it here somewhere..."
    pause
    show anon e_w
    debbie a_side e_w oa_purse "... But first, [saga.cast.tammy] mentioned something the other day about some new store here called Cupid."
    anon "Oh?"
    debbie a_clasp "I'd kinda like to go and check it out."
    debbie f_curious "What do you say?"
    anon @ f_calm "Sure, yeah."
    anon "Do you know where it is?"
    debbie f_calm "Somewhere on the second floor, I think."
    anon f_calm "Alright, let's check it out."
    debbie "Lead the way, sweetie."
    hide anon
    hide debbie
    with dissolve
    return


label deb08_car.debbie:
    call shot.debbie_lobby_bench
    show debbie a_purse c_casual e_s s_800ms
    show anon a_pocket f_confused o_right at left with dissolve
    anon "Ready?"
    debbie a_purse_02 e_w "Yeah, you can head on out to the car."
    debbie "I'll join you just as soon as I find my keys."
    show debbie a_purse e_s
    anon f_calm "Okay, [saga.cast.debbie]."
    hide anon with dissolve
    return


label deb08_car.rails:
    scene camera at stage
    show anon with dissolve
    anon @ -m_talk "( I'm supposed to meet [saga.cast.debbie] in the car. )"
    anon @ -m_talk "( I should head there now. )"
    hide anon with dissolve
    return


label deb08_shop1:
    scene gift_shop -debbie at stage(.55, .45, 2.) with None
    show debbie a_clasp c_casual f_happy o_right oa_purse
    show anon a_pocket f_disgusted o_right at left
    with dissolve
    debbie "Oh, wow!"
    debbie "Such a beautiful store!"
    debbie o_left "Isn't it wonderful, [saga.cast.anon]?!"
    show debbie f_curious
    anon e_e @ -m_talk "..."
    anon e_w "I dunno [saga.cast.debbie], it seems pretty girly in here."
    debbie "Well, yeah..."
    debbie f_happy "... But I {i}am{/i} a girl, sweetheart!"
    show anon o_left
    hide debbie
    with dissolve.nowait
    debbie "Ohh, flowers!"

    call shot.gift_shop_flowers
    show debbie a_flower e_sw oa_purse p_bend at left
    with fade
    debbie "I'd love to get some tulips for the dinning room table..."
    show anon a_pocket e_sw behind debbie at pos(.4) with dissolve.nowait
    debbie p_bend_away "... And look at those daffodils!"
    show gift_shop -kassy
    show kassy at right
    with dissolve.nowait
    debbie @ e_b -m_talk "{i}*SNIIIIIIIIIIIIIIIIIIIIFFF*{/i}"
    debbie "Mmm, it all smells so wonderful."
    kassy "You folks finding everything okay?"
    show anon e_w o_right
    debbie a_side e_w o_right p_stand "Oh, yes... thank you."
    show kassy f_happy
    debbie "I just love the vibe you've got going on in here!"
    show kassy f_calm
    anon f_confused "What kind of store is this anyways?"
    show anon e_e
    debbie a_clasp "It's called a women's boutique, sweetie."
    anon "Boutique?"
    show anon e_w
    kassy "We specialize in anything and everything that appeals to young women."
    kassy "Clothing, jewelry, perfume, flowers, decor items, gift ideas, bath and body works..."
    anon a_rub f_surprised "Sheesh, that's a lot of stuff!"
    kassy f_curious @ -m_talk "..."
    show anon a_surprised_up_both e_e f_shocked m_open
    debbie a_whisper "He doesn't have much experience with girls yet..."
    show kassy f_happy
    debbie "... I thought it would be good to introduce him to a place like this."
    show debbie a_clasp
    anon a_upset e_w o_left of_blush @ f_afraid "Wha-"
    show anon f_worried_surprised -m_open
    kassy "Oh, I see."
    anon a_whisper f_annoyed "[saga.cast.debbie]..."
    show anon f_cynical
    kassy "If only more mother's would take the time to educate their sons, maybe the dating scene wouldn't be such a catastrophe."
    debbie f_surprised "Oh, no... I'm not his-"
    anon f_annoyed "... You're embarrassing me!!"
    show anon e_e f_worried_surprised
    kassy "Aww, he's blushing... how adorable!"
    show anon a_cover_face e_b f_afraid m_teeth o_right
    debbie f_calm @ e_b f_happy m_laugh "Heh, sorry sweetie."
    kassy "I'd love to help you all!"
    kassy f_curious "Anything in particular you'd like to show off to him?"
    show anon a_side e_osw f_sad of_none -m_teeth
    debbie f_curious @ -m_talk "Hmm."
    kassy "We've got a sale on evening wear at the moment."
    show kassy f_calm
    debbie f_happy "Oh, fancy!"
    debbie "Yeah, sure. That's as good a place to start as any."
    show anon e_w f_worried
    kassy a_point o_right "You'll find the racks in the next room over, up against the back wall."
    hide debbie
    show kassy f_happy
    with dissolve.nowait
    debbie "Oh wow, you have a whole other room back here!"
    show kassy a_side
    debbie "... {i}*Gasp*{/i} Look at all the pretty!"
    anon "I'm not really, umm..."
    show kassy f_curious o_left
    anon a_uneasy f_shy "... I mean, I've got plenty of experience..."
    show kassy f_smug
    anon "... {i}*Ahem*{/i} You know, with girls."
    kassy @ e_r "Oh, I'm sure!"
    kassy "I'll bet you know {i}all{/i} the secrets when it comes to holding a woman's interest."
    anon "T-totally."
    pause
    show anon a_side f_pouty
    kassy @ e_b f_happy m_laugh "{i}*Snort*{/i} Hehe!"
    kassy f_calm "We'd better catch up to your friend so I can see this expertise of yours in action..."
    hide kassy with dissolve.nowait
    kassy "This way, Casanova."
    anon a_facepalm f_tired @ -m_talk "( Ugh, this is devolving into a nightmare. )"
    hide anon with dissolve
    return


label deb08_shop1.rails:
    scene camera at stage
    show anon a_pocket with dissolve
    anon @ -m_talk "( Hmm, I'm supposed to be looking for a store called \"Cupid\". )"

    if saga.cast.anon in saga.sets.mall_hall1:
        anon a_think e_nw f_pensive @ -m_talk "( [saga.cast.debbie] said it should be on the second floor. )"
    else:
        anon a_surprised f_surprised @ -m_talk "( Oooh, I think I see it! )"

    hide anon with dissolve
    return


label deb08_apparel:
    call shot.gift_apparel_mannequin
    show kassy a_show e_iw o_right behind dummy at pos(.275)
    show debbie c_casual e_iw f_shy oa_purse at right
    with None
    debbie "Aww, the lacework is so gorgeous!"
    kassy "Yeah, this is one of my absolute faves."
    show anon e_wnw f_surprised o_right at pos(.1) with dissolve.nowait
    kassy a_side e_w "This would really look amazing on you, ya know?"
    show anon e_w f_calm
    debbie a_embarrassed e_w "Oh, no... I could never-"
    debbie e_iw "I'm far too plain for something this fancy."
    show debbie e_w
    kassy "Nonsense!"
    show anon f_surprised
    show gift_apparel as dummy behind kassy
    show debbie f_surprised behind kassy
    show kassy a_show at pos(.4)
    kassy "With your curves..."
    show anon e_wsw f_shy
    show debbie e_s f_shy
    kassy e_sw "... And those legs..."
    show anon e_w
    show debbie a_out of_blush
    kassy a_side e_w "... You could absolutely pull it off!"
    debbie e_w f_curious "Y-you really think so?"
    show anon f_worried
    show debbie a_side f_shy
    kassy o_left "Tell her, Casanova."
    anon f_confused @ -m_talk "Hmm?"
    kassy "Wouldn't she look beautiful in this dress?"
    $ renpy.dynamic(test=False)

    menu deb08_apparel.choice:
        "Definitely!"(saga.cast.anon.chr >= 3, '{chr}'):
            $ test = True
        "Y-yeah...":

            pass

    if test:
        show kassy f_happy o_right
        anon a_point f_happy "That dress was made for you, [saga.cast.debbie]."
        debbie a_embarrassed f_happy "Oh, gosh..."
        show anon a_side
        debbie f_calm "... Thanks, sweetie."
    else:

        anon a_uneasy f_shy "{i}*Gulp*{/i} Uh huh."
        show kassy o_right
        debbie "Oh, I dunno..."

    show debbie a_tag e_sw
    pause
    show anon f_confused
    show kassy f_worried
    show debbie f_surprised of_none
    pause
    show anon a_side f_worried_surprised
    show debbie a_side e_w f_worried_surprised at pos(.8)
    with dissolve.nowait
    debbie "NOPE!"
    debbie "That is way too much... I couldn't-"
    show anon f_worried
    kassy a_calm_down "Well, hold on now."
    kassy "You've gotta at least try it on!"
    show debbie f_sad o_right
    hide kassy
    with dissolve.nowait
    kassy "Let's see here..."
    show anon f_confused
    show debbie e_iw f_shy o_left
    pause
    show anon e_sw f_worried
    show debbie a_tag e_sw f_sad at right
    pause
    show anon e_w
    kassy "... You're a size sixteen I'll bet."
    show gift_apparel as stage_right behind dummy at stage(.9, .575, 2.5, c=False), pos(1.5)
    show layer master:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1 xpos -0.2
    with None
    debbie a_side e_w f_calm o_right "Oh, wow... how did you know?!"
    show kassy a_dress f_happy at pos(1.)
    with dissolve.nowait
    kassy "Heh, please..."
    show debbie e_sw
    kassy "... It's my job to know these things!"
    show debbie a_dress e_w
    show kassy a_point o_right behind debbie at pos(.95)
    kassy "Now go on, get in there!"
    show kassy e_e f_calm
    debbie f_shy o_left "What do you think?"
    show kassy a_side e_w o_left

    if test:
        show anon a_pocket f_smug at pos(.375)
        anon "It would be a crime to leave here without seeing you in it."
        debbie f_happy "Aww, sweetie..."
        show kassy f_happy
        debbie "... Alright, I'll do it!"
    else:

        show kassy f_confused
        show anon a_think e_sw f_pensive at pos(.375)
        with dissolve.nowait
        pause
        show kassy f_worried
        anon a_wtf e_w f_shy "It wouldn't hurt just to try it on, right?"
        show kassy f_happy
        debbie f_calm "Oh, I suppose not."
        show anon a_side

    debbie o_right "I'll be right back."
    hide debbie
    with dissolve.nowait
    kassy a_wave o_right "There we go, that's the spirit!"
    pause

    if test:
        kassy a_side f_smug o_left "Well, I must say... I underestimated you, Casanova."
        kassy "That was pretty smooth."
        anon f_shy "Y-yeah?"
        anon f_smug "{i}*Ahem*{/i} I mean, yeah... I know."
        kassy f_happy @ e_b m_laugh "Hehe!"
        show anon f_shy
    else:

        kassy a_side f_calm o_left @ e_r f_annoyed "Sheesh, you've got a lot to learn about women, Casanova."
        anon f_confused @ -m_talk "Hmm?"
        kassy f_smug "I'd suggest you pay close attention to whatever lessons your friend there is willing to impart."
        anon f_worried "Oh."
        show anon f_surprised
        kassy f_curious "Or you can always come see me..."
        kassy f_horny "... I wouldn't mind giving you some advice on dating."
        anon "Really?"
        show kassy f_happy
        anon a_shy_neck e_e f_shy of_blush "That's umm..."
        pause
        anon e_w "... T-thanks, I guess."
        kassy f_horny @ -m_talk "Mhmm."
        kassy "You're cute."

    pause
    show anon a_surprised_up f_surprised of_none
    with dissolvefast.nowait
    kassy f_surprised "Oh, shoot!"
    kassy "I've gotta get back to the register."
    hide kassy
    show anon a_surprised o_left
    with dissolve.nowait
    kassy "Shout at me if you all need anything!"
    anon a_wave f_happy "Alright, will do."
    pause
    show anon a_side
    pause
    anon f_horny @ -m_talk "( Man, look at all these bras... )"
    anon a_rub e_wsw @ -m_talk "( ... And panties... )"
    anon a_hug_self e_w f_horny_smug o_right @ -m_talk "( ... And stockings. )"
    pause
    hide anon with dissolve
    return


label deb08_apparel.rails:
    scene gift_shop at stage
    show anon a_pocket f_worried o_right with dissolve
    anon "( I should catch up to [saga.cast.debbie] in the clothing department. )"
    hide anon with dissolve
    return


label deb08_stall1:
    scene gift_apparel -gift_stall1 at stage(.732, .505, 4.5)
    show gift_apparel gift_stall1 as door at stage(.732, .505, 4.5, b=0)
    show anon a_pocket f_worried o_right with dissolve
    anon "[saga.cast.debbie]?"
    anon a_knock "{i}*Ahem*{/i} H-hey, how's it going in there?"
    show anon f_shy
    debbie "Sweetie, is that you?"
    anon a_side @ -m_talk "Mhmm."
    debbie "Oh, thank goodness... I need your help real quick!"
    anon a_uneasy f_worried "Y-you want me to come in there?!"
    debbie "Yes, please!"
    anon e_e f_worried_surprised "I-"
    anon a_whisper e_w "I'm not sure that's allowed."
    debbie "It's alright, sweetie... it'll just take a second."
    anon a_shy_neck e_e @ -m_talk "{i}*Gulp*{/i}"
    anon e_w f_worried "... O-okay."

    scene gift_stall1 base
    show mimic debbie o_right p_stand_away at pos(.985), zoom(.95)
    show gift_stall1 -base as wall
    show debbie c_dress f_shy at right
    with fade
    show anon a_cover_face e_b at left with dissolve
    anon "What's going on?"
    debbie "Oh, this stupid zipper on the dress is stuck..."
    debbie "... Could you give it a try?"
    anon "Oh, umm... S-sure thing."
    show mimic debbie o_left p_stand_hair_lift
    debbie o_right p_stand_hair_lift_away "Here, lemme just-"
    anon a_surprised e_w f_surprised o_right "Wow!"
    anon e_sw "Y-you look..."
    show anon a_side e_w
    debbie f_curious @ -m_talk "Hmm?"
    anon "You look incredible, [saga.cast.debbie]!"
    debbie e_sw f_shy "I do?"
    show mimic debbie o_right p_stand_away
    show debbie e_w o_left p_stand
    anon f_shy "Y-yeah."
    debbie f_happy "Hehe, thanks sweetie!"
    anon f_confused "Are you going to buy that?"
    debbie f_worried_surprised "Oh, no... it's three hundred dollars..."
    debbie "... We can't afford that kind of money on a silly dress."

    menu:
        "Why not?":
            pass
        "I got this."(saga.cast.anon.bank + saga.cast.anon.cash >= 300, '{usd=$$$}'):

            jump deb08_stall1.alt

    anon a_palm f_calm "You deserve to treat yourself to something nice every once in a while too, you know?"
    debbie f_shy "Aww, that's so sweet of you to say."
    show anon a_side
    debbie a_out e_s f_calm "You really like it that much?"
    show mimic debbie o_left p_stand
    show debbie e_sw o_right p_stand_away
    anon e_sw f_horny "Oh, y-yeah... I really do."
    show mimic debbie o_right p_stand_away
    show debbie e_s f_happy o_left p_stand
    anon e_w f_shy "You look so beautiful, [saga.cast.debbie]."
    debbie @ e_b m_laugh "Hehe!"
    debbie a_side e_w f_shy "Well, it does feel nice hearing that..."
    debbie "... But I don't need it, sweetie."
    show anon f_worried
    debbie f_sad "When would I ever get a chance to wear it?"
    anon @ f_confused "I dunno, maybe you could-"
    debbie "With your father gone and all these bills pilling up..."
    show anon e_sw f_sad
    debbie @ e_b "Tsk."
    label deb08_stall1.merge:
    show mimic debbie o_left p_stand
    debbie f_shy o_right p_stand_away "Please, just help me get it undone."
    anon "{i}*Sigh*{/i} Y-yeah, okay."
    show anon f_worried at center
    show mimic debbie o_left p_stand_hair_lift
    debbie f_curious p_stand_hair_lift_away "Can you see where it's snagged?"
    show debbie e_wsw f_calm
    show anon a_zip_debbie_dress_01 e_wsw p_stoop at pos.debbie.zip_dress
    anon "Yup, I see it. Just hold still one second."
    anon a_zip_debbie_dress_02 @ -m_talk "..."
    show anon a_zip_debbie_dress_01
    pause
    show anon a_zip_debbie_dress_02
    show mimic debbie o_left p_stand_hair_lift
    debbie f_curious "You got it, [saga.cast.anon]?"
    anon a_zip_debbie_dress_01 f_shy @ e_wnw "I'm trying!"
    show debbie f_shy
    show anon a_zip_debbie_dress_02 f_worried
    pause
    anon a_zip_debbie_dress_01 "Man, you really got it stuck."
    show anon a_zip_debbie_dress_02
    debbie @ -m_talk "..."
    anon a_zip_debbie_dress s_2 "Almoooost..."
    anon f_sceptical s_3 "... Got iiiit..."
    anon @ -m_talk "..."
    show anon a_zip_debbie_dress_01 f_grumpy
    pause
    show anon e_wnw f_confused
    debbie f_calm @ e_b f_happy m_laugh "Hehehe."
    anon "What's so funny?"
    debbie "N-nothing. It's silly."
    anon a_zip_debbie_dress_02 e_wsw f_calm "Oh c'mon, tell me."
    show anon a_zip_debbie_dress_01
    debbie "I'm just thinking about that movie we watched the other night."
    anon a_zip_debbie_dress_02 f_sceptical "That cheesy romance flick?"
    show anon a_zip_debbie_dress_01
    debbie "Y-yeah."
    anon a_zip_debbie_dress_02 "What about it?"
    show anon a_zip_debbie_dress_01 e_nw f_pensive
    debbie "There was a scene just like this... Remember?"
    anon @ -m_talk "..."
    anon e_wnw f_shy "Oh yeah!"
    anon "He helped the girl out with her dress, and then he-"
    anon f_surprised @ -m_talk "{i}*Gulp*{/i}"
    anon e_wsw f_shy "Kissed her."
    show anon a_zip_debbie_dress_02
    debbie "Uh huh."
    show anon e_wnw f_surprised
    debbie f_curious "Have you kissed a girl yet, [saga.cast.anon]?"
    pause
    show debbie f_calm
    anon a_zip_debbie_dress_01 e_wsw f_shy "N-no, not really."
    show anon a_zip_debbie_dress_02
    debbie @ -m_talk "..."
    show anon a_zip_debbie_dress_01
    debbie "Well, that's okay, sweetheart! There's nothing wrong with that."
    anon a_zip_debbie_dress_02 f_surprised "Oh, I think I've got it!"

    label deb08_stall1.cookie hide:
    scene gift_stall_zip
    show debbie b_anon c_dress p_gift_stall_zip_01
    with fade
    anon "Just a little wiggle and-"
    show debbie p_gift_stall_zip_02
    anon "There it goes!"
    show debbie p_gift_stall_zip_03
    pause
    anon "( Wow, I've never seen this part of her before... )"
    anon "( ... So smooth and pretty. )"
    debbie "Would you like to?"
    anon "Hmm?"

    scene gift_stall1 base
    show mimic debbie o_right p_stand_away at pos(.985), zoom(.95)
    show gift_stall1 -base as wall
    show anon f_confused o_right
    show debbie a_cover c_dress_open f_shy at right
    with fade
    debbie "I asked, if you would like to try..."
    anon @ -m_talk "..."
    show anon a_surprised f_surprised
    debbie "... Kissing, I mean."
    anon "You're serious?"
    show anon f_happy_surprised
    debbie "Well, yeah... I suppo-"
    hide anon
    hide mimic
    show debbie b_anon p_kiss_surprised at pos(.65)
    with dissolve.nowait
    debbie "( !!! )"
    show debbie p_peck_01
    pause
    debbie p_peck s_700ms "Mmm..."
    pause

    scene gift_stall_kiss
    show debbie b_anon c_dress_open p_gift_stall_kiss s_600ms
    with fade
    pause
    debbie "Mmm...."
    anon "Mmm..."
    pause

    scene gift_stall1 base
    show gift_stall1 -base as wall
    show anon f_horny_smug o_right at pos(.45)
    show debbie a_cover c_dress_open f_horny of_blush at pos(.625)
    with fade
    debbie "... Wow."
    pause
    debbie "Sweetie, that was-"
    pause
    debbie @ f_happy "Wow."
    pause
    $ renpy.end_replay()
    debbie @ -m_talk "..."
    show debbie f_shy
    pause
    show anon f_worried
    show debbie f_worried_surprised at right
    show mimic debbie o_right p_stand_away behind wall at pos(.985), zoom(.95)
    debbie "W-we shouldn't have... done that."
    anon "I'm sorry, [saga.cast.debbie]."
    show anon a_surprised_up f_surprised
    debbie "NO!"
    show debbie e_b o_right p_stand_away
    show mimic debbie o_left p_stand
    pause
    show anon a_side f_worried_surprised
    debbie e_s f_sad "No... It's my fault, I shouldn't have let myself..."
    show anon e_s f_worried
    pause
    debbie @ -m_talk "..."
    show anon e_w
    debbie "{i}*Ahem*{/i}"
    show mimic debbie o_right p_stand_away
    debbie e_w f_shy o_left p_stand "T-thanks, for helping me... with the zipper."
    anon f_shy @ -m_talk "..."
    anon a_uneasy "Y-yeah, sure thing, [saga.cast.debbie]."
    debbie "I'll uhh... take it from here."
    anon "R-right."
    anon a_point_back "I'll just, head out front..."
    anon "... And wait for you."
    hide anon with dissolve.nowait
    pause
    show debbie f_sad
    pause
    debbie a_facepalm e_b @ -m_talk "( Oh god... I can't believe I just did that! )"
    debbie @ -m_talk "( The poor thing is having a hard enough time as it is. )"
    debbie @ -m_talk "( What in the world was I thinking?! )"

    call shot.gift_apparel_mannequin
    with fade
    show anon a_rub f_shy at pos(.8) with dissolve
    anon @ -m_talk "( Wow, [saga.cast.debbie] and I just kissed... )"
    anon e_sw @ -m_talk "( ... On the mouth and everything! )"
    anon a_pocket f_happy @ -m_talk "( Maybe she is capable of seeing me as something other than an my father's awkward kid? )"
    anon @ e_b m_teeth "( What a great day! )"
    hide anon with dissolve
    return


label deb08_stall1.alt:
    anon a_point_self f_happy "I'll buy it for-"
    show anon f_surprised m_teeth
    debbie f_annoyed "Oh, no you will not!"
    show anon a_side f_worried_surprised -m_teeth
    debbie "You're saving all your money up for next years tuition and that's the end of the conversation!"
    pause
    anon a_finger f_shy "B-but-"
    show anon f_worried
    debbie "I won't hear another word about it, Mister!"
    show anon a_side e_sw f_sad
    jump deb08_stall1.merge


label deb08_stall1.fence:
    scene gift_apparel at stage
    show anon a_pocket e_nw f_pensive with dissolve
    anon @ -m_talk "( I wonder how [saga.cast.debbie] is getting on? )"
    anon a_think @ -m_talk "( Maybe I should check on her? )"
    anon e_e f_worried @ -m_talk "( I feel awkward standing around in here by myself. )"
    hide anon with dissolve
    return


label deb08_shop2:
    call shot.gift_shop_plushes
    show anon a_tired f_confused o_right p_bend at pos(.3)
    with fadewait
    pause

    call shot.gift_shop_flowers
    show anon a_think e_sw f_pensive
    with fadewait
    pause

    call shot.gift_shop_jewelry
    show anon a_phone e_sw f_bored o_right at left
    with fadewait
    pause
    anon a_pocket e_w f_happy @ -m_talk "( Oh, here she comes! )"
    show debbie c_casual f_shy oa_purse at right
    anon f_calm "You all ready to go?"
    debbie "Actually, sweetie... I was thinking, maybe it's best I finish the shopping on my own today."
    show anon f_confused
    pause
    anon "Oh?"
    debbie "I'm sure there are things you'd rather be doing, besides helping your old lonely landlady carry groceries."
    anon f_worried "That's not-"
    anon f_shy "I mean, I don't mind!"
    debbie "Will you be okay getting home on your own?"
    anon "Y-yeah, but I can stay if you-"
    show anon e_o f_worried
    hide debbie
    with dissolve.nowait
    debbie "Alright then, sweetie... I'll see you later this evening."
    anon a_wave "O-okay."
    pause
    anon a_think e_s @ -m_talk "( Welp, that's not what I was expecting... )"
    anon @ -m_talk "( ... That kiss must have made her uncomfortable. )"
    pause
    anon a_side e_o @ -m_talk "( Man, just when I thought things were starting to go well. )"
    hide anon with dissolve
    return


label deb08_shop2.rails:
    scene gift_apparel at stage
    show anon a_pocket o_right with dissolve
    anon "( Nah, I should just head up front and wait for her to come out. )"
    anon "( Man, what a great day! )"
    hide anon with dissolve
    return


label deb08_outro:
    scene mono debbie_garage_greet hide
    mono "Despite my better judgement, I really wanted to show [saga.cast.debbie] that what had unfolded at the mall didn't need to make things awkward between us." with fade
    mono "Though perhaps, in retrospect, surreptitiously staking out the garage and waiting for her to return was not the best course of action."

    call shot.debbie_garage_rear
    show anon o_right behind car at left
    with fade
    show debbie a_grocery c_casual f_shy behind car at right with dissolve
    anon "Hey, [saga.cast.debbie]."
    debbie @ e_e f_worried_surprised "Oh, umm..."
    debbie "... Hi, sweetie."
    show anon a_surprised at pos(.4)
    anon @ e_sw "Can I help with that?"
    debbie "No, that's alright."
    show anon a_side f_confused
    debbie "I've got it."
    show debbie behind anon at pos(.55)
    anon a_surprised p_stand_away "You sure?"
    hide debbie
    show anon o_left
    with dissolve.nowait

    if saga.cast.debbie < 'mall':
        debbie "Yup."
        anon a_side "I'm really sorry about earlier, I didn't mean to-"
        debbie "What?"
        anon "I said-"
        debbie "Can't hear you sweetie..."
        debbie "... Let me put these groceries away, and get dinner started, okay?"
        anon a_think e_sw f_pensive p_stand @ -m_talk "..."
        anon @ -m_talk "( I guess she doesn't wanna talk about it. )"
        anon a_side e_w f_worried @ -m_talk "( Better give her some space for now. )"
    else:

        debbie "I'm good, sweetie, but thanks for the offer."
        anon a_side "Y-yeah, okay."
        anon f_worried p_stand @ -m_talk "( I guess things are still awkward. )"
        anon @ -m_talk "( I'd better give her more time. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
