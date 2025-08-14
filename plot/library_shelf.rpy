label library_shelf:
    return


label library_shelf.item:
    show library_lobby -desk at stage(.4, .56, 6.5)
    show anon at right with dissolve.nowait
    jane "Ah ah!"
    jane "You'll need a library card if you want access to those."
    anon a_uneasy f_shy "Oh, right."
    hide anon
    with dissolve
    return


label library_shelf.jane:
    show old_anon 10
    anon "How much was that membership again?"
    show old_anon 13
    jane "Twenty dollars."
    jane "Have you reconsidered?"

    menu:
        "Yes, sign me up!" if saga.cast.anon.cash >= 20:
            jump library_shelf.signup2
        "Not right now.":

            pass

    show old_anon 10
    anon "I think I'll pass, thanks."
    show old_anon 13
    jane "Oh, okay then."
    jane "Have a good day!"
    hide old_anon
    with dissolve
    return


label library_shelf.lobby:
    scene library_lobby at stage
    show old_anon 1 at old_left
    show jane at right
    with dissolve
    jane "Hi!"
    show old_anon 14
    anon "Oh, hi!"
    anon "I'm looking for some school textbooks."
    show old_anon 1
    jane "Do you have a membership card?"
    show old_anon 10
    anon "Umm... no, I don't think I have one."
    show old_anon 13
    jane @ e_b f_happy m_laugh "Oh. That's okay!"
    jane "Would you like to get one?"
    show old_anon 11
    jane @ e_b f_happy m_laugh "Membership is twenty dollars, and you get access to all of our selections!"
    show old_anon 2
    anon "Uhh... I guess I have no choice. Haha."
    show old_anon 13
    jane @ e_b f_happy m_laugh "Knowledge is priceless, right?"
    jane "Would you like to join right now?"

    menu:
        "Yes please." if saga.cast.anon.cash >= 20:
            jump library_shelf.signup1
        "Maybe later.":

            pass

    show old_anon 4
    anon "Hmm..."
    show old_anon 35
    anon "Actually, I think I'll pass..."
    show old_anon 1
    jane "Oh... Alright then."
    show old_anon 2
    anon "I might come by another time!"
    show old_anon 1
    jane "Okay, have a good day!"
    hide jane
    with dissolve
    return


label library_shelf.signup1:
    show old_anon 4
    anon "Hmm..."
    show old_anon 174 with dissolvefast
    show jane a_hand_out
    anon "All right. Here's twenty dollars."
    show old_anon 1 with dissolvefast
    jane a_side @ e_b f_happy m_laugh "Thank you!"
    jane "If you're looking for a specific book, just come to the front desk."
    jane "I'll look them up and find 'em for ya!"
    show old_anon 2
    anon "That sounds great! Thanks!"
    hide jane
    with dissolve
    return True


label library_shelf.signup2:
    show old_anon 2
    anon "Yes."
    show old_anon 174 with dissolvefast
    show jane a_hand_out
    anon "Here you go."
    show old_anon 1 with dissolvefast
    jane a_side "Thank you!"
    jane "Any time you're looking for a book, just come and ask."
    jane "I can look them up and find 'em for ya."
    show old_anon 2
    anon "That'd be great, thanks!"
    hide old_anon
    with dissolve
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
