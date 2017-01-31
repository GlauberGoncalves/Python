peso = float(input('informe o peso '))
excesso = 0.0
multa = 0

if peso > 50:
    exesso = peso - 50
    multa = exesso * 4
print('exesso: %2.3f\nMulta R$%2.2f' %(exesso, multa))


