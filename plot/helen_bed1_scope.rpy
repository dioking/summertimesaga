label helen_bed1_scope:
    return


label helen_bed1_scope.empty(seen=False):
    call shot.helen_bed1_scope

    if seen:
        return

    anon "( They're not home... )"
    return


label helen_bed1_scope.pray(seen=False):
    call shot.helen_bed1_scope
    show old_helen scope 1 behind wall onlayer aux

    if seen:
        return

    anon "( [saga.cast.mia]'s mom is always praying in the morning... )"
    return


label helen_bed1_scope.row(seen=False):
    call shot.helen_bed1_scope

    if seen:
        show old_helen scope 3 behind wall onlayer aux
        return

    show old_helen scope 2 behind wall onlayer aux
    anon "( Oh boy. )"
    anon "( Looks like [saga.cast.helen] is mad at him... )"
    anon "..."
    anon "( [saga.cast.harold] always looks so sad... )"
    return


label helen_bed1_scope.sleep(seen=False):
    call shot.helen_bed1_scope
    show old_helen scope 3 behind wall onlayer aux

    if seen:
        return

    anon "( It's odd how they both have their own bed... )"
    anon "( ... I've never seen them sleep together. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
