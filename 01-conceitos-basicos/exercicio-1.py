'''Faça um Programa que peça três números,realize as principais operações 
soma,subtração, multiplicação, divisão'''
#entrada
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Adivinha...digita mais um número: '))
#processamento
soma = numero1 + numero2 + numero3
subtracao = numero1 - numero2 - numero3
multiplicacao = numero1 * numero2 * numero3
divisao = numero1 / numero2 / numero3
#saída
print(f'A soma dos números é: {soma}, a subtração: {subtracao}, a multiplicação: {multiplicacao} e a divisão: {divisao:.2f}.')