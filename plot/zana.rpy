label zana_cinema_lobby:
    jump zana_cinema_lobby.intro

    menu zana_cinema_lobby.choice:
        "Never mind.":
            pass

    jump zana_cinema_lobby.outro


label zana_cinema_lobby.intro:
    scene cinema_desk
    show zana
    show cinema_desk desk as desk
    show anon a_pocket o_right at pos(.175) with dissolve
    zana "Welcome to CineSaga Theater, my name is Bubbles."
    zana "How can I help you?"
    jump zana_cinema_lobby.choice


label zana_cinema_lobby.outro:
    anon "I'm just looking around, thanks."
    zana "Alright."
    zana "Just let me know if you wanna watch something."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
