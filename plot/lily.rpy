label lily_comic_shop:
    call shot.comic_shop_lily
    show anon a_pocket o_right at pos(.4) with dissolve
    lily "What's up?"

    menu lily_comic_shop.choice:
        "Cyclone." if saga.event.peek(choice='cyclone', who=saga.cast.lily):
            return saga.event.emit(choice='cyclone', who=saga.cast.lily)

        "Costumes." if saga.event.peek(choice='costumes', who=saga.cast.lily):
            return saga.event.emit(choice='costumes', who=saga.cast.lily)
        "You seem familiar.":

            jump lily_comic_shop.familiar
        "Any suggestions?":

            jump lily_comic_shop.ideas
        "I found what I need.":

            pass

    anon f_calm "Yeah, I think I have everything I need. Thanks!"
    lily "Great! Thanks for shopping at Cosmic Cumics..."
    show anon f_shy
    lily e_b f_happy m_laugh @ -m_talk "And tell your friends about us!"
    hide anon with dissolve
    return


label lily_comic_shop.familiar:
    anon a_think f_confused "I feel like I've seen you somewhere."
    lily e_b f_happy m_laugh @ -m_talk "Right. Well, you've probably seen me on the internet..."
    show anon a_side
    lily e_w f_calm -m_laugh "I do a lot of video game streams and I post them on my GooTube channel."
    lily f_horny "I usually go by the name of VirginLily69."
    anon f_happy "Oh, right! My friend [saga.cast.erik] loves your stuff!"
    anon f_shy of_blush "He keeps talking about your videos and your huge... Err... Fan base!"
    lily e_b f_happy m_laugh @ -m_talk "Aww... You guys are so sweet."
    lily e_w f_calm -m_laugh "Is there anything else you want to talk about?"
    show anon -of_blush
    jump lily_comic_shop.choice


label lily_comic_shop.ideas:
    anon "Do you have any suggestions? New products that you would recommend?"
    lily @ -m_talk "Hmmm..."
    lily "Well, I really love cosplay!"
    lily f_horny "I like to wear {i}sexy outfits{/i}. Actually, we have a new line of costumes that just came in!"
    anon f_shy of_blush "Oh, yeah? Sounds interesting..."
    lily "It's sometimes hard to fit my... Umm... Forms into them."
    lily "They make them so tight, you know?"
    lily @ e_b f_happy m_laugh "But guys usually don't seem to mind!"
    anon a_uneasy -of_blush "Haha. I see."
    anon "Thanks, I'll have a look."
    show lily f_calm
    jump lily_comic_shop.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
