# trabalhando com modulos no python
#------------------------------------------------------------#
# cria um menu 
def menu():
    print('1: Informe a opção desejada')
    print('2: Olá')
    print('3: Como vai você?')
    print('4: tudo bem?')
    return int(input('informe a opção?: '))
    # retorna o numero da opção selecionada
#------------------------------------------------------------#    
# calcula expoente 
def exp(n,ex):
    return n**ex
#------------------------------------------------------------#    
# calcula valor do inss

def calcINSS(SalarioBruto):
    return SalarioBruto*0.06
#------------------------------------------------------------#    
# calcula rendimento da poupanca
def poup(valor, tempo):
    return (valor*0.05)*tempo

#------------------------------------------------------------#  
# menu()
# print(exp(5,2))
#
# Salario = 980.00
# SalarioLiquido = calcINSS(Salario)
# print(SalarioLiquido)
#
# print(poup(1000,2))
