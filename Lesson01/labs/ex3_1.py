def getStrLength(word="Hello"):
    return len(word)


def getTotalLength(arr=[]):
    total = 0
    for str in arr:
        total += getStrLength(str)
    return total


print(getStrLength())

print(getTotalLength(["ab, koby, mashiach"]))
