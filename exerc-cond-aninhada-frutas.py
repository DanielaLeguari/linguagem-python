print('Escolha o que deseja comprar.:')
print('1 - para maçã.')
print('2 - para laranja.')
print('3 - para banana.')
produto = int(input('Qual a sua escolha?'))
qtd = int(input('Quantidade?'))
if (produto == 1):
    pagar = qtd * 2.3
    print('Voce comprou {} maçãs e o valor total a pagar é R$ {}'.format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd * 3.6
        print('Voce comprou {} laranjas e o valor total a pagar é R$ {}'.format(qtd, pagar))
    else:
        if (produto == 3):
            pagar = qtd * 1.85
            print('Voce comprou {} bananas e o valor total a pagar é R$ {}'.format(qtd, pagar))
        else:
            print('Produto inexistente!')
