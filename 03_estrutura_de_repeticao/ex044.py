"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são: 

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. 
"""

votes = {1: {"especification": "candidate1", "votes": 0}, 
         2: {"especification": "candidate2", "votes": 0}, 
         3: {"especification": "candidate3", "votes": 0},
         4: {"especification": "candidate4", "votes": 0},
         5: {"especification": "nullVote", "votes": 0},
         6: {"especification": "whiteVote", "votes": 0}}

total = 0
null = 0
white = 0

print("1 - candidate1\n2 - candidate2\n3 - candidate3\n4 - candidate4\n5 - null vote\n6 - white vote\n")

while True:

    vote = int(input("Who does your vote go to? "))
    total += 1

    if vote == 5:
        null += 1

    if vote == 6:
        white += 1

    if vote == 0:
        break

    if vote not in votes:
        print("invalid vote")
    else:
        votes[vote]["votes"] += 1


        
print("\ntotal of votes")
for index in votes:
    print(f"{votes[index]["especification"]} = {votes[index]["votes"]:.0f} vote(s)")

print(f"{(null/total)*100:.0f}% null votes\n{(white/total)*100:.0f}% white votes")