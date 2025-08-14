screen game_menu():
    style_prefix 'game_menu' tag menu


    fixed:
        at blur(20)

        add saga.easy.image('art/menu/main/base.png')
        add saga.easy.image('art/menu/main/clouds1.png')
        add saga.easy.image('art/menu/main/clouds2.png')
        add saga.easy.image('art/menu/main/trees.png')
        add Solid('000000bf')

    use core_menu


define _game_menu_screen = 'game_menu'


style game_menu_button is core_menu_button


style game_menu_button_text is core_menu_button_text


style game_menu_vbox is core_menu_vbox:

    align (.5, .5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
