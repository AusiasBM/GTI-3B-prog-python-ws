
# Hasta ahora hemos visto que existen estructuras de datos que podemos recorrer con bucles, como strings, listas, diccionarios, etc. 
# Estas estructuras son estructuras iterables.

#recorremos un string
palabra = "hola"
for i in palabra:
  print(i)

#recorremos una lista
lista = [2, 5, 8, 0, 11]
for i in lista:
  print(i)

#recorremos un diccionario
dic = {123: "Juan", 456: "Maria", 789: "Pedro"}
for i in dic:
  print(i)



# Teniendo una estructura iterable, podemos utilizar la función iter pasándole esta estructura, de manera que nos devuelve lo que se denomina un iterador. 
# Este iterador lo podemos utilizar para recuperar el siguiente valor cada vez que sea necesario mediante la función next. 
# De esta forma, no hace falta tener todos los datos a la vez, sino ir obteniéndolos cada vez que sean necesarios:

lista = [2, 5, 8, 0, 11]

#obtenemos un iterator sobre la lista
iterador = iter(lista)

#utilizamos next cada vez que queremos el siguiente dato del iterador
print("Ahora me hace falta un dato")
print(next(iterador))
print("Ahora me hace falta otro")
print(next(iterador))
print("Ahora otro")
print(next(iterador))




# Podemos utilizar iteradores sobre estructuras que ya tengamos (como una lista o un diccionario), 
# pero en ocasiones la secuencia de datos viene dada por una función que genera estos datos. Este tipo de funciones, se denominan funciones generadoras.

# Una función generadora es una función que devuelve un generador. 
# Este generador no es la secuencia de datos en si, sino que cada vez que se le pasa como parámetro a next devolverá un valor nuevo generado por la función.

# Para construir una función generadora, simplemente tenemos que utilizar yield en vez de return, pero el resto del código es similar. 
# Lo mejor es verlo con un ejemplo. La siguiente función genera valores pares hasta el infinito, pero simplemente se obtiene un nuevo valor cada vez que se llama al generador:

#Función generadora de números pares
def numeros():
  i = 0
  #bucle infinito  
  while True:
    yield i
    i+=2

#La función generadora nos devuelve un generador
generador = numeros()

#utilizamos next cada vez que queremos generar un nuevo dato
print("Ahora me hace falta un dato")
print(next(generador))
print("Ahora me hace falta otro")
print(next(generador))
print("Ahora otro")
print(next(generador))

# Cuando la función generadora se llama, devuelve el generador sin tan siquiera comenzar la ejecución de la función. 
# Cuando llamamos a next la primera vez, la función se ejecuta hasta encontrar el yield, 
# que devuelve el valor indicado y que congelará la ejecución de la función hasta la próxima vez que pidamos un nuevo valor.

# Ahora ejecuta el siguiente código, donde hemos puesto algunos comentarios para observar mejor la traza de ejecución:

#Función generadora de números pares
def numeros():
  print("NUMEROS: inicio de la función")
  i = 0
  #bucle infinito  
  while True:
    print("NUMEROS: antes del yield")
    yield i
    print("NUMEROS: después del yield")
    i+=2

#La función generadora nos devuelve un generador
generador = numeros()
print("Después de llamar a la función y obtener el generador")

#utilizamos next cada vez que queremos generar un nuevo dato
print("Ahora me hace falta un dato")
print(next(generador))
print("Ahora me hace falta otro")
print(next(generador))
print("Ahora otro")
print(next(generador))


# No es necesario que una función generadora tenga un bucle infinito. Puedes transformar a funciones generadoras la mayoría de funciones que devuelvan una secuencia:

#Función generadora de números pares
def numeros():
  for n in range(10):
    if n % 2 == 0:
      yield n

#La función generadora nos devuelve un generador
generador = numeros()

print(next(generador))
print(next(generador))
print(next(generador))

# En este caso, puedes recorrer el generador de la misma forma que recorres cualquier tipo de estructura iterable (p.e. listas). Esto, lo que hace es ir pidiendo valores hasta que ya no queden:

#Función generadora de números pares
def numeros():
  for n in range(10):
    if n % 2 == 0:
      yield n

#La función generadora nos devuelve un generador
generador = numeros()

#Recorremos el generador
for i in generador:
  print(i)




