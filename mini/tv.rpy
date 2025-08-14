screen tv(what, _sensitive=renpy.get_mode() == 'screen', auto=False):
    layer 'master'
    sensitive _sensitive

    if _sensitive:
        dismiss action Function(renpy.set_editable_input_value, None, False)

    use view(what, _sensitive)

    if _sensitive or auto is not False:
        add saga.easy.image('art/mini/tv/remote.png')

        imagebutton:
            focus_mask True
            at button, saga.easy.placement('art/mini/tv/quit.png')
            idle 'art/mini/tv/quit.png'
            action Emit(app='sys', op='quit')

        imagebutton:
            focus_mask True
            at button, saga.easy.placement('art/mini/tv/prev.png')
            idle 'art/mini/tv/prev.png'
            action Emit(app='sys', op='pgdn')

        imagebutton:
            focus_mask True
            at button, saga.easy.placement('art/mini/tv/next.png')
            idle 'art/mini/tv/next.png'
            action Emit(app='sys', op='pgup')


style tv_info:
    background '#000a'
    color 'ccc'
    outlines ((1, 'ccc', 0, 0),)
    padding (25, 10, 25, 5)
    size 60


transform tv_info:
    anchor (1., 0.)
    pos (1., .03)
    subpixel True
    pause 2.6
    easeout .4 xanchor 0.


screen tv_auth(chan, _sensitive=renpy.get_mode() == 'screen', auto=False):
    style_prefix 'tv_auth'
    sensitive _sensitive

    default inputs = chan.inputs

    default acc = inputs.acc
    default pin = inputs.pin

    if auto:
        for i in range(1, 1 + len(acc.key)):
            timer i * .075 action acc.next

        for i in range(1 + i, 1 + i + len(pin.key)):
            timer i * .075 action pin.next

    elif acc.error:
        timer .275 action SetField(acc, 'error', False)

    elif pin.error:
        timer .275 action SetField(pin, 'error', False)

    add f'art/mini/tv/auth/{chan.ref}.png'

    grid 2 2:
        text _('Account')

        frame:
            modal True

            has button
            key_events True

            if acc.error:
                background '#600'

            elif not auto and not acc.focused:
                action Function(acc.focus, True)
                alt _('Account input')
                at button
                keysym 'any_K_TAB'

            input:
                copypaste True
                pixel_width 280
                value acc

        text _('PIN')

        frame:
            modal True

            has button
            key_events True

            if pin.error:
                background '#600'

            elif not auto and not pin.focused:
                action Function(pin.focus, True)
                alt _('PIN input')
                at button

                if acc.focused:
                    keysym 'any_K_TAB'

            input:
                copypaste True
                pixel_width 280
                value pin


style tv_auth_button:
    background '#111'
    padding (10, 10, 10, 8)
    xsize 300

style tv_auth_frame:
    background '#eee7'
    padding (3, 3)
    xalign .5

style tv_auth_grid:
    align (.5, .65)
    spacing 15
    xanchor .66

style tv_auth_hint:
    size 15
    xalign .5

style tv_auth_input:
    color 'ccc'
    size 20
    ysize 20

style tv_auth_text:
    align (1., .5)
    bold True
    size 22
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
