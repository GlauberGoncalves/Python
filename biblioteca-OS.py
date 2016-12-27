# Trabalhado com modulo OS no python

import os # faz a importação do modulo

# listdir('.') lista todos os arquivos do diretorio

count = 0
lista = os.listdir()

for i in lista:    
    print(i)

# getcwd mostra o diretorio atual
print(os.getcwd())

# mkdir cria diretorio/pasta

os.mkdir("glauber")


# makedirs cria pastas uma dentro da outra de uma
# só vez

os.makedirs("glauber/python/teste")

# renomeia pastas

os.rename("glauber","cursos")
