def linha(espaco, titulo): # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if titulo != ' ':
        print(titulo)
        print('-='*espaco)

relacao = []  # Criando um vetor vazio para relacao das pessoas com mais de 1.7m
for i in range(50):
    nome = input('Digite o nome: ')  # Lendo o nome
    altura = float(input('Digite a altura em metros: '))  # Lendo altura
    if altura > 1.7:
        relacao.append([nome, altura])
linha(15, ' Relacao dos maiores de 1.7m')
for i in relacao:
    print(f'{i[0]} - {i[1]:.02f} metros')
linha(15,' ')
