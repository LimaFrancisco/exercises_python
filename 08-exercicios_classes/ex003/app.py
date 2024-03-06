from math import ceil

from rectangle import rectangle

base = float(input("what is the size of the base? "))
height = float(input("what is the size of the height? "))

local = rectangle(base, height)

ceramicFloor = rectangle(0.56, 0.32) # most common sizes

addition = ceramicFloor.area() * 0.1

final_calculation = ceil((local.area() / ceramicFloor.area()) * addition) + (local.area() / ceramicFloor.area())

print(f"\nyou need to pay {ceil(final_calculation):.0f} ceramics for your floor")