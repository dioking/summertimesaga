label prologue:
    play music sad if_changed volume .25
    play sfx rain1 if_changed

    scene mono intro1
    mono "March 3rd, on a rainy afternoon." with fadewait
    mono "My father's funeral."
    mono "I can't believe he's really gone."
    mono "He died from a work related accident at the age of forty-seven, leaving me all alone with no family to speak of..."

    play sound rain2 if_changed loop

    scene mono intro2
    mono "Circumstances surrounding his death have been found \"suspicious\" by the police." with fadewait
    mono "They were at our house for an entire week, bombarding me with questions to which I had no answers."
    mono "No conclusive evidence has been found and the knowledge that my father will get no justice weighs heavily upon me."

    scene mono intro3
    mono "Luckily, my father's lifelong friend has taken me in and given me a room in her home." with fadewait
    mono "She's a kind woman, with a big home, and only her daughter living there with her."

    stop sound fadeout 2
    play sfx rain3 if_changed

    scene mono intro4
    mono "The night of the funeral, I overheard her reminiscing about my father in the kitchen." with fadewait
    mono "She eventually broke down and said she didn't know what to do."
    mono "It seems my father had gotten involved with some really bad people who were now pressuring her to cover his debts."

    stop music fadeout 3
    stop sfx fadeout 3

    scene black
    mono ""

    play sfx suburb if_changed
    pause 1

    scene mono intro5
    mono "Now, a month later, things are finally starting to settle down." with dissolve
    mono "I've gotten used to the new living arrangements, and today will be my first day back at college."
    mono "It'll be nice to see my friends again."
    mono "There are three things I have to take care of before the end of the semester."
    mono "1) I need to earn some money and help pay off my father's debts."
    more "2) I have to uncover the truth about my father's death."
    more "3) I have to find a date for the Sorority Ball."

    stop sfx fadeout 2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
