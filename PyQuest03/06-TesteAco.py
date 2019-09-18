# Grau aço
print('=' * 30)
print('{:^30}'.format('TESTE AÇO'))
print('=' * 30)
result = 0
carb = 'NAO'
dureza = 'NAO'
resist = 'NAO'
resultado = """ TESTE 1: Conteúdo de carbono abaixo de 7%: {}
TESTE 2: Dureza Rokwell maior que 50: {}
TESTE 3: Resistencia a tração maior que 80.000 psi: {}
Amostra de aço {} obteve o grau de:  {}.
"""
amostra = input('Numero de amostra: ')
cnt_carb = float(input('Conteudo de carbono em porcentagem: '))
dureza_rkwl = float(input('Dureza Rokwell: '))
resist_tracao = float(input('Resistencia a tração em psi: '))
if cnt_carb < 7:
    result += 8 #  Teste 1
    carb = 'OK'
if dureza_rkwl > 50:
    result += 1 #  Teste 2
    dureza = 'OK'
if resist_tracao > 80000:
    result+= 3 # Teste 3
    resist = 'OK'
if result == 10:
    print(resultado.format(carb, dureza, resist, amostra, '10'))
elif result == 9:
    print(resultado.format(carb, dureza, resist, amostra, '9'))
elif result == 12:
    print(resultado.format(carb, dureza, resist, amostra, '8'))
else:
    print(resultado.format(carb, dureza, resist, amostra, '7'))