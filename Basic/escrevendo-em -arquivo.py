#Declaração de variaveis

nome = 'Glauber'
idade = '28'
sexo = 'marculino'

#escrevendo no arquivo

arquivo = open('encrevendo-em-arquivo.txt','w')
arquivo.write(nome)
arquivo.write('\n')
arquivo.write(idade)
arquivo.write('\n')
arquivo.write(sexo)
arquivo.close()
