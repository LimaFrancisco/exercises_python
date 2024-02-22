"""Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada. 
F
FU
FUL
FULA
FULAN
FULANO
"""

brokenName = ""
name = input("enter your name: ")

for item in name:
    brokenName += item
    print(brokenName)