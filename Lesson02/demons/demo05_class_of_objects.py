class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.birthYear = 0
        self.phones = []

    def printData(self):
        print(f"id: {self.id}, name: {
              self.name}, Birth year: {self.birthYear}, phones: {self.phones}")

    def getAge(self, currectYear):
        return currectYear - self.birthYear


p1 = Person(1, "Avi")
p1.birthYear = 1996
p1.phones.append("050-0000")
p1.phones.append("054-4444")


p2 = Person(2, "Ron")
p2.birthYear = 2000

arr = [p1, p2]
for p in arr:
    p.printData()
