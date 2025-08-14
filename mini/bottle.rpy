screen mini_bottle(who, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive

    default game = saga.mini.bottle(who)

    add saga.easy.image('art/mini/bottle/base.png'):
        alt _('Spin the bottle!')

    for who in game.pool:
        add saga.easy.image(f'art/mini/bottle/{who.ref}.png'):
            if game.mode == 'outro' and who is game.who:
                at mini_bottle_pulse

    fixed at game.spin:
        add saga.easy.image('art/mini/bottle/bottle.png')

    if game.mode == 'init':
        imagebutton:
            action Function(game.begin)
            alt _('Spin')
            at button, saga.easy.placement('art/mini/bottle/spin.png')
            idle 'art/mini/bottle/spin.png'

    add game.wait


transform mini_bottle_pulse:
    matrixcolor BrightnessMatrix(0)
    linear .15 matrixcolor BrightnessMatrix(.2)
    linear .15 matrixcolor BrightnessMatrix(0)
    repeat 2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
