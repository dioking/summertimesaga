label loop:
    call loop.drain from loop.gui
    scene
    call expression f'gui.{saga.gui.step.ref}' from loop.emit
    $ saga.event.emit(_return)
    jump loop


label loop.drain:
    while saga.event.more:
        $ saga.event.next()
        label loop.more:
    return


label loop.flush:
    if not main_menu and not saga.event.stack:
        jump loop.drain
    return


label gui:
    return


label gui.nav:
    call screen nav(saga.camera.what, _with_none=False) with dissolvefast
    return _return


label gui.use:
    call screen use(saga.camera.focus, _with_none=False)
    return _return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
