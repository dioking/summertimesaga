screen core_menu():
    vbox:
        if main_menu:
            textbutton _('Start') action ShowMenu('mode')

        else:
            textbutton _('Resume') action Return()

            if _in_replay:
                textbutton _('End Replay') action EndReplay(confirm=True)
            else:
                textbutton _('Save') action ShowMenu('save')

        if not _in_replay:
            textbutton _('Load') action ShowMenu('load')

        textbutton _('Settings') action ShowMenu('preferences')

        if main_menu:
            textbutton _('Cookie Jar') action ShowMenu('cast')
            textbutton _('Credits') action ShowMenu('team')
            textbutton _('Changelog') action ShowMenu('logs')

        else:
            textbutton _('Main Menu') action MainMenu()

        if renpy.variant('pc'):
            textbutton _('Quit') action Quit(confirm=not main_menu)


style core_menu_button:
    background gui.button_idle
    hover_background gui.button_over
    insensitive_background gui.button_noop
    padding (35, 20, 35, 30)
    selected_background gui.button_live
    xfill True

style core_menu_button_text:
    align (.5, .55)
    font 'acme'
    outlines ((5, '0007', 0, 0),)
    size gui.text_size + 10

style core_menu_vbox:
    spacing 20
    xsize 350
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
