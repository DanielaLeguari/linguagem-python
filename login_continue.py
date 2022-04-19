"""Escreva um algoritmo que realize um login em um sistema
O usuário deve informar seu nome e senha"""
while True:
    nome = input('Qual é o seu nome?')
    if (nome != 'Lenhadorzinho'):
        continue
    senha = input('Qual a sua senha?')
    if (senha == 'UnInTeR'):
        break
print('Acesso concedido.')

