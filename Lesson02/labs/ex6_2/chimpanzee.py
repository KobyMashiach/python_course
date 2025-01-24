from animal import Animal


class Chimpanzee(Animal):
    def __init__(self, numOfLegs, height):
        super().__init__(numOfLegs)
        self.height = height

    def printData(self):
        print(f"Legs: {self.numOfLegs}, height: {self.height}")
