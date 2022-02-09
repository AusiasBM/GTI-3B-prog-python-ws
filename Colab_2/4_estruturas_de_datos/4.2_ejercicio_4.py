
# Dada una lista de enteros, averiguar si el primer o el último elemento es el mayor y sustituir el resto de elementos por éste (sin contar el primero el último). Por ejemplo, la lista [11, 5, 9, 7] debería quedar como [11, 11, 11, 7].

lista = [10, 11, 12, 13, 14]

mayor = 0

if lista[0] > lista[-1]:
    mayor = lista[0]
else:
    mayor = lista[-1]

posicion = 1
for i in lista:
    if posicion < (len(lista)-1):
        lista[posicion] = mayor;

    posicion += 1

print(lista)