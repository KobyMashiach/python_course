from zoo import *
from animal import *
from chimpanzee import *
from monkey import *
from zebra import *

a = Animal(3)
c = Chimpanzee(4, 150)
m = Monkey(4, "brown")
z = Zebra(4)
z.NumofStrips = 22

zoo = Zoo()
zoo.addAnimal(a)
zoo.addAnimal(c)
zoo.addAnimal(m)
zoo.addAnimal(z)

zoo.countAnimals()

zoo.feed()
