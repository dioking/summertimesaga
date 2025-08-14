label barb_menu:
    return


label barb_menu.art_banana:
    call shot.school_art_barb
    show school_art -table
    show old_xtra 22b as basket at pos(.6)
    show old_barb 4
    show old_anon 1 at old_left
    jump bar03_art2.cookie


label barb_menu.art_model:
    jump bar04_art2


label barb_menu.art_paint:
    call shot.school_art_barb
    show school_art -table
    show old_anon 11 at face_right, pos(.175)
    show old_annie outfit 2 at face_left, pos(.65)
    show old_ursula outfit 1 at face_left, pos(.8)
    jump bar05_art2.cookie


label barb_menu.office_sex:
    jump bar06_office3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
