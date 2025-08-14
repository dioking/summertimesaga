label ano01_intro:
    scene debbie_bed3 at stage(.6, .425, 2.5)
    with fadewait
    show anon a_fist_mouth f_tired with dissolve.nowait
    anon @ e_b m_yawn "{i}*Yawn*{/i}"
    anon a_side @ -m_talk "( Ugh... I hate getting up early. )"
    anon a_phone e_sw f_worried @ -m_talk "( No text messages from [saga.cast.erik]. Maybe he's still sleeping. )"
    anon a_pocket e_b f_happy m_teeth @ -m_talk "( I'll stop by his house on the way to school. )"
    hide anon
    with dissolve
    jump tutor.hud


label ano01_jenny:
    scene debbie_landing_wakeup
    "*Footsteps*"
    show jenny p_debbie_landing_wakeup1
    jenny "{i}*Yawn*{/i}"
    jenny p_debbie_landing_wakeup2 "Hnnggghh!!"
    jenny p_debbie_landing_wakeup3 "Hmm?"

    scene debbie_landing_wakeup at stage(.642, .53, 1.9, b=0)
    show jenny e_c f_annoyed p_debbie_landing_wakeup_close
    with fade
    jenny "Why don't you just take a picture, it'll last longer!"
    pause

    call shot.debbie_bed2_door
    show anon a_pocket f_worried o_right at left
    with fade
    show jenny f_annoyed at right with dissolve.nowait
    anon "Oh, uhh... sorry."
    show jenny f_disgusted
    anon f_surprised @ a_wave f_calm "H-how's it goi-"
    jenny f_annoyed "Save it, loser!"
    anon "..."
    anon f_sceptical "Jeez, what's your problem?!"
    jenny "Tch, what do you think my problem is?!"
    jenny "... Stuck here, living with you."
    anon f_tired "{i}*Sigh*{/i} Yeah, whatever..."
    jenny f_calm "Shouldn't you be at school or something?"
    anon f_sceptical "Shouldn't you be out looking for a new job?!"
    with dissolvefast.nowait
    jenny a_upset f_surprised "!!!"
    jenny a_fold f_annoyed "Oh, you do not want to play this game with me, smart ass."
    anon "Hey, you're the one who started it!"
    anon @ -m_talk "..."
    anon a_think e_nw f_pensive @ -m_talk "{i}*Sniff*{/i}"
    jenny f_confused "What are you making that face for?"
    anon @ -m_talk "{i}*Sniff*{/i}"
    anon a_pocket e_w f_horny "Something smells really good..."
    jenny f_annoyed "Uhh, yeah... It's the breakfast that's waiting for you downstairs, dummy."
    jenny @ e_r "I can't believe she's still making you breakfast every day."
    jenny "It's been over a month since your dad died."
    anon f_worried "Yeah, well... Maybe she likes doing it?"
    anon "She's a nice lady."
    jenny "Ugh, yeah. She's too nice if you ask me."
    show anon f_angry
    hide jenny
    with dissolve.nowait
    pause
    anon @ -m_talk "( I wonder what crawled up her butt? )"
    anon f_calm @ -m_talk "( I should get downstairs and see what smells so delicious! )"
    hide anon
    with dissolve
    return


label ano01_jenny.fence:
    scene debbie_bed3 at stage
    show anon with dissolve.nowait
    anon @ -m_talk "( I should get going, I am back in school today. )"
    hide anon
    with dissolve
    return


label ano01_debbie:
    scene debbie_kitchen_stove
    show debbie p_stove_cook
    pause
    debbie e_c p_stove "Good morning, sweetie! I'm making you some breakfast!"
    debbie "I thought you'd like something special for your first day back at school."
    anon "Thanks [saga.cast.debbie], but I'm not sure I have time."
    debbie "You're sure? I'm making your favorite..."
    show debbie p_stove_hug
    pause

    scene debbie_kitchen -debbie at stage
    show debbie b_anon o_right p_hug_away at pos(.65)
    show anon p_debbie_hug_away at pos.debbie
    with fade
    debbie "... Happy face pancakes with three strips of baaaacon!"
    show debbie -b_anon -p_hug_away at pos(.4)
    show anon -p_debbie_hug_away behind debbie
    anon "Oh man..."
    show debbie a_pancake p_stand_away -o_right at left
    pause
    show debbie f_elated o_right -p_stand_away
    anon e_sw f_surprised @ -m_talk "..."
    anon f_shy_surprised "... No, I really shouldn't..."
    anon @ -m_talk "..."
    show anon e_w f_shy
    pause
    show debbie f_calm
    anon "I think [saga.cast.erik] overslept again and I don't wanna be late on my first day back."
    debbie p_stand_away -o_right "Hah, again huh?"
    debbie a_mug o_right -p_stand_away "Well, I guess you'd better get a move on then."
    anon f_calm "Yeah, thanks anyways, [saga.cast.debbie]."
    show anon o_right
    debbie "My pleasure, sweet- Oh! Wait!"
    anon -o_right @ -m_talk "Hmm?"
    debbie @ e_b f_happy m_laugh "I nearly forgot!"
    debbie "I spoke with [saga.cast.diane] yesterday, and she mentioned that she could use some help with her garden."
    debbie "She asked if you might be willing?"
    anon f_worried "What?!"
    anon "I don't know anything about gardening, [saga.cast.debbie]..."
    debbie @ e_b f_happy m_laugh "Oh c'mon, it's easy! [saga.cast.diane] will teach you, and if you do a good job, she'll pay you as well!"
    debbie "It could be a good way to earn a little extra money for college, don't you think?"
    anon "Yeah, I guess."
    anon f_calm "I'll swing by her place after school sometime."
    debbie "Atta' boy!"
    show debbie b_anon e_sw p_hug_lean behind anon at center
    show anon e_s f_worried p_debbie_hug_lean at pos.debbie
    debbie "I know these last few weeks have been hard..."
    debbie "But your father would want you to carry on, you know?"
    debbie "You'll get through this. I promise things will get better."
    anon @ e_nw "Yeah, I-I know."
    pause
    show anon e_w f_calm -p_debbie_hug_lean at right
    debbie e_w -b_anon -p_hug_lean "Chin up, sweetie! I'm here for you."
    anon "Thanks, [saga.cast.debbie]."
    hide anon
    with dissolve
    return


label ano01_debbie.fence:
    scene camera at stage
    show anon with dissolve.nowait
    debbie "[saga.cast.anon], what's taking so long?!"
    debbie "You're going to be late!"
    anon "Coming [saga.cast.debbie]!"
    anon @ -m_talk "( I should head to the kitchen and say good morning before I leave. )"
    hide anon
    with dissolve
    return


label ano01_leave:
    return


label ano01_leave.bed1:
    call shot.debbie_bed1_door

    if saga.cast.debbie in saga.sets.debbie_bed1:
        show anon f_worried with dissolve
        anon @ -m_talk "( Barging in there really doesn't seem like a good idea. )"
        anon @ -m_talk "( Besides, I need to go and meet [saga.cast.erik] before we're late. )"
    else:

        show anon a_point with dissolve
        pause
        show anon a_surprised_up_both f_surprised m_teeth
        with none.nowait
        debbie "[saga.cast.anon]?" with hpunch
        show anon a_uneasy f_shy o_right -m_teeth
        show debbie at pos(.85)
        with dissolve.nowait
        debbie "Are you looking for something in my room?"
        anon "I was... umm... looking for my phone!"
        show debbie f_curious
        anon a_phone @ e_sw f_surprised "But it's right here in my pocket actually!"
        debbie "Isn't [saga.cast.erik] waiting for you?"
        anon a_pocket f_calm "Yeah, I'm on my way!"

    hide anon with dissolve
    return


label ano01_leave.debbie:
    call shot.debbie_kitchen_hob
    show anon at right with dissolve.nowait
    pause
    show debbie_kitchen pan
    debbie a_mug_down o_right -p_stand_away "Hey, sweetie! Shouldn't you get going?"
    anon "Yeah. I was on my way."
    hide anon
    with dissolve
    return


label ano01_leave.fence:
    scene camera at stage
    show anon with dissolve.nowait
    anon @ -m_talk "( I can't just hang around I have to get to school! )"
    hide anon
    with dissolve
    return


label ano01_tammys:
    return


label ano01_tammys.rails:
    scene camera at stage
    show anon with dissolve.nowait
    anon @ -m_talk "( I should head next door and pick up [saga.cast.erik]. )"
    anon @ -m_talk "( I hope he's not still sleeping... )"
    hide anon
    with dissolve
    return


label ano01_erik:
    scene tammy_main -erik at stage(.26, .65, 3.5)
    show tammy_main erik as body at stage(.26, .65, 3.5, b=0)
    show anon e_sw o_right at left with dissolve.nowait
    anon "Dude!"
    erik "Hmm?"
    anon f_confused "What are you doing?"
    hide body
    show anon e_w
    show erik a_game_play ob_backpack
    with dissolve.nowait
    erik "Oh, man... You gotta check out this new game I got."
    erik e_sw "It's called Bushi Bushi Bukkake Baseball Bunny Babes in Space."
    anon @ e_sw "Huh?"
    erik "Bushi Bushi Bukkake Baseba-"
    anon "No, I heard you, I just... What the heck kinda name is that?"
    erik "I dunno..."
    erik a_game_show e_w "... But check it, sexy samurai bunny girls playing baseball in outer space!"
    anon e_sw "Hmm, weird."
    pause
    anon "Wait, what's going on over there in the dugout?"
    erik f_shy "Ah, yeah... that."
    erik @ e_sw f_calm "Well, you see..."
    erik "... before the girls step up to the plate, you have to power them up."
    anon f_shy_surprised "Are they-"
    pause
    anon f_shocked m_open @ f_surprised "Is that-"
    erik "Hehehe!"
    anon f_surprised -m_open "Holy crap... it looks like she fell in a vat at the mayonnaise factory!"
    erik @ e_b f_happy m_laugh "Hehehe!"
    anon e_w f_worried "Where do you even find this stuff, man?"
    erik "Japan, my dude!"
    erik "Japan."
    anon f_calm "And your landlady is okay with you having this?"
    erik f_worried "Oh, definitely not!"
    erik "But what a landlady doesn't know, can't hurt her, right?"
    anon e_sw "Yeah, I guess."
    erik a_game_play e_sw f_calm "C'mon, I'll show you more on the way."
    erik e_w f_horny "Wait 'til you see what happens when you hit a home run!"
    tammy "[saga.cast.erik]!"
    show anon e_w f_worried_surprised
    erik a_game_pocket f_surprised @ -m_talk "( !!! )" with hpunch

    label ano01_erik.cookie hide:
    scene tammy_main_intro1
    with fade
    tammy "Yoo-hoo!"
    erik "[saga.cast.tammy]?"

    scene tammy_main_intro2
    show tammy c_yoga p_tammy_main_intro2_run
    with fade
    tammy "You forgot your lunch, baby."
    erik "Oh, umm..."

    scene tammy_main -erik at stage(.26, .65, 3.5)
    show erik a_lunch o_right ob_backpack at pos(.425)
    show anon o_right at left
    show tammy c_yoga at pos.erik.pinch_cheek
    with fade
    erik f_shy "... Thanks."
    tammy "Tuna fish on rye, with celery and applesauce."
    erik "Did you cut the crusts off?"
    tammy a_hips f_annoyed @ e_r "Of course I cut the crusts off; You think I dunno how to take care of my little puddin' face?!"
    erik f_calm "Sweet!!"
    tammy a_side f_calm "Hello, [saga.cast.anon]."
    anon @ a_wave "Hey, [saga.cast.tammy]."
    tammy f_sad "I'm so sorry about your father."
    show anon f_sad
    show erik e_e f_worried
    tammy "How's everyone holding up?"
    anon "Oh, we're doing okay."
    show erik e_w
    tammy "Are you taking good care of your landlady?"
    tammy f_calm "You only get one, ya know!"
    anon f_worried "Yes, ma'am."
    tammy e_ssw f_sad "Poor woman has to be hurtin' after all this..."
    tammy e_w f_calm "... I should take her a nice quiche."
    erik "Yeah, that's great [saga.cast.tammy]."
    erik e_sw @ a_wrist "Wow, look at the time!"
    erik e_w @ e_e "We should really get going."
    tammy a_hips "Uh, uh, uh!"
    tammy a_pinch_cheek "Not before I get some lovin' from my little puddin' face!"
    show anon f_surprised
    erik f_sad "Aww, Mrs. [saga.cast.tammy.clan.name[0]]..."
    show tammy a_wide behind erik
    tammy "Come 'ere you!"
    erik "You said you'd stop doing this in front of my-"

    scene tammy_main_intro2
    show tammy c_yoga p_tammy_main_intro2_kiss
    show erik e_o f_distressed p_tammy_main_intro2_kiss
    with fade
    tammy "{i}*Muuuuuaaaah*{/i}"
    erik "... friends."
    show tammy e_b p_tammy_main_intro2_hug
    hide erik
    with dissolve.nowait
    erik "{i}*Hurk*{/i}"
    tammy "Oh, I just love you so much!!"
    erik "Myee, ah ruv ew choo..."
    tammy "You're the most wonderful boy in the whole world!"
    pause

    scene tammy_main -erik at stage(.26, .65, 3.5)
    show erik a_lunch f_shy o_right ob_backpack of_blush v_askew at pos(.425)
    show tammy c_yoga at pos.erik.pinch_cheek
    show anon f_happy o_right at left
    with fade
    erik a_adjust "Y-yeah, thanks."
    show erik a_side v_normal
    tammy "You two have a wonderful day, okay?"
    show erik -o_right -of_blush at pos(.45)
    erik "C'mon, [saga.cast.anon]."
    anon a_point f_calm "Say, could I get one of those?"
    show erik f_worried
    tammy a_wide f_happy "Of course you can!"
    show anon a_surprised f_horny_smug at pos(.35)
    erik f_surprised "No!!"
    show tammy f_surprised
    show erik b_anon p_drag_away at pos(.325)
    show anon f_worried_surprised p_erik_drag_away at pos.erik
    anon "B-but-"
    show erik at pos(.2)
    show anon f_pouty at pos.erik
    erik "C'mon, we're gonna be late!"
    hide erik
    hide anon
    show tammy a_side
    with dissolve
    anon "Ah, man."
    tammy a_wave f_calm "See you tonight, baby!"
    $ renpy.end_replay()

    scene helen_main at stage(.75, .6, 2)
    show erik b_anon p_drag_away at right
    show anon f_pouty o_right p_erik_drag_away at pos.erik
    with fade
    anon "Dude!"
    show anon -o_right -p_erik_drag_away
    show erik f_surprised o_right ob_backpack -b_anon -p_drag_away at left
    erik "What?"
    erik "We're late."
    anon @ -m_talk "..."
    erik f_worried "We {i}aaaare{/i}."
    anon "Fine, let's just go."
    hide anon
    hide erik
    with dissolve
    return


label ano01_erik.rails:
    scene camera at stage
    show anon e_b f_happy m_teeth with dissolve.nowait
    anon @ -m_talk "( Of course he's gaming, typical [saga.cast.erik]. )"
    anon e_w -m_teeth @ -m_talk "( I should let him know I'm ready to go. )"
    hide anon
    with dissolve
    return


label ano01_mia:
    scene school_main at stage(.65, .55, 2) with None
    show erik a_game_play e_sw ob_backpack at pos(.55)
    show anon e_sw f_confused at right
    with dissolve.nowait
    erik "Oh, baby... it's a triple play!"
    anon "Uh huh."
    erik "That's gonna send my team into ultimate bunny babe gangbang mode!"
    show anon e_w
    erik "I've got thirty seconds to fill up all her holes and max her 'o-power' gauge."
    show anon f_surprised behind erik
    erik a_game_show o_right "Dude, you gotta check this out!"

    scene school_main_mia with fade
    erik "Which hole do you think I should start with?"
    erik "... The answer may surprise you!"

    scene school_main_mia_close away with RadialZoom((.472, .485), .162)
    anon "Uh huh."
    erik "Dude."

    scene school_main_mia_close turn with dissolve.nowait
    erik "Hey, dude!"

    scene school_main_mia_close smile with dissolve.nowait
    anon "Uh huh."

    scene school_main at stage(.65, .55, 2)
    show anon e_o f_surprised at right
    show erik a_game_show f_angry o_right ob_backpack at pos(.55)
    erik "DUDE!!!" with hpunch
    anon e_wsw f_worried "Huh?"
    anon f_confused "What?"
    erik f_horny "Guess which hole!"
    anon e_s "Uhh, I dunno..."

    menu:
        "The carrot hole?":
            anon e_wsw "... the carrot one?"
            erik f_calm "Wrong!"
            show anon f_worried
            erik f_nervous "You gotta save the carrot hole for last, otherwise you risk having your bunny maker bitten off."
            show erik e_sw f_horny
        "The bunny hole?":

            anon e_wsw "... the bunny hole?"
            erik f_calm "That's right!"
            show anon f_calm
            erik f_horny "You gotta fill up that bunny hole 'til it's fit to bursting..."
            show anon e_s f_surprised
            erik e_sw "... Then you ease it in the bunny bum bum nice and slow."
        "The bunny bum-bum?":

            anon e_wsw "... wait. The \"bunny bum-bum\"?!"
            erik f_calm "Wrong!"
            show anon f_worried
            erik f_horny "The bunny bum-bum is second but it also applies the biggest multiplier."
            show anon f_confused
            erik e_sw "Once you're inside, the scoreboard goes crazy!"

    anon e_w f_calm @ e_wsw f_confused "Dude, what the fu-"
    show mia a_books o_right at left
    with dissolve.nowait
    mia "Heya, guys!"
    show erik a_game_pocket e_w f_surprised -o_right behind anon
    anon a_wave "Hey, [saga.cast.mia]!"
    show erik a_side f_nervous
    mia "Hey, [saga.cast.anon]! Glad to see you're back!"
    show anon a_side
    mia "Hi, [saga.cast.erik]! How was your weekend?"
    erik "I mostly stayed in my room..."
    mia @ f_happy "That's cool. Sometimes I like alone time too!"
    mia "What about you, [saga.cast.anon]? What have you been up to?"
    show erik e_e f_worried
    anon e_osw f_sad "Well, I'm not sure if you've heard or not, but my dad passed away. So I've been dealing with that..."
    show erik e_w
    mia f_worried "Oh yeah. I heard from my mom..."
    mia "I didn't mean to bring it up. I'm sorry you had to go through that. I'm just glad you're finally back!"
    anon e_w f_calm "Thanks. I'll be fine. Don't worry."
    mia f_calm "Listen, I was looking for someone to help me get ready for the final exams, so..."
    show anon f_surprised
    show erik f_surprised
    mia "... If you're interested, let me know!"
    show erik e_e f_calm
    anon a_uneasy f_shy "Uhh, sure... I guess?"
    anon "Where do you want to meet? The library?"
    show anon a_pocket f_calm
    show erik e_w
    mia f_worried "Umm, I'd have to ask my parents, first."
    mia "They probably won't let me, though."
    show anon f_worried
    show erik f_worried
    mia "I'm not really allowed to stay late after school or see friends outside of my house."
    show erik e_e
    anon "Really?! That sucks!"
    show erik e_w
    mia "Yeah... Heh, heh."
    mia f_calm "Anyway, it'd be easier if you just came over to my house to study..."
    show anon f_calm
    show erik f_calm
    mia f_happy "You know where I live, so just drop by whenever you want!"
    pause
    mia f_calm "I'd better get going. Science class is starting soon!"
    mia f_happy "[saga.cast.tori] said today's laboratory experiment will be challenging."
    show anon f_worried
    show erik f_worried
    mia "That means it's probably gonna to take the entire hour to complete."
    erik a_facepalm "Ugh. Don't remind me..."
    show erik e_sw
    mia "Talk to you later guys!"
    hide mia
    with dissolve
    return


label ano01_mia.rails:
    scene helen_main at stage with None
    show erik o_right ob_backpack at left
    show anon at right
    with dissolve.nowait
    erik "We should get moving, you remember what [saga.cast.ursula] is like!"
    anon f_worried @ -m_talk "{i}*Gulp!*{/i}"
    anon "I wish I could forget."
    hide anon
    hide erik
    with dissolve
    return


label ano01_roxxy:
    scene school_hall1 -crowd2 at stage
    show dexter a_ball_crotch at pos(.7)
    show roxxy a_hips e_b f_happy m_laugh at pos(.8)
    with None
    show erik o_right ob_backpack behind dexter at pos(.3)
    show anon a_pocket o_right behind dexter at pos(.15)
    with dissolve.nowait
    roxxy @ -m_talk "... So then [saga.cast.becca] threw her retainer in the toilet!"
    dexter @ e_b f_happy m_laugh "Bahahahahahah!"
    roxxy e_w f_cynical -m_laugh @ -m_talk "..."
    roxxy "... Ugh, what are you two losers looking at?!"
    erik "I think we're looking at the combined IQ of 2."
    show erik e_b f_happy m_laugh
    anon @ e_b f_happy m_laugh "Hah!!"
    show erik e_w f_calm -m_laugh
    roxxy f_angry "Excuse me?!"
    dexter f_angry "... Huh? I don't get it."
    roxxy @ e_r f_annoyed "They're calling us stupid..."
    dexter "They are?!"
    dexter a_ball_point "Hey! You calling us stupid?!"
    show anon f_surprised
    erik f_worried "I... N-no, I didn't... I mean, I wouldn't..."
    dexter a_ball_crotch @ a_ball_threat "'Cause I'll smash your face in, you little shit!"
    roxxy f_horny @ f_cynical "... And what are {i}you{/i} laughing at?"
    roxxy "Didn't your deadbeat loser of a father kill himself or something?"
    show anon e_osw f_sad
    erik e_e f_bored @ -m_talk "..."
    anon e_w f_angry "At least I {i}had{/i} a father growing up..."
    show erik e_w f_calm
    anon "... And I don't live in a {i}trailer{/i}!!"
    show dexter e_b f_happy m_laugh
    roxxy f_surprised "!!!" with hpunch
    show dexter e_w f_surprised -m_laugh
    roxxy f_angry "... You're dead!"
    show dexter f_angry
    roxxy "[saga.cast.dexter], get 'em!!!"
    show anon f_surprised
    dexter f_calm "Hold up, [saga.cast.roxxy]. [saga.cast.ursula] is coming..."
    dexter "If I get caught fighting again, [saga.cast.bridget] said she'll kick me off the team."
    hide dexter with dissolve.nowait
    roxxy @ e_r f_annoyed "Pfft, fine..."
    roxxy "... This isn't over, [saga.cast.anon]!"
    roxxy "I'll deal with you later!"
    hide roxxy
    with dissolve.nowait
    pause
    show ursula a_ruler f_angry behind erik at right with dissolve
    show anon f_worried
    show erik f_worried
    ursula "You two! Get over here, RIGHT NOW!!!"
    show erik e_sw
    ursula "What are you still doing in the damn hallway?!"
    erik @ e_w "Sorry, [saga.cast.ursula]! We were just-"
    ursula f_calm "Ah, [saga.cast.anon]! Finally returned to us I see..."
    anon "Y-yes, ma'am."
    ursula f_angry @ e_b m_yell "Well, it's about time! Do you have any idea how far your grades have fallen?!"
    anon f_surprised "... They have?"
    erik e_w "That doesn't seem fair!"
    erik "Don't you know his dad-"
    ursula "That's quite enough, young man!"
    ursula "I suggest you get your butt to class before you find it sitting in detention!"
    erik e_sw @ -m_talk "..."
    ursula "... And as for you, [saga.cast.anon], we need to discuss your failing grades!"
    ursula "I want you upstairs, in my office, right away!"
    anon f_worried "Yes, [saga.cast.ursula]."
    hide ursula with dissolve
    show erik e_w -o_right at center
    erik "Man, she's pure evil..."
    anon f_calm "Heh, yeah."
    erik "I'm serious! She's like the Evil Ice Queen from Whorecraft!"
    show erik f_calm
    anon "Well, I'd better get up to her office before her mood worsens."
    erik "Good luck, dude..."
    anon "... Thanks."
    erik @ e_b f_happy m_laugh "Oh shoot, I almost forgot!"
    erik "I slipped a little welcome back present into your locker!"
    anon "Really?"
    erik "Glad to have you back, dude!"
    anon "Thanks, [saga.cast.erik]!"
    anon a_think e_nw f_pensive @ -m_talk "Hmm..."
    anon "... You know, I don't remember my locker combination."
    show anon a_pocket e_w f_worried
    erik f_worried "You didn't write it down?"
    anon "No, but I guess I should have, huh?"
    erik f_calm "You're probably going to have to talk to [saga.cast.ursula] about it."
    anon f_calm @ f_worried "Ugh, you're probably right..."
    anon @ a_wave "I'll see you later, [saga.cast.erik]."
    erik "Yup, see ya, [saga.cast.anon]."
    hide anon
    hide erik
    with dissolve
    return


label ano01_roxxy.rails:
    scene school_main at stage(.65, .55, 2) with None
    show anon at right
    show erik f_nervous o_right ob_backpack
    with dissolve.nowait
    erik "C'mon, you don't wanna be late on your first day back!"
    anon "Right."
    hide anon
    hide erik
    with dissolve
    return


label ano01_kevin:
    scene school_hall2 at stage with None
    show anon a_pocket o_right at pos(.3)
    show kevin a_pot c_apron at pos(.7)
    with dissolve.nowait
    kevin "Whoa, [saga.cast.anon]?!"
    kevin "When did you get back?"
    anon @ a_wave "Hey, [saga.cast.kevin]."
    anon "Today's my first day."
    kevin "Right on, bro."
    kevin a_brofist f_woozy m_talk "Good to see you!"
    show anon a_handshake f_surprised
    pause
    show anon a_uneasy f_shy
    kevin a_head f_sceptical -m_talk "Sorry about your dad by the way..."
    anon a_pocket f_worried "Yeah, thanks."
    pause
    anon f_calm "What's with the apron?"
    kevin a_pot f_sad "Ugh, [saga.cast.ursula] put me on cafeteria duty until I raise my grade in [saga.cast.tori]'s class..."
    anon f_surprised "You're failing science?"
    kevin "Well, I'm not failing yet but it definitely isn't looking good, bro."
    anon f_worried "That sucks man."
    kevin "Tell me about it!"
    kevin "I haven't had a good workout in weeks!"
    anon f_calm "Oh, yeah?"
    anon "Still hanging out down at that gym?"
    kevin @ e_b f_happy m_laugh "You know it, bro!"
    kevin a_flex f_calm "I can't let these guns go unpolished, can I?"
    anon "Heh, no, I guess not..."
    kevin a_pot "Oh, that reminds me!"
    kevin "We got that new Muay Thai trainer there."
    kevin "His name is [saga.cast.peng]."
    kevin "He's like a grandmaster or something, with all his ancient teachings..."
    kevin "It's pretty awesome!"
    anon f_confused "Muay Thai?"
    kevin "Yeah, bro!"
    kevin "You know, like, kickboxing and stuff."
    anon f_calm "Really?"
    kevin "You should go in there and check it out!"
    anon a_uneasy f_shy "Oh, I dunno..."
    kevin "C'mon, bro!"
    kevin "You gotta get that body in shape."
    kevin "The people demand beefcake, not sweet cake!"
    anon a_pocket f_worried "Eh?"
    anon "I guess I could check it out..."
    show anon f_calm
    kevin @ e_b f_happy m_laugh "That's the spirit, bro!"
    kevin "Who knows, you might even be able to whoop [saga.cast.dexter]'s ass once you've got a few classes under your belt."
    anon "Psh, yeah right."
    pause
    anon "I should get going, man."
    anon "[saga.cast.ursula] is waiting on me upstairs in her office."
    kevin "Oh shit, bro... I didn't know that!"
    kevin "You better hurry on then before you end up in the cafeteria with me."
    anon @ a_wave "See ya, [saga.cast.kevin]."
    kevin "Come by the cafeteria later, and we can hang."
    anon "Alright."
    hide anon
    hide kevin
    with dissolve
    return


label ano01_kevin.rails:
    scene camera at stage
    show anon a_pocket f_worried with dissolve.nowait
    anon @ -m_talk "( [saga.cast.ursula] wanted to see me in her office, up on the third floor. )"
    anon @ -m_talk "( I'd better get there quick if I don't want detention. )"
    hide anon
    with dissolve
    return


label ano01_ursula:
    scene school_office1 -annie -ursula at stage
    show ursula a_ruler at pos(.65)
    show annie a_behind at pos(.85)
    show anon a_pocket f_worried o_right at left with dissolve.nowait
    anon "You wanted to see me, [saga.cast.ursula]?"
    ursula "Indeed, [saga.cast.anon]."
    ursula "We need to discuss your grades and whether or not you intend to graduate."
    anon f_surprised "It's really that bad?"
    ursula a_grades_show "Have a look for yourself..."
    show anon a_surprised e_sw f_shocked m_open
    pause

    scene school_office1 -annie -ursula at stage(.5, .9, 5)
    show misc_report
    anon "( !!! )" with hpunch
    pause

    scene school_office1 -annie -ursula at stage
    show ursula a_ruler at pos(.65)
    show annie a_behind at pos(.85)
    show anon a_rub f_worried o_right at left
    with fade
    anon "Oh man, I'm failing everything?!"
    ursula "I told you..."
    annie f_annoyed "That's what happens when you skip school for a month!"
    anon a_side "I wasn't skipping! My dad died!"
    ursula a_hips @ e_r f_bored "Be silent, [saga.cast.annie]!"
    annie @ f_curious "S-sorry, ma'am."
    show annie f_calm
    ursula "... Regardless of the circumstances."
    ursula "You'll need to find a way to raise these grades if you don't want to repeat next year."
    ursula "I'd suggest you speak to your teachers about making up the work you've missed."
    ursula "Perhaps they can come up with some extra credit assignments or something?"
    anon a_pocket "Y-yeah, okay."
    ursula "Do whatever it takes!"
    anon "Yes, ma'am."
    ursula "Good, now get to class."
    anon f_shy "... Actually, ma'am?"
    ursula "Yes?"
    anon "I forgot the combination to my locker. Can you help me get it open?"
    show ursula f_confused
    annie f_angry "What do you mean you forgot?!"
    show anon f_surprised
    annie "Everyone was told at the beginning of the year to write down their combinations!"
    anon f_shy "I umm..."
    anon "I lost it!"
    annie f_calm @ f_disgusted "Pfft, typical."
    ursula f_calm "That's very disappointing, [saga.cast.anon]."
    ursula "We'll have to get you a new lock."
    anon @ -m_talk "..."
    ursula "I'll send [saga.cast.annie] down with her master key momentarily..."
    ursula "I suggest you get everything that you need out now."
    ursula "It could be a while before the new lock arrives."
    anon f_calm "Yes, ma'am."
    ursula "Head there now and then get your butt to class after you're finished!"
    hide anon
    with dissolve
    return


label ano01_ursula.rails:
    scene camera at stage
    show anon a_pocket f_worried with dissolve.nowait
    anon @ -m_talk "( [saga.cast.ursula] wanted to see me in her office. )"
    anon @ -m_talk "( I should hurry up if I don't want detention. )"
    hide anon
    with dissolve
    return


label ano01_annie:
    scene school_hall1 -crowd2 at stage
    show anon a_pocket f_worried at right
    show annie a_behind o_right at left with dissolve.nowait
    annie "Alright, let's get this over with."
    show annie a_key_get e_s -o_right
    pause
    show annie a_key e_w
    anon f_calm @ f_surprised "Wow, so that key opens everybody's locker?"
    show annie a_key_get e_s
    pause
    annie a_behind e_w o_right "Pfft, this key opens every lock and door in the school."
    anon f_surprised "For real?!"
    annie "Duh, that's why it's called a {i}master{/i} key."
    anon f_sceptical "How come you get it?"
    annie f_annoyed "Umm, because I bust my ass every day helping [saga.cast.ursula] keep all you kids in line?!"
    anon f_worried "Kids? We're the same age..."
    annie @ f_calm "... Yeah, right. Everyone around here is so immature."
    anon "So you just have that master key with you all the time?"
    annie "Of course not! [saga.cast.ursula] keeps it in her office, but we like, never have to use it."
    anon "Never?"
    annie f_horny "Nobody else is dumb enough to lose their locker combination..."
    show anon a_side e_osw f_sad
    annie f_calm "Hurry up and grab what you need."
    annie "We're gonna be late for Athletics class!"
    anon e_w f_tired "Yeah, yeah. I'm going."
    return


label ano01_annie.annie:
    scene school_office1 -annie at stage
    show annie a_behind f_angry at right
    show anon a_pocket f_worried o_right at left with dissolve
    annie "Didn't [saga.cast.ursula] tell you to beat it?!"
    annie f_annoyed "Head down to your locker and I'll meet you there shortly!"
    hide anon
    with dissolve
    return


label ano01_annie.rails:
    scene camera at stage
    show anon with dissolve.nowait
    anon @ -m_talk "( I'm supposed to wait for [saga.cast.annie] by my locker... )"
    hide anon
    with dissolve
    return


label ano01_annie.ursula:
    jump ano01_annie.annie


label ano01_locker:
    scene school_hall1 -crowd2 at stage
    show anon a_think e_nw f_pensive o_right with dissolve.nowait
    anon @ -m_talk "( Hmm, so [saga.cast.ursula] has a master key in her office somewhere. )"
    anon @ -m_talk "( ... that would be a useful thing to have! )"
    anon @ -m_talk "( ... )"
    anon @ -m_talk "( Something to think about. )"
    anon @ -m_talk "( For now, I should head to the boys' locker room and get changed for Athletics class. )"
    hide anon
    with dissolve
    return


label ano01_judith:
    call shot.school_hall1w_judith
    show judith a_clasp e_ssw f_sad at right
    show anon a_pocket o_right at left with dissolve.nowait
    anon "Hey, [saga.cast.judith]..."
    anon f_worried @ -m_talk "..."
    anon "Is everything all right?"
    judith e_w "Oh, hey, [saga.cast.anon]..."
    judith "I'm just not feeling too well; I might just go home."
    anon "You're not coming to the Athletics class?"
    judith e_ssw "Well..."
    judith "... I just..."
    judith e_w "... I can't go in the boys' locker room."
    anon f_surprised "... The boys' locker room?"
    anon "Why would you need to go in the boys' locker room?"
    judith f_surprised "You mean nobody told you?"
    anon f_worried "... No?"
    judith f_shy "A pipe burst in the girls' locker room and it's closed for repairs..."
    judith f_sad @ e_ssw "We're sharing the boys' locker room now."
    anon f_surprised "For real?!"
    judith "I don't really feel comfortable about it, like the other girls."
    show judith e_ssw
    anon f_calm @ a_think e_nw f_pensive "Well..."
    anon "The class is starting soon, so there's probably not that many people left in there anyway?"
    judith e_w f_shy "Yeah, I guess you're right..."
    anon "I can go in with you, to make sure you're okay..."
    anon @ a_wave e_b f_smug "... And I won't look!"
    judith "Okay... I'll follow you, then."
    hide anon
    hide judith
    with dissolve
    return


label ano01_judith.rails:
    scene camera at stage
    show anon with dissolve.nowait
    anon @ -m_talk "( I should hit the boys' locker room and get changed for Athletics class. )"
    return


label ano01_change:
    scene school_boys at stage with None
    show anon a_pocket e_e o_right at pos(.35)
    show judith a_clasp f_shy o_right at pos(.15)
    with dissolve.nowait
    anon "See?"
    anon "It's not too bad, there's only a few people in here!"
    show anon e_w f_surprised
    show judith f_surprised
    show annie a_behind at right
    with dissolve.nowait
    annie "I hope you two remember the rules in regards to being late!"
    annie "If you're not in uniform and in the courtyard in one min-"
    anon e_b f_smug m_talk "It's okay, [saga.cast.annie]... we get it."
    anon "We'll be outside in just a moment..."
    show anon e_w f_worried -m_talk
    show judith f_confused
    annie "As the Student Union President and official hallway monitor..."
    annie "... It is my duty to write infractions to anyone breaking school guidelines!"
    anon f_pouty "Look..."
    show judith f_shy
    anon @ f_bored "[saga.cast.judith] is not very comfortable in the guys' locker room."
    anon @ f_bored "She's going to need some extra time to get ready, okay?"
    show anon f_angry
    annie f_annoyed "Is that right, [saga.cast.judith]?"
    show anon e_e f_worried
    judith e_ssw f_sad "Well..."
    judith "Y-yes..."
    show judith e_w
    show anon e_w f_angry
    annie "What's the matter?"
    annie "Just a little bit insecure around the boys?"
    annie "Or are you inciting disorder and disobeying the rules?"
    show anon e_e f_worried
    judith e_ssw "It's not..."
    judith a_cover_face "It's just that..."
    show anon f_surprised
    judith e_b f_crying @ a_cover_boobs f_sad "... I'm not... wearing a bra!"
    show anon e_w
    annie "Oh, I see... coming up with excuses to skip class, are we?"
    annie f_calm "Your lack of obedience is alarming, and I will not allow it!"
    annie @ f_angry "Get dressed immediately, or I'm sending you both to detention!!"
    show anon a_top_off c_casual_bottom f_calm
    show judith e_ssw f_sad p_top_off_01
    pause
    show judith p_top_off_02
    pause
    show anon p_bottom_off
    show judith p_top_off_03
    show judith p_top_off_04 with dissolve
    show judith p_top_off_05
    pause
    show judith c_casual_bottom p_bottom_off
    show anon a_side c_pants e_osw f_sad -p_bottom_off
    pause
    show judith a_clasp c_pants -p_bottom_off
    anon e_se f_surprised @ -m_talk "..."
    pause
    show anon e_s
    pause
    show anon d_firm
    show annie e_sw f_surprised m_talk
    pause
    show anon d_hard z_b_f_a_d
    show annie f_surprised_shocked
    pause
    anon e_w f_worried @ a_rub e_osw f_sad "Shit..." with hpunch
    judith a_surprised e_sw f_surprised "Oh, my..."
    annie a_point @ f_surprised "This..."
    annie "... This is..."
    annie e_w f_angry -m_talk "... This is improper and shameful!!"
    show judith a_clasp e_ssw f_sad
    anon @ e_e "I'm so sorry..."
    annie a_note_write @ a_jersey_give "Put your uniforms on and get your asses to class, NOW!!!"
    show annie e_ssw f_annoyed
    show judith c_gym_bottom p_bottom_off
    show anon c_gym_bottom d_none p_bottom_off z_reset
    pause
    show judith a_top_on_01 -p_bottom_off
    show anon c_gym p_top_on
    annie "I will have to report this incident to [saga.cast.ursula], along with your infractions for being late..."
    show judith a_top_on_02
    show anon a_pocket -p_top_on
    pause
    show judith a_clasp c_gym
    annie a_note_hips e_w "... Now, move it!!"
    hide judith
    hide anon
    with dissolve
    return


label ano01_change.rails:
    scene school_hall1w at stage
    show anon a_pocket f_confused o_right at left
    show judith a_clasp f_shy with dissolve.nowait
    judith "I thought you were coming with me!"
    anon a_uneasy f_worried "Relax, I'm coming."
    hide anon
    hide judith
    with dissolve
    return


label ano01_bridget:
    scene school_track -bridget -rhonda at stage
    show bridget a_fold at pos(.8)
    show anon a_pocket c_gym o_right at left with dissolve.nowait
    bridget "Look who decided to show up!"
    anon e_b f_happy m_laugh @ -m_talk "Hi, [saga.cast.bridget]!"
    anon @ -m_talk "I know I've missed a few training sessions, but I assure you that I will be ready for the Regional Athletics Tri-"
    show anon e_w f_surprised m_teeth
    bridget f_angry "Shut up, you maggot!" with hpunch
    bridget "You are one month behind everyone else, [saga.cast.anon], and I'm not going to let you drag down the team with your lack of commitment!"
    bridget "If you can't make the qualifying scores, you can forget about your credits and graduating this year."
    anon f_worried -m_teeth "Don't worry, ma'am! I'm sure the qualifiers will be no problem!"
    bridget "... Oh yeah?"
    bridget "Why don't you show us your \"elite athletic skills\" by doing twenty push-ups right now, you pathetic little twerp?!"
    show bridget a_whistle e_b m_yell
    anon "But-"
    show anon f_shocked m_open
    bridget @ -m_talk "{i}*WHISTLE*{/i}"
    show anon p_pushup_02
    show bridget e_sw p_bend -m_yell
    with dissolvefast.nowait
    anon "Ghh..."
    show anon p_pushup_01
    with dissolvefast.nowait
    bridget "One..."
    show anon p_pushup_02
    with dissolvefast.nowait
    anon "Ghhhh..."
    show anon p_pushup_01
    with dissolvefast.nowait
    bridget "Two..."
    show anon p_pushup_02
    with dissolvefast.nowait
    anon "... I... I can't..."
    bridget "Thr-"
    hide anon
    bridget @ -m_talk "..." with vpunch
    bridget "What?! Is that all you got?"
    show anon a_pocket c_gym e_osw f_sad o_right of_blush at left
    bridget a_fold e_w -p_bend "You can't even do three miserable push-ups?!"
    anon e_s f_worried "I..."
    anon @ e_w "I'm... Sorry... Ma'am..."
    bridget "You better get your ass to the local gym now, and start lifting, if you want to pass this class..."
    bridget "... Or just stick to French class, where hard work and good grades don't matter!"
    bridget e_b m_yell @ -m_talk "Now, GET OUT OF MY SIGHT!!!"
    hide bridget
    with dissolve
    pause
    show rhonda c_gym_lewd f_curious at right
    show anon e_w f_tired -of_blush
    with dissolve.nowait
    rhonda "You're never going to make it past the qualifiers..."
    rhonda "Why do you even bother coming to this class?"
    anon "I can still make it..."
    anon "And you know what... I was thinking, maybe you could help me tr-"
    rhonda @ f_angry "Hold it right there!"
    rhonda f_serious "If, by some miracle, you manage to make the trials... Then come talk to me. Otherwise, you can stop wasting your breath."
    show rhonda f_curious
    anon f_calm "Okay!"
    anon "But when I do, you'll have to show me some of your tricks!"
    rhonda "I'll be at the swimming pool for the next two weeks, training for the 200-meter trials..."
    rhonda "If you make the team, then come see me."
    anon a_handshake e_b f_happy m_teeth @ -m_talk "Deal!!"
    show anon e_w f_surprised -m_teeth
    rhonda @ e_r f_annoyed "Ugh... Pathetic..."
    hide anon
    with dissolve
    return


label ano01_bridget.rails:
    scene camera at stage
    show anon f_worried with dissolve.nowait
    anon @ -m_talk "( I should go to the field for my Athletics class... )"
    hide anon
    with dissolve
    return


label ano01_shower:
    call shot.school_hall1w_boys
    show anon c_gym o_right with dissolve.nowait
    anon @ -m_talk "( I better be quick or I'll be late for French class. )"
    hide anon
    with dissolve

    call shot.school_hall1w_boys
    with fadewait
    show anon a_surprised c_casual with dissolve
    pause
    hide anon
    with dissolve
    return


label ano01_shower.rails:
    scene camera at stage
    show anon with dissolve.nowait
    anon @ -m_talk "( I need to shower and change out of my gym clothes. )"
    hide anon
    with dissolve
    return


label ano01_viv:
    call shot.school_french_front
    show viv a_note_front at right
    show anon a_pocket o_right at left with dissolve.nowait
    viv "There you are!"
    anon @ a_wave "Hi, [saga.cast.viv]!"
    viv f_sad "Listen, [saga.cast.anon], I know you've had some personal matters to take care of, and that's why you've been absent lately..."
    viv "... But is everything okay?"
    anon f_worried @ e_sw "Yeah. I think I should be okay..."
    viv "You're not the only one a bit behind, you know."
    anon f_shy @ a_uneasy "It's definitely the hardest class we have, I think."
    viv f_calm "Well, if you ever need anything, let me know."
    anon "Thanks, [saga.cast.viv]."
    viv @ a_note_finger e_b f_happy m_laugh "Oh! That reminds me!"
    viv "I'm implementing a new learning opportunity for those trying to catch up."
    anon "Oh yeah?"
    viv f_horny "It'll be a bit more... One on one type of learning..."
    viv @ a_note_hair "... And I'm hoping it will energize students."
    anon f_calm "I see."
    viv f_calm "Why don't you take your seat and I'll be discussing it in front of the class."
    anon "Okay."
    hide anon
    with dissolve

    scene mono school_french_viv
    mono "[saga.cast.viv] had an interesting announcement to make that day." with fade
    mono "She planned to reward the student who showed the most improvement after the final quiz."
    more "Even offering to privately tutor anyone that was interested."

    scene mono school_french1
    mono "As much as I wanted to make an effort and get fully back into the swing of things..." with fade

    show mono school_french2
    more "... I had forgotten how much French class made me sleepy." with dissolve
    mono "It was a real struggle to focus on the lesson..."

    scene mono school_french3
    more ".. But fortunately my classmates were all too eager to help keep me alert." with hpunch

    scene mono school_french4 with dissolve
    mono "It felt a bit rough that first day back, but it was probably just because I'd not been around for a while, and so I'd temporarily become the center of attention."

    scene mono school_french5 with dissolve
    mono "It didn't matter though, I was more than capable of holding my own and showed them in no uncertain terms that they couldn't get to me..."

    scene mono school_french6
    more "... At least in theory." with hpunch

    call shot.school_french_front
    show viv a_note_front
    with fade
    viv @ a_note_finger "Oh! And before you all leave."
    viv "Any students interested in the after-school tutoring sessions, come talk to me in my office or tomorrow in class."
    viv @ e_b f_happy m_laugh "Au revoir!"
    hide viv
    with dissolve

    call shot.school_french_desks
    show eve a_pencil e_e o_right p_desk at pos(.6)
    show anon a_pencil o_right p_desk at pos(.25, 1.02)
    with fade
    eve "Hey, welcome back!"
    anon "Hi, [saga.cast.eve]."
    anon "Wow, I really like the new hair color!"
    eve a_hair e_b f_happy m_laugh @ -m_talk "Yeah?"
    eve a_pencil e_e f_calm -m_laugh "I was a little worried I couldn't pull it off..."
    anon @ e_b f_happy m_laugh "Oh, you definitely pull it off!"
    eve @ e_b f_happy m_laugh "Hehe, thanks, [saga.cast.anon]..."
    show eve f_nervous
    pause
    eve f_sad "... Sorry to hear about your dad."
    show anon f_worried
    eve "I know it's rough."
    anon "Yeah."
    eve "If you ever need to talk or something..."
    anon "Nah, it's really nice of you to offer but I'm okay."
    anon "I'm just trying not to think about it."
    anon "Focus on getting back into the swing of things, you know?"
    eve "Yeah, believe me, [saga.cast.anon]... I get it."
    show eve e_ssw
    pause
    eve f_nervous "You know, sometimes when I'm feeling down or whatever..."
    eve e_e "... I take my drawing pad and sit by this big fountain, over at the park."
    anon f_shy "Oh, yeah?"
    eve "It's so peaceful there, especially in the evenings..."
    anon "Sounds nice."
    eve "It is."
    eve "You should come check it out, sometime."
    anon f_calm "Alright, maybe I will."
    eve e_b f_happy m_laugh @ -m_talk "Cool."
    show eve e_ssw f_nervous -m_laugh
    pause
    anon f_worried "So, are you going to take [saga.cast.viv] up on her private lessons?"
    eve e_e f_confused "Private lessons?"
    anon "Yeah, the ones she was talking about at the start of class..."
    anon "Weren't you paying attention?"
    eve e_b f_happy m_laugh @ -m_talk "I might have dozed off a bit, haha."
    show eve e_e f_calm -m_laugh
    anon "Really?!"
    eve "Yeah, most of these classes put me to sleep..."
    anon f_shocked m_open @ -m_talk "But don't you have one of the highest GPAs in school?"
    eve f_nervous "Y-yeah, sorta..."
    anon f_worried -m_open "How do you manage that?"
    eve @ e_r f_annoyed "Oh, I dunno... Just lucky, I guess..."
    anon f_shy "What, that's crazy..."
    eve @ e_b f_happy m_laugh "No, I'm serious!"
    eve "I've just always been good at school."
    eve "It's like a gift or something, I can't really explain it."
    anon "Well, it's quite a gift."
    eve e_r f_annoyed "Yeah, I guess..."
    show eve e_ssw f_nervous
    pause
    show anon f_calm
    pause
    anon "I can curl my tongue."
    eve e_e f_confused "Hmm?"
    show eve f_nervous
    show anon f_pouty m_tongue
    pause
    anon @ -m_talk "Thee?"
    eve @ e_b f_happy m_laugh "Hehe!"
    show eve f_happy
    show anon e_b f_happy m_teeth
    pause
    anon e_w f_calm -m_teeth "That's really my only gift."
    anon "I'll trade you?"
    eve @ e_b m_laugh "Heh, mmm... Tempting but no."
    anon "Dang."
    show eve e_ssw f_nervous
    show anon e_s f_shy
    pause
    show eve e_e
    pause
    eve "Seriously [saga.cast.anon], if you ever need a pick me up come see me at the park."
    show anon e_w f_calm
    eve @ e_b_e f_horny "Bring that sense of humor with you."
    anon "Yeah, okay."
    anon "The park in the evening, huh?"
    eve e_b f_happy m_laugh @ -m_talk "Yup!"
    show eve o_right ob_chair z_ob as eve_chair behind eve at pos(.525)
    show eve o_right ob_desk z_ob as eve_desk behind anon at pos(.6)
    show eve a_shy e_w -m_laugh -o_right -p_desk
    with dissolve.nowait
    eve "I should get going."
    eve "[saga.cast.barb] had some art project she wanted to talk to me about..."
    anon "Alright."
    eve a_wave "Later, [saga.cast.anon]!"
    anon @ e_b f_happy m_laugh "See ya!"
    hide eve
    with dissolve
    return


label ano01_viv.rails:
    scene camera at stage
    show anon f_pensive with dissolve.nowait
    anon @ -m_talk "( I should go to French class now. )"
    hide anon
    with dissolve
    return


label ano01_outro:
    scene school_hall1 -crowd2 at stage
    show anon a_pocket e_nw f_pensive at right with dissolve.nowait
    anon @ -m_talk "( I should probably talk to [saga.cast.viv] about that private tutoring. )"
    anon @ -m_talk "( I can't understand any of the material in class... )"
    anon @ -m_talk "( ... I think I'm too far behind to catch up on my own. )"
    anon @ -m_talk "( A little bit of extra help never hurt anybody... )"
    anon a_think @ -m_talk "( ... And I may get that reward if I do well in the final quiz! )"
    pause
    show erik o_right ob_backpack at left with dissolve.nowait
    erik "Hey, [saga.cast.anon]!"
    anon a_side e_w f_calm "Oh... Hey..."
    erik "How was your first day back at school?"
    anon a_facepalm f_worried "Ugh... I don't even want to talk about it."
    erik f_worried "I see..."
    show anon a_side
    erik "What are you up to now?"
    anon e_nw f_pensive "Well, I told [saga.cast.debbie] that I would visit her friend [saga.cast.diane] at some point."
    anon e_w f_calm "She's gonna pay me to do some work for her."
    erik f_sad "Man... I wish I had a job..."
    erik @ e_b f_happy m_laugh "A job where I could just sit at my computer playing games all day, heh..."
    show erik f_calm
    anon f_worried @ a_point "Oh, speaking of computers... Mine is definitely broken."
    anon "I think I need to replace some parts in it, or something..."
    anon f_calm "You know any good stores where I could buy some?"
    erik "Hmmm... I usually shop for parts at Consum-R in the mall."
    erik "They sell lots of things for a reasonable price."
    anon "Alright then, I'll check it out!"
    erik @ e_b f_happy m_laugh "See you later!"
    hide erik
    with dissolve
    return


label ano01_outro.rails:
    scene school_french at stage
    show anon a_pocket with dissolve.nowait
    anon @ -m_talk "( Class is over, time to get out of here! )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
