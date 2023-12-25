"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. """

product1 = float(input("enter a price of a product: ")) 
product2 = float(input("enter the price of another product: "))
product3 = float(input("enter a price of another product: "))

if product1 < product2 and product1 < product3:
    print(f"{product1} is lowest price")
elif product2 < product3 and product2 < product1:
    print(f"{product2} is lowest price")
elif product3 < product2 and product3 < product1:
    print(f"{product3} is lowest price")