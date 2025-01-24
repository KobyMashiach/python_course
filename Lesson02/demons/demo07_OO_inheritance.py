class Person:
    def __init__(self):
        self.id = 0
        self.name = ""


class Employee(Person):
    def __init__(self):
        self.department = ""


p = Person()
p.id = 1
p.name = "Ron"

e = Employee()
e.id = 2
e.name = "Ron"
e.department = "IT"
