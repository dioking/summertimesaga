screen hud():
    style_prefix 'hud'

    if saga.camera.focus:
        use hud_prop()
    else:
        use hud_main()


screen hud_back(rv=None):
    style_prefix 'hud'

    frame:
        xalign 1.

        has button
        action (Emit(interact=saga.mode.nav) if rv is None else Return(rv))
        alt _('Back')
        at button

        add saga.easy.image('art/mini/hud/back.png')


screen hud_full(label):
    style_prefix 'hud'

    frame:
        xalign 1.

        has button
        action Call(label, from_current=True)
        alt _('Toggle Fullscreen')
        at button

        add saga.easy.image('art/mini/hud/full.png')


screen hud_main():
    frame:
        style_suffix 'time'
        modal True

        has fixed
        xfit True
        yfit True

        add Solid('000', xysize=(320, 33)):
            pos 16, .014

        add saga.easy.image('art/mini/hud/energy1.png') at (
            hud_flip if saga.time.tod > saga.time.dawn else None)

        add saga.easy.image('art/mini/hud/energy2.png') at (
            hud_flip if saga.time.tod > saga.time.noon else None)

        add saga.easy.image('art/mini/hud/energy3.png') at (
            hud_flip if saga.time.tod > saga.time.dusk else None)

        use hud_time(saga.time.dawn)
        use hud_time(saga.time.noon)
        use hud_time(saga.time.dusk)
        use hud_time(saga.time.dark)

    frame:
        has hbox

        button:
            action ShowMenu('game_menu')
            alt _('Pause Menu')
            at button
            add saga.easy.image('art/mini/hud/menu.png')

        null width 10
        label '[saga.time.dow!t]' alt '' xminimum .0875
        null width 10
        label '[saga.camera.what!it]' alt ''

    frame:
        xalign 1.
        has hbox

        label '[saga.camera.track.cash:,]' alt '' style_suffix 'cash'
        null width 10

        button:
            action Emit(interact=saga.mode.tel)
            alt '[saga.gui.tel!t]'
            at button
            add saga.easy.image(f'art/mini/hud/{saga.gui.tel.ref}.png')

        button:
            if hasattr(saga.gui.buy, 'page'):
                action Emit(interact=saga.mode.buy)
                alt '[saga.gui.buy!t]'
                at button
                add saga.easy.image(f'art/mini/hud/{saga.gui.buy.ref}.png')
            else:
                action Emit(interact=saga.mode.inv)
                alt '[saga.gui.inv!t]'
                at button
                add saga.easy.image(f'art/mini/hud/{saga.gui.inv.ref}.png')

        button:
            action Emit(interact=saga.gui.nav)
            alt '[saga.gui.nav!t]'
            at button
            add saga.easy.image(f'art/mini/hud/{saga.gui.nav.ref}.png')


screen hud_prop():
    frame:
        xalign 1.
        has hbox

        if saga.camera.focus is saga.prop.map_town:
            button:
                action Emit(interact=(
                    None if saga.camera.track.where is saga.sets.debbie_bed3
                         else saga.sets.debbie_bed3))
                alt '[saga.sets.debbie_bed3!t]'
                at button
                add saga.easy.image('art/mini/hud/bed.png')

        button:
            action Emit(interact=None)
            alt _('Back')
            at button
            add saga.easy.image('art/mini/hud/back.png')


screen hud_time(time):
    default path = f'art/mini/hud/{time.ref}.png'

    imagebutton:
        action Emit(interact=time)
        alt f'[saga.time.{time.ref}!t]'
        at button, saga.easy.placement(path)
        idle path
        if saga.time.tod is not time:
            insensitive hud_dull(path)
        sensitive saga.time.tod < time


define hud_dull = Transform(matrixcolor=(
    ColorizeMatrix('012', '9ab') * gui.grey))
define hud_flip = Transform(matrixcolor=(
    SaturationMatrix(1.25) * ContrastMatrix(.25) * BrightnessMatrix(-.75)))


image hud_label = Frame('art/mini/hud/box.png', 17, 17)
image hud_cash = Fixed('hud_label', Image(
    'art/mini/hud/cash.png', yalign=.5, xpos=10))


style hud_button:
    xysize (108, 108)

style hud_cash is hud_label:

    background 'hud_cash'
    xminimum .1

style hud_cash_text is hud_label_text:

    xalign 1.

style hud_frame:
    margin (15, 5)

style hud_label:
    background 'hud_label'
    padding (15, 10)
    top_margin 10
    xminimum .2

style hud_label_text:
    size 20

style hud_time:
    padding (10, 0, 10, 10)
    top_margin 5
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
