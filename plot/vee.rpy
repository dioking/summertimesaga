label vee_store_aisle:
    jump vee_store_aisle.intro

    menu vee_store_aisle.choice:
        "Vegetable stock." if saga.event.peek(choice='stock', who=saga.cast.vee):
            return saga.event.emit(choice='stock', who=saga.cast.vee)

        "What do you sell here?" if saga.cast.diane < 'bugs':
            jump vee_store_aisle.sales
        "Just browsing.":

            pass

    jump vee_store_aisle.outro


label vee_store_aisle.intro:
    jump vee_store_aisle.intro1


label vee_store_aisle.intro1:
    call shot.store_aisle_vee
    show old_anon 13 at pos(.8) with dissolve
    vee "Welcome to Consum-R, where all your needs are just an aisle away."
    vee "How can I help you today?"
    jump vee_store_aisle.choice


label vee_store_aisle.outro:
    show old_anon 10
    anon "I'm just looking around, thanks."
    show old_anon 5
    vee "No problem."
    vee "Lemme know if you need help with anything."
    show old_anon 10
    anon "Will do."
    hide old_anon with dissolve
    return


label vee_store_aisle.sales:
    show old_anon 10
    anon "What do you sell here?"
    show old_anon 5
    vee @ e_b f_happy m_laugh "It would probably be faster to tell you things we don't sell."
    vee "We carry pretty much everything a person needs to get by."
    show old_anon 10
    anon "So I can buy tools here?"
    show old_anon 5
    vee "Of course."
    show old_anon 10
    anon "How about groceries?"
    show old_anon 5
    vee "Uh huh."
    show old_anon 401
    anon "Computer parts?!"
    show old_anon 403
    vee "We got 'em."
    show old_anon 402
    anon "Clothes?"
    show old_anon 403
    vee @ e_b f_happy m_laugh "In all sizes."
    show old_anon 402
    anon "Kitchen appliances?!"
    show old_anon 403
    vee "Aisle 12."
    show old_anon 4 with dissolve
    anon "Hmm."
    show old_anon 401 with dissolve
    anon "How about bicycles?"
    show old_anon 403
    vee e_nw f_pensive @ -m_talk "Mountain bikes or BMX?"
    vee e_w f_horny "'Cause we have both."
    show old_anon 402
    anon "Wow, you guys really do carry everything."
    show old_anon 403
    vee "I told you."
    show vee f_calm
    jump vee_store_aisle.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
