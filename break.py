"""Escreva um algoritmo que fique recebendo frases ou palavras digitadas pelo usuário
Encerre o algoritmo quando a palavra sair for digitada"""
print('Digite uma mensagem que irei repetir para você.:')
print('Digite "sair" para encerrar.')
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('Encerrando o programa...')
