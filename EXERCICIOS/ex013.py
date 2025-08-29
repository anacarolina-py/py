salario = float(input('Digite seu salário: '))
porc = int(input('Qual a porcentagem? '))
aumento = salario*(porc/100)
novo_sal = salario+aumento
print(f'Com um aumento de',porc,'%, seu novo salário é ', novo_sal)
