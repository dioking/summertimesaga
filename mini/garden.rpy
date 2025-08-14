screen mini_garden(mode, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_garden'

    default game = saga.mini.garden(mode)

    add saga.easy.image('art/mini/garden/base.png')

    grid 7 3:
        for ref, name, cash, path, reveal in game.layout:
            if ref is None:
                add path
                continue

            showif ref not in game.gone:
                button:
                    action Function(game.clear, ref, cash)
                    alt name
                    at button, reveal

                    add path

    text '[game.cash]'

    label _('Clear [game.hint!it] before the time runs out!'):
        style_prefix 'mini'

    if game.wait:
        add game.wait

    else:
        frame:
            add Solid('fff') at mini_timer(game.ttl)

        timer game.ttl action Function(game.outro)


style mini_garden_button:
    xysize (230, 230)

style mini_garden_frame:
    anchor (.5, .5)
    foreground gui.frame
    padding (5, 5)
    pos (.512, .91)
    xysize (.575, .035)

style mini_garden_grid:
    anchor (.5, 0.)
    pos (.5, .13)

style mini_garden_text:
    anchor (.5, .5)
    pos (.139, .9)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
