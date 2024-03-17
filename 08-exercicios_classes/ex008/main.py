from monkey import Monkey
from cannibal_monkey import CannibalMonkey

m1 = Monkey("Cesar")
m2 = Monkey("Morrice")

mc = CannibalMonkey("Hannibal")

m1.to_eat("banana")
m1.to_eat("bread")
m1.to_eat("meet")

m2.to_eat("pasta")
m2.to_eat("apple")

m1.getStomach()
m2.getStomach()

m1.digest()
m2.digest()

m1.getStomach()
m2.getStomach()

mc.to_eat(m1)
mc.to_eat(m2)

mc.getStomach()

mc.digest()