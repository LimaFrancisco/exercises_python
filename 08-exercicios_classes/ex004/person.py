class person:

    def __init__(self, name, age, weight, height):

        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


    def getting_older(self):
        
        if self.age < 21:
            self.height += 0.5

        self.age += 1

    def fatten(self):
        self.weight += 1
    
    def to_lose_weight(self):
        self.weight -= 1

    def grow(self):
        self.height += 1