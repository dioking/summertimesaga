screen nvl(dialogue, items=None):
    style_prefix 'nvl'

    window:
        has vbox

        use nvl_dialogue(dialogue)


screen nvl_dialogue(dialogue):
    for d in dialogue:

        window:
            id d.window_id style_suffix 'entry'

            if d.who is not None:
                text d.who id d.who_id style_suffix 'label'

            text d.what id d.what_id style_suffix 'speak'


style nvl_speak is adv_speak:

    xfill True

style nvl_entry:
    xfill True

style nvl_window is adv_window:

    background gui.box
    margin gui.nvl_margin
    padding gui.nvl_padding
    yalign gui.nvl_yalign
    yfill True
    ysize None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
