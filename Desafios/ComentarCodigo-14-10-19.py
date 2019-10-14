
listaCD = []  # Criando lista vazia para lista dos CDs

#Funcoes
def exibirMenu():   # Criando funcao para exibicao do menu
    print("1 - Inserir novo CD")  # Imprimindo opcoes
    print("2 - Excluir CD")
    print("3 - Listar CDs")
    print("4 - Sair")
    opcao = int(input("Escolha uma opcao: "))  # Entrada de opcao
    return opcao  # Retorna o valor digitado

def inserirCD():  # Criando funcao para insercao do CD na lista
    novoCD = input("Digite o nome do Artista: ")  # Entrada do nome do artista
    listaCD.append(novoCD)  # Adicionando artista a lista, antes vazia, dos CDs

def listarCD():  # Criando funcao para listar os CDs
    for elemento in listaCD:  # Iniciando estrutura de repeticao para impressao da lista
        print (elemento)  # Desta maneira, a impressao sera linha apos linha, e nao da lista inteira.

def excluirCD():  # Criando funcao para exclusao de itens da lista
    nomeCD = input("Nome do CD que deseja excluir:")  # Entrada artista que deseja excluir
    indice = -1  # Atribuindo -1 ao indice para controle futuro
    encontrou = False  # Atribuindo valor booleano false a variavel encontrou (questao de organizacao do codigo)
    for elemento in listaCD:  # Estrutura de repeticao para buscar o artista na lista
        indice += 1  # Controle do indice (caso nao tivesse sido atribuido -1 acima, começaria em 0, e a cada elemento, incrementaria em 1, ultrapassando o limite da lista
        if elemento == nomeCD:  # Condicao: se o item da lista for igual ao nome do artista a ser excluido, faça:
            encontrou = True  # Atribuindo valor booleano true a variavel encontrou
            break  # Quebrando estrutura de repticao
    if (encontrou):  # Condicao, se for VERDADEIRO (atribuicao acima), faça:
        del listaCD[indice]  # Excluindo da lista o item na posicao INDICE. (caso nao tivesse sido atribuido -1, acarretaria em erro.)

# Programa principal
while True:  # Iniciando loop do programa
    opcao = exibirMenu()  # Opcao sera o valor retornado pela funcao do menu
    if opcao == 4:  # Condicao: Se o valor digitado p/ opcao igual a 4 (SAIR), faça
        break  # Quebra a estrutura de repeticao, acarretando no encerramento do programa.
    elif opcao == 3:  # Condicao: Se o valor digitado p/ opcao igual a 3(LISTAR CDs), faça
        listarCD()  # Chamando funcao para listar os CDs
    elif opcao == 1:  # Condicao: Se o valor digitado p/ opcao igual a 1 (INSERIR), faça
        inserirCD()  # Chamando funcao para insercao de CD.
    elif opcao == 2:  # Condicao: Se o valor digitado p/ opcao igual a 2(EXCLUIR), faça
        excluirCD()  # Chamando funcao para exclusao de CD da lista.
