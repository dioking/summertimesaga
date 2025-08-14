label ang_church_nave:
    jump ang_church_nave.intro

    menu ang_church_nave.choice:
        "Linens." if saga.event.peek(choice='linens', who=saga.cast.ang):
            return saga.event.emit(choice='linens', who=saga.cast.ang)
        "I was just leaving.":







            pass

    jump ang_church_nave.outro


label ang_church_nave.intro:
    call shot.church_nave_ang
    show old_ang 1 at old_right
    show old_anon 2 at old_left with dissolve
    anon "Umm... hello."
    show old_anon 1
    show old_ang 2
    ang "Be welcome in the house of our lord."
    ang "Have you come to unburden yourself?"
    show old_ang 1
    jump ang_church_nave.choice


label ang_church_nave.outro:
    show old_anon 29
    show old_ang 1
    anon "I'm not sure I have time to ehh... \"unburden\" myself today..."
    anon "... Maybe next time."
    show old_anon 13
    show old_ang 4
    ang "Go with god, child."
    hide old_anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
