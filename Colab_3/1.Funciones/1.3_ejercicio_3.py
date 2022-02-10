

# Crea una función llamada every_element_greater_than que tome por parámetro un número y una lista numérica y devuelva 
# True si todos los elementos son mayores que el número pasado por parámetro y False en caso contrario.

numeros = [32, 4, 6, 20, 10, 50]
num = 2

print(list(filter(lambda n: n < num, numeros)) == [] )

