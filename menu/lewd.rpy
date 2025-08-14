screen lewd_menu(ref):
    style_prefix 'lewd_menu' tag menu


    use base_menu(esc='cast'):
        side 't b c':

            label persistent.cast.get(ref) or saga.cast[ref].name
            null height 30

            vpgrid:
                allow_underfull True
                cols 6
                draggable True
                mousewheel True
                pagekeys True
                scrollbars 'vertical'

                for name, key, opts in saga.menu.lewd(ref):
                    imagebutton:
                        action Replay(name, scope={'opts': opts}, locked=not opts)
                        alt __('Replay ') + key.replace('_', ' ')
                        at button
                        idle f'art/menu/cast/{ref}/{key}.png'
                        insensitive 'art/menu/cast/lock.png'


style lewd_menu_label is cast_menu_label


style lewd_menu_label_text is cast_menu_label_text


style lewd_menu_vpgrid is cast_menu_vpgrid:

    margin (40, 0, 20, 0)

style lewd_menu_vscrollbar is pref_menu_vscrollbar
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
