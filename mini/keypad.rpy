screen mini_keypad(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_keypad'

    default game = saga.mini.keypad()

    add saga.easy.image('art/mini/keypad/base.png')

    if game.mode is True:
        add saga.easy.image('art/mini/keypad/pass.png') alt _('Unlocked')

    elif game.mode is False:
        add saga.easy.image('art/mini/keypad/fail.png') alt _('Locked')

    else:
        key 'input_enter' action Function(game.input, '#')

        grid 8 1:
            alt game.code
            style_suffix 'input'

            for i in game.code:
                frame:
                    add f'art/mini/keypad/{i}.png':
                        xalign 1.

            if len(game.code) < 8:
                frame:
                    add 'mini_keypad_prompt'

    grid 3 4:
        for i in '123456789*0#':
            textbutton i:
                action Function(game.input, i)
                at button

                if i == '*':
                    keysym ('input_backspace', 'input_delete')
                elif i == '#':
                    pass
                else:
                    keysym (f'K_{i}', f'K_KP_{i}')

    if game.wait:
        add game.wait
    else:
        use hud_back(False)


image mini_keypad_prompt = Solid('fec4a1', xysize=(.8, 5), align=(.5, 1.1))


style mini_keypad_button:
    background Frame('art/mini/keypad/key.png', 20, 20)
    xysize (150, 140)

style mini_keypad_button_text:
    align (.5, .5)
    color 'c4c4caee'
    outlines ((2, '1124', 0, -1),
              (1, '1122', 0, -1),
              (2, 'fff1', -0, 2),
              (1, 'eee2', -0, 1))
    size 60

style mini_keypad_frame:
    xysize (50, 76)

style mini_keypad_grid:
    anchor (.5, .5)
    pos (.5, .55)
    spacing 20

style mini_keypad_input:
    spacing 10
    xalign .5
    yoffset saga.easy.placement('art/mini/keypad/0.png').yoffset
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
