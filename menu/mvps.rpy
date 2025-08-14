screen mvps():
    style_prefix 'mvps_menu' tag menu


    use base_menu(esc='team'):
        side 't c':

            label _('Thank you for all your support!')

            viewport:
                draggable True
                edgescroll (250, 375)
                mousewheel True

                text saga.menu.mvps.data


style mvps_menu_label is cast_menu_label


style mvps_menu_label_text is cast_menu_label_text


style mvps_menu_text:
    font saga.menu.mvps.font
    size gui.text_size * .65
    text_align .5
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
