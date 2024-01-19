'''Crie um dicionário representando contatos (nome,telefone). Permita ao usuário procurar por um contato pelo nome'''
agenda_telefone = {'Juliana': 123456789, 'Letícia': 321654987, 'Junior': 123789456}
contato = input('Digite o nome: ')
if contato in agenda_telefone:
    print(agenda_telefone[contato])