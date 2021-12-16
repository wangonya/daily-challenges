import math


def frog_jmp(x, y, d):
    z = y - x
    return math.ceil(z / d)


assert frog_jmp(10, 85, 30) == 3
