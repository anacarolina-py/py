salario = float(input('Digite seu salário: '))
aum10 = salario * (10/100)
aum15 = salario * (15/100)
if salario >= 1250:
    print(f'Você recebeu um aumento de 10%, seu novo salário é R${salario + aum10:.2f}')
else:
    print(f'Você recebeu um aumento de 15%, seu novo salário é R$ {salario + aum15:.2f}')
