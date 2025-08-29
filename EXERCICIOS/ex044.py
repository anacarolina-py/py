preco = float(input('Digite o valor desejado: R$ '))
print('''Escolha uma forma de pagamento: 
[ 1 ] Pagamento à vista no dinheiro/cheque - 10 % de desconto
[ 2 ] Pagamento à vista no cartão - 5% de desconto
[ 3 ] Em até 2x no cartão - preço formal
[ 4 ] Em 3x ou mais no cartão - 20% de juros''')
opção = int(input('Sua opção: '))
if opção == 1:
    novo_preco = preco - ((10/100) * preco)
    print(f'O valor de sua compra ficará R$ {novo_preco:.2f}')
elif opção == 2:
    novo_preco = preco - ((5/100) * preco)
    print(f'O valor de sua compra ficará R$ {novo_preco:.2f}')
elif opção == 3:
    print(f'O valor de sua compra ficará R$ {preco:.2f} em 2 vezes de R$ {preco/2:.2f} SEM JUROS.')
elif opção == 4:
    novo_preco = preco + ((20/100) * preco)
    vezes = int(input('Em quantas vezes deseja fazer? '))
    print(f'O valor de sua compra ficará R$ {novo_preco:.2f} em {vezes} vezes  de R$ {novo_preco/vezes:.2f}')
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')




