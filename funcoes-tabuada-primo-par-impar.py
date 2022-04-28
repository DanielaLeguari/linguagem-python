"""for i in range(10, 20, 2):
    print(i)"""
"""Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para cada número,
vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10."""

def primo (n):  #  função
    i = 2
    contador = 0
    while (i < n):
        if (n % 2 == 0):
            contador += 1
        i = i + 1
    if (contador > 0 or n == 1 ):  # via de regra o 1 não é primo
        print('O número {} não é primo.'.format(n))
    else:
        print('O número {} é primo.'.format(n))

# programa principal
print('Bem-vindo!')
for i in range(1, 11, 1):
    print('TABUADA DO {}'.format(i))
    print('')
    for tabuada in range(1, 11, 1):
        print('{} X {} = {}'.format(i, tabuada, i * tabuada))
        if ((i * tabuada) % 2 == 0):
            print('Numero par.')
        else:
            print('Numero ímpar')
        primo(i * tabuada)
    print('')
print('Fim da tabuada!')