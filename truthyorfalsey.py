nome = ''  # ‘String’ vazia é tratada como falso.
while not nome: # estou pegando um nome como falso e negando ele "not".
    nome = input('Digite um nome.:')  # como eu preencho a 'String' ela passa a ser True e com o Not ela fica false.
valor = int(input('Digite um número qualquer.:'))  # deu false e o sistema continua.
if valor:
    print('Você digitou um valor diferente de zero.')
else:
    print('Você digitou zero.')
