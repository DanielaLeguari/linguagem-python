""" Crie um algoritmo que receba um valor do tipo inteiro via teclado.
No entanto, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos.
Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado."""
x = int(input('Digite um valor maior do que zero.:'))
while (x <= 0):  # o programa vai rodar até eu digitar um valor maior que 0.
    x = int(input('Digite um valor maior do que zero:'))
print('Você digitou {}. Encerrando o programa...'.format(x))
