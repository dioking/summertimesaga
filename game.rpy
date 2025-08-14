label start:
    $ saga.cast.anon.name = persistent.cast.get('anon', 'Anon')
    jump loop


label start.cheat:
    python hide:
        saga.cast.anon.bank = 9_990_000
        saga.cast.anon.cash = 10_000
        saga.cast.anon.chr = 10
        saga.cast.anon.dex = 10
        saga.cast.anon.int = 10
        saga.cast.anon.str = 10

    jump start


label start.recap:
    jump start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
