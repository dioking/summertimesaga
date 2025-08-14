screen logs():
    style_prefix 'logs_menu' tag menu


    default keys = saga.menu.logs.keys()
    default log = next(iter(saga.menu.logs))
    default scroll = ui.adjustment()

    use base_menu():
        side 't c':

            label _('Changelog')

            vbox:
                hbox:
                    for v in keys:
                        textbutton v action (SetScreenVariable('log', v),
                                         Function(scroll.change , 0))
                    textbutton _('Older') action SetScreenVariable('log', None)

                viewport:
                    draggable True
                    mousewheel True
                    scrollbars 'vertical'
                    yadjustment scroll

                    if log:
                        text saga.menu.logs[log] substitute False
                    else:
                        text _('Older changelog entries can be found on the '
                           'official wiki.')


style logs_menu_button_text is pref_menu_button_text:

    selected_color '4091fc'

style logs_menu_group is logs_menu_text:

    color gui.text_color + 'd'
    italic True

style logs_menu_hbox:
    box_wrap True
    spacing 50

style logs_menu_label is cast_menu_label


style logs_menu_label_text is cast_menu_label_text


style logs_menu_text:
    color gui.text_color + 'a'
    line_spacing 2
    size gui.text_size * .8

style logs_menu_vbox:
    spacing 30

style logs_menu_vscrollbar is pref_menu_vscrollbar
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
