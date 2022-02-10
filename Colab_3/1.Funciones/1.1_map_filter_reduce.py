
# Las funciones map, filter y reduce nos ofrecen una programación funcional que nos permiten tener una solución más "elegante" para ciertos problemas.

# ----------------------------------------------------------------------------------------------------------------------------------------
# La función map se encarga de aplicar una función a cada uno de los items de una lista, sin modificar la lista original. En el siguiente ejemplo, convertimos a minúsculas cada item.

def minusculas(s):
  """
  Args: s (string)
  Returns: string
  """
  return s.lower()

#------------main-------------
nombres = ["Pepe", "ana", "juan", "Toni"]
resultado = map(minusculas, nombres)
print(list(resultado)) #convertimos el resultado a una lista


# ----------------------------------------------------------------------------------------------------------------------------------------
# La función filter se encarga de crear una nueva lista con los elementos de una lista original que cumplen una cierta condición 
# (es decir, con los elementos que devuelven True al llamar a una cierta función):

def longitud_mayor_que_3(s):
  """
  Args: s (string)
  Returns: bool
  """
  if len(s) > 3:
    return True
  return False

#------------main-------------
nombres = ["Pepe", "ana", "juan", "Toni"]
resultado = filter(longitud_mayor_que_3, nombres)
print(list(resultado)) 

#Es código sería equivalente:
#def longitud_mayor_que_3(s):
#  return len(s) > 3

# ----------------------------------------------------------------------------------------------------------------------------------------
# La función reduce llama a una función con los dos primeros items de una lista. 
# Esta función devuelve un valor, que se utiliza para llamar de nuevo a la función junto con el tercer item, y así, hasta terminar la secuencia de elementos. 
# Opcionalmente, podemos pasar un parámetro inicial que se enviará a la función en la primera llamada, junto con el primer item de la lista. 
# A continuación tienes un ejemplo de reduce. Fíjate que tenemos que importar una librería.

from functools import reduce

def suma(x, y):
  """
  Args: x (int), y (int)
  Returns: int
  """
  return x + y

#------------main-------------
lista = [2, 5, 7, 3]
print(reduce(suma, lista))

lista = [2, 5, 7, 3]
print(reduce(suma, lista, 0)) #en este caso, pasamos un primer valor inicial

# ----------------------------------------------------------------------------------------------------------------------------------------