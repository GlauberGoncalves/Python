tamanho = int(input('Informe o tamanho do arquivo em MB '))
velocidade = int(input('informe a velocidade em Mbps '))
tempo = tamanho/velocidade
tempo = tempo/60

if tempo < 1:
    print('Levará menos de 1 minuto ')
else:
    print('Levará aproximadamente %d minutos' %(int(tempo)))
