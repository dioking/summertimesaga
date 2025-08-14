label jen03_intro:
    scene debbie_bed3 at stage
    show anon a_surprised e_nw f_pensive o_right at left with dissolve
    anon @ -m_talk "( Wow, something smells delicious! )"
    anon a_side e_w f_calm @ -m_talk "( [saga.cast.debbie] must be cooking breakfast downstairs. )"
    anon @ -m_talk "( I should go check it out! )"
    hide anon
    with dissolve
    return


label jen03_kitchen:
    scene debbie_kitchen -debbie at stage
    show debbie a_mug at right
    show anon a_pocket o_right at left with dissolve
    anon "Morning [saga.cast.debbie]."
    show anon e_s f_worried p_debbie_hug_lean at pos.debbie
    debbie b_anon p_hug_lean "Good morning, sweetie."
    pause
    show anon e_w f_calm -p_debbie_hug_lean at left
    show debbie -b_anon -p_hug_lean
    anon "Mmm, breakfast smells wonderful!"
    debbie @ e_b f_happy m_laugh "Hehe, it's almost done."
    debbie "Why don't you go sit down at the table and I'll bring it to you?"
    anon "Awesome, thanks, [saga.cast.debbie]!"
    anon -o_right "( [saga.cast.debbie] makes the best breakfast! )"
    hide anon
    with dissolve

    call shot.debbie_dining_breakfast
    show debbie_dining_table food3 plate3 -bowl3 as table
    show anon a_down e_e p_table behind table
    show jenny a_spoon e_s p_table behind table
    with fade
    pause
    anon "Morning."
    jenny @ -m_talk "Mmhmm."
    anon e_w f_tired "Why are you eating cereal?"
    anon "Didn't you see [saga.cast.debbie] cooking breakfast?"
    show anon e_e f_calm
    jenny f_annoyed @ e_r "Yes, but I was recently told I need to grow up and support myself, remember?"
    anon f_surprised @ -m_talk "..."
    anon f_calm "Are you really still pouting about that?"
    jenny "I'm not pouting."
    anon "Yes, you are."
    jenny "Tsk, shut up."
    pause
    jenny e_w "Hey, lend me sixty dollars."
    anon f_worried "Huh?!"
    jenny "I said, lend me sixty dollars."
    anon "What for?!"
    jenny e_r "Ugh, that's none of your business!"
    show jenny e_w
    anon "Umm, it's my money... so yes, it kinda is my business!"
    jenny "{i}*Sigh*{/i} Look, I know a way I can make some money but I need to buy something first."
    jenny "I'll pay you back."
    anon f_calm "Yeah, right."
    anon "How are you gonna pay me back?!"
    anon "You don't even have a job."
    jenny f_angry m_teeth "Don't be a dick, [saga.cast.anon]!"
    jenny f_annoyed -m_teeth "I know [saga.cast.diane] is overpaying you for whatever the hell you're doing at her house."

    if saga.cast.diane < 'garden':
        anon f_grumpy "I've not even spoken to her about it yet!"
        anon "[saga.cast.debbie] just suggested I ask if she needs help tending to her garden."
    else:

        anon "I'm tending her garden."

    jenny f_snide "Yeah, whatever."
    jenny "Don't care."
    jenny "The point is, you can spare sixty measly dollars."
    anon f_worried "No way!"
    anon "I need every cent I can get if I want to make tuition next year..."
    anon "... Especially now that Dad's gone."
    jenny f_angry m_teeth "Grr, fine..."
    jenny "... But I'm gonna remember this!"
    show debbie_dining_table pull4
    show debbie a_potato e_wsw p_table_stand behind table
    with dissolve
    pause
    show jenny e_s f_calm -m_teeth
    show anon f_calm
    debbie "Here you go, sweetie."
    show debbie e_sw p_table_bend
    anon e_w "Thanks, [saga.cast.debbie]."
    show anon a_bowl e_s f_shy
    debbie e_wsw p_table_stand "You want me to fix you a plate, [saga.cast.jenny]?"
    show debbie_dining_table pull2
    jenny e_w f_annoyed p_table_rise "No, I do not."
    show debbie f_sad
    show anon a_eat f_calm m_bite
    hide jenny
    with dissolve
    pause
    show anon a_down v_chew -m_bite
    debbie "What's the matter with her?"
    anon e_nw f_surprised "She's still pouting over what you said the other night."
    debbie "{i}*Sigh*{/i} I guess, I should go and apologize to her."
    anon "No you shouldn't, [saga.cast.debbie]."
    anon "She's just being a bitch."
    debbie "[saga.cast.anon]!"
    debbie "Don't say that about [saga.cast.jenny]!"
    anon "Sorry, [saga.cast.debbie]..."
    anon "... But it's true."
    debbie f_calm "Tsk, just eat your breakfast."
    anon f_calm v_normal "Thanks again for this, it's delicious!"
    show anon a_bowl e_s
    debbie "You're welcome, sweetie."
    show anon a_eat m_bite with dissolve

    scene black
    with dissolve
    mono ""

    call shot.debbie_dining_breakfast
    show debbie_dining_table plate3 -bowl2 -bowl3 -milk as table
    show anon a_down e_nw f_pensive p_table behind table
    with dissolve
    anon @ -m_talk "( What in the heck does she need sixty dollars for any way? )"
    anon e_w f_pouty @ -m_talk "( Her broke ass should be out looking for a job. )"
    show debbie_dining_table pull3
    show debbie_dining_table -plate3 as table
    hide anon
    with dissolve
    pause

    scene debbie_kitchen at stage with fade
    show anon a_plate f_happy o_right with dissolve
    anon @ -m_talk "( Oh well, not my problem. )"
    hide anon
    with dissolve
    return


label jen03_kitchen.rails:
    scene camera at stage
    show anon o_right with dissolve
    anon @ -m_talk "( That smell is coming from the kitchen! I can almost taste it! )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
