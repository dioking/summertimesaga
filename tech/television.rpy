label television:
    return


label television.boot(what):
    scene
    show screen tv(what, auto=None)
    pause .6
    return


label television.surf(what):
    scene onlayer aux
    show tv info as num onlayer aux zorder 1 at tv_info

    if what.chan.auth is False:
        show tv auth onlayer aux

        if not what.chan.auto:
            return

        if not renpy.suppress_transition():
            scene
            show screen tv(what, auto=True)
            pause what and .5 + len(''.join(what.chan.keys)) * .075

    show tv auto onlayer aux
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
