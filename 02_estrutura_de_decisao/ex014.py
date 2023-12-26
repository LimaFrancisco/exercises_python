"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
 
 Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  
  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. """

grade1 = float(input("enter a fist student grade: "))
grade2 = float(input("enter a second student grade: "))

media = (grade1 + grade2) / 2

print("\naverage performace        concept ")

if media >= 0 and media < 4.0:
    print(f"{media:.1f}                       E              disapproved")
elif media >= 4.0 and media < 6.0:
    print(f"{media:.1f}                       D              disapproved")
elif media >= 6.0 and media < 7.5:
    print(f"{media:.1f}                       C              disapproved")
elif media >= 7.5 and media < 9.0:
    print(f"{media:.1f}                       B              approved")
elif media >= 9.0 and media < 10.0:
    print(f"{media:.1f}                       A              approved")