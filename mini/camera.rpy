screen mini_camera(*args, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'mini_camera'

    default game = saga.mini.camera(*args)

    viewport:
        draggable True
        xadjustment game.x
        xinitial .5
        yadjustment game.y
        yinitial .5

        if game.mode == 'reset':
            at mini_camera_shutter

        fixed:
            fit_first True

            add f'art/mini/camera/{game.shot}.png' zoom game.zoom

    add saga.easy.image('art/mini/camera/frame.png')

    frame:
        bar value game
        text '[game.zoom:.02f]x' alt '' yalign 1 - game.z.value / game.z.range

    if game.size < 1:
        label _('Buffer usage:') + f' {game.size:.0%}'

    else:
        label _('Select a photo to save.')
        label _('BUFFER EXHAUSTED') at mini_camera_notice style_suffix 'notice'

    add game

    vbox:
        for snap in game.pics:
            window:
                at mini_camera_thumb

                imagebutton:
                    action Return(snap)
                    alt _('Thumbnail')
                    at button, mini_camera_snap(*snap)
                    idle f'art/mini/camera/{game.shot}.png'

        imagebutton:
            action (Function(game.take) if game.size < 1 else With(hpunch))
            alt _('Shutter')
            at button
            idle 'art/mini/camera/shutter.png'

    add game.wait


image mini_camera_thumb = Solid('ffffff80', ysize=30)
image mini_camera_zoom = Frame(u('art/mini/camera/zoom.png'), 3, 3)


style mini_camera_bar:
    bar_vertical True
    thumb 'mini_camera_thumb'

style mini_camera_frame:
    anchor (1., .5)
    background 'mini_camera_zoom'
    padding (6, 6)
    pos (.98, .5)
    xysize (36, .95)

style mini_camera_label:
    pos (.02, .025)

style mini_camera_label_text:
    size 22

style mini_camera_notice:
    align (.5, .7)

style mini_camera_notice_text is mini_camera_label_text


style mini_camera_text:
    color 'ffffff80'
    line_leading 2
    line_spacing 3
    size 20
    xanchor 1.
    xpos -10

style mini_camera_vbox:
    anchor (0., 1.)
    pos (.02, .975)
    xsize 175

style mini_camera_window:
    bottom_margin 20


transform mini_camera_notice:
    alpha .8
    ease .75 alpha 1.
    ease .75 alpha .8
    repeat

transform mini_camera_shutter:
    mesh True shader 'saga.wipemiddle' u_warp 0
    linear .1 u_warp 1
    linear .1 u_warp 0
    mesh None shader None

transform mini_camera_snap(x, y, z):
    crop_relative False fit 'contain'
    crop (x / z, y / z, config.screen_width / z, config.screen_height / z)

transform mini_camera_thumb:
    alpha 0 xoffset -20 yzoom 0
    pause .25
    ease .1 yzoom 1
    easein .2 alpha 1 xoffset 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
