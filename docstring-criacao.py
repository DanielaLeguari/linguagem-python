#doc string
def soma(x=0, y=0, z=0):
    """Retorna o somatório de até 3 valores numéricos quaisquer
    Todos os parâmetros são opcionais.

    x: valor numérico (opcional)
    y: valor numérico (opcional)
    z: valor numérico (opcional)
    """
    return x+y+z

print(soma(3,2))
help(soma)