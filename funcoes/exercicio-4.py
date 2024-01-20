'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda 
estrangeira. Considere a tabela de conversão abaixo: 
Dólar Americano: R$4,91 
Peso Argentino: R$0,02 
Dólar Australiano: R$3,18 
Dólar Canadense: R$3,64
Franco Suiço: R$0,42 
Euro: R$ 5,36 
Libra esterlina: R$6,21'''

def converte_moeda(a):
    dolar_americano = 4.91 * a 
    peso_argentino = 0.02 * a  
    dolar_australiano = 3.18 * a  
    dolar_canadense = 3.64 * a 
    franco_suico = 0.42 * a  
    euro = 5.36 * a  
    libra_esterlina = 6.21 * a 
    print(f'O valor em reais R${a:.2f} é: \n em dólar americano é R$ {dolar_americano:.2f}; \n em peso argentino R$ {peso_argentino:.2f}; \n em dolar australiano R$ {dolar_australiano:.2f}; \n em dólar canadense R$ {dolar_canadense:.2f}; \n em franco suíço R$ {franco_suico:.2f}; \n em euro R$ {euro:.2f}; \n em libra esterlina R${libra_esterlina:.2f}.')

converte_moeda(a=float(input('Digite uma valor em reais: ')))