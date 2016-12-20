doencas = [1,2,3,4]
sintomas = [0]*4
option = '0'

def perguntas(option, doencas):
    option = input('Sente dor de cabeça?')
    if option == 'sim': sintomas [0] = '1'
    

    option = input('Sente febre?')
    if option == 'sim': sintomas [1] = '1'

    option = input('sente dor nos braços?')
    if option == 'sim': sintomas [2] = '1'

    option = input('Está pouco ou muito tonto?')
    if option == 'sim': sintomas [3] = '1'

def verifica(doencas):
    for i in range(1,5):
        endereco = str(i)+'.txt'
        print(endereco)

verifica(doencas)
print(sintomas)
print(doencas)
