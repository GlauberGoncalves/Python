# Dicionarios funcionam parecido com os structs na
# linguaguem C

estudante = {
    "nome": 'Glauber',
    "idade": 28,
    "sexo": 'masculino',
    "matricula": 1001010
    }


print('Nome do aluno: '+estudante['nome'])
print('Idade: '+str(estudante['idade']))
print('Sexo: '+estudante['sexo'])
print('Matricula: '+str(estudante['matricula']))

# criando dicionarios dinamicamente

pessoa = {}


pessoa["nome"] = input('Informe seu nome ')
pessoa["idade"] = input('Informe sua idade ')

print(pessoa["nome"])
print(pessoa["idade"])

