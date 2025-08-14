label tool_shovel(busy):
    scene debbie_garage at stage(.76, .55, 2.5)
    show anon a_shovel e_sw f_shy o_right at left with dissolve

    if saga.cast.diane < 'met':
        anon @ -m_talk "Hmm."
        anon @ -m_talk "( I'm sure this shovel will come in handy at somepoint. )"
    else:

        anon @ -m_talk "( Yeah, this should work! )"
        anon @ -m_talk "( It'll be nice to have some money for a change... )"

    if busy:
        hide anon with dissolve
        return

    jenny "{i}*Ahem*{/i}"
    anon e_w f_surprised m_teeth @ -m_talk "!!!" with hpunch
    show jenny a_fold f_annoyed at right with dissolve.nowait
    jenny "What are you doing with that shovel?"
    anon f_worried -m_teeth "... Huh?"

    if saga.cast.diane < 'met':
        anon @ e_nw "Oh, ehh... nothing specific, really..."
        anon f_shy "... I just thought it might be nice to have a shovel on hand."
        jenny f_disgusted @ -m_talk "..."
        anon f_happy "You never know what you're gonna run into out in Summerville, ya know?"
        jenny "What the fuck are you doing with your life that you randomly find yourself needing a shovel?"
        anon f_shy "Well, I-"
        show anon f_surprised
        jenny a_wave_off f_annoyed "Ugh, never mind... I don't care."
        show anon f_pouty
        jenny "You're such a weirdo!"
        show jenny a_fold
        anon @ -m_talk "..."
    else:

        anon f_calm "Oh! I'm taking it to [saga.cast.diane]'s house."
        anon "I'm going to be working for her this summer."
        jenny "[saga.cast.diane] gave you a job?"
        jenny "... She's never offered me any work!"
        anon a_pocket "Well, it's physical labor in her garden."
        anon "She probably just assumed you wouldn't be interested..."
        jenny e_r "Ugh, in this heat?"
        jenny e_w "Yeah, no way. Screw that!"

    anon f_confused "What are you doing in the garage?"
    anon "You never come out here..."
    jenny a_hips f_calm "I need some batteries. Don't we still have some out here?"
    show anon a_think e_nw f_pensive
    pause
    anon a_pocket e_w f_calm "Yeah, I think so."
    anon @ a_point "Try that box on bottom shelf there."
    pause
    show jenny o_right p_bend_away at pos(.65, 1.013)
    anon e_sw f_surprised "!!!"
    pause
    show jenny p_pickup_away
    pause
    show jenny a_battery f_annoyed o_left p_stand at right
    anon e_w f_sceptical "Holy crap, what do you need so many for?"
    jenny "None of your business, loser!"
    jenny "Just take your shovel and beat it."
    anon "Tch, whatever."

    if saga.cast.diane < 'met':
        jenny f_snide "Have fun playing with your shovel."
    else:
        jenny f_snide "Have fun busting your ass for [saga.cast.diane]..."

    jenny e_b f_calm m_laugh @ -m_talk "Hahaha!"
    hide jenny with dissolve.nowait
    anon "... She's such a bitch."

    if saga.cast.diane < 'met':
        pause
        anon @ -m_talk "( Whatever. )"
        anon @ -m_talk "( One shovel: acquired! )"
    else:

        anon @ -m_talk "( {i}*Sigh*{/i} Alright, well... I've got a shovel for [saga.cast.diane] now. )"

        if saga.time.tod < saga.time.dusk:
            anon e_b f_happy m_laugh @ -m_talk "( Time to head back to her place and start gardening. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
