label shop:
    return


label shop.fence:
    scene camera at stage

    if renpy.get_transition() is None:
        with dissolve.nowait

    menu:
        "Keep browsing.":
            pass
        "Abandon [saga.gui.buy!lt] and continue.":

            return True

    return


label shop.pay:
    menu:
        "Buy items for $[cash]." if cash and cash <= saga.camera.track.cash:
            return True

        "Borrow [saga.gui.buy!lt]." if not cash:
            return True
        "Keep browsing.":

            pass
        "Abandon [saga.gui.buy!lt].":

            return False

    return


label shop.take(what, label=None):
    $ renpy.dynamic(view=what.ref if hasattr(what, 'art') else None)

    scene camera focus at stage

    if view:
        $ renpy.show(('camera', 'focus', f'-{view}'))
        show expression saga.easy.ref(view)

    with dissolvefast.nowait

    if label:
        call expression label

    if view:
        pause

    menu:
        "Add to [what.cart!lt].":
            return True

        "Put it back." if view:
            pass

        "Leave it." if not view:
            pass

    return


label shop.ivy(cash, what):
    call shot.toy_shop_ivy
    show anon o_right at pos(.35) with dissolve.nowait
    ivy "Hi, [saga.cast.anon]. What have you got in that basket today?"
    pause
    ivy "That'll be $[cash], please."
    jump shop.pay


label shop.jane(cash, what):
    call shot.library_lobby_jane
    show anon at right with dissolve.nowait
    jane "Hi, [saga.cast.anon]. Checking something out?"
    jump shop.pay


label shop.kassy(cash, what):
    call shot.gift_shop_kassy
    show anon at pos(.65) with dissolve.nowait
    kassy "Hi, [saga.cast.anon]. What have you got in that basket today?"
    pause
    kassy "That'll be $[cash], please."
    jump shop.pay


label shop.lily(cash, what):
    call shot.comic_shop_lily
    show anon o_right at pos(.35) with dissolve.nowait
    lily "Hi, [saga.cast.anon]. What have you got in that basket today?"
    pause
    lily "That'll be $[cash], please."
    jump shop.pay


label shop.vee(cash, what):
    call shot.store_aisle_vee
    show anon at pos(.8) with dissolve.nowait
    vee "Hi, [saga.cast.anon]. What have you got in that basket today?"
    pause
    vee "That'll be $[cash], please."
    jump shop.pay
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
