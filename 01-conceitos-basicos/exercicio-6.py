'''Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião,carro e ônibus. Levando em consideração: ●avião=600km/h ●carro=100km/h ●ônibus=80km/h'''
#entrada
distancia = float(input('Digite a distância percorrida: '))
velocidade = float(input('Digite a velocidade do veículo: '))
#processamento 
tempo_viagem = distancia/velocidade * 60
tempo_aviao = distancia/600 * 60
tempo_carro = distancia/100 * 60
tempo_onibus = distancia/80 * 60
#saida
print('Comparativo: ')
print(f'Tempo de viagem: {tempo_viagem:.2f} minutos''\n'f' de avião: {tempo_aviao:.2f} minutos''\n'f' de carro: {tempo_carro:.2f} minutos''\n'f' de ônibus: {tempo_onibus:.2f} minutos')
