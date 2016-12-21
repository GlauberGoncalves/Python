# lê um arquivo com varios codigos de barra e após gera um
# novo arquivo com o codigo lido e a mensagem 'verdadeiro'
# ou 'falso' do lado
#-----------------------------------------------------------------------------------------#

# função gerar_validador recebe o codigo de barras sem
# o digito verificador e retorna o digito verificador

def gerar_validador(cod):    
    tamanho = len(cod)
    temp = [0] * 3

    # soma das posições impares
    if(tamanho%2 == 0):                         # caso o total de numeros do codigo seja par
        for i in range(0,tamanho,2):        
            temp[0] = temp[0]+ int(cod[i])      # soma posições impares
            temp[1] = temp[1]+ int(cod[i+1])    # soma posições pares
        print(temp[0])
        print(temp[1])
        temp[0] = temp[0]*3 + temp[1]           # aplicação da formula
        print(temp[0])
        temp[2] = 10 - (temp[0]%10)             # gerando digito verificador
        print(temp[2])
    else:                                       # caso o total de numeros do codigo seja impar        
        for i in range(0,int(tamanho),2):
            temp[0] = temp[0]+ int(cod[i])  # soma posições impares
            if( i != (tamanho-1)):
                temp[1] = temp[1] + int(cod[i+1])
        temp[0] = temp[0]*3 + temp[1]   # aplicação da formula
        temp[2] = 10 - (temp[0]%10)     # gerando digito verificador    
    return temp[2]
#---------------------------------------------------------------------------------------------------#

# função valida_codigo recebe o codigo de barras com codigo verificador
# e retorna 1 se o codigo for verdadeiro
# 0 para falso

def valida_codigo(cod):
    codigo = []
    temp = ''
    tam = int(len(cod))

    # transforma a variavel str em lista sem o codigo verificador
    for i in range(tam-1):
        temp = (temp + cod[i])
    correto = gerar_validador(temp)
    # confere o codigo verificador
    if (str(correto) == cod[-1]):        
        return 1
    else:
        return 0
#---------------------------------------------------------------------------------------------------#
def trata_linha(linha):
    string = ''
    for i in range(0,len(linha)-1):
        string = string + linha[i]
    return string
#---------------------------------------------------------------------------------------------------#    
"""temp = ''
arquivo = open('codigosdebarras.txt','r')
linha_tratada = []
codigos = arquivo.readlines()
for linha in codigos:
    temp = trata_linha(linha)    
    print(temp,'\t',valida_codigo(temp))
arquivo.close()"""
#---------------------------------------------------------------------------------------------------#    

# programa principal

"""print(valida_codigo('484848498418'))
print(valida_codigo('1234567890128'))
print(valida_codigo('15487948191526'))"""


validador = gerar_validador('123456789012')
print('codigo 1234567890128 validador ',validador)

#---------------------------------------------------------------------------------------------------#