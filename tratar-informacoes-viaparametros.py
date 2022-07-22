# importacao de biblioteca
import sys

# sys.argv lista de argumentos que comeca do 1 e vai até o infinito
nome = sys.argv[1]
idade = sys.argv[2]
pais = sys.argv[3]

usuario = {}
usuario['nome'] = nome
usuario['idade'] = idade
usuario['pais'] = pais

print(usuario)
