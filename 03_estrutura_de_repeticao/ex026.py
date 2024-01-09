"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. """

cand1 = 0
cand2 = 0
cand3 = 0

voters = int(input("enter the number of voters: "))

for index in range(0, voters):
    vote = int(input("which candidate do you want to cast your vote for?\n1 - for candidate 1\n2 - for candidate 2\n3 - for candidate 3\n"))

    match vote:

        case 1:
            cand1 += 1
        case 2:
            cand2 += 1
        case 3:
            cand3 += 1
        case _:
            print("candidate not found")
        
print(f"\ncounting of votes:\ncandidate 1 --------------- {cand1:.0f} vote(s)\ncandidate 2 --------------- {cand2:.0f} vote(s) \ncandidate 3 --------------- {cand3:.0f} vote(s)")
