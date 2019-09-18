#Numeros diferentes
while True:
    num1 = int(input('Insira o numero 1: '))
    num2 = int(input('Insira o numero 2: '))
    num3  = int(input('Insira o numero 3: '))
    if (num1 == num2) or (num1 == num3) or (num2 == num3):
        print('Os valores nao sao diferentes. Tente novamente.')
    else: break
if (num1 > num2) and (num1 > num3):
    print(f'O maior deles e: {num1}')
elif (num2 > num1) and (num2 > num3):
    print(f'O maior deles e: {num2}')
else:
    print(f'O maior deles e: {num3}')