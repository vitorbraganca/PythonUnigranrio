# preco 10 produtos

def linha():
    print('=' * 55)


compras = []
cont, soma = 0, 0.00

while cont <= 9:
    produto = input('Nome do produto (digite FIM para encerrar): ')
    produto = produto.upper()
    if produto == 'FIM': break
    qntd = int(input('Quantidade: '))
    preco = float(input('Valor do produto: '))
    compras.append([produto, qntd, preco])
    cont += 1
soma = 0.0
linha()
print('                   Lista de compras')
linha()
for compra in compras:
    print("%20s x%5d %5.2f %6.2f"
          % (compra[0],  # Nome produto
             compra[1], compra[2],  # Quantidade e preco unitario
             compra[1] * compra[2]))  # Preco parcial
    soma += compra[1] * compra[2]
linha()
print('Valor total dos produtos: {:.2f}'.format(soma))
