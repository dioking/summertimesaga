screen pc(what, _sensitive=renpy.get_mode() == 'screen', auto=False):
    layer 'master'
    sensitive _sensitive

    window:
        pos (367, 176) xysize (1187, 743)

        if auto or not what.auto:
            use pc_auth(what)
        else:
            use pc_sys(what)

    use view(what.env, _sensitive)


screen pc_auth(what):
    style_prefix 'pc_auth'

    default app = what.auth

    if what.auto:
        for i in range(1, 1 + len(app.key)):
            timer i * .075 action app.next

    elif app.error:
        timer .275 action SetField(app, 'error', False)

    elif app.focused:
        dismiss action Function(app.focus, False)

    add f'art/mini/pc/user/{what.owner.ref}/login.png'

    vbox:
        add f'art/mini/pc/user/{what.owner.ref}/avatar.png' xalign .5

        null height 20

        text '[what.user]'

        null height 50

        frame:
            modal True

            has button
            key_events True

            if app.error:
                background '#f777'

            elif not what.auto and not app.focused:
                action Function(app.focus, True)
                alt _('Password input')
                at button
                keysym 'K_TAB'

            input:
                copypaste True
                pixel_width 280
                value app

        null height 5

        text 'Password hint: [what.hint]' style_suffix 'hint'


style pc_auth_button:
    background '#fff7'
    padding (10, 10, 10, 8)
    xsize 300

style pc_auth_frame:
    xalign .5

style pc_auth_hint:
    size 15
    xalign .5

style pc_auth_input:
    color '333'
    size 20
    ysize 20

style pc_auth_text:
    bold True
    size 22
    xalign .5

style pc_auth_vbox:
    align (.5, .35)


screen pc_camslut(what, app):
    style_prefix 'pc_camslut'

    default ram = app.ram

    use pc_window(what, app, base='#990000c0'):
        window:
            has side 'l c'

            hbox:
                frame:
                    has vbox

                    text what.user bold True size 18 xalign .5
                    add 'art/mini/pc/camslut/profile.png' xalign .5
                    text _('{emoji=offline} {size=-3}OFFLINE') size 17 xalign .5
                    text _('Rating: ( {emoji=star}{emoji=star}'
                                 '{emoji=star}{emoji=star}'
                                 '{emoji=star_half} )') size 20 xalign .5

                    null height 15

                    text _('Sex: Female') size 18
                    text _('Age: [saga.cast.jenny.age]') size 18
                    text _('Cup Size: [saga.cast.jenny.size]') size 18
                    text _('Hair: Dark Brown') size 18
                    text _('Eyes: Gray') size 18

                add 'pc_camslut_sep'

            frame:
                has vbox style 'vbox'

                hbox:
                    textbutton _('Profile'):
                        at button

                        if ram.mode:
                            action Emit(app=app.ref, op='click')
                        else:
                            background style.pc_camslut_tab.background

                    textbutton _('Videos'):
                        at button

                        if not ram.mode:
                            action Emit(app=app.ref, op='click')
                        else:
                            background style.pc_camslut_tab.background

                frame:
                    style_suffix 'tab'

                    if ram.mode:
                        grid 3 3:
                            for ref in what.videos:
                                imagebutton:
                                    action Emit(app=ref, op='init')
                                    alt __('Video: ') + __(what.apps[ref].args[0])
                                    at button
                                    idle Transform(what.apps[ref].args[1](
                                    f'pc_video_{ref}'), xysize=(170, 126))

                    else:
                        vbox:
                            text _('Hiiii!!... My name is HOTKITTY and I provide '
                               'a premium {emoji=star_cluster} cam service!! '
                               '{emoji=lips}')

                            null

                            text _('I am a beautiful [saga.cast.jenny.age] year '
                               'old goddess with a killer body, amazing set '
                               'of {emoji=heart}{emoji=heart}{emoji=heart} '
                               'and I love to play with my toyzzz!! LOL!')

                            null

                            text _('Here\'s a list of things I like to do in my '
                               'live shows:')
                            text _('- Strip\n- Toys\n- Masturbation\n- Requests '
                               'on donations! {color=fdc016}$$${/color}')

                            null height 5

                            text _('For the generous daddies out there, you can '
                               'DM to send me private gifts!!!! See you '
                               'soooon! xoxo')


image pc_camslut_sep = Solid('611c', xsize=2)


style pc_camslut_button:
    hover_background '#2004'
    idle_background None
    padding (15, 10)
    xalign .5

style pc_camslut_button_text:
    align (.6, .5)
    idle_color 'fffe'
    outlines ((2, '611', 0, 0),)
    size 20

style pc_camslut_frame:
    margin (20, 0)

style pc_camslut_grid:
    spacing 15

style pc_camslut_image_button:
    background '#530508'
    padding (3, 3)

style pc_camslut_tab:
    background '#f774'
    padding (15, 15)
    xysize (176 * 3 + style.pc_camslut_grid.spacing * 2 + 15 * 2,
            134 * 3 + style.pc_camslut_grid.spacing * 2 + 15 * 2)

style pc_camslut_text:
    outlines ((1, '0003', 1, 1),)
    size 20

style pc_camslut_vbox:
    first_spacing 10
    spacing 5

style pc_camslut_window:
    margin (0, 20)


screen pc_dir(what, app):
    use pc_window(what, app):
        use pc_explorer(what, 4, 2, app.args)


screen pc_editor(what, app):
    style_prefix 'pc_editor'

    use pc_window(what, app, name=__(app.name) + '.rtf - Wintour'):
        vbox:

            frame:
                has hbox

                text _('File')
                text _('Edit')
                text _('View')
                add 'art/mini/pc/editor/bold.png'
                add 'art/mini/pc/editor/italic.png'
                add 'art/mini/pc/editor/underline.png'
                add 'art/mini/pc/editor/color.png'
                add 'art/mini/pc/editor/left.png'
                add 'art/mini/pc/editor/center.png'
                add 'art/mini/pc/editor/list.png'

            add 'pc_editor_sep'

            window:
                transclude


image pc_editor_sep = Solid('aac', ysize=2)


style pc_editor_frame:
    padding (12, 8, 12, 4)

style pc_editor_hbox:
    spacing 20

style pc_editor_text:
    align (.5, .575)
    color '669'
    line_spacing (style.pc_editor_frame.top_padding -
                  style.pc_editor_frame.bottom_padding) / 2
    size 16

style pc_editor_vbox:
    xsize 650

style pc_editor_window:
    background '#aac'
    margin (50, 10, 50, 0)
    padding (2, 2, 2, 0)


screen pc_egay(what, app):
    style_prefix 'pc_egay'

    default qry = app.input
    default ram = app.ram

    use pc_web(what, app):
        window:
            has vbox

            showif qry.focused:
                dismiss action Function(qry.focus, False) modal False

            window:
                style_prefix 'pc_egay_find'

                has fixed

                add 'art/mini/pc/egay/logo.png' ypos .05

                frame:
                    modal True

                    has button
                    key_events True

                    if not qry.focused:
                        action Function(qry.focus, True)
                        alt _('Search input')
                        at button
                        keysym 'K_TAB'

                    if qry.text or qry.focused:
                        input:
                            copypaste True
                            pixel_width 300
                            value qry

                    else:
                        text _('Search for items')

            window:
                style 'pc_egay_head_window'

                if ram.path in ('/', '/not-found'):
                    style_prefix 'pc_egay_head'

                    hbox:
                        fixed:
                            add 'art/mini/pc/egay/promo.png'
                            text _('75% OFF') style_suffix 'promo':
                                at transform:
                                    rotate -12.5 rotate_pad False
                        text _('On all\nsummer items!')

                if ram.path == '/orcette':
                    style_prefix 'pc_egay_orc'

                    fixed:
                        add 'art/mini/pc/egay/orcette.png':
                            alt _('The Orcette') xalign .5
                        text '$300' style_suffix 'price'
                        text _('Free shipping!') style_suffix 'subtitle'

                if ram.path == '/confirmation':
                    style_prefix 'pc_egay_head'

                    frame:
                        has hbox

                        add 'art/mini/pc/egay/tick.png' align .5, .5
                        text _('Congratulations!')
                        add 'art/mini/pc/egay/cart.png' align .5, .5

            window:
                style 'pc_egay_body_window'

                if ram.path == '/':
                    style_prefix 'pc_egay_home'

                    hbox:
                        fixed:
                            add 'art/mini/pc/egay/stick.png'
                            text _('Selfie Stick')
                        fixed:
                            add 'art/mini/pc/egay/spinner.png'
                            text _('Meat Spinner')
                        fixed:
                            add 'art/mini/pc/egay/board.png'
                            text _('Hoverboard')

                if ram.path == '/not-found':
                    style_prefix 'pc_egay_body'

                    vbox:
                        text _('Your search - {b}[ram.last!q]{/b} - did not '
                           'match any items.')
                        null
                        text _('Suggestions:')
                        null
                        text _('- Make sure all words are spelled correctly.')
                        text _('- Try different keywords.')
                        text _('- Try more general keywords.')


                if ram.path == '/orcette':
                    style_prefix 'pc_egay_orc'

                    vbox:
                        text _('Zug Zug!') style_suffix 'tagline'
                        text _('Go where no manhood has gone before past the '
                           'alluring pussy of the Orcette. This mesmerizing '
                           'pearlescent green begs to eat you up for a close '
                           'encounter of the preferred kind. The Orcette '
                           'Fleshlight comes with the pearlescent green Orc '
                           'sleeve and a deep green outer case that combine '
                           'to take your orcette fantasy to the outer limits '
                           'of your imagination.')

                        textbutton _('Purchase now!'):
                            action Emit(app=app.ref, op='click')
                            at button

                if ram.path == '/confirmation':
                    style_prefix 'pc_egay_body'

                    vbox:
                        text _('Payment successful!')
                        text _('Your package should arrive on {b}TUESDAY{/b}!')
                        null height 30
                        text _('Transaction ID: '
                           '74656368-7570-6461-7465-687572746d65') size 13


image pc_egay_body = Frame(u('art/mini/pc/egay/body.png'), 4, 4, 4, 0)
image pc_egay_buy = Frame('art/mini/pc/egay/buy.png', 8, 11)
image pc_egay_find = Frame(u('art/mini/pc/egay/find.png'), 5, 5)
image pc_egay_head = Frame(u('art/mini/pc/egay/head.png'), 5, 5, 5, 0)
image pc_egay_input = Frame(u('art/mini/pc/egay/input.png'), 4, 4)
image pc_egay_mag = Image('art/mini/pc/egay/mag.png',
                          xanchor=1., xpos=-10, yalign=.5)


style pc_egay_window:
    margin (10, 10, 10, 0)
    xysize (775, 450)


style pc_egay_body_text:
    color '111'
    size 18

style pc_egay_body_vbox:
    align (0, .5)
    spacing 5

style pc_egay_body_window:
    background 'pc_egay_body'
    padding (20, 10, 20, 0)
    xfill True
    yfill True


style pc_egay_find_button:
    background 'pc_egay_input'
    padding (8, 6)
    xsize 320

style pc_egay_find_fixed:
    fit_first 'height'

style pc_egay_find_frame:
    align (1., .5)
    background 'pc_egay_mag'

style pc_egay_find_input:
    color '333'
    size 18
    yoffset 1

style pc_egay_find_text is pc_egay_find_input:

    color '3337'

style pc_egay_find_window:
    background 'pc_egay_find'
    margin (0, 0, 0, 10)
    padding (11, 8)


style pc_egay_head_fixed:
    fit_first True

style pc_egay_head_frame:
    margin (0, 10)

style pc_egay_head_hbox:
    xfill True

style pc_egay_head_promo:
    align (.5, .5)
    bold True
    color 'fff'
    outlines ((1, '0009', -1, 1),)
    size 60

style pc_egay_head_text:
    align (.5, .5)
    color '536d9f'
    outlines ((1, '0002', 1, 1),)
    size 40
    textalign .5

style pc_egay_head_window:
    background 'pc_egay_head'
    padding (20, 2, 20, 0)


style pc_egay_home_fixed:
    fit_first True

style pc_egay_home_hbox:
    align (.5, 1.)
    spacing 30

style pc_egay_home_text:
    align (.5, .1)
    color '12213f'
    size 23


style pc_egay_orc_button:
    background 'pc_egay_buy'
    padding (35, 12)
    xalign .5

style pc_egay_orc_button_text:
    bold True
    size 20

style pc_egay_orc_fixed:
    fit_first 'height'

style pc_egay_orc_price:
    align (.2, 1.)
    bold True
    color 'fff'
    outlines ((2, '000', 0, 0),)
    size 23

style pc_egay_orc_subtitle is pc_egay_head_text:

    anchor (.5, .5)
    pos (.7, .8)
    size 30

style pc_egay_orc_tagline:
    bold True
    color '536d9f'
    size 20
    xalign .5

style pc_egay_orc_text is pc_egay_body_text


style pc_egay_orc_vbox:
    align (.5, .5)
    spacing 5


screen pc_explorer(what, cols, rows, refs, layout='rows', light=False):
    style_prefix 'pc_explorer'

    window:
        has grid cols rows
        transpose layout != 'rows'

        for app in what.explore(refs):
            if app is None:
                null
                continue

            button:
                action Emit(app=app.ref, op='init')
                at button

                has vbox

                frame:
                    add saga.easy.image(f'art/mini/pc/fs/{app.icon}.png')

                text app.name:
                    if light:
                        style_suffix 'text_light'


style pc_explorer_frame:
    xalign .5
    xysize (126, 117)

style pc_explorer_grid:
    xspacing 10
    yspacing 5

style pc_explorer_text:
    color '111'
    hover_color '333'
    size 18
    textalign .5
    xalign .5
    xmaximum 126

style pc_explorer_text_light is pc_explorer_text:

    color 'eee'
    hover_color 'fff'
    outlines ((absolute(.75), '333', 1, 1),)

style pc_explorer_window:
    padding (10, 5)


screen pc_image(what, app):
    use pc_window(what, app, base=None, name=f'{app.name}.jpg'):
        add f'art/mini/pc/image/{app.args[0]}.png'


screen pc_mail(what, app):
    style_prefix 'pc_mail'

    default ram = app.ram

    use pc_window(what, app):
        window:
            has side 't c'

            hbox:
                label _('COMPOSE') style_suffix 'compose'
                label _('Search in mail') style_suffix 'search'

            side 'l r c':
                vbox:
                    textbutton _('INBOX'):
                        if ram.mode != 'inbox':
                            action Emit(app=app.ref, op='click', what='inbox')

                    label _('SENT')
                    label _('DRAFT')
                    label _('SPAM')
                    label _('TRASH')

                    frame:
                        style_suffix 'contacts'

                        add 'art/mini/pc/mail/people.png' align .5, .5

                add u('art/mini/pc/mail/scroll.png')

                frame:
                    if ram.mode != 'inbox':
                        use pc_mail_email(what.mail[ram.mode]):
                            use expression 'pc_mail_email_' + ram.mode

                    else:
                        window:
                            style_prefix 'pc_mail_inbox'

                            vbox:
                                for mail in what.mail.values():
                                    use pc_mail_inbox_row(what, app, mail)

                            text _('Anything you type can be used to market '
                               'against you. You have the right to not use '
                               'this service.') style_suffix 'legal'


screen pc_mail_email(msg):
    window:
        style_prefix 'pc_mail_email'
        has side 't b c'

        fixed:
            frame:
                has vbox

                hbox:
                    label _('from')
                    text msg.who
                hbox:
                    label _('subject')
                    text msg.what bold True

            add 'pc_mail_sep' yalign 1.

        fixed:
            label _('Inspected by Gaspersigh Anti-Virus. No unsanctioned '
                    'threats found.') style_suffix 'legal'

            add 'pc_mail_sep'

        fixed:
            transclude


screen pc_mail_email_419():
    style_prefix 'pc_mail_email_plain'

    frame:
        text _('Dear Beloved Friend,\n\n'
               'I know this message will come to you as a surprise but I am '
               'Prince Kaosu Uzu of Nigeria. I am presently being held '
               'captive in a cage and in need of assistance. I have many '
               'money, hidden in my palace. If you send a ransom to this '
               'adress below, my captores will release me and I will reward '
               'you with many gold, and women.\n\n'
               'Any money will do. Please send quickly!\n\n'
               '123 Starvation Lane, Shack 5\n\n'
               'Best regards,\n\n'
               'Kao the best prince')


screen pc_mail_email_beg():
    style_prefix 'pc_mail_email_plain'

    frame:
        text _('wil pay $15 4 u 2 rite \'i <3 SS\' on thm')


screen pc_mail_email_cam():
    style_prefix 'pc_mail_email_cam'

    window:
        has side 't c'

        fixed:
            add 'art/mini/pc/mail/cam/logo.png'
            label _('"Woohoo! You just got paid!"')

        frame:
            has vbox

            text _('Congratulations! This month you have earned:')

            label '$ {color=fff}445.00{/color}' style_suffix 'cash'

            text _('Your earnings will be sent from your CAMslut account to '
                   'your bank!\n\n'
                   'Thank you for using our premium service. If you have any '
                   'issues with money transfers please contact us at '
                   'support@camslut.dc. Stay sexy!\n\n- CAMslut Team')


screen pc_mail_email_p69():
    style_prefix 'pc_mail_email_plain'

    frame:
        has vbox

        text _('"Oye mami, I wanted to show you mi Pinga Latina {emoji=wink}"')
        add 'art/mini/pc/mail/p69/pablo.png'


screen pc_mail_email_ptv():
    style_prefix 'pc_mail_email_ptv'

    add 'art/mini/pc/mail/ptv/base.png'

    vbox:
        text _('*** Do not forward or share your account details. ***') size 14

        grid 2 2:
            label _('Subscription:')
            text 'L6bv12R' style_suffix 'credential'
            label _('Password:')
            text '12345' style_suffix 'credential'

        text _('Thank you for subscribing to our premium satellite service! '
               'We offer the best adult content on demand.\n\n- The Pink Team')


screen pc_mail_email_toy():
    style_prefix 'pc_mail_email_toy'

    add 'art/mini/pc/mail/toy/base.png'

    vbox:
        label _('Item: Deep Blue')

        null height 20

        text _('The Deep Blue is part of our new glow in the dark butt plug '
               'collection!')

        null height 100

        text _('Thank you for your online purchase! All our orders can take '
               'up to 4 business days to reach their destination. If you have '
               'not received your package, please contact us at '
               'support@lewdtoys.dc.\n\n- LewdToys')

    text _('* All products have been tested on animals.') style_suffix 'legal'


screen pc_mail_inbox_row(what, app, msg):
    button:
        action Emit(app=app.ref, op='click', what=msg.ref)

        if msg.ref in what.read:
            style_suffix 'read'

        fixed:

            text msg.who.partition('<')[0].strip() xpos 65
            text msg.what xpos 260

            if 'file' in msg.opts:
                add saga.easy.image('art/mini/pc/mail/clip.png') align 1., .5


image pc_mail_dull = Frame(u('art/mini/pc/mail/dull.png'), 7, 7)
image pc_mail_idle = Frame(u('art/mini/pc/mail/idle.png'), 7, 7)
image pc_mail_over = Frame(u('art/mini/pc/mail/over.png'), 7, 7)
image pc_mail_sep = Solid('576d8e', ysize=3)

image pc_mail_email_cam_cash = Frame('art/mini/pc/mail/cam/cash.png', 6, 6)

image pc_mail_inbox_read = Image('art/mini/pc/mail/read.png',
                                 xpos=15, yalign=.55)
image pc_mail_inbox_unread = Image('art/mini/pc/mail/unread.png',
                                   xpos=15, yalign=.55)


style pc_mail_button:
    background 'pc_mail_idle'
    hover_background 'pc_mail_over'
    padding (20, 9)
    xfill True

style pc_mail_button_text:
    color '235'
    line_leading 2
    size 18
    xalign .5

style pc_mail_compose is pc_mail_button:

    background 'pc_mail_dull'
    xsize 150

style pc_mail_compose_text is pc_mail_button_text


style pc_mail_contacts is pc_mail_button:

    background 'pc_mail_dull'

style pc_mail_frame:
    xysize (842, 477)

style pc_mail_hbox:
    spacing 10

style pc_mail_label is pc_mail_button:

    background 'pc_mail_idle'

style pc_mail_label_text is pc_mail_button_text


style pc_mail_search is pc_mail_label:

    xsize 550

style pc_mail_search_text is pc_mail_button_text:

    color '999'
    xalign 0

style pc_mail_side:
    spacing 10

style pc_mail_vbox:
    spacing 5
    xmaximum 100

style pc_mail_window:
    padding (10, 10)


style pc_mail_email_fixed:
    fit_first 'height'

style pc_mail_email_frame:
    padding (15, 15)

style pc_mail_email_hbox:
    spacing 8

style pc_mail_email_label:
    xsize 80

style pc_mail_email_label_text:
    color '999'
    size 17
    xalign 1.

style pc_mail_email_legal:
    margin (10, 10)

style pc_mail_email_legal_text is pc_mail_email_label_text:

    size 13

style pc_mail_email_text:
    color '235'
    size 17

style pc_mail_email_vbox:
    spacing 5

style pc_mail_email_window:
    background 'pc_mail_idle'
    padding (3, 3)


style pc_mail_email_cam_cash:
    background 'pc_mail_email_cam_cash'
    padding (50, 12)
    xalign .5

style pc_mail_email_cam_cash_text:
    align (.5, .5)
    color 'fdc016'
    kerning 1.25
    outlines ((2, '9f2307', 0, 0),)
    size 22

style pc_mail_email_cam_fixed:
    fit_first 'height'

style pc_mail_email_cam_frame:
    background style.pc_camslut_button.background
    margin (0, 15, 0, 0)
    padding (10, 20, 10, 0)
    xfill True
    yfill True

style pc_mail_email_cam_label:
    align (.5, .5)

style pc_mail_email_cam_label_text:
    bold True
    outlines ((1, '0001', 1, 1),)
    size 22

style pc_mail_email_cam_text:
    outlines ((1, '0001', 1, 1),)
    size 18
    xalign .5

style pc_mail_email_cam_vbox:
    spacing 15
    xfill True

style pc_mail_email_cam_window:
    background '#990000c0'
    padding (55, 10, 55, 0)
    xalign .5
    xfill True
    yfill True


style pc_mail_email_plain_frame:
    padding (10, 10)
    yfill True

style pc_mail_email_plain_text:
    color '235'
    size 16

style pc_mail_email_plain_vbox:
    spacing 10


style pc_mail_email_ptv_credential:
    bold True
    size 19

style pc_mail_email_ptv_grid:
    xalign .5
    xspacing 10
    yspacing 5

style pc_mail_email_ptv_label:
    xalign 1.

style pc_mail_email_ptv_label_text:
    line_spacing 3
    size 19

style pc_mail_email_ptv_text:
    color 'c45afb'
    size 16
    xalign .5

style pc_mail_email_ptv_vbox:
    spacing 15
    xalign .5
    xmaximum .65
    ypos .375


style pc_mail_email_toy_label:
    xalign .5

style pc_mail_email_toy_label_text:
    bold True
    size 26

style pc_mail_email_toy_legal:
    align (.5, .9925)
    color 'fff6'
    size 12

style pc_mail_email_toy_text:
    size 17
    xalign .5

style pc_mail_email_toy_vbox:
    spacing 10
    xalign .5
    xmaximum .8
    ypos .075


style pc_mail_inbox_button:
    background 'pc_mail_idle'
    foreground 'pc_mail_inbox_unread'
    hover_background 'pc_mail_over'
    padding (15, 13)

style pc_mail_inbox_fixed:
    fit_first 'height'

style pc_mail_inbox_legal:
    align (.5, 1.)
    color '235'
    size 13

style pc_mail_inbox_read is pc_mail_inbox_button:

    foreground 'pc_mail_inbox_read'
    idle_background 'pc_mail_dull'

style pc_mail_inbox_text:
    color '235'
    line_leading 2
    size 18

style pc_mail_inbox_vbox:
    spacing 5


screen pc_saga(what, app):
    style_prefix 'pc_saga'

    default ram = app.ram

    use pc_window(what, app, base=None):
        button:
            action Emit(app=app.ref, op='click')

            if ram.mode == 1:
                add Solid('0b0d17')
                add 'art/mini/pc/saga/splash.png':
                    at transform:
                        pause (ram.st - renpy.display.interface.frame_time)
                        alpha 0
                        linear 1.5 alpha 1
            elif ram.mode == 2:
                add 'pc_saga_menu'

            elif ram.mode == 3:
                viewport as vp:
                    xinitial ram.mark

                    if app.focused:
                        edgescroll (150, 500)

                    add u('art/mini/pc/saga/bedroom.png')

                $ vp.xadjustment.changed = app.mark

            elif ram.mode == 4:
                add 'pc_saga_ex'


image pc_saga_menu = Fixed(u('art/mini/pc/saga/menu.png'),
                           Movie(play='art/mini/pc/saga/menu.mkv'))


style pc_saga_button:
    xysize (512, 336)


screen pc_sys(what):
    style_prefix 'pc_sys'

    add f'art/mini/pc/user/{what.owner.ref}/desktop.png'

    use pc_explorer(what, 8, 4, what.root, layout='cols', light=True)

    draggroup:
        for app index app.ref in what.windows:
            use expression app.screen pass (what, app)

    frame:
        modal True

        has side 'l r'

        imagebutton:
            action Emit(app='sys', op='quit')
            alt _('Logout')
            at button
            idle 'art/mini/pc/sys/quit.png'

        add 'art/mini/pc/sys/tray.png' yalign .5


style pc_sys_frame:
    background '#fff7'
    padding (20, 3)
    xfill True
    yalign 1.

style pc_sys_hbox:
    align (1., .5)
    spacing 10

style pc_sys_side:
    xfill True


screen pc_video(what, app):
    style_prefix 'pc_video'

    use pc_window(what, app, base=None, name=f'{app.name} - FunMediaPlaya'):

        add f'pc_video_{app.ref}' at app.args[1]
        label app.args[0]

        imagebutton:
            action Emit(app=app.ref, op='click')
            align (.5, .5)
            at button
            idle u('art/mini/pc/video/play.png')

        if app.focused:
            add 'aux' at app.args[1]


image pc_video_vid1 = Fixed(
    'debbie_bed2_video base noon',
    'jenny c_naked p_debbie_bed2_cam_electro_anim_01 #_thumb',
    'debbie_bed2_video noon ui')

image pc_video_vid2 = Fixed(
    'debbie_bed2_video base noon',
    'jenny c_naked p_debbie_bed2_cam_vibrate_anim_01 #_thumb',
    'debbie_bed2_video noon ui')

image pc_video_vid3 = Fixed(
    'debbie_bed2_video base noon',
    'jenny c_naked p_debbie_bed2_cam_monster_anim_01 #_thumb',
    'debbie_bed2_video noon ui')


style pc_video_label:
    background '#0007'
    margin (8, 8)
    padding (8, 8)

style pc_video_label_text:
    bold True
    color 'fff'
    size 18


screen pc_web(what, app):
    style_prefix 'pc_web'

    default ram = app.ram

    use pc_window(what, app, name=__(app.name) + ' - Internet Sexplorer'):
        side 't c':

            vbox:
                frame:
                    text ram.host + ram.path

                add 'pc_web_sep'

            window:
                transclude


image pc_web_sep = Solid('333', ysize=1)
image pc_web_url = Frame('art/mini/pc/web/url.png', 65, 10, 90, 10)


style pc_web_frame:
    background 'pc_web_url'
    margin (10, 7, 10, 7)
    padding (70, 7, 60, 7)
    xfill True

style pc_web_text:
    color '121212'
    size 17


screen pc_window(what, app, name=None, base='#fffc'):
    style_prefix 'pc_window'
    modal True

    drag as self:
        drag_name app.ref
        drag_raise False
        dragged app.move
        droppable False
        pos app.pos

        if not app.focused:
            activated app.focus
            alt ''
            clicked app.init

        side 't tl tr l r bl b br c':

            side 't c b':
                add 'pc_window_h'

                frame:
                    if app.focused:
                        background '#669c'

                    hbox:

                        text name or app.name

                        window:
                            modal True
                            xalign 1.

                            has hbox style_suffix 'ctrl'

                            add 'art/mini/pc/window/min.png'
                            add 'art/mini/pc/window/max.png'

                            imagebutton:
                                action app.quit
                                alt _('Close')
                                at button
                                idle 'art/mini/pc/window/quit.png'

                add 'pc_window_h'

            add 'pc_window_v'
            add 'pc_window_v'
            add 'pc_window_v'
            add 'pc_window_v'
            add 'pc_window_c'
            add 'pc_window_h'
            add 'pc_window_c'

            window:
                background base
                modal True

                has fixed

                transclude

                if not app.focused:
                    button action app.init

    $ self.z = app.zorder


image pc_window_h = Solid('40556a', ysize=1)
image pc_window_v = Solid('40556a', xsize=1)
image pc_window_c = Solid('40556a', xysize=(1, 1))


style pc_window_ctrl:
    spacing 2

style pc_window_fixed:
    fit_first True

style pc_window_frame:
    background '#999c'
    padding (10, 4, 3, 4)

style pc_window_hbox:
    xfill True

style pc_window_text:
    outlines ((1, '5559', 1, 1),)
    size 25
    yalign 1.


screen pc_wish(what, app):
    style_prefix 'pc_wish'

    use pc_editor(what, app):
        frame:
            has vbox

            text _('List of Cam {err=18}toyz{/err} to get:') xalign .5
            text _('- The Dildo "Fuck-Hammer"')
            text _('- Glow in the dark Butt plug')
            text _('- Dual sybian (multi-{err=18}controler{/err})')
            text _('- UltraVibrator 2000')
            text _('- The Doom Dong')
            text _('- Sex Doll "Dirty Harold"')
            text _('- DarthMoan')
            text _('- BAD MONSTER')
            text _('- Electro Clit')


style pc_wish_frame:
    background '#fff'
    padding (30, 20, 30, 10)

style pc_wish_text:
    color '000'
    size 18

style pc_wish_vbox:
    first_spacing 20
    spacing 10
    xfill True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
