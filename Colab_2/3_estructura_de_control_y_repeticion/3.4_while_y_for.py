
# Bucle while, se repite mientras se cumple una condición
i = 0

while i < 5:
  print(i)
  i+=1


# bucle for, lo utilizamos cuandos sabemos cuentas veces queremos que se repita
for i in range(10):
  print(i)

print("Fin")

# También podemos especificar el rango exacto mediante dos números separados por comas
for i in range(1,10):
  print(i)

print("Fin")

# Esto mismo lo podemos hacer escribiendo los valores que queremos iterar
for i in 1, 2, 3, "casa", "coche", 3.14:
  print(i)

print("Fin")