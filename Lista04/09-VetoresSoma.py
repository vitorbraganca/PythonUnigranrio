# Funcoes
def linha(espaco, titulo, dupla):  # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if (titulo != ' ') and (dupla != 0):
        print(titulo)
        print('-='*espaco)
    elif (titulo != ' ') and (dupla == 0):
        print(titulo)


# Codigo principal
num_a = []
num_b = []
num_c = []  # Criando vetores vaios para atribuicao

for i in range(10):  # Leitura numeros vetor A
    num_a.append(int(input(f'|VETOR A| Digite o numero na posicao {i+1}: ')))
linha(30, ' ', 0)
for c in range(10):  # Leitura numeros vetor A
    num_b.append(int(input(f'|VETOR B| Digite o numero na posicao {c+1}: ')))
linha(30, ' ', 0)
for x in range(10):  # Soma numeros vetor A + vetor B
    num_c.append(num_a[x]+num_b[x])  # atribuicao ao vetor c da soma do numero na posicao x (for) de cada vetor
    print(f'|A: {num_a[x]}| + |B: {num_b[x]}| ||POSICAO {x+1}||')   # Impressao para controle de quais numeros e de quais posicoes
linha(30, 'VETOR C:', 0)
linha(30, num_c, 1)  # Impressao final do vetor C.
