label deb04_landing:
    call shot.debbie_bath_door

    if saga.camera.last is saga.sets.debbie_lobby:
        show debbie f_sad o_right at left
    else:
        show debbie f_sad at pos(.6)

    if saga.camera.last is saga.sets.debbie_lobby:
        show anon a_pocket f_worried at pos(.6) with dissolve
    else:
        show anon a_pocket f_worried o_right at left with dissolve

    debbie "Sweetie! Oh, thank goodness you're here!"
    anon "What's wrong?"
    debbie a_nervous "We've got a big problem in the bathroom!"
    anon f_confused "Huh?"
    debbie "The pipe under the sink broke and it's spraying water everywhere!"
    show anon f_surprised
    debbie "Could you come take a look at it?"
    anon a_point_self "M-me?"
    debbie "We can't afford to call a repairman right now, and neither [saga.cast.jenny] or I know a thing about plumbing..."
    anon a_uneasy e_e f_worried "I'm not all that knowledgeable about it either, I'm afraid."
    debbie a_side e_s "Right, of course."
    show anon a_side e_w
    pause
    debbie "Silly of me to think you would be... I'm just-"
    show anon a_up f_surprised
    debbie a_cover_face e_b "I don't know what to do!"
    show anon e_se f_disgusted
    pause
    show anon a_side e_w f_shy
    pause
    anon "Alright, well... I guess, lemme look and see if I can figure it out."
    debbie a_cover_face_peek e_w "Really?"
    debbie a_clasp f_shy "Oh, that would be great..."
    debbie "... Thanks, sweetie!"

    if saga.camera.last is saga.sets.debbie_lobby:
        show debbie f_surprised
    else:
        show debbie f_surprised o_right

    hide anon with dissolve.nowait
    anon "Don't thank me yet, I'm just as likely to make things worse!"

    if saga.camera.last is saga.sets.debbie_lobby:
        show debbie a_surprised at center
    else:
        show debbie a_surprised o_right

    with dissolve.nowait
    debbie "What?!"
    hide debbie with dissolve.nowait
    debbie "Don't say that!"

    label deb04_landing.cookie hide:
    scene mono debbie_bath_fix1
    mono "I rushed towards [saga.cast.jenny]'s cursing." with fade
    more "The scene upon entering was almost comical."
    mono "[saga.cast.jenny] was absolutely flustered and looked like a drowned rat. The exposed pipe was spouting water all over the place and making quite a mess."

    scene debbie_bath at stage
    show jenny a_hips c_casual_pants_wet f_annoyed at pos(.65)
    with fade
    show anon f_surprised o_right at left with dissolve
    jenny "It's about time you showed up!"
    anon f_confused "What did you do?!"
    jenny f_angry "ME?!"
    jenny "Fuck you, all I did was turn on the faucet!"
    show debbie a_clasp f_sad o_right behind anon at pos(.1) with dissolve.nowait
    jenny "It was making this awful sound like an elephant dying and when I opened the cabinet to look, the fucking thing sprayed me right in the face!"
    show debbie f_annoyed
    show jenny f_angry_pouty
    anon f_happy @ e_b m_laugh "Pfft, hahaha!"
    debbie "[saga.cast.jenny], language!!"
    jenny f_annoyed @ e_r "Oh, for fuck's sake, Mother..."
    show debbie f_sad
    jenny "... We have an emergency here, I think a bit of swearing is to be expected!"
    anon @ e_b m_laugh "Man, I wish I had a camera right now."
    jenny "Stop laughing at me and fix it, you block head!"
    anon f_smug "You maybe wanna move out of the way?"
    jenny f_disgusted "Ugh."
    jenny f_annoyed @ e_r "I can't believe you're the closest thing we have to a man around here now."
    anon f_grumpy "Yeah, keep bitching... that's really helpful."
    debbie "Would you kids knock it off please?!"
    show anon f_worried -o_right behind debbie at pos(.35)
    jenny f_angry_pouty @ f_annoyed "Tch!"
    anon "Sorry, [saga.cast.debbie]."
    anon f_calm "Look, before I can do anything, we'll have to shut the water off."
    anon "There's a valve down in the basement for that, right?"
    debbie "Uhh, I'm... not... sure..."
    debbie f_shy "... But I will need some water for cooking, so I'll go fill a saucepan before you turn it off."
    hide debbie with dissolve.nowait
    jenny f_annoyed @ e_r "Oh my god, we're going to drown."
    anon o_right "No, it's down there..."
    anon "... I remember Dad had to shut it off once."
    anon "I'll be right back!"
    hide anon with dissolve
    return


label deb04_utility:
    scene debbie_utility at stage
    show anon a_pocket e_nw f_pensive o_right with dissolve
    anon @ -m_talk "( The water valve should be next to the water heater... )"
    anon @ -m_talk "( ... I'd better shut it off before upstairs floods! )"
    hide anon with dissolve
    return


label deb04_utility.bath:
    scene debbie_bath at stage
    show jenny a_hips c_casual_pants_wet f_annoyed at pos(.65)
    show anon o_right at left with dissolve
    jenny "What are you doing?!"
    anon f_confused "Uhh, I dunno... what {i}am{/i} I doing?"
    jenny f_angry m_teeth "Turn the water off, you human kumquat!"
    anon f_surprised "Oh, right!"
    hide anon with dissolve
    return


label deb04_utility.debbie:
    scene camera at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( I've gotta fix the bathroom sink somehow. )"
    hide anon with dissolve
    return


label deb04_utility.fence:
    scene camera at stage
    show anon f_worried with dissolve
    anon @ -m_talk "( The valve to shut the water off should be somewhere in the basement. )"
    hide anon with dissolve
    return


label deb04_valve:
    scene debbie_utility -debbie_valve at stage(.421, .518, 2.6, b=0)
    show debbie_utility debbie_valve as valve at stage(.421, .518, 2.6, b=0)
    show anon a_boiler o_right p_bend_away behind valve at pos(.35) with dissolve
    pause
    hide valve
    show debbie_utility debbie_valve
    anon a_side -p_bend_away @ -m_talk "( Okay, the valve's shut. )"
    anon @ -m_talk "( I should head back upstairs and take a look under that sink. )"
    hide anon with dissolve
    return


label deb04_valve.fence:
    scene debbie_utility at stage
    show anon a_whisper f_worried_surprised at pos(.85, 1.4) with dissolvefast.nowait
    anon "Greenwall, stop the water!"
    hide anon with dissolvefast.nowait
    pause 1
    show anon a_point_back f_worried_surprised o_right at pos(.35, 1.3) with dissolvefast.nowait
    anon "The valve on the wall beside you! Go for it!"
    hide anon with dissolvefast.nowait
    pause 1
    show anon f_afraid at pos(.6, 1.45) with dissolvefast.nowait
    anon "Turn it, QUICK!"
    hide anon with dissolvefast
    return


label deb04_bath(fast):
    scene debbie_bath at stage
    show jenny a_hips c_casual_pants_wet f_annoyed at pos(.65)
    show anon f_happy o_right at left with dissolve
    jenny @ e_r "Fucking finally!"
    anon a_point f_smug "See, I told you it was down there!"
    jenny "Yeah, great. Now stop wasting time and fix it!"
    anon a_wtf f_pouty "I haven't even looked at it yet."
    jenny @ f_angry "Well, hurry up... I've got shit to do today!"
    show jenny f_disgusted

    if fast:
        anon a_side f_sceptical "Okay, okay! I'm sure my trusty spanner and I can handle it."
    else:
        anon a_side f_sceptical "Okay, okay! I'll have to see what I can do."

    anon e_sw f_surprised @ -m_talk "..."
    show jenny e_s f_calm
    pause
    jenny e_w f_angry m_teeth @ -m_talk "..."
    jenny "Did you get a good look, you little perv?!"
    anon a_uneasy e_w f_tired_happy "I wasn't-"
    jenny "Oh please, it's so obvious you're staring at my tits."
    anon e_sw f_horny @ -m_talk "..."
    jenny "What's the matter with you?"
    anon a_side e_w f_shy "I'm sorry, [saga.cast.jenny]. It's just hard not to when-"
    show anon f_tired
    jenny "Oh, shut up!"
    jenny f_annoyed -m_teeth "If you're going to stare, at least be a man about it!"
    show anon f_confused
    jenny "Denying it or making excuses just makes you look like a wimp."
    jenny "No one wants to be checked out by a spineless little wimp!"

    if fast:
        show anon f_pouty
        pause
        anon e_sw f_horny @ -m_talk "..."
        jenny e_r "Ugh, gross!"
        show anon e_w -o_right
        hide jenny
        with dissolve.nowait
        pause
        return

    show anon e_osw f_sad
    pause
    jenny "If you had gotten up here to deal with this pipe situation sooner, perhaps I'd be in a better mood."
    jenny "But since you decided to take your sweet time, and clearly have no clue what you're doing..."
    jenny f_horny "... I think you should take this..."
    show anon e_w f_confused
    show jenny e_sw p_top_off_01
    pause
    show anon f_surprised
    show jenny p_top_off_02
    pause
    show anon a_surprised e_sw
    show jenny p_top_off_03
    with dissolve
    show jenny p_top_off_04
    pause
    show anon a_side e_w of_blush
    jenny a_shirt c_pants e_w f_annoyed -p_top_off_04 "... Downstairs to the wash for me."
    anon e_sw @ -m_talk "..."
    anon e_w f_horny "S-sure..."
    show anon a_shirt_jenny e_sw
    jenny a_hips f_angry m_teeth @ -m_talk "..."
    show anon e_w f_shocked m_open
    jenny "Stop staring and go... It's not gonna wash itself, dummy!"
    hide anon with dissolve
    pause
    jenny f_horny -m_teeth "Heh, I knew it!"
    jenny "That little loser totally has a thing for me!"
    $ renpy.end_replay()

    scene debbie_landing at stage with fade
    show anon a_shirt_jenny e_sw f_horny o_right at left with dissolve
    anon "Wow..."
    anon @ -m_talk "( I can't believe [saga.cast.jenny] actually took her top off in front of me... )"
    anon e_w f_horny_smug @ -m_talk "( Her breasts are so nice... )"
    hide anon with dissolve

    scene debbie_utility -debbie_basket at stage(.58, .538, 2)
    show debbie_utility debbie_basket as basket at stage(.58, .538, 2, b=0)
    with fade
    show anon a_shirt_jenny e_sw f_happy behind basket at pos(y=.85) with dissolve
    pause
    show anon a_reach e_s f_calm p_bend at pos(y=1.)
    pause
    show anon a_pocket e_sw f_happy -p_bend at pos(y=.85)
    anon @ -m_talk "( One soggy t-shirt, safely deposited in the laundry. )"
    anon e_nw f_pensive @ -m_talk "( Now, time to work out how to fix that pipe. )"
    hide anon with dissolve
    return


label deb04_bath.debbie:
    if saga.cast.debbie in saga.sets.debbie_kitchen:
        call shot.debbie_kitchen_island
    else:
        call shot.debbie_utility_laundry

    show debbie at right
    show anon o_right at left with dissolve
    debbie "Any progress on the sink, sweetie?"
    anon a_uneasy f_shy "I'm still working on it."
    debbie "Okie dokie."
    hide anon with dissolve
    return


label deb04_sink:
    scene mono debbie_bath_fix2
    mono "Tool in hand, I summoned all my manliness and got to work. The pipe proved a worthy opponent, but in the end I was able to torque my way around it." with fade
    mono "It felt good, proving I was capable of maintenance on the house, especially with [saga.cast.debbie] and [saga.cast.jenny] watching so intently. I think Dad would have been proud."

    scene debbie_bath at stage
    show anon at right
    show jenny a_fold f_annoyed o_right at pos(.42)
    show debbie a_clasp o_right at left
    with fade
    debbie "Hey, look... he did it!"
    show anon f_happy
    debbie @ f_happy "Great work, sweetie!"
    show anon f_pouty
    jenny "Yeah, and it only took him for-{i}ever!{/i}"
    show jenny e_e
    debbie @ f_sad "Don't be rude, [saga.cast.jenny]... If it wasn't for him, we'd be showering at the neighbors house from now on!"
    show jenny e_w
    anon a_fold f_smug "Heh, yeah [saga.cast.jenny]... you're welcome!"
    jenny @ e_r "Ugh, whatever."
    anon a_wtf f_calm "I was happy to do it."
    anon "And besides..."
    show jenny f_disgusted
    show debbie a_embarrassed f_elated
    anon a_point_self "... [saga.cast.jenny] was right when she said fixing stuff like this is my responsibility now."
    jenny @ -m_talk "..."
    show anon a_side f_shy of_blush
    debbie f_happy "Aww, I'm so proud of you!"
    show anon f_surprised
    show jenny e_e f_surprised
    debbie a_clasp "You're going to make some lucky girl a great husband one day!"
    show debbie f_curious
    jenny "Whoa, hold on now..."
    jenny f_annoyed "... Don't go giving him a big head!"
    show anon f_pouty -of_blush
    show debbie e_r f_bored
    jenny e_w f_horny "He's still a skinny little wimp, after all."
    anon "I am not a wimp!"
    show anon f_grumpy
    jenny "Hah, whatever, wimp!"
    debbie e_w f_calm "Don't listen to her, [saga.cast.anon]... She only teases you because she loves you."
    show anon e_b f_happy m_laugh
    jenny a_side f_annoyed -o_right "As if!"
    jenny @ e_r "Now can you two get out?"
    show anon e_w f_calm -m_laugh
    jenny "I am not waiting a second longer to use this shower!"
    show anon e_b f_happy m_laugh
    debbie "C'mon, [saga.cast.anon]... Let's get out of {i}Princess'{/i} way before her foul mood infects us."
    hide debbie
    hide anon
    with dissolve.nowait
    jenny f_horny "Hah, like calling me \"Princess\" is an insult!"
    return


label deb04_sink.bed2:
    call shot.debbie_bed2_door
    show anon f_worried o_right at pos(.55) with dissolve
    anon "[saga.cast.jenny]?"
    show anon f_surprised m_teeth
    jenny "Fix the bathroom sink, [saga.cast.anon]!!" with hpunch
    anon f_worried_surprised -m_teeth "I'm working on it!"
    hide anon with dissolve
    return


label deb04_sink.dark:
    scene debbie_bath at stage
    show anon o_right at pos(.55) with dissolve
    anon @ -m_talk "( It's a bit late in the day for that. )"
    anon @ -m_talk "( I'll come back tomorrow. )"
    hide anon with dissolve
    return


label deb04_sink.debbie:
    jump deb04_bath.debbie


label deb04_sink.item:
    scene debbie_bath at stage(.696, .696, 1.65, b=0)
    show anon a_tired e_s o_right p_bend at pos(.425) with dissolve
    anon @ -m_talk "( Hmmm... I'll need a wrench to fix this properly. )"
    anon @ -m_talk "( Pretty sure Consum-R in the mall sells stuff like that. )"
    hide anon with dissolve
    return


label deb04_sink.jenny:
    scene debbie_bed2 at stage
    show anon a_pocket e_nw f_pensive o_right at left with dissolve
    pause
    anon e_w f_disgusted @ -m_talk "( Yeah, no. )"
    anon @ -m_talk "( I really don't need {i}another{/i} reminder to fix the bathroom sink, thanks. )"
    hide anon with dissolve
    return


label deb04_sink.npc1:
    scene mono debbie_bath_fix2 -jenny
    mono "Tool in hand, I summoned all my manliness and got to work. The pipe proved a worthy opponent, but in the end I was able to torque my way around it." with fade
    mono "It felt good, proving I was capable of maintenance on the house, especially with [saga.cast.debbie] watching so intently. I think Dad would have been proud."

    scene debbie_bath at stage
    show anon at right
    show debbie a_clasp o_right at left
    with fade
    debbie "Hey, look... you did it!"
    show anon f_happy
    debbie @ f_happy "Great work, sweetie!"
    anon a_uneasy "Heh, yeah... I can't believe it."
    debbie "I only wish I could pay you for it."
    anon a_surrender f_shy "Oh, don't be silly, [saga.cast.debbie]..."
    anon "... I was happy to do it."
    anon a_point_self f_happy "And besides, fixing stuff like this is my responsibility now."
    show debbie a_embarrassed f_elated
    pause
    show anon a_side f_shy of_blush
    debbie f_happy "Aww, I'm so proud of you!"
    show anon f_surprised
    debbie a_clasp "You're going to make some lucky girl a great husband one day!"
    anon a_jaw_in e_sw f_shy "R-really, you think so?"
    debbie "Absolutely!"
    show anon a_side e_w
    debbie "Many women want someone who can take care of and provide for them."
    show anon f_confused
    debbie "Being handy around the house is a big part of that."
    anon f_worried -of_blush "Cool."
    show debbie at pos(.1) with dissolve.nowait
    debbie a_side f_calm -o_right "C'mon, we'd better clear out of here… [saga.cast.jenny] has been dying to take a proper shower."
    hide debbie with dissolve.nowait
    anon f_calm "Yeah, alright."
    hide anon with dissolve
    return


label deb04_sink.npc2:
    scene mono debbie_bath_fix2 -debbie
    mono "Tool in hand, I summoned all my manliness and got to work. The pipe proved a worthy opponent, but in the end I was able to torque my way around it." with fade
    mono "It felt good, proving I was capable of maintenance on the house, especially with [saga.cast.jenny] watching so intently. I think Dad would have been proud."

    scene debbie_bath at stage
    show anon f_happy at right
    show jenny a_hips f_annoyed o_right at pos(.4)
    with fade
    anon "Hey, I think I've done it!"
    anon a_point_back "Check it out."
    jenny "Yeah, great... it only took you for-{i}ever!{/i}"
    anon a_side f_grumpy "Seriously, [saga.cast.jenny]?!"
    anon "You can't even pretend to be grateful after I bust my butt fixing the sink that {i}you{/i} broke?"
    jenny a_upset f_angry m_teeth "Grr, I didn't-"
    pause
    jenny a_fold f_annoyed -m_teeth -o_right @ e_r "Tch, you are so annoying!"
    anon f_calm @ e_b f_happy m_laugh "Heh!"
    anon "C'mon, admit it..."
    anon "... I did a good job with my first project as man of the house."
    jenny a_wave_off o_right "Sure. Great. Whatever."
    jenny a_hips f_confused "Can I shower now?"
    anon f_tired "{i}*Sigh*{/i} Yeah, okay."
    show jenny a_side f_annoyed -o_right
    hide anon with dissolve.nowait
    anon "Enjoy, the hot water that {i}I{/i} got working for you!"
    show jenny e_s f_calm o_right
    pause
    show jenny e_r f_annoyed p_top_off_01
    anon "You're welcome!"
    return


label deb04_sink.solo:
    scene mono debbie_bath_fix2 -debbie -jenny
    mono "Tool in hand, I summoned all my manliness and got to work. The pipe proved a worthy opponent, but in the end I was able to torque my way around it." with fade
    mono "It felt good, proving I was capable of maintenance on the house. I think Dad would have been proud."

    scene debbie_bath at stage
    show anon a_surprised o_right p_stand_away at right
    with fade
    anon "And that should do it."
    anon a_cheer f_happy -o_right -p_stand_away @ e_b m_laugh "Fixed!"
    pause
    anon a_side f_pensive @ -m_talk "Hmm."
    anon "Kinda anti-climactic with nobody around to witness it."
    pause
    anon f_tired "{i}*Sigh*{/i} Oh, well... at least it's done."
    anon f_tired_happy "Good job me, I guess."
    hide anon with dissolve
    return


label deb04_quick:
    return


label deb04_quick.fence:
    scene debbie_bath at stage
    show anon e_sw o_right at pos(.55) with dissolve
    anon @ -m_talk "( Nothing left to do now but fix this sink. )"
    anon @ -m_talk "( Best get to it. )"
    hide anon with dissolve
    return


label deb04_wrench:
    return


label deb04_wrench.sink:
    scene debbie_bath at stage(.6, .425, 1.35, b=0)
    show anon e_sw f_pensive o_right with dissolve
    anon @ -m_talk "( I'll need a wrench to fix this properly. )"
    anon @ -m_talk "( They should sell them at Consum-R. )"
    hide anon with dissolve
    return


label deb04_wrench.take:
    anon "( Yeah, this should do for fixing that broken pipe. )"
    anon "( I hope the girls appreciate all the trouble I'm going through. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
