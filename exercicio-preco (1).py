preco = float(input('Digite o preço do produto.:'))
perc_desc = float(input('Digite o percentual de desconto (0-100)%.:'))
desc = preco * (perc_desc /100)
final = preco - desc
print ('O preço do produto é {} e o desconto será de {} %'.format(preco, perc_desc))
print (' A valor calculado do desconto é {} e valor final é {}'.format(desc, final))
