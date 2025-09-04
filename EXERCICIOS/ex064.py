n = cont = soma = 0
n = int(input('Digite um número inteiro [Digite 999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro [Digite 999 para parar]: '))


print(f'Você digitou {cont} números e soma deles é {soma}.')