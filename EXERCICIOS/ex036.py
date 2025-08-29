casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
tempo = int(input('Em quantos anos deseja pagar sua casa? '))
parcela = casa/(tempo*12)
if parcela >= (0.3 * salario):
    print(f'Seu empréstimo não foi aprovado. Sua parcela ficaria R${parcela:.2f}')
else:
    print(f'Parabéns! Seu empréstimo foi aprovado! Sua parcela ficou R$ {parcela:.2f}')
