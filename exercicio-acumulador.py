""" Escreva um algoritmo que calcule a sua média de notas em derterminada disciplina
Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas"""
soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}ª nota: .'.format(cont)))
    soma = soma + x  # soma += x
    cont = cont + 1  # cont += 1
media = soma / 5
print('Média final: {}'.format(media))




