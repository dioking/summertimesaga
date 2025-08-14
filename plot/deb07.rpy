label deb07_lobby:
    scene debbie_lobby -debbie at stage
    show debbie a_clasp at right
    show anon a_pocket o_right at left with dissolve
    debbie "Oh, hey there sweetie!"
    debbie f_curious "Heading to bed?"
    anon "Nah, just looking around for something to do."
    anon "Why, what are you up to?"
    debbie f_calm "I was just about to sit down for a movie."
    anon "Cool."
    debbie @ -m_talk "..."
    debbie "Why don't you come join me?"
    anon f_surprised "Really?"
    debbie "Yeah, why not?"
    debbie "It's still early and I would love the company."
    anon f_happy "Y-yeah, okay... That sounds really nice, [saga.cast.debbie]."
    debbie f_happy "Great!"
    debbie "I'll go get situated and you just come join me when you're ready, alright?"
    anon "Sounds good."
    hide debbie with dissolve
    return


label deb07_debbie:
    scene debbie_lounge at stage(.348, .475, 3.5)
    show anon a_pocket at right with dissolve
    show debbie_lounge -debbie
    show debbie a_clasp o_right at left, zoom(.95)
    with dissolve.nowait
    debbie "There you are..."
    debbie "... Ready to start the movie?"
    anon "Yup! What are we watching?"
    debbie f_sad "Hmm, I haven't decided yet... I'm kind of in the mood for romance."
    anon f_shy "Ugh, seriously?"
    debbie f_happy "Hehe, yeah!"
    debbie f_curious "Why, what would you like to watch?"
    anon f_worried "I dunno... Something with some action maybe?"
    show anon f_sceptical
    debbie @ e_r f_bored "Pfft, typical man."
    anon "Heh, is that a bad thing?"
    debbie f_happy "Hehehe, no... I suppose not."
    show anon f_calm
    debbie f_sad "Tsk, I'm really in the mood for a sappy romance though!"
    debbie "How about you let me choose this one and you can pick next time?"
    anon f_shy "Yeah, alright..."
    anon "... Let's see what we can find."
    debbie f_happy "Yay!! Thanks, sweetie!"

    scene black
    with dissolve
    return


label deb07_debbie.bed1:
    call shot.debbie_bed1_door
    show anon at pos(.4) with dissolve
    show debbie_lounge -debbie
    show debbie at right, zoom(.95)
    with dissolve.nowait
    debbie "Are you ready to watch a movie?"
    anon a_uneasy f_worried o_right "I'll be right there."
    debbie "Okay, sweetie."
    hide anon
    hide debbie
    show debbie_lounge debbie
    with dissolve
    return


label deb07_debbie.fence:
    scene camera at stage
    show anon a_pocket o_right at left with dissolve
    anon @ -m_talk "( I shouldn't keep [saga.cast.debbie] waiting... )"
    hide anon with dissolve
    return


label deb07_movie:
    scene debbie_tv
    debbie "Oooh, There we go!"
    debbie "I don't think I've seen this one yet."
    anon "Yeah, great."

    scene debbie_lounge_couch dark
    show anon a_side_knee f_pensive o_right p_couch_turn at pos.couch_sit_right
    show debbie e_b f_happy m_laugh p_couch at pos.couch_sit
    with fade
    debbie @ -m_talk "Haha!"
    debbie e_w f_calm -m_laugh @ p_couch_turn "Don't be like that!"
    debbie "You never know... you might like it."
    show debbie a_remote e_onw
    anon "I won't."
    anon e_onne p_couch "Believe me, I know."
    debbie a_side @ e_r f_bored "Oh, just hush and watch!"

    scene mono debbie_lounge_couch1
    mono "I'll admit, the film wasn't so bad. Not much action but it at least succeeded in landing some good comedic moments." with fade
    mono "[saga.cast.debbie] certainly seemed to enjoy it. Her outbursts of melodic laughter frequently filled the room and brought more than a few smiles to my face."

    scene mono debbie_lounge_couch2
    mono "As the film progressed, she made herself more and more comfortable and I increasingly found my eyes drawn to her..." with fade
    more "... Especially when the movie took an erotic turn."

    label deb07_movie.cookie hide:
    scene debbie_lounge_couch dark
    show debbie e_ne p_couch_lay_side
    show anon e_onne o_right p_couch at pos.couch_sit_right
    with fade
    anon @ -m_talk "( Wow, this is getting pretty intense... )"
    anon e_wsw p_couch_turn @ -m_talk "( ... It's a bit awkward but [saga.cast.debbie] doesn't seem to be bothered. )"
    show anon e_onne p_couch
    pause
    show debbie e_b f_curious_hurt p_couch_lay_side_stretch
    show anon f_surprised behind debbie
    anon @ -m_talk "( !!! )"
    show debbie e_ne f_calm ob_leg_down_01 p_couch_lay_side_extend
    show anon e_s f_confused
    pause
    anon e_wsw p_couch_turn @ -m_talk "( What is she doing?! )"
    anon e_sse @ -m_talk "( She's touching my... )"
    show anon a_surprised e_s f_surprised p_couch
    show debbie ob_leg_down s_1
    pause
    anon f_worried_surprised @ -m_talk "( Did she put her foot there on purpose? )"
    anon e_wsw p_couch_turn @ -m_talk "( ... )"
    anon @ -m_talk "( ... No, I don't think she even realizes- )"
    anon e_b f_distressed m_teeth @ -m_talk "( Uh oh... )"
    show anon a_side e_s f_surprised p_couch
    pause
    show mimic anon as mimic_anon at pos.anon
    show debbie z_b_f_of
    show mimic debbie as mimic_debbie at pos.debbie
    anon d_hard f_worried_surprised z_b_ob_f_of_a_oa -m_teeth @ -m_talk "( Ah no! Ah crap! Ah jeez! )"
    anon e_ese @ -m_talk "( Please, don't notice! )"
    anon e_b @ -m_talk "( Please, oh please, oh please! )"
    show anon e_onne
    pause
    show anon e_s f_worried
    debbie f_surprised ob_leg_down_01 @ -m_talk "( Sheesh, this is so graphic! )"
    anon f_shy @ -m_talk "( Oh, thank God, she stopped. )"
    anon e_onne @ -m_talk "( Maybe it'll go away before she notices. )"
    debbie f_shy @ -m_talk "( I hope this isn't making [saga.cast.anon] uncomfortable. )"
    pause
    show anon f_surprised
    debbie e_se f_curious ob_leg_down @ -m_talk "( Hmm, what is- )"
    show anon d_none e_s m_teeth
    show debbie ob_leg_up
    pause
    show anon e_ese f_worried_surprised -m_teeth
    debbie e_ne f_surprised ob_leg_up_01 @ -m_talk "( Oh my god! )"
    show anon e_s f_surprised
    debbie e_se f_curious ob_leg_up @ -m_talk "( Is that his- )"
    show anon e_onne f_worried_surprised
    debbie e_ownw f_worried_surprised m_teeth ob_leg_up_02 @ -m_talk "( !!! )"
    debbie f_hurt @ -m_talk "( I don't understand how can he be this big?! )"
    debbie f_curious ob_leg_mid -m_teeth @ -m_talk "( Where the heck did it come from?! )"
    show anon d_hard
    debbie e_se ob_leg_down_02 @ -m_talk "( I mean, his father wasn't small, but it was nothing like this... )"
    show anon e_s
    debbie ob_leg_down_01 @ -m_talk "( ... No matter where I move my feet, it's there! )"
    show anon e_onne
    debbie e_ese f_shy m_lip @ -m_talk "( Poor thing. This has got to be awkward for him... )"
    debbie e_se f_curious @ -m_talk "( Should I just ignore it? )"
    pause
    debbie @ -m_talk "( ... )"
    debbie e_ownw f_shy @ -m_talk "( Oh gosh, I'm staring!!! )"
    debbie -m_lip @ -m_talk "( Snap out of it, [saga.cast.debbie]... What's the matter with you?! )"
    anon e_wsw p_couch_turn @ -m_talk "( ... )"
    anon @ -m_talk "( Yeah, this is not good... She's definitely noticed. )"
    anon e_sse @ -m_talk "( But why hasn't she taken her feet away? )"
    anon e_wsw @ -m_talk "( Should I say something? )"
    anon a_uneasy f_shy_surprised "I uhh... This movie got kinda {i}naughty{/i}, huh?"
    debbie of_blush @ e_ese "Y-yeah, it sure did."
    pause
    anon a_side e_ese f_confused p_couch @ -m_talk "( Is she blushing? )"
    pause
    show anon e_onne f_shy
    debbie @ -m_talk "..."
    debbie e_ese "S-sorry, I... I didn't know..."
    anon e_wsw f_calm p_couch_turn "No, it's okay! Nothing I haven't seen before."
    pause
    show anon e_onne p_couch
    debbie e_ownw m_lip of_none @ -m_talk "( Oh no, I hope he didn't notice me staring... )"
    show anon e_s f_surprised
    debbie ob_leg_down @ -m_talk "( It's just so huge! I wonder what something that big would even feel- )"
    debbie ob_leg_down_01 -m_lip @ f_surprised -m_talk "( Ahh!!! What the heck am I thinking?! )" with hpunch
    show anon e_ese f_confused
    pause
    anon e_wsw f_worried p_couch_turn "{i}*Ahem*{/i} So, ehh... Other than this scene, the movie is pretty good."
    show debbie e_ese
    anon f_shy_surprised "Or well, it's better than I thought it would be."
    debbie "O-oh, yeah? I'm glad to hear it."
    show anon e_onne f_shy p_couch
    show debbie e_ne
    pause
    debbie @ -m_talk "( Come on, how much longer is this scene gonna go on for?! )"
    show anon f_surprised
    debbie f_surprised @ -m_talk "( W-wait, they aren't gonna- )"
    show anon a_surprised f_shocked m_open z_reset
    show debbie f_shocked m_open p_couch_lay_side z_reset behind anon
    hide mimic_debbie
    hide mimic_anon
    debbie @ -m_talk "( Oh. My. God! )"
    pause
    show debbie f_surprised -m_open
    anon f_surprised -m_open "Hookay, I take it back..."
    anon a_side "... I have never seen anyone do... {i}that{/i}... before!"
    debbie e_ese f_worried "Is this going to get X-rated?!"
    debbie "Should I shut this off?"
    show debbie e_w f_shy ob_none p_couch at pos.couch_sit
    anon f_shy_surprised "Ehh-"
    debbie "I should shut this off."
    show debbie a_remote e_onw
    anon a_wait e_w f_worried p_couch_turn "N-no, not if you don't want too..."
    show debbie e_w f_surprised p_couch_turn
    anon f_shy "... I mean, I'm solid."
    debbie a_side e_sw of_blush "S-solid?"
    show anon a_side f_confused
    pause
    debbie e_onw f_worried p_couch @ -m_talk "{i}*Gulp*{/i}"
    show debbie e_w
    anon f_calm "Yeah, like... as in, I can handle it."
    debbie f_shy "O-oh, right..."
    debbie e_onw "... Uhh, okay."
    show anon e_onne p_couch
    pause
    anon @ -m_talk "( ... )"
    debbie @ -m_talk "( ... )"
    $ renpy.end_replay()

    scene black
    with dissolve
    mono ""

    scene debbie_lounge dark at stage(.5, .475, 3.5)
    show debbie a_clasp o_right at left
    show anon a_pocket at right
    with dissolve
    anon "Well, thanks for the movie, [saga.cast.debbie]."
    debbie f_shy "Yeah, that was certainly... umm, interesting."
    anon a_uneasy f_shy of_blush "No, really... It was fun."
    debbie f_curious "Yeah?"
    anon "I always have fun spending time with you, [saga.cast.debbie]."
    debbie f_happy "Heh, aww... what a wonderfully sweet thing to say!"
    anon a_side f_calm of_none "Well, it's the truth."
    debbie @ e_b m_laugh of_blush "Stop, you're making your old landlady blush!"
    anon a_wave "Alright, well... goodnight then!"
    show anon e_b f_happy p_debbie_hug_away
    show debbie b_anon p_hug_away at pos.anon
    debbie "Goodnight, sweetheart!"
    anon @ e_nne_nnw f_elated -m_talk "( Mmm, Brazilian Bum Bum! )"
    show anon a_side e_w p_stand
    show debbie a_side f_calm p_stand -b_anon at center
    debbie "Sleep well!"
    hide anon with dissolve.nowait
    anon "You too, [saga.cast.debbie]!"
    pause
    debbie a_clasp @ -m_talk "( Mmm, I really am enjoying all this time we've been spending together lately. )"
    debbie @ -m_talk "( He's such good company... )"
    debbie f_horny @ -m_talk "( ... And so handsome. )"
    show debbie a_embarrassed f_surprised with none.nowait
    with hpunch
    pause 
    debbie a_facepalm e_b f_worried_surprised @ -m_talk "( Oh gosh, what is going on with me today?! )"
    hide debbie with dissolve

    scene debbie_hall dark at stage with fade
    show anon a_pocket f_shy o_right with dissolve
    anon @ -m_talk "( Well, that was super awkward! )"
    anon @ -m_talk "( I'm just straight up popping boners right between my landlady's feet now! )"
    anon @ -m_talk "( I mean, at least she didn't say anything... )"
    anon @ -m_talk "( ... But it definitely felt uncomfortable for a while. )"
    anon f_surprised @ -m_talk "( I hope [saga.cast.debbie] isn't upset with me or anything. )"
    anon @ -m_talk "( ... )"
    anon e_osw f_sad @ -m_talk "( Ugh, I'll worry about it tomorrow. Right now, I need some sleep. )"
    hide anon with dissolve
    return


label deb07_movie.pink:
    scene debbie_tv
    show tv info 91 as num at tv_info
    show tv auth only onlayer aux
    with fadefast.aux
    anon "( Eeep! ){nw=1}"
    return


label deb07_movie.rails:
    scene debbie_tv
    anon "( We only just sat down! )"
    anon "( I need to find a movie to watch with [saga.cast.debbie]. )"
    return


label deb07_outro:
    return


label deb07_outro.block:
    call shot.debbie_bed1_door
    show anon with dissolve
    anon @ -m_talk "( After the night we've just had, probably best I leave her be. )"
    anon a_uneasy of_blush @ -m_talk "( No reason to make things even more awkward. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
