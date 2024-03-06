class rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def changeSides(self, newBase, newHeight):
        self.base = newBase
        self.height = newHeight

    def showSides(self):
        print(f"base: {self.base:.2f}\n: {self.height:.2f}")

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * (self.base + self.height)