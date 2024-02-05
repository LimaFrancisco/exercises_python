"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. """

from math import prod

nums = []

sum_elements = 0
mult_elements = 0

for item in range(0, 5):
    try:
        nums.append(int(input("enter a value: ")))
    except ValueError:
        print("invalid value")

sum_elements = sum(nums) 
mult_elements = prod(nums)

print(f"\nall values: {nums}\nsum of values: {sum_elements:.0f}\nproduct of values: {mult_elements:.0f}")
