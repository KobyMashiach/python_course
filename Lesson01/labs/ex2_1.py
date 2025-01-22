num = 0
arr = []

while num <= 10:
    num = int(input("Enter a number: "))
    if num not in arr:
        arr.append(num)

print(arr)

for i in range(len(arr)):
    print(f"remove number: {arr.pop()}")
