'''Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de 
vogais na string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar 
as vogais.'''

import re
from collections import Counter
def vogais(x):
    return Counter(re.sub('[^aeiouAEIOU]', '', x))


print(vogais('Juliana'))