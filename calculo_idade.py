"""Desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual.
Calcule a sua idade e apresente na tela.
Para fins de simplificação, despreze o dia e o mês do ano. Após o cálculo, verifique se a idade é
maior ou igual a 18 anos e apresente na tela uma mensagem informando que já é possível tirar a
carteira de motorista caso seja de maior."""

nasc = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade = ano_atual - nasc
print('Você tem {} anos.'.format(idade))
if (idade >= 18):
    print('Você é maior de idade. Já é possível tirar a carteira de habilitação.')
