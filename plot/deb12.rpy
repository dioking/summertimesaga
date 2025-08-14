label deb12_intro:
    scene debbie_bed3 at stage
    show anon a_think e_nw f_pensive with dissolve
    anon @ -m_talk "( Maybe I could speak with [saga.cast.debbie] about my weird dreams. )"
    anon @ -m_talk "..."
    anon a_pocket e_w f_shy @ -m_talk "( I just have to find a way to ease into it without making things awkward. )"
    hide anon with dissolve
    return


label deb12_debbie(busy):
    anon f_worried "Hey, umm... [saga.cast.debbie]?"
    debbie "Yes, sweetie?"
    anon "Could I ask you something?"
    debbie "Of course, you can ask me anything."
    anon a_shy_neck e_s "Well, it's kinda... embarrassing."
    debbie f_curious "Embarrassing?"
    show anon e_w
    debbie "There's no need to feel that way..."
    show anon f_shy
    debbie f_calm "... Not with me, sweetie."
    anon a_side "Okay."

    menu:
        "Weird dreams.":
            pass
        "Nothing.":

            jump deb12_debbie.bail

    anon f_worried "I've been having these, well... umm..."
    show anon e_s f_confused
    pause
    anon e_w f_worried "... I guess, let's just call it anxiety... recently."
    debbie f_curious "Anxiety?"
    debbie "About what, sweetheart?"
    show debbie f_surprised
    anon a_behind_held e_s "Ehh, well... S-sex stuff, I guess."
    debbie "Oh."
    show debbie f_sad
    anon "Yeah."
    pause
    anon "Maybe it's just because I'm so inexperienced or something but I just-"
    debbie f_curious "You're worried girls might make fun of you if you disappoint them?"
    anon f_confused "Uhh..."
    anon e_w "... Y-yes?"
    show anon f_worried
    debbie f_shy "I understand, sweetie."
    debbie "That's a perfectly natural thing for people your age to worry about..."
    show anon f_shy
    debbie "... And rest assured that any girl who would make fun of you for something as small as that isn't worth your time or effort."
    anon a_side "Right, yeah..."
    anon "... Totally."
    pause
    anon f_worried "B-but these, umm... anxieties..."
    anon a_pocket e_s "... They've kinda been affecting my sleep recently, and I was hoping there was maybe some... advice you could give me?"
    show debbie f_curious
    anon e_w f_shy "Or maybe some pointers?"
    debbie "What kind of pointers?"
    anon @ e_s "I dunno, like..."
    anon a_point_pocket "... Remember the other day at the mall?"
    show debbie f_sad
    anon @ -m_talk "..."
    debbie "... Yes?"
    label deb12_debbie.cookie hide:
    anon a_rub "I was hoping... maybe you could teach me more, you know... about kissing?"
    debbie @ -m_talk "..."
    anon "I mean, it might help me out... with the anxiety."
    debbie "Sweetie, the other day was a mistake... I should never have suggested-"
    anon a_side "I know, and I'm really sorry about that... it's just..."
    show debbie f_surprised
    show anon a_palm at pos(.325)
    with dissolve.nowait
    anon "... You're so good at kissing and I imagine you could teach me a lot about what women like, ya know?"
    debbie f_curious "Hmm, well, I could maybe explain to you what women like..."
    show anon a_side
    label deb12_debbie.merge:
    debbie f_shy "... But I don't think showing you is a good idea, given all that's happened recently."

    if saga.cast.anon.chr < 5 or busy:
        jump deb12_debbie.fail

    anon "Aww, c'mon [saga.cast.debbie]!"
    show debbie f_surprised
    anon a_wtf f_calm "You're the one who said I need to get out and start dating."
    anon "It would definitely help if I knew how to kiss a girl properly, wouldn't it?"
    debbie f_sad "I-"
    pause
    $ renpy.notify('{chr} check passed.')
    show anon a_side f_happy
    debbie f_shy "I suppose, so long as it's purely educational..."
    anon f_calm "Yeah, absolutely!"
    show debbie a_mug e_wsw p_twist_turn
    anon a_point f_shy "One hundred percent educational."
    debbie a_nervous e_w p_stand "{i}*Sigh*{/i} Alright, but let's be quick about it."
    anon a_side f_happy "Sweet, thank you!"
    show anon e_sw
    debbie a_gimme oa_hand "Come here."
    show anon a_handshake e_w f_calm at pos(.535)
    show debbie f_surprised z_oa
    show mimic debbie at pos.debbie
    with dissolve.nowait
    anon "L-like this?"
    debbie f_shy "Good. Now, lean in."
    hide anon
    hide mimic
    show debbie b_anon oa_none p_peck s_800ms z_reset
    with dissolve.nowait
    pause
    debbie "... Mhmm."
    pause
    debbie "Mmm."
    show anon f_shy o_right at pos(.535)
    show debbie a_side f_horny of_blush p_stand -b_anon
    with dissolve.nowait
    pause
    anon "How was that?"
    debbie a_embarrassed f_shy "{i}*Ahem*{/i} F-fine."
    debbie "See, you're got nothing to worry about, sweetie."
    show debbie a_clasp f_curious
    anon f_confused "Okay, but do you have any tips?"
    anon "You know, to like... really wow them?"
    debbie e_nw f_pensive of_none "Well, let's see..."
    pause
    show anon f_shy
    debbie a_side e_w f_happy "Oh, I know!"
    show anon f_happy
    debbie @ f_calm "Kiss me again and I'll show you a little trick I learned in college!"
    anon "Alright."
    hide anon
    show debbie b_anon p_kiss
    with dissolve.nowait
    pause
    debbie "Mmm."
    show jenny a_fold f_disgusted o_right at left with dissolve.nowait
    pause
    jenny "Eugh!"
    show anon a_surprised f_surprised at pos(.55)
    show debbie a_surprised f_surprised of_blush p_stand -b_anon
    with none.nowait
    anon @ -m_talk "( !!! )" with hpunch
    jenny "What the fuck are you two doing?"
    debbie "N-no, nothing... we were just, umm..."
    anon f_worried "Uhhh."
    jenny "You're kissing each other on the mouth now?!"
    anon a_calm_down f_shy "What?! No, that's... crazy talk!"
    show debbie a_side f_calm
    anon "[saga.cast.debbie] was just, umm..."
    show anon e_nw f_pensive
    debbie f_curious @ -m_talk "..."
    show debbie a_facepalm e_b f_sad
    anon a_finger e_w f_smug "... Checking me for tonsillitis!"
    pause
    jenny f_confused "She was checking you... for tonsillitis."
    anon a_side "Uh huh."
    show anon f_happy o_right
    pause
    show anon f_worried
    pause
    show anon o_left
    jenny f_annoyed "That's the most pathetic thing I've-"
    show anon f_worried_surprised
    show debbie a_clasp e_s
    jenny a_wave_off e_r "Eugh, whatever. I don't care."
    show anon o_right at pos(.575)
    show jenny a_surprised e_w at pos(.925)
    with dissolve.nowait
    jenny "So fucking weird!"
    hide jenny with dissolve.nowait
    anon f_worried "Really, [saga.cast.jenny] it's not what you think."
    jenny "What part of, \"I don't care.\" did you not understand?"
    $ renpy.end_replay()
    debbie a_side e_w o_right of_none "Would you stop it please, I was just trying to help [saga.cast.anon] out with some anxiety he's been feeling."

    if saga.cast.anon in saga.sets.debbie_kitchen:
        show jenny a_juice f_confused at pos(.925) with dissolve.nowait
        jenny "Oh, by sucking face in the kitchen?!"
    else:

        show jenny a_towel f_confused at pos(.925) with dissolve.nowait
        jenny "Oh, by sucking face in the basement?!"

    jenny f_annoyed @ e_r "'Cause that makes a lot of sense."
    show anon o_left behind debbie at pos(.535)
    show debbie a_clasp e_s o_left at pos.anon.touch_face
    show jenny at pos(.2)
    with dissolve.nowait
    debbie "I didn't think-"
    jenny o_right "Seriously, Mom... Just-"
    show anon f_annoyed
    jenny f_disgusted "Eww."
    show debbie e_w f_surprised
    hide jenny
    with dissolve.nowait
    anon a_whisper "Do you have to be such an unsufferable bitch about {i}*literally*{/i} everything?!"
    debbie f_sad "Don't call her that, [saga.cast.anon]."
    anon a_side f_confused o_right "But-"
    debbie "She's not wrong."
    debbie "You and I shouldn't be doing stuff like this, sweetie."
    debbie "It's very inappropriate."
    anon e_osw f_sad "{i}*Sigh*{/i} I know... It's just-"
    anon e_w f_worried "I'm sorry, [saga.cast.debbie]."
    debbie f_shy "No, it's my fault."
    debbie "I'm the adult here and I shouldn't have let things get so out of hand."
    anon "I don't want you to feel like it's all on you though!"
    show anon f_shy
    debbie a_touch_anon_face "Aww."
    debbie f_calm "Then we'll both have to try harder going forward, hmm?"
    debbie "See that everything gets back on track around here and functioning normally."
    anon "Y-yeah, I guess."
    debbie a_side "That's my boy."
    debbie "Now run along and do something productive, okay?"
    debbie "I've got a lot to get done."
    anon f_calm "Do you want help?"
    debbie "Nah, I've got it."
    hide anon with dissolve
    return True


label deb12_debbie.bail:
    anon "Actually..."
    anon a_calm_down "... Never mind."
    debbie f_curious "Are you sure?"
    show anon a_pocket
    debbie f_sad "I'd like to think you can talk to me about anything, [saga.cast.anon]."
    anon "Yeah, nah... it's nothing."
    anon "Sorry to bug you."
    debbie f_shy "You never bug me, sweetie."
    hide anon with dissolve
    return


label deb12_debbie.fail:
    anon a_point_self "I'm really better at learning by doing... You know?"

    if not busy:
        $ renpy.notify('Insufficient {chr}!')

    debbie "Well, maybe try one of the girls at your school then?"
    show anon f_worried
    debbie "I bet some of them would be willing to practice kissing with you."
    anon a_side e_osw f_sad "{i}*Sigh*{/i} Y-yeah, maybe."
    debbie "You'll never know unless you try, sweetie."
    anon a_wave e_w "Yeah, thanks."
    hide anon with dissolve
    return False


label deb12_retry(busy):
    anon f_confused "Are you certain we can't practice kissing a bit?"
    debbie f_shy "Tsk, this again?"
    anon f_shy "You're just so good at it and I really think it would help me feel more confident."
    debbie "I can try explaining some things to you..."
    jump deb12_debbie.merge
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
