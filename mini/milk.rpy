screen mini_milk(who, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.milk(who)
    default milk = game.milk
    default touch = renpy.variant('touch')

    add 'art/mini/milk/base.png'

    for s, v in game.pump.items():
        fixed:
            if s == 'right':
                at Transform(xzoom=-1)

            add f'art/mini/milk/{who.ref}/idle.png':
                at (mini_milk_gland(who) if s == game.side else
                    saga.easy.placement(f'art/mini/milk/{who.ref}/idle.png'))

            fixed:
                if s == game.side:
                    at mini_milk_shift

                add 'art/mini/milk/milk1.png':
                    at (mini_milk_slosh(v, *milk) if v else mini_milk_fluid)

                add saga.easy.image('art/mini/milk/pump.png')
                add saga.easy.image('art/mini/milk/bar.png')

        use mini_milk_interact(game, s, v)

    if touch:
        label _('Slowly switch between the pumps to milk [game.hint!i]!')
    else:
        label _('Alternate left and right arrow keys to milk [game.hint!i]!')

    add game.wait


screen mini_milk_interact(game, s, v):
    if v < 1 and not game.side:
        key f'focus_{s}' action Function(game.pull, s)


screen mini_milk_interact(game, s, v):
    variant 'touch'

    imagebutton:
        action Function(game.pull, s)
        at mini_milk_button, saga.easy.placement(f'art/mini/milk/{s}.png')
        idle f'art/mini/milk/{s}.png'
        keysym f'focus_{s}'
        sensitive v < 1 and not game.side


transform mini_milk_button:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor gui.over
    on insensitive:
        matrixcolor gui.grey

transform mini_milk_fluid(child):
    yanchor 1. ypos 443
    offset saga.easy.placement(child.filename).offset
    crop (0., 0., 1., 0.)

transform mini_milk_gland(who, child):
    offset saga.easy.placement(child.filename).offset
    f'art/mini/milk/{who.ref}/pull.png'
    pause .4
    child with dissolvefast

transform mini_milk_shift:
    yoffset 15
    pause .4
    ease .1 yoffset 0

transform mini_milk_slosh(v, im1, im2, im3):
    parallel:
        linear .5 crop (0., 0., 1., v)
    parallel:
        im2 with dissolvefast
        pause .2
        im1 with dissolvefast
        pause .2
        im3 with dissolvefast
        pause .2
        im1 with dissolvefast
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
