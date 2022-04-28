"""Escreva uma rotina que crie um laço de repetição que faz uma contagem e imprime esta
contagem na tela em uma só linha. Porém, como parâmetro, a função deve receber o valor inicial da
contagem, o final, e o passo da iteração. Deixe os parâmetros inicial e de passo como opcionais. Você
pode fazer o laço com for ou com while.
Dica: para realizar o print sem quebrar a linha, utilize um parâmetro opcional end='' da função
print. Exemplo: print(x, end='')."""

def contador (fim,inicio = 0, passo = 1):
    for i in range(inicio, fim, passo):
        print('{}'.format(i), end=' ')
    print('\n')
# programa principal
contador(20, 10, 2)
contador(12)





