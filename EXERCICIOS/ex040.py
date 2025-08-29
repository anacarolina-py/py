n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print(f'Suas notas foram {n1} e {n2}. Sua média foi {media}.')
if media < 5.0:
    print('Você foi REPROVADO.')
elif 5.0 <= media < 7.0:
    print('Você está de RECUPERAÇÃO.')
else:
    print('Você foi APROVADO.')
