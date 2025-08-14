label bar04_barb1:
    anon f_confused "So, what's next for our art lessons, [saga.cast.barb]?"
    barb "I've got exciting news on that front, actually!"
    barb "I met the nicest lady in the mall last night and we got to talking..."
    barb f_horny "... It turns out, she had done a bit of nude modeling in the past..."
    barb a_hip "... And with a bit coaxing, I was able to convince her to model for our next lesson!"
    anon a_surprised f_surprised "W-wait, really?!"
    barb "Isn't that awesome, [saga.cast.anon]?!"
    anon a_shy_neck "S-she's gonna pose..."
    anon "... N-nude?"
    barb a_hips f_calm "We'll finally be doing real art!"
    anon a_side @ -m_talk "{i}*Gulp*{/i}"

    if saga.cast.barb in saga.sets.school_art:
        barb a_side f_sad "These old easels just won't do though..."
    else:
        barb a_side f_sad "Those old easels in the art room just won't do though..."

    barb "... It's such a shame I can't afford to get us new ones."
    anon "L-like, totally and completely nude?"
    barb @ f_calm -m_talk "Mhmm."
    barb "I just worry that the art will suffer on those old broken down easels..."
    barb "... Maybe I should just figure out some other lesson for us to do."
    anon a_up f_afraid "NO!"
    anon a_uneasy f_shy "I mean, don't do that... I can make some new easels for us."
    barb f_confused "Really?"
    anon f_calm "Sure."
    show barb f_calm
    anon a_side f_confused "It's just wood and nails, right?"
    anon "How hard could it be."
    show anon e_b f_happy m_teeth
    barb "Oh, you're amazing, [saga.cast.anon]!!"
    hide anon
    hide barb

    if saga.cast.anon in saga.sets.school_art:
        show old_barb 21 at face_right, pos(.55)
    else:
        show old_barb 21 at face_left, pos(.45)

    with dissolve.nowait
    barb "Just the most delicious young man I've ever met!"
    show old_barb 20
    pause
    hide old_barb

    if saga.cast.anon in saga.sets.school_art:
        show barb o_right
        show anon a_surprised f_shy of_blush at right
    else:

        show barb
        show anon a_surprised f_shy o_right of_blush at left

    with dissolve.nowait
    anon "Gee, thanks [saga.cast.barb]."
    anon a_side "Y-you're real nice too!"
    anon f_calm "I guess I should get to it then..."
    hide anon
    with dissolve.nowait
    barb a_hips "Oh, this is so exciting!"

    if saga.cast.anon in saga.sets.school_art:
        scene school_hall1w at stage with fade
    else:
        scene school_hall3 at stage with fade

    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( Hmm, it should be easy enough to build a couple easels. )"

    if saga.prop.tool_drill in saga.cast.anon:
        anon "( I already have that old drill of Dad's in my backpack... )"
    else:
        anon "( Dad's tools are at home in the garage... )"

    if saga.cast.anon in {saga.prop.misc_planks.where, saga.prop.misc_planks_x2.where}:
        anon a_side e_w f_happy @ -m_talk "( ... And I can make them out of the planks I collected from the treehouse! )"
    else:
        anon @ -m_talk "( ... And I'm pretty sure there's still some leftover planks near our old tree house. )"

    hide anon with dissolve
    return


label bar04_planks:
    call shot.meadow_main_planks
    show old_anon 585 with dissolve
    anon "These will work great!"
    show old_anon 586
    pause
    anon "( I can take these to Dad's old workbench in the garage to build some easels. )"
    hide old_anon with dissolve
    return


label bar04_planks.barb:
    anon f_shy "I can't believe we're going to paint a real life nude model!"
    barb f_happy "Heh, glad you're excited, [saga.cast.anon]."
    show anon a_side
    barb f_curious "How are those easels coming along?"
    anon a_uneasy "I'm still working on it."
    barb f_calm "Well, let me know when you've finished so I can schedule the model, okay?"
    anon a_side f_calm "Yes, ma'am."
    return


label bar04_craft:
    scene mono debbie_garage_craft3
    mono "Now, we all know I'm no master craftsman, but as I set to work that day an almost Zen-like calm came over me the likes of which I'd never previously experienced." with fade
    mono "These few pieces of dead tree and melted rock were all that stood between me and a naked woman exposing herself in my art class."
    mono "I was unstoppable, and not to toot my own horn, but those easels might have been the some of the highest quality work I've ever done, before or since."

    scene black
    with dissolve
    return


label bar04_craft.item:
    scene debbie_garage at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( A drill would make constructing these easels a lot easier. )"
    anon a_side e_w f_shy @ -m_talk "( Conveniently, Dad's old drill is just over there on the shelf... )"
    anon e_osw f_sad_happy @ -m_talk "( ... It'll be a little weird using it without him though... )"
    hide anon with dissolve
    return


label bar04_craft.late:
    jump mel01_craft.late


label bar04_barb2(when):
    show barb f_confused
    anon a_backpack e_s f_shy "Here's those easels I promised you, [saga.cast.barb]."
    show anon a_backpack_easel e_nw f_calm
    pause

    if saga.cast.anon in saga.sets.school_art:
        show anon a_handshake e_sw at pos(.8)
        show old_xtra 45c at face_right, pos(.6)
    else:

        show anon a_handshake e_sw at pos(.2)
        show old_xtra 45c at face_left, pos(.4)

    with dissolve.nowait
    barb f_happy "{i}*Gasp*{/i} Such beautiful craftsmanship, [saga.cast.anon]!"
    show old_xtra behind anon

    if saga.cast.anon in saga.sets.school_art:
        show anon a_side e_w f_shy at right
    else:
        show anon a_side e_w f_shy at left

    barb f_calm "You're truly an artist through and through."
    anon "Thanks."

    if when == 1:
        barb "I'll get on the phone and schedule our model for tomorrow afternoon."
    else:
        barb "I'll get on the phone and schedule our model for [saga.time.dow + when] afternoon."

    anon f_calm "Sweet, I can't wait!"
    hide anon with dissolve
    return


label bar04_pause1:
    return


label bar04_pause1.barb(when):
    anon f_confused "So we're really gonna have a nude model show up for our next lesson?"
    barb "You bet we are!"
    anon f_sceptical "Like, a real nude female {i}lady{/i} model?!"
    barb "Heh, that's correct!"
    show anon f_horny_smug
    barb "So don't be late, eh?"
    anon f_horny "Oh, I'll be on time..."
    anon "... Definitely not missing this!"
    return


label bar04_pause1.mia(when):
    show old_anon 2
    anon "Did [saga.cast.barb] tell you about the next lesson."
    show old_anon 1
    show old_mia 10

    if when == 1:
        mia "Yup, tomorrow afternoon."
    else:
        mia "Yup, [saga.time.dow + when] afternoon."

    show old_mia 7
    show old_anon 2
    anon "I'm so excited!"
    show old_anon 1
    return


label bar04_delay1:
    scene camera at stage
    show anon a_pocket f_happy with dissolve
    anon @ -m_talk "( It's finally time! )"
    anon e_b m_teeth @ -m_talk "( I can't believe [saga.cast.barb] is getting a nude model for us to draw! )"
    hide anon with dissolve
    return


label bar04_delay1.barb:
    anon f_confused "Do I need anything extra for our lesson this afternoon?"
    barb "You shouldn't."
    barb "Just try and be on time, we don't want to keep our model waiting."
    anon f_horny "Oh, don't worry..."
    anon a_point_pocket "... There's no way I'll be late for this!"
    barb @ e_b f_happy m_laugh "Heh, you kids are so adorable when you're excited."
    show anon a_pocket
    return


label bar04_delay1.mia:
    show old_anon 2
    anon "Can you believe we've got a nude model coming for our art lesson?!"
    show old_anon 1
    show old_mia 12
    mia "I know, I'm really nervous..."
    show old_mia 8
    show old_anon 10
    anon "What, why?!"
    show old_anon 14
    anon "It's not you that's going to be naked."
    show old_anon 13
    show old_mia 12
    mia "I know, it's just... very..."
    mia "... Umm.. I don't know..."
    show old_mia 12b
    mia "... It gives me butterflies in my tummy."
    show old_mia 8b
    show old_anon 14
    anon "Yeah, it kinda gives me butterflies too..."
    show old_anon 110
    anon "( ... Just not in my tummy. )"
    show old_anon 13
    return


label bar04_art1:
    call shot.school_art_barb
    show old_mia 8b at pos(.435)
    show old_barb 13 at old_left
    barb "... Oh, sure. I've done two at once before."
    barb "Three at once even... Well, a couple times actually."
    show old_barb 11
    show old_mia 8
    barb "Some girls really enjoy that kind of thing but I find it to be a bit too overwhelming."
    show old_barb 12
    show old_mia 12
    mia "Yeah, it sounds that way."
    show old_barb 13
    show old_mia 8
    barb "That's why I recommend going the other direction with two girls and a guy..."
    barb "... So much easier to relax and enjoy the sensations when there's only one penis involved."
    show old_mia 8b
    barb "Women tend to be much gentler too."
    show old_barb 12
    show old_mia 12b
    mia "Okay, but don't you get jealous?"
    mia "Seeing your partner with another woman?"
    show old_barb 13
    show old_mia 8b
    barb "Jealous?! Whyever would I feel jealous?"
    barb "It's just sex, dear..."
    barb "... And besides, I love to watch... It's art in motion!"
    show old_barb 12
    show old_mia 12b
    mia "Hmm, I'm not sure."
    show old_mia 8b
    show old_anon 2 at old_right
    with dissolve.nowait
    anon "Hey, ladies."
    show old_mia 8b at pos(.385), face_right
    with dissolve.nowait
    anon "Wow, [saga.cast.mia] beat me here?"
    show old_anon 1
    show old_mia 10b
    mia "Yeah, I had a few questions I wanted to ask [saga.cast.barb]."
    show old_mia 7
    show old_anon 2
    anon "Oh, yeah?"
    anon "What kind of questions?"
    show old_anon 1
    show old_barb 13
    barb "Private questions between us gals and never you mind about it!"
    show old_barb 13b
    show old_anon 10
    anon "Oh, uhh... alright, sorry."
    show old_anon 5
    show old_barb 11b
    barb "Heh, always so polite."
    show old_barb 11
    barb "He's gonna make some lucky girl a wonderful boyfriend some day, don't you think, [saga.cast.mia]?"
    show old_barb 10
    show old_mia 56 at pos(.375), face_left
    with dissolve.nowait
    mia "Oh, I-"
    mia "Umm-"
    show old_mia 55
    show old_barb 11
    barb "Now if you'll both excuse me, I need to check in on our model and see what's taking her so long to arrive!"
    hide old_barb
    show old_mia 7 at pos(.385), face_right
    show old_anon 1 at face_right
    with dissolve.nowait
    pause
    show old_anon 2 at pos(.6), face_left
    with dissolve.nowait
    anon "So, you seem to be getting along better with [saga.cast.barb]."
    show old_anon 1
    show old_mia 10
    mia "Yeah, I suppose so."
    show old_mia 10
    mia "She's a little indecent but she certainly knows her stuff!"
    show old_mia 7
    anon "Mhmm."
    show old_mia 56
    mia "It kinda makes me wish I was as free spirited as her."
    show old_mia 55
    show old_anon 2
    anon "What do you mean?"
    show old_anon 1
    show old_mia 56
    mia "Well..."
    show old_mia 8b
    show old_barb 25 at old_right
    with dissolve.nowait
    barb "Oh, this is a disaster!!"
    show old_barb 24
    show old_anon 1 behind old_mia at pos(.525), face_right
    with dissolve.nowait
    anon "Hmm?"
    show old_anon 11
    show old_mia 7
    show old_barb 23
    barb "She backed out on me!"
    show old_barb 22
    show old_mia 12
    mia "She what?!"
    show old_mia 8
    show old_anon 10
    anon "The model cancelled?"
    show old_anon 5
    show old_barb 23
    barb "Yeah!"
    barb "Apparently, some big client showed up and she couldn't tear herself away..."
    barb "... It's so unprofessional!"
    show old_barb 22
    show old_anon 10
    anon "So what now?"
    show old_anon 5
    show old_barb 25
    barb "I don't know..."
    barb "Our next lesson really requires a nude model..."
    show old_barb 24
    mia "..."
    show old_barb 25
    barb "Do you guys know anybody that would do it?"
    show old_barb 24
    show old_anon 10
    anon "... I don't think so."
    show old_anon 5
    show old_mia 10
    mia "We could ask around?"
    show old_mia 7
    show old_anon 113
    anon "Who would we even ask?"
    show old_anon 114
    show old_mia 10
    mia "... Maybe someone here at school will do it."
    show old_mia 7
    show old_anon 5
    show old_barb 25
    barb "You think maybe one of the students would do it?"
    show old_barb 24
    show old_anon 10
    anon "I doubt it."
    show old_anon 5
    show old_mia 10
    mia "Well, it wouldn't hurt to ask."
    show old_mia 7
    show old_anon 113
    anon "Yeah, I guess we could ask..."
    show old_anon 5
    show old_barb 11
    barb "Why don't you two split up and ask some of your classmates if they would be willing?"
    show old_barb 10
    show old_anon 1
    show old_mia 9
    mia "Sure thing!"
    show old_mia 7
    show old_anon 2
    anon "Alright."
    hide old_anon
    hide old_mia
    with dissolve
    return


label bar04_art1.rails:
    scene camera at stage
    show anon f_happy with dissolve
    anon @ -m_talk "( I need to get along to art class... )"
    anon e_b m_teeth @ -m_talk "( ... There's a nude model waiting to be drawn! )"
    hide anon with dissolve
    return


label bar04_judith1:
    hide anon
    hide judith
    show old_judith 1 at old_right
    show old_anon 2 at old_left
    anon "I'm working on a project for [saga.cast.barb] and it requires a live model."
    anon "Would you be interested?"
    show old_anon 1
    show old_judith 5
    judith "You want me to model for you?"
    show old_anon 2
    show old_judith 4
    anon "Yeah, that would be awesome!"
    show old_anon 10
    anon "It's nude modeling though..."
    show old_anon 11
    show old_judith 3
    judith "... Oh."
    show old_judith 1
    judith "..."
    show old_judith 3
    judith "... You really want me to?"
    show old_anon 10
    show old_judith 1
    anon "Of course!"
    show old_anon 11
    show old_judith 5
    judith "Then I'll do it! For you, [saga.cast.anon]!"
    show old_anon 2
    show old_judith 4
    anon "Thanks, [saga.cast.judith]! That's really awesome of you!"
    anon "Just meet me after art class."
    show old_anon 1
    show old_judith 5
    judith "Alright."
    show old_judith 4
    show old_anon 2
    anon "[saga.cast.barb] will let you know which day."
    hide old_anon with dissolve
    return


label bar04_judith1.annie:
    anon f_calm "I'm working on a project for [saga.cast.barb] and it requires a live model."
    anon "Would you be interested?"
    annie f_calm "Can't do it. I have rounds!"
    anon f_confused "Huh?"
    show anon f_surprised
    annie f_angry "I've gotta patrol for miscreants!"
    annie "Get outta my way!"
    anon f_sceptical "Alright, sheesh!"
    hide anon with dissolve
    return


label bar04_judith1.barb:
    anon f_confused "Heard anything from [saga.cast.mia] about finding a model?"
    barb f_sad "No. What about you, any luck?"
    anon f_worried "Not yet."
    barb "Well, make sure you ask all your classmates."
    barb e_ssw "Hopefully, somebody will be brave enough to model for us..."
    pause
    show barb e_w
    return


label bar04_judith1.dexter:
    show old_anon 10
    anon "I don't suppose you'd be interested in modeling for an art piece?"
    show old_dexter 8
    show old_anon 5
    dexter "Huh?"
    show old_anon 10
    show old_dexter 2
    anon "[saga.cast.barb] needs someone to pose for a painting."
    show old_anon 5
    dexter "..."
    show old_anon 3
    anon "..."
    show old_dexter 6
    dexter "What the heck are you saying?"
    show old_dexter 2
    show old_anon 24
    pause
    show old_anon 12
    anon "{i}*Sigh*{/i} Would.{w} You.{w} Be.{w} Willing..."
    anon "... To.{w} Stand.{w} Naked..."
    anon "... So.{w} Art.{w} Students.{w} Can.{w} Draw-"
    show old_dexter 4
    show old_anon 22
    dexter "Eww, you wanna see me naked?!"
    show old_dexter 2
    show old_anon 10
    anon "No, it's for art-"
    show old_dexter 6
    show old_anon 11
    dexter "What are you, queer or something?!"
    show old_anon 37
    show old_dexter 5
    anon "Ugh, just forget it."
    show old_dexter 4
    show old_anon 24
    dexter "Yo everybody, this nerd here just asked me to show him my junk!"
    show old_dexter 2
    show old_anon 15
    anon "You're such an asshole."
    hide old_anon
    show old_dexter 3
    with dissolve.nowait
    dexter "Aww, is the little gay nerd gonna cry?!"
    dexter "Hahahaha!"
    return


label bar04_judith1.erik:
    show old_anon 10
    anon "I'm working on a project for [saga.cast.barb] and it requires a live model."
    anon "Would you be interested?"
    show old_anon 5
    show old_erik 5
    erik "Uhh, you really think I would make a good model?"
    show old_erik 1
    show old_anon 10
    anon "Hmm, no... probably not."
    show old_anon 2
    anon "I'll look elsewhere."
    show old_anon 1
    show old_erik 4
    erik "Good luck, dude."
    show old_erik 1
    hide old_anon with dissolve
    return


label bar04_judith1.eve:
    anon f_calm "I'm working on a project for [saga.cast.barb] and it requires a live model."
    anon "Would you be interested?"
    eve "Modeling? That could be fun."
    anon "Really?! Awesome! I was hoping you would say that!"
    eve f_happy "Yeah, I don't mind."
    eve @ e_b m_laugh "It's a good thing I wore this cute outfit today."
    anon f_worried "... Oh, umm. It would be nude modeling."
    eve f_confused "Nude?!"
    eve a_fold f_surprised "Oh, hell no!"
    show eve e_ssw f_nervous
    anon "So you won't do it? I thought you were into artsy stuff?"
    eve "Yeah..."

    if saga.cast.eve in saga.sets.school_french:
        show eve e_e f_sad
    else:
        show eve e_w f_sad

    eve "... But that doesn't mean I'm into public nudity!"
    anon f_shy "Good point. Sorry."
    eve f_nervous "It's alright. Just not interested."
    anon "Well, thanks anyways..."

    if saga.cast.eve in saga.sets.school_french:
        show eve o_right ob_chair z_ob as anon_chair at pos(.15, 1.02)
        show eve o_right ob_desk z_ob as anon_desk at pos(.25, 1.02)

    hide anon with dissolve
    return


label bar04_judith1.june:
    show old_anon 2
    anon "I'm working on a project for [saga.cast.barb] and it requires a live model."
    anon "Would you be interested?"
    show old_anon 1
    show old_june 3
    june "Modeling?"
    show old_june 3b
    june "Do I look like a model to you?"
    show old_june 5
    show old_anon 10
    anon "Sure, why not?"
    show old_anon 5
    show old_june 3b
    june "Pfft, nice try."
    show old_june 3
    june "I've got other stuff planned anyways..."
    show old_june 5
    show old_anon 10
    anon "You do?"
    show old_anon 11
    show old_june 3
    june "Yeah, the expansion pack for {i}Orcette's Dungeon{/i} launched today."
    june "You better believe I'm getting a copy!"
    show old_june 5
    show old_anon 2
    anon "Alright, have fun I guess."
    show old_anon 1
    show old_june 3b
    june "Oh, I will!"
    hide old_anon with dissolve
    return


label bar04_judith1.kevin:
    show old_anon 2
    anon "I'm working on a project for [saga.cast.barb] and it requires a live model."
    anon "Would you be interested?"
    show old_anon 1
    show old_kevin 2
    kevin "Modeling. Like I just have to stand there?"
    show old_kevin 1
    show old_anon 2
    anon "Yeah, you just have to stand there."
    show old_anon 10
    anon "Naked."
    show old_anon 11
    show old_kevin 3
    kevin "Naked?!"
    kevin "Oh, man. I dunno, bro."
    kevin "Is it just gonna be you there drawing?"
    show old_kevin 1
    show old_anon 10
    anon "Well, [saga.cast.mia] and I will both be drawing."
    anon "[saga.cast.barb] will be there too."
    show old_anon 11
    show old_kevin 4
    kevin "Ugh, pass..."
    show old_kevin 3
    kevin "I don't want girls to see me naked, bro. That's kinda gross."
    show old_kevin 1
    anon "..."
    show old_anon 10
    anon "O-okay."
    hide old_anon with dissolve
    return


label bar04_judith1.mia:
    show old_anon 14
    anon "Any luck finding a replacement model?"
    show old_anon 13
    show old_mia 12b
    mia "No, not really..."
    mia "... But then, I've only asked a few people."
    show old_mia 12
    mia "Doesn't it make you feel super embarrassed, asking people to volunteer for this?"
    show old_mia 8
    show old_anon 4
    with dissolve.nowait
    pause
    show old_anon 14
    with dissolve.nowait
    anon "No, not really."
    show old_anon 2
    anon "[saga.cast.barb] told us that nudity is natural and beautiful, remember?"
    show old_anon 1
    show old_mia 12b
    mia "Y-yeah, I guess."
    show old_mia 8b
    return


label bar04_judith1.rhonda:
    anon f_shy "I'm working on a project for [saga.cast.barb] and it requires a live model."
    anon @ a_point_pocket "Would you be interested?"
    rhonda "Busy."
    anon f_worried "Busy?"
    anon "Doing what?"
    rhonda f_angry "For real, [saga.cast.anon]?!"

    if saga.cast.rhonda in saga.sets.pool_side:
        rhonda f_serious @ f_angry "I've only got 40 minutes to get some laps in before the pool closes."
    else:
        rhonda f_serious @ f_angry "I've gotta run 6 miles and hit an ice bath before soccer practice."

    anon f_surprised @ e_sw f_worried "Uhh..."

    if saga.cast.rhonda in saga.sets.pool_side:
        rhonda @ f_angry "Afterwards, I've gotta run 6 miles and hit an ice bath before soccer practice."
    else:
        rhonda @ f_angry "Afterwards, I've only got 40 minutes to get some laps in before the pool closes."

    anon m_teeth "That's cra-"
    rhonda @ f_angry "Then it's back home to a heating pad and crunches."
    anon f_worried -m_teeth "Okay, okay! I got it..."
    hide anon with dissolve
    return


label bar04_judith1.roxxy:
    show old_anon 10
    anon "I'm working on a project for [saga.cast.barb] and it requires a live model."
    anon "Would you be interested?"
    show old_anon 11
    show old_roxxy 2
    with dissolve.nowait
    roxxy "Pfft, as if!"
    roxxy "Keep dreaming, ya dweeb!"
    show old_roxxy 1
    show old_anon 16
    anon "..."
    hide old_anon with dissolve
    return


label bar04_barb3(when):
    anon f_shy "I did it, [saga.cast.barb]!"
    anon f_calm "I found us a model!"
    barb f_curious "You did?"
    anon "Yeah, [saga.cast.judith]."
    barb f_surprised "{i}*Gasp*{/i} [saga.cast.judith]?!"
    barb a_clasp f_happy "That's perfect!"
    barb "She has such a wonderful body for paint on canvas!"
    show barb a_side f_calm
    anon a_uneasy f_confused "Y-yeah, totally."

    if when == 1:
        barb "I'll set everything up for tomorrow afternoon then."
    else:
        barb "I'll set everything up for [saga.time.dow + when] afternoon then."

    anon a_side f_calm "Great, see you then!"
    hide anon with dissolve
    barb a_clasp f_happy "Oh, this is turning into the best semester ever!"
    return


label bar04_barb3.judith:
    anon f_calm "Thanks again, for volunteering to be a model, [saga.cast.judith]."
    anon "It's super cool of you!"
    judith f_surprised "Y-you think I'm cool?"
    anon a_uneasy f_shy "Well, yeah."
    judith f_happy @ -m_talk "..."
    judith a_side f_calm "It's no problem, I'm happy to do it!"
    anon a_wave f_calm "You're the best, [saga.cast.judith]. I'll see you there!"
    hide anon
    show judith of_blush
    with dissolve.nowait
    pause
    judith a_cover_face f_surprised @ -m_talk "( !!!!!!!!!!!! )"
    return


label bar04_barb3.mia:
    show old_anon 2
    anon "Great news!"
    anon "You can halt the model search."
    show old_anon 91
    show old_mia 12b
    mia "What, you actually found someone?"
    show old_mia 8b
    show old_anon 2
    anon "Mhmm, [saga.cast.judith]."
    show old_anon 1
    show old_mia 43
    mia "For real?!"
    show old_mia 12
    mia "Why would [saga.cast.judith] agree to do that?"
    show old_mia 8
    show old_anon 10
    anon "I dunno, but she did."
    show old_anon 1
    show old_mia 12b
    mia "Oh, my..."
    mia "... Well, okay then."
    show old_mia 8b
    return


label bar04_pause2:
    return


label bar04_pause2.barb(when):
    if when == 1:
        anon f_confused "So we're good to go for tomorrow afternoon?"
    else:
        anon f_confused "So we're good to go for [saga.time.dow + when] afternoon?"

    barb "Yup."
    show anon f_calm
    barb "This is all so exciting!"
    return


label bar04_pause2.judith(when):
    jump bar04_barb3.judith


label bar04_pause2.mia(when):
    show old_anon 2
    anon "Did you hear the art lesson is back on?"
    show old_anon 1
    show old_mia 10

    if when == 1:
        mia "Yeah, tomorrow afternoon."
    else:
        mia "Yeah, [saga.time.dow + when] afternoon."

    show old_mia 12b
    mia "I can't believe [saga.cast.judith] volunteered to model for us."
    show old_mia 8b
    show old_anon 2
    anon "I know, right?!"
    show old_anon 1
    show old_mia 10
    mia "She's so brave!"
    show old_mia 7
    return


label bar04_delay2:
    scene camera at stage
    show anon a_cheer e_b f_happy m_teeth with dissolve
    anon @ -m_talk "( Stop the presses! It's finally naked drawing time for real! )"
    anon a_side e_w f_surprised @ -m_talk "( God, I hope [saga.cast.judith] doesn't flake on us. )"
    hide anon with dissolve
    return


label bar04_delay2.barb:
    anon f_confused "Everything is ready to go this afternoon, right?"
    barb "Yes, of course."
    anon f_calm "Okay, cool."
    barb "I have to say, it's refreshing to see one of my students so enthusiastic over an art project."
    anon @ f_happy "Yeah, I'm definitely beginning to see the appeal of art!"
    return


label bar04_delay2.judith:
    jump bar04_barb3.judith


label bar04_delay2.mia:
    show old_anon 2
    anon "Don't forget we've got an art lesson this afternoon."
    show old_anon 1
    show old_mia 10
    mia "Yeah, I haven't."
    show old_mia 12b
    mia "I hope everything works out okay with [saga.cast.judith]..."
    mia "... I'm nervous for her!"
    show old_mia 8b
    show old_anon 2
    anon "Oh, it'll be fine... I imagine [saga.cast.barb] has probably done this hundreds of times."
    show old_anon 1
    show old_mia 10
    mia "You're probably right."
    show old_mia 7
    return


label bar04_judith2:
    call shot.school_hall1w_judith
    show judith a_clasp f_sad at right
    show anon f_confused o_right at left with dissolve
    anon "Everything okay, [saga.cast.judith]?"
    judith @ f_confused -m_talk "Hmm?"
    judith "Oh, umm... hi [saga.cast.anon]."
    anon "It's time for the art project."
    anon "Are you feeling okay?"
    judith "I uhh-"
    judith "Guess I'm just nervous."
    anon f_shy "That's understandable."
    show judith f_shy
    anon @ f_confused "You don't have to do this, you know?"
    judith "But it would help you out a lot, wouldn't it?"
    anon "Yeah, it would."
    judith "So, in a way... you sorta... kinda... need me?"
    anon f_confused "Umm, you could put it that way..."
    anon f_shy "... Sure!"
    show anon a_surprised f_surprised
    judith a_cover_boobs e_n f_nervous m_lip @ -m_talk "Ngh!"
    anon "[saga.cast.judith]?"
    show judith a_cover_face of_blush
    anon a_side f_worried_surprised "What was that?"
    judith e_s -m_lip "N-nothing! I-"
    show anon f_confused
    judith "Just need a minute..."
    judith "... to collect... my thoughts."
    show judith e_w f_shy
    anon f_worried "O-okay."
    anon a_point f_shy "I'll see ya in there, okay?"
    show anon f_surprised
    judith a_clasp "Anything for you, [saga.cast.anon]!"
    show judith o_right
    hide anon
    with dissolve
    return


label bar04_judith2.rails:
    scene camera at stage

    if saga.cast.anon in saga.sets.school_hall1w:
        show anon a_pocket f_confused o_right at left with dissolve
        anon "( Hmm, what's wrong with [saga.cast.judith]? )"
        anon "( She looks kinda pale. )"
    else:

        show anon a_pocket f_worried with dissolve
        anon "( Everyone will be waiting, I should get to art class as soon as possible! )"

    hide anon with dissolve
    return


label bar04_art2:
    call shot.school_art_barb
    show school_art -table
    show old_barb 10 at face_right, pos(.35)
    show old_anon 2 at face_left, pos(.85) with dissolve
    anon "Hey, [saga.cast.barb]."
    show old_anon 10
    anon "[saga.cast.mia] isn't here yet?"
    show old_anon 5
    show old_barb 11
    barb "Nope, not yet."
    barb "You ready to start working?"
    barb "I'm expecting big things from you."
    show old_barb 10
    show old_anon 2
    anon "I won't let you down, [saga.cast.barb]."
    show old_anon 1
    show old_judith 2 behind old_anon at pos(.95)
    with dissolve.nowait
    judith "Umm, hello."
    show old_judith 1
    show old_barb 27
    with dissolve.nowait
    barb "And there's our star of the moment!"
    barb "Welcome, welcome, dear... come on in and let me have a look at you."
    show old_barb 26
    show old_judith 4 at pos(.6)
    with dissolve.nowait
    judith "..."
    show old_barb 45
    with dissolve.nowait
    pause
    show old_barb 46
    barb "Oh, yeah... look at those delicious hips..."
    show old_barb 45
    show old_judith 3
    judith "D-delicious?"
    show old_judith 1
    show old_barb 28 at face_right, pos(.4)
    with dissolve.nowait
    barb "... And these curves!"
    barb "You're the perfect subject for an art piece, [saga.cast.judith]."
    show old_barb 12
    with dissolve.nowait
    show old_judith 5
    judith "{i}*Gulp*{/i} Y-you mean it?"
    show old_judith 4
    show old_barb 13
    barb "Absolutely."
    show old_barb 11
    barb "I can't wait to get you out of those clothes and get started!"
    show old_barb 10
    show old_judith 5 at face_right, pos(.625)
    with dissolve.nowait
    judith "Oh umm, [saga.cast.barb] is gonna be here too huh?"
    show old_barb at face_left, pos(.15)
    show old_judith 1
    show old_anon 10
    with dissolve.nowait
    anon "Yeah, is that alright?"
    hide old_barb
    show old_anon 5
    show old_judith 2
    with dissolve.nowait
    judith "I dunno..."
    show old_judith 6
    show old_barb 60 at face_right, pos(.3)
    with dissolve.nowait
    barb "Oh look at her turning red, how delightful!"
    show old_judith 1 at face_left, pos(.6)
    with dissolve.nowait
    barb "Here, sweetie, take this and go change out of those clothes."
    barb "We'll wait right here for you."
    show old_barb 59
    show old_judith 3
    judith "Umm..."
    show old_barb 60
    show old_judith 6
    barb "Don't dawdle, we want as much time with you as possible."
    hide old_judith
    show old_barb 10
    with dissolve.nowait
    pause
    show old_barb 11
    barb "Great job, [saga.cast.anon]! She's gonna make a superb model!"
    show old_barb 10
    show old_anon 203
    pause
    show old_mia 8b behind old_anon at face_left, pos(.7)
    show old_barb 11
    with dissolve.nowait
    barb "... And here's our little cutie pie, just in time!"
    show old_barb 10
    show old_mia 12b
    mia "Sorry, I got held up."
    show old_barb 11
    show old_mia 8b
    barb "Oh, no worries... [saga.cast.judith] is just changing now."
    show old_barb 10
    show old_mia 10b
    mia "She's really gonna go through with it, huh?"
    show old_mia 9
    mia "I wish I was as brave as she is."
    show old_mia 11
    show old_anon 2
    anon "Yeah, it's pretty incredible isn't it?"
    show old_anon 11
    show old_judith 59 behind old_barb at face_right, pos(.45)
    show old_mia 7
    with dissolve
    pause
    show old_judith 44
    show old_judith robe overlay as judith_robe behind old_barb at face_right, pos(.45)
    with dissolve
    pause
    judith "..."
    show old_judith 45
    judith "W-what's [saga.cast.mia] doing here?!"
    show old_judith 44
    show old_barb 11
    barb "She's going to be drawing you as well, sweetie."
    show old_judith 45
    show old_barb 10
    judith "I'm having second thoughts about all this..."
    show old_anon 5
    show old_judith 52
    judith "... You didn't say there was going to be other people, [saga.cast.anon]!"
    show old_judith 51
    show old_barb 25
    barb "Calm down, [saga.cast.judith]... Everything is going to be fine, dear."
    show old_barb 11
    barb "You have nothing to be embarrassed about. Does she guys?"
    show old_barb 10
    show old_anon 2
    anon "Not at all."
    show old_anon 1
    show old_mia 10
    mia "Yeah, don't worry, [saga.cast.judith]. [saga.cast.barb] has been teaching us that everyone's body is beautiful."
    show old_mia 7
    show old_barb 11
    barb "That's right, [saga.cast.mia]. You're all beautiful in your own unique way."
    barb "You should be proud of your body, [saga.cast.judith]."
    show old_barb 10
    show old_judith 52
    judith "I dunno..."
    show old_judith 51
    show old_barb 58 with dissolve
    barb "I've got an idea!"
    hide old_barb with dissolve
    pause
    show old_barb 40 at face_right, pos(.2)
    with dissolve.nowait
    barb "These always calm me down when I'm feeling anxious..."
    show old_judith behind old_mia at face_left, pos(.55)
    show old_judith as judith_robe behind old_mia at face_left, pos(.55)
    with dissolve.nowait
    barb "Everybody take one."
    show old_barb 41
    show old_anon 2
    anon "Oh, I've heard you make the best brownies!"
    show old_anon 1
    show old_barb 40
    barb "Hehe, you better believe it!"
    barb "It's my secret recipe..."
    show old_barb 44 with dissolve
    pause
    show old_barb 43 with dissolve
    barb "... One hundred percent all natural."
    show old_barb 42
    show old_anon 602 at face_left, pos(.625)
    with dissolve.nowait
    pause
    show old_anon 599 at pos(.85) with dissolve
    pause
    show old_anon 600
    show old_mia 73 at pos(.6)
    with dissolve.nowait
    mia "They do look good..."
    hide judith_robe
    show old_mia 71 at pos(.7)
    show old_judith 60
    with dissolve.nowait
    judith "I do love brownies!"
    show old_judith 46
    with dissolve.nowait
    pause
    show old_judith 47
    show old_judith robe overlay as judith_robe behind old_mia at pos(.55)
    show old_mia 72
    with dissolve.nowait
    mia "Yum!! These are delicious!"
    show old_mia 71
    show old_judith 48
    judith "{i}*Nom nom nom*{/i}"
    hide judith_robe
    show old_judith 60
    with dissolve.nowait
    judith "Oh my gosh! They're so good!"
    show old_barb 43
    show old_judith 46
    with dissolve.nowait
    barb "Take it slow, [saga.cast.judith]. You don't wanna eat these too fast."
    show old_barb 42
    show old_judith 47
    show old_judith robe overlay as judith_robe behind old_mia at pos(.55)
    with dissolve.nowait
    pause
    show old_judith 49
    with dissolve.nowait
    judith "Mmm..."
    show old_mia 74
    show old_anon 26
    with dissolve.nowait
    anon "Heh, they had a kinda... earthy flavor."
    show old_anon 13
    show old_barb 12
    with dissolve.nowait
    pause
    show old_barb 13
    barb "How's everybody feeling?"
    show old_barb 12
    show old_anon 26
    anon "Goooood. Really gooood."
    show old_anon 13
    show old_judith 50
    judith "Meeee tooo."
    show old_judith 49
    show old_mia 75b
    with dissolve.nowait
    mia "Heheheheheheheehee!"
    show old_judith 50
    show old_mia 74
    with dissolve.nowait
    judith "This robe is super itchy!"
    show old_judith 49
    show old_barb 13
    barb "Well, now that you're feeling more relaxed, why don't you take it off, sweetie."
    barb "We can get this show on the road."
    show old_barb 12
    show old_judith 50
    judith "Mmm, yeah, okay..."
    hide old_judith
    hide judith_robe
    show old_judith 56 behind old_barb at old_right, pos(.45)
    with dissolve
    pause
    show old_judith 49 with dissolve
    pause
    show old_barb 13
    barb "Very good, dear."
    show old_barb 11
    barb "Now then, [saga.cast.anon] and [saga.cast.mia], why don't you two get seated and find your charcoal."
    show old_barb 10
    show old_mia 75b
    with dissolve.nowait
    mia "Heheheheeahahaaha!"
    mia "Everything is so twirly!!"
    show old_mia 74
    show old_barb 11
    with dissolve.nowait
    barb "Yes, it sure is, cutie pie."
    show old_barb 13
    barb "[saga.cast.judith] you need to take off your underwear too, sweetie."
    show old_barb 12
    show old_judith 51
    judith "Hmm?"
    show old_judith 52
    judith "You mean I have to show my..."
    judith "My..."
    judith "... Pussy?"
    show old_judith 51
    show old_mia 75b
    with dissolve.nowait
    mia "Pffftt!!! AHahahaah! That's such a funny word!"
    mia "Puuuusssy! HahahaaH!"
    show old_mia 74
    show old_barb 11
    with dissolve.nowait
    barb "Heh, calm down, [saga.cast.mia]!"
    show old_barb 25
    barb "You're still feeling self-conscious, [saga.cast.judith]?"
    show old_barb 24
    judith "Mmmhmm..."
    show old_barb 11
    barb "Well, what if the rest of us stripped down too?"
    show old_barb 10
    show old_judith 54
    pause
    show old_judith 55
    judith "... Yeah! That's a good idea!"
    show old_judith 54
    show old_anon 26
    anon "You want us to get naked too?"
    show old_anon 13
    show old_barb 11
    barb "We'll just strip down to our underwear."
    barb "That should be good enough, right [saga.cast.judith]?"
    show old_barb 10
    show old_judith 55 at face_right, pos(.475)
    with dissolve.nowait
    judith "... Yeah! I wanna see [saga.cast.anon]'s underwear!"
    show old_judith 54
    show old_barb 11
    barb "Very good then..."
    show old_barb 14
    with dissolve.nowait
    pause
    show old_barb 15 with dissolve.nowait
    pause
    show old_barb 16 with dissolve.nowait
    pause
    show old_barb 17 with dissolve.nowait
    pause
    show old_barb 36 with dissolve.nowait
    barb "Go ahead you two..."
    show old_barb 37
    show old_mia 75
    with dissolve.nowait
    mia "... Wait! Me?"
    show old_mia 74
    show old_barb 36
    barb "Especially you, cutie pie!"
    show old_barb 37
    show old_mia 75b
    with dissolve.nowait
    mia "Heheheheheeeh, okey-dokey!"
    show old_mia 76 with dissolve.nowait
    pause
    show old_mia 77 with dissolve.nowait
    pause
    show old_mia 78 with dissolve.nowait
    pause
    show old_mia 79 with dissolve.nowait
    pause
    show old_mia 80 with dissolve.nowait
    pause
    show old_mia 81
    show old_barb 36
    with dissolve.nowait
    barb "You didn't have to take off your bra, cutie pie!"
    show old_mia 82
    show old_barb 37
    mia "I didn't?"
    show old_mia 81
    show old_barb 36
    barb "Hehe, nope I said, \"Down to our underwear.\""
    show old_mia 82
    show old_barb 37
    mia "Ooooh..."
    mia "Okey-dokey!"
    show old_mia 82b
    with dissolve.nowait
    mia "This is fun!"
    show old_mia 81
    show old_barb 36
    with dissolve.nowait
    barb "Yes, it certainly is, dear."
    barb "We're waiting, [saga.cast.anon]."
    show old_barb 37
    show old_anon 21
    anon "Y-yeah. Okay!"
    show old_mia at face_right, pos(.6)
    show old_anon 8
    with dissolve.nowait
    pause
    show old_anon 265 with dissolve.nowait
    pause
    show old_judith 53
    pause
    show old_anon 267
    anon "( !!! )" with hpunch
    judith "... Wow!"
    show old_mia 82b with dissolve.nowait
    mia "It looks kinda angry! Pffft, hahahahaa!!!"
    show old_mia 81
    show old_judith 55
    with dissolve.nowait
    judith "It's so big..."
    show old_judith 54
    show old_anon 265b
    show old_barb 36
    barb "It sure is, dear."
    barb "... You still have to take those panties off before we can draw you."
    show old_barb 37
    show old_judith 55
    judith "... And pink."
    show old_judith 54
    show old_barb 36
    barb "Here, I'll help!"
    hide old_barb
    show old_mia at face_left, pos(.7)
    show old_judith 61
    with dissolve.nowait
    pause
    show old_judith 62
    with dissolve.nowait
    pause
    show old_barb 36 behind old_judith at old_left
    show old_judith 65b
    with dissolve.nowait
    barb "There's a good girl."
    show old_barb 37
    show old_judith 66
    judith "I-"
    show old_judith 65b
    show old_barb 36
    barb "Now, you two start drawing, okay?"
    show old_barb 37
    show old_anon 265c
    anon "Yes, ma'am."

    scene mono school_art_judith_pose
    mono "I could tell [saga.cast.judith] was still really nervous as [saga.cast.barb] helped her up onto the pedestal." with fade
    mono "It was very brave of her to model for an audience."
    mono "... But she wasn't exactly striking an inspirational pose up there."

    call shot.school_art_barb
    show school_art -table
    show old_barb 37 at face_right, left
    show old_judith 65b at face_left, pos(.42)
    with fade
    pause
    show old_barb 36
    barb "Sweetie? You have to loosen up a little..."
    show old_barb 37
    show old_judith 66
    judith "I don't..."
    judith "I mean, I..."
    show old_barb 36 at face_left, pos(.62)
    show old_judith 65b
    with dissolve.nowait
    barb "Shhh."
    barb "It's alright, [saga.cast.judith]."
    show old_judith 64 as old_barb at face_left, pos(.44)
    with dissolve.nowait
    barb "Just breathe in deeply..."
    show old_judith 66
    pause
    show old_judith 65b
    barb "... That's it."
    show old_judith 63 as old_barb
    pause
    show old_judith 64 as old_barb
    barb "You're a beautiful angel, [saga.cast.judith]."
    show old_judith 63 as old_barb
    show old_judith 66
    judith "... I am?"
    show old_judith 64 as old_barb
    show old_judith 65b
    barb "Oh yes! You're breathtaking, sweetie!"
    show old_judith 63 as old_barb
    pause
    hide old_barb
    show old_judith 67 at old_right, pos(.4)
    with dissolve
    barb "Spread your wings, [saga.cast.judith]."
    barb "Let the world see you fly!"
    show old_judith 68b
    show old_barb 36 behind old_judith at old_right, pos(.58)
    with dissolve
    barb "{i}*Gasp*{/i} Perfection!"
    show old_judith 69
    show old_barb 37
    judith "... You think I'm perfect?"
    show old_judith 68
    show old_barb 36
    barb "Of course, sweetie!"
    barb "Just look at that curvaceous body..."
    barb "How could anyone resist it?"
    show old_barb 37
    pause
    show old_barb 36
    barb "Now, don't you move an inch!"
    barb "Give the artists a chance to capture your beauty!"
    show old_barb 37
    show old_judith 69b
    judith "O-okay..."

    scene mono school_art_observe
    mono "[saga.cast.barb] had definitely made [saga.cast.judith] more comfortable." with fade
    mono "... And she had given me the perfect inspiration for my drawing!"
    mono "Though it was little hard to concentrate on my work with [saga.cast.barb] hovering over my shoulder..."

    call shot.school_art_barb
    show school_art -table
    show old_judith 68 at face_left, pos(.4)
    with fade
    barb "It's very good, [saga.cast.anon], but I think you could do better."
    show old_barb 36 behind old_judith at face_left, pos(.8)
    with dissolve.nowait
    barb "I'm not sure you're really capturing the curves of her delicious body."
    show old_barb 37 at face_left, pos(.58)
    with dissolve.nowait
    anon "What do you mean?"
    show old_barb 36 at face_right, pos(.6)
    with dissolve.nowait
    barb "Well, have a look!"
    barb "Sometimes you have to really get hands on with your subject and feel the shapes."
    show old_barb 36 at face_left, pos(.58)
    with dissolve.nowait
    barb "... And [saga.cast.judith] here has such great contours!"
    hide old_barb
    show old_judith 70
    with dissolve.nowait
    judith "Ahh!"
    show old_judith 71 with dissolve.nowait
    pause
    show old_judith 72 with dissolve.nowait
    judith "{i}*Whimpers*{/i}"
    show old_judith 72b
    judith "AAAhh!" with hpunch
    show old_judith 72e
    barb "... Well, look who came out to play!"
    show old_judith 72c_72d
    pause
    judith "Mmm..."
    show old_judith 72e
    barb "How does that feel, sweetie?"
    show old_judith 72
    judith "Really..."
    judith "Ahh, really good!"
    show old_judith 72e
    barb "Yes, you just enjoy, dear."
    show old_judith 72c_72d
    judith "NNGGHH!"
    pause
    show old_judith 72
    judith "Haaaah!"
    show old_judith 72e
    barb "Beautiful!"
    show old_judith 72
    judith "OH, I CAN'T!"
    show old_judith 73 at old_right, pos(.38)
    show old_barb 37 behind old_judith at old_right, pos(.58)
    judith "AAAHHH!" with hpunch
    show old_judith 66
    judith "Haaah... Haaah..."
    show old_judith 65
    show old_barb 36
    barb "Very good, sweetie!"
    show old_judith 58 at face_right, pos(.15)
    show old_barb 37
    with dissolve.nowait
    judith "That was..."
    show old_judith 57
    judith "..."
    show old_judith 58
    judith "... Can we do that again?"
    show old_judith 57
    show old_barb 36
    barb "... Maybe later, sweetie."
    show old_barb 36 at face_right, pos(.6)
    with dissolve.nowait
    barb "Do you understand now, what I mean about feeling the shapes, [saga.cast.anon]?"
    show old_barb 37
    anon "I'm not sure..."
    show old_mia 82 behind old_judith at face_right, pos(.29)
    with dissolve.nowait
    mia "I think I get it, [saga.cast.barb]!"
    show old_mia 81
    show old_barb 36 at face_left, pos(.5)
    with dissolve.nowait
    barb "Good, you can help me show him then."
    show old_barb 36 at face_right, pos(.45)
    with dissolve.nowait
    barb "Come up here and join us, [saga.cast.anon]!"
    show old_barb 37
    anon "Really?"
    show old_barb 36
    barb "Yes, this is something every good artist needs to understand."
    show old_anon 101c at pos(.585)
    with dissolve.nowait
    anon "O-okay."
    hide old_anon
    hide old_mia
    show old_barb group 4
    with dissolve.nowait
    anon "Hehehehe."
    show old_barb group 1
    barb "Now, go ahead."
    show old_barb group 2
    barb "Both of you..."
    show old_barb group 1
    barb "... Feel the shapes."
    show old_barb group 4
    mia "Hehehe, okay!"
    show old_barb group 5_6 with dissolve.nowait
    pause
    show old_barb group 3 with dissolve.nowait
    anon "... Like that?"
    show old_barb group 1
    barb "Mmmhmm... Just like that..."
    show old_barb group 4
    mia "Hehehee, I hope God isn't watching..."
    show old_barb group 2
    barb "You're both doing a great job!"
    show old_barb group 1
    barb "Keep going."
    show old_barb group 5_6 with dissolve.nowait
    pause
    barb "Mmm..."
    pause
    show old_barb group 1 with dissolve.nowait
    barb "Very good, [saga.cast.anon]!"
    show old_barb group 2
    barb "Now try feeling, [saga.cast.mia]'s shapes."
    show old_barb group 3
    anon "I uhh..."
    show old_barb group 4
    mia "It's okay!"
    mia "Feel the shapes, [saga.cast.anon]!"
    show old_barb group 7_8 with dissolve.nowait
    pause
    show old_barb group 4 with dissolve.nowait
    mia "Honk honk!"
    show old_barb group 9 with dissolve.nowait
    mia "Pfft, hahahahaha!!"
    show old_barb group 2 with dissolve.nowait
    barb "Oh, isn't she just the most adorable thing ever?!"
    barb "Alright, now feel mine again..."
    show old_barb group 5_6 with dissolve
    pause
    show old_judith 58
    judith "... You guys can feel my shapes if you want."
    show old_judith 57
    show old_barb group 2 with dissolve.nowait
    barb "Well, goodness! Look who's finally coming out of her shell!"
    barb "We'll get to you in a second, sweetie. Why don't you go check the supply cabinet for me..."
    barb "There should be some incense and candles in there to help us set the mood."
    show old_judith 58
    show old_barb group 5_6 with dissolve.nowait
    judith "... Yes, ma'am."
    hide old_judith
    with dissolve
    pause
    show old_barb group 10 with dissolve.nowait
    ursula "WHAT IN THE WORLD IS GOING ON IN HERE?!" with hpunch
    ursula "WHY ARE YOU ALL NAKED?!"
    show old_anon 100 behind old_barb at face_right, pos(.575)
    show old_ursula 3 at pos(.825)
    show old_barb 39
    show old_mia 83 at face_right, pos(.305)
    with dissolve.nowait
    barb "[saga.cast.ursula.name]! I was just teaching the students some art techniques..."
    show old_barb 38
    show old_ursula 38
    ursula "ART TECHNIQUES?! DO I LOOK LIKE AN IDIOT TO YOU?!"
    show old_barb 39
    show old_ursula 3
    barb "Of course not, we were just-"
    show old_ursula 28
    show old_barb 38
    ursula "DO I NEED TO REMIND YOU THAT THIS IS A SCHOOL AND NOT A BROTHEL!"
    show old_barb 39
    show old_ursula 3
    barb "You're being ridiculous, I'm just trying to help them improve their art."
    show old_ursula 34
    show old_barb 38
    ursula "JUST GET SOME CLOTHES ON, ALL OF YOU!" with hpunch
    $ renpy.end_replay()
    hide old_mia
    hide old_anon
    show old_ursula 29
    show old_barb 17
    with dissolve
    pause
    show old_barb 16 with dissolve.nowait
    pause
    show old_barb 15 at face_left, pos(.25) with dissolve.nowait
    pause
    show old_barb 14 with dissolve.nowait
    pause
    show old_barb 24 at face_right, pos(.3)
    show old_ursula 27
    with dissolve.nowait
    ursula "You had better have a damn good explanation for this, [saga.cast.barb.name]!"
    show old_anon 11 behind old_barb at face_right, pos(.425)
    show old_mia 45 at face_right, pos(.155)
    show old_barb 25
    show old_ursula 29
    with dissolve.nowait
    barb "[saga.cast.mia] and I were helping [saga.cast.anon] here practice."
    barb "Trying to prepare him for-"
    show old_barb 24
    barb "..."
    show old_ursula 27
    ursula "Prepare him for what?!"
    show old_ursula 29
    show old_mia 46
    mia "This ar-"
    show old_mia 45
    show old_barb 25
    barb "A gift!"
    barb "... He was going to paint something for you, [saga.cast.ursula.name]!"
    show old_barb 24
    pause
    show old_barb 25
    barb "A gift, to hang up in your office!"
    show old_barb 24
    show old_ursula 27
    ursula "A gift?! For me?! What, like a portrait?"
    show old_ursula 29
    show old_barb 25
    barb "Well, sure! If that's what you want..."
    show old_barb 24
    show old_ursula 27
    ursula "Is he any good?"
    show old_barb 25
    show old_ursula 29
    barb "Very good, have a look for yourself!"
    show old_barb 24
    pause
    hide old_ursula with dissolve.nowait
    pause
    show old_ursula 42 at pos(.825) with dissolve.nowait
    ursula "What the hell is this?"
    show old_ursula 41
    show old_mia 46
    mia "Oh, that's umm... that's mine, ma'am."
    mia "... I'm not very good."
    show old_mia 45
    ursula "..."
    show old_ursula 42
    ursula "Then why are you here, after school, taking private courses?"
    show old_ursula 41
    show old_barb 25
    barb "My classes aren't just for talented artists."
    barb "They are open to anyone with a desire to express themselves through art."
    barb "... And [saga.cast.mia] here has a great love for art."
    show old_barb 24
    show old_ursula 42
    ursula "Uh huh..."
    ursula "In reality, you just found yourself a cute little package, didn't you?"
    show old_ursula 41
    show old_barb 25b
    barb "That's not..."
    show old_barb 24
    show old_ursula 42
    ursula "... And now you're just working to unwrap it, huh?"
    ursula "Have yourself a little taste?"
    ursula "... I'm well aware of your methods, [saga.cast.barb.name]."
    show old_ursula 43 with dissolve.nowait
    pause
    show old_ursula 44 with dissolve.nowait
    ursula "Hmm."
    show old_ursula 45
    ursula "The boy painted this?"
    show old_ursula 44
    show old_anon 10
    anon "Yes, ma'am."
    show old_anon 5
    show old_ursula 45
    ursula "Well, I guess I was wrong about you, [saga.cast.anon]."
    ursula "You're actually good for something, after all..."
    show old_ursula 44
    show old_barb 11
    barb "He is very talented, isn't he?"
    show old_barb 24
    show old_ursula 27
    with dissolve.nowait
    ursula "Oh, shut up!"
    ursula "I should fire you, right here and now!"
    ursula "In here getting groped by naked students..."
    show old_ursula 35b with dissolve.nowait
    ursula "..."
    show old_ursula 35c
    ursula "It is impressive work though."
    show old_ursula 35
    ursula "Hmm..."
    show old_ursula 27 with dissolve.nowait
    ursula "I'm feeling generous, so I {i}might{/i} let this incident slide!"
    show old_ursula 26
    show old_barb 11
    barb "That would be wond-"
    show old_barb 24
    show old_ursula 27
    ursula "... But only if your student here can recreate this quality on a portrait of me!"
    show old_ursula 26
    show old_barb 25
    barb "Oh, that's shouldn't be a problem. Right, [saga.cast.anon]?"
    show old_barb 24
    show old_anon 10 at face_left, pos(.45) with dissolve.nowait
    anon "Uhh..."
    show old_anon 11 at face_right, pos(.425)
    show old_ursula 27
    with dissolve.nowait
    ursula "And it has to be to my exact specifications!"
    ursula "No funny business!"
    show old_ursula 29
    show old_barb 25
    barb "Oh, of course! Anything you want, ma'am."
    show old_ursula 27
    show old_barb 24
    ursula "Damn right, anything I want!"
    show old_ursula 27
    ursula "Now you kids get your asses home before I change my mind and expel you both!"
    show old_ursula 29
    show old_barb 25
    barb "Go on you two. I'll see you tomorrow."
    hide old_anon
    hide old_mia
    with dissolve
    return


label bar04_art2.judith:
    call shot.school_hall1w_judith
    show judith a_clasp f_shy at right
    show anon f_worried o_right at left with dissolve
    judith "I just need a minute, [saga.cast.anon]."
    anon f_shy "Alright, I'll see you inside."
    hide anon with dissolve
    return


label bar04_art2.rails:
    scene school_hall1w at stage
    show anon a_pocket f_worried o_right at left with dissolve
    anon @ -m_talk "( I'm sure [saga.cast.judith] will be fine, probably. )"
    anon @ -m_talk "( Best hurry into the art room. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
