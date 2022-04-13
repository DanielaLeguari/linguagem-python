"""Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de
desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto"""

preco = float(input('Digite o preço do produto R$'))
percentual = float(input('Digite o percentual de desconto (0 a 100%.:'))

desconto = preco * (percentual / 100)
final = preco - desconto

print(' O preço do produto é R${}. Desconto de {}%'.format(preco, percentual))
print(' O valor do desconto é R$ {} e o preço final do produto com desconto R${}'.format(desconto, final))
