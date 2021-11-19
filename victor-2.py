nota = 999
opcao = 0
relacao = []
while nota > 0:
  nome = input("Digite o nome do aluno: ")
  nota = float(input("Digite a nota do aluno: "))
  if nota > 0:
    relacao.append([nome, nota])
  else:
    while opcao != 6:
      print("1 - Apresentar estatisticas sobre as notas \n")
      print("2- Apresentar relação de alunos e notas entre faixa de valores \n")
      print("3- Apresentar relação de alunos e notas ordenada por nome \n")
      print("4- Apresentar uma relaçao de notas e frequências entre uma faixa de valores \n")
      print("5- Incluir um novo aluno/nota \n")
      print("6- Terminar o programa \n")
      opcao = int(input("Digite a opcao escolhida: "))

      if opcao == 1: 
        print("Manutencao")

      if opcao == 2:
        nota_min = float(input("Digite a nota minima: "))         
        nota_max = float(input("Digite a nota maxima: "))
        for i in range(len(relacao)):
          if (relacao[i][1] > nota_min) and (relacao[i][1] < nota_max):
            print("Aluno: ", relacao[i][0])
            print("Nota: ", relacao[i][1])
      
      if opcao == 3:
        texto = input("Qual texto deve conter no nome do aluno? Deixe em branco para listar todos.")
        if texto == "":
          for i in range(len(relacao)):
            print("Aluno: ", relacao[i][0])
            print("Nota: ", relacao[i][1])
        else: 
          for i in range(len(relacao)):
            if (texto in relacao[i][0]):
              print("Aluno: ", relacao[i][0])
              print("Nota: ", relacao[i][1])

      if opcao == 4:
        print("Manutencao")

      if opcao == 5:
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        if nota > 0:
          relacao.append([nome, nota])
        else:
          print("A nota deve ser positiva. Voltando para o menu...")
