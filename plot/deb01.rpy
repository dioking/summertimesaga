label deb01_lobby:
    scene debbie_lobby at stage with None
    show anon a_pocket f_tired

    if saga.cast.debbie in saga.sets.debbie_kitchen:
        show anon o_right

    with dissolve
    debbie "No, I'm not going to pay you!"
    anon f_confused @ -m_talk "( Is that [saga.cast.debbie]? )"
    debbie "Because I don't even know who you are!!"
    pause
    debbie "Ugh, that's ridiculous!"
    show anon f_surprised
    debbie "No, he worked for the bank."
    anon @ -m_talk "( She's talking about Dad! )"
    show anon f_confused
    debbie "N-no, that's not-"
    debbie "None of this makes any sense!!"
    anon @ -m_talk "( I should see what's going on. )"
    hide anon with dissolve
    return


label deb01_lobby.nap:
    scene debbie_bed3 at stage
    show anon a_pocket e_nw f_surprised with dissolve
    "*Distant voice*"
    anon f_pensive @ -m_talk "( Is that [saga.cast.debbie] on the phone? )"
    anon e_w f_worried @ -m_talk "( She sounds upset... )"
    anon @ -m_talk "( ... I should go see if she's okay. )"
    hide anon
    with dissolve
    return


label deb01_catch:
    return


label deb01_catch.rails:
    scene camera at stage with None
    show anon a_pocket f_worried_surprised

    if saga.cast.anon in saga.zone.debbie_floor1:
        if saga.cast.debbie in saga.sets.debbie_kitchen:
            show anon o_right

    elif saga.cast.anon not in saga.sets.debbie_bed3:
        show anon o_right

    with dissolve
    anon @ -m_talk "( Better check on [saga.cast.debbie] before bed... )"
    hide anon with dissolve
    return


label deb01_debbie:
    if saga.cast.debbie in saga.sets.debbie_kitchen:
        scene debbie_kitchen -debbie at stage
        show debbie o_right at right
    else:

        scene debbie_lounge -debbie -desk at stage
        show debbie at left
        show debbie_lounge desk as desk

    show debbie a_phone_talk f_angry
    with none
    debbie "No, I've told you already!"
    debbie "I don't know anything about any money!"

    if saga.cast.debbie in saga.sets.debbie_kitchen:
        show anon o_right at left
    else:
        show anon at right

    show anon a_pocket f_worried
    with dissolve.nowait
    pause
    debbie "Oh, I don't believe that!"
    pause
    debbie f_sad "What?!"
    debbie "Y-you can't-"
    pause
    debbie "We don't have that kind of money!"
    pause
    debbie f_angry @ -m_talk "..."
    debbie "Hey, don't you threaten me, mister!"
    anon f_shocked m_open @ -m_talk "!!!" with hpunch
    anon f_worried -m_open @ -m_talk "( Someone is threatening her? )"
    pause
    debbie "Ugh, I'm not going to listen to this!"
    pause
    debbie "I'm hanging up now."
    debbie "Don't you call back here again!"
    pause
    debbie "JUST LEAVE US ALONE!!!"
    show debbie a_phone_facepalm e_b f_sad
    pause
    anon "[saga.cast.debbie]?"
    debbie @ -m_talk "Hmm?"

    if saga.cast.debbie in saga.sets.debbie_kitchen:
        show debbie o_left
    else:
        show debbie o_right

    debbie a_phone_side e_w "Oh, umm... Hi, sweetie."
    anon "Who was that on the phone?"
    debbie "It was nobody."
    anon "Nobody?"
    anon "It didn't sound like nobody."
    debbie "Just some people making up a bunch of nonsense about your father."
    anon a_facepalm e_osw f_sad @ -m_talk "..."
    anon e_w f_worried "Did Dad owe people money or something?"
    anon a_side "Because I can find a job and-"
    debbie f_worried_surprised "No, no, don't be silly!"
    debbie "You need to focus on school and save your money for tuition."
    anon "[saga.cast.debbie], seriously, I can help."
    anon "I'm old enough."
    anon "You shouldn't have to carry the burden all on your own."
    debbie f_sad "Oh, sweetie..."
    show debbie b_anon p_hug_away at pos.anon
    show anon a_none b_none
    debbie "... You're such a wonderful boy!"
    debbie "This isn't something I want you to worry about, okay?"
    show debbie f_calm -b_anon -p_hug_away at center
    show anon a_side -b_none behind debbie
    debbie "It's just a simple misunderstanding, and I can handle it... I promise."
    anon f_calm "O-okay."
    pause
    debbie "Did you go see [saga.cast.diane] about that gardening work, like I told you?"

    if saga.cast.diane < 'met':
        anon f_shy "Ehh, not quite."
        debbie "What happened?"
        anon a_uneasy f_worried @ e_sw "I guess, I sorta... got distracted."
        anon "Sorry, [saga.cast.debbie]."
        show anon a_side
        debbie "Oh, it's alright, sweetie."
        show anon f_shy
        debbie "Just don't put it off for too long..."
        debbie "... [saga.cast.diane] is practically family, ya know?"
        anon f_calm "Yeah, I know."
    else:

        anon "Yeah, I went by to see her after school."
        debbie "And how was it?"
        anon a_uneasy "Umm, it was okay."
        anon "I wasn't expecting her garden to be so full and lush."
        show anon a_side
        debbie @ e_b f_happy m_laugh "Hehe, I can imagine."
        anon f_tired "It's gonna take a lot of work to maintain."

        if saga.cast.diane < 'garden':
            debbie "Have you eaten?"
        else:

            anon "I'm pretty exhausted, to be honest."
            debbie "Oh, you poor thing!"

    debbie "Let me fix you something to eat."
    anon "No, that's okay."
    debbie "You sure?"
    anon "Yeah, I think I'm just going to head straight to bed."
    debbie "Oh, alright."
    debbie "Sweet dreams, sweetie."
    anon @ a_wave "Good night, [saga.cast.debbie]."
    hide anon with dissolve

    if saga.cast.debbie in saga.sets.debbie_kitchen:
        scene debbie_lobby at stage with fade
    else:

        scene debbie_hall at stage with fade
        show anon o_right

    show anon a_pocket f_worried
    with dissolve
    anon @ -m_talk "( Hmm, [saga.cast.debbie] said there's nothing to worry about, but what if she's just putting on a brave face? )"
    anon a_think e_nw f_pensive @ -m_talk "( And who could that have been on the other end of the call? )"
    anon @ -m_talk "( I've got a bad feeling about this. )"
    hide anon
    with dissolve
    return


label deb01_debbie.rails:
    jump deb01_catch.rails


label deb01_kitchen:
    return


label deb01_kitchen.rails:
    jump deb01_debbie.rails


label deb01_lounge:
    return


label deb01_lounge.rails:
    jump deb01_debbie.rails
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
