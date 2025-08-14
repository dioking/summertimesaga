screen main_menu():
    style_prefix 'main_menu' tag menu


    on 'replace' action Play('music', config.main_menu_music,
                             fadein=.7, fadeout=.7, if_changed=True)

    add saga.easy.image('art/menu/main/base.png')

    add main_menu_cloud('art/menu/main/clouds1.png', 184) id 'clouds1'
    add main_menu_cloud('art/menu/main/clouds2.png', 180) id 'clouds2'

    add saga.easy.image('art/menu/main/trees.png')

    add 'main_menu_leaves' id 'leaves'

    add saga.easy.image('art/menu/main/text.png')

    frame:
        use core_menu()

    label '[config.version]'


image main_menu_leaves:
    anchor (.25, 0.)
    pos (.64, 0.)
    rotate 12
    rotate_pad False
    transform_anchor True
    contains:
        SnowBlossom(Animation(saga.easy.image('art/menu/main/leaf1.png'), .75,
                              saga.easy.image('art/menu/main/leaf2.png'), .75))
        crop (0, 0, .5, .7)


style main_menu_button is core_menu_button


style main_menu_button_text is core_menu_button_text


style main_menu_frame:
    background gui.menu
    xalign 1.
    xsize .31
    yfill True

style main_menu_label:
    align (1., 1.)
    padding (5, 5)

style main_menu_label_text:
    outlines ((1, '0007', 0, 0),)
    size 15

style main_menu_vbox is core_menu_vbox:

    align (.5, .5)


transform main_menu_cloud(child, t):
    instant renpy.random.randint(10 - t, -10)
    child
    subpixel True
    yoffset saga.easy.placement(child).yoffset
    block:
        xanchor 1. xpos 0.
        linear t xanchor 0. xpos 1.
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
