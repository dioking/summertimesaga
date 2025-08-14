screen inv(what, _sensitive=renpy.get_mode() == 'screen'):
    style_prefix 'inv'
    layer 'master'
    sensitive _sensitive

    default content = what.sift(saga.prop, sort=True)
    default length = len(content)

    default prev = f'art/mini/inv/{what.ref}/prev.png'
    default next = f'art/mini/inv/{what.ref}/next.png'

    default c = 8
    default r = 4
    default s = c * r
    default l = max(0, ~(length // -s))
    default px = 185

    $ page = what.page = min(what.page, l)
    $ tooltip = GetTooltip()

    add saga.easy.ref(saga.camera.track.where.ref) at stage
    add saga.easy.image(f'art/mini/inv/{what.ref}/base.png')

    window:
        xysize (c * px, r * px + 174)

        has vbox

        grid c r:
            allow_underfull True

            for p in content[page * s:][:s]:
                $ png = f'art/prop/{p.ref}/icon.png'

                button:
                    action MaybeEmit(interact=p)
                    alt p
                    tooltip p
                    xysize (px, px)

                    has fixed

                    add saga.easy.outline(png, color='0009'):
                        at saga.easy.placement(png)

            if not length:
                null height px width px

        null height 5

        frame:
            has vbox

            if tooltip:
                label '[tooltip.name!it]'
                null height 8
                text '[tooltip.note!it]'
            else:
                text _('Hover over an item to see more information.'):
                    italic True

    imagebutton:
        action Emit(op='pgdn')
        alt _('Previous page')
        at button, saga.easy.placement(prev)
        idle prev
        insensitive Transform(alpha=.5, child=prev)
        sensitive page > 0

    imagebutton:
        action Emit(op='pgup')
        alt _('Next page')
        at button, saga.easy.placement(next)
        idle next
        insensitive Transform(alpha=.5, child=next)
        sensitive page * s + s < length


style inv_button:
    hover_background '#0002'

style inv_fixed:
    align (.5, .5)
    xysize (176, 176)

style inv_frame:
    margin (15, 10)

style inv_text:
    line_leading 2
    size gui.text_size * .84375

style inv_window:
    align (.5, .5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
