screen quick():
    zorder 100

    if persistent.quick:
        frame:
            modal True
            style_prefix 'quick'

            has fixed
            fit_first True

            vbox as vb:
                at quick

                textbutton _('Back') action Rollback() selected renpy.roll_forward_info() is not None
                textbutton _('Skip') action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _('Auto') action Preference('auto-forward', 'toggle')

                if not _in_replay:
                    textbutton _('Save') action ShowMenu('save')
                    textbutton _('Q.Save') action QuickSave()
                    textbutton _('Q.Load') action QuickLoad() sensitive saga.menu.slot(1, page='quick') is None

                textbutton _('Prefs') action ShowMenu('preferences')

            mousearea:
                hovered SetTransformEvent(vb, 'hover')
                unhovered SetTransformEvent(vb, 'idle')


style quick_button is default:

    padding (10, 3)
    xalign 1.

style quick_button_text is button_text:

    color '999'
    hover_color 'ccc'
    insensitive_color '333'
    selected_color '399'
    size gui.text_size * .6

style quick_frame:
    xalign 1.
    yanchor 1.
    ypos gui.adv_yalign - gui.adv_height


transform quick:
    blend 'add'
    on idle:
        alpha .25
    on start:
        alpha .25
    on hover:
        alpha 1.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
