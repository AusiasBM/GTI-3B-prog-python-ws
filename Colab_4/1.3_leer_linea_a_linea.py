

# Aunque la función read() se utiliza a menudo, Python ofrece otras funciones que nos permiten leer un fichero línea a línea. 
# La función readline() lee, como su nombre indica, una línea del fichero:

f = open("fichero.txt", mode="rt", encoding="utf-8")

texto = f.readline()
print("Leemos una línea: "+texto)

texto = f.readline()
print("Leemos otra línea: "+texto)

f.close()

# Podemos recorrer un fichero mediante bucles for y while de una manera sencilla. Observa estos ejemplos:

f = open("fichero.txt", mode="rt", encoding="utf-8")

linea = f.readline()
while linea != "" :
  print("he leído1: " + linea)
  linea = f.readline()

f.close()

# otra forma de leer un fichero linea a linea

f = open("fichero.txt", mode="rt", encoding="utf-8")

for linea in f:
  print("he leído2: " + linea)

f.close()

#stdout.write() no mete una línea en blanco como un print

# Con la función readlines() podemos leer todas las líneas del fichero. 
# En este caso, nos devuelve una lista donde cada elemento es una línea leída:

f = open("fichero.txt", mode="rt", encoding="utf-8")

lista_lineas = f.readlines()
print("Lista de líneas leídas: ", lista_lineas)

f.close()

# En ocasiones queremos añadir información a un fichero ya existente. 
# Esto lo podemos hacer abriendo el fichero con la opción a y utilizando después la función write():

f = open("fichero.txt", mode="at", encoding="utf-8")

f.write("Esto es un mensaje añadido. \n")

f.close()


"""De forma similar a la función readlines(), también tenemos disponible la función writelines() 
para escribir en un fichero múltiples líneas. 
Esta función, recibe como parámetro la lista de líneas a escribir:"""

f = open("fichero.txt", mode="at", encoding="utf-8")

f.writelines(["Línea añadida de un listado \n", "otra línea añadida \n"])

f.close()

"""No obstante, también puedes utilizar la opción de lectura-escritura con r+, que nos permite realizar ambas operaciones. 
En el caso de escribir, lo que hace es añadir al fichero y no machacar lo que haya (cosa que sí que hace la opción w):"""

f = open("fichero.txt", mode="r+t", encoding="utf-8")

texto = f.read(10)
print("Leemos 10 caracteres: "+texto)

f.write("Esto es un mensaje añadido. \n")

f.close()

"""Hasta ahora hemos visto que para trabajar con un fichero es importante tanto abrirlo como cerrarlo. 
En Python existe un mecanismo que asegura que estas operaciones se hacen automáticamente: un bloque with. 
Esta estructura es útil para manejar recursos como ficheros. Observa cómo se utilizaría en el siguiente ejemplo:"""

with open("fichero.txt", mode="rt", encoding="utf-8") as f:
  for linea in f:
    print("he leído: " + linea)