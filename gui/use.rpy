screen use(what, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive

    use expression what.screen pass (what, _sensitive)

    if _sensitive:
        use hud_back()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
