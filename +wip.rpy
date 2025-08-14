init python hide:
    from renpy.exports import dynamic, image


    def missing_label_callback(l):
        dynamic(label=l)
        return 'wip.missing_label'


    config.missing_label_callback = missing_label_callback
    config.raise_image_exceptions = False

    image('wip', Window(
        Text('WORK IN PROGRESS', color='1ceda7', style='notify_label_text'),
        anchor=(1., 0.), padding=(20, 15, 15, 15), pos=(1., .26), style='notify_label'))


label wip:
    return


label wip.missing_label(*args):
    scene camera at stage
    "Sorry, this section of the game is still under construction! Please check back in future updates.\n{size=-5}\n{color=4287f5}ref:{/color} [label]{/size}"
    return


label wip.spoiler:
    menu:
        "{color=eda41c}warning:{/color} The following content is unfinished and would normally unlock later in the story."
        "Continue, I know it's not finished but show me anyway!":

            return True
        "No thanks, I'd rather wait.":

            pass

    return


label wip.deb_shower:
    call wip.spoiler

    if not _return:
        return

    menu wip.deb_shower_choice:
        "Blowjob":
            jump wip.deb_shower_blowjob
        "Sex in shower":

            jump wip.deb_shower_glass
        "Sex after shower":

            jump wip.deb_shower_sink
        "Done.":

            return

    return


label wip.deb_shower_blowjob:
    call shot.debbie_bath_soap
    show debbie b_anon c_naked p_debbie_bath_bj_anim s_8 behind steam
    show wip
    with fade
    pause
    jump wip.deb_shower_choice


label wip.deb_shower_glass:
    scene debbie_bath_glass
    show debbie b_anon c_naked p_debbie_bath_glass_anim s_12
    show debbie_bath_glass glass as glass
    show wip
    with fade
    pause
    show debbie p_debbie_bath_glass_cum s_400ms
    with flash
    pause
    jump wip.deb_shower_choice


label wip.deb_shower_sink:
    scene debbie_bath_sink base
    show mimic debbie z_ob at pos.debbie
    show debbie_bath_sink -base -glass as wall
    show debbie b_anon c_naked ob_mirror p_debbie_bath_sink_anim s_12 z_b
    show debbie_bath_sink glass as glass
    show steam
    show wip
    with fade
    pause
    show debbie p_debbie_bath_sink_cum s_400ms
    with flash
    pause
    jump wip.deb_shower_choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
