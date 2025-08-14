screen books(what, _sensitive=renpy.get_mode() == 'screen'):
    layer 'master'
    sensitive _sensitive

    default game = saga.mini.books(what)

    add saga.easy.image('art/mini/books/base.png')

    for book, path, abs, mask, rel in game.stack:
        if not book:
            add saga.easy.image(mask)
            continue

        button:
            action Emit(interact=book)
            alt book
            at button, Transform(mesh=True, offset=abs)
            focus_mask True

            has fixed
            fit_first True

            add path

            if mask:
                add mask blend 'clip' offset rel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
