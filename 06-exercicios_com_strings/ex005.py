"""Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida. 
FULANO
FULAN
FULA
FUL
FU
F
"""

name = input("enter your name: ")
count = 0 

for item in range(0, len(name)):
    print(name[0:len(name) - count])
    count += 1