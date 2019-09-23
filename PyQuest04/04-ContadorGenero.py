#   Contador genero
masc = 0
fem = 0
qntd = 0
while True:
    print('Digite FIM a qualquer momento para parar.')
    sexo = input('Insira o sexo |Atalhos: M para MASCULINO e F para FEMININO|: ')
    sexo = sexo.upper()
    if sexo == 'FIM':
        break
    elif (sexo == 'M') or (sexo == 'MASCULINO'):
        masc +=1 #    Contador de masculino
    elif (sexo == 'F')  or (sexo == 'FEMININO'):
        fem +=1   #    Contador de feminino
    else:
        print('Invalido. Tente novamente.')
    qntd+=1 # Contador de pessoas
print('{} Pessoas cadastradas | {} do sexo MASCULINO e {} do sexo FEMININO'.format(qntd, masc, fem))