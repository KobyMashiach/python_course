from toy import Toy


class Ball(Toy):
    def __init__(self):
        self.radius = 0
        self.material = ""

    def play(self):
        print("playing the ball")

    def buy(self):
        print("buying the ball")
