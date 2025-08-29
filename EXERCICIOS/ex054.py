from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = atual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'O total de pessoas maiores de idade é {totmaior} e {totmenor} menores de idade.')