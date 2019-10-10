# Funcoes
def linha(espaco, titulo, dupla):  # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if (titulo != ' ') and (dupla != 0):
        print(titulo)
        print('-='*espaco)
    elif (titulo != ' ') and (dupla == 0):
        print(titulo)


# Codigo principal
num_a = [int(input(f'Numero no vetor A, posicao {i+1}: ')) for i in range(10)]  # Criando lista para o vetor A utilizando compreensao de listas
linha(30, ' ', 0)
num_b = [int(input(f'Numero no vetor B, posicao {c+1}: ')) for c in range(10)]  # Criando lista para o vetor B utilizando compreensao de listas
linha(30, ' ', 0)
num_c = [(num_a[x]+num_b[x]) for x in range(10)]  # Criando lista para o vetor C utilizando compreensao de listas
linha(30, 'VETOR C:', 0)
print(num_c)  # Impressao final do vetor C.
linha(30, ' ', 0)
