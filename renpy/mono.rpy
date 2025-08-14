screen mono_text(who, what):
    style_prefix 'mono'

    window:
        id 'window'

        text what id 'what' style_suffix 'think'


style mono_think:
    align (.5, .5)
    layout 'subtitle'
    line_spacing 5
    text_align .5

style mono_window:
    align (.5, 1.)
    xpadding 50
    ysize .2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
