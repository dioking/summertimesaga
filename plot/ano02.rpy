label ano02_intro:
    scene debbie_bed3 at stage
    "*Ding Dong*"
    show anon a_think e_nw f_pensive o_right at left with dissolve
    anon @ -m_talk "( Was that the doorbell? )"
    anon @ -m_talk "( Who could be here this early in the morning? )"
    anon e_b f_happy m_teeth @ -m_talk "( I'm the man of the house now, I should probably check it out. )"
    hide anon
    with dissolve
    return


label ano02_harold:
    scene debbie_lobby at stage
    show anon a_pocket o_right at left with dissolve
    debbie "Can I get you a cup of coffee, officer?"
    show anon f_surprised
    harold "Oh, you can call me [saga.cast.harold], ma'am."
    harold "Coffee would be lovely."
    debbie "Sure."
    anon @ -m_talk "( It's a police officer. )"
    show anon f_worried
    harold "I thought you might like an update on your friend's case."
    anon f_shocked m_open @ -m_talk "!!!"
    debbie "{i}*Gasp*{/i} You have news?"
    anon @ -m_talk "( He's here about Dad! )"

    scene debbie_kitchen -debbie at stage
    show harold f_worried o_right at left
    show debbie a_mug f_sad at right
    with fade
    harold "Ehh, not as much as I'd hoped."
    show debbie a_mug_give at pos(.65)
    pause
    show debbie a_clasp
    harold a_mug f_calm "Thank you for this."
    show harold a_mug_sip e_b m_talk
    pause
    harold a_mug e_w -m_talk "Mm, that's nice!"
    debbie "What have you found out?"
    harold f_worried "Right."
    harold "Well, the autopsy report confirms that he died from asphyxiation..."
    harold "... And that coupled with the excessive bruising around his throat means suicide is the most likely scenario."
    debbie "{i}*Sigh*{/i} It just doesn't make any sense."
    debbie "[saga.cast.frank] would never have killed himself."
    harold "Hmm, I can't really speak to that, ma'am."
    harold "But it seems like your friend was keeping quite a lot from you."
    debbie "What do you mean?"
    harold "You said he was working as an accountant, correct?"
    debbie "Yes."
    harold "And he was employed at Saga Financial Bank?"
    debbie "That's right, for fifteen years."
    harold "Well, I spoke with the bank manager there, and she told me that your friend was fired eighteen months ago."
    debbie @ f_worried_surprised "WHAT?!"
    debbie "No, no, that can't be right..."
    harold "The paperwork cited a declining work performance and multiple incidents involving shady characters."
    debbie "But that doesn't-"
    debbie a_facepalm e_b f_crying "{i}*Sniff*{/i} How could he keep this from me?!"
    pause
    debbie "W-what was he doing for work all this time?"
    harold "{i}*Sigh*{/i} Well, I'm afraid we haven't figured that part out yet."
    debbie @ -m_talk "..."
    harold "We do have evidence linking him to several high-value accounts, and eyewitness statements claim he was moving a lot of money around."
    debbie a_clasp e_w f_sad "Witness statements?"
    harold "Yes, apparently he was quite friendly with a teller by the name of... [saga.cast.liu] Wang."
    debbie "I'm not familiar with her..."
    harold "She said he had recently started working for a new client and that their accounts were all valued at well over seven figures."
    debbie @ f_worried_surprised -m_talk "!!!"
    harold "Unfortunately, that money vanished not long after your friend's death."
    harold "From what we can tell, it was moved electronically into offshore accounts. But so far, we've been unable to trace it."
    harold "At this time, we don't have a clue where it came from or who else might have been involved."
    debbie a_facepalm e_b f_crying @ -m_talk "..."
    harold "It's my opinion that your friend got mixed up with some sort of criminal element and was most likely helping them to launder money."
    debbie "This can't be happening..."
    pause
    harold "It would also explain the threats you've been receiving."
    debbie @ -m_talk "..."
    harold "You said they're demanding money?"
    debbie a_clasp e_w f_sad "{i}*Sniff*{/i} Y-yes."
    harold "I pulled your phone records from the past couple days and it seems the calls are coming from an overseas number."
    debbie "How is that possible?"
    harold "I don't know, ma'am."
    harold "{i}*Sigh*{/i} There's really not much I can do to help you at this point..."
    debbie "B-but, what am I supposed to do?!"
    harold "I'm terribly sorry, ma'am."

    scene debbie_lobby at stage
    show anon a_pocket f_shocked m_open o_right at right
    with fade
    anon @ -m_talk "( ... Eighteen months?! )"
    anon @ -m_talk "( That doesn't make any sense! )"
    anon @ -m_talk "( My dad would never work for a bunch of criminals... Would he? )"
    anon a_think e_nw f_pensive -m_open @ -m_talk "( Was he just lying to us the whole time? )"
    pause
    show yumi o_right at left with dissolve
    anon @ -m_talk "( It's just so hard to believe, he- )"
    yumi "Excuse me?"
    anon a_surprised_up_both e_w f_surprised m_teeth -o_right @ -m_talk "!!!" with hpunch
    anon a_pocket f_sceptical -m_teeth "Holy crap lady, you scared the bejesus out of me!"
    yumi @ e_b f_happy m_laugh "Hehe, sorry about that."
    yumi "I'm looking for my partner, [saga.cast.harold]."
    anon f_worried "Y-yeah, he's in there."
    yumi "Thanks."
    hide yumi with dissolve
    anon e_osw f_sad @ -m_talk "..."

    scene debbie_kitchen -debbie at stage
    show debbie a_facepalm e_b f_crying at pos(.635)
    show harold f_worried o_right at pos(.35)
    with fade
    harold "I'm sure there's something we're overlooking."
    harold "I just need a little more time-"
    show yumi f_worried o_right behind debbie at pos(.15) with dissolve
    yumi "Excuse me, sir?"
    show debbie a_clasp e_w f_sad
    show anon a_pocket f_worried behind debbie at pos.debbie.hand
    show harold -o_right
    with dissolve
    harold "What is it, [saga.cast.yumi]?"
    show anon a_beer_cheer
    show debbie a_anon_hand_01
    show harold behind anon
    yumi a_point_back "We just got a call on a possible 10-62."
    show yumi a_side
    harold "The bedtime bandit again?"
    yumi "Most likely."
    harold @ a_facepalm e_b f_calm "{i}*Sigh*{/i} I'll be right there."
    hide yumi with dissolve
    harold "The fun never stops..."
    harold o_right "I'm afraid we're going to have to cut this short."
    harold "Hey there, kiddo."
    anon "Hello."
    show debbie a_anon_hand_02
    pause
    harold a_card "If you think of anything else that might help in our investigation, or the threats escalate into something worse, don't hesitate to call me..."
    show harold a_card_give
    debbie "{i}*Sniff*{/i} Yeah, okay."
    harold a_side "I'll have my partner [saga.cast.yumi] drop in on you from time to time..."
    harold "... Just to check that your family is safe."
    debbie "Thanks."
    harold "We're gonna sort this whole thing out, ma'am."
    harold "You have my word."
    debbie "..."
    harold "Son, you take good care of your landlady now, alright?"
    anon "Y-yes, sir."
    harold "I'll be in touch."
    hide harold with dissolve
    pause
    anon "[saga.cast.debbie]?"
    show anon a_side
    show debbie a_clasp o_right at pos(.55)
    debbie "{i}*Sniff*{/i} How much of that did you overhear?"
    anon "I..."
    show anon e_osw f_sad
    pause
    anon "I dunno."
    anon "Enough to be worried."
    pause
    anon e_w f_worried "What are we going to do?"
    debbie "Sweetie, this isn't something you need concern yourself with..."
    debbie "That's my job."
    anon "Y-yeah, but-"
    debbie "I'll handle it."
    anon "[saga.cast.debbie], you don't have to do this alone..."
    debbie "I want you to focus on school."
    debbie "That's the most important thing for you right now."
    anon @ -m_talk "..."
    debbie "It's what your father would want."
    anon "{i}*Sigh*{/i} Dad doesn't want anything anymore..."
    debbie "[saga.cast.anon], don't say things like that!"
    anon "Sorry, [saga.cast.debbie]."
    show anon e_osw f_sad p_debbie_hug_away
    show debbie b_anon p_hug_away behind anon at pos.anon
    debbie "{i}*Sniff*{/i} Everything is going to be alright."
    debbie "I promise."
    anon @ -m_talk "..."
    show anon e_w f_worried -p_debbie_hug_away
    show debbie -b_anon -p_hug_away at pos(.55)
    debbie "Now go get ready for school."
    anon "Yeah, okay."
    hide anon with dissolve
    return


label ano02_harold.rails:
    scene camera at stage
    show anon with dissolve.nowait
    anon @ -m_talk "( Someone's at the front door. )"
    anon @ -m_talk "( I should check it out. )"
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
