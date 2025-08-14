screen gate():
    style_prefix 'gate_menu' tag menu


    add Solid(gui.menu_color)
    add saga.easy.image('art/menu/misc/logo.png') alt '[config.name!t]'

    frame:
        has side 'l c'

        window:
            has vbox
            add 'art/menu/gate/cert.png' alt '18+'
            text _('MATURE CONTENT')

        vbox:
            label _('I am 18 years of age or older.')
            grid 2 1:
                at Transform(zoom=.65)
                textbutton _('Yes') action Return()
                textbutton _('No') action Quit(confirm=False)


style gate_menu_button is core_menu_button:

    xsize 200
    bottom_margin -10

style gate_menu_button_text is core_menu_button_text


style gate_menu_frame:
    anchor (.5, .5)
    background Frame('art/menu/gate/box.png', 30, 30)
    padding (25, 25, 24, 24)
    pos (.5, .85)

style gate_menu_grid:
    spacing 20
    xalign .5

style gate_menu_label:
    margin (60, 0, 60, 10)

style gate_menu_label_text:
    size gui.text_size * .65

style gate_menu_text:
    color '4a4c54'
    kerning 1.
    layout 'subtitle'
    line_leading 2
    line_spacing 1
    outlines ((1, '4a4c5422', 0, 0),)
    size gui.text_size * .25
    text_align .5
    xalign .5
    xmaximum 115

style gate_menu_vbox:
    align (.5, .5)

style gate_menu_window:
    background '#fff'
    padding (1, 1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
