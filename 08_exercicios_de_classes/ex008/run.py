from models import Macaco, MacacoCanibal

macaco1 = Macaco('Ape')
macaco2 = Macaco('Kong')
macaco3 = Macaco('Abu')

macaco1.comer('Banana')
macaco1.comer('Manga')
macaco1.comer('Maçã')

print(macaco1.mostrar_bucho())
macaco1.digerir()
print(macaco1.mostrar_bucho())


macaco_canibal = MacacoCanibal('Hannibal')
macaco_canibal.comer(macaco1)
macaco_canibal.comer(macaco2)
macaco_canibal.comer(macaco3)
print(macaco_canibal.mostrar_bucho())

macaco_canibal.digerir()

print(macaco_canibal.mostrar_bucho())
