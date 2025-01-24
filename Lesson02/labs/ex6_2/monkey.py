from animal import Animal


class Monkey(Animal):
    def __init__(self, numOfLegs, color):
        super().__init__(numOfLegs)
        self.color = color

    def printData(self):
        print(f"Legs: {self.numOfLegs}, color: {self.color}")

    def eat(self):
        print("Monkey is eating")
