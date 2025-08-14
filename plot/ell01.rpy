label ell01_intro:
    scene camera at stage
    show anon a_surprised f_surprised with dissolve
    anon @ -m_talk "( What on earth is- )"
    anon @ -m_talk "..."
    anon f_shy @ -m_talk "( Well obviously I need to introduce myself, right? )"
    hide anon with dissolve
    return


label ell01_ella:
    scene forest_woods1 -ella at stage(.188, .476, 2.67)
    show ella p_bend at pos(.775)
    pause
    show anon a_wave e_wsw o_right at pos(.1) with dissolve.nowait
    anon "H-hi there-"
    show anon e_w f_surprised
    ella f_surprised p_rear "Eeep!"
    show ella p_rear_turn at center
    pause
    show ella p_run_away
    pause
    hide ella with dissolve

    scene mono forest_ella_run
    mono "Before I could get out another word, the mysterious quadruped had bolted across the clearing and was already rapidly vanishing into the undergrowth." with fade

    scene forest_woods1 -ella at stage(.188, .476, 2.67)
    show anon a_wave f_surprised o_right at pos(.1)
    with fade
    anon @ -m_talk "..."
    pause
    anon a_rub f_confused "Huh."
    pause
    anon f_shy @ -m_talk "( Well, still not the worst reaction anyone's ever had to meeting me, I guess. )"
    hide anon with dissolve
    return


label ell01_ella.rails:
    scene camera at stage
    show anon f_pouty with dissolve
    anon @ -m_talk "( Oh right, because I'm {i}not{/i} going to try take this opportunity to meet whoever she is. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
