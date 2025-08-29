r1 = float(input('Digite o valor do segmento 1: '))
r2 = float(input('Digite o valor do segmento 2: '))
r3 = float(input('Digite o valor do segmento 3: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    if r1 == r2 == r3:
        print('Este é um triângulo EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este é um triângulo ISÓSCELES')
    else:
        print('Este é um triângulo ESCALENO')
else:
    print('Ah não! Isso não é um triângulo!')
