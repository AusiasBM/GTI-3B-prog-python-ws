


# Python soporta el concepto de funciones anónimas o lambda. Estas funciones no necesitan tener un nombre (pero pueden tener uno si queremos). 
# La sintaxis mínima es lambda parámetros : expresión.
    # parámetros --> son los valores que pasamos a la función.
    # expresión --> es la lógica que queremos que devuelva la función.

# ----------------------------------------------------------------------------------------------------------------------------------------
# Un ejemplo de uso de este tipo de funciones es cuando todo lo que queremos que haga la función es una simple línea. En este caso, podemos evitar el def:

res = lambda x, y : x * y
print(res(5, 2))

# En la función de arriba, x e y son los parámetros de entrada, mientras que x * y es la expresión que se evalúa y retorna. 
# Este código de arriba sería más o menos equivalente al siguiente:

def multiplica(x, y):
  return x * y

print(multiplica(5, 2))


# ----------------------------------------------------------------------------------------------------------------------------------------
# Las funciones lambda son diferentes de una función normal porque únicamente contienen una expresión, no pueden tener bloques y devuelven una función. 
# En este sentido, los dos códigos no son equivalentes del todo. 
# Más bien, la función lambda no devuelve el resultado de sumar x e y, sino más bien, la función que calcula esta suma.


# ----------------------------------------------------------------------------------------------------------------------------------------
# La potencia de una función lambda se ve cuando la utilizamos junto con otra función de primer orden como map, filter o reduce. 
# Ten en cuenta que estas tres funciones utilizan una función como primer parámetro. 
# En este sentido, podemos pasar una función lambda que se utilice una única vez. 
# A continuación, puedes ver los tres ejemplos de arriba implementados con funciones lambda:

#Ejemplo de map
nombres = ["Pepe", "ana", "juan", "Toni"]
resultado = map(lambda s : s.lower(), nombres)
print(list(resultado)) 

#Ejemplo de filter
nombres = ["Pepe", "ana", "juan", "Toni"]
resultado = filter(lambda s: len(s) > 3, nombres)
print(list(resultado)) 

#Ejemplo de reduce
from functools import reduce
lista = [2, 5, 7, 3]
print(reduce(lambda x, y : x + y, lista))



# ----------------------------------------------------------------------------------------------------------------------------------------