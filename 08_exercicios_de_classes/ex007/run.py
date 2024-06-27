from models import Tamagushi
from mostrador import Mostrador

tamagushi = Tamagushi('Mud', 3)
mostrador = Mostrador()

print(mostrador.exibir_tudo(tamagushi))

tamagushi.set_fome(25)
tamagushi.set_idade(5)
tamagushi.set_saude(35)
tamagushi.set_nome('Ted')
print(mostrador.exibir_tudo(tamagushi))

tamagushi.set_saude(10)
print(mostrador.exibir_tudo(tamagushi))

tamagushi.set_saude(50)
tamagushi.set_fome(50)
print(mostrador.exibir_tudo(tamagushi))
