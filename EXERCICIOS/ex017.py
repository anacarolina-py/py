from math import hypot
cat1 = (float(input('Digite o valor do cateto oposto: ')))
cat2 = (float(input('Digite o valor do cateto adjacente: ')))
print(f'A hipotenusa é {hypot(cat1, cat2):.2f}')
