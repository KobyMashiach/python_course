class Person:
    def __init__(self):
        self.age = 0
        self.name = ""

    def __gt__(self, obj):
        return self.age > obj.age

    def __add__(self, obj):
        p = Person()
        p.age = self.age + obj.age
        p.name = self.name + obj.name
        return p

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"


p1 = Person()
p1.age = 40
p1.name = "Ron"

p2 = Person()
p2.age = 50
p2.name = "Dana"

if p1 > p2:
    print("p1 is bigger")
else:
    print("p2 is bigger")

p3 = p1 + p2
# print(p3.name)
# print(p3.age)
print(p3)
