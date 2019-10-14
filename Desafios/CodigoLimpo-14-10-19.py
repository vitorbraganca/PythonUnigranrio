listaCD = []
def exibirMenu():
    print("1 - Inserir novo CD")
    print("2 - Excluir CD")
    print("3 - Listar CDs")
    print("4 - Sair")
    opcao = int(input("Escolha uma opcao: "))
    return opcao

def inserirCD():
    novoCD = input("Digite o nome do Artista: ")
    listaCD.append(novoCD)

def listarCD():
    for elemento in listaCD:
        print (elemento)

def excluirCD():
    nomeCD = input("Nome do CD que deseja excluir:")
    indice = -1
    encontrou = False
    for elemento in listaCD:
        indice += 1
        if elemento == nomeCD:
            encontrou = True
            break
    if (encontrou):
        del listaCD[indice]

while True:
    opcao = exibirMenu()
    if opcao == 4:
        break
    elif opcao == 3:
        listarCD()
    elif opcao == 1:
        inserirCD()
    elif opcao == 2:
        excluirCD()
