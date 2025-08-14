label jen13_intro:
    scene debbie_bed3 at stage
    show anon a_pocket f_horny o_right at left with dissolve
    anon @ -m_talk "( I haven't checked [saga.cast.jenny]'s CAMslut profile in a while... )"
    anon @ -m_talk "( I wonder if she's saved any new videos? )"
    hide anon
    with dissolve
    return


label jen13_camslut:
    scene jenny_laptop
    anon "( Dang it! )"
    pause
    anon "( Not a single new video... )"
    pause
    anon "( It says she was online yesterday... I wonder why she's not saving her new shows? )"

    scene debbie_bed3 at stage
    show anon a_think e_nw f_pensive o_right
    with fade
    anon @ -m_talk "( Hmm, maybe there's a limit to how many she can save? )"
    anon @ -m_talk "( That would make sense, the saved ones are mostly promotional after all... )"
    anon @ -m_talk "( Just another way to draw in more subscribers. )"
    pause
    anon a_pocket e_b f_happy m_teeth @ -m_talk "( I bet if I bought her a new toy she'd make a new video! )"
    anon @ -m_talk "( Didn't she mention one named Bad Monster in her diary? )"

    if saga.prop.toy_monster in saga.cast.anon:
        anon e_w f_horny -m_teeth @ -m_talk "( I should see if she wants the one I got from Pink! )"
    else:
        anon @ -m_talk "( I should go to Pink and get one for her! )"

    hide anon
    with dissolve
    return


label jen13_shop:
    scene toy_shop at stage
    show anon a_pocket o_right with dissolve
    anon @ -m_talk "( Alright, I'm looking for a toy called Bad Monster for [saga.cast.jenny]. )"
    anon @ -m_talk "( It's gotta be here somewhere. )"
    hide anon
    with dissolve
    return


label jen13_monster:
    return


label jen13_monster.take:
    scene toy_shop -toy_monster at stage
    show anon a_toy_badmonster e_sw f_worried o_right at left with dissolve
    anon @ -m_talk "( This thing is scary! )"
    anon @ -m_talk "( I hope [saga.cast.jenny] likes it... )"
    hide anon
    with dissolve
    return


label jen13_jenny:
    scene debbie_bed2_bed -laptop at stage
    show jenny a_phone_talk e_b m_laugh p_lay_reading
    jenny @ -m_talk "Can you believe that?!"
    pause
    jenny e_w f_happy -m_laugh "Yeah, I told him how much money it was bringing in, but he's being a little bitch about it!"
    pause
    jenny "No, he won't do it."
    jenny @ e_b f_calm m_laugh "Haha! Yeah, I know!"
    pause
    jenny "I dunno, I'll find someone eventually..."
    show anon a_pocket o_right at pos(.25, .838) with dissolve
    jenny f_annoyed "!!!"
    jenny a_phone_cover "I'm on the phone!"
    anon "I got you something."
    jenny f_surprised "Huh?"
    show jenny f_angry m_teeth
    anon "A present."
    jenny f_annoyed -m_teeth "You bought me something?"
    anon "Yes."
    jenny "Was it expensive?"
    anon @ a_think e_nw f_pensive -m_talk "..."
    anon "Yes."
    jenny a_phone_talk f_happy "[saga.cast.jane], I'm gonna have to call you back."
    pause
    jenny "Haha, yeah... I'm sure they would love that."
    pause
    jenny "I'll keep that in mind..."
    jenny "You're such a slut!"
    pause
    jenny e_b f_calm m_laugh @ -m_talk "Haha, bye!"
    show jenny a_down e_w f_annoyed p_bed_sit -m_laugh
    pause
    jenny "Okay, this had better be good."
    show anon a_backpack e_s
    pause
    show anon a_toy_badmonster e_w
    jenny f_surprised "!!!" with hpunch
    jenny "I-is that a Bad Monster?!"
    anon "Yup."
    jenny "How did you-"
    jenny f_annoyed "Why did you buy this for me?!"
    anon "Well, you-"
    jenny f_angry m_teeth "Did you read my diary?!"
    anon f_surprised "W-what?"
    anon f_worried "No!"
    anon "You just had me buying sex toys for you and I heard this was the best one and..."
    pause
    anon f_sceptical "I didn't read your diary! Sheesh!"
    jenny "You better not have!"
    jenny "Give me that!"
    show jenny a_toy_monster e_ssw f_snide -m_teeth
    show anon a_pocket f_worried
    pause
    jenny "It's awesome..."
    show anon f_horny
    jenny "They're gonna go nuts for this!"
    anon "Who's gonna-"
    jenny e_w f_annoyed "Hmm?"
    jenny "Oh, uhh... Nobody!"
    jenny "Just, shut up and get out!"
    anon f_grumpy "You're not even gonna say thank you?"

    if saga.cast.jenny.dom < saga.cast.jenny.sub:
        jenny e_r "Ugh, thank you."
        show jenny e_w
        anon a_uneasy f_calm "You're welcome."
    else:

        jenny e_r "Uhh, no?"
        jenny e_w "I know there's probably some creepy motive behind this..."
        anon a_uneasy f_worried "No there's not!"
        anon "Can't I just do something nice for you?"
        jenny "Yeah right, whatever."

    jenny f_angry m_teeth "Now get out!"
    anon a_pocket e_osw f_sad "{i}*Sigh*{/i} Fine."
    hide anon
    with dissolve
    pause
    jenny e_ssw f_snide -m_teeth "Hehehehehe!"

    scene debbie_landing at stage
    with fade
    show anon a_pocket f_grumpy o_right at left with dissolve
    anon @ -m_talk "( Typical bitchy result... )"
    pause
    anon e_b f_happy m_teeth @ -m_talk "( Oh well, maybe she'll make another video for her CAMslut profile! )"
    anon @ -m_talk "( I'll just have to wait and check it in the morning. )"
    hide anon
    with dissolve
    return


label jen13_videos:
    scene jenny_laptop
    anon "( It worked, she saved a new video! )"
    return


label jen13_watch:
    anon "( Holy crap! )"
    pause
    anon "( Totally worth it. )"
    anon "( That was awesome! )"
    return


label jen13_watch.rails:
    scene jenny_laptop
    anon "( Dude, you're here for the porn. Click the porn! )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
