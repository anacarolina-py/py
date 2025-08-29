from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogada = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 15)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador jogou {itens[jogada]}')
print('-=' * 15)
if computador == 0:
    if jogada == 0:
        print('EMPATE!')
    elif jogada == 1:
        print('JOGADOR VENCEU!')
    elif jogada == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogada == 0:
        print('COMPUTADOR VENCEU!')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogada == 0:
        print('O JOGADOR VENCEU!')
    elif jogada == 1:
        print('COMPUTADOR VENCEU!')
    elif jogada == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')


