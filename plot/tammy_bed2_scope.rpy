label tammy_bed2_scope:
    return


label tammy_bed2_scope.empty(seen=False):
    call shot.tammy_bed2_scope

    if seen:
        return

    anon "( He's not in his room. )"
    return


label tammy_bed2_scope.game(seen=False):
    call shot.tammy_bed2_scope
    show tammy_bed2_scope on
    show old_erik scope 1 behind wall onlayer aux

    if seen:
        return

    anon "( He probably stayed up all night playing that game... )"
    return


label tammy_bed2_scope.jenny(seen=False):
    call shot.tammy_bed2_scope
    show tammy_bed2_scope cam
    show old_erik scope 2_3 behind wall onlayer aux

    if seen:
        return

    anon "( What's [saga.cast.erik] looking at? )"
    anon "( That looks oddly familiar... )"
    return


label tammy_bed2_scope.late1(seen=False):
    call shot.tammy_bed2_scope

    if seen:
        return

    anon "( He's always playing that game... )"
    return


label tammy_bed2_scope.late2(seen=False):
    call shot.tammy_bed2_scope
    show tammy_bed2_scope shut as wall

    if seen:
        return

    anon "( The blinds are closed. Maybe he's using his lotion again. )"
    return


label tammy_bed2_scope.orc(seen=False):
    call shot.tammy_bed2_scope
    show tammy_bed2_scope orc
    show old_erik scope 4_5 behind wall onlayer aux

    if seen:
        return

    anon "Uhh!!" with hpunch
    anon "( I can see why he was so excited about getting it... )"
    return


label tammy_bed2_scope.tammy1(seen=False):
    call shot.tammy_bed2_scope
    show tammy_bed2_scope on
    show old_erik scope 1 behind wall onlayer aux

    if seen:
        show tammy_bed2_scope shut as wall
        return

    anon "( He probably stayed up all night play- )"
    show old_tammy scope 13 behind old_erik onlayer aux
    with dissolve.aux
    anon "( [saga.cast.tammy] is there. )"
    show old_tammy scope 14
    with dissolve.aux
    anon "( She's probably just checking on him... )"
    show old_erik scope 6
    with dissolve.aux
    anon "..."
    show old_tammy scope 15
    with dissolve.aux
    anon "( They're kissing on the mouth!? That's weird... )"
    show old_erik scope hand 1 as hand behind wall onlayer aux
    with dissolvefast.aux
    anon "( What the... )"
    anon "( Did he just grab her boob?? )"
    hide hand
    show old_erik scope 1
    show old_tammy scope 16
    with dissolve.aux
    anon "( She's closing his blinds... )"
    show tammy_bed2_scope shut as wall
    with dissolvefast.aux
    return


label tammy_bed2_scope.tammy2(seen=False):
    call shot.tammy_bed2_scope
    show tammy_bed2_scope on
    show old_erik scope 1 behind wall onlayer aux

    if seen:
        show tammy_bed2_scope shut as wall
        return

    anon "( He probably stayed up all night play- )"
    show old_tammy scope 13 behind old_erik onlayer aux
    with dissolve.aux
    anon "( [saga.cast.tammy] is there. )"
    show old_tammy scope 14
    with dissolve.aux
    anon "( She's probably just checking on him... )"
    show old_erik scope 6
    with dissolve.aux
    anon "..."
    show old_tammy scope 15
    with dissolve.aux
    anon "( They're kissing on the mouth!? That's weird... )"
    show old_erik scope hand 1 as hand behind wall onlayer aux
    with dissolvefast.aux
    anon "( What the... )"
    anon "( Did he just grab her boob?? )"
    show old_erik scope hand 1_2_3_4_5_6 once as hand
    anon "..."
    show old_erik scope hand 7_8 loop slow as hand
    anon "( !!! )" with hpunch
    anon "Wow, things really escalated..."
    hide hand
    show old_erik scope 1
    show old_tammy scope 17
    with dissolve.aux
    anon "( What a sight... )"
    show tammy_bed2_scope shut as wall
    with dissolvefast.aux
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
