screen name(ref, mode=None):
    style_prefix 'name_menu' tag menu


    default name = saga.menu.name(ref, mode)

    showif name.focused:
        dismiss action Function(name.focus, False)

    add saga.easy.ref('forest_main') at stage
    add saga.easy.ref(ref)
    add saga.easy.image('art/menu/name/base.png')

    hbox:
        frame:
            modal True

            has button
            key_events True
            style_suffix 'input_button'

            if not name.focused:
                action Function(name.focus, True)
                alt _('Edit name')
                at button
                keysym 'K_TAB'

            input:
                allow printable
                copypaste True
                exclude '[]{}'
                length 12
                value name

        window:
            modal True

            has button
            action Function(name.enter)
            alt _('Start!')
            at name_menu_button
            selected False
            sensitive name.text.strip()
            add gui.right

    if mode:
        use base_menu_back('mode')


style name_menu_button is core_menu_button:

    margin (5, -3)
    padding (32, 25, 30, 35)
    xalign .5
    xfill False

style name_menu_frame:
    background gui.frame

style name_menu_hbox:
    align (.5, .85)
    xsize 500

style name_menu_input:
    color 'eee'
    xalign .5

style name_menu_input_button:
    padding (15, 25)
    xfill True


transform name_menu_button:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor gui.over
    on insensitive:
        matrixcolor gui.grey
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
