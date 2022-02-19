

# Los diccionarios son un ejemplo de estructura de datos donde almacenamos pares de tipo clave-valor. Las claves no se pueden repetir.

# En Python contamos con el tipo dict, el cual representa un diccionario de tipo clave-valor. 
# La creación de un diccionario en Python es sencilla. 
# Primero veremos cómo podemos crear un diccionario vacío empleando dos sintaxis diferentes:

dic1 = {}
dic2 = dict()

# también podemos inicializar un diccionario con unas claves y valores específicos empleando la sintaxis de tipo llave:

dic = {123: "Juan", 456: "Maria", 789: "Pedro"} 
print(dic)

# Podemos emplear cualquer tipo de dato mientras sea inmutable.

dic = { 11: 42.1, "usuario2": 33, (1,3,4): "valor3" }
print(dic)


# Leer valores de un diccionario

dic = { "usuario1": 23, "usuario7": 10, "usuario2" : 4 }
result = dic["usuario1"] + dic["usuario2"]
print(result)

# Más operaciones

dic = {123: "Juan", 456: "Maria", 789: "Pedro", "sdfas": 344} 
print(dic)

#Acceder a un valor a partir de su clave
res = dic[456]
print("El valor de la clave 456 es: ",res)

#Otra forma de acceder, pero esta no da error si no existe, sino que devuelve "None"
res = dic.get(45116)
print("El valor de la clave 45116 es: ",res)

#Obtener el tamaño de un diccionario
res = len(dic)
print("El tamaño del diccionario es: ",res)

#Comprobar si una clave existe
res = 456 in dic
print("La clave 456 existe? ",res)

# Podemos añadir nuevos datos al diccionario o modificar los que ya tiene

d = { 'usuario1': 23, 'usuario7': 10, 'usuario2' : 4 }
d['usuario3'] = 11
d['usuario1'] = 0
print(d)

dic = {123: "Juan", 456: "Maria", 789: "Pedro", "sdfas": 344} 
print(dic)

#Añadir/modificar un item
dic[122] = "Eva" #si no existe lo añade
dic["sdfas"] = 355 #si existe lo modifica
print("Modifico clave 'sdfas' y añado la 122: ",dic)

#Otra forma de añadir/modificar el valor de una clave
dic.update({124: "Manolo"}) #si no existe lo añade
dic.update({123: "Pepe"}) #si existe lo modifica
print("Modifico clave 123 y añado la 124: ",dic)

#Eliminar un elemento por su clave
del dic[456]
#Otra forma mediante la que nos podemos guardar el valor eliminado
#res = dic.pop(456) 
print("Elimino la clave 456: ",dic)

#Eliminar todo el diccionario y la variable
#del dic
#Eliminar todos los datos pero mantener la variable
dic.clear()
print("Elimino el diccionario: ",dic)

# Otra operación bastante común cuando usamos diccionarios es recorrer las claves que tenemos en un diccionario 
# para acceder a sus correspondientes valores. Esto lo podemos realizar de varias maneras:

dic = {123: "Juan", 456: "Maria", 789: "Pedro", "sdfas": 344}

#Recorrer un diccionario
print("Recorremos un diccionario:")
for i in dic:
  print("Clave: ",i," Valor: ",dic[i])

#Otra forma de recorrerlo un diccionario
print("\nOtra forma de recorrerlo:")
for i in dic.keys():
  print("Clave: ",i," Valor: ",dic[i])

#Recorrer sólo por los valores
print("\nPor valores:")
for i in dic.values():
  print(i)

#Otra forma de recorrer en dos variables 
print("\nPor claves y valores:")
for k, v in dic.items():
  print("Clave: ",k," Valor: ",v)


# Por último, también puedes utilizar una comprehension sobre un diccionario. Lo único que cambia con respecto a listas es que tienes que definir la clave.
# Observa en el siguiente ejemplo cómo creamos un diccionario de aquellos items mayores que 100:

dic = {"first": 20, "second": 556, "third": 212, "fourth": 89}

nuevo_dic = {i : dic[i] for i in dic.keys() if dic[i] > 100}
print(nuevo_dic)

"""
    Aquí tienes algunas de las funciones más interesantes que puedes utilizar con diccionarios:

    clear() Vacía un diccionario eliminando toads las claves y valores.
    copy() Devuelve una copia del diccionario.
    fromkeys() Devuelve una nueva copia del diccionario pero solo con unas claves concretas.
    get() Devuelve el valor de una clave concreta, o None si no existe.
    items() Devuelve una lista de items como una tupla para cada par de clave-valor.
    keys() Devuelve una lista de todas las claves.
    pop() Elimina el item que tenga una clave determinada y lo guarda en una variable.
    popitem() Elimina el último par de clave-valor.
    update() Modifica el valor de una clave determinada, o lo añade si no existe.
    values() Devuelve una lista de todos los valores.

"""

# Hasta ahora hemos visto cómo podemos trabajar con diccionarios con un valor para cada clave, 
# pero también es común encontrar casos donde necesitamos tener múltiples pares clave-valor para cada item.

# Imagina que no es suficiente con conocer el nombre de una persona, 
# sino que necesitamos otros datos como su fecha de nacimiento y población. 
# En este caso, podemos pensar que cada uno de los datos tendría un aspecto similar al siguiente ejemplo:

persona = {
    "nombre" : "Paco",
    "fecha" : "02/04/1980",
    "poblacion" : "Valencia"
}

#La forma de acceder a los datos de una persona sería así:
print(persona["nombre"])
print(persona["fecha"])
print(persona["poblacion"])

# Teniendo en cuenta esto, podríamos tener una clave asociada a cada persona:

persona = {
    "nombre" : "Paco",
    "fecha" : "02/04/1980",
    "poblacion" : "Valencia"
}

persona2 = {
    "nombre" : "Ana",
    "fecha" : "22/10/1985",
    "poblacion" : "Gandia"
}

dic = {123: persona, 456: persona2}
print(dic)

