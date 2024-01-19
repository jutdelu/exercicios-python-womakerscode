'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.'''

nota = int(input('Digite uma nota de 1 a 10: '))
while nota not in range(1,11):
    nota = int(input('Número inválido, digite outro número: '))
print('Nota válida.')

# nota = int(input('Digite uma nota de 1 a 10: '))
# while nota > 10:
#     nota = int(input('Número inválido, digite outro número: '))
# print('Nota válida.')