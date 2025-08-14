screen skip_indicator():
    style_prefix 'skip'
    zorder 100

    frame:
        has hbox
        spacing 6

        text _('Skipping')

        text '▸' alt '' at skip_blink(.0, 1)
        text '▸' alt '' at skip_blink(.2, 1)
        text '▸' alt '' at skip_blink(.4, 1)


style skip_frame is notify_label:

    ypos .125

style skip_text is notify_label_text



transform skip_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.
        pause .2
        linear .2 alpha .5
        pause (cycle - .4)
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
