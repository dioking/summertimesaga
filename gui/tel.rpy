screen tel(what, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive
    style_prefix 'tel_app'

    add saga.easy.ref(saga.camera.track.where.ref) at stage

    fixed:
        use expression 'tel_' + what.app.ref pass (what, what.app)

    add saga.easy.image('art/mini/tel/base.png')

    imagebutton:
        action Emit(app='sys', op='wifi')
        alt _('Wifi Settings')
        at button, saga.easy.placement('art/mini/tel/wifi.png')
        idle 'art/mini/tel/wifi.png'

    if what.app.ref != 'home':
        imagebutton:
            action Emit(app=what.app.esc or 'home', op='init')
            alt what.apps['home'].name
            at button, saga.easy.placement('art/mini/tel/back.png')
            idle 'art/mini/tel/back.png'

        if what.app.name:
            text what.app.name


style tel_app_fixed:
    align (.5, 1.)
    fit_first True

style tel_app_side:
    xalign .5
    xsize 1480

style tel_app_text:
    anchor (.5, .5)
    color '9ba3c7'
    font 'acme'
    pos (.5, .105)
    size 35

style tel_app_vpgrid:
    margin (35, 75, 30, 50)
    spacing 50
    xfill True

style tel_app_vscrollbar:
    thumb '#fff7'
    unscrollable 'hide'
    xsize (style.tel_app_vpgrid.left_margin -
           style.tel_app_vpgrid.right_margin)
    ypos style.tel_app_vpgrid.top_margin
    ysize position(-style.tel_app_vpgrid.top_margin
                   -style.tel_app_vpgrid.bottom_margin, relative=1.)


screen tel_cast(what, app):
    style_prefix 'tel_cast'

    default list = what.cast

    add 'art/mini/tel/misc/dark.png'

    vpgrid as vp:
        cols 2
        draggable True
        mousewheel bool(list)
        scrollbars ('vertical' if list else None)
        yinitial app.offset



        for who in list:
            button:
                action Emit(app='info', op='read', who=who)
                at button

                has fixed

                add f'art/mini/tel/cast/{who.type}.png'
                add f'art/menu/cast/{who.ref}/open.png' pos (20, 15) zoom .527

                text '[who.name] [who.clan]' style_suffix f'name_{who.type}'
                text '[who.type!c]' style_suffix f'type_{who.type}'













    $ vp.yadjustment.changed = app.mark


style tel_cast_button:
    xalign .5

style tel_cast_fixed:
    fit_first True

style tel_cast_side is tel_app_side


style tel_cast_text:
    anchor (.0, .5)
    font 'acme'
    pos (.275, .3)
    size 50

style tel_cast_type:
    alt ''
    size 40
    ypos .725

style tel_cast_vpgrid is tel_app_vpgrid:

    spacing 20

style tel_cast_vscrollbar is tel_app_vscrollbar



init python hide:
    src = (('home', '3b237a'),
           ('monster', '82236d'),
           ('student', '2f4591'),
           ('teacher', '724f1e'),
           ('town', '1f6a2c'),
           ('villain', '292929'))

    style.tel_cast_type = Style(style.tel_cast_text)

    for t, c in src:
        s = Style(style.tel_cast_text)
        s.outlines = ((3, c, 0, 0),)
        setattr(style, f'tel_cast_name_{t}', s)
        
        s = Style(style.tel_cast_type)
        s.outlines = ((3, c, 0, 0),)
        setattr(style, f'tel_cast_type_{t}', s)


screen tel_chat(what, app):
    style_prefix 'tel_chat'

    add 'art/mini/tel/misc/light.png'

    viewport as vp:
        draggable True
        mousewheel True
        scrollbars 'vertical'
        yinitial app.offset

        has window
        vbox:

            for t, mesg in what.chat(app.hdd.who):
                if t is not None:
                    use tel_util_ago(t)

                frame:
                    style_prefix ('tel_chat_send' if what.owner is mesg.who else
                              'tel_chat_recv')

                    text '[mesg.what!i]'

    $ vp.yadjustment.changed = app.mark


style tel_chat_side is tel_app_side


style tel_chat_recv_frame:
    background Frame('art/mini/tel/chat/recv.png', 40, 40, 40, 45)
    padding (40, 25, 40, 35)
    xsize .9

style tel_chat_send_frame is tel_chat_recv_frame:

    background Frame('art/mini/tel/chat/send.png', 40, 40, 40, 45)
    xalign 1.

style tel_chat_send_vbox:
    spacing 5

style tel_chat_ago:
    color 'fffb'
    size 30
    xalign .5

style tel_chat_recv_text:
    color '000'
    size 35

style tel_chat_send_text is tel_chat_recv_text:

    xalign 1.

style tel_chat_vbox is tel_app_vpgrid:

    spacing 20

style tel_chat_viewport is tel_app_vpgrid


style tel_chat_vscrollbar is tel_app_vscrollbar


style tel_chat_window is tel_app_vpgrid



screen tel_home(what, app):
    style_prefix 'tel_home'

    add 'art/mini/tel/misc/dark.png'

    grid 4 2:
        for ref in app.args:
            if ref in what.apps:
                imagebutton:
                    at button, saga.easy.placement(f'art/mini/tel/home/{ref}.png')
                    idle f'art/mini/tel/home/{ref}.png'
                    action Emit(app=ref, op='init')
                    alt what.apps[ref].name
            else:
                add saga.easy.image(f'art/mini/tel/home/{ref}.png'):
                    matrixcolor ColorizeMatrix('012', '9ab') * gui.grey


style tel_home_grid:
    xalign .5
    xspacing 100
    ypos 125
    yspacing 80


screen tel_info(what, app):
    style_prefix 'tel_info'

    default who = app.hdd.who

    default name = EmitInputValue(who.ref, who.name)
    default stat = who.info + (None,) * 6
    default tab = 'book'

    add 'art/mini/tel/misc/dark.png'

    showif name.text.strip() and name.focused:
        dismiss action Function(name.focus, False)

    hbox:
        style_suffix 'split'

        side 'tl t l c':
            fixed:

                at transform:
                    fit 'contain'
                add 'art/mini/tel/info/profile.png'
                add f'art/menu/cast/{who.ref}/open.png' pos (28, 23)

            vbox:
                button:
                    style_suffix 'label'
                    key_events True

                    if not name.focused:
                        action Function(name.focus, True)
                        at button

                    fixed fit_first 'height':

                        input:
                            allow printable
                            copypaste True
                            exclude '[]{]'
                            length 12
                            style_suffix 'label_text'
                            value name

                        if not name.focused:
                            add 'art/mini/tel/info/edit.png' xalign 1. yalign .5

                label '[who.clan]'
                label 'Age: [who.age]'

                if who.kind == 'f':
                    label 'Bust: [who.size]'
                else:
                    label 'Size: ???'

            vbox:
                style_suffix 'column'

                for card in stat[:6:2]:
                    if card:
                        use tel_util_card(card, who)
                    else:
                        add 'art/mini/tel/info/icon/tab.png' alpha .5

            vbox:
                style_suffix 'column'

                for card in stat[1:6:2]:
                    if card:
                        use tel_util_card(card, who)
                    else:
                        add 'art/mini/tel/info/icon/tab.png' alpha .5

        window:
            background 'tel_info_box'
            xfill True
            yfill True
            padding (45, 45)

            if tab != 'book':
                add f'art/mini/tel/info/{tab}/{who.ref}.png':
                    align (.5, 1.)
            else:
                vbox:
                    label _('Background') style_suffix 'header'
                    text who.bio

            imagebutton:
                action CycleLocalVariable('tab', ('book', 'outfit') + (
                    () if who < 'nude' else ('naked',)))
                alt _('Next')
                at button

                if tab == 'book':
                    idle f'art/mini/tel/info/{tab}.png'
                else:
                    idle f'art/mini/tel/info/{tab}_{who.kind}.png'


image tel_info_box = Model().grid_mesh(2, 2).shader('gui.box'). \
    uniform('u_color', color('4b549680').premultiplied). \
    uniform('u_feather', 50)


style tel_info_column:
    spacing 20

style tel_info_fixed:
    align (.5, .5)
    fit_first True

style tel_info_header:
    bottom_margin 25

style tel_info_header_text:
    font 'acme'
    size 40

style tel_info_image_button:
    align (1., 1.)

style tel_info_label:
    background 'tel_info_box'
    padding (30, 20)
    xfill True

style tel_info_label_text:
    size gui.text_size * 1.15
    yalign .5

style tel_info_side:
    spacing 20
    yfill True

style tel_info_split is tel_app_side:

    spacing 20
    xysize (.967, .95)
    yalign .625
    yfill True

style tel_info_stat:
    anchor (.5, .5)
    font 'acme'
    outlines ((3, '426890', 0, 0),)
    pos (.664, .255)
    size gui.text_size * 1.25

style tel_info_text:
    justify True
    line_spacing 3
    size 27

style tel_info_value is tel_info_stat:

    size gui.text_size
    spacing 5
    ypos .725

style tel_info_vbox:
    spacing 5


screen tel_mesg(what, app):
    style_prefix 'tel_mesg'

    default list = what.chats()

    add 'art/mini/tel/misc/light.png'

    vpgrid as vp:
        cols 1
        draggable True
        mousewheel bool(list)
        scrollbars ('vertical' if list else None)
        yinitial app.offset

        if not list:
            yfill True
            label _('No messages.')

        for t, chat, seen in list:
            button:
                action Emit(app='chat', op='read', who=chat.who)
                at button

                has fixed
                add 'art/mini/tel/mesg/chat.png'

                add f'menu_cast_{chat.who.ref}':
                    xoffset -style.tel_mesg_button.left_padding
                    zoom .9

                frame:
                    has vbox

                    text '[chat.who]'

                    use tel_util_ago(t)

                if not seen:
                    add 'art/mini/tel/misc/ping.png':
                        alt _('Unread')
                        anchor (.5, .5)
                        pos (1., .35)

    $ vp.yadjustment.changed = app.mark


style tel_mesg_ago:
    color '7777'
    size 30

style tel_mesg_button:
    left_padding 115
    xalign .5

style tel_mesg_fixed:
    fit_first True

style tel_mesg_label:
    align (.5, .5)

style tel_mesg_ping:
    align (.925, .5)
    bold True
    color 'f33'
    size 40

style tel_mesg_side is tel_app_side


style tel_mesg_text:
    color '484848'
    font 'acme'
    size 45

style tel_mesg_frame:
    padding (75, 15, 60, 25)
    yalign .5

style tel_mesg_vbox:
    spacing 5

style tel_mesg_vpgrid is tel_app_vpgrid


style tel_mesg_vscrollbar is tel_app_vscrollbar



screen tel_note(what, app):
    style_prefix 'tel_note'

    default list = what.notes()
    default todo = set()

    add 'art/mini/tel/misc/dark.png'

    viewport as vp:
        draggable True
        mousewheel bool(list)
        yinitial app.offset
        scrollbars ('vertical' if list else None)

        has window
        vbox:

            for i, f in enumerate(list):
                button:
                    action ToggleSetMembership(todo, f), With(dissolvefast)
                    at button

                    if i % 2:
                        background 'tel_info_box'

                    hbox:

                        add f'menu_cast_{f.icon}'

                        frame:
                            has hbox style_suffix 'hint'

                            text '•'

                            if f in todo:
                                text f.step.todo or 'Wait.' color '093'
                            else:
                                text f.step.hint or 'No hint.'

    $ vp.yadjustment.changed = app.mark


style tel_note_button:
    padding (25, 25)
    xalign .5
    xfill True

style tel_note_frame:
    margin (0, 15)

style tel_note_hbox:
    spacing 50

style tel_note_hint:
    spacing 10

style tel_note_side is tel_app_side


style tel_note_text:
    color 'eee'
    size 30

style tel_note_vbox is tel_app_vpgrid:

    spacing 0

style tel_note_viewport is tel_app_vpgrid


style tel_note_vscrollbar is tel_app_vscrollbar


style tel_note_window is tel_app_vpgrid:

    left_margin 25
    right_margin 20


screen tel_stat(what, app):
    add saga.easy.image('art/mini/tel/stat/base.png')

    for stat, value in what.stats('chr', 'dex', 'int', 'str'):
        hbox:
            at saga.easy.placement(f'art/mini/tel/stat/{stat}.png')
            style_prefix 'tel_stat'

            for i in range(value):
                add f'art/mini/tel/stat/{stat}.png' subpixel True


style tel_stat_hbox:
    spacing 12.5


screen tel_util_ago(t):
    if t == 0:
        text _('Just now') style_suffix 'ago'
    elif t < 1:
        text _('Earlier today') style_suffix 'ago'
    elif t == 1:
        text _('Yesterday') style_suffix 'ago'
    else:
        text _('[t] days ago') style_suffix 'ago'


screen tel_util_card(type, who):
    fixed:
        add 'art/mini/tel/info/icon/tab.png'
        add saga.easy.image(f'art/mini/tel/info/icon/{type}.png')

        if type == 'baby':
            text _('Babies') style_suffix 'stat'
            text str(getattr(who, 'babies', 0)) style_suffix 'value'

        elif type == 'dates':
            text _('Dates') style_suffix 'stat'
            hbox:
                style_suffix 'value'

                for i in range(3):
                    add 'tel_info_pip' xsize int((175 - 5 * 2) // 3)

        elif type == 'flow':
            text _('Story') style_suffix 'stat'
            text 'TBD' style_suffix 'value'

        elif type == 'house':
            text _('Harem') style_suffix 'stat'
            add 'tel_info_bool' anchor (.5, .5) pos (.664, .725)

        elif type == 'path':
            text _('Route') style_suffix 'stat'
            text 'TBD' style_suffix 'value'

        elif type == 'prom':
            text _('Prom Date') style_suffix 'stat'
            add 'tel_info_bool' anchor (.5, .5) pos (.664, .725)

        else:
            pass


image tel_info_bool = Frame('art/mini/tel/info/pip.png', 10, 10, xysize=(90, 28))
image tel_info_pip = Frame('art/mini/tel/info/pip.png', 10, 10, xysize=(55, 28))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
