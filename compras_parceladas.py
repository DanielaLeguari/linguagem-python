""" Uma loja de departamentos está oferecendo diferentes formas de pagamento,conforme
opções listadas a seguir. Faça um algoritmo que leia o valor total de uma compra e calcule
o valor do pagamento final de acordo com a opção escolhida.Se a escolha for por
pagamento parcelado, calcule também o valor de cada parcela.
Ao final, apresente o valor total da compra e o valor das parcelas:
Pagamento à vista – conceder desconto de 5%;
Pagamento em 3x – o valor não sofre alterações;
Pagamento em 5x – acréscimo de 2%;
Pagamento em 10x – acréscimo 8%."""

print('Pagamento:')
print('1- Pagamento à vista.')
print('2- Parcelamento em 3x.')
print('3- Parcelamento em 5x.')
print('4- Parcelamento em 10x.')
print('Pressione outra tecla para sair.')
op = int(input('Qual forma de pagamento deseja fazer?'))
valor = float(input('Qual é o valor da compra?'))
if (op == 1):
    valor_final = valor - (valor * 0.05)
    print('Produto comprado à vista. Total a pagar R${}'.format(valor_final))
if (op == 2):
    valor_final = valor
    parcela = valor_final / 3
    print('Produto comprado em 3 x. Total a pagar R${}, valor da parcelaR${}'.format(valor_final, parcela))
if (op == 3):
    valor_final = valor + (valor * 0.02)
    parcela = valor_final / 5
    print('Produto comprado em 5 x. Total a pagar R${}, valor da parcelaR${}'.format(valor_final, parcela))
if (op == 4):
    valor_final = valor + (valor * 0.08)
    parcela = valor_final / 10
    print('Produto comprado em 10 x. Total a pagar R${}, valor da parcelaR${}'.format(valor_final, parcela))
else:
    print('Operação inválida!')

