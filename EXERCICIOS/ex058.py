from random import randint
computador = randint(0, 10)
palpites = 0
print('Pensei em um número de 0 a 10')
print('Será que você consegue adivinhar?')
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou!')
print(f'Você acertou com {palpites} tentativas.')


