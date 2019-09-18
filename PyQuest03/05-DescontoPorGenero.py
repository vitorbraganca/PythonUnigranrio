# Desconto por sexo
while True:
    salb = int(input("Insira o salario bruto do funcionario: "))
    if (salb < 0): print('Salario nao pode ser negativo. Tente novamente.')
    else: break
while True:
    sexo = input("Insira o sexo do funcionario (Atalhos: M para Masculino e F para feminino): ")
    sexo = sexo.upper()
    if (sexo == "masculino") or (sexo == "M"):
        desc = salb * 0.05
        break
    elif (sexo == "feminino") or (sexo == "F"):
        desc = salb * 0.03
        break
    else: print('Sexo invalido. Tente novamente.')
sall = salb - desc
print("Salario liquido com desconto de {} reais igual a: {} reais.".format(desc, sall))