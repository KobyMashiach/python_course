
class Store():
    def __init__(self):
        self.__toys = []

    def addToy(self, toy):
        self.__toys.append(toy)

    def PlayAllToys(self):
        for t in self.__toys:
            t.play()
