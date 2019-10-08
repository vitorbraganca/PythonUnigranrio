def linha():
    print('-='*15)


relacao = []  # Criando um vetor vazio para relacao das pessoas com mais de 1.7m
for i in range(3):
    nome = input('Digite o nome: ')  # Lendo o nome
    altura = float(input('Digite a altura em metros: '))  # Lendo altura
    if altura > 1.7:
        relacao.append([nome, altura])
linha()
print('Relacao dos maiores de 1.7m')
linha()
for i in relacao:
    print(f'{i[0]} - {i[1]:.02f} metros')
linha()
