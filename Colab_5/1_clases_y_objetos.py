

# Observa el siguiente ejemplo donde definimos una clase persona con dos parámetros adicionales: nombre (n) y edad (e). 
# Estos parámetros los utilizaremos para asignarlos a dos atributos de la clase, llamados nombre y edad:

"""Como has podido comprobar, a diferencia de otros lenguajes, en Python no es necesario hacer explícitos los atributos de la clase, 
sino que son creados en el momento que utilizamos la sintaxis self.atributo. 
Podemos ver la palabra self como el this que utilizamos en otros lenguajes.

De hecho, si definimos un atributo a nivel de clase (igual que hacemos en otros lenguajes como Java o C#), 
estaremos definiendo un atributo de clase, es decir, un atributo que tiene el mismo valor para todos los objetos que se creen:"""

# Definimos una clase Persona
class Persona:
  """ Atributo de clase (mismo valor para todas las personas) """"
  unidad_masa = "kg"

  """ Atributos de instanacia. Cada persona puede tener un nombre y una edad distintos """
  def __init__(self, n, e):
    self.nombre = n
    self.edad = e


"""Para crear un objeto o instancia de una clase, simplemente llamaremos a una función cuyo nombre es el nombre propio de la clase 
y pasando por parámetro aquellos que reciba su función __init__ a excepción del primer parámetro self. Una vez creado el objeto, 
podemos acceder a sus atributos simplemente con un punto:"""

p = Persona("Juan", 25)

print("El nombre de p es ",p.nombre, " y la edad es ",p.edad)

"""De forma similar a los atributos, podemos definir métodos al igual que definimos cualquier función. 
Lo único que tenemos que tener en cuenta es que los métodos de clase tienen que ir identados 
dentro de la clase y que debemos añadir self como primer parámetro. A continuación se muestra 
el ejemplo de uso de un método mostrar_info():"""

# Definimos una clase Persona
class Persona:
  """ Creamos una nueva persona con un nombre y una edad """
  def __init__(self, n, e):
    self.nombre = n
    self.edad = e

  def mostrar(self):
    print("El nombre es ",self.nombre, " y la edad es ",self.edad)

p = Persona("Juan", 25)
p.mostrar()

"""En otros lenguajes, se utiliza Null para hacer referencia a un puntero que no apunta a nada, denotando un objeto o una variable vacía. 
Python utiliza None para definir objetos y variables nulas. Lo podrás ver normalmente en alguna función que no devuelve nada.

En el siguiente ejemplo puedes ver una función que devuelve la cantidad de claves de un diccionario cuyo 
valor coincida con el valor pasado por parámetro. Si no existe ninguna, devuelve None. Observa también como, 
por convenio, utilizamos is y is not para comparar con None en vez de == y !="""

def matching_list(dict, value):
  matchings = []
  for item in dict:
    if dict[item] == value:
      matchings.append(item)

  if len(matchings) != 0:
    return len(matchings)
  else:
    return None
  
res = matching_list(pairs, "moto")
if res is not None:
  print("Se han encontrado "+str(res)+" elementos")
else:
  print("No hay ningún item que coincida")

