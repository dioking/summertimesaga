label tori_menu:
    return


label tori_menu.science_strip:
    jump tor01_science.cookie


label tori_menu.science_xray:
    jump tor02_tori.cookie


label tori_menu.office_exam:
    jump tor02_office2


label tori_menu.office_fondle:
    jump tor03_office2


label tori_menu.science_vibe:
    call shot.school_science_door
    show old_tori 1 at old_right
    jump tor04_tori


label tori_menu.office_handjob:
    python hide:
        saga.time.now = saga.time.dusk

    call shot.school_office2_entry
    show old_anon 11 at face_right
    show old_tori 3 at old_right
    jump tor05_office2.cookie


label tori_menu.office_sex:
    jump tor06_office2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
