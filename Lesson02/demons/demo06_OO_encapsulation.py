class Person:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.__phones = []

    def addPhone(self, phone):
        self.__somePrivateFunction()
        if len(phone) == 7:
            self.__phones.append(phone)
        else:
            print("Phone is invalid")

    def __somePrivateFunction(self):
        print("Private function called")


p = Person()
p.id = 1
p.name = "Avi"

p.addPhone("050-000")
print(p)

# p.__phones.append("03-33")
# p.__somePrivateFunction()
