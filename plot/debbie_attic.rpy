label debbie_attic:
    scene mono debbie_attic_door
    mono "Using the stool, I was able to get into the attic.\nI had never been up there before." with fade
    mono "I was filled with excitement wondering what treasures [saga.cast.debbie] and Dad had stashed away."

    scene black
    with dissolve
    return


label debbie_attic.item:
    scene debbie_landing at stage
    show old_anon 34 with dissolve
    anon "Hmm..."
    show old_anon 35
    anon "( I need something to stand on to reach the opening... )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
