numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Seu número {numero} pode ser dividido por:\n Unidade: {unidade}'
      f'\n Dezena: {dezena} \n Centena: {centena} \ne Milhar: {milhar}')



