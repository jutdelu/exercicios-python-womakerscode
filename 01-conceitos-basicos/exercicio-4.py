'''Receba do usuário a quantidade de litros de combustível consumidos e adistância percorrida. Calcule e imprima o consumo médio em km/l.'''
#entrada
litros_combustivel = float(input('Digite quantos litros foram consumidos: '))
distancia = float(input('Digite a km percorrida: '))
#processamento
consumo_medio = distancia/litros_combustivel
#saida
print (f'O consumo médio foi de {consumo_medio:.2f} km/l.')