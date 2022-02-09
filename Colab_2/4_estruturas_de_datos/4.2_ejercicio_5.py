

# Calcular la cantidad de números impares que hay en una lista de enteros.

lista = [10, 11, 12, 13, 14]

cantidad = 0

for i in lista:
    if i % 2 != 0:
        cantidad += 1

print(cantidad)