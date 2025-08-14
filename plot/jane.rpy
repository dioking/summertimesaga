label jane_library_lobby:
    jump jane_library_lobby.intro

    menu jane_library_lobby.choice:
        "Membership." if saga.event.peek(choice='join', who=saga.cast.jane):
            return saga.event.emit(choice='join', who=saga.cast.jane)

        "French dictionary." if saga.event.peek(choice='vocab', who=saga.cast.jane):
            return saga.event.emit(choice='vocab', who=saga.cast.jane)

        "French food." if saga.event.peek(choice='food', who=saga.cast.jane):
            return saga.event.emit(choice='food', who=saga.cast.jane)

        "Overdue books." if saga.event.peek(choice='books', who=saga.cast.jane):
            return saga.event.emit(choice='books', who=saga.cast.jane)

        "French poetry." if saga.event.peek(choice='poetry', who=saga.cast.jane):
            return saga.event.emit(choice='poetry', who=saga.cast.jane)

        "Magazines." if saga.event.peek(choice='mags', who=saga.cast.jane):
            return saga.event.emit(choice='mags', who=saga.cast.jane)

        "Dairy operations." if saga.event.peek(choice='dairy', who=saga.cast.jane):
            return saga.event.emit(choice='dairy', who=saga.cast.jane)
        "Never mind.":

            pass

    jump jane_library_lobby.outro


label jane_library_lobby.intro:
    call shot.library_lobby_jane
    show old_anon 1 at right with dissolve
    jane "Hi! How can I help you?"
    jump jane_library_lobby.choice


label jane_library_lobby.outro:
    show old_anon 24
    show jane f_sad
    anon "Sorry. I'll return once I remember the book's name."
    show old_anon 5
    jane f_calm "See you then."
    hide old_anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
