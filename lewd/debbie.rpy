label debbie_menu:
    return


label debbie_menu.shower_peek:
    python hide:
        saga.sets.debbie_bath.add('busy', 'wash')
        renpy.dynamic(seed=renpy.random.random() * .5)

    call shot.debbie_bath_door

    menu:
        "Washing." if 'wash' in opts:
            call deb_shower.peek1 (seed + .5)

        "Drying." if 'dry' in opts:
            call deb_shower.peek2 (seed)

        "Playing." if 'play' in opts:
            call deb_shower.peek3 (seed + .5)

    return


label debbie_menu.kitchen_gawk:
    call shot.debbie_kitchen_stool
    show debbie a_pen e_s f_sad o_right oa_hand p_table_lean_in z_b_ob_f_of_a behind island at pos.kitchen_stool
    show mimic debbie at pos.debbie
    show anon a_tired e_sw f_confused o_right p_bend behind island at pos(.425)
    with fade
    jump deb02_debbie.cookie


label debbie_menu.laundry_strip:
    jump deb03_outro.cookie


label debbie_menu.lotion_rub:
    scene mono debbie_lobby_stairs vacuum
    mono "After spending several days helping [saga.cast.debbie] around the house, I began to get the feeling that no one had ever really taken the time help her much before." with fade



    scene mono debbie_dishes
    mono "She was very appreciative of the assistance and chatting to her while working was surprisingly fun. I'm so lucky to be living with her." with fade



    scene mono debbie_utility_laundry2
    mono "One day, while helping her with the laundry, she asked me to carry a basket of clean clothes up to her bedroom..." with fade

    mono "... And, well... one thing lead to another..."

    $ renpy.transition(fade)
    jump deb05_debbie


label debbie_menu.movie_tease:
    jump deb07_movie.cookie


label debbie_menu.shop_kiss:
    jump deb08_stall1.cookie


label debbie_menu.dream_handjob:
    jump deb09_dream


label debbie_menu.bedroom_play:
    jump deb10_bed1


label debbie_menu.dream_blowjob:
    jump deb11_dream


label debbie_menu.kitchen_kiss:
    python hide:
        saga.cast.anon.chr = 5
        renpy.dynamic(busy=False)

    call shot.debbie_kitchen_island
    show debbie a_mug f_sad at right
    show anon a_rub e_w f_shy o_right at left
    jump deb12_debbie.cookie


label debbie_menu.car_kiss:
    scene debbie_car_inside garage invoice
    show anon a_side_knee p_car_turn
    show debbie p_car_turn
    show debbie_car_inside wheel as wheel
    with fade
    jump deb13_outro.cookie


label debbie_menu.bedroom_pants:
    call deb14_pants (busy=False)
    return


label debbie_menu.shower_sneak:
    python hide:
        saga.sets.debbie_bath.add('busy', 'wash')

    jump deb15_bath


label debbie_menu.couch_play:
    python hide:
        saga.time.now = saga.time.dark

    jump deb16_tv.cookie


label debbie_menu.visit_handjob:
    python hide:
        saga.time.now = saga.time.dark

    jump deb17_visit.cookie


label debbie_menu.shower_handjob:
    python hide:
        saga.sets.debbie_bath.add('busy', 'wash')

    jump deb18_lobby.cookie


label debbie_menu.sleep_suck:
    python hide:
        saga.time.now = saga.time.dark

    jump deb19_kitchen.cookie
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
