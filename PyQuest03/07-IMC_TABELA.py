#IMC com tabela
massa = float(input('Insira a massa em quilogramas (kg): '))
altura = float(input('Insira a altura em metros (m): '))
indice = massa / (altura**2) # Calculo IMC

result_adlt = """           SEU IMC: {:.2f}
============================================================
IMC                 |   CLASSIFICAÇÃO       | VOCE ESTA AQUI:
============================================================
ABAIXO DE 18.5      |   ABAIXO DO PESO      |       {}
ENTRE 18,6 e 24,9   |   PESO IDEAL          |       {}
ENTRE 25,0 e 29,9   |   LEVEMENTE ACIMA     |       {}
ENTRE 30,0 e 34,9   |   OBESIDADE GRAU I    |       {}
ENTRE 35,0 e 39,9   |   OBESIDADE GRAU II   |       {}
ACIMA DE 40         |   OBESIDADE GRAU III  |       {}
============================================================
"""
if indice < 18.5:
    print(result_adlt.format(indice,'<==',' ',' ',' ',' ',' '))
elif (indice > 18.6) and (indice < 24.9):
    print(result_adlt.format(indice,' ','<==',' ',' ',' ',' '))
elif (indice > 25.0) and (indice < 29.9):
    print(result_adlt.format(indice,' ',' ','<==',' ',' ',' '))
elif (indice > 30.0) and (indice < 34.9):
    print(result_adlt.format(indice,' ',' ',' ','<==',' ',' '))
elif (indice > 35.0) and (indice < 39.9):
    print(result_adlt.format(indice,' ',' ',' ',' ','<==',' '))
else:
    print(result_adlt.format(indice,' ',' ',' ',' ',' ','<=='))