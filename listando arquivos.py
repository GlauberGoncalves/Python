# Copia todos os arquivos
# copia os arquivos renomeando-os

import glob, os

count = 0

for file in glob.glob("*.pdf"):
    print(file)
    count = count + 1
    string = 'tratados/apostila'+str(count)+'.pdf'
    arq = open(file,'rb')
    new = open(string,'wb')
    buffer = arq.read()
    new.write(buffer)
    arq.close()
    new.close()
