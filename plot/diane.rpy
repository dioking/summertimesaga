label diane_diane_yard:
    jump diane_diane_yard.intro

    menu diane_diane_yard.choice:
        "Shovel." if saga.event.peek(choice='shovel', who=saga.cast.diane):
            return saga.event.emit(choice='shovel', who=saga.cast.diane)

        "Compost." if saga.event.peek(choice='compost', who=saga.cast.diane):
            return saga.event.emit(choice='compost', who=saga.cast.diane)

        "Wages. ($[saga.prop.diane_plot.owed])"(saga.prop.diane_plot.owed) if saga.event.peek(choice='cash', who=saga.cast.diane):
            return saga.event.emit(choice='cash', who=saga.cast.diane)
        "Bye.":

            pass

    jump diane_diane_yard.outro


label diane_diane_yard.intro:
    jump diane_diane_yard.intro1


label diane_diane_yard.intro1:
    scene diane_yard -diane at stage
    show diane a_shovel_hip at right
    show anon a_pocket o_right at left with dissolve
    diane "Hey there, [saga.cast.anon]!"
    diane "I'm so glad you decided to come and help me."
    anon "Yeah, it's no problem [saga.cast.diane]."
    jump diane_diane_yard.choice


label diane_diane_yard.outro:
    jump diane_diane_yard.outro1


label diane_diane_yard.outro1:
    show diane f_calm

    if saga.prop.diane_plot.last < saga.time.date:
        anon f_calm "I should probably get started on the garden."
    else:
        anon f_calm "I should probably get going."

    diane "Alright."
    diane "Thanks again for helping!"
    anon "No problem."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
