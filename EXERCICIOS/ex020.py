import random

n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))
sorteio = f'{n1} {n2} {n3} {n4}'.split()
random.shuffle(sorteio)
print(sorteio)

