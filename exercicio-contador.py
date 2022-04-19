"""Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo específico
pelo usuário e que sejam números pares."""
inicial = int(input('Digite um valor para iniciar a contagem.:'))
final = int(input('Digite um valor para encerrar a contagem.:'))
x = inicial
while (x <= final):
    if (x % 2 ==0):  # verificação de numeros pares.
        print(x)
    x = x + 1