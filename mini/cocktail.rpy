screen mini_cocktail(what, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.cocktail(what)

    add saga.easy.image('art/mini/cocktail/base.png')

    use expression f'mini_cocktail_{game.mode}' pass (game)


screen mini_cocktail_mix(game):
    add saga.easy.image('art/mini/cocktail/board.png')

    hbox:
        style_prefix 'mini_cocktail'

        for i in game.opts:
            if i in game.mix:
                null width 252 height (252 if i < 7 else 288)

            else:
                button:
                    action Function(game.add, i)
                    alt game.tts[i]
                    at button
                    xsize 252 ysize (252 if i < 7 else 288)

                    add saga.easy.image(f'art/mini/cocktail/item/{i}.png')

    vbox:
        style_prefix 'mini_cocktail'

        for i in game.mix:
            fixed:
                add 'art/mini/cocktail/icon/box.png' alpha .8
                add saga.easy.image(f'art/mini/cocktail/icon/{i}.png')

        for i in range(3 - len(game.mix)):
            add 'art/mini/cocktail/icon/box.png' alpha .8

    label _('Pick out the ingredients for a [game.hint!i]!')

    add game.wait


screen mini_cocktail_shake(game):
    add game.shaker
    add game

    label _('Mix it by shaking the container up and down, side to side!')


style mini_cocktail_fixed:
    fit_first True

style mini_cocktail_hbox:
    anchor (.5, .5)
    box_wrap True
    pos (715, .525)
    xsize 756

style mini_cocktail_vbox:
    anchor (.5, .5)
    pos (1418, .55)
    spacing 45
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
