screen mini_serum(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.serum()

    add saga.easy.image('art/mini/serum/base.png')

    if game.show:
        add saga.easy.image(f'art/mini/serum/{game.serum}.png') at game.fluid
        add saga.easy.image('art/mini/serum/flask.png')

    vbox:
        style_prefix 'mini_serum'
        xpos .2

        for i in game.opts[:3]:
            if i in game.mix:
                add 'art/mini/serum/box.png' alpha .4
            else:
                imagebutton:
                    action Function(game.add, i)
                    alt game.tts[i]
                    at button
                    background 'mini_serum_ltr'
                    idle f'art/mini/serum/{i}.png'

    if game.show:
        vbox:
            style_prefix 'mini_serum'
            box_reverse True

            for i in game.mix:
                add f'art/mini/serum/{i}.png'
            for i in range(3 - len(game.mix)):
                add 'art/mini/serum/box.png' alpha .4

    vbox:
        style_prefix 'mini_serum'
        xpos .8

        for i in game.opts[3:]:
            if i in game.mix:
                add 'art/mini/serum/box.png' alpha .4
            else:
                imagebutton:
                    action Function(game.add, i)
                    alt game.tts[i]
                    at button
                    background 'mini_serum_rtl'
                    idle f'art/mini/serum/{i}.png'

    label _('Combine the ingredients for the [game.hint!i] serum!')

    add game.wait


image mini_serum_ltr = Transform(
    'art/mini/serum/arrow.png', align=(1.5, .5), xzoom=-1)
image mini_serum_rtl = Transform(
    'art/mini/serum/arrow.png', align=(-.5, .5))


style mini_serum_vbox:
    anchor (.5, 1.)
    pos (.5, .7)
    spacing 15
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
