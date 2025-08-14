screen nav(what, _sensitive=renpy.get_mode() == 'screen'):
    style_prefix 'nav'
    layer 'master'
    sensitive _sensitive

    default esc = saga.camera.last if what.esc is True else what.esc

    use view(what, _sensitive)

    if _sensitive:
        if esc:
            textbutton '[esc.alt or esc!it]' action Emit(interact=esc) at button

        use hud()


style nav_button:
    anchor (.5, 1.)
    background '#1e1e2dcc'
    padding (15, 10)
    pos (.5, .99)
    xminimum .2

style nav_button_text:
    size 24
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
