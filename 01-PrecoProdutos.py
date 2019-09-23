# preco 10 produtos
compras = [   ]
soma = 0.0
while True:
    produto = input('Nome do produto (digite FIM para encerrar): ')
    produto = produto.upper()
    if produto == 'FIM':    break
    qntd = int(input('Quantidade: '))
    preco = float(input('Valor do produto: '))
    compras.append([produto, qntd, preco])
    soma += preco*qntd
print('Lista de compras: PRODUTO | QUANTIDADE | VALOR UNITARIO:')
print(compras)
print('Valor total dos produtos: {:.2f}'.format(soma))
