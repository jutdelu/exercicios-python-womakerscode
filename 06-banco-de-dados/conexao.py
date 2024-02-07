import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

'''Exercícios Banco de Dados 
1.Crie uma tabela chamada "alunos" com os seguintes campos:id(inteiro), nome(texto), idade(inteiro) e curso(texto). '''

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Juliana", 30, "TADS"), (2, "Pedro", 33, "Letras Português"), (3, "Rafael", 29, "Sistema de Informação"), (4, "Ana", 26, "TADS"), (5, "Letícia", 34, "Medicina")')

'''3.Consultas Básicas 
Escreva consultas SQL para realizar as seguintes tarefas:'''

#a) Selecionar todos os registros da tabela "alunos". 
# dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20anos.
# dados = cursor.execute('SELECT * FROM alunos WHERE idade > 20')
# for alunos in dados:
#     print(alunos)    

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
# dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia"')
# for alunos in dados:
#     print(alunos)  

#d) Contar o número total de alunos na tabela 
# dados = cursor.execute('SELECT COUNT(*) FROM alunos')
# print(dados)  #fazer tratamento to str

'''4.Atualização e Remoção 
a)Atualize a idade de um aluno específico na tabela.'''

#cursor.execute('UPDATE alunos set idade= 34 WHERE nome = "Pedro"')

#b)Remova um aluno pelo seu ID.

#cursor.execute('DELETE FROM alunos WHERE id = 2')

'''5.Criar uma Tabela e Inserir Dados 
Crie uma tabela chamada "clientes" com os campos: id(chave primária), nome(texto), idade(inteiro) e saldo(float).
Insira alguns registros de clientes na tabela.'''

#cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Mariana", 30, 20.00), (2, "Godofredo", 33, 50.00), (3, "Manuel", 29, 20.00), (4, "Ana", 26, 10.00), (5, "Felícia", 34, 40.00)')

'''6.Consultas e Funções Agregadas 
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superiora 30 anos.
b) Calcule o saldo médio dos clientes. 
c) Encontre o cliente como saldo máximo.
d)Conte quantos clientes têm saldo acima de 1000.

7. Atualização e Remoção com Condições 
a) Atualize o saldo de um cliente específico. 
b) Remova um cliente pelo seu ID.

8. Junção de Tabelas Crie uma segunda tabela chamada "compras" com os campos: id(chaveprimária), cliente_id(chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.'''

# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT')
#cursor.execute('DROP TABLE usuario')

# dados = cursor.execute('SELET * FROM usuario')
# for usuario in dados:
#     print(usuario)

conexao.commit()
conexao.close