primeiro_termo = int(input("Digite o primeiro termo da P.A (Progressão Aritmética): "))
razao = int(input("Digite a razão da P.A(Progressão Aritmética): "))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end='  ')


