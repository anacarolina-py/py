somaidade = 0
mediaidade = 0
maioridadehomem = 0
maisvelho = ''
totmulher20 = 0
for i in range(1, 5):
    print(f"{i}ª PESSOA: ")
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo: '))
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem += idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


mediaidade = somaidade / 4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O homem mais velho se chama {maisvelho} e tem {maioridadehomem} anos')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')