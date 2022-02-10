

# Crea una función llamada without_first_letter que dada una lista de palabras, devuelva una nueva lista con la primera letra de cada palabra eliminada.

palabras = ["Hola", "como", "estas", "tu"]

without_first_letter = map(lambda p : p[1:], palabras)

print(list(without_first_letter))
