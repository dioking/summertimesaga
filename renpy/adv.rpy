screen adv(who, what, lang=None):
    style_prefix 'adv'

    window:
        id 'window'
        has vbox id 'vbox'

        text who or '' id 'who' style_suffix 'label'

        if lang:
            text lang id 'lang' style_suffix 'speak':
                alt '' slow not renpy.suppress_transition() slow_abortable True
            text what id 'what' style_suffix 'think':
                alt _('In another language, [text]')

        else:
            text what id 'what' style_suffix 'speak'


style adv_label:
    properties gui.text_properties('name')
    font 'acme'
    line_spacing gui.name_spacing
    outlines ((3, '000a', 0, 0),)
    size gui.text_size * 1.5
    xpos gui.name_xpos
    yalign .5

style adv_speak:
    properties gui.text_properties('speak')
    line_leading 5
    outlines ((1, '0007', 0, 0),)

style adv_think is adv_speak:

    properties gui.text_properties('think')
    italic True

style adv_vbox:
    xfill True

style adv_window:
    align (.5, gui.adv_yalign)
    background gui.window
    padding gui.adv_padding
    xfill True
    yminimum gui.adv_height
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
