import sys
entrada = sys.argv[1]


def case(data):
    dic = {
        'nome': 'Daniela',
        'idade': '27',
        'pais': 'Brasil'
    }
    try:
        return dic[data]
    except:
        print('Dado não encontrado: ' + data)


print(case(entrada))
