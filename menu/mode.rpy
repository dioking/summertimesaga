screen mode():
    style_prefix 'mode_menu' tag menu


    use base_menu(shade=False):
        side 't c':

            label _('Mode Select') style_suffix 'title'

            grid 3 1:

                button:
                    action ShowMenu('name', 'anon', 'start.cheat')
                    at Transform(xalign=1., ypos=.3, zoom=.85)
                    has vbox
                    label _('Preview') text_line_spacing 2
                    text _('Start with money and stats as there is no '
                       'way to earn them yet. Extra money can be found in the '
                       'ATM in the bank. More content will be restored in '
                       'future releases.') line_spacing 14

                button:
                    action ShowMenu('name', 'anon', 'start')
                    at Transform(alpha=.5, matrixcolor=SaturationMatrix(0))
                    sensitive False
                    has vbox
                    label _('Normal')
                    text _('Not yet available')
                    text _('Start from the beginning')
                    text _('No money in the bank')
                    text _('Start with base stats')

                button:
                    action ShowMenu('name', 'anon', 'start.recap')
                    at Transform(alpha=.5, xalign=0., ypos=.3, zoom=.85,
                             matrixcolor=SaturationMatrix(0))
                    sensitive False
                    has vbox
                    label _('Recap')
                    text _('Not yet available')
                    text _('New since last update')
                    text _('Money in the bank')
                    text _('Play with boosted stats')


style mode_menu_button is core_menu_frame:

    background gui.box
    padding (50, 50)

style mode_menu_grid:
    align (.5, .3)
    margin (200, 0)
    spacing 50
    xfill True

style mode_menu_label is core_menu_button


style mode_menu_label_text is core_menu_button_text


style mode_menu_side:
    yfill True

style mode_menu_text:
    size 26
    xalign .5

style mode_menu_title is cast_menu_label


style mode_menu_title_text is cast_menu_label_text


style mode_menu_vbox:
    spacing 50
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
