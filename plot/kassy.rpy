label kassy_gift_shop:
    jump kassy_gift_shop.intro


label kassy_gift_shop.intro:
    if saga.cast.kassy < 'met':
        jump kassy_gift_shop.intro1

    jump kassy_gift_shop.intro2


label kassy_gift_shop.intro1:
    call shot.gift_shop_kassy
    show old_anon 1 at right with dissolve
    kassy "Welcome to Cupid. My name is [saga.cast.kassy], is there anything I can help you find today?"
    show old_anon 2
    anon "No thanks, I'm just looking around."
    show old_anon 1
    kassy "Alright. Well, let me know if you need any help."
    show old_anon 2
    anon "Will do! Thanks, [saga.cast.kassy]."
    show old_anon 1
    kassy "My pleasure!"
    hide old_anon with dissolve
    return


label kassy_gift_shop.intro2:
    call shot.gift_shop_kassy
    show old_anon 2 at right
    with dissolve
    anon "Hey [saga.cast.kassy]!"
    show old_anon 1
    kassy "Hello there, what can I help you with?"
    show old_anon 2
    anon "Nothing right now, just browsing."
    show old_anon 1
    kassy "Alright. Well, give me a shout if you need something."
    show old_anon 2
    anon "Will do! Thanks, [saga.cast.kassy]."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
