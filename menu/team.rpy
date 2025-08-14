screen team():
    style_prefix 'team_menu' tag menu


    use base_menu():
        side 't c b':

            label _('Credits') style_suffix 'title'

            grid 2 1:
                vbox:
                    grid 2 1:
                        label _('ART')
                        text 'DarkCookie'

                    null height 10

                    grid 2 1:
                        label _('CODE')
                        text 'strayerror'

                    null height 10

                    grid 2 1:
                        label _('STORY')
                        text 'CaptainSploosh'

                    null height 50

                    grid 2 1:
                        label _('POSING')
                        vbox:
                            text 'MindWright'
                            text 'Volé'
                            text 'ToxicCrobat'

                    null height 50

                    grid 2 1:
                        label _('HR')
                        text 'CreamyCookie'

                    grid 2 1:
                        label _('IT')
                        text 'sam9'

                vbox:
                    grid 2 1:
                        label _('PLAYTESTERS')
                        vbox:
                            text 'paleofinn'
                            text 'Arboris'
                            text 'BlightedTalon'
                            text 'habsdad.'

                    null height 50

                    grid 2 1:
                        label _('CONTRIBUTORS')
                        vbox:
                            text 'AoiichiNiiSan'
                            text 'dildorog'
                            text 'Joaka'

            grid 2 1:
                xsize .25
                textbutton _('About') action ShowMenu('tech')
                textbutton _('Patrons') action ShowMenu('mvps')


style team_menu_button is core_menu_button


style team_menu_button_text is core_menu_button_text


style team_menu_grid:
    align (.5, .25)
    xspacing 75

style team_menu_label:
    xalign 1.

style team_menu_label_text:
    font 'acme'
    size gui.text_size * .9

style team_menu_side:
    yfill True

style team_menu_text:
    color gui.accent_color

style team_menu_title is cast_menu_label


style team_menu_title_text is cast_menu_label_text


style team_menu_vbox:
    spacing 10
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
