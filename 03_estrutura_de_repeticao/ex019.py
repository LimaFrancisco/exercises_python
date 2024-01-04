"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000"""

n = int(input("enter a quantity of numbers: "))

list = []

for index in range(0, n):
    num = int(input("inform a number: "))

    while num < 0 or num > 1000:
        num = int(input("inform a number: "))
    
    list.append(num)

bigger = list[0]
smaller = list[0]

for index in range(0, n):
    if list[index] > bigger:
        bigger = list[index]

    if list[index] < smaller:
        smaller = list[index]

print(f"bigger: {bigger}\nsmaller: {smaller}\nsum: {bigger + smaller}")