

# Escribe una función que reciba un diccionario de valores numéricos y devuelva el valor mínimo de este diccionario. Muestra el resultado por pantalla.

def dicNumToMin(dic):
    return min(dic.values())


# ----------- MAIN -----------

dic = {"first": 20, "second": 556, "third": 212, "fourth": 89}

print( dicNumToMin(dic) )