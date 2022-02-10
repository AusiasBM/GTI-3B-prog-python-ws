

# Para crear un función en Python debemos utilizar la palabra def seguida del nombre de la función
# El ejemplo siguiente calcula la media de una lista de números pasada como entrada a la función:
# Tras definir el nombre de función, entre paréntesis definimos cuántos parámetros de entrada (separados por comas) tendrá la función y damos un nombre a cada una de estas entradas

def media(lista_numeros): 
    """Calcula la media de una lista
    Args: lista_numeros (list[])
    Returns: float
    """
    suma = 0
    for n in lista_numeros:
        suma = suma + n
    return suma / len(lista_numeros)

# Para llamar a la función, basta con escribir su nombre y pasarle los parámetros de entrada, si es que tiene:

#------------main-------------
num = [1, 5, 3, 2]

resultado = media(num)
print("El resultado es "+str(resultado))


# ----------------------------------------------------------------------------------------------------------------------------------------
# También podemos definir parámetros opcionales, los cuáles, si no se pasan, cogen un valor por defecto

def saludar(nombre = "Pepe"): 
  """
  Args: nombre (default is "Pepe")
  Returns: string
  """
  return "Hola " + nombre

#------------main-------------
res = saludar()
print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------
# En caso de tener varios parámetros, debemos poner los opcionales al final:

def saludar(edad, nombre = "Pepe"): 
  """
  Args: edad (int), nombre (default is "Pepe")
  Returns: string
  """
  return "Hola " + nombre + ", tienes " + str(edad) + " años"

#------------main-------------
res = saludar(25)
print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------
# En Python también es habitual utilizar los kwargs (keyword arguments) para pasar parámetros a las funciones. 
# Esto nos permite cambiar el órden en el que están definidos. Para ello, debemos especificar a qué parámetro corresponde cada valor pasado:

def saludar(edad, nombre): 
  """
  Args: edad (int), nombre (default is "Pepe")
  Returns: string
  """
  return "Hola " + nombre + ", tienes " + str(edad) + " años"

#------------main-------------
res = saludar(nombre="Pepe", edad=25)
print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------
# Vamos a modificar una lista. Observa el siguiente código y sin ejecutarlo, piensa qué mostrará el mensaje:

def ordenar(lista): 
  """
  Args: lista (list[])
  Returns: list[]
  """
  lista.sort()
  lista[2] = 12 
  return lista

#------------main-------------
lista = [5, 2, 7, 4]
print("Después de llamar a la función: ", ordenar(lista), lista)

# Como has podido comprobar, una lista se pasa por referencia, de manera que la función recibe un puntero o dirección de memoria donde está la lista original.

# ----------------------------------------------------------------------------------------------------------------------------------------
# También podemos pasar un número arbitrario de parámetros a una función mediante la palabra *args.
# Observa el siguiente ejemplo cómo la función sirve para mostrar en orden cualquier cantidad de números recibidos:

def ordenar(*args): 
  """
  Args: *args (list[])
  """
  lista = list(args) #creamos una lista con los valores recibidos
  lista.sort()
  print(lista)

#------------main-------------
ordenar(5, 2, 7, 4)
ordenar(7, 2, 8, 6, 3, 1, 5)



