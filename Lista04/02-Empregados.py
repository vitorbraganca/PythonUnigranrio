def linha(espaco, titulo): # Criando uma funcao para impressao de linha (manter o codigo limpo, visto que se repete algumas vezes)
    print('-='*espaco)
    if titulo != ' ':
        print(titulo)
        print('-='*espaco)

relacao = []   # Criando um vetor vazio para relacao das pessoas com mais de 1.7m
for i in range(100):  # Ler 100 empregados
    matricula = input('Digite a matricula do empregado: ')  # Lendo a matricula
    sal_brt = float(input('Digite o salario bruto: '))  # Lendo salario bruto
    descnt = sal_brt * 0.11 # Descontando 11% do salario bruto
    sal_lqd = sal_brt - descnt
    relacao.append([matricula, sal_brt, descnt, sal_lqd])
linha(35, '               Relacao dos salarios dos empregados')
print(f'MATRICULA   -   BRUTO   -   DESCONTO    -   LIQUIDO')   #   Indicador da forma que aparece o resultado
for i in relacao:
    print(f'{i[0]:>5}   -   {i[1]:>8.2f}R$   -   {i[2]:>5.2f}R$   -   {i[3]:>8.2f}R$')  # Imprimir valores da lista
linha(35, ' ')
