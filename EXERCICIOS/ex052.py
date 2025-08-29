print('DESCUBRA SE O NÚMERO É UM NÚMERO PRIMO!')
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m', end=' ')
        tot += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n O número {num} foi dividido {tot} vezes')
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')