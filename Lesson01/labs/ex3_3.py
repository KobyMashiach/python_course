def add(num1, num2):
    print(num1+num2)


def sub(num1, num2):
    print(num1-num2)


def mul(num1, num2):
    print(num1*num2)


def exec_func(arr, x, y):
    for f in arr:
        f(x, y)


arr = [add, sub, mul]

exec_func(arr, 4, 2)
