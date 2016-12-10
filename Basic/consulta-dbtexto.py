#consulta banco de dados em arquivo txt

db = open('cadastro.db','r')
print('-------Nomes--------\n')
print(db.read())
db.close()