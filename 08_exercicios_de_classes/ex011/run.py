from model import Carro

meuFusca = Carro(15)                        # 15 quilômetros por litro de combustível.       

meuFusca.adicionar_gasolina(20)             # abastece com 20 litros de combustível.            
meuFusca.andar(100)                         # anda 100 quilômetros.
print(meuFusca.obter_gasolina())            # Imprime o combustível que resta no tanque.