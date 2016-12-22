
# range gera uma lista que irá do 1 paremetro até o
# ultimo -1
# exemplo

#inteiros = range(0,11)

inteiros = [1,2,3,4,5,6,7,8,9,10]
print(inteiros)

# in vefifica se o valor está na lista
# exemplo

boleana = range(5,9) in inteiros
print(boleana)

# comprimento da lista
# len()

print(len(inteiros))

# remove um elemento da lista
# del()

del inteiros[3]
print(inteiros)

# ponteiros
a = [1,2,3]
b = a
print(a)
del b[2]
print(a)

# clonando lista

c = [1,2,3,4]
d = c[:]
print(c)
print(d)
del d[2]
print(c)
print(d)