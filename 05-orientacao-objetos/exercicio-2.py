from abc import ABC, abstractmethod


class AbstractConta(ABC):
    def _init_(self, saldo: float = 0, renda_mensal: float = 0) -> None:
        self.__saldo = saldo
        self.__renda_mensal = renda_mensal

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def renda_mensal(self) -> float:
        return self.__renda_mensal

    def depositar(self, valor) -> None:
        self.__saldo += valor
        print("Deposito realizado com sucesso")
        print(f"Seu atual saldo é R${self.__saldo:.2f}")

    def verSaldo(self) -> None:
        if self.__saldo > 0:
            print(f"Seu saldo atual é R${self.__saldo:.2f}")
        else:
            print(f"Seu saldo atual é -R${abs(self.__saldo):.2f}")

    @abstractmethod
    def sacar(self, valor) -> None:
        ## Sabendo que existe tipo diferente de regras para sacar de acordo com o sexo do cliente
        ...


class ContaMulher(AbstractConta):
    def _init_(self, saldo: float = 0, renda_mensal: float = 0) -> None:
        super()._init_(saldo, renda_mensal)

    def sacar(self, valor) -> None:
        if self.AbstractContasaldo + self._AbstractConta_renda_mensal >= valor:
            self.AbstractConta_saldo -= valor
            print(f"Saque realizado com sucesso, valor de R${valor}")
            if self.AbstractConta_saldo > 0:
                print(f"Seu saldo é R${self.AbstractConta_saldo:.2f}")
            else:
                print(f"Seu saldo é -R${abs(self.AbstractConta_saldo):.2f}")
        else:
            print("Saldo insuficiente")
            if self.AbstractConta_saldo > 0:
                print(f"Seu saldo é R${self.AbstractConta_saldo:.2f}")
            else:
                print(f"Seu saldo é -R${abs(self.AbstractConta_saldo):.2f}")


class ContaHomem(AbstractConta):
    def _init_(self, saldo: float = 0, renda_mensal: float = 0) -> None:
        super()._init_(saldo, renda_mensal)

    def sacar(self, valor) -> None:
        if self.AbstractConta_saldo >= valor:
            self.AbstractConta_saldo -= valor
            print(f"Saque realizado com sucesso, valor de R${valor}")
            if self.AbstractConta_saldo > 0:
                print(f"Seu saldo é R${self.AbstractConta_saldo:.2f}")
            else:
                print(f"Seu saldo é -R${abs(self.AbstractConta_saldo):.2f}")
        else:
            print("Saldo insuficiente")
            if self.AbstractConta_saldo > 0:
                print(f"Seu saldo é R${self.AbstractConta_saldo:.2f}")
            else:
                print(f"Seu saldo é -R${abs(self.AbstractConta_saldo):.2f}")


class Cliente:
    def _init_(
        self,
        nome: str,
        sexo: str,
        telefone: str = "",
        renda_mensal: float = 0,
        saldo: float = 0,
    ) -> None:
        self.__nome = nome
        self.__sexo = sexo
        self.__telefone = telefone
        self.__renda_mensal = renda_mensal
        if self.__sexo == "F":
            self.__conta = ContaMulher(saldo, renda_mensal)
        else:
            self.__conta = ContaHomem(saldo, renda_mensal)

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None:
        self.__nome = valor

    @property
    def sexo(self) -> str:
        return self.__sexo

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, valor: str) -> None:
        self.__telefone = valor

    @property
    def renda_mensal(self) -> float:
        return self.__renda_mensal

    @renda_mensal.setter
    def renda_mensal(self, valor: float) -> None:
        self.__renda_mensal = valor

    def verSaldo(self) -> None:
        self.__conta.verSaldo()

    def sacar(self, valor):
        self.__conta.sacar(valor)

    def depositar(self, valor):
        self.__conta.depositar(valor)


class Conta(Cliente):
    def _init_(self, *args):
        super()._init_(*args)
