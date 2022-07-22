def calcula_operacao(n1, n2, operacao):
    num1 = 0
    num2 = 0
    try:
        num1 = int(n1)
        num2 = int(n2)
    except ValueError:
        return 'Você digitou letras!'

    if not(valida_intervalo(num1, num2)):
        return 'Você digitou valores fora do intervalo!'

    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    else:
        return 'Operação "{}" é inválida!'.format(operacao)

def valida_intervalo(n1, n2):
    if (n1 > 0 and n1 <= 10) or (n1 >= 20 and n1 <= 30):
        if (n1 > 0 and n2 <= 10) or (n2 >= 20 and n2 <= 30):
            return True
    return False

resultado = calcula_operacao(1, '20', "+")
print(resultado)
