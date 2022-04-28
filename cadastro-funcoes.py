"""
Suponha que você é um colecionar de jogos
de videogame. Escreva um algoritmo que
permita cadastrar esses jogos informando o
nome e a qual videogame ele pertence
Para isso, crie um menu de opções contendo:
cadastrar novo item, listar tudo que foi
cadastrado e sair
Para resolver esse exercício, crie pelo menos
uma função para cada item do menu
Além disso, armazene todos os dados em
um arquivo de texto que deve ser salvo em
disco e manter os dados cadastrados
"""
def valida_int(pergunta, min, max):  #função de validação
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'wt+')  # w abrir arquivo para a escrita e t arquivo texto, + criação caso não exista.
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo {} criado com sucesso!\n'.format(nomeArquivo))


def existeArquivo(nomeArquivo):  #try tentativas, se ter sucesso acontece se não tratar a excessão
    try:
        a =open(nomeArquivo,'rt') # r leitura e t arquivo txt
        a.close()
    except FileNotFoundError:
        return False  # se der erro dá erro
    else:
        return True

def listarArquivo(nomeArquivo):  #função para mostrar o que tenho cadastrado no arquivo.
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())   #faz o print na tela de todos os dados do arquivo.
    finally:
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
     try:
         a = open(nomeArquivo,'at')  #caso de erro
     except:
         print('Erro ao abrir o arquivo.')
     else:
         a.write('{};{}\n'.format(nomeJogo, nomeVideoGame)) #caso Nâo erro
     finally:                #tanto faz
         a.close()

# programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no pc')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('Menu')
    print(' 1 - Cadastrar novo item ')
    print(' 2 - Listar cadastros ')
    print(' 3 - Sair ')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:#criar o menu de fato
        print('Opção de cadastrar novo item selecionado ... \n')
        nomeJogo = input('Nome do Jogo:')
        nomeVideoGame = input('Nome do VideoGame:')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)
    elif op == 2:
        print('Opção de listar novo item selecionado ... \n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa!')
        break



