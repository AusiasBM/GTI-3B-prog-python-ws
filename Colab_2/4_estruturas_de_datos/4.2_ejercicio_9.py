

# Dada una lista de enteros, elegir un número aleatorio de la lista.

import random

lista = [11, 9, 20, 7, 2]

index = random.randint(0, len(lista)-1)

print(lista[index])