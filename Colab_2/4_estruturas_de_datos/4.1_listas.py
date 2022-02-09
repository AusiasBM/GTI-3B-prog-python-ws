

#Creamos una lista:
datos = [] #vacía
datos = list() #otra forma
datos = [4, "mensaje", -15, 3.4] #con elementos

# Mostrar dato
print("Elemento de la pos 2:", datos[2])

#Modificamos un valor de la lista
datos[2] = 10
print(datos)

#Índices negativos (del final hacia adelante, siendo -1 el último)
print("Penúltimo elemento:", datos[-2])

# Ejemplos donde troceamos una lista, todos devuelven otra lista
datos = [10, 11, 12, 13, 14]
print(type(datos))

#Slicing para obtener una porción de la lista 
print("Desde la posición 1 hasta una anterior a la 3:", datos[1:3])
print("Los dos primeros:", datos[:2])
print("Desde la posición 1 hasta el final:", datos[1:])
print("Desde la posición -1 hasta el final: ", datos[-1:])
print("Desde la posición 1 a la -2 (no incluida): ", datos[1:-2])
print("Desde la posición -4 a la -2 (no incluida): ", datos[-4:-2])
print("Aunque tenga un elemento, lo que devuelve la operación de slicing continúa siendo una lista:", type(datos[-1:])) 
print("Si no especificamos índices, obtenemos todos los valores: ", datos[:]) 

#Repetir elementos
print("Repetimos la lista dos veces:", datos * 2)
print("Creamos una lista con 5 ceros:", [0] * 5)

"""
    También podemos utilizar steps para saltarnos algunos elementos en la operación de slicing. 
    En el siguiente ejemplo, el valor 3 indica que nos saltaremos 3 elementos después de cada selección. 
    Si no le pasamos steps, se considera 1:
"""
datos = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print("Desde la posición 2 hasta la 7 (no incluida) pero de 3 en 3: ", datos[2:7:3]) 

print("Devuelve desde el principio hasta la posición 7 ( no incluida ), pero de 3 en 3: ", datos[:7:3])

"""
    Las listas nos ofrecen varios métodos muy útiles para trabajar con ellas, entre los que destacamos los siguientes:

    len() Devuelve la longitud de la lista.
    append() Añade un elemento al final de la lista.
    clear() Elimina todos los elementos de la lista, dejándola vacía.
    copy() Crea una copia de la lista.
    count() Cuenta cuántas veces aparece un elemento en la lista.
    extend() Añade los elementos de una lista al final de otra.
    index() Devuelve la posición de un elemento dentro de la lista.
    insert() Añade un elemento en una determinada posición de la lista.
    pop() Elimina un elemento de la lista y lo devuelve.
    del() Elimina un elemento de la lista por su posición.
    remove() Elimina un elemento de la lista por su valor.
    reverse() Invierte el orden de elementos de una lista.
    sort() Ordena una lista. Con el parámetro reverse=True especificamos que sea orden inverso.

    En el siguiente enlace puedes encontrar todas las funciones: https://python-reference.readthedocs.io/en/latest/docs/list/
"""

# Ejemplo 1 ***************************************************************************

datos = [4, "mensaje", -15, 3.4]

#Obtener la longitud de una lista
longitud = len(datos)
print(longitud)

#Añadir un elemento al final
datos.append(12)
print("Añado el 12 al final: ", datos)

#Añadir un elemento en una posición determinada (sin machacar el existente)
datos.insert(2,"nuevo_elemento")
print("Añado 'nuevo_elemento' en pos 2: ", datos)

#Buscar un elemento
print("Posición del -15:", datos.index(-15))
print("Está el -15?:", -15 in datos)

#Combinar dos listas
datos.extend([55, 22])
print("Combino dos listas: ", datos)

# Ejemplo 2 ***************************************************************************

datos = [4, "mensaje", -15, 3.4, -15, 25, 12]

#Eliminar un elemento (si hay varios, el primero que encuentra)
datos.remove(-15)
print("Elimino el -15: ",datos)

#Eliminar el elemento de determinada posición
del(datos[2])
#Otra forma mediante la que nos podemos guardar el valor eliminado
#res = datos.pop(2) 
print("Elimino el de la pos 2: ",datos)

#Vaciar parcialmente una lista
datos[:2] = []
print("Vacio desde la pos 0 hasta la 2: ",datos)

#Vaciarla totalmente
#datos = []
#Otra forma
#datos.clear()
#Otra forma que borra incluso la lista
#del(datos)
print("La vacío entera: ",datos)

# Ejemplo 3 ***************************************************************************

datos = [4, "mensaje", -15, 3.4, -15, 25, 12]

#Contar cuántas veces aparece un elemento en la lista
res = datos.count(-15)
print("Veces que aparece el -15: ",res)

#Encontar el índice de un elemento de la lista (su primera aparición)
res = datos.index(-15)
print("Posición del -15: ",res)

#Ordenar de varias formas. Observa como podemos ordenar por longitud:
datos = ["esto", "es", "un", "mensaje"]
datos.sort()
print("Nuevos datos ordenados:", datos)
datos.sort(key=len)
print("Nuevos datos ordenados por longitud:", datos)

#Invertir: datos.reverse()
#Copiar: copia = datos.copy()

# Recorrer una lista con un for ***************************************************************************

datos = [4, "mensaje", -15, 3.4]

for i in datos:
  print(i)

# Comprobar si un item está en una lista ***************************************************************************

#Ejemplo con in  -------------------------
datos = [4, "mensaje", -15, 3.4]

is_34 = 3.4 in datos
print(is_34)

is_23 = 23 in datos
print(is_23)

#Ejemplo manual  -------------------------
lista = [5, 2, 3, 7, 4, 1, 7]
encontrado = False
i = 0

while (not encontrado) and (i < len(lista)): #Los paréntesis son para facilitar la lectura, pero no son necesarios
  if lista[i] == 7:
    print("Encontrado en posición "+str(i))
    encontrado = True
  i += 1 #No existe la instrucción i++

if not encontrado:
  print("No se ha encontrado")

# Instrucción break, nos permite romper un bucle en cualquier momento ***************************************************************************

for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    break

print("Fin")

# Instrucción continue, para romper una iteración determinada ***************************************************************************

for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    continue
  print("Este código sólo se ejecuta si no entra por el if, ya que el continue se carga la iteración")

print("Fin")

# Modulo random nos permite realizar acciones aleatorias ***************************************************************************

import random
  
#imprimimos un valor aleatorio
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(lista))

#barajamos una lista
random.shuffle(lista)
print(lista)

#creamos un entero aleatorio entre 1 y 4 (ambos incluidos)
res = random.randint(1, 4)
print(res)