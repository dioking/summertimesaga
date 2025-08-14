label jen11_intro:
    scene debbie_bed3 at stage
    show anon a_think e_nw f_pensive o_right with dissolve
    anon @ -m_talk "( Hmm, there has to be some way I can figure out what [saga.cast.jenny] is doing for that money? )"
    pause
    anon a_pocket e_w f_calm @ -m_talk "( She might have written something down in that diary of hers... )"
    anon @ -m_talk "( I just have to wait until she's showering and then I can sneak into her room again and check it. )"
    hide anon
    with dissolve
    return


label jen11_diary:
    return


label jen11_diary.bath:
    call shot.debbie_bath_peek
    show jenny c_naked_wet p_shower_legs s_1 behind glass
    show layer master at blur(20)
    pause
    show layer master
    with dissolve
    anon "( Okay, cool... she's in the shower. )"
    anon "( It's the perfect time to see what she's been writing in her diary. )"
    return


label jen11_react:
    scene debbie_bed2 at stage
    show old_anon 23 with dissolve
    anon "Whoa!!"
    anon "[saga.cast.jenny] is masturbating for men over the internet?!"
    anon "She's completely lost her mind!"
    anon "[saga.cast.debbie] would totally freak if she found out about this..."
    show old_anon 22
    pause
    show old_anon 35
    anon "I wonder if I can sneak a peek at this somehow?"
    show old_anon 34
    pause
    show old_anon 35
    anon "... Maybe I can find some stuff on her laptop?"
    hide old_anon
    with dissolve
    return


label jen11_laptop:
    scene jenny_laptop
    anon "( I need her password! )"
    pause
    anon "( \"My favorite toy...\" )"
    anon "( Didn't she mention something about a toy in her diary? )"

    if saga.time.dark:
        jenny "Damnit, where the hell is my hair straightener?!"
    else:
        jenny "[saga.cast.debbie], have you seen my hair straightener?!"

    scene debbie_bed2 at stage
    show old_anon 22
    with fade
    anon "( Oh crap, it sounds like [saga.cast.jenny] is done with her shower! )"

    if saga.cast.debbie in saga.zone.debbie_inside and not saga.time.dark:
        debbie "No, sweetie."
        jenny "Well, I can't find it!"

    anon "( I'd better get out of here! )"
    hide old_anon
    with dissolve

    call shot.debbie_bed2_door
    with fade
    show old_anon 11 at pos(.6) with dissolve
    pause
    show old_anon 11 at pos(.3) with dissolve
    pause
    show jenny a_hips c_towel f_annoyed at right with dissolve.nowait
    jenny "Did you just come out of my room?!"
    show old_anon 10 at face_right with dissolve.nowait
    anon "Huh?"
    anon "No..."
    show old_anon 5
    show jenny f_angry m_teeth
    pause
    show old_anon 6 with dissolve
    anon "Please don't hit me with the hair dryer again!"
    jenny e_r f_annoyed -m_teeth "Ugh, just get out of my way, loser!"
    hide jenny
    with dissolve
    pause
    show old_anon 37 with dissolve
    anon "( Phew, that was close! )"
    pause
    show old_anon 5 with dissolve
    anon "( Who knows how long it will take me to find naughty stuff on her laptop... )"
    anon "( I should only attempt this when I know I'll have plenty of time to snoop around. )"
    pause
    show old_anon 4 with dissolve
    anon "( Maybe at night, when she's sleeping? )"
    pause
    show old_anon 17 with dissolve
    anon "( I'll have to be careful but I think it's worth a shot. )"
    hide old_anon
    with dissolve
    return


label jen11_laptop.rails:
    scene debbie_bed2 at stage
    show anon a_think e_sw f_pensive with dissolve
    anon @ -m_talk "( Maybe I should check her laptop hefore I leave. )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
