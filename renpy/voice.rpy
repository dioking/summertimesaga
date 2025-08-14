screen _self_voicing():
    style_prefix 'notify'
    zorder 1500

    if _preferences.self_voicing == 'clipboard':
        $ message = _("Clipboard voicing enabled.{vspace=3}Press 'shift+c' to disable.")
    elif _preferences.self_voicing == 'debug':
        $ message = _("Self-voicing would say \"[renpy.display.tts.last!q]\".{vspace=3}Press 'v' twice to disable.")
    else:
        $ message = _("Self-voicing enabled.{vspace=3}Press 'v' to disable.")

    label message alt '' ypos .18
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
