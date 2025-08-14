screen choice(items):
    style_prefix 'choice'

    vbox:
        for i in items:
            if not i.args or i.args[0]:
                textbutton '[i.caption!it]' action i.action at button
            elif len(i.args) == 2:
                textbutton '[i.caption!it] [[[i.args[1]]]'
            else:
                textbutton '[i.caption!it]'


style choice_vbox:
    xalign .5 yanchor .5 ypos .45
    spacing 20

style choice_button:
    background gui.choice
    padding (100, 10)
    xsize .5

style choice_button_text:
    insensitive_color gui.text_color + '9'
    layout 'subtitle'
    text_align .5
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
