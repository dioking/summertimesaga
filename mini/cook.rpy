screen mini_cook(what, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_cook'

    default game = saga.mini.cook(what)

    add saga.easy.image('art/mini/cook/base.png')

    if game.mode in ('init', 'swap'):
        add saga.easy.image('art/mini/cook/crust.png') at mini_cook_enter

    showif game.mode in ('play', 'fail'):
        fixed:
            at saga.easy.placement('art/mini/cook/crust.png'), mini_cook_leave

            add 'art/mini/cook/crust.png'

            for v in game.mix:
                add saga.easy.image(f'art/mini/cook/tops/{v}.png')

    grid 7 2:
        for v in game.food:
            imagebutton:
                action Function(game.add, v)
                alt v
                at button
                foreground saga.easy.image(f'art/mini/cook/food/{v}.png')
                idle 'art/mini/cook/box.png'

    if game.mode == 'play':
        add f'art/mini/cook/food/{game.next}.png' at mini_cook_pulse
        add f'art/mini/cook/arrow.png' at mini_cook_point

        frame:
            add Solid('0003')
            add Solid('c55') at mini_timer(game.ttl)

        timer game.ttl action Function(game.fail)

    elif game.mode in ('intro', 'init'):
        for i in range(1, 4):
            text '[i]' at mini_cook_intro(.5, 4. - i)

        text 'GO' at mini_cook_intro(.5, 4.)

    label _('Add the indicated toppings before time runs out!')

    add game.wait


style mini_cook_fixed:
    fit_first True

style mini_cook_frame is mini_timer


style mini_cook_grid:
    anchor (.5, .5)
    pos (.5, .8)
    spacing 30

style mini_cook_label is mini_label


style mini_cook_label_text is mini_label_text


style mini_cook_text:
    align (.5, .3)
    bold True
    outlines ((16, 'f70', 0, 0),)
    size 180


transform mini_cook_intro(t, w):
    alpha 0. mesh True subpixel True zoom .6
    w
    ease .1 alpha 1. zoom 1.
    t
    ease .4 alpha 0.

transform mini_cook_enter:
    subpixel True xpos 1.
    .5
    ease 1 xpos 0.

transform mini_cook_leave:
    subpixel True xpos 0.
    on hide:
        .5
        ease 1 xpos -1.
        xpos 0.

transform mini_cook_point:
    align (.5, .25) subpixel True
    ease 1 yoffset -5
    ease 1 yoffset 5
    repeat

transform mini_cook_pulse:
    anchor (.5, .5) pos (.5, .175) subpixel True
    ease 1 zoom .90
    ease 1 zoom 1.05
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
