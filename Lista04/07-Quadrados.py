# Funcoes
def linha(espaco, titulo):  # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if titulo != ' ':
        print(titulo)
        print('-='*espaco)


# Codigo principal
quadrados = []
numeros = [int(input(f'Numero na posicao {i+1}: ')) for i in range(5)]  # Criando lista utilizando compreensao de listas
i = 0
for i in numeros:
    index = numeros.index(i)
    quadrados.append(numeros[index]**2)
linha(25, f'{quadrados}')
