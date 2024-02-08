"""Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores: 
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante 
"""

gross_sales = [3000, 5000, 7000, 2500, 6000, 8000, 3500, 1500, 9000, 4000]

count = [0]*9

for sales in gross_sales:
    salary = 200 + 0.09 * sales
    if salary < 1000:
        index = int(salary / 100) - 2
    else:
        index = 8
    count[index] += 1

for i in range(8):
    print(f'salespeople with salaries between ${100*(i+2)} and ${100*(i+3)-1}: {count[i]}')
print(f'Salespeople with salary from $1000 onwards: {count[8]}')
