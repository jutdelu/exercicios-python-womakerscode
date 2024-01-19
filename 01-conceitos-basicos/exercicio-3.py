'''Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.'''
# entrada
kilometros = float(input('Digite a quantidade de kilômetros: '))
#processamento
metros = kilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10
#saída
print('A conversão fica: ')
print(f'kilometros: {kilometros:.2f} ''\n'f'metros: {metros:.2f} ''\n'f'centímetros: {centimetros:.2f} ''\n'f'milímetros: {milimetros:.2f}')