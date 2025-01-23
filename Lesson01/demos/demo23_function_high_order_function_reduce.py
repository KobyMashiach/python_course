from functools import *
arr = [5, 2, 3, 6]

total = reduce(lambda x, y: x + y, arr)
print(total)
