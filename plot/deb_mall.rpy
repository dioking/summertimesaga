label deb_mall_setup:
    return


label deb_mall_setup.debbie(when):
    anon f_confused "You going shopping anytime soon?"

    if when < 4:
        debbie f_calm "Probably in the next few days."

    elif when < 7:
        debbie e_nw f_pensive @ -m_talk "Hmm."
        debbie "I dunno."
        debbie e_w f_calm "Maybe later this week, I haven't decided."
    else:

        debbie f_sad "Oh, probably not for a week of so, sweetie."

    debbie f_curious "Why, did you need something?"
    anon f_shy "No, not really."

    if when < 4:
        anon "I just haven't seen you go for a bit."
        debbie f_calm @ f_happy "Oh, well... don't worry, I'll make sure we don't run out of food, sweetie."
    else:

        debbie f_calm "Alright, well... if you think of anything, lemme know and I'll pick it up next time."

    anon "Cool."
    return


label deb_mall_debbie(busy, seed):
    if saga.cast.debbie < 'kiss' or busy:
        jump deb_mall_debbie.busy

    if saga.cast.debbie < 'rub':
        jump deb_mall_debbie.deny

    call shot.debbie_lobby_bench
    show debbie a_purse c_casual e_s s_1
    show anon a_pocket o_right at left with dissolve
    anon "Morning, [saga.cast.debbie]."
    debbie a_purse_02 e_w "Morning, sweetie."
    anon f_confused "You heading out again?"
    debbie a_side oa_purse "Yup."
    debbie f_curious "You wanna join me?"
    anon f_surprised "Really?"
    anon "I can?"
    debbie f_calm "Sure, sweetie!"

    menu:
        "Let's go!":
            pass
        "Maybe next time.":

            jump deb_mall_debbie.bail

    anon f_happy "I'd never pass up a chance to spend the day with my favorite lady."
    debbie f_happy "Aww, my little charmer."
    debbie "Ready to go?"
    anon "Absolutely!"
    hide debbie with dissolve.nowait
    show anon e_b m_teeth o_left
    pause
    hide anon with dissolve

    scene mono debbie_car_outing1
    mono "I found myself looking forward to this little ritual of ours more and more." with fade
    mono "Not only was it gratifying to assist [saga.cast.debbie] with her shopping..."
    more "... But it was the perfect opportunity to spend some one on one time with her."

    scene mall_hall1 noon at stage(.35, .5, 5)
    with fade
    show debbie a_clasp c_casual oa_purse at pos(.65)
    show anon a_pocket at pos(.85)
    with dissolve.nowait
    anon "So what's on the agenda for today?"
    debbie e_nw f_pensive "Hmm, let's see..."

    if seed < .1:
        jump deb_mall_debbie.shop1

    elif seed < .2:
        jump deb_mall_debbie.shop2

    elif seed < .3:
        jump deb_mall_debbie.shop3

    elif seed < .4:
        jump deb_mall_debbie.shop4

    elif seed < .5:
        jump deb_mall_debbie.shop5

    elif seed < .6:
        jump deb_mall_debbie.shop6

    elif seed < .7:
        jump deb_mall_debbie.shop7

    elif seed < .8:
        jump deb_mall_debbie.shop8

    elif seed < .9:
        jump deb_mall_debbie.shop9

    show debbie e_w f_calm o_right at pos(.6)
    debbie "... Oh, nothing in particular today."
    debbie f_curious "It's just nice to be out and about, don't you think?"
    anon "Yeah, sure."
    show debbie f_happy
    anon f_happy "Especially with such good company."
    debbie "Aww, that's such a wonderful compliment!"
    show anon e_b p_debbie_hug_away
    show debbie b_anon p_hug_away at pos.anon
    debbie "That's why you're my sweetie..."
    show anon m_laugh
    debbie "... Sweetie."
    show debbie a_side p_stand -b_anon at pos(.6)
    anon a_side e_w p_stand -m_laugh "Heh, thanks."

    label deb_mall_debbie.merge:

    if .5 <= seed < .6:
        scene mono mall_hall1_deb push
    else:
        scene mono mall_hall1_deb

    mono "Our time together at the mall sailed by in a flash." with fade
    mono "It felt like we had no sooner decided what do than it was time to leave."

    scene debbie_car_inside
    show anon a_side_knee p_car_turn
    show debbie c_casual p_car
    show debbie_car_inside wheel as wheel
    with fade
    debbie "Phew, thanks again for coming with me and helping, sweetie."
    anon f_happy "No problem!"
    anon "Actually, it was a lot of fun."
    debbie f_curious p_car_turn "Yeah?"
    anon "I always have fun when I'm with you, [saga.cast.debbie]."
    debbie f_shy "Aww, me too, sweetie."
    debbie "I'm so happy we've become so close over these past few weeks."
    anon "Yeah, I know what you mean."

    menu:
        "Kiss.":
            pass

    show debbie f_curious
    show anon f_horny
    pause
    hide anon
    debbie a_push_anon_face f_surprised "W-wait, sweetie..."
    show debbie e_e
    anon "Mmmnnphf?"
    show debbie a_side e_w
    show anon a_wait f_confused p_car_turn
    anon "Huh?"
    show anon a_side_knee
    debbie f_worried_surprised "... We shouldn't do that here..."
    debbie e_e "... Someone might see us."
    anon f_worried_surprised "O-oh, right."
    show anon e_e
    pause
    show debbie e_w f_sad
    anon a_uneasy e_w f_shy "Sorry, I wasn't thinking."
    debbie f_shy "It's alright."
    debbie f_calm "Let's just wait on that until we get home, yeah?"
    anon a_side_knee f_confused @ -m_talk "Hmm?"
    debbie f_horny "We can have some private time before we head inside."
    anon f_surprised "Oh!"
    pause
    anon f_shy "Y-yeah, okay."
    show debbie a_wheel_down e_oe f_calm oa_fingers p_car z_b_f_a
    show mimic debbie at pos.debbie
    anon f_happy "I can't wait."
    debbie @ -m_talk "Mmm."

    scene mono debbie_car_outing2
    mono "For some reason, those rides home always seemed to take forever." with fade
    mono "Maybe it was all the anticipation of what awaited us at our destination."

    scene debbie_car_inside dusk garage
    show anon a_side_knee p_car_turn
    show debbie a_wheel_down c_casual e_oe oa_fingers p_car z_b_f_a
    show debbie_car_inside dusk wheel as wheel
    show mimic debbie at pos.debbie
    with fade
    debbie "Oh, thank goodness..."
    hide mimic
    debbie a_side e_w f_horny oa_none p_car_turn z_reset "... Finally!"
    hide anon
    show debbie p_car_peck_surprised
    anon @ -m_talk "( !!! )"
    debbie "Mmm."
    show debbie p_car_kiss
    pause
    show anon a_wait f_horny p_car_turn z_b_f_d behind debbie
    show mimic anon at pos.anon
    debbie a_touch_anon_knee f_shy p_car_turn "I can't believe we're doing this..."
    debbie "... It's so wrong."
    hide mimic
    hide anon
    debbie p_car_kiss "Mmm."
    pause
    show anon a_wait f_horny p_car_turn z_b_f_d behind debbie
    show debbie f_horny p_car_turn
    show mimic anon at pos.anon
    anon "You're a real good kisser, [saga.cast.debbie]."
    debbie "Oh, sweetie."
    hide mimic
    hide anon
    debbie p_car_kiss "Mmm."
    pause
    show debbie d_anon_hard
    pause
    show anon a_wait d_hard f_horny_smug p_car_turn z_b_f_d behind debbie
    show debbie p_car_turn
    show mimic anon at pos.anon
    pause
    hide mimic
    show anon z_reset
    debbie a_side e_sw f_surprised @ -m_talk "( !!! )"
    show anon a_side_knee
    pause
    debbie e_w f_shy of_blush "{i}*Ahem*{/i} G-goodness, umm..."
    debbie "... I think that's probably enough for one day... don't ya think?"
    anon e_s f_confused p_car @ -m_talk "Hmm?"
    anon a_surprised f_surprised "Ah, geez!"
    show debbie of_none
    anon a_cover_dick e_w f_worried p_car_turn "S-sorry, [saga.cast.debbie]... I just-"
    debbie f_calm "It's alright, sweetie..."
    debbie "... Perfectly natural."
    debbie f_shy "You'd probably better stay out here until that goes down though, yeah?"
    anon e_s "Y-yeah, okay."
    debbie "That's my good boy."
    show anon e_w f_shy
    debbie a_touch_anon_knee f_calm "Thanks again for today."
    anon f_calm "Y-yeah, you too."
    debbie "I'll see you in there."
    anon "Okay."
    show anon p_car_twist_away
    show debbie_car_inside -base
    show debbie_car_inside base dusk garage as base behind debbie_car_inside
    show debbie a_side p_stand behind debbie_car_inside at pos(.725, .5), blur(10), zoom(.5)
    with dissolve.nowait
    pause
    show debbie p_stand_away at pos(.1), blur(10), zoom(.5)
    anon a_side_knee e_s f_shy p_car @ -m_talk "( Man, that was really starting to get hot and steamy. )"
    hide debbie with dissolve.nowait
    anon a_facepalm e_b f_worried_surprised @ -m_talk "( Stupid penis... )"
    anon e_s @ -m_talk "( ... Why do you always have to ruin everything?! )"
    pause
    anon a_side e_n f_shy @ -m_talk "( Oh well, it was still a good day. )"
    return 'kiss'


label deb_mall_debbie.bail:
    anon a_rub f_shy "I've kinda got something else going on today."
    debbie @ f_sad "Oh."
    debbie "Well, that's wonderful!"
    show anon a_side f_confused
    debbie "Makes me so happy to see you're getting out there and taking the world by the horns."
    anon "Uh huh."
    show anon a_think e_nw f_pensive
    show debbie f_confused
    pause
    anon e_w f_shy "Rain check?"
    debbie f_calm "Of course, sweetie."
    show anon a_side o_left
    hide debbie
    with dissolve.nowait
    debbie "I'll see you later!"
    anon a_wave "Bye, [saga.cast.debbie]!"
    hide anon with dissolve
    return


label deb_mall_debbie.busy:
    call shot.debbie_lobby_bench
    show debbie a_purse c_casual e_s s_1
    show anon a_pocket o_right at left with dissolve
    anon "Hey, [saga.cast.debbie]."
    anon "Going somewhere?"
    debbie a_purse_02 e_w "Yeah, I'm just running to the mall to pick up a few things for dinner..."
    debbie a_side f_curious "... Did you need something?"
    anon "Nah, I'm good."
    debbie f_calm "Heh, alright sweetie."
    hide debbie with dissolve.nowait
    anon a_wave o_left "Drive safe!"
    hide anon with dissolve
    return


label deb_mall_debbie.deny:
    call shot.debbie_lobby_bench
    show debbie a_purse c_casual e_s s_1
    show anon a_pocket o_right at left with dissolve
    anon "Hey, [saga.cast.debbie]."
    anon "Grocery shopping again?"
    debbie @ -m_talk "Mhmm."
    anon f_shy "You want some help?"
    debbie f_curious @ -m_talk "Hmm?"
    show debbie a_purse_01 e_w
    pause
    debbie f_shy "Oh, umm... N-no, that's alright..."
    show anon f_worried
    debbie "... I should be fine... handling this one alone."
    anon "You're sure?"
    debbie a_side oa_purse "Yeah, I think that's for the best."
    anon "Because really, it wouldn't be a problem if-"
    show anon f_worried_surprised o_left
    hide debbie
    with dissolve.nowait
    debbie "See ya tonight, sweetie!"
    anon a_whisper "W-wait, I was just gonna tell you that-"
    pause
    anon a_side f_sad "{i}*Sigh*{/i} She's gone."
    pause
    anon a_think e_sw f_pensive o_right @ -m_talk "( I suppose she's still feeling awkward about the kissing. )"
    anon @ -m_talk "( Nothing for it, I guess... )"
    anon a_side e_w f_worried @ -m_talk "( ... I'll just have to give her time to process. )"
    hide anon with dissolve
    return


label deb_mall_debbie.shop1:
    debbie "... We need toilet paper and kitchen roll."
    debbie "I'd like to get some more cleaner for my mop."
    show debbie e_w f_calm o_right at pos(.6)
    debbie "And I think [saga.cast.jenny] mentioned needing more juice."
    anon f_confused "She's not doing that stupid juice cleanse thing again, is she?"
    debbie f_shy "Heh, I'm not sure."
    anon "Ugh, she's such a sap... falling for one of those internet trend diets."

    if renpy.random.random() < .5:
        show anon f_smug
        debbie "Yeah, you might be right about that."
    else:

        show anon f_surprised
        debbie "Well, it's hard to argue with results, sweetie"

    jump deb_mall_debbie.merge


label deb_mall_debbie.shop2:
    debbie "... I've got this recipe for boneless beef short ribs I think you kids will like."
    show debbie e_w f_calm o_right at pos(.6)
    debbie "I just need to pick up a few things from Consum-R to get it going."
    anon f_worried "No olives, right?"
    show anon f_worried_surprised
    debbie @ e_b f_happy m_laugh "Hehe!"
    debbie "Don't worry... I wouldn't do that to you."
    show anon f_shy
    debbie f_happy "In fact, it's got all your favorites..."
    show anon f_happy_surprised
    debbie "... onion, mushrooms, pepperoncini, and some parmigiano-reggiano cheese."
    anon f_happy "You're the best, [saga.cast.debbie]!"
    debbie @ f_calm "Aww!"
    debbie "Thanks, sweetie."
    jump deb_mall_debbie.merge


label deb_mall_debbie.shop3:
    debbie "... I'd like to see about getting a new crock pot."
    debbie f_sad "That old one we have at home is definitely on its last leg."
    show debbie e_w f_calm o_right at pos(.6)
    anon "Alright."
    debbie f_curious "Does salad sound good for tonight?"
    anon f_sceptical "Just salad?"
    debbie @ -m_talk "Mhmm."
    pause
    debbie f_confused "What's wrong with that?"
    anon f_grumpy "Well, there's no meat... for starters."
    debbie f_happy @ e_b m_laugh "Hehe!"
    debbie f_calm "Alright, sweetie."
    show anon f_shy
    debbie "We'll grab some pork chops too."
    anon f_confused "And some katsu sauce?"
    debbie "Sure, if you'd like."
    show anon a_cheer e_b f_happy m_teeth
    show debbie e_b f_happy m_laugh
    pause
    jump deb_mall_debbie.merge


label deb_mall_debbie.shop4:
    debbie "... [saga.cast.tammy] from next door said they're having a clothing sale at Cupid this week."
    show debbie e_w f_curious o_right at pos(.6)
    debbie "Do you mind if we swing by there and have a look?"
    anon a_shy_neck e_nw f_pensive "Ehh, clothes shopping?"
    debbie a_fists f_elated "Yeah!"
    anon a_side e_w f_sceptical "I'm totally gonna end up sitting in a corner holding your purse aren't I?"
    debbie a_side f_worried_surprised "What, no!"
    debbie f_calm "I need your discerning eye to help me find something pretty."
    show debbie f_shy
    anon @ e_r f_bored "{i}*Sigh*{/i} Uh huh, sure..."
    show debbie f_curious
    anon f_pouty "... I know exactly where this is going."
    debbie f_happy @ e_b m_laugh "Hehe!"
    debbie "I promise... it'll be fun!"
    anon f_tired "Alright, if you say so."
    jump deb_mall_debbie.merge


label deb_mall_debbie.shop5:
    debbie "... [saga.cast.jenny] asked me to grab her a couple new pairs of jeans."
    anon f_confused "What, why?!"
    show debbie e_w f_curious o_right at pos(.6)
    anon "She hardly ever wears pants."
    debbie f_shy "Oh, that's just because she's in a rut at the moment, sweetie."
    debbie f_calm "She'll pull herself out of it soon enough, maybe even get herself a nice job."
    anon f_disgusted @ f_worried "If you say so."
    debbie @ e_b f_happy m_laugh "Hehe!"
    debbie "She will!"
    debbie "You'll see."
    anon f_confused "Cupid then?"
    debbie @ -m_talk "Mhmm."
    jump deb_mall_debbie.merge


label deb_mall_debbie.shop6:
    debbie "... I'm nearly out of lotion at home and I'd like to get some flowers for the kitchen table."
    show debbie e_w f_surprised o_right at pos(.6)
    anon f_surprised "Bum Bum cream?!"
    debbie f_curious "Heh, how do you know the name of my lotion?"
    anon e_s f_worried "That's... not important..."
    anon a_finger e_w f_worried_surprised "... We gotta get you more, right now!"
    debbie f_shy "Well, hold on."
    show anon a_surprised o_right behind debbie at pos(.45)
    debbie a_side e_e f_curious "There's a few other things I'd like to-"
    show anon a_calm_down f_grumpy at pos(.475)
    show debbie a_fists f_surprised
    anon "Not now, [saga.cast.debbie]..."
    show anon at pos(.675)
    show debbie at pos(.8)
    with dissolve.nowait
    anon "... Cupid."
    show anon at pos(.875)
    show debbie at pos(1.)
    with dissolve.nowait
    anon "Brazilian Bum Bum!!"
    hide anon
    hide debbie
    with dissolve.nowait
    debbie "Oh, geez... Alright, sweetie."
    jump deb_mall_debbie.merge


label deb_mall_debbie.shop7:
    debbie "... I just need to grab some canned goods for our sides during dinner this week."
    show debbie e_w f_curious o_right at pos(.6)
    debbie "Is there anything you wanted to do?"
    anon a_think e_nw f_pensive "Anything I want?"
    debbie f_calm "Sure!"
    anon @ -m_talk "Hmm."
    anon a_uneasy e_w f_shy "Maybe we could swing by Cosmic Cumics... see if they have the new issue of Brine Boy and Pickle Girl?"
    debbie f_confused "I'm sorry. What?!"
    show anon a_wtf f_happy behind debbie
    anon "They're a dynamic duo of super heroes who it turns out are actually twins separated at birth!"
    debbie @ -m_talk "..."
    show debbie f_surprised behind anon
    anon a_fists "They fight against the tyranny of Dill Diddler and his pack of evil ninja cyborg lizard men."
    debbie f_confused "And this is a comic... that you read?"
    anon a_hips "Yeah!"
    anon "It's awesome."
    debbie f_shy "Umm, okay..."
    debbie "... Let's go have a look then."
    show debbie f_curious
    show anon a_cheer e_b m_teeth
    pause
    jump deb_mall_debbie.merge


label deb_mall_debbie.shop8:
    show debbie e_w f_calm o_right at pos(.6)
    debbie "... I thought this could be your day."
    anon f_surprised "Really?"
    debbie "Yeah, we don't always have to do {i}my{/i} shopping..."
    debbie f_curious "... What would you like to do?"
    anon f_happy "Maybe we can go check out the new video games?"
    debbie f_calm "Sure, sweetie."
    debbie "I just want you to have the best day possible!"
    anon "Awesome!"
    jump deb_mall_debbie.merge


label deb_mall_debbie.shop9:
    show debbie e_w f_curious o_right at pos(.6)
    debbie "... Are there any new movies out?"
    anon f_confused "What do you mean?"
    debbie f_sad "Well, I just haven't seen anything good on TV in a while..."
    debbie f_shy "... So I thought, maybe we could look at the new releases in the video store."
    anon "You mean Cosmic Cumics?"
    debbie f_curious "I dunno, do they sell movies there?"
    anon "Yeah, I think so."
    anon f_calm "Or, well... I know they sell anime at the very least."
    debbie f_confused "What is an \"anime\"?"
    anon f_surprised "Whoa, you serious?"
    debbie @ -m_talk "..."
    anon a_finger f_happy "They're like cartoons but with adult-"
    anon f_worried "You know what... never mind..."
    anon a_side f_shy "... It's just something you need to experience first hand."
    debbie f_calm "Alright, sweetie."
    jump deb_mall_debbie.merge


label deb_mall_garage:
    if 'kiss' < saga.cast.debbie < 'rub':
        jump deb08_outro

    scene mono debbie_garage_greet
    mono "I may not have always been a perfect tenant, but that's not to say I didn't have my moments." with fade
    mono "And occasionally surprising [saga.cast.debbie] to welcome her home and help unload the shopping was definitely one of them."

    call shot.debbie_garage_rear
    show anon o_right behind car at left
    with fade
    show debbie a_grocery c_casual behind car at right with dissolve
    debbie "Oh, hey sweetie."
    anon "Hey, [saga.cast.debbie]."
    show anon a_surprised e_sw at pos(.4)
    anon "Can I help you with that?"
    debbie a_grocery_give e_sw "Oh yes, please!"
    show anon a_grocery e_s
    debbie a_hips e_w "Thank you!"
    anon e_w "My pleasure."
    show anon o_left with dissolve
    hide anon with dissolve
    debbie "You're such a good boy!"
    hide debbie with dissolve

    scene debbie_kitchen -debbie at stage with fade
    show anon a_grocery e_sw o_right at right with dissolve
    anon a_reach e_s p_bend "( I'll just leave these here. )"
    anon a_side p_stand @ -m_talk "( [saga.cast.debbie] can decide where she wants them after she gets changed. )"
    hide anon with dissolve

    call shot.debbie_garage_rear
    with fade
    show anon a_think e_nw f_pensive o_right behind car with dissolve.nowait
    anon @ -m_talk "( Now what was I doing? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
