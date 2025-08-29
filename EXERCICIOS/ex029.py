velocidade = float(input('Qual a velocidade do carro? '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade, portanto recebeu uma multa no valor de R$ {multa :.2f}')
else:
    print('Você está dentro da velocidade permitida.')
