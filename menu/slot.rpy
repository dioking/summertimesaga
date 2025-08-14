screen slot_menu():
    style_prefix 'slot_menu'

    default mode = renpy.current_screen().screen_name[0]
    default name = __('Save') if mode == 'save' else __('Load')
    default nuke = __('Delete')

    use base_menu():
        vbox:

            label name

            hbox:
                button:
                    action FilePagePrevious()
                    at button
                    background None

                    add gui.left align (.5, .5)

                if config.has_autosave or config.has_quicksave:
                    hbox:
                        style_suffix 'pages'
                        if config.has_autosave:
                            textbutton _('A{#auto_page}') action FilePage('auto')
                        if config.has_quicksave:
                            textbutton _('Q{#quick_page}') action FilePage('quick')

                hbox:
                    style_suffix 'pages'
                    $ lower = max(1, int(FilePageName(0, 0)) - 4)
                    for page in range(lower, lower + 9):
                        textbutton '[page]' action FilePage(page)

                button:
                    action FilePageNext()
                    at button
                    background None

                    add gui.right align (.5, .5)

            $ page = FileCurrentPage()

            grid 3 2:
                for slot in range(1, 7):
                    python:
                        date = FileTime(slot, empty=__('{i}empty slot{/i}'),
                                          format=__('{#date_fmt}%B %d, %H:%M'))
                        desc = f'{page}-{slot}. {date}'
                        verb = name
                        void = None

                        if file := FileLoadable(slot):
                            note = FileSaveName(slot)
                            
                            if mode == 'save':
                                verb = __('Overwrite')
                            else:
                                void = saga.menu.slot(slot)
                            
                            shot_idle = FileScreenshot(slot, empty=null)
                            shot_over = Transform(shot_idle, matrixcolor=gui.over)
                            
                            slot_nuke = FileDelete(slot)

                    vbox:
                        style_prefix 'slot_each'

                        label desc alt ''

                        frame:
                            has fixed

                            button:
                                alt f'{verb} {page}-{slot}. [text]'

                                if not void:
                                    action FileAction(slot)

                                if mode == 'save' and not page == 'auto':
                                    alternate Show('slot_note', None, slot)

                                if file:
                                    background shot_idle
                                    hover_background shot_over

                                    if void:
                                        at slot_void
                                        label _('Saves made in [void!q] are not '
                                            'usable in this version.'):
                                            style_suffix 'void'

                                    elif note:
                                        label '[note!q]' style_suffix 'note'

                                    key 'save_delete' action slot_nuke

                            if file:
                                button:
                                    action slot_nuke
                                    alt f'{nuke} {page}-{slot}'
                                    at button
                                    style_suffix 'delete'

                                    has fixed

                                    text '\u2718' style_suffix 'delete_text'
                                    key 'save_delete' action slot_nuke


            if mode == 'load':
                text _('Select a save to load.')
            elif page == 'auto':
                text _('It is not possible to manually save in autosave slots.')
            elif renpy.variant('touch'):
                text _('Long press to save with a caption.')
            else:
                text _('Right-click to save with a caption.')


screen slot_note(slot):
    modal True
    style_prefix 'slot_note'

    default file = FileLoadable(slot)
    default note = FileSaveName(slot) or \
                   f'{saga.cast.anon} - Day {saga.time.date}'
    default okay = _('Overwrite') if file else _('OK')

    window:
        has vbox

        label _('Enter a note to help recognise this save:')

        frame:
            xsize 555
            input:
                allow printable
                alt '[text!q]'
                copypaste True
                pixel_width 515
                value ScreenVariableInputValue('note')

        hbox:
            textbutton okay:
                action (SetField(store, 'save_name', note.strip()),
                        FileSave(slot, confirm=False),
                        SetField(store, 'save_name', ''), Hide())
                alt okay
                keysym 'input_enter'
                selected False
                sensitive note.strip()

                if file:
                    at Transform(matrixcolor=HueMatrix(120))

            textbutton _('Cancel'):
                action Hide()
                keysym 'game_menu'


style slot_each_button:
    xysize (config.thumbnail_width, config.thumbnail_height)

style slot_each_delete:
    align (1., 0.)
    padding (5, 0)

style slot_each_delete_text:
    color 'd33'
    outlines ((2, '000', 0, 0),)

style slot_each_fixed:
    fit_first True

style slot_each_frame:
    background gui.frame
    padding (8, 8)

style slot_each_label:
    margin (0, 0, 0, 5)

style slot_each_label_text:
    size gui.text_size * .65

style slot_each_note:
    align (.5, 1.)
    background '#0007'
    xfill True
    ysize round(config.thumbnail_height * gui.adv_height)

style slot_each_note_text:
    align (.5, .5)
    hinting 'auto'
    outlines ((2, '000', 0, 0),)
    size gui.text_size * .55

style slot_each_void is slot_each_note:

    ypadding 10
    ysize None

style slot_each_void_text is slot_each_note_text:

    layout 'subtitle'
    textalign .5

style slot_menu_button is core_menu_button:

    padding (20, 20, 20, 30)
    xfill False
    xminimum 85

style slot_menu_button_text is core_menu_button_text:

    selected_bold True
    size gui.text_size * .75

style slot_menu_grid:
    align (.5, .5)
    margin (0, 50)
    spacing 80

style slot_menu_hbox:
    spacing 20
    xalign .5

style slot_menu_label is cast_menu_label


style slot_menu_label_text is cast_menu_label_text


style slot_menu_pages:
    spacing 8

style slot_menu_text:
    xalign .5

style slot_note_button is core_menu_button:

    xfill False

style slot_note_button_text:
    size gui.text_size * .75

style slot_note_frame:
    background '#0007'
    margin (0, 25)
    padding (20, 15)

style slot_note_hbox:
    spacing 50
    xalign .5

style slot_note_input:
    size gui.text_size * .75

style slot_note_label_text:
    size gui.text_size * .75

style slot_note_window:
    align (.5, .5)
    background Fixed(Window('#124', margin=(5, 5)), gui.frame)
    fit_first True
    padding (25, 35)


transform slot_void:
    matrixcolor gui.grey
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
