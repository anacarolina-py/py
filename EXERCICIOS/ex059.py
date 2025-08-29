n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('''O que deseja fazer?
      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NÚMEROS
      [5] SAIR DO PROGRAMA''')
    opção = int((input('Qual é a opção escolhida? ')))
    if opção == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opção == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif opção == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opção == 5:
        print('Fim')

