label jen06_intro:
    scene debbie_bed3 at stage
    show anon a_pocket e_b f_happy m_teeth with dissolve
    anon @ -m_talk "( Man, those pictures of [saga.cast.jenny] were so hot! )"
    anon @ -m_talk "( I wish I could get another look at them... )"
    pause
    anon a_think e_nw f_pensive -m_teeth @ -m_talk "( Hmm, you know what? )"
    anon @ -m_talk "( I think she leaves her bedroom door unlocked while she's showering. )"
    anon e_w f_tired_happy @ -m_talk "( I could sneak in and find her camera, if I'm quick. )"
    show anon f_calm
    pause
    anon @ -m_talk "( I just need to wait until she's in the shower. )"
    hide anon
    with dissolve
    return


label jen06_bed2:
    scene debbie_bed2 at stage
    show anon a_pocket f_worried o_right at left with dissolve
    anon @ -m_talk "( Okay, I just need to find that camera and get out of here as quickly as possible. )"
    anon @ -m_talk "( She probably keeps it- )"
    anon f_surprised @ -m_talk "( !!! )"
    anon @ -m_talk "( Is that a diary?! )"
    anon e_b f_happy m_laugh @ -m_talk "( Oh, I have to check that out! )"
    hide anon
    with dissolve
    return


label jen06_bed2.bath:
    call shot.debbie_bath_peek
    show jenny c_naked_wet p_shower_legs s_1 behind glass
    show layer master at blur(20)
    pause
    show layer master
    with dissolve
    anon "( Okay, cool... she's in the shower. )"
    anon "( This is my chance to find those photos. )"
    return


label jen06_bed2.plan:
    call shot.debbie_bed2_door
    show anon a_pocket f_pensive o_right with dissolve
    anon @ -m_talk "( Now is a bad time for this. )"
    anon @ -m_talk "( I'll come back later. )"
    hide anon with dissolve
    return


label jen06_bed2.wait:
    call shot.debbie_bed2_door
    show anon f_worried o_right with dissolve
    anon @ -m_talk "( Too risky to snoop in there now. )"
    anon @ -m_talk "( I should try it when she's in the shower. )"
    hide anon with dissolve
    return


label jen06_snoop:
    scene debbie_bed2 at stage
    show anon a_reach e_s m_talk o_right p_bend at right
    pause
    show anon a_side e_sw f_pensive -m_talk -p_bend

    if saga.prop.pants_jenny in saga.cast.anon:
        show anon a_pants_jenny e_s f_horny

    label jen06_snoop.merge:
    pause
    show anon a_pocket e_w

    if saga.prop.pants_jenny in saga.cast.anon:
        show anon oa_pants_jenny

    pause
    show jenny a_hips f_angry m_teeth o_right at left

    if saga.cast.jenny in saga.sets.debbie_bath:
        show jenny c_towel

    jenny "What the fuck, [saga.cast.anon]?!"
    anon a_surprised_up_both f_surprised m_teeth -o_right @ -m_talk "!!!" with hpunch

    if saga.prop.pants_jenny in saga.cast.anon:
        jenny e_wsw f_surprised -m_teeth "Oh.{w=1} My.{w=1} God."
        jenny e_w f_angry m_teeth "ARE THOSE MY PANTIES?!"
        show anon e_sw f_shocked m_open
        pause
        anon @ -m_talk "..."
        anon e_w f_worried_surprised -m_open "N-no?"
        pause
        anon "I didn't-"
        show anon f_surprised m_teeth
        jenny a_wave_off "Save it, loser. Give them here!"
        show jenny a_pants_snatch at pos(.4)
        show anon e_sw oa_none
        pause
        show anon e_w
        show jenny a_pants_grasp at pos(.35)
        pause
        jenny f_annoyed -m_teeth "I suppose you just stumbled in here by accident, huh?"
    else:

        jenny "What are you doing in my room, you perverted little loser?!"
        anon f_worried_surprised "N-nothing!"
        show anon f_surprised
        jenny f_annoyed -m_teeth "Oh, yeah right. You just stumbled in here by accident, huh?"

    anon a_uneasy e_osw f_sad -m_teeth "Not exactly..."
    anon e_w f_tired "{i}*Sigh*{/i} I was looking for your digital camera, okay?"
    jenny a_hips "Huh, why?!"
    pause
    jenny f_snide "Oh, I get it."
    jenny "You're so pathetic, you know that?"
    jenny "You'd rather sit in your room fapping to stolen pictures of me, than go out and find real a girlfriend."
    anon a_pocket f_worried "N-no."
    jenny "Haha, yeah right!"
    anon e_osw f_sad "..."
    jenny a_camera_give "Tell you what, I'll let you look at the pictures, okay?"
    anon e_w f_surprised "Y-you will?"
    jenny "Sure."
    show anon f_worried
    jenny a_camera_back "Sixty bucks."
    anon "What?!"
    jenny "Sixty bucks and you can look at them for two minutes."
    anon "Two minutes?!"
    anon f_sceptical "You're out of your mind."
    jenny f_annoyed "Hey, you're the pathetic one who's hard up to get his rocks off..."
    jenny "You want to see the sexy pics or not?"

    menu:
        "Fine. {color=7ff7}[[Submissive]{/color}":
            pass
        "Screw you. {color=f77b}[[Dominant]{/color}":

            jump jen06_snoop.alt

    if saga.cast.anon.cash > 59:
        anon a_cash f_worried "Here."
        show anon a_camera
        jenny a_money f_snide "Hahaha! Oh my god, you're so pathetic!"
        show anon a_camera_look e_sw
        jenny "You've got two minutes..."

    elif saga.cast.anon.cash:
        anon e_osw f_sad "I don't even have sixty dollars..."
        jenny e_r "{i}*Sigh*{/i} God, you're pathetic."
        show jenny e_w
        pause
        jenny "Fine, just give me what you do have."
        show anon a_cash_bills e_w f_worried
        jenny "You've got two minutes..."
    else:

        show jenny e_wsw
        anon a_respect p_bow "I don't have anything... Please can I just look?"
        jenny f_disgusted "Pathetic."
        pause
        jenny a_camera_give "You've got thirty seconds..."
        show jenny a_hips e_w
        anon a_camera f_worried -p_bow "Thank you, [saga.cast.jenny]!"
        show jenny e_r f_annoyed
        show anon a_camera_look e_sw
        pause

    scene mini camera 01 onlayer aux at mini_camera_snap(*saga.cast.jenny.pics['01'])

    scene debbie_bed2_bed -laptop
    show debbie_bed2_bed camera view as camera at stage(.25, .75, 2, b=0)
    with fade
    pause
    anon "Man, these turned out so good!"
    jenny "Umm, duh..."
    jenny "... It's like, basically impossible to take a bad picture of me."
    show mini camera 02 at mini_camera_snap(*saga.cast.jenny.pics['02'])
    with pushleftfast.aux
    pause
    anon "Mmm, I'd love to rub my face on that..."
    jenny "Eww, don't be gross!"
    anon "... I'm just saying, it looks nice!"
    jenny "I don't wanna hear that from you, [saga.cast.anon]!"
    show mini camera 03 at mini_camera_snap(*saga.cast.jenny.pics['03'])
    with pushleftfast.aux
    pause
    anon "I'm not sure about classy but it's definitely sexy."
    jenny "Of course it's sexy, it's me."
    anon "And so modest."
    jenny "I know right! Exactly what I was going for."
    anon "..."
    show mini camera 04 at mini_camera_snap(*saga.cast.jenny.pics['04'])
    with pushleftfast.aux
    pause
    anon "I definitely captured your good side in this one."
    jenny "Pfft, as if I have a bad side..."
    anon "Okay, your best asset then!"
    jenny "Oh my god, you're so annoying!"

    scene onlayer aux
    with hold.aux

    scene debbie_bed2 -jenny at stage
    show anon a_pocket f_surprised at right
    show jenny a_camera f_annoyed o_right at left
    with fade
    jenny "Time's up, loser!"
    show jenny a_hips with dissolve
    show anon f_confused

    if saga.cast.anon.cash:
        anon "That wasn't even two minutes!"
    else:
        anon "That wasn't even thirty seconds!"

    jenny f_snide "Aww, poor little virgin..."
    show anon f_pouty
    jenny f_annoyed "Go whine to somebody who cares."
    hide jenny
    with dissolve
    jenny "And get the fuck outta my room, loser!"
    anon f_annoyed "Fine!"
    hide anon
    with dissolve

    call shot.debbie_bed2_door
    with fade
    show anon a_pocket f_pouty with dissolve
    anon @ -m_talk "( She's such a bitch! )"
    anon f_horny_smug @ -m_talk "( Those pics were worth it though... )"
    hide anon
    with dissolve
    return +1


label jen06_snoop.alt:
    anon f_annoyed "I'm not paying you sixty dollars for a couple stupid pictures..."
    jenny f_angry m_teeth "Excuse me?!"
    anon f_sceptical "You heard me!"
    jenny a_fold f_angry_pouty -m_teeth @ -m_talk "Hmph!"
    pause
    jenny f_annoyed "Thirty bucks?!"
    anon f_angry "NO!"
    jenny f_disgusted "Seriously?!"
    jenny f_angry m_teeth "Grr, just get out!"
    anon f_sceptical "What?"
    jenny a_upset "Get out of my fucking room before I tell my mom you're perving on me!"
    anon "Gladly."
    hide anon
    with dissolve.nowait
    jenny a_fold f_angry_pouty -m_teeth -o_right @ -m_talk "( He's such a pain in my ass! )"

    call shot.debbie_bed2_door
    with fade
    show anon a_pocket f_annoyed with dissolve
    anon @ -m_talk "( Damn, I really wanted to see those pictures but not so much that I'll let her walk all over me. )"
    anon f_horny_smug @ -m_talk "( At least I found out she's got a diary and just how sexually frustrated she is. )"
    anon e_b f_happy m_laugh @ -m_talk "( Haha! )"
    hide anon
    with dissolve
    return -1


label jen06_snoop.diary(fast=None):
    scene debbie_bed2 at stage with None
    show anon a_pocket f_surprised

    if saga.prop.pants_jenny in saga.cast.anon:
        show anon oa_pants_jenny

    with dissolve
    anon @ -m_talk "( Wow, I can't believe how conceited she is... )"
    pause
    anon f_calm @ -m_talk "( I should hurry up and find that camera! )"
    show anon o_right
    pause

    if fast:
        show anon e_sw f_pensive at right
        jump jen06_snoop.merge

    anon a_think e_nw f_pensive @ -m_talk "( ... Maybe it's in her nightstand? )"
    hide anon
    with dissolve
    return


label jen06_snoop.drawer:
    scene jenny_drawer
    anon "( Hmm, it's not in here... )"
    pause

    if saga.prop.pants_jenny in saga.prop.jenny_drawer:
        anon "( Are those her panties? )"

    return


label jen06_snoop.rails:
    scene debbie_bed2 at stage
    show anon f_worried o_right at left with dissolve
    anon @ -m_talk "( I should move quickly, [saga.cast.jenny] could finish up with her shower at any moment. )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
