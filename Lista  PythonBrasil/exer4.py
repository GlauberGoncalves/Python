# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média

media = 0

for i in range(1,5):
    media += float(input('informa a nota %dª ' %(i)))
print("A sua media é %f" %(media/4))    
