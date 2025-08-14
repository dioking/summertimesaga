label jen28_jenny:
    scene debbie_landing at stage
    show jenny a_fold c_casual_towel at right
    show anon a_pocket o_right at left with dissolve
    jenny "Hey, [saga.cast.anon]!"
    anon f_worried "Oh, h-hey [saga.cast.jenny]..."
    anon "Did you just get out of the shower?"
    jenny f_disgusted "Duh, what gave it away?"
    show jenny f_calm
    anon f_sceptical @ -m_talk "..."
    jenny e_b m_laugh @ -m_talk "Hahahaah!"
    anon "Very funny."
    show jenny e_w f_snide -m_laugh
    pause
    anon f_calm "So, what are you doing today?"

    if saga.cast.jenny.womb and not (saga.cast.jenny.womb.belly and saga.cast.jenny > 'baby.sex'):
        jenny e_r f_annoyed "Uhh, being pregnant, mostly... What do you want?"
    elif saga.cast.jenny.womb.post:
        jenny e_r f_annoyed "Uhh, taking care of {i}our{/i} child... Why?!"
    else:
        jenny e_r f_annoyed "Uhh, {i}we're{/i} doing a camshow, remember?"

    show jenny e_w f_calm
    anon "Well, yeah... I figured."
    anon "But maybe at some point later, if you're free, we could spend some time together?"
    jenny f_disgusted "You wanna spend time... together?"
    anon "Yeah, You know... cuddle up on the couch or maybe go out and see a movie?"
    jenny "Why would we do that?"
    anon @ e_b f_happy m_laugh "'Cause it would be fun!"
    jenny "..."
    anon "We had fun at the movie theater the other day, didn't we?"
    jenny "Uhh, I guess..."
    pause
    jenny f_annoyed "{i}*Sigh*{/i} Do we need to have the dating talk again?"
    anon f_tired @ -m_talk "..."
    anon "I just thought-"
    show anon f_surprised
    jenny "You thought what, that I didn't really mean it the first two times I told you I'm not interested?"
    anon f_worried "B-but-"
    jenny f_angry m_teeth "I DON'T WANNA DATE YOU, [saga.cast.anon!u]!"
    show jenny f_annoyed -m_teeth
    anon "Why not?!"
    jenny e_r "Because we've known each other for like, our entire lives, and dating you would be super weird!!!"
    show jenny e_w
    anon a_rub e_nw f_pensive @ -m_talk "..."
    jenny f_disgusted "It would be like dating my brother or something..."
    show jenny f_snide
    show anon a_pocket e_b f_happy m_laugh
    pause 1
    anon e_w f_worried -m_laugh "That's not-"
    anon f_pouty "What?!"
    jenny f_annoyed "I'm serious, [saga.cast.anon]!"
    jenny "We have a good thing going here..."
    jenny "Why are you trying to ruin it?"
    anon "Alright, whatever."
    anon "Forget about it."
    jenny "Gladly!"

    if saga.cast.jenny.womb.state and not (saga.cast.jenny.womb.belly and saga.cast.jenny > 'baby.sex'):
        show jenny o_right
        hide anon with dissolve.nowait
    else:

        jenny f_snide "Now, don't forget about our show this afternoon!"
        anon "Yeah, yeah..."
        show jenny o_right
        hide anon with dissolve.nowait
        jenny "... And make sure you eat something!"
        jenny "My fans are expecting a good performance!"

    pause
    jenny e_r f_annoyed "Pain in my ass..."

    scene debbie_lobby at stage with fade
    show anon a_pocket f_tired o_right at left with dissolve
    anon @ -m_talk "( Well, that could have gone better... )"
    anon @ -m_talk "( She's really being stubborn about this! )"
    anon a_think e_nw f_pensive @ -m_talk "( There's gotta be some way to convince her! )"
    anon @ -m_talk "( Hmm, maybe I should check her diary again? )"
    anon @ -m_talk "( It's been pretty helpful so far... )"
    hide anon with dissolve
    return


label jen28_react:
    scene debbie_bed2 at stage
    show anon a_pocket e_b f_happy m_laugh o_right with dissolve
    anon @ -m_talk "( That's it! )"
    anon e_w f_calm -m_laugh "( I should buy her something nice and see if that makes her rethink this whole dating thing! )"
    anon e_nw f_pensive @ -m_talk "( Now the only question is, what do I buy her? )"
    anon a_think @ -m_talk "( Hmm, she'll want something expensive, no doubt! )"
    anon a_pocket e_w f_calm @ -m_talk "( I should head to the mall and see about getting her a necklace or something. )"
    hide anon with dissolve
    return


label jen28_gift(what):
    scene gift_shop at stage with None
    show anon e_s

    if what is saga.prop.necklace_crystal:
        show anon a_necklace_crystal
    elif what is saga.prop.necklace_heart:
        show anon a_necklace_heart
    else:
        show anon a_necklace_pearl

    with dissolve
    anon @ -m_talk "( Yeah, this'll thaw out [saga.cast.jenny]'s cold dead heart for sure... )"
    anon @ -m_talk "( ... I should hurry back home and surprise her with it! )"
    hide anon with dissolve
    return


label jen28_gift.take:
    anon "( Hmm, I bet [saga.cast.jenny] would like this. )"
    anon "( Maybe should buy it for her. )"
    return


label jen28_give(what):
    anon f_happy "I have a surprise for you!"
    jenny @ e_r f_annoyed "Well, it had better be something nice!"
    show anon a_backpack e_s f_shy
    pause

    if what is saga.prop.necklace_crystal:
        show anon a_necklace_crystal
    elif what is saga.prop.necklace_heart:
        show anon a_necklace_heart
    else:
        show anon a_necklace_pearl

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon e_e
    else:
        show anon e_w

    anon @ e_b f_happy m_laugh "Ta-da!"
    show anon f_calm
    jenny f_surprised "..."
    jenny f_disgusted "Eww!"
    anon f_worried "Y-you don't like it?"
    show anon f_tired
    jenny "Eugh, no!"
    anon "..."
    jenny "Why in the hell would you buy me that?!"
    anon "I just thought, maybe it would convince you to-"
    show anon f_worried
    jenny @ f_annoyed "Oh my god, are you trying to butter me up for a date again?!"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon a_down f_tired
    else:
        show anon a_side f_tired

    anon @ -m_talk "..."
    jenny e_r f_annoyed "What the fuck, [saga.cast.anon]?!"
    jenny e_w "{i}*Sigh*{/i} Okay, first of all, you have terrible taste..."
    jenny "That necklace looks cheap as hell!"
    anon @ -m_talk "..."
    jenny "I mean, honestly, if by some miracle you actually do land a girlfriend one day... you should just give her cash and let her-"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_laugh f_surprised
    else:
        show jenny f_surprised

    jenny "!!!"
    anon f_confused "Let her what?"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_spoon f_snide
    else:
        show jenny a_hips f_snide

    jenny "Oh my god, I just had a brilliant idea!"
    anon f_worried @ -m_talk "..."
    jenny "I'm thinking, since you're obviously pathetic and desperate for a girlfriend..."
    anon f_sceptical "Hey, that's not-"
    jenny "I {i}might{/i} be willing to act like one... for a modest fee of course."
    anon "Wait a second."
    anon "Are you seriously suggesting that I pay you to be my girlfriend?"
    jenny "No, I'm suggesting that you pay me to {i}pretend{/i} to be your girlfriend..."
    anon @ -m_talk "..."
    anon "Why would I ever do that?"
    jenny @ e_b f_calm m_laugh "Because like I said, you're pathetic and desperate."
    anon f_pouty "I am not!"
    jenny @ e_b f_calm m_laugh "Hahahaah, you so are!"
    anon @ -m_talk "..."
    jenny "Plus, this will give me a chance to work on my acting!"
    anon f_disgusted "Yeah, you are a terrible actress..."
    jenny f_annoyed @ f_angry "{i}*Gasp*{/i} Fuck you!"
    jenny "I'm an awesome actress!"
    anon @ f_pouty "Yeah, right."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon e_sse f_surprised
        show jenny a_rub_01 f_snide
    else:

        show anon e_s f_surprised behind jenny
        show jenny a_touch_high f_snide at center

    jenny "C'mon, this would be a perfect excuse for us to spend more time together."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon e_e
    else:
        show anon e_w

    anon "W-what are you doing?"

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_rub s_1
        show anon e_sse
    else:

        show jenny a_touch_low
        show anon e_s

    jenny "I really wanna do this, [saga.cast.anon]..."
    jenny "Let me show you how I really feel about you."
    anon @ -m_talk "..."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show anon e_e
    else:
        show anon e_w

    jenny "I don't wanna hide it anymore..."
    show anon f_confused
    jenny "I wanna tell the whole world just how much I care about you!"
    jenny "How I think about you all the time..."
    jenny "Your handsome face, your strong arms... Your adorable little haircut!"
    anon f_worried "R-really?"
    jenny "Mhmm."
    jenny "I want to hold your hand, [saga.cast.anon]!"
    anon @ -m_talk "..."
    jenny "I want to taste your lips..."
    show anon f_shy
    jenny "... Fall asleep in your arms."
    anon @ -m_talk "..."
    jenny "I want to tell you that I love you!"
    anon "I want that too!"
    pause

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show jenny a_fold e_b f_calm m_laugh
    elif 'o_right' in renpy.get_attributes('jenny'):
        show jenny a_fold e_b f_calm m_laugh at left
    else:
        show jenny a_fold e_b f_calm m_laugh at right

    jenny @ -m_talk "Pfft, HAHAHAHAHAAAH!!"
    anon f_surprised @ -m_talk "..."
    anon f_angry "That's not funny, [saga.cast.jenny]!"
    jenny @ -m_talk "You should have seen your face!!"
    jenny @ -m_talk "HAHAHAAH! {i}*Snort*{/i}"
    anon "You are such a bitch!"
    jenny e_w -m_laugh "You're the one who said I couldn't act!"
    jenny f_snide "Admit it, I'm damn good!"
    anon f_tired @ -m_talk "..."
    jenny "I could girlfriend the shit out of you... for the right price."
    anon "{i}*Sigh*{/i} How much do you want?"
    jenny f_horny "Mmm, let's say five hundred dollars for the night."
    anon f_surprised "Five hundred!!"
    anon "That's a lot, [saga.cast.jenny]!"
    jenny f_annoyed @ e_r "Oh, please... It's chump change."

    if saga.cast.jenny.womb or saga.time.tod < saga.time.dusk:
        jenny f_snide "Tell ya what, I'll throw in the morning after too."
    else:
        jenny f_snide "Tell ya what, I'll throw in tomorrow morning too."

    anon f_calm "Y-you mean you'll stay with me all night?"
    jenny "That's what you want, isn't it?"

    menu:
        "Yes.":
            pass
        "No, I want the real thing!":

            anon f_worried "No, I want the real thing."
            jenny e_r f_annoyed "Yeah, not happening, loser."

            if saga.cast.jenny.womb:
                jenny e_w "Perhaps by the time this baby arrives you'll have come to your senses..."
            else:
                jenny e_w "Let me know when you come to your senses..."

            anon e_osw f_sad @ -m_talk "..."

            if 'debbie_dining_table' in renpy.get_showing_tags():
                show debbie_dining_table pull3

            hide anon
            with dissolve
            return

    anon "Yes."
    jenny "Then we have a deal!"

    if saga.cast.jenny.womb:
        jenny "Come back once I've had this baby and for five hundred dollars I'm all yours."
    elif saga.time.tod < saga.time.dusk:
        jenny "Come back this evening with five hundred dollars and I'm all yours."
    else:
        jenny "Come back tomorrow with five-hundred dollars and I'm all yours."

    anon f_worried "Why can't we start now?"
    show jenny f_annoyed

    if saga.cast.jenny.womb:
        jenny "Uhh, because this pregnancy is making me nauseous enough without also having to deal with you, idiot!"
    elif saga.time.dawn:
        jenny "Uhh, because five hundred gets you an evening, not my entire day, idiot!"
    elif saga.time.noon:
        jenny "Uhh, because it's camshow time and that pays way more then five hundred measly dollars, idiot!"
    else:
        jenny "Uhh, because I already have plans tonight, idiot!"

    anon f_pouty "Ugh, fine."

    if 'debbie_dining_table' in renpy.get_showing_tags():
        show debbie_dining_table pull3

    hide anon
    with dissolve
    return


label jen28_give.baby:
    show anon f_calm
    jenny "You're gonna grow up and be a movie star, aren't you?"
    jenny "Make lots of money and buy Mommy a nice big house!"
    anon f_shy "So, hey... I got you something and-"
    show anon f_worried
    jenny @ e_w f_annoyed "Not now, [saga.cast.anon]... Can't you see I'm busy with the baby?!"
    anon a_backpack e_s "But it'll just take a second and I think you'll-"
    jenny "Don't you listen to Daddy..."
    show anon a_backpack_02 e_w f_confused
    jenny "... He's only got two braincells in his head and they're both fighting for third place."
    anon a_side f_sad @ e_osw "{i}*Sigh*{/i}"
    anon "Never mind..."
    return


label jen28_outro:
    return


label jen28_outro.soon:
    anon f_confused "You wanna do the girlfriend thing?"
    jenny f_annoyed "I said I have plans tonight, idiot!"
    anon f_pouty "Ugh, fine."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
