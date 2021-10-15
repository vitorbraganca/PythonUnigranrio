voto, joao, jose, maria, branco, nulos = 0, 0, 0, 0, 0, 0

print("-" * 30)
print("Vamos começar a votação.")
print("-" * 30)
print("-" * 9, "CANDIDATOS", "-" * 9)
print("1 - João da Silva")
print("2 - José Ramalho")
print("3 - Maria Mattos")
print("0 - Para votos em branco")
print("Qualquer outro valor para nulos")
print("-" * 30)
for i in range (6):
    voto = int(input("Qual o seu voto? "))

    if (voto == 1):
        joao += 1
        
    elif (voto == 2):
        jose += 1
        
    elif (voto == 3):
        maria += 1
        
    elif (voto == 0):
        branco += 1
        
    else:
        nulos += 1
        
print("-" * 30)
print("TOTAL DE VOTOS")
print("-" * 30)
print("Candidato 1 - João: ", joao)
print("Candidato 2 - José: ", jose)
print("Candidato 3 - Maria: ", maria)
print("Votos em branco: ", branco)
print("Votos nulos: ", nulos)
print("-" * 30)
