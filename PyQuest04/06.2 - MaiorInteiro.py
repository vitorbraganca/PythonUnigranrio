#   Maior inteiro
num = num_maior = 0
print('Digite 999 a qualquer momento para parar. Ele nao sera contabilizado.')
while True:
    num = int(input('Digite um numero inteiro: '))
    if num == 999:
        break
    if num > num_maior:
        num_maior = num
print(f'O maior numero e: {num_maior}')
