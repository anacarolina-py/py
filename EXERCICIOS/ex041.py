from datetime import date
atual = date.today().year
ano_nasc = int(input('Qual seu ano de nascimento? '))
idade = atual - ano_nasc
print('Você nasceu em {}, portanto tem {} anos em {}.'.format(ano_nasc,idade, atual))
if idade <= 9:
    print('Você está na categoria: MIRIM')
elif idade <= 14:
    print('Você está na categoria: INFANTIL')
elif idade <= 19:
    print('Você está na categoria: JÚNIOR')
elif idade <=25:
    print('Você está na categoria: SÊNIOR')
else:
    print('Você está na categoria: MASTER')

