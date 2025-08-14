transform stage(x=.5, y=.5, z=1, *, b=10, c=True):
    blur b or None
    mesh z > 1 or None
    shader (('-renpy.geometry', 'saga.stage') if z > 1 else None)
    u_focus (sorted((0, x - .5 / z, 1 - 1 / z))[1] if c else x - .5 / z,
             sorted((0, y - .5 / z, 1 - 1 / z))[1] if c else y - .5 / z)
    u_zoom 1 / z


transform blur(r):
    blur r

transform left:
    anchor (.5, 1.) pos (.25, 1.)

transform right:
    anchor (.5, 1.) pos (.75, 1.)

transform rotate(a):
    rotate a rotate_pad False transform_anchor True

transform tint(c):
    matrixcolor (TintMatrix(c) if c else c)

transform zoom(z):
    zoom z transform_anchor True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
