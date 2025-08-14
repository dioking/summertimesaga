screen cast():
    style_prefix 'cast_menu' tag menu


    use base_menu():
        side 't c':

            label _('Cookie Jar')

            vpgrid:
                allow_underfull True
                cols 9

                draggable True
                mousewheel True

                for ref, open in saga.menu.cast():
                    if open:
                        imagebutton:
                            action ShowMenu('lewd_menu', ref)
                            alt persistent.cast.get(ref) or saga.cast[ref].name
                            at button
                            idle f'menu_cast_{ref}'
                    else:
                        add f'menu_lock_{ref}'


style cast_menu_label:
    bottom_margin 32
    xalign .5
    ysize 100

style cast_menu_label_text:
    font 'acme'
    outlines ((5, '0007', 0, 0),)
    size gui.text_size * 1.25
    yalign .5

style cast_menu_vpgrid:
    align (.5, .5)
    spacing 20
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
