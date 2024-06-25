from models import Retangulo

base = float(input('Informe a base para o retangulo: '))
altura = float(input('Agora informe a altura: '))

retangulo = Retangulo(base, altura)

print(f'{retangulo.calcular_area():.2f} m² de piso deve ser comprado.')

print(f'{retangulo.calcular_perimetro():.2f} metros de rodapés deve ser comprado.')
