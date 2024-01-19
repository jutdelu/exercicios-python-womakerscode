'''Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, uma dolescente,
adulto ou idoso.'''
idade = int(input('Digite a idade da pessoa: '))
if (idade <= 12) :
    print('É uma criança.')
elif (idade > 12) and (idade <=18):
    print('É um adolescente.')
elif (idade >=19) and (idade < 60):
    print('É um adulto')
else:
    print('É um idoso.')