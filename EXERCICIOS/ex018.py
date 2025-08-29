import math
ang = (float(input('Digite o ângulo: ')))
seno = math.sin(math.radians(ang))
tangente = math.tan(math.radians(ang))
cosseno = math.cos(math.radians(ang))
print(f'O ângulo {ang} possui:\na tangente {tangente:.2f}, '
      f'\no cosseno {cosseno:.2f}, \ne o seno {seno:.2f}.')
