'''Solicite ao usuário o número de horas de exercício físico por semana.Calcule o total de calorias queimadas em um mês,considerando uma média de 5 calorias por minuto de exercício.'''
#entrada
horas_exercicio_semana = int(input('Digite o número de horas de exercício semanal: '))
#processamento
horas_exercicio_mes = horas_exercicio_semana * 4
queima_calorica = 5 * 60 * horas_exercicio_mes
#saida
print(f'A queima calórica mensal foi de {queima_calorica} calorias.')