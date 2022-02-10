

# Crea una función llamada get_minimum que dado una lista de números, devuelva el valor mínimo encontrado en el dicho array.

from functools import reduce

numeros = [32, 4, 6, 20, 0, 50]

get_minimum = reduce(lambda x, y :  min(x, y) , numeros)

print(get_minimum)