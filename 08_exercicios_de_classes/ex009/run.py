from models import Retangulo
from models import Ponto

retangulo1 = Retangulo(4.5, 9.8)
retangulo2 = Retangulo(3.3, 5.7)

print(f'Base do Retangulo: {retangulo1.get_base():.1f}')
print(f'Altura do Retangulo: {retangulo1.get_altura():.1f}')
centro = retangulo1.get_centro()
print(f'Centro do retangulo:\nx:{centro.get_x():.1f}\ny:{centro.get_y():.1f}\n\n')

base = float(input('Informe a nova base para o retangulo: '))
altura = float(input('Informe a nova altura para o retangulo: '))

retangulo1.set_base(base)
retangulo1.set_altura(altura)

print(f'Base do Retangulo: {retangulo1.get_base():.1f}')
print(f'Altura do Retangulo: {retangulo1.get_altura():.1f}')
centro = retangulo1.get_centro()
print(f'Centro do retangulo:\nx:{centro.get_x():.1f}\ny:{centro.get_y():.1f}')
