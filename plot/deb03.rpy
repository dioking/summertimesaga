label deb03_lobby:
    scene debbie_lobby -debbie at stage
    show debbie a_mug at right
    show anon a_pocket o_right at left with dissolve

    if saga.time.dawn and saga.time.dow < saga.time.sat:
        debbie "Good morning, sweetie."
        anon "Morning, [saga.cast.debbie]."
        debbie "Ready for school?"
    else:

        debbie "Hello, sweetie."
        anon "Hello, [saga.cast.debbie]."
        debbie "Happy to be back at school?"

    anon f_worried "Yeah, I suppose... There's just so much homework to catch up on!"
    debbie @ f_disgusted "Eww, I can imagine..."
    debbie "It's good you're getting back into a normal routine though."
    anon "I guess."
    anon f_calm "What are you doing today?"
    debbie @ f_curious "Oh, me?"
    debbie "Housework mostly."
    debbie f_shy "It's not easy taking care of this big place by myself you know?"
    show anon e_nw f_pensive
    pause
    anon a_point_self e_w f_happy "Is there anything I can do?"
    debbie f_surprised "You want to help with the housework?"
    anon a_uneasy f_shy "I mean, sure... I live here, I should pull my own weight, right?"
    debbie f_happy "That's a great attitude to have, [saga.cast.anon]."
    show anon a_side f_calm
    debbie e_nw f_pensive @ -m_talk "Hmm..."
    debbie "... Lemme see..."
    pause
    debbie e_w f_shy "... You know, the lawn hasn't been mowed since your father passed."
    debbie f_curious "You wanna give it a shot?"
    anon a_point_back f_confused "The mower's in the garage, yeah?"
    debbie f_calm @ -m_talk "Mhmm."
    anon a_side f_calm "Yeah, I'll go take a look."
    debbie "That would be wonderful, sweetie!"
    show anon f_happy
    debbie "Thank you so much!"
    anon "My pleasure."
    hide anon with dissolve
    return


label deb03_mower:
    call shot.debbie_garage_mower
    show anon a_cap e_sw f_confused p_bend
    anon @ -m_talk "( I finally have some gas for the mower. )"
    anon a_gas @ -m_talk "( That should be enough. )"
    anon a_reach @ -m_talk "( Hope this works because I've got no idea what else to do. )"
    show anon a_pull1 e_s f_calm
    pause
    show anon a_pull2
    pause
    show anon a_pull1
    pause
    show anon a_pull2
    pause
    anon a_pull1 @ -m_talk "( Hmm, it's not working... maybe I need to pull harder? )"
    show anon a_pull2 e_b f_worried m_teeth with none.nowait
    with hpunch
    pause
    anon a_tired e_sw f_confused -m_teeth "( That got it! )"

    scene mono debbie_lawn1
    mono "Mowing the lawn turned out to be a piece of cake. I just thought back to watching Dad on the occasional sunny afternoon and tried my best to do the same." with fade
    show mono debbie_lawn2 with dissolve
    mono "It didn't look half bad by the time I was done, and I remember hoping that [saga.cast.debbie] would think the same."

    scene mono debbie_lawn3
    mono "I don't know at what point she arrived and started watching, but I got the feeling it'd probably been quite a while..." with fade

    scene debbie_main -debbie_mail at stage(.835, .65, 5)
    show anon a_wipe f_happy ob_grass of_grass
    show debbie a_mug_down o_right at left
    with fade
    anon "Phew, all done!."
    show anon a_side
    debbie "Yeah, I see that."
    show anon a_fold e_sw o_right at pos(.435)
    debbie @ e_b f_happy m_laugh "It looks wonderful."
    debbie "I'm so proud of my boy!"
    anon a_shy_neck e_e f_shy "I was just doing it the way I thought Dad would."
    show anon f_happy
    debbie "Well, I'm sure he'd be proud too."
    show anon a_side f_shy
    debbie f_shy "He was always so good about making sure everything was taken care of around here."
    anon "And now I will too, [saga.cast.debbie]... I feel like it's what he'd want."
    debbie f_calm "You're such a sweetheart!"
    anon a_point_back f_confused "Shall we go inside now?"
    debbie @ f_shy "Oh, you go on..."
    show debbie a_mug e_b at pos(.6)
    show anon a_side e_w
    debbie "... I'm gonna stay here and enjoy the air for a minute."
    pause
    anon "You sure?"
    debbie "Absolutely."
    pause
    debbie a_mug_down e_sw -o_right "Why don't you head downstairs and get those sweaty clothes in the wash?"
    debbie e_w "There should be a clean towel down there for you."
    anon "Yeah, okay... Thanks!"
    hide anon with dissolve
    show debbie e_b o_right
    pause
    show debbie a_mug_sip f_sad
    pause
    show debbie a_mug f_crying
    pause
    return


label deb03_mower.busy:
    scene debbie_garage at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( Hmm, the grass is too damp to mow right now. )"
    anon @ -m_talk "( I should come back some other time. )"
    hide anon with dissolve
    return


label deb03_mower.item:
    call shot.debbie_garage_mower
    show anon a_tired e_sw f_confused p_bend
    anon @ -m_talk "( I haven't used a lawn mower in years... Do I even remember how to use one? )"
    anon a_finger e_s f_calm @ -m_talk "( Dad used to pull the cord and it would start. Let me try that. )"
    show anon a_pull1
    pause
    show anon a_pull2
    pause
    anon a_pull1 e_sw f_confused @ -m_talk "( It must be out of gas. It barely started, so at least I know it's running. )"
    anon a_cap @ -m_talk "( Yup. )"
    anon a_tired @ -m_talk "( Well it's not going to start without gas. I should probably get some from Consum-R. )"
    hide anon with dissolve
    return


label deb03_mower.late:
    scene debbie_garage at stage
    show anon f_pensive with dissolve
    anon @ -m_talk "( Who mows the lawn at night? I should return during the day. )"
    hide anon with dissolve
    return


label deb03_gas:
    scene store_aisle at stage with fade
    show anon o_right with dissolve
    anon @ -m_talk "( All set. Long grass your time is short! )"
    hide anon with dissolve
    return


label deb03_gas.take:
    anon "( Careful, we wouldn't want to do anything fuelish here. )"
    return


label deb03_hall:
    scene debbie_hall at stage(.5, .45, 1.65)
    show jenny f_disgusted o_right at left

    if saga.camera.last is saga.sets.debbie_garage:
        show debbie_hall flip
        show jenny -o_right at right

    with none
    show anon f_sceptical ob_grass of_grass at right

    if saga.camera.last is saga.sets.debbie_garage:
        show anon o_right at left

    with dissolve
    jenny "Eugh, what's that smell?!"
    anon a_surprised e_s f_pensive "Me I think."
    jenny @ e_sw "Ugh, you're disgusting!"
    anon a_side e_w f_grumpy "Gimme a break, [saga.cast.jenny]... I was outside helping [saga.cast.debbie] with the yard."
    jenny f_annoyed "So what, you're going to start doing chores around here now?"
    jenny a_fold f_horny "You got a thing for [saga.cast.debbie] or something?"
    anon f_confused "No! I'm just-"
    jenny e_r f_annoyed "Pfft, don't play dumb... I see what you're up to!"

    if saga.camera.last is saga.sets.debbie_garage:
        show anon o_left
    else:
        show anon o_right

    hide jenny with dissolve
    pause
    anon a_rub @ -m_talk "( What I'm up to?! )"
    anon e_nw f_pensive @ -m_talk "( The heck is she on about? )"
    pause
    show anon a_pants_off_01 e_s

    if saga.camera.last is saga.sets.debbie_garage:
        show anon o_right
    else:
        show anon o_left

    anon @ -m_talk "( Whatever, I should get these clothes downstairs to the wash. )"
    hide anon with dissolve
    return


label deb03_hall.rails:
    scene camera at stage
    show anon ob_grass of_grass with dissolve
    anon @ -m_talk "( I should get out of these dirty clothes. )"
    anon @ -m_talk "( The washing machine is downstairs in the basement. )"
    hide anon with dissolve
    return


label deb03_outro:
    scene debbie_utility at stage(.6, .5, 2)
    show anon a_surprised e_s f_worried ob_grass of_grass
    anon @ -m_talk "( Man, I hate peeling off wet clothes! )"
    show anon a_top_off c_casual_bottom
    pause
    anon a_towel f_disgusted @ -m_talk "( It's like I fell in a bog or something. )"
    show anon a_throw_top e_se
    pause
    anon a_pants_off_01 c_naked e_s f_horny -ob_grass @ -m_talk "( A shower is gonna feel real nice after this. )"
    show anon p_pants_off_02
    pause
    anon a_hold_pants d_soft f_disgusted -p_pants_off_02 @ -m_talk "( Yuck! )"
    show anon a_throw_pants e_se
    pause
    anon a_side e_s f_horny @ -m_talk "( That's better! )"
    anon e_w f_confused @ -m_talk "( Now, where's that fresh towel she was talking about? )"
    show anon e_sw o_right
    pause
    anon e_nw f_pensive @ -m_talk "( Too bad those up on the shelf are purely decorative. )"
    anon a_rub @ -m_talk "( I mean, who even has decorative towels? )"
    anon @ -m_talk "( And in a basement of all places?! )"
    pause
    anon a_side e_w f_pouty @ -m_talk "( Whatever. The search continues. )"
    show anon a_search p_bend_low s_2 at right
    pause
    anon a_side_nervous e_s f_pensive -p_bend_low @ -m_talk "( Hmm, no... not here. )"
    show anon a_surprised e_sw f_confused -o_right at center
    anon @ -m_talk "( Maybe it's- )"
    show anon a_search p_bend_low at left
    pause
    anon a_side_nervous e_s f_pensive -p_bend_low @ -m_talk "( Nope, not here either. )"
    anon a_rub e_w f_grumpy @ -m_talk "( Where the heck did she put it? )"
    show anon a_surprised e_nw f_shocked m_open with none.nowait
    debbie "I didn't say anything, [saga.cast.jenny]!" with hpunch
    anon a_up e_w f_surprised m_teeth o_right @ -m_talk "( Oh, crap!! [saga.cast.debbie] is coming! )"
    show anon at center
    with dissolve.nowait
    jenny "Yeah, but I know you're thinking it."
    anon a_neck e_nw f_afraid -o_right @ -m_talk "( Oh my god, think... What do I do?! )"
    debbie "If it bothers you that much, there's plenty you could be doing to help out around-"

    menu deb03_outro.choice:
        "Cover up!":
            jump deb03_outro.cover
        "Put on old pants!":

            jump deb03_outro.pants
        "Shamelessly pose!":

            pass

    anon a_side_nervous e_s f_worried -m_teeth @ -m_talk "( Ah, man... there's no way out of this. )"
    show anon e_nw
    jenny "Oh, and would that make {i}me{/i} your favorite?!"
    debbie "Ugh, I don't have favorites, [saga.cast.jenny]!"
    anon a_hips e_sw f_nervous m_teeth @ -m_talk "( Embrace the chaos, I suppose. )"
    show anon e_nw
    show debbie a_gimme e_nw f_sad at pos(.025, .84)
    with dissolve.nowait
    debbie "Must you be such a drama queen all the time?!"
    show debbie a_side
    jenny "Whatever."
    show debbie a_wtf e_r f_bored
    "*Door closes*"
    show debbie a_side e_nw f_sad
    pause
    show debbie e_w f_calm o_right at pos(.225, 1.)
    show anon e_w
    debbie "Sorry, sweetie... [saga.cast.jenny] distracted me and-"
    show debbie a_surprised e_wsw f_surprised with none.nowait
    with hpunch
    pause
    show debbie e_sw m_talk
    pause
    show anon f_surprised
    debbie a_shock of_blush -m_talk @ -m_talk "Oh my god!!"
    show anon f_worried_surprised -m_teeth
    debbie a_cover_face e_b f_worried_surprised "Sweetie, what are you doing?!"
    anon "I'm sorry, I-"
    debbie "Why are you naked?!"
    show anon e_s
    debbie "A-and why are you posing like a superhero?!"
    anon a_side_nervous e_w "I umm, honestly... I'm not sure..."
    anon "... You were coming down the stairs and I think... I sorta just... blacked out?"
    debbie @ a_cover_face_peek e_sw f_surprised -m_talk "..."
    label deb03_outro.merge:
    debbie f_curious "Where's your towel?!"
    anon a_rub f_confused o_right "Yeah, I was wondering the same thing."
    debbie a_cover_face_peek e_w @ -m_talk "Hmm?"
    anon a_side -o_right "I looked everywhere, down here but I couldn't find it."
    anon "Are you sure you left one?"
    debbie a_cover_face e_b f_worried_surprised "I thought I did."
    debbie f_sad -of_blush "Just, cover yourself and let me see if I can find you something!"
    anon a_cover f_worried @ e_s "Y-yeah, okay."
    show debbie at right
    anon o_right "I'm really sorry, [saga.cast.debbie]."
    debbie a_facepalm "No, it's okay."
    debbie e_s f_shy "I was just surprised, that's all."
    pause
    show anon e_ssw f_surprised
    debbie a_reach p_bend_away "You checked the dryer?"

    label deb03_outro.cookie hide:
    scene mono debbie_utility_laundry1
    mono "I was more than a bit mortified, having just exposed my jiggly bits to my new landlady..." with fade
    mono "... But as I watched her fish through the dryer, the embarrassment began to fade away."
    show mono debbie_utility_laundry1 hard
    more "Replaced with a much different and more intense feeling." with dissolve

    scene debbie_utility_laundry
    show anon a_surprised c_naked d_hard e_sw f_surprised of_grass at right
    show debbie a_reach_machine p_bend_away at pos.dryer
    with fade
    debbie "I could have sworn there was one in here..."
    pause
    show anon a_side_nervous
    debbie "... Shoot!"
    debbie "I'm sorry, sweetie..."
    show anon e_w f_shy
    show debbie a_washcloth o_right -p_bend_away at pos.anon.washcloth
    debbie "... I guess I-"
    show anon f_confused
    debbie e_sw f_surprised "I-"
    show debbie a_washcloth_drop m_talk of_blush
    pause
    show debbie a_side
    pause
    debbie -m_talk @ -m_talk "{i}*Gulp*{/i}"
    anon a_up e_s @ -m_talk "Hmm?"
    show anon f_shocked m_open of_blush
    pause
    anon a_cover e_w f_worried_surprised -m_open "I'm sorry, I-"
    debbie e_w f_worried_surprised "N-no, no!!"
    debbie a_cover_face e_b f_shy "I'm sorry, it's-"
    pause
    show anon e_s f_worried
    debbie "{i}*Ahem*{/i} It's perfectly natural for a boy your age to, umm... well..."
    debbie "... I mean, it's not like you can control... these things..."
    debbie a_cover_face_peek e_sw f_surprised "... and it's just... so big..."
    anon e_w f_surprised "What?"
    show anon f_confused
    debbie a_cover_face e_b f_worried_surprised "Ahh, I mean... accident!"
    debbie "It's just an accident."
    anon e_e f_worried_surprised "Ugh, I'm so embarrassed."
    debbie a_side e_e f_surprised "N-no, no... Sweetie, there's no need to be embarrassed!"
    show anon e_w f_worried
    debbie "These things happen, it's normal..."
    show anon e_s f_surprised
    debbie a_reach e_s f_shy p_bend "... We'll just, umm..."
    show anon a_side_nervous d_hard_out m_teeth z_b_ob_f_of_a_oa_d_od
    debbie a_washcloth e_se "... Cover you with this."
    show anon f_sceptical od_washcloth -m_teeth
    debbie a_embarrassed e_sw f_calm -of_blush -p_bend "Oh, dear... that's not really accomplishing much, is it?"
    show debbie e_w
    anon a_side e_w f_pouty -of_blush "I feel like a towel rack."
    debbie a_shock f_happy @ e_b m_laugh "Pfft, hahahaha!"
    anon @ -m_talk "..."
    $ renpy.end_replay()
    debbie a_cover_face e_b f_calm "Sorry, sorry!"
    debbie "I'll just, umm..."
    show debbie at pos(.9)
    show anon e_e
    with dissolve.nowait
    debbie "... Run upstairs and grab you a real towel!"
    hide debbie with dissolve.nowait
    anon e_nw f_worried o_right "I'm really sorry, [saga.cast.debbie]."
    debbie "There's nothing to be sorry about, sweetie!"
    debbie "I'll be right back, okay?"
    show anon a_surprised_shrug e_b f_hurt m_teeth
    "*Crash*" with hpunch
    show anon e_nw f_afraid
    debbie "Oww!"
    show anon a_side f_worried -m_teeth
    debbie "I stubbed my toe on the stupid step!"
    anon "Are you alright?"
    debbie "Gah! Y-yeah, I'm good."
    anon "Be careful."
    debbie "Hold tight, sweetie!"
    anon "Uh huh."
    pause
    anon e_s f_pensive -o_right @ -m_talk "( Man, what is your deal lately?! )"
    show anon a_surprised at center
    anon @ -m_talk "( That's our landlady, not some floozy on the internet! )"
    show anon a_hips at left
    anon @ -m_talk "( Ugh, I've gotta find a way to control myself. )"
    jenny "What in the world is going on down there?"
    show anon a_side_nervous e_nw f_worried o_right
    debbie "N-nothing, there was just... umm..."
    show anon f_confused
    debbie "... A big spider! Yeah!"
    jenny "Really?! Ewww!!!"
    show anon a_hips e_b f_happy m_teeth
    debbie "[saga.cast.anon] got it though, so no worries."
    debbie "I'm just bringing him a fresh towel so he can go shower after all his hard work."
    anon @ -m_talk "( Now, that was a good story. )"
    anon @ -m_talk "( At least I won't have to worry about [saga.cast.jenny] poking fun at me about all this. )"
    show anon a_side e_w f_surprised -m_teeth
    show debbie a_cover_face_towel e_b at pos(.85)
    with dissolve.nowait
    pause
    show debbie a_side at pos(.65)
    show anon e_sw
    debbie @ a_towel_give "Here you go, sweetie."
    anon a_towel e_s f_shy z_reset -od_washcloth "Thanks, [saga.cast.debbie]."
    show anon a_towel_wrap
    pause
    show debbie e_w
    anon a_side c_towel f_pensive z_b_ob_f_of_a_oa_d_od @ -m_talk "Hmmm."
    show debbie e_sw f_surprised
    pause
    show anon e_w f_confused
    debbie @ -m_talk "..."
    pause
    anon a_point f_shy "I should probably-"
    debbie a_shock e_w of_blush "Oh!"
    show anon a_side
    debbie a_nervous f_shy "R-right, of course."
    debbie "Go on upstairs to the shower and I'll clean up down here."
    anon "Alright."
    show anon at pos(.9)
    show debbie a_side o_right behind anon
    pause
    hide anon
    show debbie e_nw
    pause
    debbie a_relieved e_wnw f_calm -o_right "{i}*Sigh*{/i} Ahh, goodness..."
    debbie a_fan e_sw @ -m_talk "( ... That was- )"
    debbie @ -m_talk "( Phew, what a mess that turned into! )"
    debbie a_clasp f_surprised @ -m_talk "( I did not need to know my tenant was lugging that around... )"
    pause
    debbie a_embarrassed e_nw f_shy o_right @ -m_talk "( ... Sheesh! )"

    scene black
    with dissolve
    mono ""

    call shot.debbie_bath_shower
    show anon a_towel c_naked d_soft e_s
    show steam
    with dissolve
    anon @ -m_talk "( Okay, nice and clean now. )"
    anon p_top_on @ -m_talk "( I just wish I could wash my brain and get all these weird thoughts out! )"
    anon a_rub c_casual_top e_sw f_tired -p_top_on @ -m_talk "( Ugh, what is going on with me? )"
    show anon d_none p_pants_off_02
    pause
    show anon a_pants_off_01 c_casual e_s f_worried -p_pants_off_02
    pause
    anon a_side e_w @ -m_talk "( Best be a little more careful around [saga.cast.debbie] for a while. )"
    hide anon with dissolve
    return


label deb03_outro.cover:
    anon a_cover e_s f_surprised @ -m_talk "( Ah, man... this is gonna be so awkward. )"
    show anon e_nw f_afraid
    jenny "Oh, and would that make {i}me{/i} your favorite?!"
    debbie "Ugh, I don't have favorites, [saga.cast.jenny]!"
    anon @ e_b f_distressed "W-wait, [saga.cast.debbie]!!"
    show debbie a_gimme e_nw f_sad at pos(.025, .84)
    with dissolve.nowait
    debbie "Must you be such a drama queen all the time?!"
    show debbie a_side
    pause
    jenny "Whatever."
    show debbie a_wtf e_r f_bored
    "*Door closes*"
    show debbie a_side e_nw f_sad
    anon @ e_b f_distressed "Don't-"
    show debbie e_w f_calm o_right at pos(.225, 1.)
    show anon e_b_w
    debbie "Sorry, sweetie... [saga.cast.jenny] distracted me and-"
    show debbie a_surprised e_wsw f_surprised with none.nowait
    with hpunch
    pause
    show debbie e_sw m_talk
    pause
    debbie a_shock e_w of_blush -m_talk @ -m_talk "Oh my god!!"
    debbie a_cover_face e_b f_worried_surprised "Sweetie, what are you doing?!"
    anon e_w f_worried_surprised -m_teeth "I'm sorry, I-"
    jump deb03_outro.merge


label deb03_outro.pants:
    anon a_side_nervous e_s f_surprised @ -m_talk "( Crap. Crapcrapcrapcrapcrap! )"
    show anon a_search o_right p_bend_low at right
    jenny "Oh, and would that make {i}me{/i} your favorite?!"
    debbie "Ugh, I don't have favorites, [saga.cast.jenny]!"
    anon s_5 "( Wherearetheywherearetheywherearethey?!?! )"
    show debbie a_gimme e_nw f_sad at pos(.025, .84)
    with dissolve.nowait
    debbie "Must you be such a drama queen all the time?!"
    show anon a_hold_pants f_nervous -p_bend_low
    show debbie a_side
    jenny "Whatever."
    show anon p_pants_on_01 -m_teeth -o_right:
        yoffset 90
        xzoom -1
        parallel:
            ease .25 yoffset 0
            choice:
                ease .25 yoffset 90
            choice:
                ease .25 yoffset 70
            choice:
                ease .25 yoffset 60
            repeat 8
        parallel:
            ease 2. xoffset -100
            xzoom 1
            ease 2. xoffset 100
            xzoom -1
        repeat
    show debbie a_wtf e_r f_bored
    "*Door closes*"
    show debbie a_side e_nw f_sad
    anon @ -m_talk "( Ahh man, this is so gross! )"
    show debbie e_w f_calm o_right at pos(.225, 1.)
    show anon ob_pants p_fall at right
    debbie "Sorry, sweetie... [saga.cast.jenny] distracted me and-"
    show debbie a_surprised e_sw f_surprised m_talk
    show anon p_feet
    with vpunch
    pause
    hide anon
    show debbie a_shock of_blush -m_talk
    with dissolve.nowait
    debbie "Oh my god!!"
    debbie a_cover_face e_b f_worried_surprised "Sweetie, what are you doing?!"
    show anon a_surprised c_naked d_soft e_nw f_worried_surprised of_grass at pos(.6, 1.3)
    with dissolve.nowait
    anon "I'm sorry, I-"
    show anon a_side e_w at center
    with dissolve.nowait
    jump deb03_outro.merge


label deb03_outro.rails:
    jump deb03_hall.rails
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
