label tammy_bed1_scope:
    return


label tammy_bed1_scope.ball(seen=False):
    call shot.tammy_bed1_scope
    show tammy_bed1_scope ball

    if seen:
        show tammy_bed1_scope shut as wall
        return

    show old_tammy scope 6 behind wall onlayer aux
    anon "( Woah... She's completely naked!! )"
    show old_tammy scope 7
    with dissolve.aux
    anon "( Is that a bouncing ball... With a dildo on it?! )"
    show old_tammy scope 8
    with dissolve.aux
    anon "( Why didn't she close the blinds? )"
    show old_tammy scope 8_9 slow
    anon "( It's like she wants to be seen... )"
    anon "( I think she knows... )"
    anon "( She's staring right at me. )"
    return


label tammy_bed1_scope.dress(seen=False):
    call shot.tammy_bed1_scope

    if seen:
        show tammy_bed1_scope shut as wall
        return

    show old_tammy scope 3 behind wall onlayer aux
    anon "( ... Is that [saga.cast.erik]'s landlady?! )"
    show old_tammy scope 4
    with dissolve.aux
    anon "( Oh wow! She's getting dressed... )"
    show old_tammy scope 5
    with dissolve.aux
    anon "( No! Just a little bit longer! )"
    hide old_tammy
    show tammy_bed1_scope shut as wall
    with dissolve.aux
    anon "( Damn! Show's over... )"
    return


label tammy_bed1_scope.empty(seen=False):
    call shot.tammy_bed1_scope

    if seen:
        return

    anon "( She's not in her room. )"
    return


label tammy_bed1_scope.sleep(seen=False):
    call shot.tammy_bed1_scope
    show tammy_bed1_scope shut as wall

    if seen:
        return

    anon "( She must be sleeping. )"
    return


label tammy_bed1_scope.yoga(seen=False):
    call shot.tammy_bed1_scope

    if seen:
        show tammy_bed1_scope shut as wall
        return

    show old_tammy scope 1 behind wall onlayer aux
    anon "( ... Is she practicing yoga? )"
    anon "( ... On her bed? )"
    show old_tammy scope 2
    with dissolve.aux
    anon "..."
    anon "( [saga.cast.erik]'s landlady is so fit... )"
    anon "( ... She really does have a great body... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
