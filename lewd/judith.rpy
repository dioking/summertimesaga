label judith_menu:
    return


label judith_menu.boys_strip:
    jump ano01_change


label judith_menu.park_date:
    python hide:
        if 'key' in opts:
            saga.prop.key_school.where = saga.cast.anon

    jump tor02_judith2


label judith_menu.stall_grope:
    jump jud02_stall


label judith_menu.stall_handjob:
    jump jud_stall_event
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
