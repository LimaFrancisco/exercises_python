"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. """

def sum_tax(tax_rate, cost):
    return cost + (cost * (tax_rate / 100))

try:
    price = float(input("enter the cost: "))
    tax = float(input("enter the tax: "))


    print(sum_tax(tax, price))

except ValueError:
    print("invalid data type")