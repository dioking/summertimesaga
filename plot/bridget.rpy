label bridget_school_office6:
    jump bridget_school_office6.intro

    menu bridget_school_office6.choice:
        "Nothing.":
            pass

    jump bridget_school_office6.outro


label bridget_school_office6.intro:
    scene school_office6 -bridget at stage
    show bridget a_fold f_angry o_right at left
    show anon a_pocket f_worried at right with dissolve
    bridget "[saga.cast.anon]!"
    bridget "What are you doing in here?"
    anon f_surprised "Sorry, ma'am!!!"
    anon "I just had some questions!"
    bridget "Questions?!"
    bridget "Like what?"
    jump bridget_school_office6.choice


label bridget_school_office6.outro:
    show bridget f_calm
    anon f_worried "I... I forgot."
    bridget f_angry "Forgot? Boy you are the saddest piece of meat I've ever seen!"
    show anon f_surprised m_teeth
    bridget @ e_b m_yell "Now get out of here and get to WORK!!"
    anon a_salute f_worried_surprised -m_teeth "Yes, ma'am!!!"
    return


label bridget_school_track:
    jump bridget_school_track.intro

    menu bridget_school_track.choice:
        "Training.":
            jump bridget_school_track.train
        "Nothing.":

            pass

    jump bridget_school_track.outro


label bridget_school_track.intro:
    scene school_track -bridget at stage
    show bridget a_fold f_angry at right
    show anon a_pocket f_worried o_right at left with dissolve
    bridget "[saga.cast.anon]!"
    bridget "You better be training your ass off at the gym, or I'm going to shove my foot up your ass!!"
    anon f_shocked m_open @ -m_talk "Yes, ma'am!!!"
    show anon f_surprised -m_open
    bridget "Got any questions?!"
    jump bridget_school_track.choice


label bridget_school_track.outro:
    jump bridget_school_office6.outro


label bridget_school_track.train:
    show bridget f_calm
    anon f_worried "I... well, where should I train?"
    bridget f_angry @ -m_talk "..."
    show anon f_surprised
    bridget "I just told you!"
    bridget @ e_b m_yell "At the GYM!!!"
    anon f_worried "But... what should I train?"
    bridget "You have to work on your strength and dexterity if you want to make it!"
    bridget "You'll be competing in the 110-meter hurdles to qualify this school and your team into the state championship!"
    anon "That's... a lot of pressure."
    show anon f_surprised m_teeth
    bridget "... And you better NOT fail me!"
    anon a_salute -m_teeth "Yes, ma'am!!!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
