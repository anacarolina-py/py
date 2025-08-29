distancia = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias? '))
aluguel = (distancia * 0.15) + (dias * 60)
print(f'O total de quilômetros percorridos foram {distancia} durante {dias} dias, totalizando R$ {aluguel:.2f}')
