"""Escreva uma rotina que crie uma borda ao redor de uma palavra para destacá-la como sendo um
título. A rotina deve receber como parâmetro a palavra a ser destacada. O tamanho da caixa de texto
deverá ser adaptável de acordo com o tamanho da palavra. A seguir, veja alguns exemplos de como
deve ficar a borda na palavra."""


def borda(s1):
    tam = len(s1)

    if tam:
        print('+', '-' * tam, '+')
        print('|', s1,'|')
        print('+', '-' * tam, '+')

borda('Olá, Mundo!')
borda('Lógica e Algoritmos de programação')
