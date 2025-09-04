while True:
    num = int(input('Digite um número inteiro para obter sua tabuada: '))
    if num < 0:
        break
    for c in range(0, 11):
        tabuada = num * c
        print(f'{num} x {c} = {tabuada}')
print('Programa Encerrado')