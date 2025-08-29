p = float(input('Digite aqui o preço do produto: R$ '))
desc = int(input('Qual o desconto? '))
d = p*(desc/100)
np = p-d
print('O preço do seu produto com desconto é R$ ', np)

