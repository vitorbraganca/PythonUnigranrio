# Funcoes
def linha(espaco, titulo):  # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if titulo != ' ':
        print(titulo)
        print('-='*espaco)


# Codigo principal
pstvs = ngtvs = nls = 0  # Criando variaveis para armazenar os "tipos" de numeros
numeros = [int(input(f'Numero na posicao {i+1}: ')) for i in range(10)]  # Criando lista utilizando compreensao de listas
for num in numeros:
    if num > 0:  # Numeros positivos
        pstvs += 1
    elif num < 0:  # Numeros negativos
        ngtvs += 1
    else:  # Numeros nulos
        nls += 1

linha(37, f'Total de {pstvs+ngtvs+nls} numeros inseridos. Sendo {pstvs} positivos, {ngtvs} negativos e {nls} nulos.')
