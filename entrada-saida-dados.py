from email.errors import InvalidDateDefect


print('Bem-vindo!')
nome = input('Insira seu nome')
idade = input('Insira sua idade')
pais = input('Insira seu país')
# print('Seu nome é {}.'.format(nome))

usuario = {}  # dicionário
usuario['nome'] = nome
usuario['idade'] = idade
usuario['pais'] = pais

print(usuario)