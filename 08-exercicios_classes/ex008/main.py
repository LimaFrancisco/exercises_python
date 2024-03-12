from monkey import Monkey

monkey1 = Monkey("Cesar")
monkey2 = Monkey("Maurice")

monkey1.to_eat("banana")
monkey1.to_eat("sandwish")
monkey1.to_eat("apple")

monkey1.getStomach()

monkey1.to_eat("cracker")
monkey1.digest()

monkey1.getStomach()

# monkey2.to_eat("banana")
# monkey2.to_eat("sandwish")
# monkey2.to_eat("apple")
# monkey2.to_eat("cracker")

# monkey2.getStomach()