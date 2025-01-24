class Zoo():
    def __init__(self):
        self.__animals = []

    def addAnimal(self, animal):
        self.__animals.append(animal)

    def countAnimals(self):
        print(len(self.__animals))

    def feed(self):
        for a in self.__animals:
            a.eat()
