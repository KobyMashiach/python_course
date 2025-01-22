students = {11: [90, 88, 100], 44: [87, 99]}

id = int(input("Enter ID: "))

if id in list(students.keys()):
    print(max(students[id]))
else:
    print("ID don't found")
