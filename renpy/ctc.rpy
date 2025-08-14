screen ctc():
    style_prefix 'ctc'

    default delay = 5 if _last_say_what else 2

    frame:
        at ctc_appear(delay)

        has hbox
        spacing 3

        text '.' alt '' at ctc_blink(delay + .0, 10)
        text '.' alt '' at ctc_blink(delay + .2, 10)
        text '.' alt '' at ctc_blink(delay + .4, 10)


style ctc_frame:
    align (.97, .97)


transform ctc_appear(delay):
    alpha 0.

    pause delay

    linear .5 alpha 1.

transform ctc_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1. yoffset -2
        pause .2
        linear .2 alpha .5 yoffset 0
        pause (cycle - .4)
        repeat 60 // cycle
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
