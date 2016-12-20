# mais listas

lista = ['glauber']

def cadastra(variavel):
    continua = True
    while continua:
        nome = input('Informe o nome: ')
        variavel.insert(0,nome)
        if (input('Deseja continuar?: ') == 'sim'):
            continua = True
        else: continua = False
    
cadastra(lista)
