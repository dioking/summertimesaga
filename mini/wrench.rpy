screen mini_wrench(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.wrench()

    add saga.easy.image('art/mini/wrench/base.png')

    showif game.count == -1:
        add saga.easy.image('art/mini/wrench/arrow.png') at mini_wrench_help

    add game.wait
    add game

    label _('Tighten the bolt by turning the wrench clockwise!')


transform mini_wrench_help:
    on show:
        alpha 0
        linear .2 alpha 1
    on hide:
        linear .2 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
