'''O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. 
O processo de leitura deve ser encerrado quando o usuário informar o valor zero. Certifique-se de incluir 
validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.'''
CONTADOR_IMPAR = 0
CONTADOR_PAR = 0
numero = int(input('Digite um número diferente de zero e positivo: '))
while (numero != 0) and (numero > 0) :
    if numero %2 == 0:
        CONTADOR_IMPAR += 1
        numero = int(input('Digite um número diferente de zero e positivo: '))
    else:
        CONTADOR_PAR +=1
        numero = int(input('Digite um número diferente de zero e positivo: '))
print(f'Foram digitados {CONTADOR_IMPAR} números ímpares.')
print(f'Foram digitados {CONTADOR_PAR} números pares.')
print('Programa encerrado por ter digitado zero ou número negativo.')