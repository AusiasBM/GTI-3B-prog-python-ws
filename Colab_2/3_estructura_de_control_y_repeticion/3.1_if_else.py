num = 7

if num >= 5:
  print("El número es mayor o igual a 5")
else:
  print("El número es menor que 5")

print("Esta línea se ejecuta siempre")

# if-else anidados  -----------------------------------------

color = "azul"

if color == "rojo":
  print("El color es rojo")
else:
  if color == "azul":
    print("El color es azul")
  else:
    print("El color no es ni rojo ni azul")

print("Esta línea se ejecuta siempre")

# Otra forma de hacer lo mismo que antes

color = "rojo"

if color == "rojo":
  print("El color es rojo")
elif color == "azul":
  print("El color es azul")
else:
  print("El color no es ni rojo ni azul")

print("Esta línea se ejecuta siempre")

