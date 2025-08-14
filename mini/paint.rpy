screen mini_paint(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.paint()

    add saga.easy.ref('school_art') at stage(.4, .4, 2)
    add '#fff7'

    add saga.easy.image('art/mini/paint/palette.png')

    for spot in game.spots:
        add saga.easy.image(f'art/mini/paint/spot/{spot}.png')

    for tube in game.tubes:
        button:
            action Function(game.toggle, tube)
            alt tube
            at button, saga.easy.placement(f'art/mini/paint/tube/{tube}.png')

            if tube in game.mix:
                foreground game.outline

            add f'art/mini/paint/tube/{tube}.png'

    label _('Combine two paint tube colors to make [game.hint!i]!')

    add game.wait
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
