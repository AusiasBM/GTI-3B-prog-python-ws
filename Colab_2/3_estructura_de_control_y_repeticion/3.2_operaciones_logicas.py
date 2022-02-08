"""
    and --> Devuelve True si ambas expresiones se evalúan a True y False en caso contrario.
    or --> Devuelve True si alguna de las dos expresiones se evalúa a True y False en caso contrario.
    not --> Devulve true si la expresión era falsa, y false en caso conteario.

"""


a = True
b = False
x = 7
y = 0
print(a < b)
print(x >= y)
print(not a)
print(not y)
print(a and b)
print(a or b)

# Se puede utilizar parentesis
x = 6
y = 2

if x % 2 == 0 and (not ( x > 5 )):
  print("entro por if")
else:
  print("entro por else")