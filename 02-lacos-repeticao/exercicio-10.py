'''10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.'''
lista = []
for i in range(3):
    elemento = int(input('Digite um número: '))
    lista.append(elemento)
lista.sort() #ordena os elementos
print(lista)