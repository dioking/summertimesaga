label phoneleft:
    return


label phoneleft.answer:
    show layer aux at phoneleft
    show aux as phone with None
    with {'aux': phoneleft.show}
    return


label phoneleft.hangup:
    scene onlayer aux
    with {'aux': phoneleft.hide}
    "*Beep*"
    hide phone
    return


label phoneright:
    return


label phoneright.answer:
    show layer aux at phoneright
    show aux as phone with None
    with {'aux': phoneright.show}
    return


label phoneright.hangup:
    scene onlayer aux
    with {'aux': phoneright.hide}
    "*Beep*"
    hide phone
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
