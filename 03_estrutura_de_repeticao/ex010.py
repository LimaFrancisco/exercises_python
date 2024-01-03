"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. """

num1 = int(input("enter a integer: "))
num2 = int(input("enter another integer: "))

start = 0
end = 0

if num1 > num2:
    start = num2 + 1
    end = num1
elif num2 > num1:
    start = num1 + 1
    end  = num2

for index in range(start, end):
    print(index)