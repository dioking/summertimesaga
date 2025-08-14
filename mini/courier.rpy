screen mini_courier(_sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini'

    default game = saga.mini.courier()

    for p, t in game.shot:
        add saga.easy.image(f'art/mini/courier/{p}.png') at mini_courier_pan(t)

    for h index h in game.road:
        add h

    label _('Click the matching pizza as you pass a house to deliver it!')

    add game.wait

    showif game.mode:
        add game.ride at mini_courier_ride1, mini_courier_ride2

        hbox:
            at mini_courier_hide
            style_prefix 'mini_courier'

            for pizza, state in game.pies.items():
                imagebutton:
                    idle f'art/mini/courier/pizza/{pizza}.png'

                    if state is None:
                        action Function(game.throw, pizza)
                        at button
                        keysym f'K_{pizza}', f'K_KP_{pizza}'

                    elif state is True:
                        foreground saga.easy.image('art/mini/courier/pass.png')

                    elif state is False:
                        foreground saga.easy.image('art/mini/courier/fail.png')


style mini_courier_hbox:
    align (.99, .99)
    spacing 5


transform mini_courier_hide:
    on hide:
        mesh True
        linear .2 alpha 0

transform mini_courier_pan(t):
    subpixel True xanchor 0. xtile 3
    linear t * .75 xanchor 1 / 3
    repeat

transform mini_courier_ride1:
    function saga.mini.courier.jitter

transform mini_courier_ride2:
    on show:
        easein 3. xpos .5
    on appear:
        easein 3. xpos .5
    on hide:
        easeout 3. xpos 1.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
