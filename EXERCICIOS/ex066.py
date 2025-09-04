num = cont = soma = 0
while True:
    num = int(input('Digite um número inteiro (Digite 999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} números e a soma deles foi {soma}.')
