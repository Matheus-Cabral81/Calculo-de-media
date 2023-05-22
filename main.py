n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
media = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    n5 = float(input())
    print(f'Nota do exame: {n5:.1f}')
    media_final = (media + n5) / 2
    if media_final >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
    elif media_final <= 4.9:
        print('Aluno reprovado.')
else: 
    print('Aluno reprovado.')