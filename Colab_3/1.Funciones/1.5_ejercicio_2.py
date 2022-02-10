

# Crea una función llamada word_length que dada una lista de palabras, devuelva una nueva lista con la longitud de cada una siempre y cuando la palabra no sea "el".


palabras = ["Hola", "como", "estamos", "el"]


word_length = [len(p) for p in palabras if p != "el" ]

print(word_length)