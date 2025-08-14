label debbie_rug:
    return


label debbie_rug.alt:
    jenny "Mmm."
    pause
    jenny "That's it!"
    jenny "Call me princess!!"
    pause
    jenny "Don't talk back to me..."
    jenny "... You know you want it!"
    jenny s_10 "Ahh, fuck!"
    anon "( Hmm? )"
    pause
    jenny "Shut up and eat my pussy!"
    pause
    jenny "Mmm, just like that."
    jenny "Oh, I bet you wanna fuck me, don't you?"
    jenny "Say it, [saga.cast.anon]!"
    anon "( !!! )"
    jenny s_12 "Ngh, that's right!"
    anon "( She's imagining me! )"
    jenny "Get on your knees!"
    pause
    jenny "Now lick my feet and beg me!"
    jenny s_14 "Mhmm..."
    jenny s_16 "... All my toes."
    pause
    jenny "Ahh, fuck!"
    pause
    jump debbie_rug.merge


label debbie_rug.block:
    call shot.debbie_bed2_door
    show anon f_happy o_right with dissolve
    anon @ -m_talk "( Nah, I shouldn't interrupt her while she's practicing her mantra. )"
    anon e_b m_teeth @ -m_talk "( It tends to make her cranky. )"
    hide anon with dissolve
    return


label debbie_rug.coma:
    scene debbie_attic_spy -gap
    show jenny p_bed2_spy_coma
    show debbie_attic_spy gap as gap
    with fade
    anon "( Heh, she's really out of it. )"
    pause
    return


label debbie_rug.diary:
    scene debbie_attic_spy -gap
    show jenny a_diary p_bed2_spy_diary
    show debbie_attic_spy gap as gap
    with fade
    anon "( Hmm, she's just lying around, writing in her diary... )"
    show jenny a_diary_write
    pause
    anon "( Booooring!! )"
    return


label debbie_rug.empty:
    scene debbie_attic_spy
    with fade
    anon "( Hmm, just an empty bed... )"
    anon "( I wonder where she's at? )"
    return


label debbie_rug.laptop:
    scene debbie_attic_spy -gap
    show jenny p_bed2_spy_laptop
    show debbie_attic_spy gap as gap
    with fade
    anon "( Nice view! )"
    pause
    return


label debbie_rug.once:
    scene debbie_attic
    anon "( That's one ugly rug... )"
    anon "( I wonder why it's up here? )"

    scene mono debbie_attic_spy
    mono "Thinking as if to examine it, I lifted the corner,\nand as I did so something beneath it caught my eye." with fade
    mono "Upon closer inspection, it seemed that this rug was covering up a larger mystery."

    scene mono debbie_attic_spy_crack
    mono "What contrived combination of happenstance had conspired to create this curious aperture..." with fade
    more "... and how was it even physically possible given the orientation of the attic?"
    mono "These questions and more were quickly forgotten however, left forever unanswered, as the enormity of my discovery came into focus."
    return


label debbie_rug.play(what=None):
    scene debbie_attic_spy -gap
    show jenny p_bed2_spy_play_01
    show debbie_attic_spy gap as gap
    with fade
    anon "( I-is she- )"
    show jenny p_bed2_spy_play_02
    anon "( !!! )" with hpunch
    show jenny p_bed2_spy_play_03 with dissolve.nowait
    anon "( She's masturbating! )"
    show jenny a_rub p_bed2_spy_play_04 with dissolve.nowait
    anon "( Oh, this is awesome!! )"

    scene debbie_bed2_spy_rub
    show jenny a_rub p_debbie_bed2_rub s_8
    with fade

    if what == 'anon':
        jump debbie_rug.alt

    jenny "Mmm."
    pause
    jenny "That's it, Daddy!"
    jenny "Gimme the big one!"
    pause
    jenny "Haah, twenty-four karat..."
    jenny "... Amethyst encrusted..."
    jenny s_10 "... Ahh, fuck!"
    anon "( Hmm? )"
    pause
    jenny "What's that?"
    jenny "You wanna take me out on your new yacht?!"
    pause
    jenny "Mmm, champagne in the hot tub?!"
    jenny s_12 "Oh, yes..."
    jenny "... Fill me up!"
    anon "( This is what she thinks about when she's masturbating?! )"
    pause
    jenny "Ahh, but I can't decide between the red convertable and the black-"
    jenny "Oh, really?"
    jenny "You're gonna buy them both for me?!"
    jenny s_16 "Ngh, you're the best!"
    pause

    label debbie_rug.merge:
    scene debbie_attic at stage
    show anon a_pocket e_s f_shocked m_open at right

    if what == 'anon':
        show anon d_hard e_w f_horny_smug z_b_ob_a_oa_f_of_d_od -m_open

    with fade
    anon @ -m_talk "( Oh kay... )"

    if what == 'anon':
        anon @ -m_talk "( ... That's a little disturbing... )"
    else:
        anon e_w f_worried m_idle @ -m_talk "( ... That's kinda messed up... )"

    show anon a_think e_nw f_pensive -z_b_ob_a_oa_f_of_d_od
    pause
    anon a_side e_b f_happy m_teeth @ -m_talk "( ... But still hot. )"
    anon @ -m_talk "( Thank you, peephole! )"
    hide anon
    with dissolve
    return


label debbie_rug.redo:
    scene debbie_attic at stage(.84, .85, 5, b=0)
    anon "( Let's see what [saga.cast.jenny] is up to... )"
    return


label debbie_rug.seen:
    scene debbie_attic_spy -gap
    show jenny a_rub p_bed2_spy_play_04
    show debbie_attic_spy gap as gap
    with fade
    anon "( Looks like she's going to be going at it for a while... )"
    anon "( ... Best move on before I get a cramp. )"
    pause

    scene debbie_attic at stage
    show anon a_shy_neck e_b f_hurt m_teeth
    with fade
    anon @ -m_talk "( It's super uncomfortable leaning over this hole. )"
    hide anon
    with dissolve
    return


label debbie_rug.sleep:
    scene debbie_attic_spy -gap
    show jenny p_bed2_spy_sleep
    show debbie_attic_spy gap as gap
    with fade
    anon "( Aww, she's already gone to bed for the night. )"
    pause
    anon "( Heh, she looks kinda cute and innocent when she's sleeping... )"
    anon "( ... Not at all like the bitchzilla she really is! )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
