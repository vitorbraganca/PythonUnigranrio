# Funcoes
def linha(espaco, titulo):  # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if titulo != ' ':
        print(titulo)
        print('-='*espaco)


def consulta():  # Funcao para consulta de dados a partir do codigo unico
    consulta = int(input('Consultar: '))
    if consulta in cadastrados:
        index = cadastrados.index(consulta)  # Buscando item na lista a partir do codigo
        linha(20, ' ')
        print('Usuario cadastrado. Dados:')
        print(f'{cadastrados[index+1]}')
        linha(20, ' ')
    else:
        linha(20, 'Usuario nao cadastrado.')


# Codigo principal        
cadastrados = []
for i in range(5):
    codigo = int(input('Codigo: '))  # Leitura codigo unico
    nome = input('Nome: ')  # Leitura nome
    telefone = input('Telefone: ')  # Leitura telefone
    cadastrados.append(codigo)  # Adicionando o codigo na lista
    cadastrados.append([nome, telefone])    # Adicionando nome e telefone como um unico espaco
    linha(15, ' ')
while True:
    consulta()
    resp = input('Deseja consultar novamente? ')
    resp = resp.upper()  # Deixando em caixa alta para reduzir possibilidades
    if (resp == 'N') or (resp == 'NAO'):
        linha(15, 'Consulta encerrada ')
        break
    else:
        linha(15, 'Nova consulta... ')
