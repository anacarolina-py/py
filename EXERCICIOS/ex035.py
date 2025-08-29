r1 = float(input('Digite o valor da reta: '))
r2 = float(input('Digite o valor da reta: '))
r3 = float(input('Digite o valor da reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:
    print('Sim, é um triângulo!')
else:
    print('Ah não! Isso não é um triângulo!')
