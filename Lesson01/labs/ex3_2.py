from functools import reduce

arr = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]
print(arr)

arr2 = list(map(lambda x: len(x), arr))
print(arr2)

arr3 = list(filter(lambda x: x > 4, arr2))
print(arr3)

total = reduce(lambda x, y: x+y, arr3)
print(total)
