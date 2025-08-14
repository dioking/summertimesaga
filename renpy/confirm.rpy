screen confirm(message, yes_action, no_action, yes_text=None, no_text=None):
    modal True
    style_prefix 'confirm'

    default url = 'https://www.patreon.com/summertimesaga'

    if message == gui.GAME_OVER:
        add 'art/menu/asks/condom.png'
    elif message == gui.DELETE_SAVE or message == gui.OVERWRITE_SAVE:
        add 'art/menu/asks/trash.png'
    else:
        add 'art/menu/asks/tissue.png'

    vbox:
        label message

        hbox:
            textbutton yes_text or _('Yes'):
                action yes_action
                selected False

            textbutton no_text or _('No'):
                action no_action
                keysym 'game_menu'
                selected False

    vbox:
        style_suffix 'plug'

        imagebutton:
            action OpenURL(url)
            at button
            idle u('art/menu/misc/patreon.png')
            xalign .5

        null height 20

        text _('To support the continued development of this game you can '
               'go to:')
        text '{a=[url]}[url]{/a}'
        text _('Thank you!')


style confirm_button is core_menu_button:

    xsize 250

style confirm_button_text is core_menu_button_text


style confirm_hbox:
    spacing 100
    xalign .5

style confirm_label:
    xalign .5

style confirm_label_text:
    layout 'subtitle'
    text_align .5

style confirm_plug:
    anchor (.5, 1.)
    pos (.5, .975)

style confirm_text:
    color gui.text_color + '7'
    line_spacing 5
    size gui.text_size * .75
    xalign .5

style confirm_vbox:
    anchor (.5, 0.)
    pos (.5, .525)
    spacing 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
