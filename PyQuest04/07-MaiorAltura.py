#   Nome e altura
qntd = 0
maior_altura = 0
maior_nome = ''
while True:
    nome = input('Insira o nome: ')
    altura = float(input('Insira a altura em metros: '))
    nome = nome.capitalize()
    if altura < 0:
        print('Altura nao pode ser negativa.')
        qntd -= 1
    elif altura > maior_altura:  # Se altura atual for maior que antiga, antiga = atual.
        maior_altura = altura
        maior_nome = nome
    qntd+=1 # Incrementa contador
    if qntd == 3: # Limite pessoas
        break
print('{} e o mais alto do grupo, medindo {:.2f} metros!'.format(maior_nome, maior_altura))