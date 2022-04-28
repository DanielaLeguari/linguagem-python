"""Escreva uma função que calcule o fatorial
de um número recebido como parâmetro e
retorne o seu resultado
Faça uma validação dos dados por meio de
uma outra função, permitindo que somente
valores positivos sejam aceitos
Crie o help da sua função (exercício da
apostila – aula 5)
"""
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """
     Calcula a fatorial
    :param num:
    :return:
    """
    fat = 1  #o menor valor de fatorial possível é 1.
    if num == 0:
        return fat
    for i in range(1, num+1, 1): #num+1 porque é sempre um a menos.
        fat *= i # fat= fat * i
    return fat
#fora da função

x = valida_int('Digite um valor para clacular a fatorial.', 0,99999)
print('{}! = {}'.format(x, fatorial(x)))

help(fatorial)




