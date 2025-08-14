label deb_island(busy):
    anon f_horny "Feeling a little naughty?"

    if busy:
        jump deb_island.busy

    debbie f_curious "What, now?!"
    anon f_horny_smug @ -m_talk "Mhmm."
    debbie f_sad "Sweetie, we can't do that..."
    debbie "... What if [saga.cast.jenny] comes down?"
    anon f_horny "Oh, don't worry."
    show debbie f_curious

    if saga.cast.jenny in saga.zone.debbie_inside:
        anon "She's on the phone with [saga.cast.jane]..."
        anon "... You know how those two are."
        anon "She'll be busy for hours."
    else:

        anon "She's out at the moment."

    debbie f_horny "Ngh, okay..."
    show anon e_sw
    show debbie a_pancake o_right p_stand_away at pos(.9)
    pause
    show anon e_w
    show debbie a_open_01 o_left p_stand at right
    debbie "... But we have to be quick!"
    show debbie a_open_03 c_robe_open e_s
    anon a_pants_off_01 e_s f_shy "You got it."
    show anon c_casual_top p_pants_off_02
    show debbie a_open_04 c_pants e_sw
    pause

    scene debbie_kitchen_counter_missionary
    show debbie b_anon c_robe_open p_kitchen_island_pickup
    with fade
    debbie "Whoa, sweetie!"
    debbie "You're being so..."
    show anon c_casual_top e_sse f_nervous p_kitchen_island_insert
    show mimic debbie at pos.debbie
    debbie a_leg e_s p_kitchen_island z_b_ob_f_of -b_anon "... so..."
    hide anon
    hide mimic
    debbie b_anon p_kitchen_island_anim s_10 z_reset "... Oh, goodness!!"
    pause
    call deb_island.dialogue (1)
    call deb_island.dialogue (2)
    call deb_island.dialogue (3)
    call deb_island.dialogue (4)
    call deb_island.dialogue (5)
    call deb_island.dialogue (6)
    jump deb_island.loop


label deb_island.busy:
    debbie f_sad "Ahh, sweetie... You know I'd love nothing more but I'm kinda overwhelmed at the moment."
    anon f_confused "Oh?"
    debbie "Let's hold off for another time, yeah?"
    anon f_calm "Yeah, okay."
    hide anon with dissolve
    return


label deb_island.dialogue(opt, rng=-1):
    if opt == 1:
        debbie "Oh, sweetie!"
        debbie "Yes!!"

    elif opt == 2:
        debbie "You're such a good boy!"
        debbie "Good... and {i}big{/i}!!"

        if rng < .5:
            debbie "So- Ahh!!"
            debbie "So {i}BIG{/i}!!"

    elif opt == 3:
        if rng < .5:
            anon "Mmm, [saga.cast.debbie]."

        debbie "I can't believe we're doing this on the kitchen counter..."
        debbie "... It's so naughty!"

    elif opt == 4:
        anon "You like that, [saga.cast.debbie]?"
        debbie "Ngh, yes!"

        if rng < .5:
            debbie "You make me feel so good, sweetie!"
            debbie "Ahh!!"

    elif opt == 5:
        anon "You're squeezing me so tight!"

        if rng < .5:
            debbie "Give it to me, sweetie!"
            debbie "Oh!!!"

    elif opt == 6:
        anon "I love you, [saga.cast.debbie]."
        debbie "Oh, I love you too!"

        if rng < .5:
            debbie "So much, sweetie!"

    pause
    return


label deb_island.inside:
    anon "Ahh, [saga.cast.debbie]!"
    anon "I'm getting close!"
    debbie "Cum for me, sweetie!"
    debbie "Cum for me!"
    pause
    anon "[saga.cast.debbie], I'm gonna-"
    anon "Oh!!"
    show debbie p_kitchen_island_cum s_400ms
    anon "HNNGGG!!!" with flash
    debbie "NGGHHH!!!"
    pause
    show debbie p_kitchen_island z_b_ob_f_of -b_anon
    show anon c_casual_top e_b m_kiss od_wet p_kitchen_island_after
    show mimic debbie at pos.debbie
    anon @ f_elated "Haah... Haah..."
    debbie "Oh, I can feel it..."
    show anon e_sse f_nervous -m_kiss
    debbie "... There's so much!!"
    anon e_e "Y-yeah."
    debbie e_b f_happy m_laugh @ -m_talk "Hehehe!"
    pause

    call shot.debbie_kitchen_island
    show debbie a_shy c_robe_open e_s f_horny at right
    show anon a_rub c_casual_top d_soft e_sw f_shy o_right od_wet
    with fade
    anon "Man, I'm feeling kinda dizzy..."
    debbie e_w "Yeah, you were really worked up there."
    anon e_w f_horny "You do that to me, [saga.cast.debbie]."
    debbie a_embarrassed f_calm "Heh, you're such a sweet boy."
    show anon a_side
    pause
    jump deb_island.post


label deb_island.loop:
    menu(range=(8, 20, 3), screen='lewd', tag='debbie'):
        "Keep going":
            pass
        "Cum Inside":

            jump deb_island.inside
        "Cum Outside":

            jump deb_island.outside

    $ renpy.dynamic(pool=saga.lewd.pool(6, max=2))

    while pool:
        call deb_island.dialogue (pool.pop(), rng=renpy.random.random()) from deb_island.pool

    jump deb_island.loop


label deb_island.outside:
    anon "[saga.cast.debbie]!"
    anon "I'm almost... there!"
    debbie "Do it, sweetie!"
    debbie "I'm ready!"
    pause
    anon "Oh, [saga.cast.debbie]!!"
    show debbie e_b f_distressed m_talk p_kitchen_island z_b_ob_f_of -b_anon
    show anon c_casual_top e_b m_kiss od_cumshot p_kitchen_island_after
    show mimic debbie at pos.debbie
    anon @ f_distressed "HNNGGG!!!" with flash
    debbie "NGGHHH!!!"
    show debbie e_s f_calm -m_talk
    anon "Haah... Haah..."
    show anon e_se f_nervous -m_kiss
    pause
    show anon e_e
    debbie f_surprised "Oh, goodness..."
    debbie "... So much!!"
    anon "H-heh."
    debbie e_b f_happy m_laugh @ -m_talk "Hehehe!"
    pause

    call shot.debbie_kitchen_island
    show debbie a_embarrassed c_robe_open e_s f_horny ob_cum_island at right
    show anon c_casual_top d_soft e_sw f_shy o_right
    with fade
    pause
    debbie "Wow, you really made a mess!"
    anon a_uneasy e_w "Sorry, [saga.cast.debbie]."
    debbie a_side e_w f_shy "N-no, that's okay!"
    debbie f_calm "I just need to go clean up a bit and then I'll get back to fixing dinner."
    show anon a_side
    jump deb_island.post


label deb_island.post:
    debbie a_nervous "Why don't you go rest for a bit and I'll let you know when dinner is done."
    anon f_shy "Y-yeah, okay."
    show anon d_none p_pants_off_02
    show debbie a_shy e_sw
    pause
    show anon a_pants_off_01 c_casual e_s od_none p_stand
    show debbie e_w
    pause
    hide anon
    show debbie b_anon e_b p_hug
    anon "Thanks, [saga.cast.debbie]!"
    debbie "You're welcome, sweetie."

    if 'ob_cum_island' in renpy.get_attributes('debbie'):
        debbie e_s "Now, mind your top, someone made a bit of a mess."
        anon "Guilty as charged!"
        debbie e_b @ f_happy m_laugh "Hehe!"

    show debbie p_kiss
    pause
    debbie "{i}*Muah*{/i}"
    show anon f_shy o_right
    show debbie a_side e_w p_stand -b_anon
    anon "I love you, [saga.cast.debbie]."
    debbie f_happy "I love you too..."
    hide anon with dissolve.nowait

    if 'ob_cum_island' in renpy.get_attributes('debbie'):
        show debbie a_open_03 e_s z_b_f_of_a_oa_ob

    debbie f_horny "... My big strong man!"
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
