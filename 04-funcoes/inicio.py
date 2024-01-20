num1 = int(input('numero um:'))
num2 = int(input('numero dois:'))

def soma(num1,num2):

    calculo = num1+num2 #funcoes e variaveis não pode ter o mesmo nome
    file = 'arquivo.txt'
    #open
 
    #abertura para escrita
    arquivo_escrita = open(file, 'w')
    arquivo_escrita.write(f'O resultado da soma é {calculo}')
    arquivo_escrita.close()
    
    #abertura de arquivos binários
    #arquivo_binario = open(file, 'wb')
    
    #leitura
    #abertura para leitura
    arquivo_leitura = open(file, 'r')
    leitura = arquivo_leitura.read()
    print(leitura)



def subtracao(num1,num2):
    sub = num1-num2
    print(f'o resultado da subtração é {sub}')
    soma(num1,num2)


soma(num1,num2)
