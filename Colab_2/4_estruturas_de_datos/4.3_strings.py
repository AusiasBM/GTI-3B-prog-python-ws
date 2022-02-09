
# Los strings en Python son una estructura de datos similar a otros lenguajes.
# Podemos verlos como una cadena de caracteres: 
# ******************************************************************************************************************
palabra = "hola"

#Mostramos el primer caracter
print(palabra[0])

#Índices negativos (del final hacia adelante, siendo -1 el último)
print("Penúltimo caracter:", palabra[-2])

#Slicing: mostramos los dos primeros caracteres
print(palabra[0:2])
print(palabra[:2])

#Los dos últimos
print(palabra[-2:])


# Anteriormente, también hemos visto cómo hacer un casting de una variable de otro tipo (p.e. int) para poderla concatenar con otro string:
# ******************************************************************************************************************

x = 485
print("El valor es "+str(x))

# Función type(), nos devuelve el tipo de una variable
# ******************************************************************************************************************

x = 485
print(type(x))

x = str(x)
print(type(x))

"""

    Con la función help(str) podemos ver los métodos de la clase str, algunas de las cuáles son las siguientes:
    
    lower(): transforma a minúsculas la cadena pasada como parámetro
    upper(): transforma a mayúsculas la cadena pasada como parámetro
    title(): transforma a mayúscula el carácter inicial de cada palabra
    replace(): busca el patrón (arg2) en arg1 y los substituye por el valor del arg3. Ejemplo: arg1.replace(arg2,arg3)
    format(): reemplaza cada uno de sus argumentos por las marcas {i} incluidas en la cadena.
    len() devuelve la longitud de la que cadena pasada por parámetro
    split(): separa un string por el delimitador que se pasa como parámetro.
    partition(): separa un string en tres partes (antes del separador, el separador mismo y después del separador).

    En el siguiente enlace tienes puedes encontrar más funciones: https://python-reference.readthedocs.io/en/latest/docs/str/

"""

x = "esto es un mensaje"

print("upper:", x.upper())
print("title:", x.title())
print("replace:", x.replace("es","kk"))
print("format:", "La edad de {0} es {1}".format("Pepe", 25))
print("split:", x.split(" "))
print("partition:", x.partition("un")) #devuelve una lista, esto lo veremos más adelante

departure, separator, arrival = "Valencia:Londres".partition(":")
print("otro ejemplo: ",departure, separator, arrival)

# También podemos iterar por los caracteres de un string con la instrucción for. Observa cómo funciona el siguiente código:
# ******************************************************************************************************************

for i in "Hola":
  print(i)

print("Fin")