def linha(espaco, titulo):  # Criando uma funcao para impressao de linha (manter o codigo limpo)
    print('-='*espaco)
    if titulo != ' ':
        print(titulo)
        print('-='*espaco)


relacao = []  # Criando um vetor vazio para relacao das pessoas
for i in range(3):
    relacao.append([input('Digite o nome: '), float(input('Digite a altura: '))])  # Leitura e implementacao
linha(15, ' Relacao dos maiores de 1.7m')
for i in relacao:
    if i[1] > 1.7:
        print(f'{i[0]:10} - {i[1]:.02f} metros')
linha(15, ' ')
