screen mini_atm(who, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'atm'

    default game = saga.mini.atm(who)

    add saga.easy.image('art/mini/atm/base.png')

    text '[who.name]' style_suffix 'name'

    hbox:
        ypos .344

        text _('Balance')
        fixed:
            style_suffix 'balance'
            text '$'
            text '[game.bank:,]':
                xalign 1.

    hbox:
        ypos .455

        text _('Interest')
        text '2%':
            xalign 1.

    side 'r l c':
        style_prefix 'atm_input'
        add game.caret
        text '$'
        text '[game.delta]'

    grid 3 4:
        style_prefix 'atm_keypad'

        at saga.easy.placement('art/mini/atm/key.png')
        spacing 2
        yanchor .745

        for k, c in game.keypad[:-1]:
            use atm_key(game, k, c):
                text '[k]'

        add 'art/mini/atm/key.png'

        for k, c in game.keypad[-1:]:
            use atm_key(game, k, c):
                text '[k]'

        use atm_key(game, '\x08', ('K_BACKSPACE', 'repeat_K_BACKSPACE')):
            add 'art/mini/atm/back.png' align (.5, .5) alt _('Backspace')

    fixed:
        at saga.easy.placement('art/mini/atm/wallet.png')
        fit_first True
        add 'art/mini/atm/wallet.png' alt _('Wallet')
        text '$[game.cash:,]' style_suffix 'button_text'

    use atm_button(game, game.end, 'art/mini/atm/end.png'):
        style_prefix 'atm_button'
        text _('Exit')

    use atm_button(game, game.put, 'art/mini/atm/put.png'):
        style_prefix 'atm_button'
        text _('Deposit')

    use atm_button(game, game.get, 'art/mini/atm/get.png'):
        style_prefix 'atm_button'
        text _('Withdraw')


screen atm_button(game, act, art):
    button:
        action act
        at atm_button, saga.easy.placement(art)
        sensitive game.sensitive(act)

        has fixed
        fit_first True

        add art
        transclude


screen atm_key(game, key, code):
    button:
        action Function(game.push, key)
        at button
        keysym code

        has fixed
        fit_first True

        add 'art/mini/atm/key.png'
        transclude


style atm_balance:
    xalign 1.
    xsize 390
    yfit True

style atm_button_text:
    align (.5, .5)
    color 'fff'
    outlines ((3, '000109', 0, 0),)
    xpos .355

style atm_hbox:
    anchor (.5, .5)
    xpos .5
    xsize 840

style atm_input_side:
    anchor (1., .5)
    pos (.6, .5675)
    xfill True
    xsize 380

style atm_input_text is atm_text:

    size 40
    xalign 1.

style atm_keypad_text is atm_button_text:

    color '5c6aa3'
    size 40
    xpos .5

style atm_name:
    anchor (.5, .5)
    pos (.5, .245)

style atm_text:
    outlines ((2, '0004', 2, 2),)


transform atm_button:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor gui.over
    on insensitive:
        matrixcolor gui.grey
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
