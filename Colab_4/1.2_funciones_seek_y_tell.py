

"""La función seek() nos permite mover el puntero a una determinada posición que pasamos por parámetro. 
La función tell() devuelve la posición actual del puntero. En el siguiente ejemplo, 
después de leer 10 caracteres movemos de nuevo el puntero a la posición 0:"""

f = open("fichero.txt", mode="rt", encoding="utf-8")

#leemos 10 caracteres
texto = f.read(10)
print("Leemos 10 caracteres: "+texto)

pos = f.tell()
print("La posición actual del puntero es ", pos)

#movemos el puntero al inicio y volvemos a leer
f.seek(0)
texto = f.read(10)
print("Volvemos a leer: "+texto)

f.close()