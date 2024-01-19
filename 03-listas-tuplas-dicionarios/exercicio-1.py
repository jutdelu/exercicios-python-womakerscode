'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
""Telefonou para  avítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa 
responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice""
e 5 como ""Assassino"". Caso contrário, ele será classificado como ""Inocente"".'''
print('Responda com "sim" ou "não":')
respostas_positivas = []
resposta = input('Telefonou para a vítima? ').upper()
if resposta == 'SIM':
    respostas_positivas.append(resposta)
resposta = input('Esteve no local do crime? ').upper()
if resposta == 'SIM':
    respostas_positivas.append(resposta)
resposta = input('Mora perto da vítima? ').upper()
if resposta == 'SIM':
    respostas_positivas.append(resposta)
resposta = input('Devia para a vítima? ').upper()
if resposta == 'SIM':
    respostas_positivas.append(resposta)
resposta = input('Já trabalhou com a vítima? ').upper()
if resposta == 'SIM':
    respostas_positivas.append(resposta)
if len(respostas_positivas) == 2:
    print('A pessoa é suspeita.')
elif len(respostas_positivas) in range(3,5):
    print('A pessoa é cúmplice.')
elif len(respostas_positivas) == 5:
    print('A pessoa é assassina.')
else:
    print('A pessoa é inocente.')
