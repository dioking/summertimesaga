screen mini_safe(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_safe'

    default game = saga.mini.safe()

    add saga.easy.image('art/mini/safe/base.png')

    fixed at game.spin:
        add 'art/mini/safe/dial.png'

        for tick in xrange(0, 10):
            textbutton str(tick * 1):
                action Function(game.turn, tick)
                at mini_safe_rotate(tick * 36)
                keysym f'K_{tick}', f'K_KP_{tick}'

    add game.wait

    use hud_back(False)


style mini_safe_button:
    anchor (.5, 210)
    padding (30, 50, 30, 20)
    pos (.5, .5)
    subpixel True

style mini_safe_button_text:
    color '000c'
    hover_color '000'
    hover_outlines ((1, '0004', 0, 0),)
    size 22

style mini_safe_fixed:
    align (.5, .5)
    fit_first True


transform mini_safe_rotate(a):
    rotate a
    transform_anchor True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
