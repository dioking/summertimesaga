label bar_office:
    anon f_shy "Yeah, I'd love that!"
    barb "Mmm, hurry and lock the door!"
    anon "O-okay..."
    hide anon with dissolve
    jump bar06_office3.reuse


label bar_office.area:
    anon a_point_pocket f_horny "You feel like doing some of our special art together?"
    barb f_horny "Oh, you naughty, {i}naughty{/i} boy!"
    show anon a_pocket
    pause
    barb f_sad "I'm afraid it'll have to wait until after class."
    anon a_side f_worried "Aww."
    pause
    anon e_osw f_sad "Yeah, okay."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
