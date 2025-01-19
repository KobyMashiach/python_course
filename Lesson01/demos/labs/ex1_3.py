length = int(input("Enter arr length: "))
arr = []

for i in range(length):
    arr.append(int(input("enter " + str(length) + " numebrs: ")))


x = int(input("Enter a number: "))

for i in range(3, length):
    if x < 5:
        arr[i] += x
    elif x > 5 and x <= 10:
        arr[i] *= x
    else:
        arr[i] **= x

print(arr)
