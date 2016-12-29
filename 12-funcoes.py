# trabalhando com modulos no python
#------------------------------------------------------------#
def menu():
    print('1: Informe a opção desejada')
    print('2: Olá')
    print('3: Como vai você?')
    print('4: tudo bem?')
    return int(input('informe a opção?: '))
    # retorna o numero da opção selecionada
#------------------------------------------------------------#    
def exp(n,ex):
    return n**ex

print(exp(5,2))




