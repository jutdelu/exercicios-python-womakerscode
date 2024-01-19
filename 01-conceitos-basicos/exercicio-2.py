'''Peça ao usuário para informar o ano de nascimento. Em seguida,calcule e imprima a idade atual.'''
#entrada
from datetime import date
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
#processamento
idade = ano_atual - ano_nascimento
#saída
print(f'Você tem ou fará {idade} anos, esse ano.')