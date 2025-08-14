label debbie_debbie_bed1:
    return


label debbie_debbie_bed1.sleep:
    scene debbie_bed1 at stage
    show anon a_pocket e_sw f_surprised o_right with dissolve
    anon @ -m_talk "( Should I sneak into her bed? )"
    anon e_nw f_pensive @ -m_talk "..."
    anon e_sw @ -m_talk "( Nah, I shouldn't bother her when she's sleeping. )"
    hide anon with dissolve
    return


label debbie_debbie_kitchen:
    jump debbie_debbie_kitchen.intro

    menu debbie_debbie_kitchen.choice:
        "Chores." if saga.event.peek(choice='chores', who=saga.cast.debbie):
            return saga.event.emit(choice='chores', who=saga.cast.debbie)

        "Lotion." if saga.event.peek(choice='lotion', who=saga.cast.debbie):
            return saga.event.emit(choice='lotion', who=saga.cast.debbie)

        "Shop." if saga.event.peek(choice='shop', who=saga.cast.debbie):
            return saga.event.emit(choice='shop', who=saga.cast.debbie)

        "Dreams." if saga.event.peek(choice='dreams', who=saga.cast.debbie):
            return saga.event.emit(choice='dreams', who=saga.cast.debbie)

        "Kissing." if saga.event.peek(choice='kiss', who=saga.cast.debbie):
            return saga.event.emit(choice='kiss', who=saga.cast.debbie)

        "Visit." if saga.event.peek(choice='bed3', who=saga.cast.debbie):
            return saga.event.emit(choice='bed3', who=saga.cast.debbie)

        "Movie." if saga.event.peek(choice='movie', who=saga.cast.debbie):
            return saga.event.emit(choice='movie', who=saga.cast.debbie)

        "Fool around." if saga.event.peek(choice='garage', who=saga.cast.debbie) and saga.time.tod < saga.time.dusk:
            return saga.event.emit(choice='garage', who=saga.cast.debbie)

        "Fool around." if saga.event.peek(choice='island', who=saga.cast.debbie) and saga.time.dusk:
            return saga.event.emit(choice='island', who=saga.cast.debbie)
        "Never mind.":

            pass

    jump debbie_debbie_kitchen.outro


label debbie_debbie_kitchen.intro:
    if saga.cast.debbie < 'sex':
        jump debbie_debbie_kitchen.intro1

    jump debbie_debbie_kitchen.intro2


label debbie_debbie_kitchen.intro1:
    call shot.debbie_kitchen_island
    show debbie a_mug at right
    show anon a_pocket o_right at left with dissolve
    debbie "Hi, sweetie!"
    debbie "Is everything okay at school?"
    anon "Yeah..."
    debbie f_shy "I hope you didn't fall too far behind, what with all that's happened?"
    anon "Nah, I'll catch up."
    debbie @ f_sad "Just let me know if there is ever anything I can do to help?"
    anon f_shy "Okay, [saga.cast.debbie]..."
    jump debbie_debbie_kitchen.choice


label debbie_debbie_kitchen.intro2:
    call shot.debbie_kitchen_island
    show debbie a_mug at right
    show anon a_pocket o_right at left with dissolve

    $ renpy.dynamic(rn=renpy.random.random())

    if rn < .1:
        debbie "There's my big man..."

    elif rn < .2:
        debbie "Hey there, sweetie."
        debbie "What can I do for you?"

    elif rn < .3:
        debbie "Awww..."
        debbie "No hello squeeze?"

    elif rn < .7:
        debbie "Looking for me, I hope."

    elif rn < .8:
        debbie "Need something, sweetie?"
        debbie "Or can I do something for you?"

    elif saga.cast.jenny in saga.sets.debbie_bath:
        debbie "[saga.cast.jenny] is in the shower."
        debbie "In case you needed me for a quick sec."
    else:

        debbie "I was hoping I'd see you today."

    if renpy.random.random() < .5:
        anon "Hello, [saga.cast.debbie]."
    else:
        anon "You're looking good today."

    show anon f_shy
    jump debbie_debbie_kitchen.choice


label debbie_debbie_kitchen.outro:
    anon f_shy "I should go."
    debbie f_happy "Don't stay out too late!"
    hide anon with dissolve
    return


label debbie_debbie_utility:
    jump debbie_debbie_utility.intro

    menu debbie_debbie_utility.choice:
        "Chores." if saga.event.peek(choice='chores', who=saga.cast.debbie):
            return saga.event.emit(choice='chores', who=saga.cast.debbie)

        "Lotion." if saga.event.peek(choice='lotion', who=saga.cast.debbie):
            return saga.event.emit(choice='lotion', who=saga.cast.debbie)

        "Shop." if saga.event.peek(choice='shop', who=saga.cast.debbie):
            return saga.event.emit(choice='shop', who=saga.cast.debbie)

        "Dreams." if saga.event.peek(choice='dreams', who=saga.cast.debbie):
            return saga.event.emit(choice='dreams', who=saga.cast.debbie)

        "Kissing." if saga.event.peek(choice='kiss', who=saga.cast.debbie):
            return saga.event.emit(choice='kiss', who=saga.cast.debbie)

        "Visit." if saga.event.peek(choice='bed3', who=saga.cast.debbie):
            return saga.event.emit(choice='bed3', who=saga.cast.debbie)

        "Movie." if saga.event.peek(choice='movie', who=saga.cast.debbie):
            return saga.event.emit(choice='movie', who=saga.cast.debbie)

        "Fool around." if saga.event.peek(choice='laundry', who=saga.cast.debbie):
            return saga.event.emit(choice='laundry', who=saga.cast.debbie)
        "I should go.":

            pass

    jump debbie_debbie_utility.outro


label debbie_debbie_utility.intro:
    call shot.debbie_utility_laundry
    show debbie a_mug at right
    show anon a_pocket o_right at left with dissolve
    anon "Hey, [saga.cast.debbie]."
    debbie "Hey, sweetie."
    debbie f_curious "What are you doing down here?"
    jump debbie_debbie_utility.choice


label debbie_debbie_utility.outro:
    anon f_confused "Can I help you with anything before I go?"
    debbie f_shy "Oh, no... I've got this."
    show anon f_calm
    debbie f_calm "You get out there and enjoy the day!"
    anon "Thanks, [saga.cast.debbie]."
    hide anon with dissolve
    return


label debbie_debbie_yard:
    jump debbie_debbie_yard.intro


label debbie_debbie_yard.intro:
    jump debbie_debbie_yard.intro1


label debbie_debbie_yard.intro1:
    scene debbie_yard_pool_edge
    show debbie a_down e_sw f_sad ob_pool_water p_sit_edge_bend at right
    pause
    show anon o_right p_stand_legs at pos(.45, .95) with dissolve.nowait
    anon "[saga.cast.debbie]?"

    if saga.cast.debbie.last == saga.time.now:
        jump debbie_debbie_yard.intro1b

    debbie e_nw @ -m_talk "Hmm?"
    show debbie e_w
    show anon f_worried ob_sandal p_kneel at pos(.35, .975)
    with dissolve.nowait
    anon "You look sad..."
    anon f_confused "... Everything alright?"
    show anon f_shy
    debbie f_shy "Oh, I'm okay, sweetheart."
    debbie "I just needed to get some air."
    anon f_confused "Thinking about Dad?"
    show anon f_worried
    debbie e_sw f_sad "Y-yeah, maybe a bit."
    pause
    debbie "We had so many plans for the future, you know..."
    debbie "... And now it's all just-"
    anon "Gone?"
    debbie "Yeah."
    show anon e_ssw
    debbie "It makes me feel so lost."
    pause
    debbie e_w "What am I supposed to do now?"
    anon "I-"
    pause
    show debbie e_sw
    anon "I don't know."
    anon e_w "... Wish like hell I did."
    hide anon
    show debbie a_anon_hug e_w f_surprised p_sit_edge_back
    with dissolve.nowait
    anon "But I'm certain you'll figure it out."
    show debbie f_shy
    anon "And I'll be here for you every step of the way as you work through it."
    debbie e_b "Aww, sweetie..."
    debbie "... That was such a wonderful thing to say."
    show debbie f_sad
    pause
    show debbie f_crying
    pause
    show anon f_shy o_right ob_sandal p_kneel at pos(.35, .975) with dissolve.nowait
    debbie a_wipe_tears "{i}*Sniff*{/i}"
    debbie a_down e_w f_shy "Heh, look at me... I'm a mess."
    anon "Nah, you're just grieving."
    pause
    anon "We all are."
    debbie "Why don't you head inside and give me a moment to compose myself."
    debbie "I'll be along shortly and get dinner started."
    anon f_calm "Alright."
    show debbie e_wnw
    show anon p_stand_legs at pos(.45, .95)
    with dissolve.nowait
    anon "See ya in a bit."
    hide anon with dissolve.nowait
    debbie "Love ya, sweetie."
    pause
    show debbie a_rub_leg e_sw f_calm p_sit_edge_bend
    pause
    debbie "Such a wonderful boy."
    pause
    return


label debbie_debbie_yard.intro1b:
    debbie e_nw f_shy "I just need a moment, sweetie."
    debbie "You head on inside."
    anon "Alright."
    show debbie e_sw
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
