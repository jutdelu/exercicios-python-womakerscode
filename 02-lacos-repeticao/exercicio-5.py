'''Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e 
classifique-o comoe quilátero, isósceles ou escaleno. equilátero:todos os lados com o mesmo valor 
isósceles:dois lados com o mesmo valor escaleno:todos os lados com medidas distintas'''
lado_a = float(input('Digite o lado a: '))
lado_b = float(input('Digite o lado b: '))
lado_c = float(input('Digite o lado c: '))
if (lado_a == lado_b) and (lado_a == lado_c) :
    print('Equilatero')
elif (lado_a==lado_b) or (lado_a==lado_c) or (lado_b==lado_c):
    print('Isósceles')
else:
    print('Escaleno')