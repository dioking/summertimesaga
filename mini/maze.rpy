screen mini_maze(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_maze'

    default game = saga.mini.maze()

    add saga.easy.image(game.base)

    for dir, idle in game.nav:
        imagebutton:
            at button, saga.easy.placement(idle)
            idle idle
            action Function(game.move, dir)

    frame:
        add Solid('5cf') at mini_timer(15.)

    timer 15. action Return(False)

    use hud_back(False)


style mini_maze_frame:
    align (.5, .9)
    foreground gui.frame
    padding (5, 5)
    xysize (.525, .0325)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
