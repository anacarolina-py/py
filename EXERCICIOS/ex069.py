homem = mulher = maioridade = 0
continua = ' '
while continua not in 'Nn':
    idade = int(input('Digite a sua idade: '))
    if idade > 18:
        maioridade += 1
    sexo = str(input('Digite o sexo [F/M] ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Temos {maioridade} pessoas com mais de 18 anos. \n'
      f'Foram cadastrados {homem} homens. \n'
      f'Temos {mulher} mulheres com menos de 20 anos.')