from animal import Animal


class Zebra(Animal):
    def __init__(self, numOfLegs):
        super().__init__(numOfLegs)
        self.NumofStrips = 0

    def printData(self):
        print(f"Legs: {self.numOfLegs}, Strips: {self.NumofStrips}")

    def eat(self):
        print("Zebra is eating")
