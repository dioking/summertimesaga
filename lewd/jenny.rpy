label jenny_menu:
    return


label jenny_menu.shower_peek:
    python hide:
        saga.sets.debbie_bath.add('busy', 'wash')

    jump jen01_bath


label jenny_menu.laptop_porn:
    python hide:
        saga.time.now = saga.time.dark

    jump jen04_bed2


label jenny_menu.peephole_play:
    python hide:
        saga.time.now = saga.time.dusk

    scene debbie_attic at stage(.84, .85, 5)

    menu:
        "\"Daddy\"." if 'daddy' in opts:
            call debbie_rug.play

        "\"[saga.cast.anon]\"." if 'anon' in opts:
            call debbie_rug.play ('anon')

    return


label jenny_menu.bathroom_leak:
    python hide:
        saga.sets.debbie_bath.add('pipe', 'leak')

    call deb04_landing.cookie

    if 'strip' not in opts:
        return

    scene black
    with dissolve
    mono ""

    python hide:
        saga.sets.debbie_bath.remove('leak')

    $ renpy.transition(dissolve)
    jump deb04_bath


label jenny_menu.bedroom_photo:
    jump jen05_jenny.cookie


label jenny_menu.bedroom_grope:
    python hide:
        saga.cast.anon.cash = 200

    scene debbie_bed2 at stage(z=4)
    call jenny_menu._dom_sub

    $ renpy.transition(fade)
    jump jen07_bed2


label jenny_menu.bedroom_roxxy:
    scene debbie_landing at stage(.4, .5, 2)

    menu:
        "[saga.cast.jenny] has {i}not{/i} seen [saga.cast.anon]'s dick." if 'jenny-' in opts:
            pass

        "[saga.cast.jenny] has seen [saga.cast.anon]'s dick." if 'jenny+' in opts:
            $ saga.cast.jenny.put('seen')

    jump viv04_bed2


label jenny_menu.bedroom_strip:
    scene debbie_bed2 at stage(z=4)
    call jenny_menu._dom_sub

    scene debbie_bed2 -jenny at stage
    show jenny a_fold at right
    show anon a_pocket o_right at left

    $ renpy.transition(fade)
    jump jen08_jenny


label jenny_menu.camslut_electro:
    python hide:
        saga.prop.jenny_laptop.auto = True
        saga.prop.jenny_laptop.env = saga.prop.anon_pc
        saga.prop.jenny_laptop.ram = {'camslut': {'mode': True, 'st': 0}, 'vid1': {'st': 0}}
        saga.prop.jenny_laptop.videos = ['vid1', 'vid2']

    scene jenny_laptop
    jump jenny_laptop.vid1


label jenny_menu.camslut_vibe:
    python hide:
        saga.prop.jenny_laptop.auto = True
        saga.prop.jenny_laptop.env = saga.prop.anon_pc
        saga.prop.jenny_laptop.ram = {'camslut': {'mode': True, 'st': 0}, 'vid2': {'st': 0}}
        saga.prop.jenny_laptop.videos = ['vid1', 'vid2']

    scene jenny_laptop
    jump jenny_laptop.vid2


label jenny_menu.camslut_monster:
    python hide:
        saga.prop.jenny_laptop.auto = True
        saga.prop.jenny_laptop.env = saga.prop.anon_pc
        saga.prop.jenny_laptop.ram = {'camslut': {'mode': True, 'st': 0}, 'vid3': {'st': 0}}
        saga.prop.jenny_laptop.videos = ['vid1', 'vid2', 'vid3']

    scene jenny_laptop
    jump jenny_laptop.vid3


label jenny_menu.bedroom_suck:
    scene debbie_bed2 at stage(z=4)
    call jenny_menu._dom_sub

    $ renpy.transition(fade)
    jump jen14_dining.cookie


label jenny_menu.laptop_cam:
    python hide:
        saga.prop.jenny_laptop.add('open')
        saga.sets.debbie_bed2.add('busy')
        saga.time.now = saga.time.dark

    jump jen15_bed2


label jenny_menu.cam_handjob:
    jump jen18_jenny.cookie


label jenny_menu.couch_footjob:
    python hide:
        saga.time.now = saga.time.dark

    scene debbie_lounge at stage
    call jenny_menu._dom_sub

    menu:
        "[saga.cast.anon] catches [saga.cast.jenny]." if 'jenny' in opts:
            $ renpy.transition(fade)
            jump jen20_jenny

        "[saga.cast.jenny] catches [saga.cast.anon]." if 'anon' in opts:
            pass

    python hide:
        if 'sex' in opts:
            saga.cast.jenny.put('visit')

        renpy.transition(fade)

    scene debbie_tv
    show tv lesbian onlayer aux
    call debbie_tv.cookie
    jump debbie_tv.jenny


label jenny_menu.cam_blowjob:
    scene debbie_bed2 at stage(.72, .6, 5)
    call jenny_menu._dom_sub

    $ renpy.transition(fade)
    jump jen21_jenny.cookie


label jenny_menu.scope_lickjob:
    scene debbie_bed3 at stage(.72, .6, 5)
    call jenny_menu._dom_sub

    scene debbie_bed3_telescope_floor
    show anon d_hard f_worried o_right p_sit_back at pos.scope_back
    show jenny a_rub c_casual_pants e_w p_spy_lean_away s_4
    with fade
    jump jen23_scope.cookie


label jenny_menu.shower_blowjob:
    python hide:
        saga.sets.debbie_bath.add('busy', 'wash')
        seed = renpy.random.random()
        seed -= int(seed * 8 % 2) / 8
        renpy.dynamic(seed=seed)

    scene debbie_landing at stage(.575, .4, 2)
    call jenny_menu._dom_sub

    $ renpy.transition(fade)
    call jen_shower.peek3 (seed, test=True)
    return


label jenny_menu.cam_sex:
    python hide:
        saga.cast.anon.str = 10 if 'str' in opts else 0

    scene debbie_bed2 at stage(.72, .6, 5)
    call jenny_menu._dom_sub

    $ renpy.transition(fade)
    jump jen24_jenny.cookie


label jenny_menu.cinema_date:
    jump jen26_cinema.cookie


label jenny_menu.visit_sex:
    python hide:
        saga.cast.anon.where = saga.sets.debbie_bed3
        saga.sets.debbie_bed3.add('sleep')
        saga.time.now = saga.time.dark

    scene debbie_bed3 at stage(.72, .6, 5)
    call jenny_menu._dom_sub

    menu:
        "[saga.cast.jenny] is not pregnant.":
            pass

        "[saga.cast.jenny] is in her second trimester." if 'bump' in opts:
            $ saga.cast.jenny.womb.state += 2

        "[saga.cast.jenny] is in her third trimester." if 'belly' in opts:
            $ saga.cast.jenny.womb.state += 3

    $ renpy.transition(fade)
    jump jen26_outro


label jenny_menu.shower_sex:
    python hide:
        saga.cast.jenny.put('visit')
        saga.sets.debbie_bath.add('busy', 'wash')
        renpy.dynamic(seed=renpy.random.random())

    scene debbie_landing at stage(.575, .4, 2)
    call jenny_menu._dom_sub

    $ renpy.transition(fade)
    call jen_shower (seed)
    return


label jenny_menu.table_sex:
    scene debbie_dining at stage(.475, .5, 2)
    call jenny_menu._dom_sub

    call shot.debbie_dining_jenny
    show anon a_down e_e f_calm p_table behind jenny
    with fade
    jump jen_table


label jenny_menu.pool_sex:
    scene debbie_yard at stage(.4, .675, 3.5)
    call jenny_menu._dom_sub

    jump jen_pool.cookie


label jenny_menu.sleep_sex:
    python hide:
        saga.cast.anon.where = saga.sets.debbie_bed2
        saga.cast.jenny.add('sleep')
        saga.cast.jenny.put('visit')
        saga.cast.jenny.where = saga.sets.debbie_bed2
        saga.time.now = saga.time.dark

    scene debbie_bed2 at stage(.7, .6, 3)
    call jenny_menu._dom_sub
    jump jen_sleep


label jenny_menu.gfe_sex:
    python hide:
        saga.cast.jenny.sub = 1
        saga.cast.jenny.where = saga.sets.debbie_bed3
        saga.time.now = saga.time.dark

    scene debbie_bed3 at stage(.56, .5, 2, b=20)
    call jenny_menu._dom_sub
    jump jen_gfe_jenny


label jenny_menu.cam_belly:
    python hide:
        saga.cast.jenny.womb.state += 3

    jump jen_baby_food.cookie


label jenny_menu._dom_sub:
    menu:
        "[saga.cast.anon] is {color=7ff7}submissive{/color}." if 'dom' in opts:
            $ saga.cast.jenny.dom += 1

        "[saga.cast.anon] is {color=f77b}dominant{/color}." if 'sub' in opts:
            $ saga.cast.jenny.sub += 1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
