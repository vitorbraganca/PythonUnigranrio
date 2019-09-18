#3: media aluno
while True:
    nota1 = float(input('Nota da primeira avaliacao: '))
    nota2 = float(input('Nota da segunda avaliacao: '))
    if (nota1 < 0) or (nota2 < 0): print('Notas nao podem ser negativas. Tente novamente')
    else: break
media_parc = (nota1 + nota2) / 2
if media_parc >= 7: print(f'Aprovado com a media: {media_parc}')
else:
    print(f'Sua media ({media_parc}) nao e suficiente,')
    nota3 = float(input('Nota da terceira avaliacao: '))
    media_final = (media_parc + (nota3*2)) /3
    if media_final >= 6: print(f'Aprovado com a media: {media_final}')
    else: print(f'Reprovado com a media: {media_final}')