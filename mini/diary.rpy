screen diary(what, _sensitive=renpy.get_mode() == 'screen'):
    style_prefix 'diary'

    default data = what.read()
    default max = len(data) - 1
    default page = min(what.page, max)

    add saga.easy.ref('debbie_bed2', 'base') at stage(.6, .7, 4.5)

    fixed:
        add saga.easy.image('art/mini/diary/base.png')

        if renpy.variant('small'):
            align (.5, .675) at Transform(zoom=1.45)

        if _sensitive:
            if page > 0:
                imagebutton:
                    action Emit(op='pgdn')
                    at button
                    idle 'art/mini/diary/button.png'
                    keysym 'viewport_leftarrow'
                    xalign .165

            if page < max:
                imagebutton:
                    action Emit(op='pgup')
                    at button, Transform(xzoom=-1)
                    idle 'art/mini/diary/button.png'
                    keysym 'viewport_rightarrow'
                    xalign .835


        frame:
            text str(page + 26) style_suffix 'page'

            for i, line in enumerate(data[page], 1):
                text line:
                    ypos 55 * i


style art_diary_text:
    size 35
    yoffset 40

style rt_diary_text:
    size 35
    yoffset -18

style diary_frame:
    anchor (.5, 0.)
    pos (.585, .245)
    xysize (.3, .65)

style diary_image_button:
    yalign .5

style diary_text:
    altruby_style style.art_diary_text
    anchor (.5, renpy.BASELINE)
    antialias True
    color '#111111'
    font 'abct'
    layout 'nobreak'
    outlines ((absolute(1), '#1111110f', absolute(0), absolute(0)),)
    ruby_style style.rt_diary_text
    size 42
    xalign .5

style diary_page:
    anchor (1., 1.)
    color '#3336'
    kerning -1
    pos (.95, .95)
    size 20
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
