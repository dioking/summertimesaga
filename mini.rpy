label mini:
    pass


label mini.altar:
    scene
    call screen mini_altar(_with_none=False) with dissolve
    return _return


label mini.atm:
    scene
    call screen mini_atm(saga.camera.track, _with_none=False) with dissolvefast
    $ saga.camera.track.bank, saga.camera.track.cash = _return
    return


label mini.bottle(what=None):
    scene
    call screen mini_bottle(what, _with_none=False) with fade
    return _return


label mini.camera(*what):
    scene
    call screen mini_camera(*what, _with_none=False) with fade
    return _return


label mini.cocktail(what):
    scene
    call screen mini_cocktail(what, _with_none=False) with fade
    return _return


label mini.combat(what=None):
    python:
        config.skipping = None
        renpy.dynamic(_skipping=False)

    if what:
        scene mini_combat_splash
        with saga.mini.combat.splash(what)
        show mini_combat_vs
        pause

    scene

    python:
        renpy.dynamic(_rollback=False)
        _return = renpy.roll_forward_info()

        if _return is None or not renpy.game.after_rollback:
            renpy.game.log.forward.clear()
            renpy.transition(fade)
            _return = renpy.call_screen('mini_combat', what, _with_none=False)

        else:
            renpy.checkpoint(_return, keep_rollback=True)

    return _return


label mini.cook(what=None):
    scene
    call screen mini_cook(what, _with_none=False) with fade
    return _return


label mini.courier:
    scene
    call screen mini_courier(_with_none=False) with fade
    return _return


label mini.donut:
    scene
    call screen mini_donut(_with_none=False) with fade
    return _return


label mini.french:
    scene
    call screen mini_french(_with_none=False) with fade
    return _return


label mini.garden(what=saga.prop.diane_plot.mode):
    scene
    call screen mini_garden(what, _with_none=False) with fade
    return _return


label mini.hack:
    menu:
        "This mini game is still under construction! Please check back in future updates.\nIn the meantime, what outcome would you like to simulate?"
        "Pass":

            return True
        "Fail":
            pass

    return


label mini.hottub(*what):
    scene
    call screen mini_hottub(*what, _with_none=False) with fade
    return


label mini.keypad:
    scene
    call screen mini_keypad(_with_none=False) with fade
    return _return


label mini.maze:
    scene
    call screen mini_maze(_with_none=False) with fade
    return _return


label mini.milk(what):
    scene
    call screen mini_milk(what, _with_none=False) with fade
    return _return


label mini.paint:
    scene
    call screen mini_paint(_with_none=False) with fade
    return _return


label mini.pushup:
    scene
    call screen mini_pushup(_with_none=False) with fade
    return _return


label mini.rhythm:
    scene tammy_snug at stage(.45, .75, 8, b=20)
    with fade

    menu:
        "This mini game is still under construction! Please check back in future updates.\nIn the meantime, what outcome would you like to simulate?"
        "Pass":

            return True
        "Fail":
            pass

    return


label mini.safe:
    scene
    call screen mini_safe(_with_none=False) with fade
    return _return


label mini.scuffle:
    scene
    call screen mini_scuffle(_with_none=False) with fade
    return _return


label mini.serum:
    scene
    call screen mini_serum(_with_none=False) with fade
    return _return


label mini.tattoo:
    scene
    call screen mini_tattoo(_with_none=False) with fade
    return _return


label mini.vault:
    scene
    call screen mini_vault(_with_none=False) with fade
    return _return


label mini.weight(*what):
    scene
    call screen mini_weight(*what, _with_none=False) with fade
    return _return


label mini.womb(what):
    if _in_replay or what.womb:
        return

    if not persistent.conception:
        $ saga.event.emit(baby=what.womb.next(), who=what)
        return

    call screen mini_womb(what, _with_none=False) with fade

    python hide:
        saga.event.emit(baby=_return, who=what)

        site = renpy.get_return_stack()[-1]
        node = renpy.game.script.lookup(site)

        s = node.scry()

        while not s.interacts:
            if isinstance(s._next, renpy.ast.With):
                break
            
            s = s.next()
            
            if not s:
                break

        else:
            renpy.with_statement(fade)

    return


label mini.wrench:
    scene
    call screen mini_wrench(_with_none=False) with fade
    return _return


style mini_label:
    anchor (.5, .5) pos (.5, .05)
    background gui.frame
    padding (5, 15)
    xminimum .8

style mini_label_text:
    xalign .5
    outlines ((1, '0004', 1, 1),)

style mini_timer:
    anchor (.5, 0.) pos (.5, .082)
    foreground gui.timer
    padding (3, 0, 3, 3)
    xysize (.525, .0175)


transform mini_timer(t):
    xsize 1.
    linear t xsize 0.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
