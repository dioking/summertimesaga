label jen05_jenny:
    call shot.debbie_dining_breakfast
    show jenny a_phone e_s f_annoyed p_table behind table
    show anon a_bowl_02 e_e f_shy p_table behind jenny with dissolve
    pause
    show anon a_bowl_01 e_s
    pause
    show anon a_eat f_calm m_bite
    pause
    show anon a_down e_e f_surprised v_chew -m_bite
    jenny "Oh, what the hell!"
    anon "What are you doing?"
    jenny @ -m_talk "..."
    jenny "I can't believe how fucking stupid these people are!"
    anon f_grumpy "Uhh, hello?!"
    jenny e_w "What?!"
    anon f_surprised "I asked what you are doing?"
    jenny e_r "Nothing."
    jenny e_w "Just, shut up and go away..."
    jenny "... Wimp."
    show jenny e_s
    anon f_grumpy "Ugh, fine."
    show debbie_dining_table pull3
    show anon a_pocket e_sw p_stand_far v_normal at pos(.6)
    with dissolve
    anon "I dunno why you have to be such a bitch, all the tim-"
    show anon f_surprised
    jenny e_nw "Wait a second!"
    anon f_confused @ -m_talk "..."
    jenny f_confused "What do you know about social media?"
    anon @ -m_talk "Huh?"
    anon "Why?"
    jenny e_s f_calm @ e_nw "Sit down."
    anon f_sceptical "... Okay."
    show debbie_dining_table -pull3
    show anon a_down e_e f_confused p_table at center
    with dissolve
    jenny "I made an account on this website where loser guys pay hot girls to post pictures of themselves."
    jenny a_phone_show e_w f_snide "I'm sure you've heard of it, you are a loser after all..."

    scene debbie_dining at stage(.35, .4, 5)
    show jenny_phone_sluttygram
    with fade
    anon "Sluttygram, seriously?!"
    anon "This is your bright idea for making money?"
    pause

    call shot.debbie_dining_breakfast
    show anon a_down e_e f_worried p_table behind table
    show jenny a_phone_show f_annoyed p_table behind table
    with fade
    jenny "So what if it is?!"
    jenny a_phone e_s "I'm hot enough to do something like this..."
    jenny e_r "... Way hotter than all of these little bitches!"
    jenny e_s "I should be making a killing on this site!"
    anon "Well, you're awfully full of yourself, aren't you?"
    jenny e_w f_snide "Pfft, says the guy who won't stop perving on me!"
    anon "Hmm, fair enough."
    anon "So what's the problem?"
    jenny e_s f_calm "The problem is, I've had this account active for a couple weeks now, and I've barely gotten any followers at all!"
    anon "Well, these things take time, you know?"
    anon "You don't just get a million followers overnight."
    jenny e_w "That's bullshit!"
    jenny "I don't have time to wait around, I need money now!"
    anon "Then maybe you should go back to Consum-R and-"
    jenny e_s f_annoyed "Seriously, look at all the followers this skank has!"
    pause
    jenny "And this one!"
    show jenny a_phone_show e_w with dissolve
    show anon f_surprised
    pause
    show jenny a_phone e_s with dissolve
    show anon f_worried
    jenny "... And oh my god, look at that one!"
    show jenny a_phone_show e_w
    anon f_calm "Oh ho, I'm looking."
    show anon f_surprised
    jenny "She looks like she fell out of the ugly tree and hit every branch on the way down..."
    anon f_calm "Mmm, I dunno... she looks pretty good to me!"
    jenny a_phone e_s "Tch, the only reason you're saying that is because her tits are hanging out..."
    anon @ f_worried "No!"
    pause
    anon "That's not... the only reason."
    anon "Though now that you mention it, all of those girls are posting way more provocative pictures than you are."
    jenny e_w f_snide "Provocative?"
    pause
    jenny "Don't you mean slutty?!"
    anon "Sure, okay."
    show jenny f_sad
    pause
    jenny "So, you think I should post some sluttier pictures?!"
    anon f_worried "No, I think you should get a regular job like a normal person."
    show jenny f_angry m_teeth
    pause
    jenny f_annoyed -m_teeth "No way, screw that!"
    jenny "Come with me."
    show debbie_dining_table pull2
    show jenny e_s p_table_rise
    anon "Huh?"
    hide anon
    show debbie_dining_table pull3 -chair1
    show debbie_dining_table chair1 as table
    show jenny b_old_anon p_table_drag
    anon "Where are we-"
    hide jenny
    with dissolve.nowait
    jenny "Shut up and come on."

    label jen05_jenny.cookie hide:
    scene debbie_bed2 -jenny at stage
    with fade
    show old_anon 12 at old_left
    show jenny a_fold at right
    with dissolve
    anon "What the heck are we doing?!"
    show old_anon 90
    jenny a_camera_give f_annoyed "{i}We're{/i} taking some dirty pictures for my dumb Sluttygram account, so more horny losers will subscribe to my feed!"
    show old_anon 728b
    show jenny a_hips
    with dissolve
    anon "When did you get a digital camera?!"
    show old_anon 728
    jenny "None of your business, wimp."
    show old_anon 728b
    anon "Is that what you spent my money on?!"
    hide jenny
    with dissolve

    scene debbie_bed2_bed -laptop with fade
    show jenny a_knot_01 e_s p_bed_sit with dissolve
    jenny @ -m_talk "..."
    show jenny a_knot_02 c_casual_tied
    anon "[saga.cast.jenny], this is stupid!"
    anon "Why don't you just go back up to Consum-R and ask if you can have your old job back?!"
    show jenny a_down
    anon "I'm sure they'll-"
    show jenny p_bed_sit_lean
    anon "They'll-"
    jenny a_pants_up e_c f_confused_snide "There. How's that?"
    anon @ -m_talk "..."
    anon "You know, on second thought..."
    anon "... I think the Sluttygram idea is marvelous and I'm fully on board with this plan now."
    jenny f_snide "Heh, just shut up and take the pictures, loser!"

    label jen05_jenny.photo1:
    call mini.camera ('01', _return[-1] if type(_return) is tuple else 1.3)

    scene mini camera 01 onlayer aux at mini_camera_snap(*_return)

    scene debbie_bed2_bed -laptop
    show jenny a_down c_casual_tied e_c f_confused_snide p_bed_sit_lean
    show debbie_bed2_bed camera view as camera
    with fade
    jenny "How did that look?"
    jenny f_snide "It's hot, right?"

    menu:
        "Yeah!":
            $ renpy.dynamic(what={'01': _return})
        "Not really.":

            anon "It's umm... kinda?"
            jenny f_annoyed "What the fuck does that even mean, [saga.cast.anon]?!"
            show jenny e_s
            pause
            jenny a_pants_up e_c "Do it again and this time make it hot!"
            jump jen05_jenny.photo1

    anon "Y-yeah, really hot."
    jenny "My next pose is gonna be even better!"
    anon "This is awesome."

    label jen05_jenny.photo2:
    call mini.camera ('02', _return[-1])

    scene mini camera 02 onlayer aux at mini_camera_snap(*_return)

    scene debbie_bed2_bed -laptop
    show jenny c_casual_tied_up e_c f_confused_snide p_bed_sit_twist_turn
    show debbie_bed2_bed camera view as camera
    with fade
    jenny "How was that?"

    menu:
        "Great!":
            $ what['02'] = _return
        "I can do better.":

            anon "Ehh, lemme try again."
            jenny f_annoyed "We're not doing this so you can oogle at my tits, [saga.cast.anon]!"
            jenny "Focus!"
            jump jen05_jenny.photo2

    anon "Looks great!"
    jenny f_snide "Let's try something a little more refined."
    jenny "I bet those losers will loooove that."

    label jen05_jenny.photo3:
    call mini.camera ('03', _return[-1])

    scene mini camera 03 onlayer aux at mini_camera_snap(*_return)

    scene debbie_bed2_bed -laptop
    show jenny c_casual_tied_up e_c f_confused_snide p_bed_lay_side
    show debbie_bed2_bed camera view as camera
    with fade
    jenny "Looks real classy, right?"
    anon "Huh?"
    jenny f_calm "The pose, it's like one those old pin-up models would use."

    menu:
        "Sure?":
            $ what['03'] = _return
        "Well...":

            anon "I wouldn't call it classy, exactly..."
            jenny f_annoyed "Ugh, then you fucked up because I'm absolutely nailing this pose!"
            anon "Shouldn't I just focus in on your naughty bits?"
            jenny @ f_disgusted "Umm, no..."
            jenny "... It's about the whole package, you lemon!"
            jump jen05_jenny.photo3

    anon "Uhh, yeah... sure?"
    jenny f_annoyed "I'm trying to make it look professional, [saga.cast.anon]!"
    anon "Oh relax, it looks great, perfect."
    jenny f_snide "Of course it's perfect, I'm perfect."

    label jen05_jenny.photo4:
    call mini.camera ('04', _return[-1])

    scene mini camera 04 onlayer aux at mini_camera_snap(*_return)

    scene debbie_bed2_bed -laptop
    show jenny c_casual_tied e_c f_confused_snide p_bed_leapfrog_away_turn
    show debbie_bed2_bed camera view as camera
    with fade
    jenny "We good?"

    menu:
        "Yup.":
            $ what['04'] = _return
        "Try again.":

            anon "I think the lighting could be better..."
            show jenny f_disgusted
            anon "... Don't move."
            jenny "Seriously?!"
            jenny f_annoyed "How hard is it to take a picture of my ass?"
            jump jen05_jenny.photo4

    anon "Yeah, that's really sexy."
    jenny f_calm "Lemme see!"
    hide jenny with dissolve

    scene onlayer aux
    with hold.aux

    scene debbie_bed2 -jenny at stage
    show anon a_camera_look e_sw f_happy o_right at left
    with fade
    show jenny a_hips c_casual_tied at pos(.6) with dissolve
    show anon a_side e_w
    jenny a_camera e_s @ -m_talk "..."
    jenny "Oh yeah, if this doesn't bring in the followers, nothing will."
    jenny e_w f_snide "Those other skanks are about to learn what real hotness looks like!"
    show jenny e_ssw
    pause
    anon f_calm @ e_sw "I think you ruined your shirt..."
    jenny e_w f_confused "Huh?"
    jenny e_ssw f_snide "Yeah, whatever. I've got more shirts."
    pause
    jenny e_w f_annoyed "Why are you still here?!"
    anon f_sceptical "What do you mean?"
    show anon f_worried
    jenny "I mean, get out."
    jenny "I'm done with you."
    anon f_sceptical "What the hell, I thought we were-"
    jenny f_angry m_teeth "Goodbye, perv!"
    anon @ -m_talk "..."
    anon e_osw f_sad "{i}*Sigh*{/i}"
    hide anon with dissolve
    show jenny e_ssw f_snide -m_teeth
    pause
    jenny e_b f_calm m_laugh @ -m_talk "Damn, I'm sexy!"
    $ renpy.end_replay()

    call shot.debbie_bed2_door
    with fade
    show anon a_pocket with dissolve
    anon @ -m_talk "( I can't believe that just happened. )"
    anon @ -m_talk "( She was actually being kind of cool for a few minutes there. )"
    anon e_b f_happy m_laugh @ -m_talk "( And then she practically stripped for me! )"
    pause
    anon e_w f_worried -m_laugh @ -m_talk "( Too bad she went back into bitch mode after I took the pictures... )"
    anon f_calm @ -m_talk "( Oh well. )"
    pause
    anon a_think e_nw f_pensive @ -m_talk "( I wonder if I can get a copy of those photos somehow? )"
    hide anon
    with dissolve
    return what
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
