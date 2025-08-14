screen xray(_sensitive=renpy.get_mode() != 'start'):
    style_prefix 'mini_xray'

    if _sensitive:
        imagebutton:
            action ToggleField(persistent, 'xray', 0b11, 0b10)
            alt 'X-ray: [text]'
            at button
            idle saga.easy.image('art/mini/xray/hide.png')
            selected_idle saga.easy.image('art/mini/xray/show.png')
            selected_hover saga.easy.image('art/mini/xray/show.png')


style mini_xray_image_button:
    margin (10, 10)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
