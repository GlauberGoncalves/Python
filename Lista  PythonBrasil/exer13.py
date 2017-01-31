h = float(input('informe sua altura '))
sexo = input('informe seu sexo m ou f ')

if sexo == 'm':
    ideal = (72.7 * h) - 58
elif sexo == 'f':
    ideal = (62.1 * h) - 44.7

print('Seu peso ideal é %2.f' %(ideal))
