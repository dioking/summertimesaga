label deb11_dream:
    scene dream_clowns -balloon onlayer aux
    show anon a_spoon p_dream_clowns onlayer aux

    scene aux:
        shader ('saga.equirectangular', '-renpy.geometry', '-renpy.texture')
        mesh True subpixel True u_pitch .12 u_yaw -.25 u_zoom 2.5
        align (.5, 1.) xysize (6000, 3000)
    show layer master at Transform(align=(.5, 1.), zoom=.36)
    with fade
    jenny "... The sales clerk was really trying to push this innocuous purple dress on me but I was all:"
    show anon a_spoon_eat
    jenny "{i}Bitch, I am not wearing that to a job interview!{/i}"
    show anon a_spoon
    jenny "The green one was only two hundred dollars more {i}and{/i} it's the color of money so I'm gonna look fab as fuck!"
    show jenny c_casual_pants e_c f_snide p_dream_clowns w_normal onlayer aux
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .075 u_yaw -.05 u_zoom 2.
    pause 1
    anon "Whoa, whoa, whoa... You got my dad to spend two hundred dollars on a new dress for a stupid job interview?!"
    jenny f_smug "Wow, jealous much?"
    "{i}*Sluuuurrrrpppp*{/i}"
    anon "That's probably worth more than my entire wardrobe put together!"
    jenny f_happy "Hah, I know!"
    jenny f_snide "What do you have, like one outfit?"
    anon "I don't understand why you even need a new dress... it's a job working the cash register at the grocery store."
    "{i}*Gllccck*{w=.5} *Gllccck*{w=.5} *Gllccck*{/i}"
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .05 u_yaw -.125
    show jenny f_confused
    anon "Did you hear something?"
    jenny "No?"
    pause
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .075 u_yaw -.05
    jenny f_smug "You're just mad because your dad likes to spoil me."
    anon "Gee, you think?!"
    "{i}*Sluuuurrrrpppp*{/i}"
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .125 u_yaw .05
    show jenny f_confused
    anon "Seriously, what is that sound?!"
    jenny "What sound?"
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .075 u_yaw -.05
    anon "There's something going on under the-"
    anon "... Under the-"
    show dream_clowns -table
    show debbie c_robe p_dream_clowns_bj s_1 w_normal behind jenny onlayer aux
    show dream_clowns table as table behind jenny onlayer aux
    show anon a_down
    with none.aux
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .275 u_yaw -.25 u_zoom 2.5
    pause 1
    debbie "Mmm." with hpunch
    anon "O-oh, wow."
    debbie a_dick_hold e_c p_dream_clowns "It's okay, sweetie."
    pause
    debbie "You just enjoy your breakfast and let me take care of this, okay?"
    show debbie p_dream_clowns_bj
    anon "Is this-"
    show debbie s_800ms
    anon "{i}*Gulp*{/i} This can't be real... can it?"
    pause
    show debbie s_600ms
    anon "Oh, [saga.cast.debbie]... Ahh!"
    jenny "Umm, hello... Earth to [saga.cast.anon]?!"
    anon "Hmm?"
    show debbie s_400ms
    jenny "Are you even listening to me?"
    anon "Y-yeah, yeah... I'm listening..."
    anon "... Something about my dad loving you more or whatever-"
    show jenny c_clown f_snide v_clown
    with none.aux
    show aux:
        instant (-1.1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .075 u_yaw -.05 u_zoom 2.
        ease .1 u_zoom 1.5
    pause 1
    show dream_clowns table
    hide debbie
    hide table
    anon "Oh, holy shit!" with hpunch
    show jenny f_confused
    anon "Mother of-"
    show aux:
        instant (-.8 if renpy.suppress_transition() else 0)
        ease .8 u_zoom 2.
    jenny "What?"
    anon "W-why are you-"
    jenny f_snide "Do I have something on my face?"
    anon "Yes!!"
    jenny "Well..."
    show dream_clowns:
        matrixcolor BrightnessMatrix(-.35) * HueMatrix(200)
    show aux:
        instant (-.1 if renpy.suppress_transition() else 0)
        ease .1 u_zoom 1.5
    jenny f_scary of_nightmare p_dream_clowns_lean_in "... Get it off me!" with hpunch
    anon "I-I'm not touching that shit!"
    debbie "Mmm mmm..."
    show dream_clowns:
        matrixcolor None
    show dream_clowns -table
    show debbie a_dick_hold c_robe e_c p_dream_clowns w_normal behind jenny onlayer aux
    show dream_clowns table as table behind jenny onlayer aux
    show jenny of_none
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .1725 u_yaw -.1825
    debbie "... Such a big juicy sausage for breakfast!"
    show debbie p_dream_clowns_bj s_650ms
    pause
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .075 u_yaw -.05
    jenny f_annoyed p_dream_clowns "Okay, you're acting weird!"
    show dream_clowns table
    hide debbie
    hide table
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_zoom 2.
    anon "I'm acting weird?!"
    anon "You're a damn clown!"
    jenny @ e_r "Tch, fuck you!"
    debbie "You got some gravy in there for me, sweetie?"
    jenny e_osw f_sceptical "Wait a second, is someone under the table?"
    anon "Ehh, n-no?"
    debbie "It's okay, she can watch too."
    show dream_clowns balloon
    show aux:
        instant (-1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .085 knot .1625 u_yaw -.195 knot -.15 u_zoom 3. knot 2.25
    pause .4
    anon "Huh?!"
    debbie "Look here, sweetie."
    show dream_clowns -balloon -table
    show debbie a_balloon_hold c_clown e_c p_dream_clowns v_clown w_normal behind jenny onlayer aux
    show dream_clowns balloon table as table behind jenny onlayer aux
    show aux:
        instant (-1.1 if renpy.suppress_transition() else 0)
        ease 1. u_pitch .275 u_yaw -.25 u_zoom 2.5
        ease .1 u_zoom 3.
    pause 1.
    anon "( !!! )" with hpunch
    hide jenny
    debbie "Do you like it?"
    anon "Y-you turned my... t-t-thing into a-"
    anon "Into a-"
    debbie "It's a llama."
    show debbie e_nw
    jenny "Aww, he's adorable!"
    show debbie e_c
    anon "This is so fucked up!"
    debbie @ e_b f_happy m_laugh "Hehehe!"
    pause
    debbie p_dream_clowns_bite "{i}*Nom*{/i}"

    scene onlayer aux
    with hold.aux
    $ renpy.end_replay()

    call shot.debbie_bed3_sleep
    anon c_pants_mess p_bed3_nightmare "HNNGGG!!!" with flash
    anon a_down d_hard e_w f_shocked m_open p_bed3_sit @ -m_talk "AHHH!!!"
    anon f_afraid -m_open "Oh, god..."
    anon e_e f_worried_surprised "... What the fuck was that?!"
    anon e_w @ -m_talk "( Man, that felt so real! )"
    anon e_sw f_disgusted @ -m_talk "( And great... I made a mess of my sheets. )"
    anon f_sad p_bed3_sit_sheet @ -m_talk "( Who has wet nightmares?! )"
    show anon e_wnw f_surprised
    jenny "What the hell is happening in there?!"
    show anon p_bed3_sit
    jenny "Why are you screaming at three in the morning?"
    anon f_worried "N-nothing!"
    anon "Nothing is happening... I just... had a bad dream is all."
    jenny "What are you, a toddler?"
    anon f_sceptical "Shut up!"
    jenny "You're such a loser sometimes, it's unbearable!"
    anon "Yeah, thanks."
    anon "I'm fine now, by the way."
    show anon e_w f_pouty
    jenny "Nobody cares."
    anon e_wnw f_sceptical "Ugh, just go back to bed."
    jenny "Gladly."
    show anon e_sw f_worried
    pause
    anon e_b f_tired m_yawn @ -m_talk "{i}*Yawn*{/i}"
    show anon p_bed3_curl
    pause
    anon @ -m_talk "( Everything is fine. )"
    anon @ -m_talk "( I'm fine. )"
    anon @ -m_talk "( Nothing to worry about. )"
    pause
    anon @ -m_talk "( Man, something is really wrong with me! )"

    scene black
    with dissolve
    return


label deb11_wake:
    scene debbie_bed3 at stage
    show anon a_rub f_worried with dissolve
    anon @ -m_talk "( Okay, these weird sexual dreams are really starting to become a bit of a circus... )"
    anon f_worried_surprised @ -m_talk "( ... {i}Literally.{/i} )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
