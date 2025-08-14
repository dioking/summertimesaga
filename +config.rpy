init python early hide:
    from saga import __version__


    config.name = _('Summertime Saga')
    config.version = __version__

    config.save_directory = 'summertimesaga'


init python hide:
    from renpy.uguu import (
        GL_DST_ALPHA, GL_FUNC_ADD, GL_FUNC_REVERSE_SUBTRACT, GL_ONE,
        GL_ONE_MINUS_SRC_ALPHA)

    from saga.art.link import get as link_get
    from saga.display.anim import clear as anim_clear, sweep as anim_sweep
    from saga.game import init, upgrade
    from saga.renpy.notify import clear as notify_clear, push as notify_push
    from saga.renpy.script import show
    from saga.renpy.transition import attribute_callback, with_callback
    from saga.wind import clear as wind_clear


    config.autosave_slots = 6
    config.quicksave_slots = 6

    config.default_fullscreen = True
    config.window_icon = 'art/misc/logo.png'

    config.font_replacement_map['DejaVuSans.ttf', False, True] = (
        'font/dejavusans-oblique.ttf', False, False)

    config.gl_blend_func |= {
        'clip': (GL_FUNC_ADD, GL_DST_ALPHA, GL_ONE_MINUS_SRC_ALPHA) * 2,
        'dark': (GL_FUNC_REVERSE_SUBTRACT, GL_ONE, GL_ONE,
                 GL_FUNC_ADD, GL_ONE, GL_ONE_MINUS_SRC_ALPHA)}

    config.has_voice = False

    config.images_directory = None
    config.optimize_texture_bounds = False

    config.label_overrides['_console_return'] = 'loop.flush'

    config.bottom_layers.remove('bottom')
    config.top_layers.remove('top')
    config.context_clear_layers.remove('bottom')
    config.context_clear_layers.remove('top')

    config.detached_layers.append('aux')

    config.font_name_map['abct'] = 'font/abct-classic.ttf'
    config.font_name_map['acme'] = 'font/acme-regular.ttf'

    config.main_menu_music = 'sound/music/main.ogg'

    config.menu_clear_layers.extend(('aux', 'master'))

    config.missing_image_callback = link_get

    config.mixed_position = False

    config.notify = notify_push

    config.old_substitutions = False

    config.overlay_screens.append('quick')

    config.profile_init = 1.

    config.repeat_transform_events.append('usr1')

    config.replay_scope.clear()

    config.rollback_length = 512
    config.call_screen_roll_forward = True

    config.say_attribute_transition_callback = attribute_callback
    config.speaking_attribute = 'm_talk'

    config.show = show

    config.skip_sounds = True

    config.start_callbacks.extend((anim_clear, wind_clear, init))
    config.after_default_callbacks.extend((notify_clear,))
    config.after_load_callbacks.extend((anim_clear, wind_clear, upgrade))

    config.start_interact_callbacks.append(anim_sweep)

    config.screen_width = 1920
    config.screen_height = 1080

    config.thumbnail_width = config.screen_width // 5
    config.thumbnail_height = config.screen_height // 5

    config.window = 'hide'

    config.with_callback = with_callback
    config.end_splash_transition = fade
    config.enter_replay_transition = fade
    config.exit_replay_transition = fade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
