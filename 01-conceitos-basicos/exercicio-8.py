'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.'''
#entrada
ganho_por_hora = float(input('Digite quanto ganha por hora: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
#processamento
total_salario = ganho_por_hora*horas_trabalhadas
#saida
print(f'O salário no referido mês foi R$ {total_salario:.2f}')
