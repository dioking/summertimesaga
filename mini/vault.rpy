screen mini_vault(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_vault'

    default game = saga.mini.vault()
    default help = False
    default noop = lambda: None

    add Solid('9ea4ad')

    vpgrid as vp:
        cols 10
        rows 9
        draggable True
        edgescroll (75, 450, game.scroll)
        xinitial game.x
        yinitial game.y

        for i in game.layout:
            button:
                action (Return(True) if i == 11082 else noop)
                at button

                has fixed
                fit_first True

                add game.box
                text '[i]' align (.5, .3)

    showif help:
        showif game.distance(vp) < 100:
            fixed:
                at mini_vault_appear

                if _sensitive:
                    add 'mini_vault_hint' align .5, .02
                    add 'mini_vault_hint' align .99, .5 rotate 90
                    add 'mini_vault_hint' align .5, .99 rotate 180
                    add 'mini_vault_hint' align .01, .5 rotate 270

    else:
        timer 10 action SetScreenVariable('help', True)

    if _sensitive:
        use hud_back(False)


image mini_vault_hint = Window('help_arrow')


style mini_vault_text:
    align (.5, .35)
    color '333c'
    outlines ((0, 'ccc7', 1, 1),)
    size 30


transform mini_vault_appear:
    on show:
        alpha 0.
        linear 1. alpha 1.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
