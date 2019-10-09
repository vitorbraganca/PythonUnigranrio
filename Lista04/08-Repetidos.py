# Funcoes
def linha(espaco, titulo, dupla):  # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if (titulo != ' ') and (dupla != 0):
        print(titulo)
        print('-='*espaco)
    elif (titulo != ' ') and (dupla == 0):
        print(titulo)


# Codigo principal
numeros = [int(input(f'Numero na posicao {i+1}: ')) for i in range(9)]  # Criando lista utilizando compreensao de listas
numeros.sort()  # Organizando a lista na ordem
maior = numeros[-1]  # Buscando o maior numero na ultima posicao do vetor
rpts = numeros.count(maior)  # Contando quantas vezes o maior se repete
pos = numeros.index(maior)  # Buscando em qual posicao do vetor ele se repete
linha(20, f'Maior numero: {maior}', 0)
if rpts > 1:
    linha(20, f'Se repete {rpts} vezes nas posicoes {(pos+1)} ate {pos+rpts}', 1)
else:
    linha(20, f'Se repete {rpts} vez na posicao {pos+1}', 1)
