class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.birthYear = 0

    def printData(self):
        print(f"id: {self.id}, name: {
              self.name}, Birth year: {self.birthYear}")

    def getAge(self, currectYear):
        return currectYear - self.birthYear


p1 = Person(1, "Avi")
p1.birthYear = 1996
p2 = Person(2, "Ron")
p2.birthYear = 2000

p1Age = (p1.getAge(2025))
print(p1Age)

p1.printData()
p2.printData()
