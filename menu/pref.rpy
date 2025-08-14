screen preferences():
    style_prefix 'pref_menu' tag menu


    use base_menu():
        side 't c b':

            window:
                has hbox

                textbutton _('Display') style_suffix 'label':
                    action SetField(persistent, 'pref', 'display')
                    at button
                textbutton _('Sound') style_suffix 'label':
                    action SetField(persistent, 'pref', 'sound')
                    at button

                if renpy.variant('touch'):
                    textbutton _('Controls') style_suffix 'label':
                        action SetField(persistent, 'pref', 'controls')
                        at button

                textbutton _('Gameplay') style_suffix 'label':
                    action SetField(persistent, 'pref', 'gameplay')
                    at button

                if persistent.cheats > 6:
                    textbutton _('Cheats') style_suffix 'label':
                        action SetField(persistent, 'pref', 'cheats')
                        at button

                textbutton _('Accessibility') style_suffix 'label':
                    action SetField(persistent, 'pref', 'a11y')
                    at button

            vpgrid:
                cols 2
                mousewheel True
                scrollbars 'vertical'
                side_spacing style.pref_menu_vpgrid.spacing

                if persistent.pref == 'a11y':

                    label _('Text') style_suffix 'group'
                    null

                    text _('Font override')
                    use cycle(_preferences, 'font_transform', reset=True, opts={
                    None: _('Disabled'), 'opendyslexic': _('OpenDyslexic')})

                    text _('Text scaling')
                    bar:
                        at button
                        value Preference('font size')

                    text _('Line spacing')
                    bar:
                        at button
                        value Preference('font line spacing')

                    text _('High contrast text')
                    button:
                        action Preference('high contrast text', 'toggle')
                        at button
                        style_suffix 'toggle'

                    label _('Audio') style_suffix 'group'
                    null

                    text _('Self-voicing')
                    use cycle(_preferences, 'self_voicing', opts={
                    False: _('Disabled'), True: _('Text-to-speech'),
                    'clipboard': _('Clipboard')})

                    text _('Self-voicing volume drop')
                    bar:
                        at button
                        value Preference('self voicing volume drop')

                    textbutton _('Restore defaults'):
                        action (Preference('font transform', None),
                            Preference('font size', 1.),
                            Preference('font line spacing', 1.),
                            Preference('high contrast text', 'disable'),
                            Preference('self voicing', 'disable'),
                            Preference('self voicing volume drop', .5))
                        selected False
                    null

                elif persistent.pref == 'cheats':

                    label _('Cookie Jar') style_suffix 'group'
                    null

                    text _('Unlock all')
                    button:
                        action ToggleField(persistent, 'cookies')
                        at button
                        style_suffix 'toggle'
                        tooltip _("This will not impact your save data. Turning "
                              "this option off will revert to showing only "
                              "those scenes you have unlocked legitimately.")

                    textbutton _('Disable cheats'):
                        action (SetField(persistent, 'cheats', 0),
                            SetField(persistent, 'cookies', False),
                            SetField(persistent, 'pref', 'gameplay'))
                        selected False
                    null

                elif persistent.pref == 'controls':

                    label _('Visual Novel') style_suffix 'group'
                    null

                    text _('Rollback side')
                    use cycle(_preferences, 'mobile_rollback_side', opts={
                    'disable': _('Disabled'), 'left': _('Left'),
                    'right': _('Right')})

                elif persistent.pref == 'display':

                    if renpy.variant(('pc', 'web')):
                        label _('Window') style_suffix 'group'
                        null

                        text _('Fullscreen')
                        button:
                            action Preference('display', 'toggle')
                            at button
                            style_suffix 'toggle'

                    if renpy.variant('pc'):
                        textbutton _('Reset size'):
                            action (SetField(_preferences, 'maximized', False),
                                Function(renpy.reset_physical_size))
                            selected False
                            sensitive not preferences.fullscreen
                        null

                    label _('Features') style_suffix 'group'
                    null

                    text _('Button outlines')
                    button:
                        action ToggleField(persistent, 'outlines')
                        at button
                        style_suffix 'toggle'
                        tooltip _("Adds outlines around buttons making them "
                              "easier to spot at the expense of visuals.\n\n"
                              "Turn this off to have a more pleasant viewing "
                              "experience.")

                elif persistent.pref == 'gameplay':

                    label _('Features') style_suffix 'group'
                    null

                    text _('Difficulty')
                    use cycle(persistent, 'mode', opts={
                    'easy': _('Easy (Skip mini games)'), 'hard': _('Normal')})

                    text _('Reveal pregnancy')
                    button:
                        action ToggleField(persistent, 'conception')
                        at button
                        style_suffix 'toggle'
                        tooltip _("Enables the wheel of conception, allowing the "
                              "player to see the result of pregnancy attempts "
                              "immediately.\n\n"
                              "Turn this off to learn about pregnancies at "
                              "the same time as the characters.")

                    text _('X-Rays')
                    use cycle(persistent, 'xray', opts={
                    0b00: _('Never'), 0b10: _('Off'), 0b11: _('On')})

                    label _('Visual Novel') style_suffix 'group'
                    null

                    text _('Show quick menu')
                    button:
                        action ToggleField(persistent, 'quick')
                        at button
                        style_suffix 'toggle'
                        tooltip _("Adds various controls to the bottom of the "
                              "dialogue window that can be useful to those "
                              "playing on touch screen devices.")

                    text _('Skip unseen text')
                    button:
                        action Preference('skip', 'toggle')
                        at button
                        style_suffix 'toggle'

                    text _('Skip after choices')
                    button:
                        action Preference('after choices', 'toggle')
                        at button
                        style_suffix 'toggle'

                    text _('Text speed')
                    bar:
                        at button
                        value Preference('text speed')

                    text _('Auto-forward time')
                    bar:
                        at button
                        value Preference('auto-forward time')

                elif persistent.pref == 'sound':

                    label _('Overall') style_suffix 'group'
                    null

                    text _('Volume')
                    bar:
                        at button
                        value Preference('main volume')

                    text _('Mute')
                    button:
                        action Preference('all mute', 'toggle')
                        at button
                        style_suffix 'toggle'

                    if renpy.variant('pc'):
                        label _('Auto-mute') style_suffix 'group'
                        null

                        text _('On minimise')
                        button:
                            action InvertSelected(Preference(
                            'audio when minimized', 'toggle'))
                            at button
                            style_suffix 'toggle'

                        text _('On focus loss')
                        button:
                            action InvertSelected(Preference(
                            'audio when unfocused', 'toggle'))
                            at button
                            style_suffix 'toggle'

                    label _('Volume') style_suffix 'group'
                    null

                    text _('Music')
                    bar:
                        at button
                        value Preference('music volume')

                    text _('Effects')
                    bar:
                        at button
                        value Preference('sound volume')

            if persistent.pref == 'a11y':
                text _('The options on this menu are intended to improve '
                   'accessibility. Some combinations of options may '
                   'render the game unplayable. This is not an issue '
                   'with the game or engine. For the best results when '
                   'changing fonts, try to keep the text size the same '
                   'as it originally was.') style_suffix 'note'

            else:
                null

    if (tooltip := GetTooltip()):
        nearrect:
            focus 'tooltip'

            has frame style_suffix 'tooltip'

            text "[tooltip]" style_suffix 'tip'


screen cycle(ns, ref, opts, *, reset=False):
    $ prev, name, next = saga.menu.pref(ns, ref, opts, reset=reset)

    side 'l c r':
        style_suffix 'cycle'
        imagebutton idle gui.left action prev at button
        text name xalign .5
        imagebutton idle gui.right action next at button


style pref_menu_toggle:
    align (1., .5)
    background gui.frame
    selected_background gui.check
    xysize (50, 50)

style pref_menu_button_text is pref_menu_text:

    color gui.text_color + '7'
    hover_color gui.text_color + 'a'
    insensitive_color gui.text_color + '4'

style pref_menu_cycle:
    spacing 10
    xfill True
    yfill True

style pref_menu_group:
    yminimum 59

style pref_menu_group_text is pref_menu_text:

    color gui.accent_color
    outlines ((2, gui.shade_color, 0, 0),)
    size gui.text_size
    yalign .5

style pref_menu_hbox:
    spacing 40
    xalign .5

style pref_menu_image_button:
    yalign .5

style pref_menu_label is cast_menu_label


style pref_menu_label_text is cast_menu_label_text:

    color gui.accent_color
    selected_color gui.text_color

style pref_menu_note is pref_menu_window:

    color gui.text_color + '7'
    size gui.text_size * .9

style pref_menu_slider:
    left_bar gui.full
    left_gutter 10
    right_bar gui.empty
    right_gutter 10
    thumb 'art/menu/pref/thumb.png'
    thumb_offset 10
    ysize 59

style pref_menu_text:
    size gui.text_size * .9
    yalign .5

style pref_menu_tip:
    color gui.text_color + '7'
    size gui.text_size * .9

style pref_menu_tooltip:
    background gui.frame
    offset (20, -50)
    padding (20, 20)
    xanchor 0.
    xpos 1.
    xsize 370

style pref_menu_vpgrid:
    bottom_margin 30
    left_margin 40
    spacing 20
    xfill True
    xmaximum 1140

style pref_menu_vscrollbar:
    base_bar '#0007'
    thumb '#' + gui.text_color + '3'
    unscrollable 'hide'
    xsize style.pref_menu_vpgrid.left_margin - style.pref_menu_vpgrid.spacing

style pref_menu_window:
    xpos style.pref_menu_vpgrid.left_margin
    xsize style.pref_menu_vpgrid.xmaximum - style.pref_menu_vpgrid.left_margin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
