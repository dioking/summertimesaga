screen mini_womb(who, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive

    default game = saga.mini.womb(who.womb)

    add saga.easy.image('art/mini/womb/base.png'):
        alt _('Spin the wheel of conception!')

    if who.baby:
        dismiss action Return(who.baby.kind.none)

        add saga.easy.image('art/mini/womb/empty.png') alt _('No egg?!')

    elif game.mode is None:
        add saga.easy.image('art/mini/womb/mark.png')

        fixed at game.spin:
            add saga.easy.image('art/mini/womb/wheel.png')

        if game.wait:
            add game.wait

        else:
            imagebutton:
                action Function(game.begin)
                alt _('Spin')
                at button, saga.easy.placement('art/mini/womb/spin.png')
                idle 'art/mini/womb/spin.png'

    else:
        dismiss action Return(game.kind)

        if game.kind:
            add saga.easy.image('art/mini/womb/hit.png') alt _('Fertilized')
        else:
            add saga.easy.image('art/mini/womb/miss.png') alt _('Wasted')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
