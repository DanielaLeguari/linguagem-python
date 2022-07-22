#refatorando o código, utilizando funções

from tracemalloc import DomainFilter


print('Bem-vindo!')

ano_atual = 2022

nome = input('Insira o seu nome: ')
sobrenome = input('Insira o seu sobrenome: ')
ano_nascimento = input('Insira o ano de nascimento: ')
pais = input('Insira o país')
estado = input('Insita a UF do estado: ')
ano = int(ano_nascimento)
idade = ano_atual - ano

usuario ={
    'nome' : nome,
    'sobrenome': sobrenome,
    'idade' : idade,
    'pais': pais,
    'estado': estado
}

print(usuario)

def faixa_etaria(data):

    idade = data['idade']

    if idade >= 18 and idade < 64:

        print('Usuário é adulto.')
        data['faixa_etaria'] = 'adulto'
        return data

    elif idade >= 64 and idade > 18:

        print('Usuário é idoso')
        data['faixa_etaria'] = 'idoso'
        return data
    else:

        print('Usuário é menor de idade')
        data['faixa_etaria'] = 'menor de idade'
        return data

usuario = faixa_etaria(usuario)  # guardou a data
print(usuario) # guardou o valor retornou a faixa_etaria da pessoa




