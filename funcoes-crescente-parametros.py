"""Escreva uma rotina que recebe três valores como parâmetro e coloque-os em ordem crescente,
ou seja, o menor ao maior. Imprima na tela os três valores.
Dica: para realizar o print sem quebrar a linha, utilize um parâmetro opcional end='' da função
print. Exemplo: print(x, end='').
Utilize condicionais de múltipla escolha e composta.
"""
def valores (a = 0 ,b = 0, c = 0):
    if ((a <= b) and (a <= c)):
        if (b <= c):
            print('Em ordem crescente ficou.: {}, {}, {}'.format(a, b, c))
        else:
            print('Em ordem crescente ficou.: {}, {}, {}'.format(a, c, b))
    elif ((b <= a) and (b <= c)):
        if (a <= c):
            print('Em ordem crescente ficou.: {}, {}, {}'.format(b, a, c))
        else:
            print('Em ordem crescente ficou.: {}, {}, {}'.format(b, c, a))
    else:
        if (a <= b):
            print('Em ordem crescente ficou.: {}, {}, {}'.format(c, a, b))
        else:
            print('Em ordem crescente ficou.: {}, {}, {}'.format(c, b, a))

#programa principal
a = int(input('Digite o valor de A.'))
b = int(input('Digite o valor de B.'))
c = int(input('Digite o valor de C.'))

valores(a, b, c) #a,b,c é variável global

