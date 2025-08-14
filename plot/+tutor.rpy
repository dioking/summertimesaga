label tutor:
    return


label tutor.hud:
    scene camera
    show help_hud

    show aux
    show layer aux at tutor.mask

    tutor "Welcome to [config.name]!" with dissolvefast

    show help_menu onlayer aux
    show help_arrow at tutor.menu
    with dissolve.nowait | dissolve.aux

    nvl clear

    tutor "This is the pause button. It leads to the save and load menus, settings, and allows you to return to the main menu."




    if renpy.variant('touch'):
        tutor "It can also be accessed with tap-and-hold."
    else:
        tutor "It can also be accessed with right-click."

    show help_dow onlayer aux
    show help_arrow at tutor.dow
    with tutor.next

    nvl clear

    tutor "These two boxes tell you what day of the week it is..."

    show help_where onlayer aux
    show help_arrow at tutor.where
    with tutor.next

    extend " and where you are, respectively."
    tutor "As in life, some activities are only available on specific days of the week. A good example of this is classes, which only take place Monday through Friday."
    tutor "Advancing between days is done by sleeping, which can be triggered by interacting with [saga.cast.anon]'s bed."







    show help_map onlayer aux
    show help_arrow at tutor.map
    with tutor.next

    nvl clear

    tutor "The map icon is used to display the town map, which can be used to travel to other locations in Summerville."
    tutor "While the map is always available, sometimes it will not be possible to travel due to an active quest."
    tutor "Travelling is not teleporting and may be interrupted by an event taking place en route."








    show help_inv onlayer aux
    show help_arrow at tutor.inv
    with tutor.next

    nvl clear

    tutor "Clicking the satchel icon accesses the inventory. It contains any items collected around town, along with their names and descriptions."
    tutor "Some items can be further inspected, or in rare cases used directly from the inventory. Worth keeping in mind if you find yourself struggling with a quest involving special items."








    show help_tel onlayer aux
    show help_arrow at tutor.tel
    with tutor.next

    nvl clear

    tutor "The phone contains a multitude of in-game functionality, including text messages, statistics, and quest hints."




    show help_cash onlayer aux
    show help_arrow at tutor.cash
    with tutor.next

    nvl clear

    tutor "This display shows the cash currently on hand."
    tutor "Money can be earned around Summerville by taking on certain jobs and tasks. As you may expect, it's mostly used for shopping."





    scene help_hud onlayer aux
    show layer aux at tutor.mask

    show help_arrow at tutor.time
    with tutor.next

    nvl clear

    tutor "There are four times of day:"

    show help_arrow at tutor.dawn
    with tutor.next

    extend " morning"

    show help_arrow at tutor.noon
    with tutor.next

    extend ", afternoon"

    show help_arrow at tutor.dusk
    with tutor.next

    extend ", evening"

    show help_arrow at tutor.dark
    with tutor.next

    extend ", and night."

    show help_arrow at tutor.time
    with tutor.next

    tutor "Clicking on a time of day in the future will advance time until then.{w} Unless you're interrupted of course."




    hide help_arrow
    with dissolve.nowait

    tutor "You can't use it just yet though, plenty of things to do this morning!"
    tutor "Have fun!"





    scene onlayer aux
    with hold.aux

    nvl clear
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
