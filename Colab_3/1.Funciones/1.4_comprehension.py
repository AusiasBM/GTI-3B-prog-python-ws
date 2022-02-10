

# Las funciones anteriores no son la única forma de trabajar con listas. Las comprehensions (o comprensiones) son una forma elegante de definir y crear listas basándonos en otras listas.

# ----------------------------------------------------------------------------------------------------------------------------------------
# Imagina que queremos crear una lista que multiplique por dos los elementos de otra lista. 
# Esto lo podríamos hacer de varias maneras: 
    # (1) de manera tradicional iterando la lista con un bucle,
    # (2) utilizando una función map(), pero también 
    # (3) con una comprehension. Observa el siguiente ejemplo que produce el mismo resultado de las 3 maneras:

valores = [2, 5, 12, 10]

#Manera tradicional
resultado = []
for i in valores:
  resultado.append(i * 2)
print(resultado)

#Ejemplo con map
resultado = map(lambda i : i * 2, valores)
print(list(resultado)) 

#Ejemplo con comprehension
resultado = [i * 2 for i in valores]
print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------
# Como puedes ver, en vez de crear una lista vacía y añadir cada elemento, simplemente definimos la nueva lista y su contenido en la misma línea. 
# La sintaxis de una comprehension es la siguiente:

# nueva_lista = [expression for item in list]

# Donde:

    # expression es una expresión que devuelva un valor o una llamada a una función.
    # item es el elemento iterable de la lista.
    # list es la propia lista.

# Tienes que tener en cuenta que no todos los bucles pueden ser reescritos como una comprehension. 
# Sin embargo, según vayas sintiéndote cómodo/a, puedes ir reemplazando algunos bucles por esta sintaxis. 
# En comparación con las funciones lambda, una comprehension puede ser más fácil de leer. 
# En principio, una comprehension funciona bien en muchos problemas donde también podrías utilizar un map(). 
# La diferencia principal es que el map() devuelve un objeto que tienes que transformar a lista, mientras que la comprehension ya devuelve una lista.

# ----------------------------------------------------------------------------------------------------------------------------------------
# Además, una comprehension también funciona bien cuando quieres aplicar un filter(), por lo que con una misma solución, puedes resolver problemas que requieran map() o filter().
# Esto se puede ver más fácil mediante la inclusión de condicionales, que se escriben normalmente con la siguiente sintaxis:

# nueva_lista = [expression for item in list (if conditional)]

# Fíjate en el siguiente ejemplo donde se crea una nueva lista con los elementos pares. Es fácil de leer, ¿verdad?

lista = [14, 5, 12, 16, 9, 7, 10]

nueva = [x for x in lista if x % 2 == 0]
print(nueva)

# ----------------------------------------------------------------------------------------------------------------------------------------
# En caso de querer hacer condicionales anidados, lo podrías hacer de la siguiente manera. 
# Observa cómo en el siguiente ejemplo nos quedamos con los pares mayores de 10:

lista = [14, 5, 12, 16, 9, 7, 10]

nueva = [x for x in lista if x % 2 == 0 if x > 10]
print(nueva)

# En el ejemplo anterior podríamos sustituir el if por un and y el resultado sería el mismo, pero la idea era mostrar un if anidado.
# También podemos emplear una sintaxis if-else. 
# En el siguiente ejemplo creamos una lista con los elementos pares y los impares los sustituimos por 0. Aquí cambiamos el orden del if-else y el for:

lista = [14, 5, 12, 16, 9, 7, 10]

nueva = [ x if x % 2 == 0 else 0 for x in lista ]
print(nueva)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Vamos a complicarlo un poco más. 
# Suponemos que tenemos que computar la traspuesta de una matriz (una matriz es una lista de listas). 
# Vamos a ver cómo lo podríamos hacer con un bucle tradicional:

traspuesta = []
matriz = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matriz[0])): #range(4)
    fila_traspuesta = []

    for fila in matriz:
        fila_traspuesta.append(fila[i])
    traspuesta.append(fila_traspuesta)

print(traspuesta)

# Como puedes ver, esto se calcula con un bucle anidado. A continuación puedes ver cómo podrías obtener lo mismo con una comprehension:

matriz = [[1, 2, 3, 4], [4, 5, 6, 8]]
traspuesta = [[ fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(traspuesta)

# Los bucles anidados debes leerlos al revés. En el caso anterior, se ejecuta primero for i in range(len(matriz[0])) y después fila[i] for fila in matriz. 
# Por tanto, primero se asigna un valor a i, y después el item fila[i] se añade a la nueva lista traspuesta.

# Como puedes ver, si una comprehension hace que tu código sea difícil de leer, quizás es mejor utilizar una alternativa. 
# Por último, recuerda que una comprehension puede trasformarse en un bucle, pero no todos los bucles pueden trasformarse en una comprehension.

# ----------------------------------------------------------------------------------------------------------------------------------------


