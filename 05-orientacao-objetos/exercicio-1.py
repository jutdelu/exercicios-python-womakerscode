'''Exercícios Classes e Objetos
1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe.'''

#Definição da classe
class Carro: 
    def __init__(self):
        self.ligado = False
        self.cor = 'Azul'
        self.modelo = 'Fusca'
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 95
    
    def ligar_carro(self):
        self.ligado = True

    def desligar_carro(self):
        self.ligado = False

    def acelelar(self):
        if not self.ligado:
            return
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += 5
    
    def frear(self):
        if not self.ligado:
            return
        
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 5

    def __str__(self) -> str:
        return f'Fusca - ligado {self.ligado} - velocidade {self.velocidade}'

#Criando instância da classe carro
fusca_um = Carro()
fusca_dois = Carro()

#Alterando o estado do fusca_um
fusca_um.ligar_carro()
print('fusca_um está ligado? {}'.format(fusca_um.ligado))
print('fusca_dois está ligado? {}'.format(fusca_dois.ligado))
print()
#Desligando fusca_um, ligando fusca_dois e acelerando ele
fusca_um.desligar_carro()
fusca_dois.ligar_carro()

print('fusca_um está ligado? {}'.format(fusca_um.ligado))
print('fusca_dois está ligado? {}'.format(fusca_dois.ligado))
print()

for _ in range (3):
    fusca_dois.acelelar()

print('fusca_um velocidade: {}'.format(fusca_um.velocidade))
print('fusca_dois velocidade: {}'.format(fusca_dois.velocidade))
print()

#freando o fusca
for _ in range (3):
    fusca_dois.frear()

#utilizando __str__ para representação em string
print('fusca um: ', fusca_um)
print('fusca dois: ', fusca_dois)