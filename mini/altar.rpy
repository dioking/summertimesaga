screen mini_altar(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive

    default game = saga.mini.altar()

    add saga.easy.ref('forest_altar', 'dark', 'base')

    use expression f'mini_altar_{game.mode}' pass (game)


screen mini_altar_puzzle(game):
    draggroup:
        for offset in game.slots:
            drag:
                draggable False
                offset offset

                add 'art/mini/altar/blank.png'

        for i, offset index i in game.tiles.items():
            drag:
                drag_name i
                dragged game.move
                droppable False
                offset offset

                add f'art/mini/altar/{i:02}.png' at button

    if game.wait:
        add game.wait
    else:
        use hud_back(False)


screen mini_altar_outro(game):
    for i in (1, 5, 6):
        add saga.easy.image(f'art/mini/altar/{i:02}.png')

    add saga.easy.image('art/mini/altar/07.png') at mini_altar_hide
    add saga.easy.image('art/prop/forest_altar/03/prop/clue_map/dark;open.png'):
        at mini_altar_show
    add saga.easy.image(f'art/mini/altar/patch.png')

    for i in (2, 3, 4):
        add saga.easy.image(f'art/mini/altar/{i:02}.png')

    timer 3.75 action Return(True)


transform mini_altar_hide:
    pause .5
    parallel:
        easein 2. alpha 0.
    parallel:
        linear 2. offset (125, 125) zoom .75

transform mini_altar_show:
    alpha 0. offset (50, 50)
    pause 2.75
    parallel:
        easeout 1. alpha 1.
    parallel:
        linear 1. offset (0, 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
