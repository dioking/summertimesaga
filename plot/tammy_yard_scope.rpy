label tammy_yard_scope:
    return


label tammy_yard_scope.empty(seen=False):
    call shot.tammy_yard_scope

    if seen:
        return

    anon "( [saga.cast.tammy]'s yoga mat is there... )"
    anon "( ... There's no one in the backyard. )"
    return


label tammy_yard_scope.late(seen=False):
    call shot.tammy_yard_scope

    if seen:
        return

    anon "( [saga.cast.tammy] left her yoga mat outside. )"
    return


label tammy_yard_scope.yoga1(seen=False):
    call shot.tammy_yard_scope
    show old_tammy scope 18 onlayer aux

    if seen:
        return

    anon "( Man... )"
    anon "( [saga.cast.tammy] is so... flexible... )"
    return


label tammy_yard_scope.yoga2(seen=False):
    call shot.tammy_yard_scope
    show old_tammy scope 19 onlayer aux

    if seen:
        return

    anon "( [saga.cast.tammy] is always doing yoga... )"
    anon "( I guess she likes to stay in shape. )"
    return


label tammy_yard_scope.yoga3(seen=False):
    call shot.tammy_yard_scope
    show old_tammy scope 20 onlayer aux

    if seen:
        return

    anon "( Oh, yeah... )"
    anon "( That's my favorite position. )"
    anon "( I get turned on so much when she does that... I don't know why. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
