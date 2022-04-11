valor_dia = 60
valor_km = 0.15
qtd_dia = float(input('Digite a quantidade de dias que o carro foi alugado.:'))
qtd_km = float(input('Digite a quantidade de quilômetros rodados.:'))
preco_pagar = (qtd_dia * valor_dia) + (qtd_km * valor_km)
print ('A quantidade de dia {}, quantidade de km {}'.format(qtd_dia,qtd_km))
print('O valor a pagar é R${}.'.format(preco_pagar))
