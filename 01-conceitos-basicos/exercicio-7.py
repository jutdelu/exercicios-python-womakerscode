'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal(IMC) usando a fórmula: IMC=peso/(altura x altura).'''
#entrada
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
#processamento
imc = peso / ( altura * altura )
#saída
print(f'O IMC é: {imc:.2f}')