screen mini_hottub(min, max, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.hottub(min, max)
    default noop = lambda: None

    add saga.easy.image('art/mini/hottub/base.png')

    if _sensitive:
        add game.net

    label _('Clean the hot tub by dragging the net over the detritus!')

    grid 5 3:
        style_prefix 'mini_hottub'

        for i, item, vis in game.grid:
            if not item:
                null
                continue

            showif vis:
                button:
                    action noop
                    at mini_hottub_float((1 + i / 5 + i % 5) / 7)
                    hovered SetDict(game.mess, i, None)
                    xoffset i // 5 * (2 - i % 5) * -32

                    add saga.easy.image(f'art/mini/hottub/{item}.png')

    if not any(game.mess):
        dismiss action Return() modal False
        timer 1.5 action Return()


style mini_hottub_button:
    xysize (270, 270)

style mini_hottub_grid:
    align (.5, .5)
    xspacing -50
    yoffset 30
    yspacing -30


transform mini_hottub_float(t):
    subpixel True
    parallel:
        t
        block:
            ease 1. yoffset 6
            ease 1. yoffset 0
            repeat
    parallel:
        on hide:
            linear .3 alpha 0.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
