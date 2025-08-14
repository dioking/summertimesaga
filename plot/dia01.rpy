label dia01_intro:
    scene mono diane_garden
    mono "I may not have known the first thing about gardening, but it was nice to see [saga.cast.diane]." with fade
    mono "Growing up, I'd always liked her, she was just a fun person to be around!"
    more "Kind-hearted and supportive, with a great sense of humor and so full of warmth."

    scene diane_yard -diane -statue_whole
    show anon a_pocket o_right at left
    show diane a_shovel_hip at right
    with fade
    diane "Well, there's a handsome young man..."
    diane e_b f_shy m_laugh @ -m_talk "You've grown so much, I hardly recognized you at the funeral."
    show diane e_w f_calm -m_laugh
    anon @ e_b f_happy m_laugh "Heh, hi [saga.cast.diane]."
    show diane f_surprised
    anon "Wow! You look so much like [saga.cast.debbie]..."
    diane e_ne f_pensive @ -m_talk "Oh, come now. I'm not nearly as pretty as [saga.cast.debbie]..."
    show diane e_w f_surprised
    anon @ e_b f_smug "Well, I think you look great, [saga.cast.diane]!"
    diane a_shovel_cheek e_b f_shy m_laugh of_blush @ -m_talk "Aww, aren't you just a little charmer?!"
    diane e_w f_surprised -m_laugh @ -m_talk "..."
    diane e_b f_shy m_laugh @ -m_talk "You here to do some work for me?"
    diane e_w f_calm -m_laugh "I'm guessing [saga.cast.debbie] told you I'm looking for someone to help me this summer?"
    anon "Yeah, she told me to come see you. I could definitely use the money for tuition."
    diane "Wonderful!"
    diane "I was hoping to get you started today but I'm afraid I ran into a problem..."
    diane a_shovel_broken e_sw f_ashamed m_talk "My old shovel finally quit on me."
    show diane e_w -m_talk
    anon e_sw f_worried "Oh! Yeah, that looks pretty bad."
    diane m_talk "We may have to wait until I can replace it..."
    diane "I'm sorry, [saga.cast.anon]."
    show diane a_shovel_hip -m_talk

    if saga.prop.tool_shovel in saga.cast.anon:
        jump dia01_diane

    anon e_w f_calm "It's okay, [saga.cast.diane]."
    show diane f_calm
    label dia01_intro.merge:
    anon "Is there any way we can continue the work without it?"
    diane "Well, we can't really dig up a garden without a shovel, can we?"
    diane "I'll just have to pick up a new one next time I'm at the store."
    diane f_pouty m_talk "Unless..."
    show diane f_calm -m_talk
    anon @ f_sceptical "Unless?"
    diane "... You wouldn't happen to have one at home?"
    anon @ a_think e_nw f_pensive -m_talk "Hmm..."
    anon "We might have a shovel in our garage!"
    anon "I'll have to go check."
    diane e_b f_shy m_laugh @ -m_talk "That would be great!"
    diane e_w f_calm -m_laugh "Come on back if you find one, and we'll get started."
    hide anon with dissolve
    return


label dia01_shovel:
    return


label dia01_shovel.diane:
    anon "I still haven't found that shovel."
    jump dia01_intro.merge


label dia01_diane:
    anon a_backpack e_s @ -m_talk "Hmm..."
    show diane f_surprised
    show anon a_backpack_shovel_01
    pause
    show diane m_talk of_none
    show anon a_backpack_shovel_02
    pause
    show diane -m_talk
    anon a_shovel e_w "Here it is!"
    diane e_b f_shy m_laugh @ -m_talk "Ohh! Wonderful!"
    diane e_w f_calm -m_laugh "See, you've been a big help already!"
    show anon a_pocket
    diane a_shovel_give "Alright, before you start, I'll have to show you what to do..."
    diane a_shovel_finger e_b "Make sure you only keep the vegetables that are long and hard!"
    diane "Take out everything else... Especially those pesky rats and bugs, got it?"
    show diane a_shovel_hip e_w
    anon "Got it!!"
    diane "You should really take all the money I'm paying you to the bank too, when you're done!"
    diane "That's your decision though."
    anon @ a_uneasy "Umm, sure. I guess I could do that..."
    diane @ e_b f_happy "Alright handsome, let's get to work!"
    show diane b_anon p_kiss_cheek behind anon at pos.anon
    anon a_none b_none f_surprised @ -m_talk "..."
    show anon a_pocket -b_none
    show diane p_stand -b_anon at right
    pause
    diane "Well, don't be timid, [saga.cast.anon]."
    show anon e_wsw
    diane a_shovel_give @ e_b f_happy "Dig in!"
    show diane a_side
    anon a_shovel e_w f_shy "R-right."
    anon e_wnw @ -m_talk "( I can do this! )"
    hide anon with dissolve
    return True


label dia01_outro:
    scene mono diane_dig
    mono "It was only after [saga.cast.diane] went to lie down, and I'd started to dig up her garden, that I began to appreciate how hot it was, and just how many weeds and bugs needed to be dealt with!" with fade
    mono "I grit my teeth and kept myself to the task, hoping all the while that she'd be compensating me well for so much physical labor."

    call mini.garden ('fresh')

    scene mono diane_eyes
    mono "As I worked, it became apparant that [saga.cast.diane] was watching me very intently..." with fade
    more "... But I suppose she was just trying to make sure I did a good job."
    mono "We exchanged the odd few words here and there, but it was mostly just small talk."

    if not _return[1]:
        jump dia01_outro.fail

    scene diane_yard -diane at stage
    show anon a_pocket o_right at left
    show diane a_shovel_hip at right
    with fade
    diane "Oh, wow! My garden looks absolutely gorgeous, [saga.cast.anon]!"
    show diane f_horny
    anon "Yeah... I had to get rid of a lot of stuff..."
    show diane a_shovel_cucumber e_sw f_pouty m_talk with dissolve
    show anon f_surprised
    diane "Just look at that big, hard cucumber!"
    show diane e_w f_horny -m_talk
    anon @ -m_talk "..."
    anon f_worried "Why do you only want the vegetables that are long and hard?"
    diane f_ashamed m_talk "I err..."
    diane e_sw "Well, you see they... Umm..."
    show diane e_w -m_talk
    anon "Do they sell better or something?"
    diane e_b f_shy m_laugh @ -m_talk "Yes!! That's exactly it!"
    diane e_sw f_pouty m_talk "They sell better."
    show diane e_w f_horny -m_talk
    anon f_calm @ f_sceptical "Hmm, interesting."
    anon "I guess I have a lot to learn about vegetables..."
    diane a_shovel_hip f_calm "Well, don't you worry, [saga.cast.anon]."
    diane "I can teach you everything there is to know about gardening."
    anon "How did you get into this stuff anyways?"
    diane "Oh, I've always had a bit of a green thumb. Even when I was a kid."
    anon "Really?"
    diane e_b f_shy m_laugh @ -m_talk "You betcha!"
    diane e_w f_calm -m_laugh "You know, I used to dream about owning a farm of my own..."
    anon "Like a for real farm? With fields of crops and animals?"
    diane "That's right! I wanted the whole nine yards!"
    anon "You should totally do that, [saga.cast.diane]!"
    anon @ e_b f_happy m_laugh "I'd help you!"
    diane e_b f_shy m_laugh @ -m_talk "Haha, yeah well, thanks, [saga.cast.anon]... I'm afraid it's not as easy as all that."
    show diane e_w f_calm -m_laugh
    anon "Yeah, I suppose you're right."
    diane e_b f_shy m_laugh @ -m_talk "Thanks for your help today!"
    diane e_w f_calm -m_laugh "Why don't you come back tomorrow, and we'll continue where we left off?"
    anon "Alright, I'll see you tomorrow then."
    diane f_horny "Bye, handsome."
    hide anon with dissolve
    return _return[0]


label dia01_outro.diane:
    scene diane_yard -diane at stage
    show diane a_shovel_hip at right
    show anon o_right at left with dissolve
    diane "Well, don't be timid, [saga.cast.anon]."
    diane a_shovel_give @ e_b f_happy "Dig in!"
    show diane a_side
    anon a_shovel "R-right."
    anon @ -m_talk "( I can do this! )"
    hide anon with dissolve
    return


label dia01_outro.fail:
    scene diane_yard -diane at stage
    show anon a_pocket f_worried o_right at left
    show diane a_shovel_hip f_sad at right
    with fade
    diane "Hmm... There's some room for improvement."
    anon e_sw "Yeah... I didn't do too well. Sorry, [saga.cast.diane]!"
    diane f_ashamed m_talk "It's okay... You're new at this..."
    show anon e_w f_calm
    diane e_b f_shy m_laugh @ -m_talk "And I'm sure you'll get better at it!"
    diane e_w f_calm -m_laugh "I always need fresh vegetables..."
    anon "I guess so..."
    diane a_shovel_finger f_horny "Just make sure you only keep the vegetables that are long and hard!"
    show diane a_shovel_hip f_calm
    anon "I'll do better next time..."
    anon @ e_b f_happy m_laugh "Thanks, [saga.cast.diane]!"
    hide anon with dissolve
    return _return[0]


label dia01_outro.rails:
    scene camera at stage
    show anon a_shovel e_b f_happy m_laugh with dissolve
    anon @ -m_talk "( Heh, a rare situation that I {i}can{/i} dig my way out of! )"
    anon e_sw -m_laugh @ -m_talk "( Keep the long and hard ones, clear the rest. Got it. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
