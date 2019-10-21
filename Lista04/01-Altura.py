def linha(espaco, titulo):  # Criando uma funcao para impressao de linha (manter o codigo limpo)
    print('-='*espaco)
    if titulo != ' ':
        print(titulo)
        print('-='*espaco)


relacao_menores = []  # Criando um vetor vazio para relacao das pessoas em geral
relacao_maiores = []  # Criando um vetor vazio para relacao das pessoas com mais de 1.7m
for i in range(3):
    nome = input('Digite o nome: ')  # Lendo o nome
    altura = float(input('Digite a altura em metros: '))  # Lendo altura
    if altura > 1.7:
        relacao_maiores.append([nome, altura])
    else:
        relacao_menores.append([nome, altura])
linha(15, ' Relacao dos maiores de 1.7m')
for i in relacao_maiores:
    print(f'{i[0]:10} - {i[1]:.02f} metros')
linha(15, ' ')
