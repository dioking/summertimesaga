screen mini_donut(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive

    default game = saga.mini.donut()

    add saga.easy.ref(saga.camera.track.where.ref) at stage
    add saga.easy.image('art/mini/donut/base.png')

    for grp, ref, name in game.opts:
        button:
            action Function(game.pick, grp, ref)
            alt name
            at button, saga.easy.placement(f'art/mini/donut/{grp}/{ref}.png')

            if ref == game.mix[grp]:
                foreground game.outline

            add f'art/mini/donut/{grp}/{ref}.png'

    if game.wait:
        add game.wait
    else:
        use hud_back(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
