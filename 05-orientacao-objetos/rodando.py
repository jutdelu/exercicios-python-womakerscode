from conta import Conta

maria = Conta("Maria", "F", "123456789", 1000)
print(maria.nome)
maria.depositar(1000)
maria.sacar(2000)
maria.verSaldo()