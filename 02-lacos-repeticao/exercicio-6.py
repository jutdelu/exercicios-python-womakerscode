'''Crie um programa que solicite ao usuário um login e uma senha. 
O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123",
caso contrário imprima uma mensagem de erro.'''
login = input('Digite o login: ')
senha = input('Digite a senha: ')
while login != 'admin' and senha != 'admin123':
    print('Login ou senha incorretos.')
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
print('Acesso autorizado.')