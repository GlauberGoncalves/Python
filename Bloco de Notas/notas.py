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
    print("5: Sair")
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
        print("\n")
        print(notas[numero_nota])
        print("------------------------------------")
        return 1
    else:
        print("------------------------------------")
        return 0    
#--------------------------------------------------------------------#
# apagar notas

def apagaNota(notas):
  n = int(input("Informe o numero da nota"))
  if(n>0 and n<=100):
    notas[n-1] = 0
    print("--------------------------------")
    print("Nota apagada com sucesso")
    return 1
  else: return 0  
#--------------------------------------------------------------------#
# total de notas

def totalNotas(notas):
  count = 0
  for i in range(0,100):
    if notas[i] != 0:
      count += 1
  return count    

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
        apagaNota(notas)
        print("--------------------------")
    elif option == 4:
        print("--------------------------")
        print("Total de notas: ",totalNotas(notas))
        print("--------------------------")
    elif option == 5:
        print("--------------------------")
        print("\tAté Breve")
        print("--------------------------")