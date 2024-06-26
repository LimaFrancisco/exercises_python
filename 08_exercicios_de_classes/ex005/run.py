from models import ContaCorrente

cc = ContaCorrente(1234, 'Fernando')
print(cc.mostrar_dados())

cc.alterar_nome('Felipe')
cc.sacar(200)
cc.depositar(500)
print(cc.mostrar_dados())
