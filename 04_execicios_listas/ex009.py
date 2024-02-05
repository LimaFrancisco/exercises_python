"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor. """

nums = []
square_sum = 0

for index in range(0, 10):

    try:
        nums.append(int(input("enter an integer: ")))
        square_sum +=  nums[index] ** 2

    except ValueError:
        print("invalid value")

    
print(f"The sum of the squares of the numbers is: {square_sum:.0f}")