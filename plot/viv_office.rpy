label viv_office:
    hide anon
    show old_anon 13 at old_right
    show old_viv 29
    viv "So, would you like some wine or is it straight to the lovemaking?"
    show old_viv 28
    show old_anon 26
    anon "Lovemaking, please."
    show old_anon 13
    show old_viv 29
    viv "Dieu merci!"
    show old_viv 31 with dissolve.nowait
    viv "Hehe!"
    show old_anon at face_right
    hide old_viv
    with dissolve

    scene school_office5_desk
    show old_viv 33
    with fade
    show old_anon 13 at old_left with dissolve.nowait
    viv "I have been looking forward to this all day!"
    viv "Come, mon bel homme! Ravage me!"
    show old_viv 32
    show old_anon 14
    anon "Avec plaisir!"
    jump viv05_office5.reuse


label viv_office.area:
    hide anon
    hide viv
    show old_viv 1 at old_right
    show old_anon 10 at old_left
    anon "Do you think we could meet in your office after class?"
    show old_anon 26
    anon "You know, for some... tutoring?"
    show old_anon 13
    show old_viv 12
    viv "Oh, {i}tutoring{/i}. Oui!"
    viv "I'll see you later for some one-on-one time, yes?"
    show old_viv 13
    show old_anon 33
    anon "Oui!"
    show old_anon 13
    show old_viv 12
    viv "Très bien, mon bel homme!"
    hide old_anon with dissolve
    return


label viv_office.busy:
    "{color=1ceda7}TODO:{/color} viv_office.busy"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
