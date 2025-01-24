class Person:
    def __init__(self):
        self.id = 0
        self.name = ""

    def printData(self):
        print(f"id: {self.id}, name: {self.name}")


class Employee(Person):
    def __init__(self):
        self.department = ""

    def printData(self):
        super().printData()
        print(f"department: {self.department}")

        # Overwriting option
        # print(f"id: {self.id}, name: {
        #     self.name}, department: {self.department}")


p = Person()
p.id = 1
p.name = "Ron"
p.printData()

e = Employee()
e.id = 2
e.name = "Ron"
e.department = "IT"
e.printData()
