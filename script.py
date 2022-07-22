print('Iniciando programa')
 #criando objeto
aluno = {
    'nome' : 'Daniela',
    'sobrenome': 'Leguari',
    'ano_nascimento': 1994,
    'idade' : 28,
    'estado' : 'PR',
    'pais' : 'Brasil',
    'numeros' : [10, 7, 13]
}
idade = 2022 -aluno['ano_nascimento']
# idade = str(aluno['idade'])

print('Nome:' + aluno['nome'])
print('Sobrenome:' + aluno['sobrenome'])
print(idade)
