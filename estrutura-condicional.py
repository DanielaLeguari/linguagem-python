print('Bem-vindo!')

ano_atual = 2022

nome = input('Insira o seu nome: ')
sobrenome = input('Insira o seu sobrenome: ')
ano_nascimento = input('Insira o ano de nascimento: ')
pais = input('Insira o país')
estado = input('Insita a UF do estado: ')
ano = int(ano_nascimento)
idade = ano_atual - ano


# criar um dicionário

if idade >= 18 and idade < 64:
    faixa_etaria = 'adulto'
    usuario = {
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade,
        'pais': pais,
        'estado': estado,
        'faixa_etaria': faixa_etaria
    }

    print(usuario)

elif idade > 64 and idade > 18:
    faixa_etaria = 'idoso'
    usuario = {
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade,
        'pais': pais,
        'estado': estado,
        'faixa_etaria': faixa_etaria
    }

    print(usuario)

else:
    faixa_etaria = 'menor de idade'
    usuario = {
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade,
        'pais': pais,
        'estado': estado,
        'faixa_etaria': faixa_etaria
    }
    print('Erro, usuário menor de idade!')
    print(usuario)

