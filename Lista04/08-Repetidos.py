# Funcoes
def linha(espaco, titulo, dupla):  # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if (titulo != ' ') and (dupla != 0):
        print(titulo)
        print('-='*espaco)
    elif (titulo != ' ') and (dupla == 0):
        print(titulo)


# Codigo principal
maior = 0
listpos = []
numeros = [int(input(f'Numero na posicao {i+1}: ')) for i in range(9)]  # Criando lista utilizando compreensao de listas
for num in range(3):
    if numeros[num] > maior:
        maior = numeros[num]
rpts = numeros.count(maior)  # Contando quantas vezes o maior se repete
linha(20, f'Maior numero: {maior}', 0)
for n in range(9):
    if numeros[n] == maior:
        listpos.append(n)
linha(20, f'Se repete {rpts} vezes nas posicoes {listpos}', 1)
    
