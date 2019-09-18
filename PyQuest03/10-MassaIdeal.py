#Peso ideal
altura = float(input('Insira a altura em metros (m): '))
while True:
    sexo = (input('Insira o sexo (Atalhos: F para FEMININO e M para MASCULINO): '))
    sexo = sexo.upper()
    if (sexo == 'M') or (sexo == 'MASCULINO'):
        ideal = (72.7*altura)-58
        break
    elif (sexo == 'F') or (sexo == 'FEMININO'):
        ideal = (62.1*altura)-44.7
        break
    else:
        print('Opcao invalida. Tente novamente.')
print('Sua massa ideal e: {:.2f}kg'.format(ideal))