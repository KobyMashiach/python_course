class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


p1 = Person(1, "Avi")
p1.name = "Dana"

p2 = Person(2, "Ron")


print(p1.name)
