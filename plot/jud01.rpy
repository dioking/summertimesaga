label jud01_intro:
    if saga.cast.judith in saga.sets.school_hall1w:
        call shot.school_hall1w_judith
    else:
        scene school_art -judith at stage

    show judith a_clasp f_shy at right
    show anon a_pocket o_right at left with dissolve
    judith "Hey [saga.cast.anon]!"
    anon "Hey [saga.cast.judith], how's it going?"
    judith "Oh, I'm great!"
    judith f_sad @ e_ssw "I... I just wanted to thank you."
    anon @ f_confused "Oh. For what?"
    judith "In the boys' locker room... you made me feel... safe."
    show judith f_shy
    anon a_uneasy f_shy "Oh..."
    judith "And, you know... you stood up to [saga.cast.annie]. I think that was very brave."
    anon a_side "It's fine, [saga.cast.judith]. I was just trying to do the right thing."
    anon f_worried "I should be the sorry one... for showing you my..."
    anon @ e_s "... You know..."
    show anon f_surprised
    judith "Oh that's fine!! I enjoyed-"
    judith f_sad "I mean... I didn't mind, at all."
    show anon f_calm
    judith f_shy "We just got to... know each other a little better!"
    anon @ e_b f_happy m_laugh "Haha!"
    anon "Yeah. I suppose so..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
