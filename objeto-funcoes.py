nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
pais = input('Qual é o seu país? ')
estado = input('Informe o seu UF? ')

usuario = {
    'nome': nome,
    'idade': idade,
    'pais': pais,
    'estado': estado
}

# passando objeto para a funcao


def processa_idade(objeto):
    idade = objeto['idade']
    converte_idade = int(idade)

    if converte_idade >= 18:
        print('Usuário maior de idade ' + idade)
    else:
        print('Unusário menor de idade ' + idade)


# invocando a função
processa_idade(usuario)
