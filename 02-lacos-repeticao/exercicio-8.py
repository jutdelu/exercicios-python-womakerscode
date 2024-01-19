'''Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para 
determinar o maior entre ele se apresente o resultado.'''
numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
numero3 = int(input('Digite o número 3: '))
if (numero1 > numero2) and (numero1 > numero3):
    print(f'O maior número é o {numero1}')
elif (numero2 > numero1) and (numero2 > numero3):
    print(f'O maior número é o {numero2}')
else:
    print(f'O maior número é o {numero3}')