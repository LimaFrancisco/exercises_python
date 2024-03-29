"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso"""

installments = []
flag = None

def paymentAmount(value, delayed_days):
    final_value = value + (value * 0.03) + ((value * 0.01) * delayed_days)
    return final_value

while flag != 0:

    try: 
        value = float(input("inform the value of the installment:(end=0) "))
        delayed_days = int(input("number of days in arrears: "))
    except ValueError:
        print("invalid data type")

    if value > 0:
        installments.append(paymentAmount(value, delayed_days))
    else:
        flag = 0

print("\ninstallment report")
for index in range(0, len(installments)):
    print(f"{index + 1} - R$ {installments[index]:.2f}")