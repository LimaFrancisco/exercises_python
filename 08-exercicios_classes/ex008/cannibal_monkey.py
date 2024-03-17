from monkey import Monkey

class CannibalMonkey(Monkey):
    def __init__(self, name):
        super().__init__(name)

    def to_eat(self, food):
        self.stomach.append(food)
        
    def digest(self):

        for item in self.stomach:
            del item 
        # self.stomach.clear()
    
    def getStomach(self):
        print(f"{self.name}`s stomach:")

        if len(self.stomach) == 0:
            print("empty") 

        for food in self.stomach:
            print(food.name)