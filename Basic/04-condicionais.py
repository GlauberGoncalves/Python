#Trabalhando com condicionais no Python

#operadores relacinais
    # >  - maior que
    # <  - menor que
    # >= - maior ou igual que
    # <= - menor ou igual que
    # == - igual a
    # != - diferente



idade = int(input('Informe a sua indade '))

# condicionao simples
print('Condicional simples\n')
if idade < 18:
    print('>>>Você é menor de idade')
else: print('>>>Você já é maior de idade')

# condicionao encorpado
print('\nCondicional encorpado\n')

if idade <= 0:
    print('>>>Você ainda não nasceu')
elif idade < 12:
    print('>>>Você é uma criança')
elif idade < 18:
    print('>>>Você é um adolescente')
elif idade < 60:
    print('>>>Você é adulto')
elif idade < 200:
    print('>>>Você é um idoso')
else: print('>>>Você já está no céu descansando')
