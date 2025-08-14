label jen26_intro:
    scene cinema_desk
    show zana o_right
    show cinema_desk desk as desk
    pause
    show anon a_pocket f_surprised o_right at pos(.1)
    with dissolve
    anon @ -m_talk "( I was right, there he is! )"
    anon @ -m_talk "( That's the guy who was spying on [saga.cast.jenny] in the backyard! )"
    show anon f_sceptical o_left at pos(.825)
    anon "Hey, excuse me!"
    zana "Hey man, how can I help-"
    zana f_worried_surprised m_talk "Oh, shit..."
    zana a_point f_worried -m_talk "L-look man, it's not what you think, I swear!"
    show zana a_side
    anon "You're the guy who's been spying on [saga.cast.jenny]!"
    zana "Spying?!"
    zana "N-no, I wasn't-"
    pause
    zana "O-oh."
    zana "I suppose it probably looked like that, huh?"
    anon "You're saying, you weren't spying on her?"
    show anon f_worried
    zana f_calm "I just really want her autograph!"
    anon @ -m_talk "..."
    zana "Could you introduce me?!"
    anon "Yeah, I don't think so..."
    zana "Huh?"
    zana "Why not?"
    anon f_sceptical "You were hiding in our bushes... With binoculars!!"
    zana f_worried "Yeah, I'll admit that looks bad... I wasn't spying though!"
    zana "I was just waiting for the opportune moment..."
    anon "Opportune moment, for what?!"
    zana f_calm "To ask your girlfriend for an autograph!"
    zana "Man, how are you not getting this?!"
    anon @ -m_talk "..."
    anon "How did you even find our house?!"
    zana "Oh, she came in here a few weeks ago and I kinda... Sorta, followed her home."
    anon f_worried "That's just-"
    anon "Dude, you have to stop..."
    show anon f_sceptical
    zana f_worried "What?!"
    zana "W-why?!"
    anon f_worried "You know what you're doing is illegal, right?"
    anon "I can't just let you continue stalking [saga.cast.jenny]!"
    zana "Illegal?!"
    anon "It's criminal harassment at the very least..."
    zana "Y-you don't have to-"
    zana "I mean, I didn't-"
    anon "Look, I'm not going to call the police... I just want you to stop, okay?"
    zana "I'm really sorry!"
    zana "I wasn't trying to be creepy, I just really wanted her autograph..."
    pause
    zana "A-and maybe a hug?"
    anon f_sceptical @ -m_talk "..."
    anon "That's not happening."
    zana "Aww..."
    pause
    zana f_calm "Oh, I know!"
    zana "What if I give you guys free tickets to a movie?!"
    zana "You know, as an apology?"
    anon f_worried "You're not going to harass us, are you?"
    zana "N-no, I'll be cool."
    zana "I promise."
    anon f_sceptical "Alright, I guess a free movie would be nice..."
    zana a_tickets "Awesome!"
    show anon e_sw f_confused
    zana "You won't regret it!"
    show zana a_side
    show anon a_tickets f_calm
    pause
    show anon a_pocket e_w
    zana "Thanks for being so chill about all this!"
    anon f_sceptical "Uh huh."
    anon "Just remember, no more stalking..."
    zana "You got it!"
    hide anon with dissolve
    return


label jen26_jenny(when):
    if saga.cast.jenny in saga.sets.debbie_dining:
        call shot.debbie_dining_breakfast
        show jenny a_phone e_s p_table behind table
        pause
        show debbie_dining_table -chair3 -chair4 -table_legs
        show anon a_pocket e_wsw p_stand_far behind jenny at pos(.7)
        show debbie_dining_table chair3 chair4 table_legs as chairs behind jenny
        with dissolve.nowait

    elif saga.cast.jenny in saga.sets.debbie_yard:
        call shot.debbie_yard_jenny
        show anon a_pocket at right with dissolve.nowait
    else:

        call shot.debbie_bed2_jenny

        if saga.cast.jenny.womb.post:
            show jenny a_baby q_baby

        show anon a_pocket o_right at left with dissolve.nowait

    anon "Hey, you should get dressed."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        hide chairs
        show debbie_dining_table chair3 chair4 table_legs
        show anon a_down e_e p_table at center
        show jenny e_w

    jenny f_confused "Get dressed?!"
    jenny f_snide "You usually want me to take clothes off, not put them on..."
    anon @ e_b f_happy m_laugh "Hah, yeah I know but I have a surprise for you."
    jenny f_sad "Huh?"
    anon "I found that guy who's been spying on you."

    if not saga.cast.jenny.womb.post:
        show jenny a_fold

    jenny "Really?"
    anon "Yeah, he apologized and offered us free movie tickets!"
    jenny f_surprised @ -m_talk "..."
    jenny "You want me to see a movie... with you?"
    show jenny f_sad
    anon "Yeah?"
    jenny "In public..."
    anon f_worried "Yes?!"
    jenny @ -m_talk "..."
    jenny f_annoyed "{i}*Sigh*{/i} Do we have to?"
    anon f_calm "C'mon, it'll be nice!"
    show anon a_tickets
    pause
    show jenny e_wsw
    pause
    show jenny e_w

    if when == 0:
        jenny "Umm, those are for tonight, you moron!"
    elif when == 1:
        jenny "Umm, those are for tomorrow night, you moron!"
    else:
        jenny "Umm, those are for [saga.time.dow + when] night, you moron!"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon e_ese f_surprised
    else:
        show anon e_sw f_surprised

    anon "They are?!"
    anon f_worried "... Oh."
    pause

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon a_down e_e f_shy
    else:
        show anon a_pocket e_w f_shy

    anon "So, you wanna go then?"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_spoon
    elif not saga.cast.jenny.womb.post:
        show jenny a_side

    jenny e_r "Ugh, fine."
    jenny e_w "But I'm picking the movie!"
    anon "Okay."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_fold
    elif not saga.cast.jenny.womb.post:
        show jenny a_point

    jenny "And I want popcorn!"
    anon f_surprised @ -m_talk "..."
    jenny "And gummy worms!"
    anon f_sceptical "Okay, sheesh!"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show debbie_dining_table pull3

    hide anon
    with dissolve
    return


label jen26_pause:
    return


label jen26_pause.jenny(when):
    if when == 1:
        anon f_confused "We're still on for our movie date tomorrow evening, right?"
    else:
        anon f_confused "We're still on for our movie date [saga.time.dow + when] evening, right?"

    jenny e_w f_disgusted "Eww, don't call it a date!"
    anon f_worried "Umm, okay."
    pause
    anon f_confused "Why?"
    jenny "Because it's gross!"
    jenny f_annoyed "This is just one roommate bribing another into seeing a free movie together with the promise of popcorn and gummy worms."
    anon f_pouty "Yeah, yeah... you'll get your snacks."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_point

    jenny "And I want a blueberry slushy too!"
    anon "Fine!"
    anon "Just don't forget about it."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_fold

    return


label jen26_delay:
    scene camera at stage
    show anon f_happy with dissolve
    anon @ -m_talk "( Oh, it's almost time for my date with [saga.cast.jenny]. )"
    anon e_b m_teeth @ -m_talk "( I'd best go and get her! )"
    hide anon with dissolve
    return


label jen26_delay.jenny:
    anon f_happy "Don't forget about our movie date tonight, yeah?"
    jenny e_w f_disgusted "Ugh, can't you find someone else to go?"
    anon f_sceptical "What- No!"
    jenny f_annoyed @ f_angry m_teeth "Grr!"
    anon f_shy "C'mon, [saga.cast.jenny]... it'll be fun."
    anon "We used to go see lots of movies together!"
    jenny @ e_r "Yeah, cartoon movies when we were little kids."
    anon "So then let's go see a cartoon movie and it'll be nostalgic."
    jenny "I'm picking the movie, [saga.cast.anon]!"
    anon f_pouty "Yeah, yeah... and I gotta buy you popcorn and gummy worms and probably a million other things..."
    anon f_calm "... Just be ready to go this evening when it's time."
    return


label jen26_landing:
    return


label jen26_landing.rails:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( No doubt [saga.cast.jenny] will give me shit if I'm late. )"
    anon @ -m_talk "( I should hurry! )"
    hide anon with dissolve
    return


label jen26_bed2:
    scene debbie_bed2 at stage
    show anon f_confused o_right at left with dissolve
    anon "[saga.cast.jenny]?"
    show anon at right
    pause
    anon o_left "Umm?"
    anon a_wtf "Where the heck is she?!"
    hide anon with dissolve
    return


label jen26_bed2.rails:
    scene camera at stage
    show anon f_happy with dissolve
    anon @ -m_talk "( Oh, it's almost time for my date with [saga.cast.jenny]. )"
    anon @ -m_talk "( I hope she's ready! )"
    hide anon with dissolve
    return


label jen26_bath:
    scene debbie_bath_mirror base
    show debbie_bath_mirror -base as wall
    show jenny a_mascara_apply e_o p_debbie_bath_mirror_away
    show mimic jenny p_debbie_bath_mirror behind wall at pos.jenny
    pause
    show jenny e_c f_annoyed
    pause
    jenny a_mascara "What?"
    anon "You're putting on make-up."
    jenny "Yeah, so?"
    anon "So you're excited for our date!"
    jenny "What?!"
    jenny "No, I'm not!"
    anon "Hah, you totally are!"
    jenny "We're going out in public, of course I'm putting make-up on!"
    show jenny a_mascara_apply e_o f_calm
    anon "..."

    scene debbie_bath at stage
    show jenny a_hips f_snide at right
    show anon f_confused o_right at left
    with fade
    jenny "See, it has nothing to do with you."
    anon "Okay, but you didn't put make-up on when we went to pick up your sex toys."
    jenny a_fold f_annoyed "That's not-"
    anon f_snide "Just admit you're excited!"
    jenny a_upset f_angry m_teeth "Shut up!!"
    anon @ e_b f_happy m_laugh "Hehehe!"
    show jenny a_side
    anon a_wtf e_s f_smug "Should I change?!"
    anon e_w "If you're gonna dress up then I should probably-"
    show anon f_worried_surprised
    jenny a_upset "Shut up, shut up, shut up!!"
    show anon a_side
    jenny a_side f_annoyed -m_teeth "God, you are so annoying sometimes, I swear!"
    hide jenny with dissolve.nowait
    show anon o_left
    jenny "Besides, everyone knows you only own one outfit, you moron!"
    anon a_surprised f_angry @ f_shocked m_open "..."
    anon a_fold "Hey, that's not true!"
    pause
    anon e_sw f_pensive "I own lots of outfits..."
    pause
    anon "... Probably."
    hide anon with dissolve

    scene debbie_landing at stage
    show jenny c_casual f_annoyed o_right at left
    with fade
    show anon at right with dissolve
    jenny "Alright, I'm ready."
    anon "Come on then."
    jenny f_snide "After you, ladies first."
    show anon f_grumpy
    pause
    hide anon with dissolve
    hide jenny with dissolve
    return


label jen26_bath.fence:
    scene camera at stage
    show anon f_worried o_right with dissolve
    anon @ -m_talk "( It's nearly time for our movie date. )"
    anon @ -m_talk "( I should find [saga.cast.jenny]! )"
    hide anon with dissolve
    return


label jen26_cinema:
    scene cinema_desk
    show cinema_desk desk as desk
    with None
    show anon a_pocket e_e at pos(.575)
    show jenny a_fold c_casual at right
    with dissolve
    jenny "How about {i}Bitch Perfect{/i}?!"
    anon f_sceptical "A chick flick, seriously?"
    jenny "Hey, you agreed to let me choose, remember?!"
    anon f_worried "Yeah, but why do you insist on torturing me?"
    jenny f_snide "C'mon, [saga.cast.anon]... it's got tons of hot guys!"
    jenny "You'll love it!"
    anon f_sceptical "Eugh..."
    jenny e_b f_calm m_laugh @ -m_talk "Hahahaah!"
    show anon e_w f_calm
    show zana o_right at left
    with dissolve.nowait
    zana "Whoa, you really brought her!"
    jenny e_w f_surprised -m_laugh "What the actual fuck?!"
    show anon e_e f_surprised
    jenny f_angry m_teeth "You're that prick who's been spying on me!"
    show anon e_w
    zana a_stop f_worried "Look, I-"
    show anon e_e
    jenny "You're dead!"
    show anon e_w
    zana "P-please, no!"
    zana "I wasn't spying, I was-"
    anon e_e f_worried "He's just trying to get your autograph..."
    show anon e_w
    jenny f_confused -m_teeth "My autograph?"
    zana "Y-yeah, I'm like, your biggest fan!"
    jenny f_annoyed @ -m_talk "..."
    zana "That video of you in the cheerleader outfit..."
    show jenny f_disgusted
    zana @ f_calm "Oh man, it's so hot!"
    show anon e_e
    jenny f_annoyed "Is this why you brought me here?"
    anon "No, he seriously said he would stop."
    show anon e_w
    zana "I'm really sorry if I freaked you out, I wasn't trying to be creepy..."
    zana "Your boyfriend set me straight, and I promise I won't come to your house anymore!"
    jenny f_disgusted @ -m_talk "..."
    zana "A-and you guys can see anything you want, it's on the house."
    jenny f_angry_pouty @ -m_talk "Hmmph!"
    anon f_calm "There we go, finally!"
    anon e_e "See, I took care of things."
    anon "He's sorry and it won't ever happen again."
    show anon e_w
    zana "N-no, it won't happen again!"
    zana "I promise."
    pause
    jenny @ -m_talk "..."
    zana f_calm "B-but do you think I could get you to sign my {i}Blue Ninja Lollipop Girl{/i} body pillow?!"
    show jenny f_disgusted
    anon a_facepalm f_shy @ e_b f_smug "Dude..."
    zana f_worried "N-no?"
    show anon a_side
    pause
    zana "M-maybe this then?"
    show zana a_pants e_b f_hurt m_teeth
    show jenny e_sw f_surprised
    anon a_surprised e_sw f_surprised "!!!"
    show zana e_w f_surprised m_blow
    pause
    show jenny e_w f_disgusted
    show zana a_picture f_calm -m_blow
    anon a_side e_w f_worried "Please, tell me you didn't just pull that out of your underwear..."
    anon e_e "We should probably go."
    jenny f_angry m_teeth "No, it's alright..."
    jenny "I'll sign something for him."
    show anon e_w
    zana "You will?!"
    zana "I knew this was a good idea!"
    show anon e_e
    jenny "I'm gonna sign your face!"
    show anon e_w
    zana "M-my face?"
    hide jenny
    show zana b_jenny p_punched q_womb_jenny
    anon f_shocked m_open @ -m_talk "!!!" with hpunch
    show jenny a_upset c_casual f_snide at right
    show anon f_surprised m_teeth
    zana a_cover f_worried of_blood p_stand -b_jenny "What the hell?!"
    show jenny a_side
    zana "Ow!"
    jenny "How's that signature, asshole?!"
    zana "W-why?!"
    show anon e_e f_worried -m_teeth
    jenny f_annoyed "'Cause you're a creep, that's why!"
    jenny "I'd better not ever see your face again or you're getting way worse!"
    jenny "You hear me?!"
    show anon e_w
    zana "Y-yes, ma'am."
    show jenny f_snide
    anon @ -m_talk "..."
    show anon e_e
    jenny "C'mon, [saga.cast.anon]!"
    hide jenny with dissolve
    jenny "I don't wanna miss the trailers and you still have to buy my snacks."
    anon e_w f_tired "Saw that coming..."
    zana "M-my nose..."
    anon f_worried "I err..."
    pause
    show anon a_pocket e_s f_calm at right
    pause
    anon a_tickets e_w f_shy "Thanks again, for the tickets!"
    hide anon with dissolve
    zana "Gaahh!!"

    scene mono cinema_movie1
    mono "As we made our way into the screen the trailers were already in full swing, and I began to sit down in the first available seats to watch." with fade

    scene mono cinema_movie2 with dissolve
    mono "As with everything else however, this wasn't good enough for [saga.cast.jenny], who made no secret of the fact and dragged me down the row to her {i}perfect{/i} seats."

    scene mono cinema_movie3
    mono "We finally settled in as the movie announcer gave us the familiar spiel about putting our phones on silent and not talking." with fade

    scene mall_cinema_movie_bitch
    with fade
    "I want to help, I surely do...\nYour member's hard, and swollen, and blue."
    "It causes you pain and it makes you hurt...\nAnd as your wife, I should help you to squirt!"
    "But alas, my head, once more it aches...\nSo tonight, I beg you, hit the brakes."
    "Perhaps tomorrow I'll throw you a bone...\nBut for tonight, dear husband, you're on your own."

    scene mall_cinema_movie_bitch frame2 with fade
    "Yes, he's finally dead and not a moment too soon...\nI wouldn't have lasted much longer, with that wrinkly buffoon!"
    "It took months of my life, and all of my patience...\nBut I weathered the storm and I've earned my vacation!"
    "Hah! Of course it's all mine and I'll see it gets spent...\nRight after I'm done with this blessed event!"
    "I'll head down tomorrow, in my brand new car...\nYou should meet me for shopping and drinks at the bar."

    scene mall_cinema_movie_bitch frame3 with fade
    "We made it Fru Fru, to the top of the ladder...\nThe old codgers dead and I couldn't be gladder."
    "We have all his money, stashed away in our trunk...\nAs we drive down the coastline in search of a hunk."
    "Someone young and tan, with muscles well cut...\nTo carry our baggage and worship my butt."
    "And hopefully I find one who's well endowed...\nIt's been over a year and I need to get ploughed!"

    label jen26_cinema.cookie hide:
    scene mall_cinema_seats
    show jenny c_casual p_couch_sit_bored
    show anon e_one p_couch_front
    with fade
    jenny "..."
    anon @ -m_talk "..."
    jenny e_c f_elated p_couch_sit "This is boring!"
    anon a_surprised e_e f_worried m_teeth @ -m_talk "!!!"
    anon a_side f_shy -m_teeth "Shh, you're not supposed to talk during the movie [saga.cast.jenny]!"
    jenny e_w f_calm "Oh my god, you are so lame..."
    show anon e_s f_disgusted
    jenny e_b f_happy m_laugh @ -m_talk "Hahahaah!"
    show jenny e_w f_calm -m_laugh
    anon e_e f_shy "You're the one who picked this crappy movie... remember?"
    jenny "Yeah, well..."
    jenny e_c f_elated "I was expecting something sexier!"
    jenny "This is just, a bunch of losers whining about their feelings!"
    anon "Yeah, exactly like the first one."
    jenny e_r f_annoyed m_talk "..."
    jenny e_s f_sad -m_talk "... And my stomach hurts."
    anon e_one f_calm "That's because you wolfed down all that candy I bought you!"
    jenny a_fold e_r f_annoyed m_talk "Ugh, I did not \"wolf\" it down..."
    show jenny e_c -m_talk
    anon "It's all gone, isn't it?"
    jenny @ e_w f_pouty "... Yes."
    show jenny e_s f_sad
    anon "Uh huh."
    pause
    show jenny e_w f_calm
    pause
    show anon a_none e_e f_surprised
    show mimic jenny at pos.jenny
    jenny a_grab z_b_ob_f_of "Give me your hand."
    anon "What are you-"
    show jenny a_crotch e_s
    anon f_worried m_teeth @ -m_talk "!!!"
    show jenny e_w
    anon f_shy -m_teeth "W-we can't-"
    anon "We're in a movie theater!"
    show anon f_worried m_teeth
    jenny "So?"
    anon f_shy -m_teeth "So there's people around!"
    show anon f_worried m_teeth
    jenny e_r f_annoyed m_talk "I don't care, I'm horny and this movie fucking sucks."
    show jenny e_w f_calm -m_talk
    anon f_shy -m_teeth "B-but what if somebody see-"
    show anon f_worried m_teeth
    jenny "Don't be a chicken!"
    pause
    jenny "Can't you feel how wet I am?"
    anon @ -m_talk "{i}*Gulp*{/i}"
    show anon f_surprised -m_teeth
    pause
    jenny e_s "See if you can make me cum."
    hide mimic
    show jenny a_side z_reset
    anon a_touch_jenny_01 f_shy q_womb_jenny "R-really?"
    show anon e_se f_surprised
    jenny "Yes!"
    show anon e_s f_disgusted
    pause
    show anon a_touch_jenny
    pause
    jenny e_r f_annoyed m_talk "C'mon, faster doofus!"
    show jenny e_b f_shy
    pause
    jenny f_distressed m_lip @ -m_talk "Mmm."
    show anon e_e f_worried m_teeth
    jenny f_shy m_talk "Yeah, right there."
    show jenny f_distressed m_lip
    pause
    jenny f_shy m_talk "Deeper, [saga.cast.anon]!"
    show jenny f_distressed m_lip
    pause
    anon f_surprised -m_teeth "I can't believe we're doing this..."
    jenny e_w f_calm -m_lip "Shut up and focus!"
    show anon f_worried m_teeth
    jenny e_b f_shy m_talk "I'm nearly there."
    show jenny f_distressed m_lip
    pause
    jenny m_talk "NGGHHH!!!" with flash
    show anon a_touch_jenny_01
    show jenny m_lip
    pause
    show anon a_fingers_wet e_s f_disgusted m_talk
    jenny e_c f_elated -m_lip "Phew, I needed that!"
    anon "Uh huh..."
    show anon e_e f_worried m_teeth
    show jenny e_w f_calm
    pause
    jenny e_b f_happy m_laugh @ -m_talk "Pfft, hahaha!"
    anon e_s f_disgusted -m_teeth @ -m_talk "..."
    jenny e_w f_calm -m_laugh "You should probably go get some paper towels or something..."
    anon "You think?"
    jenny e_c @ e_b f_happy m_laugh "Hehehehe!"
    anon e_e f_surprised "I can't believe-"
    anon "You're crazy, you know that?"
    show anon a_uneasy e_s f_disgusted
    jenny "Shh!"
    jenny "People are trying to watch the movie, [saga.cast.anon]!"
    anon a_side "Ugh..."
    jenny e_b f_happy m_laugh @ -m_talk "Hehehe!"
    $ renpy.end_replay()

    scene black
    with dissolve
    mono ""

    scene debbie_lobby at stage
    show anon a_pocket f_worried o_right at left
    show jenny a_fold c_casual at right
    anon "Why did I agree to let you pick the movie?!"
    jenny "Yeah, that movie was pretty terrible."
    jenny f_snide "We still had fun though, didn't we?"
    anon "Well, {i}you{/i} had fun..."
    jenny e_b f_calm m_laugh @ -m_talk "Hahahaah!"
    show jenny e_w f_snide -m_laugh
    anon f_tired "Are you done? I'm exhausted."
    jenny f_calm "Really?"
    jenny "I'm kinda amped up, after everything that happened!"
    anon f_worried "You didn't have to punch him, you know..."
    jenny f_annoyed "Pfft, he had it coming!"
    anon "You could have let me handle it."
    jenny e_r "I can take care of myself, [saga.cast.anon]!"
    show jenny e_w
    anon e_b f_happy m_laugh @ -m_talk "Yeah, tell me about it..."
    anon @ -m_talk "That poor guy is probably still seeing stars!"
    show anon e_w f_calm -m_laugh
    jenny e_b f_calm m_laugh @ -m_talk "Hahahaah!"
    show jenny e_w f_snide -m_laugh
    anon @ e_b f_happy m_laugh "Hehe!"
    jenny "I'm really glad you tracked that prick down."
    jenny "Thanks, [saga.cast.anon]!"
    anon "Well, I couldn't just let him keep harassing you."
    show anon f_tired
    jenny f_horny "..."
    anon "Anyways, I'm going to bed..."
    jenny f_sad "What?!"
    anon "I'm exhausted."
    jenny f_annoyed "You're seriously going to bed, right now?"
    anon "Hmm?"
    anon "You have something else in mind?"
    jenny f_sad "N-no, not really..."
    anon "I'll see you tomorrow then."
    anon "Good night, [saga.cast.jenny]."
    hide anon with dissolve
    pause
    jenny f_snide @ -m_talk "..."
    jenny "Good night."
    hide jenny with dissolve
    return


label jen26_cinema.rails:
    scene camera at stage
    show anon a_pocket f_happy o_right at right with dissolve
    show jenny f_annoyed o_right at left with dissolve.nowait
    jenny "Hurry up, dummy, I don't wanna get stuck with shitty seats at the movie theater!"
    anon f_worried o_left "Alright, I'm coming!"
    hide jenny with dissolve.nowait
    anon "Sheesh."
    hide anon with dissolve
    return


label jen26_outro:
    call shot.debbie_bed3_sleep
    with fade
    pause
    show debbie_bed3_visit -bed -computer -door
    show jenny e_ose f_snide p_bed3_peek q_tod behind anon
    show debbie_bed3_visit ajar bed computer door as computer behind anon
    with dissolve
    jenny @ -m_talk "Psst!"
    jenny "[saga.cast.anon], you awake?"
    anon @ -m_talk "Mmm."
    pause

    scene debbie_bed3_side -blanket
    show anon c_pants e_b p_bed3_visit at tint('00106545')
    show debbie_bed3_side blanket pulled as blanket
    with fade
    show jenny a_down e_wsw p_visit at tint('00106545') with dissolve
    jenny "[saga.cast.anon]?"
    anon @ -m_talk "Nnnhhh."
    pause
    jenny "C'mon, wake up."
    anon @ -m_talk "NNNHHH!"
    show jenny a_reach e_sw
    anon e_ne f_surprised "Damn it, [saga.cast.jenny]..."
    anon "It's the middle of the night!"
    show anon c_pants_down f_tired p_bed3_visit_sit
    jenny a_anon_pants_down_01 "Oh, shut up."
    show anon d_rise
    show jenny a_up
    pause
    show jenny a_stroke
    anon d_none "What are you doing, [saga.cast.jenny]?"
    anon "I'm trying to slee-"
    jenny "What does it look like I'm doing?!"
    show jenny p_visit_top_off
    show anon d_hard f_surprised
    pause
    show jenny c_pants p_visit_bottom_off
    anon f_tired "We really have to do this, right now?!"
    show anon d_none
    jenny c_naked p_visit_mount "Yes, I'm fucking horny and I want it right now!"

    scene debbie_bed3_pov
    show jenny b_anon c_naked p_debbie_bed3_ride_mount
    with fade
    anon "!!!"
    anon "Damn it [saga.cast.jenny], I'm tired..."
    jenny "Oh, for fuck's sake... All you have to do is lay there!"
    jenny "I'm the one doing all the work!"
    jenny p_debbie_bed3_ride_anim_01 "{i}*Gasp*{/i}"
    jenny "God, I love your dick!"
    label jen26_outro.reuse:
    jenny p_debbie_bed3_ride_anim s_8 "Ahh!"
    pause
    anon "Okay, that feels really good..."

    if saga.cast.jenny < 'visit':
        jenny "See, and you were all whining about it!"
        anon "Well, we could have done this tomorrow!"
        jenny "Yeah, and we probably will..."
        anon "R-really?"
        jenny "Uhh, yeah... camshows, dummy."
        anon "Oh, right."
        jenny "Now shut up and let me enjoy this!"
    else:

        jenny "Ahh!"
        pause
        anon "Okay, that feels really good..."
        jenny "Yeah, it does!"

    pause
    jenny "Ahh, fuuuuck!"
    pause
    jenny "Mmm, I'm gonna cum all over that big dick of yours, [saga.cast.anon]!"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        anon "Then do it!"
        jenny s_12 "Ahh, shit!"
        anon "Tell me you want it!"
        jenny "Mmm, I want it!"
        pause
        anon "C'mon [saga.cast.jenny], faster!"
        jenny "Oh my god!"
        pause

        if saga.cast.jenny < 'visit':
            jenny "Ahh, fuck me!!"
        else:

            anon "Beg me to give it to you!"
            jenny "Ahh!"
            jenny "Please!!"
            pause
            anon "C'mon, you can do better!"
            jenny "Fuuuuck!"
            jenny "Please, [saga.cast.anon]!!"
            jenny "Give it to me!!!"
    else:

        jenny "You'd like that, wouldn't you?!"
        anon "Y-yes."
        jenny s_12 "Ahh!"
        jenny "C'mon, say it!"
        jenny "Say you want me to cum on your big dick!"
        anon "I want you to cum on my big dick!"

        if saga.cast.jenny > 'visit':
            jenny "I think you can do better..."
            pause
            jenny "Tell me I'm a sex goddess!"
            anon "Y-you're a sex goddess!"
            jenny "Come on, bitch!"
            jenny "I can't hear you!"
            anon "You're a sex goddess!!!"
            jenny "You worship this pussy, don't you?!"
            anon "Y-yes!"

        jenny "Hahahaah!!"

    anon "Shh!"
    anon "You're gonna wake up [saga.cast.debbie]..."
    jenny "I don't fucking care!"
    pause
    jenny "Ahh, I'm so close!"
    jump jen26_outro.loop


label jen26_outro.dialogue(opt, rng=-1):
    if opt == 1:
        jenny "Ahh, fuuuuck!"
    elif opt == 2:
        jenny "Fuuuuck!"
    elif opt == 3:
        jenny "Hahahaah!!"
    elif opt == 4:
        anon "Oh my god!"
    elif opt == 5:
        jenny "Ahh, fuck me!!"
    elif opt == 6:
        anon "I'm getting close..."

    return


label jen26_outro.inside:
    jenny "Oh my god, oh my god, OH MY GOD!"
    pause
    jenny "I'm cumming! I'm cumming!"
    anon "Me too!"
    jenny "AAAHHH, FUCK!!!"

    if not saga.cast.jenny.womb:
        anon "[saga.cast.jenny], get off!"

    jenny "NGGHHH!!!"
    anon "Ah, crap!"
    show jenny p_debbie_bed3_ride_cum s_400ms
    anon "HNNGGG!!!" with flash
    show jenny p_debbie_bed3_ride_anim_02
    pause
    show jenny p_debbie_bed3_ride_unmount

    call mini.womb (saga.cast.jenny)

    anon "Haah... Haah..."
    jenny e_s f_angry od_cum p_debbie_bed3_ride "Oh my god..."
    pause
    jenny e_ssw "Did you cum in me?!"

    if saga.cast.jenny.womb:
        anon "Uhh, yeah?"
    else:
        anon "I told you to get off me!"

    jenny "Goddamnit, [saga.cast.anon]!"
    anon "What?!"

    if saga.cast.jenny.womb:
        anon "It's not like you can get {i}more{/i} pregnant."
        jenny "Yah, but now I have to clean myself up or sleep with you oozing out of me all night!"
        anon "I can get you a towel if you'd like?"
    else:

        jenny "I could get pregnant you moron!"
        anon "Well, I'm sorry but I did warn you..."

    jenny "Ugh, whatever."
    show jenny e_s
    pause
    jenny e_ssw f_calm "{i}*Sigh*{/i} Fuck it..."
    jenny "Heh, my legs are shaking like crazy!"
    jump jen26_outro.post


label jen26_outro.loop:
    menu(screen='lewd', tag='jenny'):
        "Keep Going":
            pass
        "Cum Inside":

            jump jen26_outro.inside
        "Cum Outside":

            jump jen26_outro.outside

    $ renpy.dynamic(pool=saga.lewd.pool(6, max=3))

    while pool:
        call jen26_outro.dialogue (pool.pop(), rng=renpy.random.random()) from jen26_outro.pool

    jump jen26_outro.loop


label jen26_outro.outside:
    jenny "Oh my god, oh my god, OH MY GOD!"
    pause
    jenny "I'm cumming! I'm cumming!"
    jenny "NGGHHH!!!"
    pause
    anon "Me too!"
    show jenny od_cumshot p_debbie_bed3_ride_cumshot s_400ms
    anon "HNNGGG!!!" with flash
    pause
    show jenny e_ssw od_cumshot_02 p_debbie_bed3_ride
    anon "Haah... Haah..."
    jenny "Phew, that was awesome..."
    pause
    jenny "Hahaha, you're a fucking mess!"
    anon "Heh, I don't even care... I'm so exhausted."
    jenny "{i}*Snort*{/i} Hehehe!"
    jenny "You should clean yourself up, you look ridiculous..."
    jump jen26_outro.post


label jen26_outro.post:
    $ renpy.end_replay()

    if saga.cast.jenny < 'visit':
        anon "You staying?"
    else:
        anon "You leaving again?"

    jenny @ -m_talk "Hmm?"

    if saga.cast.jenny < 'visit':
        anon "Do you wanna sleep here with me tonight?"
        jenny f_angry "Eww, no!"
        jenny "I'm not your fucking girlfriend, doofus..."
    else:

        anon "You can sleep here, you know?"
        jenny f_angry "For fuck's sake..."
        jenny "Didn't we go over this already?"

    call shot.debbie_bed3_bedside
    show debbie_bed3 sleep -anon -jenny
    show jenny c_naked f_annoyed at pos(.35)
    with fade
    show anon c_pants f_sceptical at right with dissolve

    if saga.cast.jenny < 'visit':
        anon "Wait!"
    else:
        anon "Alright, fine... Whatever."

    show anon f_worried

    if saga.cast.jenny < 'visit':
        jenny a_fold o_right "What, [saga.cast.anon]?!"
        anon "I wasn't trying to-"
        anon "{i}*Sigh*{/i} Just, explain this to me..."
        anon @ f_sceptical "So, we can have sex whenever we want but you won't sleep in my bed?"
        jenny e_r "Umm, no. We can have sex whenever {i}I{/i} want..."
        jenny e_w "... So long as it doesn't interfere with my camshows."
        pause
        jenny "... And no, I won't sleep in your bed!"
        jenny "I'm not your fucking girlfriend, and you're sure as hell not my boyfriend!!!"
        jenny "Get that through your thick skull, dummy!"
        anon @ f_confused "I don't get you at all..."
        jenny "Yeah, well you don't have to {i}get{/i} me."
        jenny "That's just the way things are."
        jenny "Deal with it."
        anon @ -m_talk "..."
    else:

        show jenny a_fold o_right
        anon f_sceptical "Just forget I said anything."
        jenny "Gladly."
        pause

    jenny "Now go to sleep!"

    if saga.cast.jenny.womb.normal or saga.cast.jenny > 'cam.belly' and saga.cast.jenny.womb.belly:
        jenny f_snide "My fans are expecting a good show tomorrow."

    hide jenny with dissolve
    pause
    anon f_worried @ -m_talk "..."
    hide anon with dissolve
    return True


label jen26_outro.rails:
    scene debbie_bed3 at stage
    show anon f_tired o_right with dissolve
    anon @ -m_talk "( Nah, if I do that it'll turn into a whole thing and I'm too tired right now. )"
    anon @ -m_talk "( Let's just go to bed, eh? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
