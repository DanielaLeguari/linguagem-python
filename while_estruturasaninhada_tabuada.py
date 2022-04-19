"""Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para cada número,
vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10."""
tabuada = 1
while tabuada <= 10:
    print('Tabuada do {}'.format(tabuada))
    i = 1
    while i <= 10:
        print('{} X {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1  # iterador/contador
