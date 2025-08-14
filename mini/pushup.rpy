screen mini_pushup(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_pushup'

    default game = saga.mini.pushup(saga.cast.dexter)

    add saga.easy.image('art/mini/pushup/base.png')

    add game

    for k, v in game.reps.items():
        fixed:
            at saga.easy.placement(f'art/mini/pushup/{k.ref}/silo.png')

            add f'art/mini/pushup/{k.ref}/silo.png'
            text str(v) anchor (.5, 0.) pos (.5, 1.05)

    if game.wait:
        add game.wait

    else:
        frame:
            add Solid('0003')
            add Solid('5cf') at mini_timer(15.)

        label _('Click to do as many push-ups as possible within the time!')
        timer 15. action Function(game.outro)


style mini_pushup_fixed:
    fit_first True

style mini_pushup_frame is mini_timer


style mini_pushup_label is mini_label:

    xmaximum .7

style mini_pushup_label_text is mini_label_text
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
