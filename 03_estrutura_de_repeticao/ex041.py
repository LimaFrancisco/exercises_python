"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

    Os juros e a quantidade de parcelas seguem a tabela abaixo:

    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25

    Exemplo de saída do programa:

    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67"""

installments = 3
fees = 10

debt = float(input("what is the debt value? "))

print("\ndebt value    interest amount   number of installments installment value")
print(f"R$ {debt:.2f}    0                 1                      R$ {debt:.2f}")

for index in range(0, 4):

    addition = (debt * (fees / 100))

    print(f"R$ {debt + addition:.2f}    {addition:.2f}            {installments:.0f}                      R$ {(debt + addition) /installments:.2f}")

    installments += 3
    fees += 5