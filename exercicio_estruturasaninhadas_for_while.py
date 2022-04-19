"""Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para cada número,
vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10."""
tabuada = 1
while tabuada <= 10:
    print('Tabuada do {}'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} X {} = {}'.format(tabuada, i, tabuada * i))
    tabuada += 1

