screen mini_french(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.french()

    add saga.easy.image(f'art/mini/french/{game.page}/base.png')

    label _('Select the item that matches the word!')

    for i in game.opts:
        imagebutton:
            action Function(game.pick, i)
            at button, saga.easy.placement(f'art/mini/french/{game.page}/{i}.png')
            idle f'art/mini/french/{game.page}/{i}.png'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
