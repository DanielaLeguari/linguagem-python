""" uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de 5 anos de empresa. Todos os outros que
não se enquadram nessa categoria receberam uma bonificação de 10%, somente. Escreva um algoritmo que leia o salário do
funcionário e seu tempo de empresa, e apresente a bonificação de cada funcionário na tela."""

salario = float(input('Digite o valor do salário R$.'))
admissao = int(input('Digite o ano de admissão na empresa.:'))
ano_atual = int(input('Digite o ano atual.:'))

tempo = ano_atual - admissao
if (tempo >= 5):
    bonus = salario * 0.20
else:
    bonus = salario * 0.10
print('Voce tem {} anos de empresa.'.format(tempo))
print('Seu salário é de R${}.'.format(salario))
print('Sua bonificação é de R${}.'.format(bonus))
print('Salario final R${}.'.format(bonus + salario))


