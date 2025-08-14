screen view(what, _sensitive):
    default layers = what.view

    on 'show' action Function(what.sound)

    for entity, path in layers:
        if entity and _sensitive:
            imagebutton:
                action Emit(interact=entity)
                alt entity
                at button, saga.easy.placement(path)
                focus_mask True
                idle (saga.easy.outline(path) if persistent.outlines else path)
                insensitive path

        else:
            add saga.easy.image(path)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
