from store import Store
from toy import Toy
from ball import Ball

t1 = Toy()
t1.price = 50
t1.color = "black"

b1 = Ball()
b1.price = 40
b1.color = "blue"
b1.material = "rubber"
b1.radius = 25

s = Store()
s.addToy(t1)
s.addToy(b1)

s.PlayAllToys()
