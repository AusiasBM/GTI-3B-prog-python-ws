
# Una tupla es igual que una lista, con la única diferencia de que es inmutable. 
# No se puede modificar solo consultar.


tupla = (25, 12, 14, 29)
print(tupla)

#no es lo más habitual omitir paréntesis, pero es lo mismo
tupla = 25, 12, 14, 29
print(tupla)


# Acceder a los valores
valor = tupla[1] + tupla[2]
print(valor)

# La mayoría de métodos que hemos visto para listas, no los podemos utilizar en tuplas. 
# Algunos que sí que puedes utilizar son len(), count() o index(). 
# A continuación, puedes ver cómo se define una tupla y algunas opciones:

print(tupla[0])

print(len(tupla))

print(tupla.count(12))

print(tupla.index(14))

#Esto da error
#tupla[0] = 15

# Para crear una tupla con un único valor tenemos que poner una coma.add()
tupla = (43,)
print(tupla)

# Puesto que una tupla es una secuencia de items separados por comas, 
# podemos usar una tupla cuando queremos que una función devuelva más de un valor con el return. 
# Si estás acostumbrado a lenguajes como Java, C o C#, 
# el siguiente código puede parecerte una muy buena solución para devolver varios valores:

"""
E: float
S: float, float
"""
def area_y_perimetro(base, altura):
  area = base * altura
  perimetro = base * 2 + altura * 2
  return area, perimetro #ojo, devolvemos 2 valores!!

b = 2
a = 3

#observa cómo recuperamos los dos valores
area, perimetro = area_y_perimetro(b,a)
print("El área es "+str(area)+" y el perímetro "+str(perimetro))

