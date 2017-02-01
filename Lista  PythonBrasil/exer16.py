t = float(input('informe o tamanho em m² '))
l = float(t / 3)

if l % 18 == 0:    
    print('voce precisara de %f latas ' %(l/18))
    print('Preço: R$ %0.2f' %((l/18)*80))
else:
    print('voce precisara de %f latas ' %((l//18+1)))
    print('Preço: R$ %0.2f' %((l//18 + 1) * 80))
