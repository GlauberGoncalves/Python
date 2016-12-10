import sys

name = ' '
age  = ' '
hobby = ' '
op = '1'

# Gravando dados no arquivo
while op == '1':
    name = input("What's your name? ")
    age  = input("What's your age? ")
    hobby = input("What's your hobby? ")
    print("\n\nIt's all right?")
    print("-----------------")
    print("Name:\t",name)
    print("age:\t",age)
    print("mother:\t",hobby)
    print("-----------------")

    file = open("peaple.db","a")
    file.write(name)
    file.write(' ')
    file.write(age)
    file.write(' ')
    file.write(hobby)
    file.write('\n')
    op = input("1 - cadastrar ")
file.close()

# Acessando dados de arquivo

arquivo = open("peaple.db","r")

for i in file.readline():
    print(file)
    
    
arquivo.close()