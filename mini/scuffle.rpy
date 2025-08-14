screen mini_scuffle(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.scuffle()

    add 'art/mini/scuffle/base.png'

    for arc in range(1, 6):
        add saga.easy.image(f'art/mini/scuffle/arc/{arc}.png'):
            if arc < game.flex:
                matrixcolor SaturationMatrix(0, (.225, .015, .225))

    add saga.easy.image(f'art/mini/scuffle/grip/{game.grip}.png')

    label _('Click like your life depends on it!')

    add game.wait

    if game.mode:
        dismiss action Function(game.pull, 'l')
        timer .2 action Function(game.pull, 'r') repeat True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
