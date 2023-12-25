"""Faça um Programa que leia três números e mostre o maior deles. """

num1 = int(input("enter a number: ")) 
num2 = int(input("enter other number: "))
num3 = int(input("enter other number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the bigger")
elif num2 > num3 and num2 > num1:
    print(f"{num2} is the bigger")
elif num3 > num2 and num3 > num1:
    print(f"{num3} is the bigger")