screen mini_combat(who, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.combat(who)

    add game.base
    add saga.easy.image(f'art/mini/combat/{game.ref}/{game.shot}.png')

    if who:
        transform:
            if who is saga.cast.inky:
                xzoom -1

            use mini_combat_hp(game.defs, game.recv)
            use mini_combat_hp(game.atks, game.sent, npc=True)

    showif game.ttl:
        frame:
            at mini_combat_misc
            style_suffix 'timer'

            add Solid('0003')
            add Solid('5cf') at mini_timer(game.ttl)

        use mini_combat_qte(game)

    if game.ttl:
        timer game.ttl action Function(game.defend)

    showif game.hint:
        label _('Complete the combo before time runs out!') at mini_combat_misc

    add game.wait


screen mini_combat_hp(max, dmg, npc=False):
    style_prefix 'mini_combat'

    frame:
        if npc:
            at Transform(xzoom=-1, transform_anchor=True)

        grid max 1:
            for i in range(max):
                showif dmg <= i:
                    add mini_combat_hp(i, npc=npc)


screen mini_combat_qte(game):
    style_prefix 'mini_combat'

    hbox:
        for k in game.seq[:game.step]:
            fixed:
                add saga.easy.image(f'art/mini/combat/arrow/over/{k}.png')
        for k in game.seq[game.step:]:
            fixed:
                add saga.easy.image(f'art/mini/combat/arrow/idle/{k}.png')

    for k in game.opts:
        key f'focus_{k}' action Function(game.input, k)


screen mini_combat_qte(game):
    style_prefix 'mini_combat'
    variant 'touch'

    for i, k in enumerate(game.seq):
        showif i == game.step:
            imagebutton:
                action Function(game.input, k), SelectedIf(i < game.step)
                align game.opts[k]
                at mini_combat_misc
                idle saga.easy.image(f'art/mini/combat/arrow/idle/{k}.png')
                selected_idle saga.easy.image(f'art/mini/combat/arrow/over/{k}.png')


image mini_combat_hp = Frame('art/mini/combat/hp.png', 20, 0)
image mini_combat_splash = 'art/mini/combat/splash.png'

image mini_combat_vs:
    contains:
        .6
        'art/mini/combat/vs.png'
        align (.5, .5) alpha 0 zoom 1.1
        linear .05 alpha 1 zoom 1.
        linear .05 zoom 1.05
        linear .05 zoom 1.
        linear .05 zoom 1.02
        linear .05 zoom 1.
    contains:
        .55
        '#fff2'
        alpha 0
        linear .1 alpha 1
        linear .1 alpha 0
    contains:
        'art/mini/combat/[what.ref]/left.png'
        xpos -1. yalign 1.
        easein_quart .65 xpos 0.
    contains:
        'art/mini/combat/[what.ref]/right.png'
        xanchor 1. xpos 2. yalign 1.
        easein_quart .65 xpos 1.


style mini_combat_hbox:
    align (.5, .8)
    spacing 5

style mini_combat_fixed:
    xysize (90, 90)

style mini_combat_frame:
    anchor (1.1, .5) pos (.5, .9) xsize .4 padding (15, 8) ysize .05
    background Frame('art/mini/combat/frame.png', 30, 0)

style mini_combat_grid:
    xfill True spacing -15

style mini_combat_image_button:
    padding (175, 175)
    xysize (90, 90)


transform mini_combat_misc:
    on show:
        alpha 0
        linear .2 alpha 1
    on hide:
        linear .2 alpha 0

transform mini_combat_hp(i, npc=False):
    'mini_combat_hp'
    matrixcolor BrightnessMatrix(i * -.1) * ContrastMatrix(1 - i * .1) * (
        HueMatrix(i * -24) if npc else HueMatrix(80 + i * 24))
    on hide:
        linear .2 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
