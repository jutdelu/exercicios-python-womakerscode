'''Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. 
Calcule o total do carrinho de compra.'''
carrinho_lista = []
carrinho_compras = {'Banana': 10, 'Maçã': 11}
carrinho_compras['Pera'] = 12
carrinho_compras['Uva'] = 13
entrada_carrinho = input('Digite o produto e o valor, separado por espaço: ')
entrada_carrinho = entrada_carrinho.split(' ')
carrinho_compras[entrada_carrinho[0]] = int(entrada_carrinho[1])
print(carrinho_compras)

for i in carrinho_compras.values():
    carrinho_lista.append(i)
print(sum(carrinho_lista))
