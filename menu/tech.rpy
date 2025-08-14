screen tech():
    style_prefix 'tech_menu' tag menu


    use base_menu(esc='team'):
        vbox:

            add 'art/menu/misc/logo.png':
                alt '[config.name!t]' xalign .5 zoom .75
            label '[config.version]'

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} "
               '[renpy.version_only].\n\n[renpy.license!t]')
            text _('Various fonts and images are also used under license; '
               'including commerical, MIT, and OFL. '
               'Details can be found in game/third-party.txt.')


style tech_menu_label:
    xalign .5
    yoffset -50

style tech_menu_text:
    color '9098a3'

style tech_menu_vbox:
    align (.5, 0.)
    spacing 10
    xsize .8
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
