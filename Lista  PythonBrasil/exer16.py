salario = float(input('Informe o valor da hora de trabalho '))
horas = int(input('informe a quantidade de horas trabalhadas '))

bruto = salario * horas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print('+ Salário Bruto : R$%0.2f' %(bruto))
print("- IR (11%)  R$", ir)
print('- INSS (8%)  R$', inss)
print('- Sindicato (5%)  R$',sindicato)
print('= Salario Liquido  R$',liquido)
