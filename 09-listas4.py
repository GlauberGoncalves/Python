# criar lista com range

lista = [1,2,3,4]

print(lista)

# append() adiciona novos indices e valores a lista

lista.append(5)
lista.append(6)
lista.append(7)

print(lista)

# index() retorna o indice do valor contido na lista
# porém deve ser usado quando você tem certeza que
# o valor existe na lista
# quando você não tem certeza se existe poderá usar
# o operador "in"

print(lista.index(5))
print(5 in lista)


# inserct() insere um valor na posição escolhida
# da lista

lista.insert(0,'dog')
print(lista)

# remove() remove o indice que contem o valor passado
# na função

lista.remove('dog')
print(lista)

# pop() remove o indice que foi passado como parametro
# e retorna o valor removido

print(lista.pop(-1)) #semelhante a função del()
print(lista)

# sort() ordena uma lista do menor para maior

lista2 = [4,3,2,1]
lista3 = ['glauber','juliana','mariana','amanda']

print(lista2)
print(lista3)

lista2.sort()
lista3.sort()

print(lista2)
print(lista3)

# reverse() ordena uma lista do maior para menor

lista2.reverse()
lista3.reverse()

print(lista2)
print(lista3)

# count() retorna quantas vezes um valor aparece na
# lista

print(lista.count(2))
print(lista.count(3))
print(lista.count(4))