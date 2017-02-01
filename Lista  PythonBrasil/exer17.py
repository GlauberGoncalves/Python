t = float(input('informe o tamanho em m² '))
t = t + (t*0.1)
def arredondar(numero):
    if numero > 0:
        if numero < 1:
            return 1
        elif(numero - int(numero) > 0):            
            return int(numero) + 1
        
        else:
            return numero
    else:
        return 0
    
# quantidade de litros inteira
if t % 6 == 0:
    l = float(t / 6)
else:
    l = float(t//6 + 1)

# latas de 18l
if l % 18 == 0:    
    print('voce precisara de %d latas ' %(l/18))
    print('Preço: R$ %0.2f' %((l/18)*80))
    print('---------------------------------------')
else:
    print('voce precisara de %d latas ' %((l//18+1)))
    print('Preço: R$ %0.2f' %((l//18 + 1) * 80))
    print('---------------------------------------')

# galoes de 3,6l

if l % 3.6 == 0:    
    print('voce precisara de %d galoes ' %(l/3.6))
    print('Preço: R$ %0.2f' %((l/3.6)*25))
    print('---------------------------------------')
else:
    print('voce precisara de %d galoes ' %((l//3.6+1)))
    print('Preço: R$ %0.2f' %((l//3.6 + 1) * 25))
    print('---------------------------------------')
# as 2 latas
    l18 = (l//18)
    l36 = (((l / 18) - l18) * 18)/3.6
    if l36 <= 3:
        preco = 80*(l18)+ (25 *(arredondar(l36)))
        print('voce precisara de %d latas e %d galoes ' %(l18, arredondar(l36)))
        print('Preço: R$ %0.2f' %(preco))
        print('---------------------------------------')
    else:
        preco = 80 * l18
        l18 += 1
        l36 = 0
        print('voce precisara de %d latas e %d galoes ' %(l18, arredondar(l36)))
        print('Preço: R$ %0.2f' %(preco))
        print('---------------------------------------')        
