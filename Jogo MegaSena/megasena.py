from random import *

bolas = [0]*60
sorteadas = [0]*6
marcadas = [0]*6
pontos = 0
max_pontuacao = 0
anos = 0
contador = 0

def marcar(marcadas):
    for i in range(6):
        marcadas[i] = int(input('Informe %dº dezena: ' %(i+1)))

def restart(bolas):
    for i in range(60-len(bolas)):
        bolas.append(0)
        
    for i in range(0,60):
        bolas[i] = i+1

def sortear(bolas,sorteadas):
    for i in range(6):
        sorteadas[i] = choice(bolas)
        bolas.remove(sorteadas[i])

def conferir(marcadas,sorteadas):
    acertos = 0
    for i in range(6):
        if(marcadas[i] in sorteadas):
            acertos = acertos + 1
    return acertos    

restart(bolas)
marcar(marcadas)
sortear(bolas,sorteadas)
pontos = conferir(marcadas, sorteadas)

while(pontos < 6):
    restart(bolas)
    sortear(bolas,sorteadas)
    pontos = conferir(marcadas, sorteadas)

    if(pontos > max_pontuacao):
        max_pontuacao = pontos
        print(sorteadas)
        print(marcadas)
        print("pontos marcados %d" %(pontos))
        print("Tempo em anos: %d \n" %(anos))

    if(contador == 120):
        contador = 0
        anos = anos + 1
    
    contador = contador + 1

    if(anos > 100000):
        print("Desculpe...Já se passaram mais de 100 mil de anos e você não conseguiu ganhar")
        break