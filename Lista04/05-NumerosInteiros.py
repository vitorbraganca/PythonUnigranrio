# Funcoes
def linha(espaco, titulo):  # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if titulo != ' ':
        print(titulo)
        print('-='*espaco)


# Codigo principal
numeros = []  # Vetor para os numeros
for i in range(10):
    num = int(input(f'Digite um numero na posicao {i+1}: '))  # Lendo numero inteiro
    numeros.append(num)  # Adicionando numero na lista
numeros.sort()  # Organizando a lista em ordem crescente
linha(25, f'Ordem crescente: {numeros}')
numeros.sort(reverse = True)  # Organizando a lista em ordem decrescente
linha(25, f'Ordem decrescente: {numeros}')
