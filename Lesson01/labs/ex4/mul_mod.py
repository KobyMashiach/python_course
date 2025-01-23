from add_mod import *


def mul(x, y):
    sum = 0
    while (y > 0):
        sum = add(sum, x)
        y -= 1
    return sum
