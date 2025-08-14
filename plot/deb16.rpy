label deb16_lobby:
    call shot.debbie_lobby_stairs

    if saga.camera.last is saga.sets.debbie_landing:
        show anon a_pocket o_right with dissolve
    else:
        show anon a_pocket with dissolve

    jenny "{i}*Gasp*{/i} No!"
    anon f_confused o_left @ -m_talk "Hmm?"
    jenny "You're fucking kidding me, right?!"
    pause
    jenny "He said that?!"
    jenny "Yeah, right... he fucking wishes!"
    anon "What's going on?"
    show jenny a_phone e_sw f_annoyed o_right at pos(.1)
    with dissolve.nowait
    jenny "You couldn't pay me to-"
    show jenny a_phone_wave_off e_w at left
    show anon a_up f_surprised at pos(.55)
    jenny "Move it, loser!"
    show jenny a_phone o_left p_stand_away
    anon f_sceptical "What is your problem?!"
    hide jenny
    show anon a_side e_nw
    with dissolve.nowait
    jenny "He's one hundred percent bullshitting!"
    jenny "Uh huh."
    anon a_wave "Umm, hello?!"
    anon a_point "You left the TV on!"
    jenny "Yeah, send me a link to it."
    anon @ -m_talk "..."
    anon a_side e_w f_pouty "No, don't worry... I'll get it."
    hide anon with dissolve.nowait
    anon "Such a freakin' bitch."
    return


label deb16_lounge:
    scene debbie_lounge at stage(.725, .425, 2.25)
    show anon f_confused at right with dissolve
    anon @ -m_talk "( Huh? )"
    anon @ -m_talk "( What on earth was [saga.cast.jenny] watching? )"
    hide anon with dissolve
    return


label deb16_lounge.rails:
    scene camera at stage
    show anon a_pocket f_pouty with dissolve
    anon @ -m_talk "( I should head to the living room and turn off the TV [saga.cast.jenny] left on. )"
    anon @ -m_talk "( We can't exactly afford to be running the electric bill up right now. )"
    hide anon with dissolve
    return


label deb16_tv:
    call shot.debbie_lounge_side
    show anon e_n p_couch_side_tilt with dissolve
    pause
    anon f_surprised @ -m_talk "( What the- )"
    hym "Oh no, landlady... What happened?"
    anon f_confused @ -m_talk "( Why did she- )"
    lsd "Thank god you're here!"
    lsd "I was trying to reach a sock that was stuck to the back of the dryer and now I'm stuck..."
    hym "... You've gotta help me!"

    if saga.cast.jenny < 'footjob':
        anon @ -m_talk "( ... Is this- )"
        pause
        anon f_surprised @ -m_talk "( Oh my god, [saga.cast.jenny] was watching porn! )"
    else:

        anon f_curious @ -m_talk "( Heh, was she watching porn in the living room again? )"
        anon f_happy @ -m_talk "( And yet somehow, in her head, {i}I'm{/i} the biggest pervert in this house. )"
        anon @ -m_talk "( Sheesh, what a hypocrite! )"

    anon e_w f_surprised p_couch_side_turn @ -m_talk "( Pretty brazen of her to do it with [saga.cast.debbie] sleeping in the next room. )"
    hym "Arg, you're really wedged in there!"
    show anon e_n f_calm p_couch_side_tilt
    lsd "Tell me about it."
    hym "I can't seem to get enough leverage from this angle."
    show anon f_curious
    lsd "Maybe you should try it with your pants off?"
    hym "Excellent plan, landlady!"
    hym "Let's try that."

    scene debbie_tv
    show tv dryer onlayer aux
    with fade
    anon "( Hey, this scenario is actually kinda... )"
    hym "Perhaps if I were to apply a copious amount baby oil to your shapely rear end, you might slide free?"
    lsd "Oh yes, sweetie!"
    lsd "Cover me in oil!"
    scene onlayer aux
    with hold.aux

    label deb16_tv.cookie hide:
    call shot.debbie_lounge_side
    show anon e_n f_happy p_couch_side_tilt
    with fade
    anon @ -m_talk "( ... Dang! )"
    show anon p_couch_side_twist
    pause
    show anon p_couch_side_twist_away
    pause
    show anon f_shy p_couch_side_tilt
    hym "I can't believe this isn't working."
    lsd "Any other ideas?"
    hym "Perhaps a few whacks to your bottom will jar you loose?"
    show anon d_hard
    lsd "Y-you want to spank me?"
    hym "Only in an effort to free you from that damnable machine, landlady."
    anon e_s p_couch_side @ -m_talk "( Maybe I could just... )"
    anon a_bottom_down_01 d_none @ -m_talk "( ... I mean, the universe is pretty much telling me to do this, right? )"
    show anon a_bottom_down_02
    "{i}*Whack*{/i}"
    show anon a_jerk c_casual_down e_n f_calm p_couch_side_tilt
    lsd "Oh, my goodness!"
    "{i}*Whack* *Whack*{/i}"
    lsd "Oh, yes!!"
    anon f_happy @ -m_talk "( This dialogue is atrocious... )"
    anon @ -m_talk "( ... And yet, I can't look away. )"
    hym "Grr, this isn't working either."
    show anon f_curious
    lsd "I think, maybe your boxer shorts are hampering your efforts?"
    hym "Ah, what excellent observation!"
    show anon f_confused
    lsd "Yes, my vantage from inside the dryer is really allowing me to see the issue from a unique perspective."
    hym "I'll remove them, posthaste!"
    anon f_happy s_5 @ -m_talk "( Oh, here we go! )"
    pause
    anon f_worried @ -m_talk "( Meh, he's not so big. )"
    show debbie_lounge_couch_side open
    show debbie a_cover_mouth e_b f_tired m_yawn p_couch_side_door behind couch at default, blur(10), tint('00106545')
    with dissolve.nowait
    debbie @ -m_talk "{i}*Yawn*{/i}"
    debbie a_doorframe e_osw f_confused -m_yawn "[saga.cast.jenny], is that you?"
    anon a_jerk_01 e_w f_surprised p_couch_side_turn "Ah, crap!" with hpunch
    show anon a_cover e_s m_teeth p_couch_side
    show debbie a_side e_ow p_stand at pos.couch_side_behind_walk, blur(5), noop
    debbie "Oh, [saga.cast.anon]."
    show anon e_wnw f_worried of_blush p_couch_side_turn -m_teeth
    show debbie a_couch_rest e_w o_right z_b_f_of at pos.couch_side_behind_rest, blur(None), tint(None)
    show mimic debbie at pos.debbie
    debbie "W-what are you-"
    show debbie f_surprised m_talk
    pause
    hym "Who could have forseen all this oil making the floor so slippery?!"
    show anon e_n p_couch_side_tilt
    debbie a_embarrassed -m_talk "Oh."
    hym "If we're not careful we could end up in an even more precarious spot..."
    anon e_wnw p_couch_side_turn "I, umm... this isn't-"
    debbie a_couch_rest e_ese f_shy "I'm sorry, sweetie..."
    debbie @ e_se "... I didn't mean to interrupt."
    anon e_s p_couch_side "Y-you're not mad?"
    hide mimic
    show debbie_lounge_couch_side as couch behind debbie
    show debbie e_e o_left p_couch_side_squat_turn z_reset at reset
    debbie "No, of course not."
    show anon e_e
    debbie a_lap p_couch_side_turn "Honestly, I'm just glad you're not doing this in my room for once."
    anon f_shy "Oh."
    anon e_s f_worried "Right."
    pause
    debbie @ e_sse "Don't stop on my account."
    anon e_w f_surprised p_couch_side_turn "You mean, I can-"
    debbie f_calm "Keep going."
    anon e_s f_shy p_couch_side "O-okay, sure."
    show debbie e_sse f_shy
    show anon a_jerk s_4
    pause
    show anon e_e
    debbie e_e f_curious "I thought you didn't like pornography?"
    anon "Err, I don't... usually."
    debbie e_n p_couch_side_tilt "But this one got you going, huh?"
    anon e_n p_couch_side_tilt "Y-yeah, I guess so."
    debbie "Is it because the woman is stuck in a dryer?"
    anon "Ehh-"
    show anon f_surprised
    show debbie f_surprised
    hym "Oops, I think I accidentally ended up inside you for a second there."
    show anon s_6
    lsd "Oh, that's alright, sweetie... I don't mind."
    show anon f_curious
    show debbie f_curious
    hym "You don't?"
    lsd "If it gets me unstuck, I say go for it!"
    show anon a_jerk_01 f_surprised
    show debbie f_surprised
    hym "{i}*Gasp*{/i} But you're my {i}landlady{/i}... surely we shouldn't-"
    debbie e_e f_curious p_couch_side_turn "Really, [saga.cast.anon]?"
    anon e_e p_couch_side "H-hey, I didn't pick it... it was on when I came in here."
    debbie @ -m_talk "Mhm."
    pause
    show anon f_worried
    debbie e_n p_couch_side_tilt "How did this silly woman wind up stuck in there to begin with?"
    anon a_jerk e_n f_calm p_couch_side_tilt s_4 "Yeah, I dunno..."
    anon "... Something about trying to reach a sock, I think."
    debbie f_happy "Heh, it's such a ludicrous scenario."
    anon "Well, that's modern porn for you."
    lsd "Oh, that's it sweetie..."
    lsd "... I can feel it working!"
    hym "Ahh, {i}landlady{/i}!"
    debbie f_curious "Boy, they're really hammering home that she's his landlady, huh?"
    anon "Heh, yeah... I guess, umm..."
    anon "... {i}Some people{/i} are really into that stuff."
    debbie f_concerned of_blush "{i}*Gulp*{/i} Y-yeah, I guess so."
    pause
    hym "Ugh! It's such a tight fit!"
    show debbie f_curious
    lsd "We can't give up now..."
    show anon f_happy s_8
    lsd "... Just do it harder!"
    debbie f_calm @ e_b f_happy m_laugh "Hehe!"
    debbie e_e p_couch_side_turn "So, how is sex supposed to get her unstuck?"
    anon e_e f_shy p_couch_side "Pretty sure we left logic behind a while ago."
    debbie "Heh, I take your point."
    show anon e_n f_calm p_couch_side_tilt
    pause
    show debbie e_sse f_shy
    pause
    show debbie e_n f_calm p_couch_side_tilt
    pause
    debbie a_knee p_couch_side_legs_up_tilt "I can't believe this just happened to be on the porn channel."
    anon "Y-yeah, pretty weird, right?"
    show debbie of_none
    pause
    debbie e_e f_curious p_couch_side_legs_up_turn "Why is her butt so shiny?"
    anon "Oh, he covered her in baby oil before you came in."
    debbie @ e_r f_bored "Pfft, of course he did."
    show debbie e_n f_calm p_couch_side_legs_up_tilt
    pause
    show debbie a_rub
    pause
    show anon e_e f_confused p_couch_side
    pause
    debbie a_rub_01 e_e f_shy p_couch_side_legs_up_turn "Sweetie, don't stop watching the TV."
    anon f_worried "Right, sorry."
    show anon e_n f_calm p_couch_side_tilt
    show debbie a_rub e_n f_calm p_couch_side_legs_up_tilt
    pause

    scene debbie_lounge_couch
    show anon a_jerk c_casual_down e_onne p_couch s_12 at pos.couch_sit_left
    show debbie a_rub e_onw p_couch_legs_up
    with fade
    debbie "Man, he's really giving it to her, huh?"
    anon "Y-yeah."
    pause
    debbie "They are totally gonna break that dryer."
    anon a_jerk_01 e_w f_happy p_couch_turn "Heh, that's where your mind goes?"
    debbie "Hehe, sorry... it's just..."
    show anon e_sw f_surprised
    debbie "... Those machines are expensive."
    show anon a_jerk f_horny s_16
    pause
    show debbie e_w
    pause
    show anon a_jerk_01 e_w f_worried_surprised
    debbie a_rub_01 f_shy of_blush p_couch_legs_up_turn "Sweetie!"
    debbie "... You're embarrassing me!"
    anon f_worried "S-sorry, it's just..."
    anon f_shy @ e_sw "... You're distracting!"
    debbie f_calm "Eyes on the TV, mister."
    anon f_confused "Aww, can't I just watch you?"
    debbie f_sad of_none "Sweetie, we shouldn't-"
    anon f_worried "C'mon [saga.cast.debbie]..."
    show debbie e_sw f_worried
    anon @ e_sse "... You've watched me do it."
    debbie e_se f_shy "I know that, sweetie but-"
    anon f_confused "Please!"
    debbie m_lip @ -m_talk "Mm."
    pause
    show debbie e_w
    anon f_shy "Just a little bit?"
    show anon f_happy
    debbie e_b -m_lip "Ugh, how do you keep talking me into these things?"
    show anon e_sw
    debbie e_s of_blush p_couch_pants_off_01 "We can try it this once..."
    show anon a_jerk f_horny_smug
    show debbie p_couch_pants_off_02
    pause
    debbie a_rest c_robe_open_lewd e_w f_worried oa_pants p_couch_rub "... But don't go expecting this to become a regular thing!"
    debbie f_confused of_none p_couch_rub_turn "You hear me, [saga.cast.anon]?!"
    show debbie f_sceptical
    anon @ -m_talk "Hmm?"
    show debbie f_pensive
    anon a_jerk_01 e_w f_worried_surprised "O-oh, umm... yeah, of course."
    show anon f_nervous m_teeth
    pause
    show debbie e_r f_bored
    pause
    show anon f_happy -m_teeth
    show debbie e_onw f_calm p_couch_rub
    pause
    show anon e_sw f_horny
    show debbie a_rub s_15
    pause
    anon a_jerk "Holy crap, that is so damn sexy, [saga.cast.debbie]!"
    show anon a_jerk_01 e_w f_surprised
    debbie a_rub_11 e_w f_sad p_couch_rub_turn "Language!"
    anon "Right, sorry."
    show debbie f_surprised of_blush
    anon e_sw f_horny "But seriously, I've never really seen... {i}that{/i} part of you..."
    show anon a_jerk
    show debbie f_shy
    pause
    show debbie e_sw
    pause
    show debbie a_rub f_horny
    pause
    show debbie a_rub_01 f_surprised
    pause
    show debbie a_rest e_e f_shy p_couch_rub
    pause
    debbie "A-and?"
    anon "It's so beautiful."
    pause
    anon e_w "You're the perfect woman!"
    show anon f_confused
    debbie e_onw @ e_r f_bored "Oh, stop it."
    anon f_shy "I mean it!"
    show anon f_horny_smug s_20
    debbie a_rub m_lip @ e_b -m_talk "Ngh."
    show anon e_sw
    pause
    debbie of_none -m_lip "{i}*Ahem*{/i}"
    debbie f_curious "S-so, you think he's gonna get her unstuck?"
    anon @ -m_talk "..."
    debbie a_rub_11 e_w f_confused p_couch_rub_turn "Sweetie?"
    anon e_w f_horny @ -m_talk "Hmm?"
    debbie @ e_b f_happy m_laugh "Hehehe!"
    show anon e_sw f_horny_smug
    debbie a_rub e_onw f_calm p_couch_rub "Never mind."
    pause
    show debbie e_w f_shy p_couch_rub_turn
    pause
    debbie e_sw "I-"
    pause
    debbie "Does it feel good?"
    anon f_horny "Very good."
    debbie s_20 @ -m_talk "{i}*Gulp*{/i}"
    pause
    debbie e_w "I can't believe we're doing this."
    anon "Y-yeah, me neither."
    show debbie e_sw m_lip
    pause
    debbie f_horny @ -m_talk "Mmm."
    debbie "Sweetie, you're being so rough with it."
    anon "Nah, just a little and it feels good."
    pause
    show debbie f_shy
    anon e_w "H-how does yours feel?"
    debbie e_w -m_lip "Ahh, it's-"
    debbie e_s p_couch_rub "Haah, starting to feel... really nice."
    pause
    anon e_sw "I wish I could touch you."
    debbie e_b s_25 @ m_lip "Ngh!"
    debbie e_w f_sad p_couch_rub_turn "Sweetie, we can't-"
    anon e_w f_tired_happy "I know."
    pause
    debbie e_se f_shy "What would you want to do to me?"
    anon f_shy_surprised of_blush "I dunno... Umm..."
    anon e_sw f_shy "... Probably kiss you."
    debbie e_w f_curious "Oh?"
    debbie f_horny "On the lips?"
    anon e_w "Yeah."
    anon e_wsw "Then maybe on your neck a bit."
    anon "Down to your collarbone."
    debbie e_b f_shy p_couch_rub s_27 "Oh, sweetie."
    anon e_sw "K-kiss little circles around your..."
    anon "... Nipples."
    debbie s_30 "Haah!"
    pause
    anon e_w of_none "What would you want me to do from there?"
    debbie e_w f_sad p_couch_rub_turn "Oh, I don't know."
    anon f_confused "You don't?"
    debbie e_se f_shy of_blush "I mean, I do... but I don't wanna say, it's embarrassing."
    anon f_calm "You don't have to be embarrassed."
    anon "Not with me."
    debbie m_lip s_33 @ -m_talk "Ngh!"
    debbie "I'd-"
    pause
    anon "Say it."
    show anon f_happy
    debbie e_w -m_lip "I'd want you to take my nipple... in your mouth..."
    pause
    debbie e_e p_couch_rub "... Oh, it’s so warm in here."
    anon @ f_shy "Maybe use my tongue?"
    debbie e_b s_35 "Yes!"
    anon f_horny "Then what?"
    show anon e_sw
    debbie s_36 "Your hands... would... caress up my thighs..."
    debbie s_37 "... T-teasing me... as you kissed your way... down further."
    anon @ e_w "Uh huh?"
    debbie s_38 "Past my belly button... towards..."
    debbie s_39 "... Oh, sweetie!!"
    debbie s_40 "I think, I'm gonna-"
    anon s_24 "This is awesome!"
    show anon f_horny_smug
    debbie "O-oh, god!!!"
    debbie f_distressed m_open p_couch_cum @ -m_talk "NGGHHH!!!" with flash
    show debbie a_rest e_s f_shy p_couch_rub -m_open
    anon s_28 @ e_w "Whoa."
    debbie "Haah... Haah..."
    debbie e_sw f_sad of_none p_couch_rub_turn "You haven't finished."
    show debbie e_w
    anon e_w f_horny "I'm about to."
    show debbie f_shy
    anon "That was so hot!"
    show anon e_sw
    pause
    anon f_shy @ e_w "Can you keep rubbing yourself?"
    debbie a_rub e_sw p_couch_rub s_15 "Sure."
    anon s_32 "Ahh, [saga.cast.debbie]!"
    pause
    anon f_horny "Y-you're so amazing!"
    show debbie m_lip of_blush
    pause
    anon "I'm so lucky to have..."
    anon "... A landlady... like you!!"
    pause
    show debbie p_couch_rub_turn
    anon e_b "Oh, here it..."
    anon f_distressed "... Comes!"
    show debbie s_20
    anon m_open od_cumshot p_couch_cum s_400ms @ -m_talk "HNNGGG!!!" with flash
    debbie -m_lip "Mm, that's it, sweetie... Let it all out."
    show debbie a_rest e_w
    anon a_side d_firm f_shy m_blow od_cum of_blush p_couch @ m_pant "Haah... Haah..."
    debbie a_side f_curious p_couch_tired_turn "Feel better?"
    anon e_w f_happy p_couch_turn -m_blow "So much better."
    debbie f_happy "Well, that makes me happy."
    pause
    $ renpy.end_replay()
    anon e_onne f_calm p_couch "Good grief, that lady is still stuck in the machine!"
    debbie e_onw f_calm p_couch_tired "You're right."
    debbie @ e_b f_happy m_laugh "Hehehe!"
    debbie "I can't believe somebody thought this was a good idea for a porn narrative."
    anon f_happy "Yeah, it's not very realistic."
    hym "Dang, I thought for sure my semen would be enough lubricant to slide you out."
    lsd "Yeah, me too."
    hym "I'm starting to run out of ideas, landlady."
    show anon f_surprised
    show debbie f_surprised
    lsd "Maybe we should try anal?"
    hym "Yeah, okay."
    hym "Let's try that!"
    debbie "Oh, dear."
    debbie e_w f_shy p_couch_tired_turn "I think we should call it a night there, what do you say?"
    anon e_w f_shy p_couch_turn "Y-yeah, good idea."

    scene black
    with dissolve
    mono ""

    scene debbie_lounge dark at stage(.5, .475, 3.5)
    show debbie a_clasp o_right
    show anon a_pocket at right
    with dissolve
    anon "S-so, how are you feeling about this?"
    debbie f_curious @ -m_talk "Hmm?"
    anon "You know, what we just did."
    debbie f_sad "Oh, I dunno... it's complicated."
    anon f_confused "What do you mean?"
    debbie "Well, part of me feels good."
    show anon f_happy
    debbie f_happy "Like, really {i}really{/i} good."
    show anon f_worried
    debbie e_s f_sad "But another part of me feels guilty."
    debbie "Like, I've just done something horrendous and I'm a terrible person for enjoying it."
    anon f_shy "You're not a terrible person, [saga.cast.debbie]."
    debbie e_w "Are you sure?"
    anon f_happy "I've never been so sure of anything in my life."
    debbie f_happy "Aww, you're such a sweet boy."
    show anon a_none b_none e_sw
    show debbie b_anon p_hug_away at pos.anon
    pause
    debbie "I hope you're right."
    pause
    show anon a_side e_w -b_none
    show debbie p_stand -b_anon at center
    debbie "For now, I'm just taking solace in the fact that you're happy and healthy."
    anon "I believe you mean {i}we're{/i} happy."
    debbie @ e_r f_bored "Heh, yes..."
    debbie "... We're happy."
    debbie "Now go to bed."
    debbie "I don't want you throwing your sleep schedule out of whack."
    anon a_salute "Yes, ma'am."
    anon "Good night, [saga.cast.debbie]."
    hide anon with dissolve.nowait
    debbie "Good night, sweetie."

    scene debbie_hall at stage with fade
    show anon a_pocket e_nw f_pensive o_right with dissolve
    anon @ -m_talk "( I guess, this means I'm off the hook for the whole walking into the bathroom on her thing. )"
    anon e_w f_happy @ -m_talk "( What an amazing night... )"
    anon e_b m_teeth @ -m_talk "( ... I can't wait to see where things go from here! )"
    hide anon with dissolve
    return


label deb16_tv.rails:
    scene debbie_lounge at stage(.725, .425, 2.25)
    show anon f_confused at right with dissolve
    anon @ -m_talk "( That can wait. Right now I'm really curious about what [saga.cast.jenny] was watching. )"
    anon @ -m_talk "( Was she trying to learn how to do her own laundry? )"
    hide anon with dissolve
    return


label deb16_post:
    return


label deb16_post.block:
    call shot.debbie_bed1_door
    show anon with dissolve
    anon @ -m_talk "( [saga.cast.debbie] told me to go to bed, and she's probably doing the same. )"
    anon @ -m_talk "( No need to disturb her further. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
