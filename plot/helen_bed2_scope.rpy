label helen_bed2_scope:
    return


label helen_bed2_scope.dress(seen=False):
    call shot.helen_bed2_scope

    if seen:
        return

    show old_mia scope 2 behind wall onlayer aux
    anon "( Too late... I always miss the best part! )"
    return


label helen_bed2_scope.empty(seen=False):
    call shot.helen_bed2_scope

    if seen:
        return

    anon "( She's not home. )"
    return


label helen_bed2_scope.mirror(seen=False):
    call shot.helen_bed2_scope

    if seen:
        return

    show old_mia scope 1 behind wall onlayer aux

    if saga.time.sun:
        anon "( She's getting ready for church. )"
    elif saga.time.sat:
        anon "( I wonder what she's doing today? )"
    else:
        anon "( She's getting ready for school. )"

    return


label helen_bed2_scope.sleep(seen=False):
    call shot.helen_bed2_scope
    show helen_bed2_scope shut

    if seen:
        return

    anon "( She must be sleeping. )"
    return


label helen_bed2_scope.study(seen=False):
    call shot.helen_bed2_scope
    show old_mia scope 3 behind wall onlayer aux

    if seen:
        return

    anon "( She's always reading or studying... )"
    return


label helen_bed2_scope.teddy(seen=False):
    call shot.helen_bed2_scope

    if seen:
        show helen_bed2_scope shut
        return

    show old_mia scope 6_7 behind wall onlayer aux
    anon "( What's she doing? )"
    anon "..."
    anon "( She's... )"
    anon "( ... Humping her teddy bear? )"
    anon "( Wow... )"
    anon "( That's really hot- )"
    show old_mia scope 8
    anon "!!!"
    show old_mia scope 9
    show old_helen scope 4 behind old_mia onlayer aux
    anon "( Oh, crap! )"
    anon "( I think she just got caught... )"
    anon "( Her mom must be furious... She's always so strict with her... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
