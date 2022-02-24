

"""Por defecto, todos los atributos y métodos de una clase son públicos. Si queremos hacerlos privados, 
debemos añadir el doble subrayado delante del nombre (__). 
Observa en el siguiente ejemplo cómo desde fuera de la clase sí que podemos acceder a los atributos 
y métodos públicos pero no podemos acceder a los privados:"""

# Definimos una clase Persona
class Persona:


  def __init__(self, n, e):
    self.nombre = n #público
    self.__edad = e #privado

  def mostrar(self): #público
    print("El nombre es ",self.nombre, " y la edad es ",self.__edad)

  def __mostrar(self): #privado
    print("El nombre es ",self.nombre, " y la edad es ",self.__edad)  

p = Persona("Juan", 25)
print("El nombre es "+p.nombre)
p.mostrar()

#Estos fallan
print("La edad es "+p.__edad)
p.__mostrar()

# También puedes encontrar atributos o métodos que tienen un subrayado simple (_). 
# Esto, por convención, también se utiliza para hacer referencia a que son privados, aunque a nivel práctico, no lo serían.

"""En Python también existen métodos especiales de clases. 
Ya hemos visto __init__ pero también podemos utilizar otros. 
Un ejemplo es __str__ el cual devuelve una cadena con lo que queremos que se muestre por pantalla cuando imprimimos el objeto. 
Observa el siguiente ejemplo y después comenta la función __str__ para comprobar la diferencia:"""

# Definimos una clase Persona
class Persona:

  def __init__(self, n, e):
    self.nombre = n 
    self.edad = e 

  def __str__(self): 
    return "El nombre es "+self.nombre+" y la edad es "+str(self.edad)

p = Persona("Juan", 25)
print("El nombre es "+p.nombre)
print(p)

