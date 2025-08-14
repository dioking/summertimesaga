label view(what, where=None):
    scene expression saga.easy.ref(where.ref if where else what.where.ref, f'-{what}', '-filter') at stage
    show expression saga.easy.ref(what.ref)
    with dissolvefast
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
