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
        temp[0] = temp[1]*3 + temp[0]           # aplicação da formula        
        temp[2] = 10 - (temp[0]%10)             # gerando digito verificador
        if(temp[2] == 10):
            return 0
        return temp[2]
    else:                                       # caso o total de numeros do codigo seja impar        
        for i in range(0,int(tamanho),2):
            temp[0] = temp[0]+ int(cod[i])  # soma posições impares
            if( i != (tamanho-1)):
                temp[1] = temp[1] + int(cod[i+1])
        temp[0] = temp[0]*3 + temp[1]   # aplicação da formula
        temp[2] = 10 - (temp[0]%10)     # gerando digito verificador
        if(temp[2] == 10):
            return 0
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
#lendo arquivo com codigos de barra
def gera_relatorio(nome):
    temp = ''
    cadeia = ''
    verificador = ''
    arquivo = open(nome,'r')
    arquivo2 = open('codigostratados.txt','w')
    linha_tratada = []
    codigos = arquivo.readlines()
    for linha in codigos:
        temp = trata_linha(linha)
        if valida_codigo(temp) == 1:
            verificador = 'verdadeiro'
        else:
            verificador = 'falso'
        cadeia = temp+'\t'+verificador+'\n'
        arquivo2.write(cadeia)
    arquivo2.close()
    arquivo.close()
    return 1
#---------------------------------------------------------------------------------------------------#    
# programa principal

endereco = input('Informe o endereço do arquivo com os codigos de barra\n')
if(gera_relatorio(endereco)):
    print('Arquivo codigostradasdos.txt gerado com sucesso.')
else:
    print('Ocorreu um erro ao gerar o relatorio')
 
#Por hoje é só pepessoal :b
#---------------------------------------------------------------------------------------------------#    