

# Escribe una función que reciba dos diccionarios con claves de tipo string y valores de tipo numérico, y que devuelva un nuevo diccionario que contenga los dos anteriores. Muestra el resultado por pantalla.

# Otra forma de hacerlo
def diccionarios(dic1, dic2):
    dic3 = {}
    for i in dic1:
        dic3[i] = dic1[i];
    for i in dic2:
        dic3[i] = dic2[i]; 
    return dic3


# -------------- MAIN --------------

dic1 = { "usuario1": 23, "usuario7": 10, "usuario2" : 4 }
dic2 = {"first": 20, "second": 556, "third": 212, "fourth": 89}

# dic3 = diccionarios(dic1, dic2)

# La forma más rápida y correcta
dic3 = dict(dic1, **dic2)

print(dic3)