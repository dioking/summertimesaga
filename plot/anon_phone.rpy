label anon_phone:
    return


label anon_phone.wifi:
    scene anon_phone as phone

    if persistent.cheats == 0:
        anon "( Full bars, nice! )"
    elif persistent.cheats == 1:
        anon "( Better not touch any of the settings, I'd hate to break something that's working as intended. )"
    elif persistent.cheats == 2:
        anon "( Stop that! )"
    elif persistent.cheats == 3:
        anon "( Knock it off! )"
    elif persistent.cheats == 4:
        anon "( I know what you're looking for... )"
    elif persistent.cheats == 5:
        anon "( Last warning... )"
    elif persistent.cheats == 6:
        anon "( Fine! I give up. I'll unlock the cheat menu for you, okay? )"
    else:
        anon "( You already got what you wanted, leave it alone! )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
