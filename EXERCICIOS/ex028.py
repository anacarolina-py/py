import random
num = int(input('Escolha um número de 0 a 5: '))
sorteio = random.choice([0, 1, 2, 3, 4, 5]) #randint
if num == sorteio:
    print('Parabéns, você acertou o número premiado!')
else:
    print('Infelizmente você errou o número premiado!')



