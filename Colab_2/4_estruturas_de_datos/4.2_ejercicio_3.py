
# Dadas dos listas de longitudes diferentes, averiguar si el primero o el último elemento de ambas listas es el mismo. En este caso, eliminar dicho elemento y mostrar las listas resultantes.

lista1 = [10, 11, 12, 13, 14]
lista2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

if lista1[0] == lista2[0]:
    del(lista1[0])
    del(lista2[0])
elif lista1[-1] == lista2[-1]:
    del(lista1[-1])
    del(lista2[-1])

print(lista1)
print(lista2)