nome = input('Qual é o seu nome?')
ano = int(input('Qual é o seu ano de nascimento?'))

def calcula_idade(ano_nascimento):

    idade = 2022 -  ano_nascimento
    print('Sua idade é {} anos'.format(idade))


calcula_idade(ano)
