screen lewd(items, *, range=(8, 16, 2), tag=None):
    style_prefix 'lewd'

    default opts = tuple(i for i in items if i.caption)

    vbox:
        window:
            has grid len(opts) 1

            for i in opts:
                textbutton i.caption action i.action

        if tag:
            default speed = saga.lewd.speed(tag, range[0])
            default slower = f'{tag} s_{speed - range[2]}'
            default faster = f'{tag} s_{speed + range[2]}'

            window:
                has grid 2 1

                textbutton _('« Slower'):
                    action Return(slower)
                    sensitive speed > range[0]

                textbutton _('Faster »'):
                    action Return(faster)
                    sensitive speed < range[1]


style lewd_button:
    hover_background '#fff1'
    xalign .5
    xminimum 250
    ypadding 15

style lewd_button_text:
    hover_color 'fff'
    idle_color 'eee'
    insensitive_color '999'
    xalign .5

style lewd_vbox:
    spacing 5
    xalign .5
    yanchor 1.
    ypos .99

style lewd_window:
    background gui.choice
    xalign .5
    xpadding 200


screen old_lewd(items, *, range=('slow', 'norm', 'fast'), tag=None, tags=None):
    style_prefix 'lewd'

    default opts = tuple(i for i in items if i.caption)

    vbox:
        window:
            has grid len(opts) 1

            for i in opts:
                textbutton i.caption action i.action

        if tags:
            $ tag = tags[0]

        if tag:
            default attr = _dict(enumerate(range))
            default speed = range.index(next((
                a for t in tags or (tag,)
                  for a in renpy.get_attributes(t) if a in range), range[0]))
            default ctrl = attr.get(speed - 1), attr.get(speed + 1)

            window:
                has grid 2 1

                textbutton _('« Slower'):
                    action Return((f'{tag} {ctrl[0]}', tags)
                                  if tags else f'{tag} {ctrl[0]}')
                    sensitive ctrl[0] is not None

                textbutton _('Faster »'):
                    action Return((f'{tag} {ctrl[1]}', tags)
                                  if tags else f'{tag} {ctrl[1]}')
                    sensitive ctrl[1] is not None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
