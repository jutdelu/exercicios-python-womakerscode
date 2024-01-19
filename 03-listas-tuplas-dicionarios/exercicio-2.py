'''Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.'''
aluno_x = []
media_alunos = []

print('Cálculo de média de cinco alunos')
for alunos in range (5):  
    for nota in range (4):
        nota = float(input('Digite uma nota para o aluno: '))
        aluno_x.append(nota)
    print('As notas do aluno são: {}'.format(aluno_x))
    media_aluno_x = sum(aluno_x)/len(aluno_x)
    print('A média do aluno é: {} '.format(media_aluno_x))
    aluno_x.clear()
    if media_aluno_x >= 7:
        media_alunos.append(media_aluno_x)
print('Número alunos com média maior ou igual a 7.0 é: {}'.format(len(media_alunos)))