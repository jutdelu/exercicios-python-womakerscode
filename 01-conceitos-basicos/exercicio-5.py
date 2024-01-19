'''Escreva um programa que calcule o salário líquido.Lembrando de declarar o salário bruto e o percentual de descontodo Impostode Renda.'''
#entrada
salario_bruto = float(input('Digite o salário bruto: '))
percentual = float(input('Digite o percentual de desconto do IR: '))
#processamento
salario_liquido = salario_bruto - salario_bruto * (percentual/100)
#saida
print(f'O salário líquido é {salario_liquido:.2f}')