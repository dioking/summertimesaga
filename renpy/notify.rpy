screen notify(stack):
    style_prefix 'notify'
    zorder 100

    vbox:
        for ref, (message, clear) index ref in stack.items():
            label '[message!t]' at _notify_transform(clear)


style notify_label:
    background '#0007'
    padding (15, 15, 20, 15)
    bottom_margin 5

style notify_label_text is gui_text:

    size gui.text_size * .65

style notify_vbox:
    ypos .26


transform _notify_transform(clear):
    alpha 0.
    linear .25 alpha 1.
    pause 3.25
    linear .25 alpha 0.
    linear .25 yzoom 0.
    function clear
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
