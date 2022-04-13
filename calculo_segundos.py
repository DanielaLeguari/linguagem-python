"""Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos
e de segundos. Calcule o total de segundos resultante e imprima na tela para o usuário."""
dias = int(input('Digite a quantidade de dias.:'))
horas = int(input('Digite a quantidade de horas.:'))
minutos = int(input('Digite a quantidade de minutos.:'))
segundos = int(input('Digite a quantidade de segundos.:'))

total = segundos +(minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)
print('O total de segundos calculados é {}'.format(total))
#  método clássico
print('O total de segundos calculados é %i' % (total))
