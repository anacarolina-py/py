alt = float(input('Qual é a altura da parede? '))
lar = float(input('Qual é a largura da parede? '))
area = alt*lar
tinta = area/2

print(f'Para pintar a parede de {alt} metros de altura e {lar} metros de largura, com área de {area}m2 vamos precisar '
      f'de {tinta} litros de tinta.')
