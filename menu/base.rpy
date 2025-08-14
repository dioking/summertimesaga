screen base_menu(esc=None, shade=True):
    style_prefix 'base_menu'

    fixed:
        at blur(20)

        add saga.easy.image('art/menu/main/base.png')
        add saga.easy.image('art/menu/main/clouds1.png')
        add saga.easy.image('art/menu/main/clouds2.png')
        add saga.easy.image('art/menu/main/trees.png')

        if shade:
            add Solid('000000bf')

    use base_menu_back(esc)

    window:
        transclude


screen base_menu_back(esc=None):
    style_prefix 'base_menu'

    frame:
        has button
        action (ShowMenu(esc) if esc else Return())
        alt _('Back')
        at button
        keysym 'game_menu'
        add saga.easy.image('art/mini/hud/back.png') xzoom -1


style base_menu_button is hud_button


style base_menu_frame is hud_frame


style base_menu_window:
    margin (25, 25)
    xalign .5
    yfill True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
