#cadastro de clientes
i = 1
nome = 'x'
db = open('cadastro.db','a')

maximo = int(input('Quantos nomes deseja cadastrar? '))
for i in range(maximo):
    nome = input("Nome: ")    
    db.write(nome)
    db.write('\n')    
db.close()
