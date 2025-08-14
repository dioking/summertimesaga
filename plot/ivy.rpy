label ivy_toy_shop:
    jump ivy_toy_shop.intro

    menu ivy_toy_shop.choice:
        "Toy." if saga.event.peek(choice='toy', who=saga.cast.ivy):
            return saga.event.emit(choice='toy', who=saga.cast.ivy)
        "Just shopping.":

            pass

    jump ivy_toy_shop.outro


label ivy_toy_shop.intro:
    if saga.cast.ivy < 'met':
        jump ivy_toy_shop.intro1

    jump ivy_toy_shop.intro2


label ivy_toy_shop.intro1:
    call shot.toy_shop_ivy
    show anon f_shy o_right at left with dissolve
    ivy "Hi!"
    ivy "Can I help you with something?"
    anon a_uneasy f_worried "It's my first time here. I... Umm..."
    ivy @ e_b f_happy m_laugh "It's okay! I understand! Everyone's a little shy when they first come here..."
    ivy "We have a large selection of toys and sexy apparel that you can view on our wall display."
    show anon a_pocket f_surprised
    ivy "We can also offer a... full body massage session in one of our... Private rooms."
    ivy "Our masseuse uses a variety of natural body relaxation techniques... That will surely satisfy your needs..."
    anon f_calm @ f_confused "Oh... I didn't know you offered massages here."
    ivy @ e_b f_happy m_laugh "It's one of our... Less advertised... Services."
    ivy "Would you like to see our massage selection pamphlet?"
    jump ivy_toy_shop.choice


label ivy_toy_shop.intro2:
    call shot.toy_shop_ivy
    show anon f_shy o_right at left with dissolve
    ivy "Hi!"
    ivy "Can I help you with something?"
    jump ivy_toy_shop.choice


label ivy_toy_shop.outro:
    anon f_shy "I'm fine, thank you."
    anon "I'm just here to do some shopping..."
    ivy @ e_b f_happy m_laugh "Alright, then! Let me know if you need anything else."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
