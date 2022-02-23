
# Para leer y escribir en un fichero en Python, debemos abrir el fichero mediante la función open(). 
# Esta función admite distintos parámetros, pero los más comunes son:

# file: la ruta del fichero (obligatorio).
# mode: lectura (r), escritura (w) , añadir (a), lectura-escritura (r+),fichero binario(b) y fichero de texto (t).
# encoding: codificación a utiliar en modo texto. Si no especificamos esto, Python utilizará la codificación por defecto, 
            # que podemos averiguar con la llamada a sys.getdefaultencoding().

# Una vez abierto el fichero en modo escritura, podemos escribir mediante la función write(). 
# Finalmente, debemos cerrar el fichero para que los cambios surtan efecto mediante la función close().

f = open("fichero.txt", mode="wt", encoding="utf-8")

f.write("Esto es un mensaje. ")

f.write("Esto es otro mensaje en la misma línea. \n")

f.write("Esto es un mensaje en una nueva línea.")

f.close()


"""Para leer de un fichero utilizamos la función read(). 
En primer lugar, hay que abrir el fichero en modo lectura. 
Después, la función read() puede recibir el número de caracteres a leer, 
dejando el puntero en la última posición leída. Si no pasamos ningún parámetro, se leerá hasta el final del fichero:
"""

f = open("fichero.txt", mode="rt", encoding="utf-8")

#leemos 10 caracteres
texto = f.read(10)
print("Leemos 10 caracteres: "+texto)
print(type(texto))

#leemos los restantes
texto = f.read()
print("\n\nLeemos hasta el final del fichero: "+texto)

f.close()