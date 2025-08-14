label mall_hall1:
    return


label mall_hall1.dark:
    scene mall_main at stage
    show old_anon 10 with dissolve
    anon "( It's pretty late, I should be getting home. )"
    hide old_anon with dissolve
    return


label mall_hall1.skip:
    scene camera at stage

    menu:
        "Advance time and exit the mall.":
            return True
        "Take it slow and stick around.":

            pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
