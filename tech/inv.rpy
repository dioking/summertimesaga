label inv(what):
    scene expression saga.easy.image(f'art/mini/inv/{saga.camera.focus.ref}/zoom.png')
    show expression saga.easy.ref(what.ref)
    with dissolvefast
    pause
    $ renpy.transition(dissolvefast)
    return


label inv.french_poem:
    scene expression saga.easy.image(f'art/mini/inv/{saga.camera.focus.ref}/zoom.png')
    show french_poem
    anon "( \"I slip slowly under the satin sheets.\" )" (show_lang="( {i}\"Je me glisse lentement sous les draps de satin.\"{/i} )")
    anon "( \"You are lying on your stomach, your back welcomes my hand.\" )" (show_lang="( {i}\"Tu es allong? sur le ventre, ton dos accueil ma main.\"{/i} )")
    anon "( \"Slowly your naked body you expose.\" )" (show_lang="( {i}\"Tout doucement ton corps nu tu exposes.\"{/i} )")
    anon "( \"On your breasts my mouth rests.\" )" (show_lang="( {i}\"Sur tes seins ma bouche se pose.\"{/i} )")
    pause
    anon "( I need to turn this in to [saga.cast.viv] and hope no one else ever reads this! )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
