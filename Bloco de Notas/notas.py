# Bloco de notas
option = 0
notas = [0] * 100
#--------------------------------------------------------------------
# Cria o menu principal
def menu():    
    print("Informe a opcao desejada\n")
    print("1: Cadastrar nova nota")
    print("2: Buscar nota")
    print("3: Apagar nota")
    print("4: Total de notas")
    print("5: Total de notas")
    return int(input("Opcao: ")) 
#--------------------------------------------------------------------#
# Cadastra nova nota

def novaNota(notas):
    i = 0    
    for i in range(100):
        if notas[i] == 0:
            print("Escreva sua nota n",i+1)
            notas[i] = input("\n")
            return 1
    return 0
#--------------------------------------------------------------------#
# Busca nota

def buscaNota(notas):
    numero_nota = int(input("Informe o numero da nota: "))
    numero_nota = numero_nota - 1
    if(notas[numero_nota] != 0):
        print("------------------------------------")
        print("Aqui esta a nota numero ",numero_nota + 1,": ")
        print("------------------------------------")
        print(notas[numero_nota])
        print("------------------------------------")
        return 1
    else:
        print("------------------------------------")
        return 0    

#--------------------------------------------------------------------#
# Inicio do programa

while option != 5:
    option = menu()
    if option == 1:
        print("--------------------------")
        if(not novaNota(notas)):
            print("Houve um erro ao cadastrar nota")
        else:
            print("----------------------------")
            print("OK, nota gravada com sucesso")            
        print("--------------------------")
    elif option == 2:        
        if (not buscaNota(notas)): print("Erro ao buscar nota ")        
    elif option == 3:
        print("--------------------------")
        print("\topcao 3")
        print("--------------------------")
    elif option == 4:
        print("--------------------------")
        print("\topcao 4")
        print("--------------------------")
    elif option == 5:
        print("--------------------------")
        print("\tAte Breve")
        print("--------------------------")