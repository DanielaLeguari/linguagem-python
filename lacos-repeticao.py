trigger = " "
lista = []

while trigger != 'sair':
    nome = input('digite o seu nome:')
    lista.append(nome)
    print(lista)
    trigger = input('Pressione enter para continuar ou escreva sair ')