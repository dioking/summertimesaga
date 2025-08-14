screen mini_tattoo(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive

    default tattoos = saga.mini.tattoo.opts

    add saga.easy.ref(saga.camera.track.where.ref) at stage
    add saga.easy.image('art/mini/tattoo/base.png')

    for k, v in tattoos.items():
        imagebutton:
            action Return(k)
            alt k
            at button, saga.easy.placement(v)
            idle v
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
