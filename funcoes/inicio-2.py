def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)

    except ZeroDivisionError:
        print('Erro: impossível dividir um valor por zero')
    except TypeError as e:
        print(f'Erro: tipo de dado informado está incorreto. \n Detalhes: {e} ')
    else:
        print('Sem exceções')

divisao(10,'womakerscode')