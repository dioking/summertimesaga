label jen12_setup:
    return


label jen12_setup.block:
    call shot.debbie_bed2_door
    show anon a_think e_nw f_pensive o_right with dissolve
    anon @ -m_talk "( Eh, I think I've pushed my luck enough for now. )"

    if saga.time.dark:
        anon @ -m_talk "( Perhaps tomorrow night after she falls asleep would be a good time. )"
    else:
        anon @ -m_talk "( Perhaps later after she falls asleep would be a good time. )"

    hide anon with dissolve
    return


label jen12_bed2:
    scene debbie_bed2 at stage
    show anon a_pocket f_surprised o_right at left with dissolve
    anon @ -m_talk "( Alright, I've gotta be quiet here... )"
    anon @ -m_talk "( I just need to log into her laptop and find her CAMslut stuff. )"
    anon f_horny_smug @ -m_talk "( Easy peasy. )"
    hide anon with dissolve
    return


label jen12_bed2.wait:
    call shot.debbie_bed2_desk
    show anon a_computer p_bend_away with dissolve
    anon "( Hmm... Let's see if she left her computer on. )"
    anon "( I wonder what I could find on here... )"
    show jenny a_fold e_wsw f_angry m_teeth at right

    if saga.cast.jenny in saga.sets.debbie_bath:
        show jenny c_casual_towel

    with dissolve.nowait
    pause
    jenny @ -m_talk "..."
    jenny "Can I help you with {i}something{/i}??!" with hpunch
    show jenny e_w
    anon a_surprised f_shocked m_open o_right -p_bend_away @ -m_talk "!!!"
    show jenny f_disgusted -m_teeth
    anon a_uneasy f_shy -m_open "Sorry!! I was just... Trying to see if your internet is working!!"
    anon "I can't seem to connect on my computer..."
    jenny "Don't fucking {i}touch{/i} my computer!!"
    show anon a_pocket e_s f_calm
    jenny "Just ask me next time."
    anon e_osw f_sad "Of course!"
    show anon e_w f_surprised m_teeth
    jenny f_angry m_teeth "Now, get out of my room!!!"
    hide anon with dissolve
    return


label jen12_auth:
    scene jenny_laptop
    anon "( Got it! )"
    anon "( Alright, now let's see what she's been up to... )"
    return


label jen12_camslut:
    scene jenny_laptop
    anon "( Here it is. )"
    pause
    anon "( Ugh, her profile is awful... )"
    anon "( Twenty-two-year-old goddess? Haha! )"
    pause
    anon "( Oh, there's a videos tab! )"
    return


label jen12_camslut.rails:
    scene jenny_laptop
    anon "( Can't give up now, I should investigate that CAMslut icon. )"
    return


label jen12_videos:
    scene jenny_laptop
    anon "( She's got two videos saved here! )"
    pause

    if saga.cast.jenny in saga.sets.debbie_bed2:
        anon "( I can't watch these in her room though... she might wake up! )"
    else:
        anon "( I can't watch them now though... it's too easy to get caught! )"

    pause
    anon "( Maybe there's some way to connect her computer to mine? )"
    pause
    anon "( Hmmm... I think I remember reading something about this on Seddit. )"
    anon "( If I just... hold the alt key... and tap F4... )"




    label jen12_videos.merge:
    call mini.hack

    if not _return:
        jump jen12_videos.fail

    call shot.debbie_bed2_desk
    show anon a_cheer e_b f_happy m_teeth
    with fade
    anon @ -m_talk "( I think I did it! )"
    anon @ -m_talk "( Now I should be able to view her CAMslut profile on my computer. )"
    anon a_pocket e_w f_horny_smug -m_teeth @ -m_talk "( I can't wait to check out those videos! )"
    hide anon with dissolve
    return True


label jen12_videos.fail:
    call shot.debbie_bed2_desk
    show anon a_surprised_up e_sw f_worried_surprised
    with fade
    anon @ -m_talk "( What the... It booted me out! )"
    anon a_side e_osw f_sad @ -m_talk "( I almost had it too. )"

    if saga.cast.jenny not in saga.sets.debbie_bed2:
        anon @ -m_talk "( Well nothing more I can do here for now. )"
        hide anon with dissolve
        return

    jenny "{i}*Snort*{/i}"
    anon a_surprised_up_both e_w f_surprised m_teeth o_right @ -m_talk "( Oh, crap! )"
    jenny "Mmm, that'll cost you... {i}*yawn*{/i} four hundred... {i}*zzz*{/i}..."
    anon f_worried_surprised -m_teeth @ -m_talk "( She's stirring! )"
    pause
    anon @ -m_talk "( I gotta get out of here! )"
    hide anon
    with dissolve

    call shot.debbie_bed2_door
    with fade
    show anon a_rub e_e f_shy with dissolve
    anon @ -m_talk "( Phew, that was close! )"
    anon e_w @ -m_talk "( I'll just have to try again tomorrow... )"
    anon a_think e_nw f_pensive @ -m_talk "( If only I knew my way around computers a bit more... )"
    hide anon with dissolve
    return


label jen12_videos.rails:
    scene jenny_laptop
    anon "( I can't {i}not{/i} check that videos tab... I'd never forgive myself! )"
    return


label jen12_reset:
    return


label jen12_reset.bed2:
    call shot.debbie_bed2_door
    show anon a_calm_down f_surprised m_teeth o_right with dissolve
    anon @ -m_talk "( Nope. That was more than enough for now. )"
    anon @ -m_talk "( I'll try again once my cortisol levels have returned to normal. )"
    hide anon with dissolve
    return


label jen12_retry:
    scene jenny_laptop
    anon "( I can't risk watching these in her room... )"
    anon "( ... I know, I'll try to set up remote access again. )"
    pause
    anon "( Okay, same as last time... hold down alt... and tap... and... )"


    jump jen12_videos.merge


label jen12_watch:
    anon "( Man, I hope she makes more videos! )"
    return


label jen12_watch.rails:
    scene jenny_laptop
    anon "( No way! I worked too hard to access those videos, now queue 'em up! )"
    return


label jen12_watch.vid1:
    anon "( That was pretty hot! )"
    return


label jen12_watch.vid2:
    anon "( Wow, did she squirt?! )"
    anon "( I can see how she's making money doing this... )"
    pause
    anon "( ... Also, \"a real penis\"? )"
    anon "( Was she talking about fucking someone on camera?! )"
    anon "( Surely she wouldn't go that far, would she? )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
