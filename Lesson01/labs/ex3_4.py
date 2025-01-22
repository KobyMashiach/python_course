from functools import reduce

arr = [6, 2, 8, 12, 4]

minimum = reduce(lambda x, y: min(x, y), arr)
print(minimum)
