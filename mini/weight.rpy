screen mini_weight(*args, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_weight'

    default game = saga.mini.weight(*args)

    add saga.easy.image('art/mini/weight/base.png')

    add game

    fixed:
        at saga.easy.placement(f'art/mini/weight/silo.png')

        add f'art/mini/weight/silo.png'
        text str(game.reps) anchor (.5, 0.) pos (.5, 1.05)

    if game.wait:
        add game.wait

    else:
        frame:
            add Solid('0003')
            add Solid('fc5') at mini_timer(15.)

        label _('Click to lift the weights and complete reps!')
        timer 15. action Function(game.outro)


style mini_weight_fixed:
    fit_first True

style mini_weight_frame is mini_timer


style mini_weight_label is mini_label:

    xmaximum .7

style mini_weight_label_text is mini_label_text


style mini_weight_text:
    color '222'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
