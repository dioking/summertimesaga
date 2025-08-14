label computer:
    return


label computer.auth(what):
    scene
    show screen pc(what, auto=True)
    pause what and .5 + len(what.password) * .075
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
